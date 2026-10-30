# g-a2-7-wire-cut · A2-S6 (whole) · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (the shared map, wires, chips). Base: `compositions/g-a2-5-two-offices.html` (built first; copy its extended plate, projection, camera function, pins and wire layer). The dark line and the "×" mark follow `compositions/g-intro-4-wire-map.html`.

## 0. Claim
On Cuba the War Department ran the government telegraph and, at the Bureau's request, banned weather messages from it. Moore also cut his own Havana office's direct wire to New Orleans: Havana's reports went to Washington first, and Washington decided what New Orleans was told.

## 1. Source
All SECONDARY, one source, named on the source line (factcheck/a2-r1.md row 35; a2-r2 rows 9, 10, 12):
- War Department lines: row 36 (Roker: "the U.S. War Department controlled all of Cuba's government-owned telegraph lines").
- Ban at the Bureau's request: row 37 ("responded quickly to the Weather Bureau's request to formally ban from those lines all messages referring to weather").
- Havana to New Orleans cut: row 38 ("banned direct communication between the U.S. Weather Bureau's office in Havana and the office in New Orleans"); Econlib (Larson) agrees (a2-r2 row 12).
- Routing: row 39 ("Havana would report directly to Washington, and Washington would decide what information to give New Orleans").
- Cuba's line network: no row. Drawn as one schematic line (`_list.md` change 4).

## 2. Datum, scale, orientation
- Plate, formula, extended box: as g-a2-5. Points: Havana (1585.8, 1857.6), Santiago de Cuba (2176.2, 2180.9), New Orleans (893.7, 1148.6), Washington (2066.4, 218.3).
- Camera states (computed 28 Oct 26):
  - V-CUBA: cx 1880, cy 2020, s 1.1. Havana (636, 361); Santiago de Cuba (1286, 717).
  - V-NOLA: cx 1480, cy 1038, s 0.55. Havana (1018, 991); New Orleans (638, 601); Washington (1283, 89).
  - V-CUBA to V-NOLA is a 2x pull-out: `logZoom`.

## 3. Geometry
- Cuba's government line (plate units): one straight line Havana to Santiago de Cuba, `#c8d3e0` 3 px, with 8 px pole ticks every 40 plate px; drawn by strokeDashoffset. When banned it turns dark (dashed 14/12, `#5a768f`, opacity 0.35).
- Line label (HUD, V-CUBA): "Government telegraph lines" Arial 700 26 px `#c8d3e0`, left x 820, baseline 640; "Schematic" Arial 700 20 px `#93a3b2` tracking 4 under it, baseline 668. (Line midpoint is at screen (961, 539); the label sits below the line, never under it.)
- Stamp "WAR DEPARTMENT" (tokens `.stamp`: crimson `#8e2020` box, text Arial Black 900 40 px `#f4f0e8` tracking 4, padding 12px 26px, radius 4), centred (760, 440), rotation -6 deg. It is meant to lie across the line: `data-overlap-ok="stamp lands on the line it names"` on the stamp box (the line passes under the stamp, no text under the line).
- Direct line Havana to New Orleans (plate units): `#7fb2e5` 4 px; cut mark "×" Arial Black 900 34 px `#c0392b` at its midpoint, plate (1239.8, 1503.1) = screen (828, 796) in V-NOLA. After the cut, both halves go dark (opacity 0.35, dashed).
- Reroute: Havana to Washington and Washington to New Orleans, lit wire style (Shared rules). A message pulse (a 40 px `#f2f5f8` dash) travels each leg on its cue.
- HUD labels in V-CUBA: "Havana" 30 px `#e8c56a`, left x 662, baseline 352; "Santiago de Cuba" 24 px `#93a3b2`, right edge 1262, baseline 752.
- HUD labels in V-NOLA: "Havana" 26 px `#e8c56a`, right edge 995, baseline 1000; "New Orleans" 30 px `#f2f5f8`, left x 662, baseline 612; "Washington" 30 px `#7fb2e5`, left x 1306, baseline 100.
- Chips (Shared rules, no tag): "NO WEATHER MESSAGES" centred x 960, top 120 (V-CUBA); "WASHINGTON DECIDES" left 120, top 300 (V-NOLA; clear of every pin and label).
- Source line (top-left): "Al Roker, HistoryNet (secondary) · NOAA AOML, 2015".

