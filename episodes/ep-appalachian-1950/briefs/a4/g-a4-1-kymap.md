# g-a4-1-kymap: the cold slides south, Chicago to the Kentucky records (A4-S1 to A4-S3)
Builder: Opus 5.5, high effort. Depth: deep (camera moves, a growing fill, 8 pins). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md` (frames, pins, fill, pin style), then this brief.
Start from: `library/inhouse/master-map-us-canada.html`. Copy to `compositions/g-a4-1-kymap.html`; keep basemap paths, projection and the single camera group (svgOrigin based). Delete the Enderlin swath/track, survey points, RHS rail cards and every Enderlin label. Prefix every id/class `a41-`. Pin and chip styling as `compositions/g-intro-2-hookmap.html` (same episode).
Sits over: nothing. Full-frame designed scene on track 2, ground on from frame 0 (it opens out of the A3 to A4 chapter blackout). Corner circle on: nothing but basemap ground at x ≥ 1600, y ≥ 680.

## 0. Claim
The cold behind the front did not stop in Ohio: Chicago tied its all-time November low (-2°F, 24 Nov), and Louisville (-1°F), Lexington (-3°F) and Bowling Green (-7°F) set November records that still stand; of the Kentucky lows on the NWS Jackson list, only Farmers' 0°F has since been beaten.

## 1. Source (quoted, with rows)
- Chicago: `research/nws-facts.md` §3 JKL "Chicago dropped to -2ºF on the 24th equaling their all-time monthly low"; `factcheck/a4-r1.md` row 1 (24 Nov 1950 = the Friday after Thanksgiving).
- Louisville, Lexington, Bowling Green: §3 JKL "Louisville (-1ºF), Lexington (-3ºF) and Bowling Green (-7ºF) all recorded record lows for the month"; a4-r1 rows 4, 5.
- East Kentucky: §3 JKL "Middlesboro bottomed out at 3ºF, Williamsburg 1ºF, Farmers 0ºF and Somerset –2ºF"; "All but the 0ºF reading at Farmers still stand as record low temperatures for the month of November"; a4-r1 rows 8, 10.
- Cold sliding south: §3 JKL front passage "from the 40s and 50s ... to the teens just behind it"; a4-r1 row 3 (NCEI "all the way down into the far Southeast").
- Basemap: Natural Earth 50m admin-1 (public domain), inside the exemplar.

## 2. Datum, scale, orientation
North up, no rotation. Projection and pin map units: `_list.md`. Frames used (screen = (map - top-left) × s):
- P0: s 0.012, top-left (-15129.9, 11692.7). Chicago (640,178), Buffalo (1043,110); Kentucky pins crowd at (693..829, 421..531).
- P2: s 0.075, top-left (35150.0, 43405.3). Louisville (768,250), Farmers (1409,294), Lexington (1130,339), Somerset (1101,736), Bowling Green (560,788), Williamsburg (1229,882), Middlesboro (1356,939).
- P2s (last frame): s 0.075, top-left (35150.0, 43938.6): P2 with every pin 40 px higher. g-a4-2 opens on it exactly.
- P0 to P2 is a 6.25x push: `logZoom` from `library/inhouse/snippets/helpers.js`, never linear scale. P2 to P2s is a pan, ease none.

## 3. Geometry (px)
- Basemap as the exemplar: state fills `#0b1016` to `#15202b`, state lines `#2a3644` 1.2 px non-scaling, coastline `#4a5560` 1.6 px. Kentucky's state line stays the same as every other state (no highlight).
- Frame 0 = A3's last frame (see `_list.md` "Act 3 handoff"): if A3 leaves its cold-blue arrows and snow-white fill, they are on at frame 0; the arrows fade out 0.0 to 1.0 s while the cold fill takes over. The snow-white fill (if present) stays at 0.30 opacity under everything for the whole comp.
- Cold-blue fill: polygon, colours and feather in `_list.md`. Edge latitude per cue in §5; the edge never passes a pin later than that pin's blue turn.
- Pins: `_list.md` "Pin style". In P0 the Kentucky pins are NOT shown (they appear only after the push lands in P2). Buffalo's orange pin is on in P0 from frame 0 (it is left over from A3), with no label and no chip in this comp.
- Labels and chips (HUD layer, never scaled with the camera):
  - Chicago (P0): label "CHICAGO" centred above the pin, baseline 24 px above the dot. Chip LEFT of the pin, right edge at x 610, vertically centred on y 178: line 1 "-2°F" Arial Black 900 58 px `#7fb2e5`; line 2 "TIES ALL-TIME NOV LOW" Arial 700 22 px `#dfe7ee` tracking 3; line 3 "NOV 24" Arial 700 22 px `#93a3b2` tracking 3. Glass surface (tokens.md glass card values, radius 14, padding 10 x 18). Box about x 270 to 610, y 100 to 260: keep it clear of Buffalo (1043,110).
  - Bowling Green (P2): label "BOWLING GREEN" left of the pin (right edge 24 px left of the dot), value "-7°F" 52 px under the label, right-aligned to it; label and value at 0.5 opacity for their whole life (callback).
  - Louisville (P2): label "LOUISVILLE" left of the pin (right edge at x 744), value "-1°F" 52 px under it, right-aligned.
  - Lexington (P2): label "LEXINGTON" centred above the pin (bottom y 315), value "-3°F" 52 px centred under the pin (top y 365). Nothing right of Lexington: Farmers sits 279 px east.
  - Records chip (P2): glass, left 330, top 520, two lines: "NOVEMBER RECORDS" Arial Black 900 40 px `#f2f5f8`; "· STILL STANDING" Arial 700 26 px `#dfe7ee`. Box bottom ≤ 640, right ≤ 1000 (Somerset's label will sit at y 736 later).
  - East Kentucky (S3, small, Picture "small and fast"): one line each, label and value together, Arial 700 22 px `#dfe7ee` with the value in Arial Black 900 26 px `#7fb2e5`: "MIDDLESBORO 3°F" centred under its pin (top y 963); "WILLIAMSBURG 1°F" left of its pin (right edge 1205, centred y 882); "SOMERSET -2°F" left of its pin (right edge 1077, centred y 736); "FARMERS 0°F" right of its pin (left edge 1433, centred y 294). Pin core 12 px for these four.
  - Farmers greyed: pin fill and ring `#4a5560`; its label line turns `#93a3b2`; a small glass chip under it, left edge 1433, top 320: "RECORD SINCE BROKEN" Arial 700 22 px `#93a3b2` tracking 3. Right edge must stay ≤ 1824 and the box above y 680 (corner rule): it is at y 320 to 360.
- Source line "Source: NWS Jackson, KY" (left 110, bottom 92) and basemap credit (left 110, bottom 60), both on from frame 0.
- Scan line: the exemplar's `.mm4-scan` (2 px, 1180 px wide) top to bottom about 60 px/s, opacity 0.30, whole comp.
- Type tiers: 58/52 big, 40/26 mid, 22/20/19 small.

## 4. Must be true in the picture
1. Every pin sits where the formula puts it (±10 px against the `_list.md` frame table); Lexington is east of Louisville, Bowling Green south-west of both, Farmers north-east of Lexington, Middlesboro the most southern.
2. The cold-blue fill never covers Buffalo or anything east of the boundary in `_list.md` (Buffalo sat in the 40s). Its edge is above (north of) each pin until that pin's cue, and south of it after.
3. No number shows before its spoken word: "-2°F" not before "two" (S1 2.42), "-1°F" not before "one" (S2 3.94), "-3°F" not before "three" (S2 6.36), "3°F" not before "three" (S3 3.08), "0°F" not before "zero" (S3 8.18). "-7°F" is a callback and may show from its label cue.
4. One reading target at full opacity: when a new value lands, the previous chip dims to 0.6; Bowling Green stays at 0.5 throughout. Exception, by design: at "All three" (S2 7.48) the three Kentucky values brighten together to 1.0 for 0.8 s (Bowling Green to 0.8), then the records chip lands and they drop back to 0.6.
5. Farmers is the only grey pin; Middlesboro, Williamsburg, Somerset stay lit cold blue.
6. No text rides a camera move: every label or chip is fully out before a move starts and lands only after it settles.
7. The last frame equals P2s exactly: pins only (cold blue, Farmers grey, Bowling Green deep blue), no labels, no chips, cold fill edge at lat 36.4, source line and basemap credit on.
8. Corner x ≥ 1600, y ≥ 680 holds only basemap and fill in every frame.

## 5. Panel text (exact) and cues
Text strings: `CHICAGO` · `-2°F` · `TIES ALL-TIME NOV LOW` · `NOV 24` · `BOWLING GREEN` · `-7°F` · `LOUISVILLE` · `-1°F` · `LEXINGTON` · `-3°F` · `NOVEMBER RECORDS` · `· STILL STANDING` · `MIDDLESBORO 3°F` · `WILLIAMSBURG 1°F` · `SOMERSET -2°F` · `FARMERS 0°F` · `RECORD SINCE BROKEN` · `Source: NWS Jackson, KY` · `Basemap: Natural Earth`

Segment offsets (comp seconds; 0.40 s gaps assumed, replace with real `data-start` differences):
`SEG = { a4s1: 0.000, a4s2: 14.504, a4s3: 32.714 }` ; segment lengths 14.104, 17.810, 12.257 s.

Cues (segment-relative word times from `audio/a4-s*.words.json`; comp time = SEG + t):
- S1 0.00 "start": frame P0 (or A3's last frame, then a 1.2 s move to P0, power2.inOut). Cold fill edge starts at lat 42.5; Buffalo orange pin glowing (glow breathes 0.5 to 0.7, 2 s period, finite repeats). `/* START @0.00 */`
- S1 0.44 "Chicago,": Chicago pin turns cold blue (fill sweep top to bottom 0.5 s via a clip rect), label in; fill edge to lat 41.0 by 1.2 (power2.out). `/* CHICAGO @0.44 */`
- S1 2.42 "two": "-2°F" in (`fromTo` autoAlpha 0, scale 0.9 to 1, 0.4 s, back.out(1.4)), with the glass chip box. `/* TWO BELOW @2.42 */`
- S1 3.30 "tied": "TIES ALL-TIME NOV LOW" in (`fromTo` autoAlpha 0, x -16 to 0, 0.35 s, power3.out). `/* TIED @3.30 */`
- S1 7.70 "day": "NOV 24" in (same tween). `/* DAY AFTER THANKSGIVING @7.70 */`
- S1 9.16 "From": fill edge slides 41.0 to 38.6 over 9.16 to 12.20 (power1.inOut), front line bright 0.6 to 0.9 while moving. `/* FROM THERE @9.16 */`
- S1 11.70: Chicago chip and label out (`to` x -30, autoAlpha 0, 0.4 s, power3.in), done by 12.10.
- S1 12.32 "almost": push P0 to P2 starts (logZoom, 2.8 s, expo.inOut), arrives S2 0.70 (comp 15.204). Fill edge continues 38.6 to 37.6 during the push. `/* ALMOST NEVER @12.32 */`
- S2 0.78 "Seven": Bowling Green pin (deep blue) fades in to full with its label and "-7°F" at 0.5 (0.4 s, no pop: a callback, not a reveal). `/* SEVEN BELOW @0.78 */`
- S2 3.38 "Louisville": Louisville pin turns blue, label in. `/* LOUISVILLE @3.38 */`
- S2 3.94 "one": "-1°F" in (`fromTo` autoAlpha 0, y 16 to 0, 0.35 s, power3.out). `/* ONE BELOW @3.94 */`
- S2 5.60 "Lexington": Lexington pin turns blue, label in; Louisville value to 0.6. `/* LEXINGTON @5.60 */`
- S2 6.36 "three": "-3°F" in. `/* THREE BELOW @6.36 */`
- S2 0.70 to 7.50: fill edge 37.6 to 36.4 (ease none), so all three pins sit inside it before "All three".
- S2 7.48 "All": the three values brighten together (§4.4), each pin one pulse ring 30 to 60 px, 0.8 s. `/* ALL THREE @7.48 */`
- S2 8.34 "records": records chip in with "NOVEMBER RECORDS" (`fromTo` y 24 to 0, autoAlpha, 0.45 s, power3.out); values back to 0.6. `/* RECORDS @8.34 */`
- S2 12.40 "still": "· STILL STANDING" in. `/* STILL ON THE BOOKS @12.40 */`
- S2 14.48 "Louisville": Louisville pin one pulse ring. `/* LOUISVILLE2 @14.48 */`
- S2 13.0 to S3 0.00: slow 2 % camera drift (scale only, ease none) so the hold moves.
- S3 0.00 "Out": records chip, the three values and the Bowling Green label out (0.4 s, power3.in); Louisville, Lexington, Bowling Green labels stay at 0.45, pins stay. `/* OUT IN SOUTHEASTERN @0.00 */`
- S3 2.04 "Middlesbrough": Middlesboro pin drops in (`fromTo` y -30 to 0, autoAlpha, 0.3 s, back.out(2)), label part "MIDDLESBORO" in. `/* MIDDLESBORO @2.04 */`
- S3 3.08 "three": its value "3°F" in; then Williamsburg pin + "WILLIAMSBURG 1°F" at 3.30 and Somerset pin + "SOMERSET -2°F" at 3.45 (same drop tween, 0.25 s each). `/* THREE ABOVE @3.08 */`
- S3 4.50 "Only": the three new pins one pulse each, 0.15 s apart (they still stand). `/* ONLY ONE @4.50 */`
- S3 8.18 "zero": Farmers pin drops in, cold blue, with "0°F" (the "FARMERS" part waits). `/* ZERO @8.18 */`
- S3 9.56 "Farmer's.": "FARMERS" in; at 9.90 the pin and line grey out (fill colour tween 0.5 s) and "RECORD SINCE BROKEN" in (`fromTo` autoAlpha 0, y 12 to 0, 0.35 s). `/* FARMERS @9.56 */`
- S3 10.60 "The Deep South": every label and chip out (0.5 s, power3.in), pins stay; pan P2 to P2s (40 px down-screen, ease none) from 10.60 to comp end, fill front line pulses once. `/* DEEP SOUTH @10.60 */`
Host: data-start = A4-S1 audio start, duration = SEG.a4s3 + 12.257 + 0.40 = 45.371 s (assumed gaps). The cut to g-a4-2-southmap is a continuation on frame P2s, not a vanish.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6: compute every pin and label anchor from the formula and frame table by script and print them in the receipt. Report any §4 vs §3 conflict instead of choosing.
