# Cover art

| File | Role |
|---|---|
| `cover-v3-raymond.png` | **The cover, as shipped.** Owner-selected art with the byline repainted to Paul Raymond, 2026-07-29. 1024×1536, 2:3. |
| `cover-v2-paul.png` | The same art with the original **Paul Reynolds** byline. Kept as the source plate `rename_byline.py` reads. |
| `rename_byline.py` | Repaints the byline strip on the selected art. Run it if the pen name changes again — it does not regenerate the art. |
| `PlayfairDisplay.ttf` | The byline face (OFL). Pinned locally so the repaint is reproducible offline. |
| `ref-yoder-cover.png` | Reference only — the Yoder cover. Internal design reference, never reproduced. |
| `cover-us-typed.png` | Superseded. US hazard-map with baked type. |
| `cover-us-clean.png` | Superseded. Clean hazard-map plate. |
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
