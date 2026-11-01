# g-a1-2-bearmtn: the gust that beat Newark's (A1-S2)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, projection, pin style), bars from `library/inhouse/ranked-bars.html`. Prefix every id and class `bm2-`. g-a1-4 copies this file, so build the map panel and the whole ladder (all 8 slots, empty) here.
Sits over: nothing. Full-frame designed map + chart on track 2.

## 0. Claim
Near New York City one gust beat Newark's 108 mph: 140 mph at Bear Mountain, a state park on the Hudson north of the city (closes loop L4).

## 1. Source
`research/nws-facts.md` §1 JKL (P): "A 140 mph gust was recorded at Bear Mountain, just north of the New York City"; "Newark, NJ recorded a 108 mph wind gust". Source line "NWS Jackson KY".

## 2. Datum, scale, orientation
- Map panel x 0 to 820: frame A1-N, s 0.058, frame top-left (81836.7, 19751.4) map units, north up. Pins (screen px): Newark (467,761), Bear Mountain (504,575), Central Park (513,746) (drawn in g-a1-4 only), Albany (560,140) and Allentown (178,804) (drawn in g-a1-4 only). Panel right edge fades to `#04070c` over x 700 to 820.
- Hudson River polyline (screen px): Battery (501,773), Yonkers (528,698), Tappan Zee (532,653), Bear Mtn Bridge (509,572), Newburgh (503,513), Poughkeepsie (519,449), Kingston (515,374), Albany (560,140); 3 px `#5a768f`.
- Ladder: `briefs/a1/_list.md` "The gust ladder", 3.5 px per mph from x 900. Only the Newark and Bear Mountain rows are drawn in this comp; other slots stay empty (not drawn, not placeholders).

## 3. Geometry (px, 1920 x 1080)
- Basemap: state outlines 1.5 px `rgba(255,255,255,.14)`, land `#0b1016`, water `#04070a`; no state names.
- Newark pin: 16 px dot `#7fb2e5`, pulse ring every 1.5 s; label "NEWARK" Arial 700 22 px `#f2f5f8` tracking 3, right-aligned, 20 px left of the pin (ends x 447).
- "?" marker: 64 px circle, 3 px stroke `#d8a13a`, "?" Arial Black 900 52 px `#d8a13a` centred (the same marker that ended g-intro-5). It rides the Hudson polyline from Yonkers (528,698) to Bear Mtn Bridge (509,572) by per-leg `attr`/x-y tweens (no MotionPathPlugin), then resolves.
- Bear Mountain pin: 18 px dot `#f2f5f8`, 2 px ring `#7fb2e5`; label "BEAR MOUNTAIN, NY" Arial 700 26 px `#f2f5f8` tracking 3, left edge 44 px right of the pin (x 548 to about 800, y 575; the river runs at x 503 to 532 here, so the label clears it); sub "STATE PARK ON THE HUDSON" Arial 700 19 px `#93a3b2` under it.
- Ladder header "PEAK GUSTS · MPH" (left 900, top 70). Newark row: bar y 440, x 900 to 1278, `#7fb2e5` at 35 % (dim, it "returns" from I1-S4), name `NEWARK, NJ`, value `108 MPH` at x 1296. Bear Mountain row: bar y 330, x 900 to 1390, `#7fb2e5` full, name `BEAR MOUNTAIN, NY`, value `140 MPH` at x 1408 (ends about 1640, y 330: fine, outside the circle corner).
- A thin vertical guide at x 1278 (Newark's bar end), 1 px dashed `rgba(255,255,255,.3)`, y 300 to 470, so the eye sees the Bear Mountain bar pass it.
- Source line "Source: NWS Jackson KY" left 110, bottom 90; "Basemap: Natural Earth" left 110, bottom 60.
- Tiers: 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Bear Mountain bar length / Newark bar length = 140 / 108 = 1.296 (490 px / 378 px), ±4 px.
2. The Bear Mountain pin is on the Hudson's west bank north of the city: north of Central Park's latitude by 171 px on screen, never on the city.
3. "140 MPH" appears once (the bar's value label); "108 MPH" appears once.
4. No line joins the Newark pin to Bear Mountain (the "?" travels along the river, it draws no trail).
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a1-s2.words.json`, seconds from A1-S2 start)
Text: `NEWARK` · `BEAR MOUNTAIN, NY` · `STATE PARK ON THE HUDSON` · `PEAK GUSTS · MPH` · `NEWARK, NJ` · `108 MPH` · `BEAR MOUNTAIN, NY` (row name) · `140 MPH` · `?` · `Source: NWS Jackson KY` · `Basemap: Natural Earth`
Note: "BEAR MOUNTAIN, NY" is both the pin label and the row name: one label on two different things; declare `data-repeat-ok="pin label and ladder row name"` on the row name leaf after a frame read (no digits, so the gate does not count it; the declaration is for the reader).
- 0.00: map panel, Newark pin + label, ladder header, Newark row (dim) all on from frame 0; map drifts scale 1 to 1.03 over the host (ease none). `/* NEAR @0.00 */`
- 1.54 "gust": "?" in at Yonkers (528,698) (`fromTo` scale 0.6 to 1, autoAlpha, 0.35 s, back.out(2)), pulse every 1.0 s. `/* GUST @1.54 */`
- 2.16 "Newark's.": Newark row brightens to 70 % for 0.6 s, back to 35 %. `/* NEWARKS @2.16 */`
- 3.70 "Bear": "?" slides up the river to Bear Mtn Bridge (509,572), legs through Tappan Zee, 0.9 s, power2.inOut. `/* BEAR @3.70 */`
- 4.60: "?" morphs to the pin (circle scale 1 to 0.3, "?" autoAlpha 0, pin `fromTo` scale 0 to 1, back.out(2), 0.35 s) at (504,575). `/* MOUNTAIN @3.94, settles 4.60 */`
- 4.98 "state": pin label in, then sub at 5.86 "Hudson" (`fromTo` x -20 to 0, autoAlpha, 0.4 s). `/* STATE @4.98 */ /* HUDSON @5.86 */`
- 6.66 "New York": Hudson polyline south of the pin brightens toward the Battery (0.5 s), then back. `/* NEWYORK @6.66 */`
- 7.96 "140": Bear Mountain bar `scaleX` 0 to 1 (transformOrigin left center, 0.7 s, power4.out), passing the guide at x 1278; value `140 MPH` counts 0 to 140 on a leaf (power3.out, 0.7 s) opening at "1"; pin pulse ring doubles in size once. Sound hit here. `/* 140 @7.96 */`
- 8.70 to end: bar end glow pulses (finite repeats), pin pulses; map drift continues.
- Exit: none; ends on a cut to g-a1-3 (full-frame scene).
Host: data-start = A1-S2 start, duration = 9.610 + 0.40 = 10.01 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
