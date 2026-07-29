#!/usr/bin/env python3
"""Replace the baked-in byline on the selected cover art without regenerating the art.

The owner-selected cover (`cover-v2-paul.png`) had its typography rendered by the image
model, so the byline is pixels, not text. The name changed from Paul Reynolds to Paul
Raymond after that art was approved. Re-running the generator would produce different art
and lose an approved asset, so instead this script repaints only the byline strip:

  1. The strip is flat near-black (sampled at (1, 6, 11)), so the old glyphs are erased by
     refilling each row with that row's own background colour sampled from the empty right
     half of the same row. Nothing outside the strip is touched.
  2. The new name is drawn in Playfair Display, matched to the original by measurement:
     cap height 21px, baseline y=1491, left edge x=65, and a per-glyph advance of
     glyph width + 9px, which is the letter pitch measured off the original glyph runs.
  3. Text is drawn at 4x and downsampled so the antialiasing matches the surrounding art
     rather than looking like a screenshot pasted on top.

Verify by eye after running — this is the primary sales asset, and a byline that reads as
retouched is worse than one that reads as typeset.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "cover-v2-paul.png"
DST = HERE / "cover-v3-raymond.png"
FONT = HERE / "PlayfairDisplay.ttf"

NAME = "PAUL RAYMOND"

# Measured off the original glyph runs in cover-v2-paul.png.
STRIP = (55, 1463, 430, 1499)   # region to repaint, glyph-free margin included
LEFT = 65                        # left edge of the first glyph
BASELINE = 1491                  # glyph baseline
CAP_HEIGHT = 21                  # 'P' cap height in px
TRACKING = 8                     # gap between glyph ink, in px
WORD_GAP = 14                    # extra advance across the space, tuned to the measured 25px ink gap
INK = (240, 235, 224)
SCALE = 4                        # supersample factor for the text layer


def load_font():
    """Playfair Display at the weight that matches the original's stroke contrast."""
    draw = ImageDraw.Draw(Image.new("L", (10, 10)))
    # Target slightly under the measured cap height: downsampling from SCALE spreads the ink
    # by about a pixel, so aiming at exactly 21px lands at 22 in the finished image.
    target = CAP_HEIGHT * SCALE - 4
    for size in range(CAP_HEIGHT, CAP_HEIGHT * SCALE * 3):
        font = ImageFont.truetype(str(FONT), size)
        font.set_variation_by_axes([600])
        box = draw.textbbox((0, 0), "P", font=font)
        if box[3] - box[1] >= target:
            return font
    raise SystemExit("FAIL: could not reach the measured cap height with this font.")


def erase_old_byline(im):
    """Refill the byline strip from each row's own background, sampled to its right."""
    px = im.load()
    x0, y0, x1, y1 = STRIP
    for y in range(y0, y1):
        sample = sorted(px[x, y] for x in range(600, 1000))
        colour = sample[len(sample) // 2]
        for x in range(x0, x1):
            px[x, y] = colour


def draw_name(im, font):
    layer = Image.new("RGBA", (im.width * SCALE, im.height * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x = LEFT * SCALE
    for char in NAME:
        if char == " ":
            x += WORD_GAP * SCALE
            continue
        draw.text((x, BASELINE * SCALE), char, font=font, fill=INK + (255,), anchor="ls")
        box = draw.textbbox((x, BASELINE * SCALE), char, font=font, anchor="ls")
        x = box[2] + TRACKING * SCALE
    layer = layer.resize(im.size, Image.LANCZOS)

    # A soft 1px drop shadow, matching the bevel the generator gave the original glyphs.
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    alpha = layer.split()[3].point(lambda v: int(v * 0.55))
    shadow.putalpha(alpha)
    im.alpha_composite(shadow, (1, 1))
    im.alpha_composite(layer)
    return int(x / SCALE)


def main():
    im = Image.open(SRC).convert("RGBA")
    erase_old_byline(im)
    right = draw_name(im, load_font())
    im.convert("RGB").save(DST)
    print(f"wrote {DST}")
    print(f"byline spans x {LEFT}..{right} (original ended at 394)")


if __name__ == "__main__":
    main()
