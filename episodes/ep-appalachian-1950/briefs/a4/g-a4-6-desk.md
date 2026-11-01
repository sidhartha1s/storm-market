# g-a4-6-desk: one storm, and the forecasters drawing it by hand (A4-S11)
Builder: Opus 5.5, high effort. Depth: deep (the act's last full split map, a camera slide, a pencil that draws). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md`, then this brief.
Start from: a copy of the built `compositions/g-a4-2-southmap.html` (basemap, camera, cold fill, pins) at frame P0; else `library/inhouse/master-map-us-canada.html` set up as g-a4-1. RHS panel from `references/editing-patterns/ep2-stat-panel-anatomy.html` (quickref "RHS stat panel" values). Pencil line: catalog block `svg-stroke-trace` (dash length = ceil(len)+1). File `compositions/g-a4-6-desk.html`, prefix `a46-`.
Sits over: nothing. Full-frame designed scene on track 2; the chapter blackout follows it. Corner circle on: the panel's dark ground may sit under the circle, but no sheet, pencil, chip or text at x ≥ 1600, y ≥ 680.

## 0. Claim
All three sides of this one storm (hurricane wind on the coast, deep snow inland, record cold to the Gulf) came out of one system, and the forecasters of the day were drawing their maps by hand. The picture asks what those maps showed and does not answer (loop A4, paid in Act 5).

## 1. Source
- Split map facts: Newark 108 mph wind side (§1 JKL, hook), Pittsburgh snow side (§2 PBZ), cold to Pensacola (§3 NCEI), Buffalo 40s (§3 JKL); all spent earlier, no figures on screen here.
- Hand-drawn forecasts: AMS 2004, Kistler, Uccellini, Kocin (abstract, ams.confex.com/ams/84Annual/techprogram/paper_73168.htm; `research/maps-forecast.md` §2): "At the time of the storm, the manually derived forecasts of the day were unable to anticipate this extreme event" (`factcheck/a4-r1.md` rows 35, 36). Used here only for "drawing their maps by hand"; the "could not anticipate" finding is NOT shown (see §5 OFF block).
- Desk sheet: SCHEMATIC, NOT A REAL CHART. `media/candidates/a4/picks.md`: no era-right desk photo exists, so the desk is a self-made graphic.

## 2. Datum, scale, orientation
North up. Projection and frames: `_list.md`.
- Frame 0 = P0: s 0.012, top-left (-15129.9, 11692.7). Newark (1260,254), Pittsburgh (992,274), Buffalo (1043,110), Pensacola (659,945).
- P6: s 0.0105, top-left (9632.0, 0.8). Newark (843,345), Pittsburgh (608,362), Buffalo (653,219), Chicago (300,278), Pensacola (317,950). The map's east edge of interest (Newark) stays left of the panel's solid zone (x ≥ 1100).
- P0 to P6: 1.14x pull plus a pan, linear power2.inOut.

## 3. Geometry (px)
- Map layers (all SCHEMATIC, matching the shapes A3 and A4 used):
  - Wind side: coastal band from the Delaware Bay to Cape Cod, 60 km wide at map scale, `#7fb2e5` at 0.35; Newark pin wind blue, 16 px.
  - Snow side: the A3 snow-white fill (copy it from the A3 exit comp if built; else a band over WV, western PA and eastern OH, lat 38.5 to 42.0, lon -84.0 to -77.5, soft 40 px edge) `#f2f5f8` at 0.30; Pittsburgh pin snow white.
  - Cold side: the `_list.md` cold fill at edge lat 30.2 (fully drained to the Gulf); Kentucky and Southeast pins as 12 px blue dots at 0.6, Farmers grey.
  - Buffalo: orange pin with glow, the only warm spot.
  - No labels on the map: every pin is unlabelled in this comp (the narration names no place).
- RHS panel: quickref values (`right:0; top:0; bottom:0; width:820px; linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`), entering `fromTo(x:660 -> 0, 0.7, power3.out)`.
- Sheet (inside the panel): `#f4f0e6` (beige polaroid stock), 520 x 380 px, top-left (1060, 230), rotated -2° (set at 0 via `tl.set`, never CSS), a 1 px `#6b6257` border and a soft 18 px shadow. Faint printed grid: 1 px `#c8b98a` at 0.35, 40 px squares.
- Pencil isobars on the sheet: 4 hand-wobbly closed curves (pre-authored SVG paths, nested ovals, no letters, no numbers, no place names, no "L" or "H"), stroke `#2a2622` 1.8 px, opacity 0.8. They draw with stroke-dashoffset in order; the 4th stops at 60 % of its length and never closes (the unfinished map).
- Pencil: SVG, 300 x 20 px hexagonal body `#d8a13a`, a `#f4f0e6` wood cone and a `#2a2622` tip, angled 35°. Its tip rides the drawing head: per-leg `attr`/`x,y` tweens to the path's head points sampled at 8 times per curve (MotionPathPlugin is not bundled); assert tip-on-head at three times in the receipt. It stops with the line at "show?".
- Chip on the panel: glass, left 1060, top 130, "NOV 1950 FORECAST DESK" Arial Black 900 34 px `#f2f5f8`; an eyebrow line above inside the chip is not used.
- Basemap credit (left 110, bottom 60) on; no source line until the desk is in; then "Source: AMS 2004, Kistler, Uccellini, Kocin" Arial 700 20 px `#c8d3e0` at left 1060, top 660 (inside the panel, under the sheet; y < 680).
- Type tiers: this comp holds three text nodes only (chip, credit, source), below the flat-type threshold of 4.

## 4. Must be true in the picture
1. The three sides read at once in frame 0 to 2.0: blue coast band, white inland band, blue cold to the Gulf, and Buffalo orange in between; the cold fill never covers Buffalo or the coast band.
2. Nothing on the sheet states what the 1950 forecasts showed: no "L", "H", front, track, place, number or word. Unfinished curves only.
3. The pencil tip is on the drawing head whenever the line is drawing (±6 px), and both stop together at "show?" (7.70).
4. No text rides the slide: the chip lands only after the panel settles.
5. Nothing at x ≥ 1600, y ≥ 680 except panel ground (the sheet's bottom-right corner is at about (1580, 610) after rotation; check it).
6. The comp ends in a fade-through to black (the chapter blackout follows), never a hard vanish of one element.

## 5. Panel text (exact) and cues
Text: `NOV 1950 FORECAST DESK` · `Source: AMS 2004, Kistler, Uccellini, Kocin` · `Basemap: Natural Earth`
OFF block (not built unless the orchestrator overrules `_list.md` "Second S11 chip dropped"): a second glass chip under the first, "LATER RESEARCHERS:" Arial 700 22 px `#93a3b2` tracking 3 / "THE HAND-DRAWN FORECASTS COULD NOT ANTICIPATE IT" Arial 700 26 px `#dfe7ee`, two lines inside x 1060 to 1580; it would have no spoken word to land on.
Cues from `audio/a4-s11.words.json` (segment time = comp time):
- 0.00 "All": frame P0, layers on at 0.6; then each side brightens to full in turn: wind band 0.00, snow band 0.40, cold fill 0.80 (0.35 s each, power2.out), Buffalo glow pulse at 0.98 "one". `/* ALL OF THAT @0.00 */`
- 1.24 "storm,": all layers hold; one shared slow pulse of the three bands (0.4 s). `/* ONE STORM @1.24 */`
- 2.16 "and the": camera P0 to P6 (1.0 s, power2.inOut) and the panel slides in from the right (`fromTo` x 660 to 0, 0.7 s, power3.out, starting 2.30). `/* AND THE FORECASTERS @2.16 */`
- 2.96 "drawing": sheet in (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s, power3.out); chip "NOV 1950 FORECAST DESK" in at 3.10 (`fromTo` x 30 to 0, autoAlpha, 0.35 s); source line in at 3.30. `/* DRAWING @2.96 */`
- 3.40 "their maps": pencil in and curve 1 starts drawing (curves 1 to 3 from 3.40 to 6.30, ease none; curve 4 from 6.38 "What" to 7.70). `/* MAPS BY HAND @3.40 */`
- 4.14 "hand": the pencil lifts and drops once (tip y -6 to 0, 0.2 s) as curve 1 closes. `/* HAND @4.14 */`
- 7.70 "show?": line and pencil stop dead; the map bands dim to 0.4 (0.3 s). `/* SHOW @7.70 */`
- 7.70 to end: fade-through: the whole root goes to black (opacity 1 to 0 over the last 0.5 s of the host, power1.in) into the blackout.
Host: data-start = A4-S11 audio start, duration = 8.247 + 0.40 = 8.647 s (assumed gap); if the blackout's placement asks a different tail, the fade stays in the host's last 0.5 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6: pin anchors and the pencil head points computed by script and printed in the receipt. Report any §4 vs §3 conflict instead of choosing.
