# g-a3-3-lows-north · A3-S3 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Built on `g-a3-1-steering` (P-WIDE plate, ridge) and `g-intro-8-track` (HURDAT2 AL011900 fixes and storm ring, already in that comp) and `g-intro-4-wire-map` (the Havana arrow "Into the Gulf"). Copy after g-a3-1 passed its frame read.

## 0. Claim
Early that September a high settled off the middle and south Atlantic coasts; all month the storm systems riding the westerly winds stayed mostly north of the 45th parallel, about the latitude of Minneapolis. The Bureau's summary does not say why the storm never turned. The storm went on west-northwest across the Gulf, the road Belen had called from Havana.

## 1. Source
- MWR Sept 1900 pp. 377 to 378 (factcheck/a3-r1.md rows 8, 9, 11): "During the earlier days of the month a high area also settled off the middle and south Atlantic coasts"; lows "for the most part limited to that portion of the country north of the forty-fifth parallel" (whole month).
- 45th parallel through Minneapolis: row 11 (Wikipedia, SECONDARY).
- Row 10: the MWR never ties the lows to the track. NOTHING on screen may show cause.
- Track: HURDAT2 AL011900 as in g-intro-8 (its receipt lists the fixes). Belen: sources-cuba.md §1.

## 2. Datum, scale, orientation
- Part A (0.00 to 4.62): NOAA 1900 weather map still `media/candidates/a3/A3-S3_c2_noaa-weather-map-1900-09-04.jpg` (verifier pick pending; c3 = 6 Sep), full frame, slow push. The printed "HIGH" on the scan is the subject: a ring highlight `#d8a13a` 4 px around it, position measured on the scan by the builder (receipt names the box). If the scan's HIGH is not off the middle or south Atlantic coast, drop the ring and keep the plain push; report it.
- Part B (4.62 to end): P-WIDE plate (g-a3-1). Camera V-NORTH cx 1700, cy 600, s 0.36 for the lows; then V-GULF cx 1100, cy 1500, s 0.75 for the track (move 18.58 to 19.98, power2.inOut; use `logZoom`).
- Pins by formula: Minneapolis (-93.27, 44.98) = (605.7, -413.7); 45th parallel = plate Y -415.8; Galveston (468.0, 1216.2); Havana (1585.8, 1857.6).

## 3. Geometry
- Ridge: g-a3-1's ellipse moved to the MWR position: centre (lon -72, lat 33) = (2520, 831.6), radii 900 x 600, label "HIGH" on the HUD. No isobars, no pressure numbers.
- 45th parallel: dotted line `#93a3b2` 3 screen px, dash 6/10, full plate width at Y -415.8; label "45°N" Arial 700 22 px `#93a3b2` at its left end.
- Minneapolis pin 12 px `#f2f5f8`, label "MINNEAPOLIS" Arial 700 22 px tracking 3 right of the pin.
- Lows: three small "L" glyphs Arial Black 900 40 px `#7fb2e5` riding a westerly band (as g-a3-1's band, but held flat ABOVE the parallel, plate Y between -700 and -480, screen y 72 to 151 in V-NORTH), moving west to east along it. They never cross below the dotted line.
- Chip C1 "STAYED MOSTLY NORTH" centred x 960 top 150, tag "storm systems, all month" Arial 700 22 px `#93a3b2`.
- Track: g-intro-8's ring and past-track line, from the Sept 6 00Z fix to the Sept 8 12Z fix, stopping offshore at least 60 screen px short of the Galveston pin (landfall is A4's).
- Havana arrow: g-intro-4's arrow geometry exactly, lit `#d8a13a` with glow as the ring runs.
- Chip C2 "BELEN: INTO THE GULF" left edge x 1000, top 150, tag "Havana forecast" Arial 700 22 px `#93a3b2`.
- Source line top-left: Part A "NOAA Central Library · weather map, Sept. 4, 1900"; Part B "Monthly Weather Review, Sept. 1900, pp. 377-378 · track: NOAA HURDAT2 · Belen: NOAA AOML".

## 4. Must be true in the picture
1. No arrow, line or word connects the lows to the storm or implies they "failed" or "missed" it. No "why" text. The lows stay above the 45th parallel line in every frame.
2. HIGH sits offshore of the middle and south Atlantic coasts (never inland, never labelled "Carolinas").
3. Minneapolis pin within 10 px of its formula point and on the dotted line within 4 px.
4. Track points from HURDAT2 within 10 px; ring stops offshore.
5. Nothing in x >= 1600, y >= 680 (the Havana arrow in V-GULF: Havana's screen point is 960 + (1585.8-1100)*0.75 = 1324, 540 + (1857.6-1500)*0.75 = 808; the pin and arrow tail sit left of 1600: check it).

## 5. Text and cues (a3-s3.words.json, segment 23.70 s)
- 0.00: Part A scan, source line.
- 1.54 ("high") /* HIGH @1.54 */: ring highlight draws around the scan's HIGH.
- 4.62 ("All month") /* ALL MONTH @4.62 */: dissolve 0.5 s to Part B, ridge and HIGH label already on.
- 5.94 ("systems"): lows begin moving east along the northern band.
- 7.88 ("mostly") /* MOSTLY @7.88 */: C1 in.
- 9.78 ("45th") /* 45TH @9.78 */: dotted line draws west to east 9.78 to 10.80; "45°N" label in.
- 12.08 ("Minneapolis") /* MINNEAPOLIS @12.08 */: pin and label pop.
- 13.20 ("The Bureau's"): C1 out by 13.80. Hold (lows keep moving) through 18.58.
- 18.58 to 19.98: camera to V-GULF.
- 19.98 ("west") /* WNW @19.98 */: ring runs the track 19.98 to 21.80; Havana arrow lights at 22.40 ("Belen").
- 22.40 /* BELEN @22.40 */: C2 in.
- Host 0.00 to 23.70 plus land time (cap 24.7).

## Motion for the whole window
13.80 to 18.58 has no new text: the lows' travel and a slow camera drift fill it (gap under 5 s, mover always present).

## Exit
Cut to A3-S4 (steamer stand-in): C2 slides out, root fade 0.3 s.

## Footage under it
Part A only: the NOAA 4 Sep 1900 map scan (A3-S3_c2). Part B is a full-frame map.
