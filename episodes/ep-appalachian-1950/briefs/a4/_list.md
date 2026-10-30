# A4 section graphics: ep-appalachian-1950 (A4-S1 to A4-S11, "The cold that went south")
Written 28 Oct 26 from `acts/a4.md` (same text as `edit_script.md`), `audio/a4-s*.words.json` and `.wav` lengths, `research/nws-facts.md` §3 and §5, `factcheck/a4-r1.md`, `media/candidates/a4/picks.md` (no footage for A4: every beat is a self-made graphic).
Every brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6-§8 by reference; read both before building. Pin and frame numbers below were computed by script (projection formula below), not placed by eye.

| comp id | segments | what it shows (one line) | depth | builder model | library exemplar to start from | sits over |
|---|---|---|---|---|---|---|
| g-a4-1-kymap | A4-S1, A4-S2, A4-S3 | Act map from the A3 exit: cold-blue fill spreads south, Chicago pin "-2°F", push into Kentucky: Bowling Green callback, Louisville and Lexington records, east-Kentucky pins, Farmers greyed "RECORD SINCE BROKEN" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (basemap, projection, camera rig); g-intro-2-hookmap for pins and chips | nothing: full-frame designed map (track 2) |
| g-a4-2-southmap | A4-S4, A4-S5 | Same map pulls out over the Smokies: Asheville 1°F, Atlanta 3°F, Birmingham 5°F, Buffalo's orange "40s" pin at the top, cold reaches the Gulf, Pensacola 22°F, Georgia and South Carolina crop rows frost white, chip "WIDESPREAD CROP DAMAGE" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html`; opens on g-a4-1's last frame | nothing: full-frame designed map |
| g-a4-3-toll | A4-S7 | Drained map fades to a dim field; calendar strip NOV 24 to NOV 30 fills; counter climbs to "160", "AT LEAST" / "LIVES LOST", source line | standard | Sonnet 5.5 high | `library/inhouse/numbers-rollup.html` (counter), basemap ground copied from g-a4-2's last frame | nothing: full-frame designed |
| g-a4-4-statemap | A4-S8, A4-S9 | State map shaded by toll tally, Ohio deepest, chip "OHIO · 64 TO 70", Columbus and Newark callbacks (no numbers), West Virginia "UP TO 18", Kentucky "UP TO 17", slide south, Alabama "13" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (admin-1 state paths); choropleth fill idea from catalog `us-map` | nothing: full-frame designed map |
| g-a4-5-homes | A4-S10 | Night street of house outlines in falling snow, windows go dark block by block, counter "1,000,000+" "HOMES WITHOUT POWER", then beige quote card "The costliest storm on record up until that time" attributed to NWS Jackson, KY | standard | Sonnet 5.5 high | `library/inhouse/numbers-rollup.html` (counter); `library/inhouse/quote-card.html` (beige cite card) | nothing: full-frame designed |
| g-a4-6-desk | A4-S11 | The full split map one last time (wind blue coast, snow white inland, cold blue to the Gulf, Buffalo orange), map slides left, a 1950 forecast-desk panel slides in: a sheet with a pencil drawing isobars that stops unfinished on "show?", chip "NOV 1950 FORECAST DESK" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (map), `references/editing-patterns/ep2-stat-panel-anatomy.html` (RHS panel), catalog `svg-stroke-trace` (pencil line) | nothing: full-frame designed map |

Count: 6 graphics. Deep 4 (Opus 5.5): g-a4-1, g-a4-2, g-a4-4, g-a4-6. Standard 2 (Sonnet 5.5 high): g-a4-3, g-a4-5.
A4-S6 (Paul on camera, ins-paul-5) gets no graphic: see "Paul's clip" below.

