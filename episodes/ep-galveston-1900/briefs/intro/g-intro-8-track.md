# g-intro-8-track · I1-S1 (8.10 on) + I1-S2 + I1-S3 · DEEP · Opus 5.5 high
Shared rules: `_shared.md`. Built on the base `g-intro-4-wire-map` (same plate, projection, pins, colours, wire layer): copy it only after the base passed its full-size frame read. Exemplar for the moving storm marker: `episodes/ep6-katrina-2005/compositions/g-track.html` (ring follows the track, camera clamp).

## 0. Claim
The storm crossed Cuba on September 4. Washington expected it to recurve northeast, the way many storms did at that latitude; it did not: on the 6th the steamer Louisiana passed through its centre in the eastern Gulf, and it kept coming across the Gulf toward Galveston while Washington's wire told Galveston what to expect.

## 1. Source
- Cuba on the 4th: MWR Sept 1900 (Stockman) "crossed northward over the western central part of Cuba during the 4th" (sources-cuba.md §4; factcheck-C/D I1-S1).
- Florida Straits afternoon of the 5th: AOML (sources-cuba.md §4).
- Recurve: AOML "The USWB forecasters expected the storm to recurve to the northeast, as many storms did near this latitude" (sources-cuba.md §3; factcheck-D I1-S2).
- Louisiana: MWR "On the 6th the Cromwell Line steamer Louisiana passed through the center of the hurricane in the middle-eastern part of the Gulf" (sources-cuba.md §4; factcheck-B I1-S5, factcheck-E I1-S4).
- Toward Galveston, landfall evening of the 8th: AOML (sources-cuba.md §4).
- Moore: Wikipedia "Bureau director Willis Luther Moore" (SECONDARY, factcheck-D I1-S2).
- Wire: as g-intro-4 (AOML decree); "Warning messages were received from the Central Office at Washington on September 4, 5, 6, 7, and 8" (MWR, Cline).
- TRACK GEOMETRY HAS NO RESEARCH ROW: the 6-hourly 1900 positions are not in `research/`. Take storm AL011900 from NOAA HURDAT2 (nhc.noaa.gov/data/hurdat), Sept 2 00Z to Sept 8 18Z, list every lon/lat and its plate px in the receipt, and check them against the four sourced anchors above (Cuba on the 4th west-central; Straits on the 5th; middle-eastern Gulf on the 6th; Galveston on the evening of the 8th). If HURDAT2 is not fetched, the track is labelled "Track: schematic" in the source line and passes only through the four anchors.

