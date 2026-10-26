# g-intro-5-inland: the inland side, Pittsburgh, the cold going south, Bowling Green, back to Newark (I1-S2 to I1-S4)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `compositions/g-intro-2-hookmap.html` once built (basemap, projection, pin/label/chip styles; prefix `ii5-`). If not built yet: `library/inhouse/master-map-us-canada.html` with the styles in `briefs/intro/g-intro-2-hookmap.md` §3.
Sits over: nothing. Full-frame designed map on track 2. Overlays on track 3 above it: `g-intro-6-pbz-sheet` (I1-S2) and `g-intro-7-lmk-sheet` (I1-S3); this comp keeps its text out of their boxes in those windows (§3). Presenter circle may run: nothing with text or a highlight in x >= 1600, y >= 680.

## 0. Claim
Inland, Pittsburgh's snow was the city's biggest snowstorm on record; the cold reached a long way south, to Bowling Green, Kentucky at -7°F, still the November record there; and Newark's 108 mph was not the strongest gust. Loop L2 opens and closes inside this comp; L4 opens at the end with no place or number; L1 stays closed (no track, no low, nothing joining the pins).

## 1. Source
- Pittsburgh rank 1, 27.4 in, 24-26 Nov 1950: `research/nws-facts.md` §2 (PBZ snow.pdf); fact-check intro-r2 rows 21, 23.
- Cold reached a long way south: §3 NCEI (Pensacola 22°F, Birmingham 5°F, Atlanta 3°F, Asheville 1°F) and §6 "Cold reached FL, AL, GA, NC"; fact-check row 22.
- Bowling Green -7°F, 25 Nov 1950, still the all-November low: §3 JKL "Bowling Green (-7ºF)"; LMK PDF https://www.weather.gov/media/lmk/climate/clibwg/November_Records_Bowling_Green.pdf rows "25 74, 1896 -7, 1950" and "ALL-TIME 88, 1909 -7, 1950"; fact-check rows 24, 25, 27.
- Newark not the strongest: §1 Bear Mountain 140 mph (JKL), Mount Washington 160 mph (JKL, NCEI); fact-check row 28. Neither is named or numbered on screen here (paid in Act 1).
- The cold-air wash is SCHEMATIC: no source gives an isotherm or a boundary. It shows direction (south) and reach (Kentucky's latitude) only.

## 2. Datum, scale, orientation
North up. Projection: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213).
Map units: Newark (89893.2, 32871.1), LaGuardia (91039.4, 32641.0), Pittsburgh (67525.2, 34519.2), Bowling Green (42616.7, 53910.9), Louisville (45391.0, 46738.6).
Camera frames (screen = (map - top-left) × s):
- G (start, = g-intro-3-coast's map at its end): s 0.25, top-left (87599.4, 30481.0): LaGuardia (860, 540).
- H (Pittsburgh): s 0.04024, top-left (53608.7, 21596.7): Pittsburgh (560, 520), Newark (1460, 454).
- F (Kentucky): s 0.025, top-left (23416.7, 28310.9): Bowling Green (480, 640), Louisville (549, 461), Pittsburgh (1103, 155), Newark (1662, 114).
- D (Newark): s 0.04024, top-left (59078.1, 18954.6): Newark (1240, 560), Pittsburgh (340, 626).
G to H is a 6.2x pull-out with a westward pan: `logZoom`. H to F is a 1.6x pull-out plus a tilt south (pan); F to D is a 1.6x push plus pan east: plain eased tweens are fine (under ~1.5x each is close; use logZoom if the speed reads uneven).

## 3. Geometry (px)
- Basemap, pin, label and glass-chip styles exactly as g-intro-2 §3. Scan line for the whole comp.
- Frame G at 0: only the LaGuardia pin and "LAGUARDIA AIRPORT" label (they fade out during the pull-out, 0 to 0.6 s).
- Pittsburgh (frame H): pin fills snow white as in the hook; snow dots fall in a 90 px radius; label "PITTSBURGH" LEFT of the pin this time (right edge at x 536), so the area x >= 960 stays free for the PBZ sheet.
  - Keep-out for the PBZ sheet (track 3), I1-S2 1.8 to 5.1 s: box x 960 to 1580, y 150 to 660. No text of this comp in it. Newark's pin at (1460, 454) is inside: show the Newark dot only (no label, no chip) in frame H.
- Cold wash (frame H to F): a full-width rectangle in screen space on a layer under the pins, fill a linear gradient top to bottom: `#5a768f` at 0.45 above the leading edge, falling to 0 over 120 px at the edge. Its east side fades out over x 1150 to 1350 (horizontal gradient mask) so Newark and the coast stay outside it. The leading edge starts at y 0 and slides down to y 700 (frame F, about 40 px south of Bowling Green) by "south." A 2 px `#7fb2e5` line at 0.6 rides the leading edge. No text, no number, no pin named in this wash (L2).
- Bowling Green (frame F): ring `#93a3b2` then fill `#5a768f` with a `#7fb2e5` 3 px ring ("deep blue"); label "BOWLING GREEN, KY" right of the pin (x 504 to about 800, y 640); chip "-7°F" (glass, Arial Black 900 58 px `#7fb2e5`) under the label, box about x 504 to 700, y 670 to 750. Louisville appears as a plain dot only (no label) for context, or not at all; never labelled.
  - Keep-out for the LMK sheet (track 3), I1-S3 5.8 to 10.2 s: box x 960 to 1580, y 150 to 660. Pittsburgh (1103, 155) and Newark (1662, 114) in frame F show dots only, no labels.
- Newark (frame D, I1-S4): pin wind blue with pulse, label "NEWARK" left of the pin, chip "108 MPH" (Arial Black 900 58 px `#f2f5f8`, glass) 30 px below-left of the pin: box about x 920 to 1200, y 600 to 680. Pittsburgh pin white at (340, 626), label "PITTSBURGH" right of it. Bowling Green and the cold wash fade out during the F to D move.
- Unnamed marker (I1-S4): a HUD element, not a map point (it must not sit on a real place): a 64 px circle, 3 px stroke `#d8a13a`, centred at (1700, 170), with a "?" Arial Black 900 52 px `#d8a13a` centred in it. Pulse ring 64 to 120 px, opacity 0.8 to 0, 0.9 s, repeating every 1.0 s to the end. No leader line, no label, no number.
- Type tiers: big 58 (chips), mid 26 (place labels), small 19: a basemap credit "Basemap: Natural Earth" Arial 700 19 px `#93a3b2` at left 110, bottom 60, on for the whole comp (honest small text; no invented copy).

## 4. Must be true in the picture
1. L1: no line, band or shading joins any two pins; no track, low symbol, front teeth, isobar or wind arrow. The cold wash has no teeth and no attachment to any pin, and stops short of the coast (Newark and the shore outside it).
2. L2: until I1-S3 "Bowling" (2.66), no Kentucky place is named and no temperature is shown.
3. Bowling Green pin is at (480, 640) in frame F, ±10 px; Louisville is north-east of it; Pittsburgh is north-east of both.
4. Text never sits inside the sheet keep-out box during the sheet windows.
5. One reading target at a time: when the "-7°F" chip is up, nothing else at full opacity; during the LMK sheet window the "-7°F" chip dims to 0.35.
6. "108 MPH" appears once; the "?" marker carries no name, no number and no position on the land.
7. Nothing with text or a highlight in x >= 1600, y >= 680 in any frame.

## 5. Panel text (exact) and cues
Text strings: `Basemap: Natural Earth` · `LAGUARDIA AIRPORT` (carried in, then out) · `PITTSBURGH` · `BOWLING GREEN, KY` · `-7°F` · `NEWARK` · `108 MPH` · `?`
Segment offsets (comp-local, assumes 0.40 s gaps; replace with the real `data-start` differences):
`SEG = { i1s2: 0.000, i1s3: 7.723, i1s4: 18.099 }` ; segment lengths 7.323, 9.976, 2.021 s.
Cues (segment word time from `audio/<seg>.words.json`; comp time = SEG + t):
- I1-S2 0.00 "On": frame G; pull-out G to H starts (logZoom, 1.4 s, expo.inOut). `/* ON @0.00 */`
- I1-S2 1.42 "Pittsburgh": pin white fill sweep, snowfall, "PITTSBURGH" label in. `/* PITTSBURGH @1.42 */`
- I1-S2 2.04 to 4.58: PBZ sheet window (g-intro-6, its own cues). This comp: Pittsburgh pin pulses every 1.2 s, slow 1.5 % drift. `/* SHEET @2.04-4.58 */`
- I1-S2 5.12 "cold": tilt H to F starts (1.8 s, power2.inOut); cold wash leading edge starts sliding south. `/* COLD @5.12 */`
- I1-S2 6.94 "south.": leading edge reaches y 700 (frame F). `/* SOUTH @6.94 */`
- I1-S3 1.64 "Kentucky.": Kentucky's state outline brightens to `#93a3b2` 2 px (0.4 s), no label. `/* KENTUCKY @1.64 */`
- I1-S3 2.66 "Bowling": Bowling Green ring + "BOWLING GREEN, KY" label in. `/* BOWLING @2.66 */`
- I1-S3 3.54 "seven": pin fills deep blue (0.4 s sweep), chip "-7°F" in (`fromTo` autoAlpha 0, scale 0.85 to 1, 0.4 s, back.out(1.6)). `/* SEVEN BELOW @3.54 */`
- I1-S3 5.98 "checked": "-7°F" chip dims to 0.35; LMK sheet window (g-intro-7) runs to about 10.2. `/* CHECKED @5.98 */`
- I1-S4 0.00 "and": cold wash, Bowling Green, label and chip out (0.4 s); move F to D (0.8 s, power2.inOut). `/* AND @0.00 */`
- I1-S4 0.80: "NEWARK" label and "108 MPH" chip in after the move settles (0.25 s). `/* NEWARKS @0.14, shown on settle 0.80 */`
- I1-S4 1.22 "strongest": "108 MPH" chip dims to 0.35 (0.35 s). `/* STRONGEST @1.22 */`
- I1-S4 1.56 "one.": "?" marker in (`fromTo` scale 0.6 to 1, autoAlpha, 0.35 s, back.out(2)) and pulses to the end. `/* ONE @1.56 */`
Host: data-start = I1-S2 audio start, duration = SEG.i1s4 + 2.021 (20.12 s with the assumed gaps). It ends on the cut to the chapter blackout (a full-frame scene may end on a cut); the scan line and the "?" pulse keep moving to the last frame.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6: print every pin's screen position per frame from the formula. Item 5: check frames at I1-S2 3.0 and I1-S3 8.0 with both sheet overlays mounted: no map text under the sheets.
