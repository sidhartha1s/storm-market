# g-a1-5-ct: Bridgeport under water, Hartford's 100 mph gusts (A1-S7)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, pins), water gauge from `library/inhouse/then-now-scale.html`. Prefix every id and class `ct5-`.
Sits over: nothing. Full-frame designed map on track 2.

## 0. Claim
On the Connecticut coast the Bridgeport weather station was under 4 to 5 ft of water, and its report called this the worst storm there since the 1938 hurricane; inland Hartford, about 35 miles from the shore, logged gusts of 100 mph (at least three times, 4:30 to 7:30 pm). Opens loop A1c (the cost in lives, paid in S11).

## 1. Source
`factcheck/a1-r1.md` (all SECONDARY, NBC Connecticut quoting Weather Bureau reports, https://www.nbcconnecticut.com/news/local/the-great-southeast-of-1950/26557/): row 32 Bridgeport "Station inundated with 4 to 5 feet of water"; row 31 "Storm of Nov. 25th worst since 1938" (the storm, not a gust); row 28 Hartford about 35 miles from the nearest Sound shore (computed); row 29 Hartford "gust speeds of at least 100 m.p.h. on at least 3 occasions between 4:30 and 7:30 p.m." Source line "Source: Weather Bureau reports via NBC Connecticut".

## 2. Datum, scale, orientation
- Map: frame A1-C, s 0.18, frame top-left (90113.4, 25949.7), north up. Pins (screen px): Bridgeport (640,800), Hartford (997,210), New London (1394,623, outline only, not labelled). Long Island Sound below the Connecticut shore, Long Island outline at the bottom edge.
- Station gauge inset (Bridgeport): 0 to 6 ft over 300 px (50 px per ft); 4 to 5 ft band = 200 to 250 px above the inset floor.
- Gust strip (Hartford): time axis 4:00 PM to 8:00 PM over 480 px (2 px per minute); "100 MPH" line at a fixed height; ticks are schematic in time (the report says "at least 3 occasions" between 4:30 and 7:30, not when).

## 3. Geometry (px, 1920 x 1080)
- Basemap: land `#0b1016`, water `#04070a`, outlines 1.5 px `rgba(255,255,255,.14)`; state label "CONNECTICUT" Arial 700 26 px `#93a3b2` tracking 8 at (760, 420).
- Shore line highlight: the Connecticut coastline drawn 3 px `#7fb2e5` along its length (dash draw).
- Bridgeport pin: 16 px dot `#f2f5f8`, ring `#7fb2e5`; label "BRIDGEPORT" Arial 700 26 px `#f2f5f8` tracking 3, left of the pin (right edge x 616, y 800).
- Station inset (glass card, left 110, top 470, 380 x 420): a 1950s weather-station silhouette (flat roof, door, instrument mast; `#4a5560` lines) standing on the inset floor y 850; water rect from the floor rising to 225 px (4.5 ft midpoint) with a 25 px lighter band 200 to 250 px marking the 4-to-5 ft range; waterline wave (x drift 30 px/s, finite repeats). Ft ticks at 0, 2, 4, 6 on the inset's left (Arial 700 19 px `#93a3b2`). Chip under the inset title: "STATION FLOODED" Arial 700 26 px `#f2f5f8` + "4 TO 5 FT" Arial Black 900 58 px `#7fb2e5`, top of the inset (y 490 to 590).
- Chip "WORST SINCE 1938": glass card, title zone left 110, top 90: Arial Black 900 52 px `#f2f5f8`; sub "BRIDGEPORT STATION REPORT" Arial 700 22 px `#93a3b2` tracking 6.
- Hartford pin: 16 px dot `#f2f5f8`, ring `#7fb2e5`; label "HARTFORD" Arial 700 26 px LEFT of the pin (right edge 24 px left of the dot), so it never meets the gust card that opens at x 1100. A dashed 2 px `#93a3b2` line from Hartford straight down to the nearest shore point (Guilford/Madison, lat 41.28, lon -72.68 = screen (996, 696)) with no label (the narration says 35 miles; a computed distance, kept off screen).
- Gust strip (glass card, left 1100, top 300, 600 x 330; ends y 630, above the circle corner): clock chip at the card top "4:30 PM TO 7:30 PM" Arial Black 900 52 px `#f2f5f8` (two lines if it overflows: "4:30 PM" / "TO 7:30 PM"); time axis y 590 from x 1160 to 1640, ticks "4:30", "7:30" Arial 700 19 px `#93a3b2` at x 1220 and 1580; "100 MPH" dashed line y 470 across the strip, label "100 MPH" Arial 700 22 px `#e74c3c` at its left end above the line. Three gust spikes (2 px `#7fb2e5` polylines from the axis up past the line to y 440) at x 1290, 1410, 1520.
- Source line "Source: Weather Bureau reports via NBC Connecticut" left 110, bottom 90; "Basemap: Natural Earth" bottom 60.
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Bridgeport pin on the shore; Hartford pin inland, 486 px north of the shore line (35 mi at this scale: 35 mi = 56.3 km; the formula gives 486 px between Hartford and the Guilford shore point, ±10).
2. The water in the inset stands between the 4 ft and 5 ft ticks (200 to 250 px above the floor), never above 5 ft.
3. "WORST SINCE 1938" is set as the station report's ranking of the storm, never a gust.
4. All three spikes cross the 100 MPH line and lie between the 4:30 and 7:30 ticks; no spike carries its own number.
5. Nothing in x >= 1600, y >= 680 (New London outline at (1394,623) carries no label; the gust card ends y 630).

## 5. Panel text (exact) and cues (`audio/a1-s7.words.json`, seconds from A1-S7 start)
Text: `CONNECTICUT` · `BRIDGEPORT` · `STATION FLOODED` · `4 TO 5 FT` · `0` `2` `4` `6` (inset ticks) · `WORST SINCE 1938` · `BRIDGEPORT STATION REPORT` · `HARTFORD` · `4:30 PM TO 7:30 PM` · `4:30` · `7:30` · `100 MPH` · `Source: Weather Bureau reports via NBC Connecticut` · `Basemap: Natural Earth`
Note: "4:30" and "7:30" on the axis repeat digits of the clock chip: one time on two things (axis ticks vs the chip); declare `data-repeat-ok="axis ticks under the clock chip"` on each tick leaf after a frame read.
- 0.00: map on, state label, slow drift (scale 1 to 1.04 over the host). `/* ON @0.00 */`
- 0.24 "Connecticut": coastline draws (1.2 s). `/* CONNECTICUT @0.24 */`
- 2.24 "Bridgeport": pin + label in. `/* BRIDGEPORT @2.24 */`
- 2.94 "under": inset in (`fromTo` x -60 to 0, autoAlpha, 0.6 s, power3.out); water rises from 0 to 225 px (1.2 s, power2.out). `/* UNDER @2.94 */`
- 3.18 "4": chip lines "STATION FLOODED" / "4 TO 5 FT" in. `/* 4 @3.18 */`
- 5.38 "called": inset exits (x -60, autoAlpha 0, 0.5 s, power3.in); "WORST SINCE 1938" card in at 5.72 "this"; stamp punch scale 1.08 to 1 on 8.48 "1938". `/* THIS @5.72 */ /* 1938 @8.48 */`
- 10.02 "Inland,": camera eases north (map y +120 px, 1.0 s, power2.inOut; recompute pin screen positions by the same offset, Hartford ends at (997, 330), Bridgeport at (640, 920)); "WORST SINCE 1938" exits. `/* INLAND @10.02 */`
- 10.74 "Hartford": Hartford pin + label in. `/* HARTFORD @10.74 */`
- 11.46 "35": dashed line draws Hartford to the shore (0.8 s). `/* 35 @11.46 */`
- 14.28 "weather bureau": gust card in (slide from x +200, autoAlpha, 0.6 s, power3.out); axis, ticks and the 100 MPH line draw. `/* WEATHER @14.28 */`
- 15.96 "100": three spikes flash up in turn (0.25 s each, 0.3 s apart), each with a white flash at its top. `/* 100 @15.96 */`
- 17.52 "So": spikes repeat their flash once more slowly (finite repeats) through the question; pins pulse. `/* SO @17.52 */`
- Exit: last 0.6 s: gust card slides out (x 980, autoAlpha 0, power3.in); map fades to ground. Cut to g-a1-6.
If the camera move makes §3 positions ambiguous, author the map in a group that translates and keep every label inside that group, so labels ride with their pins.
Host: data-start = A1-S7 start, duration = 20.399 + 0.40 = 20.80 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
