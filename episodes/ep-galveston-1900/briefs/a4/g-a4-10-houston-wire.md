# g-a4-10-houston-wire · A4-S6 2.60 to 14.30 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (ISLAND PLATE). Base: `compositions/g-a4-2-half-city.html` (part A plate); `compositions/g-intro-4-wire-map.html` (part B: its projection, Gulf basemap and Washington telegraph line; reuse, do not re-derive).

## 0. Claim
Joseph went to the telegraph offices through water two to four feet deep; the wires were down, but one long-distance telephone wire still worked to Houston, and over it he gave the message to Western Union there, to go on to Washington.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 28 to 30; a4-r2.md rows 6 to 8; a3-r2.md rows 36, 37): "went to the telegraph offices through water from two to four feet deep, and found that the telegraph wires had all gone down"; "the long distance telephone had one wire still working to Houston, over which he gave the message to the Western Union telegraph office at Houston to be forwarded to the Central Office at Washington". Coordinates (standard gazetteer): Galveston (-94.80, 29.30), Houston (-95.37, 29.76), Washington DC (-77.04, 38.90): screen points from g-intro-4's projection function, printed in the receipt.

## 2. Datum, scale, orientation
- Part A (2.60 to 8.76): island plate (g-a4-2), zoomed 1.0. Figure and gauge on the street between columns 9 and 10 (x 1284), telegraph office block = column 10, row 5 (x 1292 to 1384, y 410 to 480), labelled "Telegraph offices" (schematic position).
- Part B (8.76 to end): logZoom pull-out (helpers.js; > 1.5x) from the island plate to g-intro-4's Gulf framing with Houston, then on to the Washington framing. Text only on the fixed HUD layer after each move settles.

## 3. Geometry (px)
- Part A: wading figure silhouette 18 x 46 px `#f2f5f8` walking north along x 1284 from row 2 (y 700) to the office (y 490), in water: a local water patch `#5a768f` 0.8 over the streets it crosses. Depth gauge: vertical glass card 120 x 360 at x 1420 to 1540, y 240 to 600 (clear of the corner), scale 0 to 5 ft at 60 px/ft (bottom y 600 = 0 ft), a water bar `#7fb2e5` rising to the 2 ft mark (y 480) then wavering between 2 ft (y 480) and 4 ft (y 360); label leaf "2 TO 4 FT" Arial Black 900 52 px `#f2f5f8` left of the gauge, right-aligned to x 1400 at top 380.
- Poles: 4 telegraph pole glyphs `#93a3b2` along the bay edge (x 700 to 1300, y 300), wires `#93a3b2` 2 px drawn slack and broken (two segments dangling: rotation on wire ends). No label (Change 6).
- Part B: the phone line: a `#e8c56a` 4 px glowing path Galveston to Houston (dash draw, glow via drop-shadow filter on the path), Houston pin and label "Houston" Arial 700 26 px `#f2f5f8`; then Houston to Washington path draws `#e8c56a`, Washington pin, label "Washington". Label "Western Union, Houston" as a chip (glass, main Arial Black 900 52 px) "ONE WIRE TO HOUSTON", tag "long-distance telephone", top-left under the source line (left 96, top 130).
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, pp. 372 and 373".

## 4. Must be true in the picture
1. Gauge water stays between the 2 ft and 4 ft marks after it lands (never above 4, never below 2).
2. Only one glowing line leaves Galveston; it goes to Houston first, and the Washington leg starts at Houston, not Galveston.
3. Pins sit on the gazetteer points through g-intro-4's projection within 3 px (receipt lists them).
4. No text rides the logZoom: HUD text enters after each move settles and is off during moves.
5. Nothing labelled in x >= 1600, y >= 680; gauge right edge 1540.

## 5. Text and cues (a4-s6.words.json, comp-local = word time - 2.60)
- 2.60 ("Later") /* PLATE @2.60 */: cut from the rain clip; frame 0 shows the island plate with water in the streets.
- 4.50 ("Joseph") /* JOSEPH @4.50 */: figure appears at row 2; 4.86 ("waded") walks north (4.86 to 7.80, steady, legs bob).
- 7.02 ("two") /* 2 TO 4 @7.02 */: gauge in, bar rises to 2 ft; 7.54 ("four") bar swings to 4 ft and wavers; label in at 7.82 ("feet").
- 5.54 ("telegraph"): poles and broken wires draw (0.6 s); office block outline pulses.
- 8.76 ("One") /* WIRE @8.76 */: gauge and label out (0.4 s); logZoom pull-out 8.76 to 9.76.
- 9.40 ("wire") to 10.50 ("Houston") /* HOUSTON @10.50 */: Galveston to Houston line draws 9.80 to 10.50; Houston label in at 10.50; chip in at 10.70.
- 12.68 ("message") /* MESSAGE @12.68 */: chip out; logZoom to the Washington framing 12.68 to 13.38; Western Union step: Houston pin flashes at 13.38 ("Western Union"); Houston to Washington line draws 13.40 to 14.00; Washington label in at 14.00.
- 14.30 segment end; land time to the cut.

## Motion for the whole window
Water ripple and figure walk in part A; line glow pulse (opacity 0.7 to 1, 0.8 s) in part B.

## Exit
Labels fade with a slow push; cut to g-a4-11 (A4-S7).

## Footage under it
Before the host: A4-S6_c1 water drops on window (verified Y), 0 to 2.60. Under the host: none (full-frame map).
