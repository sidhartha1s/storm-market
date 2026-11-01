# g-a6-3-wall · A6-S2 9.98 to end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `episodes/ep-galveston-1900/compositions/g-intro-6-island.html` (this episode's island cross-section: same colours, water, house glyphs) and `episodes/ep6-katrina-2005/compositions/g-surge-ms.html` (heights on a datum). Worked brief: `references/mg-brief-example-g-slope.md`.
This comp is the BASE of a family: g-a6-6-surge copies its plate, datum, scale and wall path. Send it alone for a full-size frame read before g-a6-6 is built.

## 0. Claim
The new wall stood 17 ft above mean low tide, about twice the 8.7 ft of the highest ground on the island in 1900.

## 1. Source
- ASCE (sources-a6.md §2): "16 feet wide on the base at elevation 1 foot above mean low water", "5 feet wide on top at elevation 17 feet above mean low water"; "the curved concrete section"; riprap "extending 27 ft outward from the toe".
- Rosenberg Library (sources-a6.md §2): first section "17 feet high, and measured 16 feet wide at the base and 5 feet wide on top".
- 1900 island: NPS "the highest elevation on Galveston Island was 8.7 feet" (sources-cline.md §5; edit_script.md T1-S1 rows).
- No published section drawing is on disk: the profile is built from these four numbers; the curve of the face is SCHEMATIC.

## 2. Datum, scale, orientation
- Cross-section looking west: Gulf of Mexico on the LEFT (south, seaward), the city on the RIGHT (north).
- Datum: mean low water = y 900, x 96 to 1824. Labelled "Mean low tide" Arial 700 22 px `#93a3b2`, left 120, top 912.
- Scale: 36 px per ft, the SAME horizontally and vertically, so the wall's shape is true to its numbers. Heights: 1 ft y 864 · 8.7 ft y 586.8 · 17 ft y 288.
- Datum caveat: the 8.7 ft is NPS's figure with its datum unstated; it is drawn on the mean-low-tide axis. The narration says "about twice" (17 / 8.7 = 1.95), which holds on either datum within a foot. State this in the receipt; no on-screen caveat.

## 3. Geometry (px)
- Sea: fill below y 900 left of the wall toe, `#0b1016` to `#04070c`, surface line `#5a768f` 3 px with a sine wave (amplitude 6 px).
- Beach: a sand wedge from (96, 930) rising to the toe (760, 864), fill `#2a2f36`.
- Wall (one closed path, fill `#8d96a0` concrete, edge `#c8d3e0` 3 px):
  - seaward toe (760, 864); landward base corner (1336, 864): base 576 px = 16 ft.
  - landward face vertical (1336, 864) to (1336, 288).
  - top (1336, 288) to (1156, 288): 180 px = 5 ft.
  - seaward curved face from (1156, 288) down to (760, 864): concave, bezier control points (1120, 700) and (900, 860) as a start; it must bow inward (toward the land), and the builder may adjust the controls but not the four corner points.
  - riprap: NOT drawn (27 ft = 972 px runs off the frame; not spoken).
- Land behind: fill `#15202b` from x 1336 to 1824 at y 864 down, unlabelled.
- 1900 island line: dashed `#d8a13a` 3 px (dash 14/10) at y 586.8 from x 1360 to 1824, label above its right end "HIGHEST POINT IN 1900: 8.7 FT" (diagram label, Arial 700 26 px `#d8a13a`, right edge 1800, bottom at y 572).
- Height bracket A (wall): vertical line `#f2f5f8` 3 px at x 1380 from y 900 to y 288, end ticks 30 px. Chip "17 FT" (glass, Arial Black 900 56 px) with its left edge at x 1420, top 240.
- Height bracket B (island): vertical `#d8a13a` 3 px at x 1760 from y 900 to 586.8, ticks 30 px. Unlabelled (the line label names it).
- Dimension labels (diagram tier, Arial 700 24 px `#c8d3e0`, with a 2 px dimension line and arrowheads):
  - base: under the wall at y 960, from x 760 to 1336, text "16 ft base" centred at (1048, 990).
  - top: above the wall top at y 262, from x 1156 to 1336, text "5 ft top" centred at (1246, 236): left of chip "17 FT" (chip starts x 1420). If they touch, move the chip, not the label.
- "TWICE" marker: at "twice" a ghost copy of bracket B (dashed `#d8a13a`, 313.2 px) stacks twice beside bracket A at x 1400: first segment y 900 to 586.8, second y 586.8 to 273.6, ending 14.4 px above the wall top (that 14 px is the "about").
- Source line top-left: "American Society of Civil Engineers · Rosenberg Library · National Park Service", second line "Heights above mean low tide".

## 4. Must be true in the picture
1. Wall top at y 288 ±3 and datum at y 900 ±2: bracket A = 612 px (17 x 36). Base 576 px ±4, top 180 px ±4.
2. The 8.7 ft line at y 586.8 ±3: bracket B = 313.2 px. Ratio A/B = 1.95 within 2 %.
3. The doubled ghost of B ends within 20 px of the wall top (17.4 vs 17 ft): the picture says "about twice", never "more than twice" by a visible margin.
4. Gulf on the left, city on the right; the curved face looks to the sea and bows inward.
5. No surge or flood water is shown: the sea stays at its calm level (the 1915 water belongs to g-a6-6).
6. The 8.7 line is labelled 1900 so it never reads as today's ground behind the wall (the grade raise comes in S3).
7. Nothing in the corner x >= 1600, y >= 680 except bracket B (a labelled-by-line highlighted shape): presenter circle OFF for this window.

## 5. Text and cues (a6-s2.words.json, 16.094 s; host starts at "It" 9.98)
Comp-local = word time − 9.98. Frame 0 shows datum, sea, beach and the finished wall (the cut lands on a drawn wall); waves moving.
- 9.98: source line in.
- 10.34 ("17" 10.34) /* 17 FT @10.34 */: bracket A draws up 10.34 to 11.20, power2.out; chip "17 FT" in at 10.94 ("feet").
- 11.62 ("low") : "Mean low tide" datum label brightens (opacity 0.6 to 1).
- 12.20: dimension labels "16 ft base" and "5 ft top" draw in, 0.3 s stagger.
- 12.96 ("twice") /* TWICE @12.96 */: bracket A pulses once (scaleY 1 to 1.04 to 1). "Twice" comes before "highest" in the voice, so the comparison is only completed at 15.26.
- 13.92 ("highest") /* 8.7 @13.92 */: the 1900 line draws right to left from x 1824, 13.92 to 14.60; bracket B up; label in at 14.20 ("ground").
- 15.26 ("1900.") /* DOUBLE @15.26 */: the doubled ghost of B stacks beside A, 15.26 to 15.90.
- Host end: 16.094 + the gap to A6-S3 (default 16.094 + 0.6 land time).

## Fallback (no construction photo: g-a6-2 dropped)
Host starts at 0.94 ("wall."): frame 0 = sea and datum only; the wall rises from the datum 0.94 to 2.20 (scaleY 0 to 1 from the base, power3.out); C1 "SEPT 1902" at 2.52 and C2 "3.3 MILES · 1902 TO 1904" at 6.18 sit top-left at left 120, top 150 (g-a6-2 §3), C2 out by 9.80; then the cues above.

## Motion for the whole window
Waves run the whole host (phase tween `ease:none`). A slow push on the whole plate, scale 1.00 to 1.03 around (1048, 600), linear. Chips float per shared rules.

## Exit
A6-S3 opens on g-a6-4 (a cut): root fades to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed diagram (tokens.md radial gradient ground).