## 4. Must be true in the picture
1. Every pin on its formula point within 10 px in both states; receipt lists them.
2. The Cuba line is labelled "Schematic" whenever it is lit; it has no branches and no town stops.
3. After the cut (12.04) there is no lit line from Havana to New Orleans for the rest of the comp; the only lit path to New Orleans goes through Washington.
4. The pulse order is Havana to Washington first, then Washington to New Orleans (the voice's order).
5. No Galveston pin or label in this comp (the line is about New Orleans; Galveston returns in g-a2-8).
6. Nothing enters x >= 1600, y >= 680 in either state.
7. No label rides the pull-out: V-CUBA labels, the stamp and the chip are at 0 before 9.08; V-NOLA labels enter after 10.16.

## 5. Text and cues (a2-s6.words.json)
- 0.00: plate in V-CUBA, Havana pin (amber with blue ring, as g-a2-5) and label on; source line in. Camera drifts s 1.10 to 1.12, 0 to 9.0.
- 0.24 ("island" 0.24): Cuba's coastline brightens (stroke `#5a768f` to `#7fb2e5` and back over 1.2 s).
- 2.04 ("telegraph" 2.04) /* TELEGRAPH @2.04 */: government line draws Havana to Santiago 2.04 to 2.94; Santiago pin and label in at 2.54; line label in at 2.54 ("lines").
- 3.98 ("War" 3.98) /* WAR DEPARTMENT @3.98 */: stamp slams on (scale 1.6 to 1, autoAlpha 0 to 1, 0.3 s, back.out(2)), landing on "Department." 4.26.
- 6.74 ("banned" 6.74): government line goes dark (0.4 s).
- 7.14 ("weather" 7.14) /* NO WEATHER @7.14 */: chip NO WEATHER MESSAGES enters.
- 8.50 to 9.04: chip, stamp and V-CUBA labels fade out.
- 9.08 ("Moore" 9.08) to 10.16: camera pulls V-CUBA to V-NOLA, logZoom.
- 10.16 ("Havana" 10.16): V-NOLA Havana label in.
- 11.14 ("wiring" 11.14) /* WIRING @11.14 */: direct line draws Havana to New Orleans 11.14 to 11.74; New Orleans pin drops at 11.46 ("New"), label at 11.74.
- 12.04 ("directly." 12.04) /* CUT @12.04 */: "×" pops at the midpoint (scale 0 to 1, back.out(2), 0.3 s); the line goes dark.
- 13.12 ("Havana's" 13.12) /* TO WASHINGTON @13.12 */: Havana to Washington wire draws 13.12 to 14.18; Washington pin drops at 14.18 ("Washington"), label in at 14.40; pulse runs Havana to Washington 13.46 to 14.58.
- 16.14 ("decided" 16.14) /* DECIDES @16.14 */: chip WASHINGTON DECIDES enters.
- 16.58 ("what" 16.58): Washington to New Orleans wire draws 16.58 to 17.28; pulse arrives at New Orleans on "told." 17.52; New Orleans pin flashes.
- Host: A2-S6 0.00 to 17.978.

## Motion for the whole window
Pin pulses throughout; drift 0 to 9.0; pull-out; draws and pulses. Longest gap between beats 4.26 to 6.74, covered by drift and pulses.

## Exit
Cut to the A2-S7 map: the whole root fades to 0 over the last 0.35 s (17.628 to 17.978), after the pulse lands.

## Footage under it
None: full-frame designed map (coverage 100 %).
