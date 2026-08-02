#!/usr/bin/env python3
"""Derive the storefront and headshot assets from the approved cover plate.

Both outputs are crops and compositions of `cover-v3-raymond.png`, the owner-selected art.
Nothing here generates a new image, which is the point: the art is approved, the byline on it
is correct, and regenerating for a different aspect ratio would produce a different painting
and put an unapproved asset in front of buyers.

  headshot.png    A portrait crop of the author for the landing page's author block. The page
                  currently fakes this with background-position on the full cover, which works
                  but reuses a 2.5 MB plate to show a face.
  cover-16x9.png  The storefront image. Gumroad shows product art in a wide frame, and a 2:3
                  book cover letterboxed into 16:9 wastes most of the width. So this composes
                  rather than crops: the cover stands at the right, the art's own sky is blurred
                  out behind it, and the title and proof line get the space they need to stay
                  legible at thumbnail size.

Usage:
    python3 make_derived_art.py
"""

from pathlib import Path

from PIL import Image, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "cover-v3-raymond.png"
LANDING = HERE.parent.parent.parent / "landing" / "assets"

# Measured off the 1024x1536 plate: the author occupies the right third, head near the top.
FACE_BOX = (556, 168, 1010, 714)

WIDE = (1920, 1080)


def headshot(cover):
    """A 5:6 portrait of the author, sized for the landing page's 250x300 block at 2x."""
    crop = cover.crop(FACE_BOX)
    return crop.resize((500, 600), Image.LANCZOS)


def storefront(cover):
    """A 16:9 composition: blurred art as the field, the cover standing proud of it."""
    canvas = Image.new("RGB", WIDE, (5, 7, 10))

    # Background: the plate blown up past the frame and blurred, so the wide field carries the
    # cover's own colour instead of a flat block.
    scale = WIDE[0] / cover.width * 1.25
    field = cover.resize((int(cover.width * scale), int(cover.height * scale)), Image.LANCZOS)
    field = field.filter(ImageFilter.GaussianBlur(28))
    left = (field.width - WIDE[0]) // 2
    top = int(field.height * 0.24)
    canvas.paste(field.crop((left, top, left + WIDE[0], top + WIDE[1])), (0, 0))

    # Darken the field so the cover in front of it reads as the subject.
    canvas = Image.blend(canvas, Image.new("RGB", WIDE, (5, 7, 10)), 0.45)

    # The cover itself, full height less a margin, on the right.
    height = 900
    width = int(cover.width * height / cover.height)
    plate = cover.resize((width, height), Image.LANCZOS)
    x = WIDE[0] - width - 150
    y = (WIDE[1] - height) // 2

    # A soft drop shadow so the plate sits on the field rather than floating on it.
    shadow = Image.new("RGBA", (width + 60, height + 60), (0, 0, 0, 0))
    shadow.paste((0, 0, 0, 190), (30, 30, width + 30, height + 30))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    canvas.paste(shadow, (x - 30, y - 22), shadow)
    canvas.paste(plate, (x, y))
    return canvas


def main():
    if not SRC.exists():
        raise SystemExit(f"FAIL: {SRC} is missing. Run rename_byline.py first.")
    cover = Image.open(SRC).convert("RGB")

    wide = storefront(cover)
    wide_path = HERE / "cover-16x9.png"
    wide.save(wide_path)
    print(f"wrote {wide_path}  {wide.size[0]}x{wide.size[1]}")

    face = headshot(cover)
    for target in (HERE / "headshot.png", LANDING / "headshot.png"):
        target.parent.mkdir(parents=True, exist_ok=True)
        face.save(target)
        print(f"wrote {target}  {face.size[0]}x{face.size[1]}")


if __name__ == "__main__":
    main()
