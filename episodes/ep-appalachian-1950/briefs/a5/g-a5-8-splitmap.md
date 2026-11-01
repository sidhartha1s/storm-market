# g-a5-8-splitmap: one storm, two sides, one last time (A5-S8, ground under A5-S9)
Builder: Opus 5.5, high effort. Depth: deep (the episode's closing map, track and airflow). Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, projection, camera rig). Pins, labels and colours: copy from `compositions/g-intro-2-hookmap.html` (pins, label style, glass chips, scan line, basemap credit). If the Act 3 closing split map (A3's last segment: "full split map from the hook with the red track drawn through it") is built when you start, copy ITS track path and arrow paths and re-place them in this brief's frame; otherwise use the schematic points below. Prefix every id/class `a58-`.
Sits over: nothing. Full-frame designed map on track 2, ground on from frame 0. It runs through A5-S9 as the slowly fading ground under `g-a5-9-title` (track 3).

## 0. Claim
That Saturday one low pulled warm Atlantic air northwest on one side and wrapped arctic air around the other: Newark got the wind, Pittsburgh got the snow. Today's NWS computer forecasts descend from the unit that storm's test helped start.

## 1. Source (quoted, with rows)
- NWS JKL https://www.weather.gov/jkl/appalachianstorm1950: "the arctic airmass wrapped southeastward around the low, while warm air from the Atlantic was pulled northwestward". `factcheck/a5-r2.md` row 40; `research/maps-forecast.md` §3 M3.
- Track: low formed on the arctic front over the Carolinas (25th), tracked northwest into Ohio by midday 26th, stalled over Lake Erie 27-28 (`maps-forecast.md` §3 M2, JKL, SECONDARY). Near Washington early 25th: M6, Ocean Weather (SECONDARY). The drawn track is schematic, not traced (as in Act 3).
- Newark wind (108 mph gust, 25 Nov) and Pittsburgh snow (10.1 in on 25 Nov, 27.4 in storm total): row 41. Buffalo orange (40s, no snow) is Act 3's on-screen placement (inference, never spoken).
- "ONE STORM · TWO SIDES": row 45. "EVERY HOLIDAY DRIVE": row 43 conditional; edit_script already carries the evergreen line and chip.
- Basemap: Natural Earth 50m admin-1 (public domain).

## 2. Datum, scale, orientation
- North up, no rotation. Projection: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213).
- Frame S: s 0.016, top-left (20025.2, 5144.2). Computed points (python3, 28 Oct 26):
  - Newark (40.7357, -74.1724) → (89893.2, 32871.1) → screen (1118, 444)
  - Pittsburgh (40.4406, -79.9959) → (67525.2, 34519.2) → (760, 470)
  - Buffalo (42.8864, -78.8784) → (71817.5, 20859.4) → (829, 251)
  - Track T1 Carolinas (35.5, -78.5) → (852, 911); T2 near Washington (38.6, -77.6) → (907, 634); T3 eastern Ohio (40.6, -80.8) → (711, 456); T4 Lake Erie (41.8, -81.6) → (661, 349)
- Camera: frame 0 is Frame S scaled 1.04 about (960, 540) (wide), drifting to exactly Frame S by A5-S8 10.44 (ease none); then a slow push to 1.08 through the S9 fade.

## 3. Geometry (px)
- Basemap as g-intro-2 (state fills `#0b1016` to `#15202b`, lines `#2a3644` 1.2 px non-scaling, coastline `#4a5560` 1.6 px, radial background). Credit folds into the source line.
- Track: thin red line `#c0392b`, 3 px, round caps, smooth curve T1 → T2 → T3 → T4 (Catmull-Rom), ending in a small open loop radius 14 px around T4 (the stall). Drawn by strokeDashoffset; length computed in script (`ceil(len)+1`).
- Warm arrows (east side): 3 curved arrows, `#d8a13a`, 5 px, arrowheads 16 px, drawn by strokeDashoffset then a dash-flow (dashoffset loop, finite repeats) so they stream:
  - W1 (1420, 700) → (1250, 560) → (1080, 330)
  - W2 (1480, 560) → (1300, 420) → (1010, 250)
  - W3 (1360, 820) → (1180, 700) → (960, 520)
  None passes within 30 px of a label. Corner x >= 1600, y >= 680 untouched (all start points x <= 1480).
- Cold arrows (wrapping behind): 3 arrows `#7fb2e5`, 5 px, from the north-west down the west side of the track, under it and curling back north-east to the Pittsburgh side:
  - C1 (430, 150) → (500, 470) → (640, 640) → (740, 540)
  - C2 (330, 260) → (420, 560) → (600, 720) → (700, 620)
  - C3 (520, 110) → (560, 330) → (620, 520)
