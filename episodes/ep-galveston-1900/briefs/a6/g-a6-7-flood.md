# g-a6-7-flood · A6-S5 0.00 to 12.92 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `g-a6-4-grade` plan panel (island band, grid, seawall line, colours); copy after its frame read. Exemplar for the two counts: `library/inhouse/numbers-rollup.html`.

## 0. Claim
The water still got in: parts of the city were flooded for 40 hours. The 1915 storm took at least 275 lives along the coast, but a dozen or fewer inside the walled city of Galveston.

## 1. Source
- NWS Houston/Galveston 1910s (sources-a6.md §4): "The storm surge flooded parts of the city for 40 hours"; "275 lives were lost even though the Weather Bureau had issued warnings 24 hours in advance".
- Galveston and Texas History Center (Rosenberg): "The hurricane caused 12 deaths ... in the city". Spread: Wikipedia/MWR Aug 1915 11; NOAA 200th six in the city (factcheck a6-r1 row 26) → "12 OR FEWER".
- Coast: NWS 275, AOML about 400, NHC 403 to 405 whole path (row 25) → "AT LEAST 275".
- No row says WHICH parts flooded: shading is SCHEMATIC.

## 2. Datum, scale, orientation
The g-a6-4 plan, north up, now full-frame: the plan panel scaled 1.6x about its grid centre so the grid spans about x 300 to 1500, y 300 to 830. SCHEMATIC, NOT TO SCALE ("Schematic plan" label kept, bottom-left at 120, 960). All grid squares are filled sand (the raise is done).

## 3. Geometry (px)
- Flood shading: water `#2f5d86` at opacity 0.55, appearing in 7 of the 18 squares (the northern row and two squares of the middle row, the bay side, i.e. away from the wall), with a slow ripple (opacity 0.45 to 0.6, sine). No shading on the squares touching the seawall line.
- Chip C1 "FLOODED 40 HOURS": glass, main line "FLOODED" 40 px, figure "40 HOURS" Arial Black 900 56 px; left edge x 120, top 150. A thin clock bar under it (`#7fb2e5`, 360 px, scaleX 0 to 1 over 2.0 s).
- Count chips (side by side, glass, each 640 px wide, top 640, the plan dimmed to 0.35 behind them):
  - C2 left edge x 240: eyebrow "ALONG THE COAST" Arial 700 24 px `#93a3b2` tracking 3; figure "AT LEAST 275" Arial Black 900 64 px `#f2f5f8` (the 275 counts up from 0 on a leaf span).
  - C3 left edge x 1040: eyebrow "INSIDE GALVESTON"; figure "12 OR FEWER" Arial Black 900 64 px `#f5d98b`.
  - C3's right edge = 1680 > 1600 and its bottom ≈ 800 > 680: the circle is OFF for this window. (Or shrink both to 600 px with C3 at x 1000; builder states which.)
- Source line top-left: "National Weather Service Houston/Galveston · Galveston and Texas History Center, Rosenberg Library".

## 4. Must be true in the picture
1. Shading only in some squares (7 of 18), never the whole city, and never against the wall; "Schematic plan" visible all window.
2. The two counts carry their scope words (ALONG THE COAST / INSIDE GALVESTON); the numbers never stand without them.
3. "AT LEAST 275" and "12 OR FEWER" exactly; no 400, 403, 6 or 12-alone.
4. C2 and C3 sit side by side at equal size; the coast figure is not made to look smaller than the city one by type size (same 64 px).
5. Dup-fact: "40" appears once.

## 5. Text and cues (a6-s5.words.json, 16.227 s; host 0.00 to 12.92)
Frame 0: the plan, sand-filled, seawall line; source line in at 0.20.
- 0.14 ("water") /* IN @0.14 */: water seeps into the shaded squares from the bay edge, 0.14 to 1.80 (each square 0.3 s, stepped north to south).
- 3.20 ("40" 3.20) /* 40 HOURS @3.20 */: C1 in; clock bar runs 3.20 to 5.20.
- 4.46 ("At"): C1 out at 4.30; plan dims to 0.35 at 4.46.
- 4.68 ("275" 4.68) /* 275 @4.68 */: C2 in; count-up 4.68 to 5.62 (power3.out, opening on the first tick's value).
- 9.12 ("Inside") /* 12 OR FEWER @11.70 */: C3 in at 9.94 ("Galveston,") with eyebrow; figure "12 OR FEWER" lands at 11.70 ("dozen").
- 12.32: C2 and C3 slide out (0.6 s), done 12.92.

## Motion for the whole window
Water ripple on the shaded squares all window; plan pushes 1.00 to 1.03 linear; chips float.

## Exit
Cut to g-a6-8 at "And" 12.92.

## Footage under it
None: full-frame designed plan.