## Section-wide decisions (each brief repeats the part it needs)
- **Paul's clip (A4-S6).** The Picture line asks for the drained map "beside him (graphic, no prop)". Lane rule: Paul's full-frame clips get no graphic except the date/place popfig on the first clip, and quickref says a full-frame clip is its own shot, never composited with a graphic. So no comp is briefed for A4-S6. The drained map he would have stood beside is g-a4-2's last frame (frame P0, all pins blue, Buffalo orange), which is the cut straight before him. Flagged to the orchestrator; if the owner wants a side panel, it is a new brief and a Paul-clip prompt change (the clip would have to leave room), not a builder call.
- **Second S11 chip dropped.** "LATER RESEARCHERS: THE HAND-DRAWN FORECASTS COULD NOT ANTICIPATE IT" is not spoken in A4-S11 (the voice only asks "What did the maps on their desks show?") and it states the answer that loop A4 holds open until Act 5. Reveals follow the voice (Text doctrine), so g-a4-6 shows only "NOV 1950 FORECAST DESK". Its exact spec is kept in g-a4-6 §5 as an OFF block if the orchestrator overrules.
- **Unspoken pin values in A4-S3.** The Picture line asks for "WILLIAMSBURG 1°F" and "SOMERSET -2°F"; the voice names only Middlesboro and Farmers. Kept as the act asks (locked act), set small (22 px) and landing with Middlesboro's value, never before "three". Both are JKL figures (nws-facts §3 row "East KY lows").
- **Chip wording splits.** Long chips keep the edit_script words split into a big line and a smaller line: "-2°F" / "TIES ALL-TIME NOV LOW" / "NOV 24"; "NOVEMBER RECORDS" / "· STILL STANDING"; "WIDESPREAD CROP DAMAGE" / "GEORGIA · SOUTH CAROLINA" (edit_script "GA, SC" spelled out for TV); "OHIO" / "64 TO 70". New small value labels the voice speaks but the Picture line did not list: "UP TO 18" (West Virginia), "UP TO 17" (Kentucky), matching "as many as" in the voice (factcheck a4-r1 row 26).
- **One map, one coordinate system** (same as the intro briefs): map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213). Screen px = (map unit - frame top-left) × s. Pins are a HUD layer placed from the camera maths (constant screen size), never scaled with the map.

| pin | lat, lon | map units |
|---|---|---|
| Chicago | 41.8781, -87.6298 | (38203.4, 26490.8) |
| Buffalo | 42.8864, -78.8784 | (71817.5, 20859.4) |
| Newark | 40.7357, -74.1724 | (89893.2, 32871.1) |
| Pittsburgh | 40.4406, -79.9959 | (67525.2, 34519.2) |
| Columbus | 39.9612, -82.9988 | (55991.0, 37196.7) |
| Louisville | 38.2527, -85.7585 | (45391.0, 46738.6) |
| Lexington | 38.0406, -84.5037 | (50210.7, 47923.2) |
| Bowling Green | 36.9685, -86.4808 | (42616.7, 53910.9) |
| Farmers | 38.1468, -83.5352 | (53930.7, 47330.1) |
| Somerset | 37.0920, -84.6041 | (49825.1, 53221.1) |
| Williamsburg | 36.7434, -84.1597 | (51532.0, 55168.1) |
| Middlesboro | 36.6084, -83.7166 | (53234.0, 55922.0) |
| Asheville | 35.5951, -82.5515 | (57709.1, 61581.3) |
| Atlanta | 33.7490, -84.3880 | (50655.1, 71891.8) |
| Birmingham | 33.5186, -86.8104 | (41350.7, 73178.6) |
| Pensacola | 30.4213, -87.2169 | (39789.3, 90477.0) |

| frame | s | top-left (map units) | pins on screen (px) | used in |
|---|---|---|---|---|
| P0 (act master) | 0.012 | (-15129.9, 11692.7) | Chicago (640,178), Buffalo (1043,110), Newark (1260,254), Pittsburgh (992,274), Columbus (853,306), Louisville (726,421), Lexington (784,435), Farmers (829,428), Somerset (779,498), Bowling Green (693,507), Williamsburg (800,522), Middlesboro (820,531), Asheville (874,599), Atlanta (789,722), Birmingham (678,738), Pensacola (659,945) | g-a4-1 open, g-a4-2 end, g-a4-3 ground, g-a4-6 open |
| P2 (Kentucky) | 0.075 | (35150.0, 43405.3) | Louisville (768,250), Farmers (1409,294), Lexington (1130,339), Somerset (1101,736), Bowling Green (560,788), Williamsburg (1229,882), Middlesboro (1356,939) | g-a4-1 S2, S3 |
| P2s | 0.075 | (35150.0, 43938.6) | P2 with every pin 40 px higher | g-a4-1 last frame = g-a4-2 frame 0 |
| P4 (Southeast) | 0.015 | (-5316.0, 12192.7) | Buffalo (1157,130), Chicago (653,214), Newark (1428,310), Pittsburgh (1093,335), Columbus (920,375), Louisville (761,518), Farmers (889,527), Lexington (833,536), Somerset (827,615), Bowling Green (719,626), Williamsburg (853,645), Middlesboro (878,656), Asheville (945,741), Atlanta (840,895), Birmingham (700,915) | g-a4-2 S4 |
| P6 (map left) | 0.0105 | (9632.0, 0.8) | Chicago (300,278), Buffalo (653,219), Newark (843,345), Pittsburgh (608,362), Asheville (505,647), Atlanta (431,755), Birmingham (333,768), Pensacola (317,950) | g-a4-6 after the slide |
| Q1 (toll states) | 0.02 | (17991.0, 13696.7) | Buffalo (1077,143), Newark (1438,383), Pittsburgh (991,416), Columbus (760,470), Louisville (548,661) | g-a4-4 S8 |
| Q2 (toll states, south) | 0.02 | (17991.0, 35196.7) | Q1 moved 430 px up: Columbus (760,40), Asheville (794,528), Atlanta (653,734), Birmingham (467,760) | g-a4-4 S9 |