- Pins (screen size constant; HUD layer or counter-scaled), core 18 px, ring 34 px, 3 px stroke: Newark `#7fb2e5`, Pittsburgh `#f2f5f8`, Buffalo `#d8a13a`.
- Labels (Arial 700 26 px `#dfe7ee`, paint-order stroke `#04070c` 5 px): "NEWARK" to the right of its pin (left edge 24 px right of the dot, so it clears the warm arrows ending west of it; check), "PITTSBURGH" to the right of its pin, "BUFFALO" to the right of its pin. No other place names, no state names.
- Chip 1, top-left zone (left 110, top 90): "ONE STORM · TWO SIDES" glass surface, radius 14, padding 10 x 18, Arial Black 900 52 px `#f2f5f8`.
- Chip 2, same zone after chip 1 leaves: "EVERY HOLIDAY DRIVE" glass, Arial Black 900 40 px `#f2f5f8`.
- Source line (bottom-left, left 110, bottom 60), Arial 700 20 px `#c8d3e0`, glass pill: "NWS Jackson, KY · Track schematic · Basemap: Natural Earth".
- Scan line as g-intro-2 (2 px, 1180 wide, about 60 px/s, opacity 0.30).
- Tiers: 52 (big), 40/26 (mid), 20 (small).

## 4. Must be true in the picture
1. Geography real: every pin within ±10 px of its computed point; Buffalo north of Pittsburgh (dy about -219 px), Newark east (dx about +358 px).
2. Orange arrows sit only on the east side of the track and point north-west; blue arrows come from the north-west, run down the west side and wrap around behind the low. No arrow crosses a pin or a label.
3. The track starts in the Carolinas, goes north, then bends LEFT (north-west) into Ohio and ends in the stall loop over Lake Erie; it never runs up the coast.
4. One reading target at a time: chip 1 is out before chip 2 lands; pins and their one-word place labels may sit beside a chip, no other text.
5. No numbers on the map (no mph, inches, temperatures, dates).
6. Corner x >= 1600, y >= 680 empty in every frame (only ocean).
7. In S9 the map fades to 0.25 and nothing on it sits under the title text at more than 0.25 opacity (occlusion: the title card owns the centre).

## 5. Panel text (exact) and cues
Text: `NEWARK` · `PITTSBURGH` · `BUFFALO` · `ONE STORM · TWO SIDES` · `EVERY HOLIDAY DRIVE` · `NWS Jackson, KY · Track schematic · Basemap: Natural Earth`
Segment offsets (assumes a 0.40 s gap, replace with the real `data-start` difference): `SEG = { a5s8: 0.000, a5s9: 21.460 }`; segment lengths 21.06, 11.72 s.
Cues (segment word time from `audio/<seg>.words.json`, comp time = SEG + t):
- A5-S8 0.00 "That": basemap, the three pins and their labels already on at frame 0 (the hook's picture returning), source line on, camera drifting. `/* THAT SATURDAY @0.00 */`
- A5-S8 1.08 "one": track draws T1 → T4 with the loop (1.08 to 2.60, power2.inOut). `/* ONE LOW @1.08 */`
- A5-S8 1.86 "warm": warm arrows draw W1, W2, W3 (0.15 s stagger, 0.7 s each), then stream. `/* WARM @1.86 */`
- A5-S8 4.84 "wrapped": cold arrows draw C1, C2, C3 (0.15 s stagger, 0.8 s each), then stream. `/* WRAPPED @4.84 */`
- A5-S8 6.28 "other.": chip "ONE STORM · TWO SIDES" in (`fromTo` autoAlpha 0, x -20 to 0, 0.4 s, back.out(1.4)). `/* OTHER @6.28 */`
- A5-S8 7.12 "Newark": Newark pin strong pulse (ring 34 to 90 px, 0.8 s). `/* NEWARK @7.12 */`
- A5-S8 8.80 "Pittsburgh": Pittsburgh pin pulse, white. `/* PITTSBURGH @8.80 */`
- A5-S8 10.44 "Today's": chip 1 out (`to` x -30, autoAlpha 0, 0.4 s, power3.in); arrows and track settle to 0.6 opacity; streaming continues. `/* TODAYS @10.44 */`
- A5-S8 17.48 "holiday": chip 2 "EVERY HOLIDAY DRIVE" in (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s, power3.out). `/* HOLIDAY @17.48 */`
- A5-S8 20.84 "miss." to A5-S9 0.00: chip 2 out (`to` autoAlpha 0, y -20, 0.4 s, power3.in) by A5-S9 0.00. `/* MISS @20.84 */`
- A5-S9 0.00 to 11.72: whole map group fades 1.0 to 0.25 (ease none) while the camera pushes 1.00 to 1.08; streaming arrows continue (motion every second); source line out at A5-S9 0.40. `/* ONE STORM @0.00 */`
- A5-S9 11.72 to +2.00: hold at 0.25, then fade to black over the last 0.8 s (the episode's end; the orchestrator sets the tail to match the title card).
Host: data-start = A5-S8 audio start, duration = SEG.a5s9 + 13.72 (35.18 s with the assumed gap). Root `id="g-a5-8-splitmap-root"`.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 6: compute every pin and track point from the formula by script and print them. Report any §4 vs §3 conflict (for example a label hit by an arrow) instead of choosing.
