# g-a2-1-columbus: Columbus at noon, Saturday 25 Nov 1950 (A2-S1)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, projection, pin style) for the ground; the RHS row panel of `library/inhouse/stat-panel.html` (ep2 anatomy values in mg-quickref "RHS stat panel"). Prefix every id and class `c1-`.
Sits over: nothing. Full-frame designed map on track 2, ground on from frame 0 (the chapter blackout before A2 ends on this frame).

## 0. Claim
At noon on Saturday 25 Nov 1950 Columbus, Ohio had 10°F air, an 18 mph wind, a wind chill of -8°F and half a mile of visibility in blowing snow, while Newark was gusting (closes loop A1).

## 1. Source
`research/nws-facts.md` §3 ILN "Columbus 25 Nov (Snow Bowl) | noon 10F, wind 18 mph, wind chill -8F, visibility 1/2 mi" (NWS Wilmington OH, https://www.weather.gov/iln/19501125, P). `factcheck/a2-r1.md` rows 1 to 3 CONFIRMED (KCMH table, "Snow & Blowing Snow").

## 2. Datum, scale, orientation
Camera frame A2-C (`briefs/a2/_list.md`): s 0.10, frame top-left (48991.0, 31596.7) map units, Columbus pin at screen (700, 560). Columbus lat/lon 39.9612, -82.9988 = map (55991.0, 37196.7). North up. No other place labelled.

## 3. Geometry (px, 1920 x 1080)
- Frame 0 (handoff from A1-S12's split screen): the map ground is clipped to the right half (clip-path inset 0 0 0 960px) with Columbus pin at (1180, 560) (the same pin, shifted +480 px), a 2 px `rgba(255,255,255,.14)` seam at x 960, left half `#04070c`. If A1-S12's comp, once briefed, puts its Columbus pin elsewhere, the orchestrator gives the coordinate and only frame 0 changes.
- 0.00 to 1.60: clip opens to full frame (clip-path inset 960 to 0, 1.4 s, power3.inOut) while the map layer slides x -480 (pin 1180 to 700), same tween. Seam fades with it.
- Pin: 18 px white dot `#f2f5f8`, 2 px ring `#7fb2e5`, pulse ring scale 1 to 2.4, autoAlpha .6 to 0, every 1.5 s (finite repeats to the end). Label "COLUMBUS, OHIO" Arial 700 26 px `#f2f5f8` tracking 4, 22 px right of the pin, vertical centre on the pin.
- Snow: 70 flakes (2 to 5 px white circles, opacity .35 to .8) on a full-frame layer under the HUD, falling 60 to 120 px/s with x drift +40 to +90 px/s (wind from the west-northwest), each a GSAP tween with finite repeats covering the host; seeded positions (no Math.random at seek time: precompute in a fixed array).
- Clock chip (title zone, top-left): glass card left 110, top 90, padding 18 x 28, radius 28. Line 1 "NOON" Arial Black 900 58 px `#f2f5f8`; line 2 "SAT, NOV 25" Arial 700 22 px `#93a3b2` tracking 6. Card about 300 x 130.
- Condition panel (RHS, mg-quickref RHS stat panel values but width 700): right 0, top 0, bottom 0, gradient `linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`, padding 150px 96px 0 170px. Four rows, each: value Arial Black 900 58 px `#f2f5f8`, label under it Arial 700 22 px `#93a3b2` tracking 4, row pitch 120 px, first row value baseline about y 210. Rows must end above y 680 (last row bottom about y 630) so the circle corner stays clear.
  - row 1 value "10°F", label "AIR TEMPERATURE"
  - row 2 value "18 MPH", label "WIND"
  - row 3 value "-8°F", label "FEELS LIKE" (value colour `#7fb2e5`)
  - row 4 value "1/2 MILE", label "VISIBILITY"
- Source line: "Source: NWS Wilmington OH" Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 90; basemap credit "Basemap: Natural Earth" at left 110, bottom 60.
- Tiers: 58 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Columbus pin at (700, 560) ±10 px from 1.60 s to the exit; no other town named.
2. Rows reveal in spoken order 10°F, 18 MPH, -8°F, 1/2 MILE, each on its word, never before.
3. The edit_script chip "FEELS LIKE -8°F" is set as value "-8°F" + label "FEELS LIKE" (same words, value line kept big); "WIND 18 MPH" as "18 MPH" + "WIND"; "VISIBILITY 1/2 MILE" as "1/2 MILE" + "VISIBILITY". Nothing else on screen.
4. No line, arrow or shading toward the east (L1 open); Newark is not drawn.
5. Nothing in x >= 1600, y >= 680; panel text right edge <= 1824.

## 5. Panel text (exact) and cues (`audio/a2-s1.words.json`, seconds from A2-S1 start)
Text: `COLUMBUS, OHIO` · `NOON` · `SAT, NOV 25` · `10°F` · `AIR TEMPERATURE` · `18 MPH` · `WIND` · `-8°F` · `FEELS LIKE` · `1/2 MILE` · `VISIBILITY` · `Source: NWS Wilmington OH` · `Basemap: Natural Earth`
- 0.00 frame 0 as §3: half map, pin, label, clock chip already on, snow falling. `/* WHILE @0.00 */`
- 1.68 "Columbus": clip open completes (started 0.20, 1.4 s); panel slides in `fromTo` x 660 to 0, 0.7 s, power3.out. `/* COLUMBUS @1.68 */`
- 3.80 "noon": clock chip scale 1 to 1.06 to 1 pulse (0.4 s). `/* NOON @3.80 */`
- 5.32 "18": row 2 "18 MPH" in. `/* 18 @5.32 */` (rows `fromTo` autoAlpha 0, y 24 to 0, 0.4 s)
- 7.12 "10": row 1 "10°F" in. `/* 10 @7.12 */` Note: spoken order is wind then temperature; rows sit top-down 10°F, 18 MPH, -8°F, 1/2 MILE, so row 2 appears first, then row 1 above it. Keep the slots fixed (no reflow).
- 9.00 "8": row 3 "-8°F" in, value colour flash `#f2f5f8` to `#7fb2e5` 0.5 s. `/* 8 @9.00 */`
- 11.16 "half": row 4 "1/2 MILE" in; snow layer density rises (second flake set fades in .6 s), map ground dims to 70 % (visibility). `/* HALF @11.16 */`
- 12.74 "kept": hold, flakes and pin pulse keep moving. `/* KEPT @12.74 */`
- Exit: last 0.6 s of the host: panel `to` x 980, autoAlpha 0, 0.6 s, power3.in; clock chip `to` x -60, autoAlpha 0; map fades to `#04070c` with it (hard cut to g-a2-2 card).
Host: data-start = A2-S1 start, duration = 13.30 + 0.40 = 13.70 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
