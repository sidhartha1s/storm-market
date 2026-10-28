# g-a4-2-half-city · A4-S1 4.58 to 11.02 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (ISLAND PLATE is defined there; this comp is its base: send it alone for a full-size read before g-a4-9, 10, 17 copy it). Exemplars: `compositions/g-a5-3-island-map.html` (Natural Earth island polygon, projection, city-end cut), `compositions/g-intro-4-wire-map.html` (projection function).

## 0. Claim
Cline drove to the bay side first, then the Gulf side, and found about half the city's streets under water; his own house stood on ground 5.2 ft above sea level.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 3, 4): "I drove first to the bay and then to the Gulf", "finding that half the streets of the city were under water". Ground 5.2 ft: "The ground was 5.2 feet elevation" (p. 373; factcheck/a4-r2.md row 9; A1-S6 chip wording "CLINE'S HOUSE, 1900: 5.2 FT"). Street layout and which half flooded: NO research row: SCHEMATIC.

## 2. Datum, scale, orientation
North up, plan view, g-a5-3's projection and island polygon (reuse its function and data; do not re-derive). Zoom so the city end spans x 160 to 1760. Street grid per `_list.md` ISLAND PLATE: 12 x 6 blocks, 92 x 70 px, 16 px streets, x 320 to 1600, y 324 to 824, rows counted from the Gulf (bottom). Bay (north) on top, Gulf (south) at the bottom. "Street grid: schematic" note bottom-left.

## 3. Geometry (px)
- Background tokens gradient; Gulf and bay water `#0b1016` with a slow `#5a768f` ripple line; island land `#15202b`, 2 px `#93a3b2` coast; blocks `#2a3644`, streets the land colour.
- Labels Arial 700 22 px `#93a3b2` tracking 3: "Galveston Bay" centred (960, 230); "Gulf of Mexico" centred (960, 900).
- Bay-side zone: rows 5 and 6 (y 324 to 480) outlined `#7fb2e5` 3 px, label "Bay side" Arial 700 26 px `#f2f5f8` at (300, 290) left of the grid's top-left, above it. Gulf-side zone: rows 1 and 2 (y 668 to 824) outlined the same, label "Gulf side" at (300, 860).
- Buggy icon: 48 x 32 px side-view buggy `#e8c56a`, path along the street between columns 6 and 7 (x 960), from (960, 300) south to (960, 848). Moves by GSAP `y` only; check it sits on x 960 at three times.
- Flood fill: 36 of the 72 blocks (half) turn `#5a768f` at 0.85 with a `#7fb2e5` edge, filling from the Gulf side upward: rows 1, 2, 3 (36 blocks). The pin block (column 7, row 3) is inside the flooded rows: keep it unflooded-looking? NO: draw it flooded like its row (water covers streets near his house is consistent with p. 373 later). The legend chip carries the meaning.
- Chip C1 (glass, shared spec) "ABOUT HALF THE CITY" at left 96, top 120 (below source line), tag "streets under water · p. 373". Wait: source line at top 54; C1 top 130.
- Pin: `#d0121f` 22 px dot with 4 px `#f2f5f8` ring at (1014, 617), label leaf "25th St & Q" Arial 700 26 px `#f2f5f8` with shadow, right of the pin at (1040, 600). Chip C2 "CLINE'S HOUSE, 1900: 5.2 FT" right-aligned to x 1824, top 130, tag "ground elevation, his report"; 1 px `#d8a13a` leader from C2's bottom-left to the pin.
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. Exactly 36 of 72 blocks flood (half), and the fill reads as reaching from the Gulf side inward; the receipt prints the count.
2. The buggy reaches the bay side before the Gulf side (bay first, per the report).
3. Island outline is the Natural Earth polygon (receipt states px per km of the fit); the grid is labelled schematic.
4. C1 and C2 never on screen together with any other chip in their zones; pin label does not touch a block outline or the buggy path label.
5. No street names other than the pin's "25th St & Q" (no research row for others).

## 5. Text and cues (a4-s1.words.json, comp-local = word time - 4.58)
- 4.58 ("He'd") /* START @4.58 */: frame 0 shows water, island, grid, labels; source line on; first 0.4 s the grid draws in rows (strokeDashoffset) so something moves.
- 5.24 ("Bayside") /* BAY @5.24 */: buggy at the top street end; bay-side outline pulses twice (0.5 s each); "Bay side" label in.
- 6.52 ("then") to 6.82: buggy runs south along x 960 (6.52 to 7.20, power2.inOut).
- 6.82 ("Gulf") /* GULF @6.82 */: Gulf-side outline pulses; "Gulf side" label in; blocks flood row by row 7.00 to 7.80 (stagger 0.02 per block); C1 in at 7.00.
- 7.92 ("his"): C1 out (x 980, 0.5).
- 8.20 ("house") /* HOUSE @8.20 */: pin drops in (y -40 to 0, back.out), label in.
- 10.06 ("5") /* 5.2 @10.06 */: C2 in with its leader (draw 0.4 s).
- 11.02 segment end: hold to the cut into A4-S2 (land time 0.6 s if the next segment's gap allows).

## Motion for the whole window
Water ripple lines and a slow 1.00 to 1.03 push on the map (linear is fine, under 1.5x); pin ring pulses every 1.2 s.

## Exit
Cut to A4-S2's beach footage; C2 slides out `x:980` in the last 0.6 s.

## Footage under it
None: full-frame map.
