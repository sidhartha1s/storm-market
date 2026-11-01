# g-a3-2-roads · A3-S2 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Built on the base `g-a3-1-steering` (same wide plate P-WIDE, projection, pins, colours): copy it only after the base passed its full-size frame read. Page part exemplar: `ep-1974-super-outbreak/compositions/g-cite-paper.html` (a lit line on a scan).

## 0. Claim
The Bureau's own journal, the Monthly Weather Review of September 1900 (the issue that carried Cline's report), says September hurricanes sometimes recurve north and northeast along the Atlantic coast and disappear past Newfoundland, and others pass westward over the Gulf of Mexico.

## 1. Source
factcheck/a3-r1.md rows 5 to 7: MWR Sept 1900 p. 395 (E. B. Garriott), "The hurricanes of September sometimes recurve north and northeast along the Atlantic coast of the United States and disappear over the Atlantic east of Newfoundland, and others pass westward over the Gulf of Mexico." Cline's report in the same issue, pp. 371 to 373.

## 2. Datum, scale, orientation
Two parts, one comp:
- Part A (0.00 to 7.98): full-frame page panel. Scan `media/candidates/a3/A3-S2_c1_mwr-sept1900-p395_recurve-statement.png` (verifier pick pending) cropped to the full text column (mg-quickref Text doctrine: whole lines, no word cut at either end of the push). Page box 1240 px wide, centred x 900, on the glass surface; slow push scale 1.00 to 1.06 toward the quoted sentence.
- Part B (7.98 to end): P-WIDE plate, camera V-ROADS cx 2500, cy 800, s 0.34 (Cuba to Newfoundland and the whole Gulf in frame). Pins by formula: Havana (1585.8, 1857.6); N arrow head and Newfoundland label anchor (lon -55, lat 46) = (4050.0, -519.8), screen (1487, 91).

## 3. Geometry
- Highlight on the scan: an amber band `#d8a13a` opacity 0.28 behind the quoted sentence's lines, boxes measured on the scan by the builder (list the boxes in the receipt). The rest of the page dims to opacity 0.55 as the band draws left to right.
- Arrow N ("recurve"): from Havana's east side (lon -80, lat 24) = (1800, 1767.1) north along the coast, control points (lon -79, lat 31) = (1890, 1039.5) and (lon -70, lat 40) = (2700, 104.0), to (lon -55, lat 46) = (4050, -519.8). Stroke `#7fb2e5` 8 screen px, arrowhead, drawn by strokeDashoffset.
- Arrow W ("westward"): from (lon -84, lat 23.5) = (1440, 1819.1) west across the Gulf to (lon -94, lat 25) = (540, 1663.2), gentle curve, stroke `#d8a13a` 8 screen px, arrowhead. It ends offshore: it never touches Texas or the Galveston pin.
- Label "Newfoundland" Arial 700 22 px `#93a3b2` on the HUD at the N arrow head.
- Chips: C1 "SOMETIMES RECURVE" centred x 960, top 150. C2 "OTHERS PASS WESTWARD" centred x 960, top 150 after C1 leaves (same zone, one after the other).
- Source line top-left: "Monthly Weather Review, September 1900, p. 395 (E. B. Garriott)".

## 4. Must be true in the picture
1. The scan shows whole lines in every frame of the push (check frames at 0.0 and 7.9).
2. Neither arrow is the 1900 storm's track: no date, no "1900" on the map part. The W arrow stops at least 200 plate px short of any coast.
3. Chip wording follows the MWR's ("recurve", "westward"); the voice says "curve" and "pass westward": both fit.
4. Nothing in x >= 1600, y >= 680 (the N arrow runs top-right; check its path stays above y 680 on screen).

## 5. Text and cues (a3-s2.words.json, segment 16.58 s)
- 0.00: page in, source line in.
- 3.52 ("Monthly") /* MWR @3.52 */: push starts.
- 5.76 ("same issue") /* SAME ISSUE @5.76 */: highlight band draws 5.76 to 7.08.
- 7.98 ("September") /* SEPTEMBER @7.98 */: cross-dissolve 0.5 s to Part B.
- 9.46 ("curve") /* CURVE @9.46 */: N arrow draws 9.46 to 13.38 ("Newfoundland"); C1 in at 8.94 ("sometimes"); "Newfoundland" label at 13.38.
- 14.10: C1 out.
- 14.70 ("Others") /* OTHERS @14.70 */: C2 in; W arrow draws 15.04 ("westward") to 16.28 ("Mexico").
- Host 0.00 to 16.58 plus land time (cap 17.4).

## Motion for the whole window
Page push in Part A; slow camera drift s 0.34 to 0.35 in Part B; chips drift.

## Exit
A3-S3 opens on the NOAA weather-map scans (cut): C2 slides out ending at host end, root fade 0.3 s.

## Footage under it
None besides the scan inside Part A (full-frame comp).
