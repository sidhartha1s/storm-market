# g-a5-3-island-map · A5-S3 0 to 8.74 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `compositions/g-intro-4-wire-map.html` (Natural Earth basemap, projection, Galveston pin) and `library/inhouse/master-map-us-canada.html` (projection rig). This comp is the base g-a5-7-ride copies: send it alone for a full-size read first.

## 0. Claim
The death tolls differ because they count different areas: the city (6,000 to 8,000) or the whole island (10,000 to 12,000). Even the lowest is about one in six of the city's 38,000.

## 1. Source
- City 6,000 to 8,000: TSHA "Between 6,000 and 8,000 people in the city of Galveston had died" (sources-cline.md §5; fact-check a5-r1 row 13).
- Whole island 10,000 to 12,000: TSHA "estimated casualties for the entire island ranged from 10,000 to 12,000" (same rows), NPS.
- 38,000: TSHA "the city of 38,000 inhabitants" (factcheck-A.md T1-S1). 6,000 / 38,000 = 0.158 (python3; fact-check row 14).
- Island outline: Natural Earth 10m land (the basemap already vendored for g-intro-4). City extent: NO research row. The city is drawn as the island's east end, its west limit SCHEMATIC.

## 2. Datum, scale, orientation
- North up, plan view, the same projection as g-intro-4 (reuse its projection function and data; do not re-derive).
- Fit Galveston Island's Natural Earth polygon to a box x 200 to 1720, y 330 to 720, aspect kept; the island runs SW to NE, so the east end is at the right. State the px-per-km the fit produced in the receipt, and add a scale bar "10 km" at bottom-left (left 96, top 980) built from that number.
- City tone boundary: a straight cut across the island at 22 % of the island's length from its NE tip (SCHEMATIC; there is no research row for the 1900 city limit). The note "City limit: schematic" sits under the scale bar, Arial 700 19 px `#93a3b2`.

## 3. Geometry (px)
- Background tokens radial gradient. Gulf water `#0b1016`, mainland and Bolivar Peninsula `#15202b` with `#2a3644` 2 px coast stroke, labels "Gulf of Mexico" (bottom-centre, about (760, 860)) and "Galveston Bay" (top, about (1300, 220)), Arial 700 22 px `#93a3b2` tracking 3.
- Island fill: rest of island `#5a768f` at 0.85 (Cold blue 1), city end `#d8a13a` (Amber 1), both with `#93a3b2` 2 px stroke. Initially the whole island is `#4a5560` (diagram grey) and the two tones come on with the cues.
- Labels on the map: "City of Galveston" next to the amber end, above it; "Rest of the island" over the blue part's centre. Arial 700 26 px `#f2f5f8` with a 0 2px 6px shadow (diagram label).
- Chips (glass, `_list.md` chip spec):
  - C1 "CITY: 6,000 TO 8,000", right-aligned to x 1824 at top 120. Its leader line (1 px `#d8a13a`) runs from the chip's bottom edge to the amber area's centre.
  - C2 "WHOLE ISLAND: 10,000 TO 12,000", left edge x 96, top 120; leader `#7fb2e5` to the island's mid-length.
- Tally T "ABOUT 1 IN 6": six person glyphs (36 x 72 px, `#93a3b2`) in a row under C1 at top 260, right-aligned x 1824; one turns `#d0121f`. Tag under them Arial 700 22 px `#93a3b2` "ABOUT 1 IN 6 · CITY OF 38,000".
- Source line top-left must not collide with C2: put it at top 54 and C2 at top 120 (card height ~110, both inside x 96 to 1000). Text "Texas State Historical Association · National Park Service".

## 4. Must be true in the picture
1. The island's shape is the Natural Earth polygon, not drawn by eye; the city end is the NE end (right side), Gulf to the south (bottom), bay to the north.
2. The amber city area is the smaller part: its length is 22 % of the island's ±2 % (schematic, labelled).
3. C1 points only at the amber part; C2 points at the whole island (its leader lands on the blue part, and the amber part stays lit when C2 is on, since the whole island includes the city).
4. Exactly one of six glyphs is red; no other fraction appears.
5. Nothing in x >= 1600, y >= 680 except water: the circle may stay on only if the island polygon's fit puts no land or label there; else the circle goes off for this window and the receipt says so.
6. No chip or label covers the island polygon.

## 5. Text and cues (a5-s3.words.json, segment 11.50 s)
- 0.00: frame 0 shows water, coasts, labels and the grey island already drawn; source line on.
- 1.70 ("city" 1.70) /* CITY @1.70 */: the city end fills amber (0.5 s), "City of Galveston" label in; C1 in at 1.90.
- 3.14 ("whole" 3.14) /* ISLAND @3.38 */: the rest of the island fills blue in a sweep from NE to SW (0.8 s, power2.out); "Rest of the island" label and C2 in at 3.38.
- 4.70 ("lowest" 4.70): C2 dims to 0.6; C1 border brightens.
- 5.68 ("one" 5.68) /* 1 IN 6 @5.68 */: six glyphs pop in left to right, 0.08 s apart; 6.90 ("six"): the last glyph turns red; tag line in at 7.24.
- 8.00 ("city." 8.00) holds to 8.74.
- Host: A5-S3 0.00 to 8.74 (g-a5-4 cuts in at "The" 8.74).

## Motion for the whole window
Slow camera push on the map layer only (not the HUD chips): scale 1.00 to 1.05 toward the city end, `ease:none`, over the host. Gulf surface: a faint moving shimmer line (6 px/s). Chips drift.

## Exit
Cut at 8.74 to g-a5-4 (full-frame to full-frame): fade the root to 0 over the last 0.3 s.

## Footage under it
None: full-frame map.
