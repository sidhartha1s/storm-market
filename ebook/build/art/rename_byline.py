#!/usr/bin/env python3
"""Repaint the baked-in byline on generated cover art, without regenerating the art.

The covers had their typography rendered by the image model, so the byline is pixels, not
text. When the pen name changed from Paul Reynolds to Paul Raymond the art was already
owner-approved, and re-running the generator would have produced different art for a
surname change. So this repaints only the byline strip on each plate.

Nothing is hardcoded to one image: for each plate the script measures the byline off the
pixels — locates the lowest line of bright text, reads its cap height, left edge, glyph
pitch and word gap — then erases that strip by refilling it from the flat background either
side and redraws the new name in Playfair Display at the measured metrics. The text is drawn
at 4x and downsampled so its antialiasing matches the surrounding art instead of looking
pasted on.

Usage:
    python3 rename_byline.py                 # repaint every plate in PLATES
    python3 rename_byline.py --check         # measure and report, write nothing

Always eyeball the output at 100% and zoomed. These are sales assets, and a byline that
reads as retouched is worse than one that reads as typeset.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
FONT = HERE / "PlayfairDisplay.ttf"

NAME = "PAUL RAYMOND"

# source plate -> output. The v2 plate keeps the original byline as the reference original.
PLATES = {
    "cover-v2-paul.png": "cover-v3-raymond.png",
    "cover-1x1.png": "cover-1x1-raymond.png",
    "cover-2x3-minimal.png": "cover-2x3-minimal-raymond.png",
    "cover-us-typed.png": "cover-us-typed-raymond.png",
}

INK_MIN = 120        # a pixel counts as glyph ink above this in red
MARGIN = 10          # px of clearance repainted around the measured glyph box
SCALE = 4            # supersample factor for the text layer
WEIGHT = 600         # Playfair wght axis, matched to the generator's stroke contrast


def is_ink(px, x, y):
    r, g = px[x, y][0], px[x, y][1]
    return r > INK_MIN and g > INK_MIN - 5


def measure(im):
    """Find the lowest line of bright text and read its typographic metrics off the pixels."""
    px = im.load()
    width, height = im.size

    # Row bands of text in the bottom third, which is where every plate puts its byline.
    bands, run = [], None
    for y in range(height * 2 // 3, height):
        has_ink = sum(1 for x in range(width) if is_ink(px, x, y)) > 3
        if has_ink and run is None:
            run = y
        elif not has_ink and run is not None:
            if y - run >= 8:          # ignore single-pixel noise and hairline rules
                bands.append((run, y - 1))
            run = None
    if run is not None and height - run >= 8:
        bands.append((run, height - 1))
    if not bands:
        raise SystemExit("FAIL: no text band found in the lower third.")
    top, bottom = bands[-1]

    # Glyph columns within that band.
    glyphs, start = [], None
    for x in range(width):
        has_ink = any(is_ink(px, x, y) for y in range(top, bottom + 1))
        if has_ink and start is None:
            start = x
        elif not has_ink and start is not None:
            glyphs.append((start, x - 1))
            start = None
    if start is not None:
        glyphs.append((start, width - 1))
    if len(glyphs) < 4:
        raise SystemExit(f"FAIL: only {len(glyphs)} glyphs in the byline band.")

    gaps = sorted(glyphs[i + 1][0] - glyphs[i][1] - 1 for i in range(len(glyphs) - 1))
    return {
        "top": top, "bottom": bottom,
        "cap_height": bottom - top + 1,
        "left": glyphs[0][0], "right": glyphs[-1][1],
        "tracking": gaps[len(gaps) // 2],   # median gap is the letter pitch
        "word_gap": gaps[-1],               # the one wide gap is the space
    }


def load_font(cap_height):
    """Largest size whose downsampled cap height matches the measured original."""
    probe = ImageDraw.Draw(Image.new("L", (10, 10)))
    # Downsampling from SCALE spreads ink about a pixel, so aim just under the target.
    target = cap_height * SCALE - 4
    for size in range(cap_height, cap_height * SCALE * 3):
        font = ImageFont.truetype(str(FONT), size)
        font.set_variation_by_axes([WEIGHT])
        box = probe.textbbox((0, 0), "P", font=font)
        if box[3] - box[1] >= target:
            return font
    raise SystemExit("FAIL: could not reach the measured cap height with this font.")


def ink_colour(im, m):
    """The brightest glyph pixels in the original byline, so the new name matches its tone."""
    px = im.load()
    pixels = [px[x, y][:3]
              for y in range(m["top"], m["bottom"] + 1)
              for x in range(m["left"], m["right"] + 1)
              if is_ink(px, x, y)]
    pixels.sort(key=sum)
    bright = pixels[int(len(pixels) * 0.9):]
    return tuple(sum(channel) // len(bright) for channel in zip(*bright))


def erase(im, m):
    """Refill the byline strip from each row's own background, sampled outside the glyphs."""
    px = im.load()
    width = im.size[0]
    right = min(width, m["right"] + MARGIN)
    # Sample the widest glyph-free stretch to the right of the byline; fall back to the left.
    sample_from = range(right + 20, width) if width - right > 60 else range(0, m["left"] - 20)
    for y in range(max(0, m["top"] - MARGIN), min(im.size[1], m["bottom"] + MARGIN)):
        row = sorted(px[x, y][:3] for x in sample_from)
        colour = row[len(row) // 2]
        for x in range(max(0, m["left"] - MARGIN), right):
            px[x, y] = colour + (255,)


def draw_name(im, m, font, ink):
    layer = Image.new("RGBA", (im.width * SCALE, im.height * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x = m["left"] * SCALE
    baseline = (m["bottom"] + 1) * SCALE
    for char in NAME:
        if char == " ":
            # word_gap is ink-to-ink; the per-glyph advance already adds tracking.
            x += (m["word_gap"] - m["tracking"]) * SCALE
            continue
        draw.text((x, baseline), char, font=font, fill=ink + (255,), anchor="ls")
        x = draw.textbbox((x, baseline), char, font=font, anchor="ls")[2] + m["tracking"] * SCALE
    layer = layer.resize(im.size, Image.LANCZOS)

    # A soft one-pixel drop shadow, matching the bevel the generator gave the original glyphs.
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    shadow.putalpha(layer.split()[3].point(lambda v: int(v * 0.55)))
    im.alpha_composite(shadow, (1, 1))
    im.alpha_composite(layer)
    return int(x / SCALE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="measure and report the byline metrics, write nothing")
    args = parser.parse_args()

    for src_name, dst_name in PLATES.items():
        src = HERE / src_name
        if not src.exists():
            print(f"skip {src_name}: not present")
            continue
        im = Image.open(src).convert("RGBA")
        m = measure(im)
        print(f"{src_name}: byline y {m['top']}..{m['bottom']} cap {m['cap_height']}px "
              f"x {m['left']}..{m['right']} tracking {m['tracking']} word gap {m['word_gap']}")
        if args.check:
            continue
        ink = ink_colour(im, m)
        erase(im, m)
        right = draw_name(im, m, load_font(m["cap_height"]), ink)
        im.convert("RGB").save(HERE / dst_name)
        print(f"  wrote {dst_name}  ink {ink}  new byline ends x {right} "
              f"(original ended {m['right']})")


if __name__ == "__main__":
    main()
