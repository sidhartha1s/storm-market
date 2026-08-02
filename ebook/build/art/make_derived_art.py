#!/usr/bin/env python3
"""Derive the storefront and headshot assets from the approved cover plate.

Both outputs come from `cover-v3-raymond.png`, the owner-selected art. Nothing here generates a
new image, which is the point: the art is approved and its byline is correct, and regenerating
for a different aspect ratio would produce a different painting and put unapproved art in front
of buyers.

  headshot.png     A portrait crop of the author for the landing page's author block, which
                   currently fakes it with background-position on the full 2.5 MB cover.
  cover-16x9.png   The storefront image. Gumroad shows product art in a wide frame, so a 2:3
                   cover letterboxed into 16:9 leaves most of the width empty. A first version
                   filled that space with blurred art and nothing else, which at thumbnail size
                   is just a smear. This composes instead: the cover stands at the right, and
                   the left carries the headline and the proof line, which is the only part
                   still legible when Gumroad renders it small.

The wide image is laid out in HTML and captured with headless Chrome rather than drawn in PIL,
because it is typography over an image and that is what a browser is good at.

Usage:
    python3 make_derived_art.py
"""

import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
SRC = HERE / "cover-v3-raymond.png"
FONT = HERE / "PlayfairDisplay.ttf"
LANDING = HERE.parent.parent.parent / "landing" / "assets"
CHROME = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")

# Measured off the 1024x1536 plate: the author occupies the right third, head near the top.
FACE_BOX = (556, 168, 1010, 714)

WIDE = (1920, 1080)

PAGE = """<!doctype html>
<meta charset="utf-8">
<style>
  @font-face {{ font-family: Playfair; src: url("{font}"); }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: {w}px; height: {h}px; overflow: hidden; background: #05070a; }}
  .field {{
    position: absolute; inset: -8%;
    background: url("{art}") center 28% / cover no-repeat;
    filter: blur(34px) saturate(1.1); transform: scale(1.15);
  }}
  .veil {{
    position: absolute; inset: 0;
    background: linear-gradient(100deg, rgba(5,7,10,.94) 0%, rgba(5,7,10,.88) 46%,
                                        rgba(5,7,10,.55) 72%, rgba(5,7,10,.35) 100%);
  }}
  .row {{ position: absolute; inset: 0; display: flex; align-items: center; gap: 70px;
          padding: 0 96px; }}
  .copy {{ flex: 1 1 auto; max-width: 940px; }}
  .kicker {{
    font-family: Playfair, Georgia, serif; font-size: 21px; font-weight: 600;
    letter-spacing: .34em; text-transform: uppercase; color: #e8a33a; margin-bottom: 30px;
  }}
  h1 {{
    font-family: Playfair, Georgia, serif; font-size: 104px; line-height: .98;
    color: #f4efe6; font-weight: 600; letter-spacing: -.01em;
  }}
  .sub {{
    font-family: Playfair, Georgia, serif; font-size: 33px; line-height: 1.36;
    color: #cdc6bb; margin-top: 30px; max-width: 820px;
  }}
  .rule {{ width: 190px; height: 2px; background: #b06b06; margin: 40px 0 26px; }}
  .proof {{
    font-family: Playfair, Georgia, serif; font-size: 25px; letter-spacing: .13em;
    text-transform: uppercase; color: #9a9188;
  }}
  .byline {{
    font-family: Playfair, Georgia, serif; font-size: 25px; letter-spacing: .2em;
    text-transform: uppercase; color: #f4efe6; margin-top: 34px;
  }}
  .plate {{
    flex: 0 0 auto; height: 900px; border-radius: 3px;
    box-shadow: 0 26px 70px rgba(0,0,0,.75);
  }}
</style>
<div class="field"></div><div class="veil"></div>
<div class="row">
  <div class="copy">
    <p class="kicker">Storm Market Field Manual</p>
    <h1>The<br>Storm-Ready<br>Home</h1>
    <p class="sub">What the survivors did differently &mdash; and the 130 things
      you can do before the next one.</p>
    <div class="rule"></div>
    <p class="proof">130 protections &middot; 23 hazards &middot; 60 days &middot; 5 regions</p>
    <p class="byline">Paul Raymond</p>
  </div>
  <img class="plate" src="{art}">
</div>
"""


def headshot(cover):
    """A 5:6 portrait of the author, at 2x the landing page's 250x300 block."""
    return cover.crop(FACE_BOX).resize((500, 600), Image.LANCZOS)


def storefront():
    """Lay the wide image out in HTML and capture it at exactly 1920x1080."""
    if not CHROME.exists():
        sys.exit(f"FAIL: Chrome not found at {CHROME}; cannot capture the storefront image.")
    page = HERE / "cover-16x9.html"
    page.write_text(
        PAGE.format(w=WIDE[0], h=WIDE[1], art=SRC.resolve().as_uri(),
                    font=FONT.resolve().as_uri()),
        encoding="utf-8")
    out = (HERE / "cover-16x9.png").resolve()
    subprocess.run(
        [str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
         f"--window-size={WIDE[0]},{WIDE[1]}", f"--screenshot={out}",
         page.resolve().as_uri()],
        capture_output=True, check=True, timeout=180)
    if not out.exists():
        sys.exit("FAIL: Chrome produced no storefront image.")
    return out


def main():
    if not SRC.exists():
        sys.exit(f"FAIL: {SRC} is missing. Run rename_byline.py first.")
    cover = Image.open(SRC).convert("RGB")

    wide = storefront()
    size = Image.open(wide).size
    print(f"wrote {wide}  {size[0]}x{size[1]}")
    if size != WIDE:
        sys.exit(f"FAIL: storefront image is {size}, expected {WIDE}.")

    face = headshot(cover)
    for target in (HERE / "headshot.png", LANDING / "headshot.png"):
        target.parent.mkdir(parents=True, exist_ok=True)
        face.save(target)
        print(f"wrote {target}  {face.size[0]}x{face.size[1]}")


if __name__ == "__main__":
    main()
