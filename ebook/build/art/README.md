# Cover art

| File | Role |
|---|---|
| `cover-v3-raymond.png` | **The cover, as shipped.** Owner-selected art with the byline repainted to Paul Raymond, 2026-07-29. 1024×1536, 2:3. |
| `cover-v2-paul.png` | The same art with the original **Paul Reynolds** byline. Kept as the source plate `rename_byline.py` reads. |
| `rename_byline.py` | Repaints the byline strip on every plate that has one. Run it if the pen name changes again — it does not regenerate the art. `--check` reports the measured metrics without writing. |
| `PlayfairDisplay.ttf` | The byline face (OFL). Pinned locally so the repaint is reproducible offline. |
| `ref-yoder-cover.png` | Reference only — the Yoder cover. Internal design reference, never reproduced. |
| `cover-1x1-raymond.png` | **1:1 crop of the shipped cover.** Gumroad product image and social card. Byline repainted. |
| `cover-2x3-minimal-raymond.png` | 2:3 minimal-type variant, byline repainted. Not shipped; kept as an alternative. |
| `cover-us-typed-raymond.png` | Superseded hazard-map plate with baked type, byline repainted so no asset in the tree carries the old name. |
| `cover-1x1.png`, `cover-2x3-minimal.png`, `cover-us-typed.png` | The same three plates with the original **Paul Reynolds** byline. Source plates for `rename_byline.py`. |
| `cover-us-clean.png` | Superseded. Clean hazard-map plate, no type — nothing to repaint. |
| `COVER-PROMPTS.md` | Prompts, verbatim. |
| `../cover-final.html` | HTML-type-over-plate path. Kept as the editable fallback mechanism. |

## Decision history

**2026-07-27 — owner selected the portrait cover (`cover-v2-paul.png`).** Superseded the hazard-map
direction.

**Correction on the record:** the agent argued against putting a face on the cover, asserting that
Yoder keeps his face on the landing page and off the book. That was wrong — it was inferred from
the landing page markup, which never contained the cover image. **The Yoder cover is dominated by
his portrait.** See `ref-yoder-cover.png`.

## What the Yoder cover actually does — the mechanics to match

Studied from `ref-yoder-cover.png`:

1. **The dollar outcome is the largest type on the cover — larger than the title itself.**
   "SAVE $6,000 A YEAR" dominates; "The Amish Home Savings Manual" is secondary. The cover sells
   the result, not the book.
2. **Portrait, arms crossed, direct eye contact.** Authority of the practitioner, not of a brand.
3. **Byline at the very top**, above everything: "ELIAS & ESTHER YODER · VOLUME I".
4. **Edition and provenance signals:** "Second Edition · MMXXVI", "LANCASTER COUNTY · EDITION 2026".
   These imply a serious, maintained, serialized work.
5. **Bottom band listing the domains covered:** HEAT · WATER · POWER · PANTRY · GARDEN · PESTS ·
   KITCHEN. Same job as our counts line, but concrete subjects rather than counts.
6. **Framed border with gold rules** on a deep single-colour ground. Reads as a manual, not a novel.
7. A short italic promise line: "Simple systems that help a household keep more money."

**Our cover currently has 1, 4, 5 and 6 missing.** The title is the dominant type instead of the
outcome. That is the gap to close in v3 — see the open items below.

**2026-07-29 — byline changed to Paul Raymond, art untouched.** The generator baked the byline into
the pixels, so a name change would normally mean regenerating and losing owner-approved art. Instead
`rename_byline.py` repaints only the byline strip: it refills those 36 rows from the flat background
either side, then redraws the name in Playfair Display at the metrics measured off the original
glyphs (cap height 21px, baseline y=1491, left edge x=65, glyph pitch = ink width + 8px). Verified by
eye at 100% and at 7x against the original. Shipped file is now `cover-v3-raymond.png`.

**The script measures rather than assumes.** It finds the lowest line of bright text on each plate
and reads its cap height, left edge, glyph pitch, word gap and ink colour off the pixels, so the
same run handled four plates with three different type sizes without per-file constants:

| Plate | Byline cap height | Tracking | Word gap |
|---|---|---|---|
| `cover-v2-paul.png` | 21px | 10px | 25px |
| `cover-1x1.png` | 26px | 21px | 50px |
| `cover-2x3-minimal.png` | 26px | 18px | 39px |
| `cover-us-typed.png` | 21px | 9px | 24px |

All four outputs were eyeballed before/after. **No asset in the tree still displays the old name**
except the four source plates, which are kept deliberately as the script's input and are referenced
by nothing.

## FINAL — owner locked `cover-v2-paul.png` as shipped, 2026-07-27

A v3 was specced (Prompt 3 in `COVER-PROMPTS.md`) to add the Yoder mechanics. **Owner declined it
and kept v2 as-is.** Prompt 3 stays on file in case it is ever wanted; it is not pending work.

Closed by that decision, recorded so nobody reopens them:

- **Title stays the dominant type**, rather than a benefit headline above it. Diverges from Yoder,
  who leads with "SAVE $6,000 A YEAR". Owner's call.
- **No framed border, edition line, VOLUME I, or bottom hazard band.**
- **Portrait stays as generated** — reads closer to a fashion model than to Yoder's practitioner.
- Headline "WHAT THE SURVIVORS DID DIFFERENTLY" stays where it is, as the subtitle.

## Still true, and unaffected by the cover choice

- **1024×1536 is a screen asset** — ~113 dpi at 6×9. Fine for a PDF read on a screen; short of the
  1800×2700 needed for print or Amazon KDP. Regenerate larger or upscale if print ever matters.
- If the title, the byline, or the protection count ever changes, the baked text goes stale. Either
  re-run the prompt with new strings or fall back to `../cover-final.html`, which sets type in HTML.

## Standing constraints

- No agency logo, seal, or official styling anywhere — required by the legal section of the design
  spec. Nothing may imply US government endorsement.
- The cover art is not a data product and must never be presented as one.