## 2. Datum, scale, orientation
Plate and projection exactly as g-intro-4 (`X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`; Galveston (468.0, 1216.2), Havana (1585.8, 1857.6), Washington (2066.4, 218.3)). Camera states (screen = 960 + (X - cx) * s, 540 + (Y - cy) * s):
- V-CUBA: cx 1800, cy 1900, s 0.85 (Havana at 778, 504).
- V-GULF: cx 1150, cy 1550, s 0.75 (Galveston 449, 290; Havana 1286, 771).
- V-WIRE: cx 1267, cy 1000, s 0.5 (as g-intro-4).
V-GULF to V-WIRE is 1.5x: use `logZoom`.
Comp-local time = (segment's narration data-start − host data-start) + word time (`_shared.md`). Host data-start = I1-S1 data-start + 8.10.

## 3. Geometry
- Storm marker: white ring 96 px, 6 px stroke `#f2f5f8` with glow (g-track's ring, smaller), moves only by GSAP along the HURDAT2 points (per-leg `attr`/x,y tweens; MotionPathPlugin is not bundled). Past track: solid line `#f2f5f8` 5 px behind the marker, drawn by strokeDashoffset as the marker moves; its head always under the marker (assert at three times, 7a).
- Day ticks on the past track: a 10 px dot at each 12Z position from Sept 2 to Sept 8, no date text except the two chips below.
- Washington's expected path (the "WASHINGTON ?" arrow, then resolved): dotted `#7fb2e5` 6 px (dots 2/14, round caps), from the Sept 5 Straits point, curving north then northeast to (-79.0, 31.0) = (1890.0, 1039.5), arrowhead 34 px. Phase 1 (I1-S1): only its first third is drawn, ending in a "?" glyph; label "Washington ?" Arial 700 30 px `#7fb2e5`. Phase 2 (I1-S2): drawn to its end; label changes to "Washington: recurve northeast" (a second pre-authored label swapped with autoAlpha, never written text).
- Havana's forecast arrow: the g-intro-4 arrow, same geometry and colour `#d8a13a`, label "Havana: into the Gulf".
- Chips (glass, `_shared.md` chip spec), placed on the HUD next to the point they name, settled before they enter:
  - "CROSSES CUBA · SEPT 4" beside the Sept 4 crossing point, above it, never over the ring.
  - "STEAMER LOUISIANA · SEPT 6" beside the Sept 6 position; a small ship glyph (`#e8c56a`, 40 px) sits on the track at that position and the ring passes through it.
- Lower-third (fixed HUD, `_shared.md` spec, bottom-left): "WILLIS MOORE" / "Chief, US Weather Bureau". In V-GULF the bottom-left of the screen is Mexico's land and the western Gulf with no labels: keep it so.
- Wire layer (I1-S3): exactly g-intro-4's two lines and three labels in V-WIRE, Havana line dark from its first frame, the "×" already on it.
- Source line top-left: I1-S1 part "Monthly Weather Review, Sept. 1900 · track: NOAA HURDAT2"; from I1-S2 "NOAA AOML, 2015 · Monthly Weather Review, Sept. 1900".

## 4. Must be true in the picture
1. Pins and every track point on their lon/lat by the formula within 10 px; receipt lists them.
2. The ring is over west-central Cuba (lon -84 to -80) when "CROSSES CUBA · SEPT 4" is on screen.
3. The Washington path bends to the northeast and ends over the Atlantic off Georgia or the Carolinas, never over the Gulf; the Havana arrow points northwest into the Gulf and never at Texas.
4. The real track follows neither arrow exactly: it runs west-northwest across the Gulf. At "It didn't" the Washington path fades out and the real track is the line that keeps growing.
5. The ring is in the middle-eastern Gulf (east of lon -90) when the Louisiana chip is up, and the ship glyph sits on the track.
6. The ring stops offshore, at least 60 px (screen, V-WIRE) short of the Galveston pin: landfall is not drawn here.
7. In V-WIRE only the Washington line is lit; the pulse arrives at Galveston on "Galveston".
8. One chip on screen at a time; the lower-third never overlaps a chip or a label; nothing in screen x >= 1600, y >= 680 in any settled state (check V-CUBA: Cuba's east end and the Sept 2 to 3 track sit right of x 1600; keep their labels out and report the circle-off span to the orchestrator).

## 5. Text and cues
I1-S1 (i1-s1.words.json), host opens at 8.10:
- 8.10 ("The storm") /* STORM @8.10 */: plate in V-CUBA, frame 0 already drawn; ring at the Sept 2 point; track grows Sept 2 to Sept 4, 8.10 to 9.90, ease none.
- 8.88 ("Cuba"): Cuba's outline stroke brightens (`#93a3b2` to `#dfe7ee`, 0.5 s).
- 9.90 ("4th" 9.90) /* 4TH @9.90 */: chip "CROSSES CUBA · SEPT 4" in; ring holds over Cuba, pulsing.
- 11.24 ("and"): chip out; ring moves on to the Sept 5 Straits point, 11.24 to 12.80.
- 13.00 ("different" 13.00) /* DIFFERENT @13.00 */: dotted Washington path draws its first third, 13.00 to 13.62, "?" and "Washington ?" land at 13.62 ("in mind" 13.62 to 13.80).
I1-S2 (i1-s2.words.json):
- 0.00 ("Willis") /* WILLIS @0.00 */: lower-third in. Camera V-CUBA to V-GULF 0.00 to 1.80 (plain ease, under 1.5x).
- 2.06 ("curve" 2.06) /* CURVE @2.06 */: Washington path draws to its end 2.06 to 3.40; label swap to "Washington: recurve northeast" at 2.80 ("northeast").
- 3.76 to 6.16 ("the way many storms did ... far north"): hold; lower-third out at 5.40; Havana arrow fades back in at 4.88 ("once").
- 7.30 ("It" 7.30) /* DIDN'T @7.46 */: at 7.46 the Washington path and its label fade to 0 over 0.6 s; the ring moves northwest, then west-northwest, along the real track, 7.46 to 9.30 (Sept 5 to Sept 6 point); the Havana arrow dims to 0.5.
- 9.44 ("Louisiana" 9.44): ship glyph and chip "STEAMER LOUISIANA · SEPT 6" in.
- 11.10 ("center" 11.10): the ring is exactly on the ship glyph; the glyph flashes.
- 12.56 ("Gulf"): chip out over 12.30 to 12.90.
I1-S3 (i1-s3.words.json):
- 0.00 ("It kept coming") /* COMING @0.14 */: ring and track run on WNW, 0.00 to 2.18, stopping offshore of Galveston at "island" 2.18. Galveston pin pulses from 1.84 ("toward").
- 2.90 ("and"): camera V-GULF to V-WIRE, logZoom, 2.90 to 3.90; wire lines draw at 3.08 ("Washington's" 3.08), Havana line dark with its "×".
- 3.68 ("wire" 3.68): first pulse Washington to Galveston, arriving at 4.40 ("Galveston" 4.40), pin flash.
- 4.98 ("what to expect"): second pulse, arriving at 5.80.
- Host end: I1-S3 end 5.946 + land time to the cut into I1-S4 (default 6.80, capped by the I1-S4 narration start).

## Motion for the whole window
The ring pulses (scale 0.92 to 1.1, 0.9 s yoyo, finite repeats) for the whole host; the camera is always on a move or a slow drift (scale +2 % over any hold); the plate water carries a slow 2-layer noise drift if the builder wants it (optional). Longest gap between discrete beats is under 2.5 s.

## Exit
Fade-through: root to 0 over the last 0.4 s; I1-S4 opens on the MWR page.

## Footage under it
None: full-frame designed map. The edit script's "NOAA 1900 weather maps, September 2 to 4" are not the plate (no scan on disk; a 1900 projection would put the track by eye). Orchestrator option: mount the Commons Sept 4 1900 map still for 1.5 s before 8.10 and cross-dissolve into this plate.
