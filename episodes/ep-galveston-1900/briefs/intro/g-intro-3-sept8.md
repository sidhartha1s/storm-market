# g-intro-3-sept8 · H1-S3 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (popfig, then glass card, one after the other).

## 0. Claim
The storm struck Galveston on Saturday, September 8, 1900, and at least 6,000 people died there, by Cline's own count.

## 1. Source
- Date: sources-cuba.md §4, AOML "On the evening of September 8, 1900, a major hurricane struck Galveston, Texas"; Saturday verified, factcheck intro-r2 rows 7 to 9.
- Toll: sources-cline.md §3, Cline's report "at least 6,000 people were killed in a few hours' time"; NOAA Heritage "at least 6,000" (factcheck intro-r2). Range on record 6,000 to 12,000 (sources-cline.md §5); this chip states only Cline's floor and says so.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over the Library of Congress ruins photograph (track 1, still with a slow push). Zones: centre popfig, then centre chip (same zone, strictly one after the other), source line top-left.

## 3. Geometry (px)
- Popfig: cards.css `.popfig` centred, `top:38%`. Big line "SEPT 8, 1900" (12 characters) Abril 150 px `#d0121f`; sub line "SATURDAY" Arial 700 32 px under it.
- Chip, centred at `top:560px` (`xPercent:-50` set at 0): main "AT LEAST 6,000 LIVES" Arial Black 900 52 px; tag "Cline's own count" Arial 700 22 px `#93a3b2` tracking 4. Card about 760 x 150 px.
- The figure "6,000" in the chip counts up: leaf span, `to({v})` from 1,000 to 6,000, power3.out, 0.9 s, formatted with a comma, opening on "1,000" at the first tick. "AT LEAST" and "LIVES" are separate static spans either side.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900 · NOAA".

## 4. Must be true in the picture
1. The popfig is fully gone (autoAlpha 0) before the chip starts its entrance; never both.
2. "AT LEAST" is on screen from the chip's first frame; the count never shows a bare number without it.
3. The count lands on exactly 6,000 and never passes it.
4. Nothing in x >= 1600, y >= 680.
5. Claim check on the picture (mg-quickref 7a item 7): the popfig names a date. The ruins photo was made after the storm (Broadway film copyright 24 Sep 1900; the wharf photo's LoC card says c1900 Oct 15). The orchestrator decides whether a date popfig over aftermath footage is acceptable as "the storm's date"; if not, the popfig moves onto a still that is the storm itself (none exists) or the sub line becomes "THE STORM · SATURDAY". Builder: build as specified; the decision is upstream.

## 5. Text and cues (h1-s3.words.json, segment 8.071 s)
- Source line in at 0.00.
- Popfig sub "SATURDAY" and big line in at 1.38 ("Saturday" 1.38) /* SATURDAY @1.38 */; big line slams 0.12 s after the sub.
- Popfig out 4.50 to 4.95 ("Galveston" 4.50, the landfall word lands first, then the date clears).
- Chip in at 5.48 ("At" 5.48) /* AT LEAST @5.48 */, count runs 5.78 to 6.68 ("6" 5.78, ",000" 6.12).
- Tag "Cline's own count" fades up at 7.00 ("lost" 7.00).
- Host 0.00 to 8.07; chip exit anchored to the last 0.6 s (7.47 to 8.07).

## Motion for the whole window
1.38 to 8.07 always has a mover (popfig drift, then count, then chip drift). 0.00 to 1.38 has only the source line: its drift covers it (gap under 4 s).

## Exit
Chip slides out `x:980, autoAlpha 0, 0.6, power3.in` ending 8.07 (the hard cut to H1-S4's map follows).

## Footage under it
Library of Congress ruins photograph of Galveston, September 1900 (footage-inventory.md: loc.gov blocked; a Commons LoC copy, e.g. `Galveston_Disaster,_Texas,_body_in_the_ruins_on_wharf.jpg`, or another verified PD ruins still). The orchestrator names the exact file and its provenance row before the frame read.