State label points (approximate state centres, screen px): P0 OH (863,283), WV (964,397), KY (747,471), GA (835,793), SC (950,712), AL (678,786). Q1 OH (775,432), WV (944,622), KY (583,745), PA (1159,365), NY (1336,142), NJ (1405,443), IN (506,477), MI (629,64). Q2 AL (468,840), GA (729,851).

- **Act 3 handoff.** No A3 briefs exist yet. A3's last picture (A3-S12: cold-blue arrows running south toward Georgia, Alabama and the Panhandle, snow-white fill stopping short, chip "THE SNOW STOPPED HERE") should end on frame P0 with that chip gone. If A3 is built first on another frame, g-a4-1's frame 0 copies A3's last frame and moves to P0 in A4-S1's first 1.2 s; the orchestrator names which.
- **Cold-blue fill (shared by g-a4-1, -2, -6; SCHEMATIC, NOT TO SCALE).** Land-clipped polygon, fill `#5a768f` at 0.38, its advancing south edge a 60 px feathered mask with a 2 px `#7fb2e5` front line at 0.6. East boundary (lat, lon), so Buffalo, New York and the New Jersey coast stay out of it (Buffalo sat in the 40s): (46.0, -81.0), (42.3, -79.6), (40.8, -78.0), (39.0, -77.0), (36.5, -78.5), (34.0, -77.8), (32.0, -80.8), (30.0, -81.4); west boundary off-frame (lon -100). Its north-to-south reach is one number, the edge latitude; each brief gives the edge per cue. Edge lat to map y: 41.0 = 31395.0 · 38.6 = 44799.0 · 36.4 = 57086.0 · 35.4 = 62671.0 · 33.3 = 74399.5 · 30.2 = 91713.0. Rule: the edge passes a pin's latitude before that pin turns blue.
- **Pin style.** Core dot 16 px (12 px in frame P0, where the Kentucky pins crowd), ring 30 px, 3 px stroke. Cold record pin: fill `#7fb2e5`, ring `#dfe7ee`. Callback (Bowling Green): fill `#5a768f` deep blue, ring `#7fb2e5`, its chip at 0.5 opacity. Broken record (Farmers): fill and ring `#4a5560`. Pensacola "pale blue": fill `#7fb2e5` at 0.55 over a `#dfe7ee` core. Buffalo: fill `#d8a13a` (warm), soft glow 24 px `#d8a13a` at 0.5. Unlabelled dots stay on screen in later frames, dimmed to 0.6.
- **Type.** Place labels Arial 700 26 px `#dfe7ee`, paint-order stroke `#04070c` 5 px. Values Arial Black 900 52 px `#f2f5f8` (cold values `#7fb2e5` only where named). Sub lines Arial 700 22 px `#93a3b2` tracking 3. Source line Arial 700 20 px `#c8d3e0` tracking 1, left 110, bottom 92. Basemap credit "Basemap: Natural Earth" Arial 700 19 px `#93a3b2` at left 110, bottom 60 on every map comp (same spot as the intro). 'Arial Black' always with font-weight 900.
- **Corner circle.** On through A4 except A4-S6 (Paul full frame). Every comp keeps x ≥ 1600, y ≥ 680 free of labels, numbers, pins and highlighted shapes; only basemap ground there.
- **Segment offsets inside multi-segment comps** assume a 0.40 s gap between narration segments (no index.html for A4 yet). Each brief keeps a `SEG` table; the orchestrator's real `data-start` differences replace those numbers, and every cue is `SEG[seg] + word time`. Segment lengths (wav, s): S1 14.104, S2 17.810, S3 12.257, S4 16.105, S5 18.273, S6 7.781, S7 8.704, S8 21.529, S9 15.308, S10 10.093, S11 8.247.
- **Track and mounts.** All six hosts are full-frame on track 2. No footage sits under any A4 graphic, so frame-coverage is met by the designed ground (basemap or the night street), never a black field.
- **Sound notes in the Picture lines** (cold wind layer S1, bed drop S6, low hit on "160" S7, riser ending on "show" S11) belong to the edit, not to the comps.
