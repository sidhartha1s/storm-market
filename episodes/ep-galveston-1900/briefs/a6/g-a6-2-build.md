# g-a6-2-build · A6-S2 0.94 to 9.98 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass chip over a still).

## 0. Claim
The first section of the seawall went up from 1902 to 1904 and ran 3.3 miles.

## 1. Source
- Rosenberg Library (sources-a6.md §2): "Building of the initial segment commenced in September 1902"; "When completed, this first section was 3.3 miles long".
- ASCE (sources-a6.md §2): "Built between 1902 and 1904"; contract for "a 17,593-foot seawall" (= 3.33 mi).

## 2. Datum, scale, orientation
None: overlay comp on a photograph, transparent root.

## 3. Geometry (px)
- Chip C1 "SEPT 1902": glass chip, one line Arial Black 900 44 px, left edge x 120, top 150.
- Chip C2: glass chip, main line "3.3 MILES" Arial Black 900 56 px `#f2f5f8`, tag line "1902 TO 1904" Arial 700 24 px `#93a3b2` tracking 4; left edge x 120, top 150 (C1's place after C1 leaves).
- Length rule inside C2 under the tag: 4 px `#d8a13a` bar, 420 px wide, `scaleX 0 -> 1`, `transformOrigin:"left center"` (the wall being laid; no scale claim, no label).
- Source line top-left `left:96px; top:54px`, one line, ends above y 100: "Rosenberg Library · American Society of Civil Engineers".

## 4. Must be true in the picture
1. 3.3 MILES and 1902 TO 1904 only: TSHA's "six-mile" figure is a conflict and never shows.
2. The photograph under the chips is the 1902 to 1904 construction by its `provenance.csv` row (template 7a item 7: a chip with a date is a claim about the picture). Stock or a later section fails.
3. One chip at a time; C1 is fully gone before C2 enters.

## 5. Text and cues (a6-s2.words.json, 16.094 s; host starts at 0.94 "wall.")
Comp-local = word time − 0.94.
- 0.94: source line in.
- 2.52 ("September") /* SEPT 1902 @2.52 */: C1 in.
- 4.48 ("By"): C1 out (slide right, 0.6 s).
- 6.18 ("3" 6.18) /* 3.3 MILES @6.18 */: C2 in; tag at 6.52; rule grows 6.52 to 7.70, power2.out.
- 9.38: C2 out (slide right, 0.6 s), done by 9.98.
- Host: 0.94 to 9.98; g-a6-3 cuts in at "It" 9.98.

## Motion for the whole window
The photograph on the footage track pushes scale 1.00 to 1.06 `ease:none` (orchestrator's mount); chips float per shared rules; the rule grows.

## Exit
C2 slides out right in the last 0.6 s.

## Footage under it
A 1902 to 1904 construction photograph: NONE ON DISK (A6-S2 c1 and c2 are 2.2 KB error pages, picks.md). Retry the three Wikimedia rows (LCCN construction site, 1902 concrete seawall, "Building the Sea Wall"). If nothing clears, drop this comp and run g-a6-3 from 0.94 with C1 and C2 moved inside it (g-a6-3 "Fallback").
