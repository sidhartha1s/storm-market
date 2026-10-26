# g-intro-4-wire-map · H1-S4 · DEEP · Opus 5.5 high
Shared rules: `_shared.md`. Exemplars: `library/inhouse/master-map-us-canada.html` (camera rig, lon/lat pins, projection-by-formula discipline; its basemap stops at the US border, so it cannot be reused as is) and `episodes/ep6-katrina-2005/compositions/g-track.html` (Gulf camera with a clamp; its plate has Katrina's track burned in, do not reuse the plate). This comp is the BASE of a family (g-intro-8-track reuses the plate, projection, pins and wire layer): send the base alone for a full-size frame read before g-intro-8 copies it.

## 0. Claim
Havana's Belen forecasters said the storm was going northwest into the Gulf of Mexico; the Weather Bureau in Washington ruled that only its own forecasts went over the telegraph, so the only forecast on the wire to Galveston was Washington's.

## 1. Source
- sources-cuba.md §1: AOML (2015) "the Belén forecasters said their observations indicated the storm moved to the northwest and into the Gulf of Mexico." Jesuit: cubamemorias.com via factcheck-B.md.
- sources-cuba.md §2: AOML "the USWB decreed that only its forecasts would be carried over the telegraph." No order text and no date exist (Conflicts 1 and 2); the drawing shows the effect, never a date or a route.
- Conflict 3 (sources-cuba.md): only "into the Gulf" is supported. Texas or San Antonio is secondary only.

## 2. Datum, scale, orientation (the plate)
- Basemap: Natural Earth 1:50m admin-0 countries (public domain), plus admin-1 US state lines for Texas, Louisiana and Florida only if they read; land `#15202b`, coast stroke `#5a768f` 2 px, water `#04070c` with the canvas radial gradient (tokens.md). Not on disk: fetch the NE shapefile or GeoJSON, convert to SVG path data with a one-shot, uncommitted, content-blind script (CLAUDE.md "do not write code" allows this transform), and name the file in the receipt.
- Plate: 2700 x 2703 px, north up. Projection (equirectangular with a 30° latitude stretch): `X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`. Covers lon -100 to -70, lat 15 to 41.
- Pins, computed by that formula (checked by script 26 Oct 26): Galveston (-94.80, 29.30) = (468.0, 1216.2); Havana (-82.38, 23.13) = (1585.8, 1857.6); Washington (-77.04, 38.90) = (2066.4, 218.3).
- Camera: screen = 960 + (X - cx) * s, 540 + (Y - cy) * s. Two states:
  - V-HAV: cx 1100, cy 1560, s 1.0 (Havana at screen 1446, 838; Galveston at 328, 196).
  - V-WIRE: cx 1267, cy 1000, s 0.5 (Galveston 560, 648; Havana 1119, 969; Washington 1360, 149). V-HAV to V-WIRE is a 2x pull-out: use `logZoom` from `library/inhouse/snippets/helpers.js`.
- Text lives on a fixed HUD layer above the camera layer, positioned from the projected screen point at the moment the camera has settled (never riding the move).

## 3. Geometry
- Pin: 14 px dot `#f2f5f8` with a 2 px ring pulse (scale 1 to 2.2, opacity 0.8 to 0, 1.4 s, finite repeats). Havana pin `#d8a13a` (amber: the Cuban forecast colour throughout the section); Galveston pin `#f2f5f8`; Washington pin `#7fb2e5` (cold blue: Washington's colour throughout the section).
- Havana label: right-aligned, right edge at screen x 1410, baseline y 885 in V-HAV: line 1 "Belen Observatory" Arial 700 30 px `#e8c56a`, line 2 "Havana" Arial 700 22 px `#93a3b2` tracking 3. Left of the dot so nothing enters x >= 1600.
- Havana arrow (the Belen forecast): from Havana (1585.8, 1857.6) to (-89.0, 27.0) = (990.0, 1455.2), a gentle curve (quadratic control point (1330, 1720)), stroke `#d8a13a` 8 px, round cap, arrowhead 36 px; drawn by `strokeDashoffset` from ceil(len)+1. Label at the head, on the HUD: "Into the Gulf" Arial 700 30 px `#e8c56a`, left of the head.
- Wire layer (V-WIRE): two straight lines into Galveston, 6 px:
  - Washington to Galveston: `#7fb2e5`, lit, with a glow (drop-shadow 0 0 10px). A pulse (a 40 px bright dash, `#f2f5f8`) runs Washington to Galveston on each of its two cues.
  - Havana to Galveston: same width, dashed 14/12, `#5a768f` at opacity 0.35: "dark", visibly unlit, and a small "×" 26 px `#c0392b` on its midpoint at the ruling cue.
  - Labels on the HUD in V-WIRE: "Washington" Arial 700 30 px `#7fb2e5` right of its pin (screen 1385, 158); "Galveston" Arial Black 900 40 px `#f2f5f8` left of its pin, right edge at 535, baseline 660; "Havana" Arial 700 26 px `#e8c56a` left of its pin, right edge 1095, baseline 978.
- Source line top-left, two lines: "NOAA AOML, 2015: the Bureau \"decreed that only its forecasts / would be carried over the telegraph\"".

## 4. Must be true in the picture
1. Every pin sits on its true lon/lat by the formula, within 10 px; the receipt lists the three computed points and a frame showing each.
2. The Havana arrow points northwest into the open Gulf and ends at least 300 plate px (on screen, at least 300 px in V-HAV) short of the Texas coast. It never points at Galveston or Texas (sources-cuba.md conflict 3).
3. The wire lines are straight city-to-city lines. They are not cable routes: no route shape, no relay towns, no landing points.
4. In V-WIRE the Washington line is the only lit line; the Havana line reads clearly as dark (opacity at most 0.35) the moment the ruling is spoken and for the rest of the comp.
5. No date anywhere on this comp (the decree has no date on record).
6. Nothing (pin, line, label) in screen x >= 1600, y >= 680 in either camera state.

## 5. Text and cues (h1-s4.words.json, segment 15.29 s)
- 0.00: plate in V-HAV, fully drawn (frame 0 shows the map, no dark frame after the hard cut from the ruins photo). Source line in at 0.00. Slow drift: camera scale 1.0 to 1.04 over 0 to 7.0 s, ease none.
- 0.40 ("Havana" 0.40) /* HAVANA @0.40 */: Havana pin drops in (y -30 to 0, back.out) and starts pulsing.
- 1.30 ("Jesuit" 1.30): label line 1 "Belen Observatory" in; line 2 "Havana" at 2.64 ("Belen" 2.64).
- 4.56 ("northwest" 4.56) /* NORTHWEST @4.56 */: Havana arrow draws 4.56 to 5.84, power2.inOut.
- 5.84 ("Gulf" 5.84): "Into the Gulf" label lands at the head.
- 7.12 ("But" 7.12): Havana labels fade to 0 over 0.4 s; camera pulls V-HAV to V-WIRE 7.12 to 8.40 with logZoom. The Havana arrow stays (it dims to opacity 0.5).
- 8.08 ("Washington" 8.08) /* WASHINGTON @8.08 */: Washington pin drops in at the settled point; label "Washington" at 8.40.
- 9.30 ("telegraph" 9.30): both wire lines draw from their source city to Galveston, 9.30 to 10.10; Galveston pin and label land at 9.30.
- 10.28 ("only" 10.28) /* ONLY @10.28 */: Havana line goes dark (opacity 1 to 0.35, dash pattern stays), "×" pops at its midpoint (scale 0 to 1, back.out(2)); Washington line brightens and its first pulse runs 10.28 to 11.10.
- 13.42 ("wire" 13.42): second pulse on the Washington line, 13.42 to 14.30, arriving at Galveston on "Galveston" 13.82 to 14.30; the Galveston pin flashes (scale 1 to 1.6 to 1).
- 14.48 ("Washington's" 14.48): hold; camera drifts in V-WIRE (scale 0.5 to 0.51).
- Host 0.00 to 15.29.

## Motion for the whole window
Pin pulses run the whole comp; camera drift 0 to 7.0 and 14.48 to 15.29; nothing idles 4 s (longest gap between discrete beats: 10.28 to 13.42, covered by the pulses and pin rings).

## Exit
H1-S5 is a cut back to the 1891 page: end on the settled V-WIRE hold; the last 0.35 s fades the whole root to 0 (a fade-through, mg-quickref "Exits"), 14.94 to 15.29.

## Footage under it
None: full-frame designed map (frame coverage 100 %). The edit script's "NOAA 1900 weather map" is not used as the plate: no scan is on disk, and drawing pins and arrows on a 1900 projection would be placed by eye. If the orchestrator wants the period map, it goes as a still before 0.00 or as a 1.0 s cross-dissolve into this plate, mounted by the orchestrator, not inside this comp.
