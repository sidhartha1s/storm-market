# g-a5-2-toll · A5-S2 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `library/inhouse/numbers-rollup.html` (count-up on a leaf); chip as `compositions/g-intro-3-sept8.html`.

## 0. Claim
Cline's own report said 6,000 and called it conservative; today 8,000 is the figure most cited, inside a 6,000 to 12,000 range.

## 1. Source
- Cline, MWR Sept 1900: "conservative estimates place the loss of life at the appalling figure, 6,000" (fact-check a5-r1 rows 7 to 9).
- NHC https://www.nhc.noaa.gov/outreach/history/: "the 8,000 deaths (estimates range from 6,000 to 12,000)" (sources-cline.md §5; fact-check a5-r1 row 10). "Most cited": Wikipedia 1900 hurricane lead (row 11, SECONDARY).

## 2. Datum, scale, orientation
Overlay comp over the MWR report page; the push to the toll sentence is the orchestrator's footage move and ends with the sentence in the left half (x < 1000). The chips stack in a right column. No scale (the chips are not a bar chart: no lengths encode numbers).

## 3. Geometry (px)
- Right column, glass chips, left edge x 1080, width 640 (fixed), each chip 128 px tall, gap 20:
  - C1 top 200: main "6,000" Arial Black 900 64 px `#f2f5f8`, tag "CLINE'S REPORT" Arial 700 22 px `#93a3b2` tracking 4.
  - C2 top 348: main "8,000", tag "MOST CITED".
  - C3 top 496: main "6,000 TO 12,000", tag "RANGE".
- Column bottom = 624 < 680: clear of the presenter corner.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900 · National Hurricane Center".
- Three tiers: 64 (big), 44 not used, 22 (small) + source 19: add mid tier by setting C3 main at 44 px (it is a range, read as secondary). Declare nothing.

## 4. Must be true in the picture
1. C1 reads exactly "6,000" with "CLINE'S REPORT": never "AT LEAST" (fact-check row 9).
2. C2 and C3 never show before "National Hurricane Center" is spoken; C1 never shows before "6 ,000".
3. The stack order top to bottom is 6,000 / 8,000 / range, all three visible together from 7.76 to the exit.
4. No chip covers the toll sentence on the page (sentence box x < 1000 at the end of the push; if not, the orchestrator moves the push, not the chips).
5. Dup-fact: "6,000" and "6,000 TO 12,000" are different strings; no other leaf repeats them.

## 5. Text and cues (a5-s2.words.json, segment 12.20 s)
- 0.00: source line in (the page is on from the cut).
- 2.24 ("6" 2.24) /* 6000 @2.24 */: C1 in; figure counts 1,000 to 6,000, 2.24 to 2.90, power3.out.
- 4.34 ("conservative." 4.34): C1 tag brightens to `#d8a13a` for 0.6 s then back.
- 7.48 ("8" 7.48) /* 8000 @7.48 */: C2 in, counts 6,000 to 8,000, 7.48 to 8.00.
- 7.76 (",000." 7.76): C3 in 0.3 s after C2 lands (8.05), no count.
- 8.78 ("Klein" 8.78): all three dim to 0.6; loop line "Which one holds?" carries itself (no text).
- Host: A5-S2 0.00 to 12.20 + 0.6.

## Motion for the whole window
Chips drift (y ±4, 2.4 s yoyo, phase-offset 0.4 s each). The page push under it runs the whole segment.

## Exit
11.44 ("Which"): chips slide out right in order C3, C2, C1, 0.1 s apart, `x:980, autoAlpha 0, 0.6 s power3.in`, done by 12.4.

## Footage under it
MWR Sept 1900 report page with the toll sentence (open item 6), whole lines only.
