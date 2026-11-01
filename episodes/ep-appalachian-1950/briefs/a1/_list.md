# A1 section graphics: ep-appalachian-1950 (A1-S1 to A1-S12; there is no A1-S10)
Written 28 Oct 26 from `acts/a1.md` (= edit_script.md A1 block, act locked), `audio/a1-s*.words.json` + wav lengths, `research/nws-facts.md`, `research/teardown-footage.md`, `factcheck/a1-r1.md`, `factcheck/a1-r4.md`, `media/candidates/a1/picks.md` + `provenance.csv`.
Every brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6-§8 by reference; read both, then `learnings/mg.md`, before building.

| comp id | segments | what it shows (one line) | depth | builder model | library exemplar to start from | sits over |
|---|---|---|---|---|---|---|
| g-a1-1-wall | A1-S1 | Chapter card "THE SIDE NOBODY REMEMBERS" out of the blackout, then a blurred viewer-comment wall: snow rows lit white, two wind rows lit blue; chip "MOST MEMORIES: SNOW" | standard | Sonnet 5.5 high | `library/inhouse/title-card.html` (chapter card), `library/inhouse/snippets/cards.css` `.glasscard` (chip) | nothing: full-frame designed card (track 2) |
| g-a1-2-bearmtn | A1-S2 | Northeast map (left) with the "?" sliding up the Hudson into a "BEAR MOUNTAIN, NY" pin; gust ladder (right) shows Newark 108 dim, then the Bear Mountain bar shoots past it to "140 MPH" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (basemap, pins) + `library/inhouse/ranked-bars.html` (bars) | nothing: full-frame designed map + chart |
| g-a1-3-jet | A1-S3 | Side-view cutaway: ground, hills, rooftops; fast blue wind band about a mile up, warm layer near the ground, wisps mixing down at four unnamed points; chip "FAST WIND ABOUT 1 MILE UP"; then push to a New England map with tree and power-out markers | deep | Opus 5.5 | `references/editing-patterns/ep2-met-explainer.html` (cutaway), `library/inhouse/master-map-us-canada.html` (map) | nothing: full-frame designed explainer, then map |
| g-a1-4-ladder | A1-S4, A1-S5, A1-S6 | Same map + ladder as g-a1-2: Mount Washington 160 lands as a dimmed footnote bar above a divider; Albany 83, Allentown 88 land, Newark 108 marked ITS RECORD; NYC bar appears split and "?"; resolves into NYC 94 and Central Park 70 with tags | deep | Opus 5.5 | g-a1-2's built file (copy its map and ladder, frame 0 = its last frame); `library/inhouse/ranked-bars.html` | nothing: full-frame designed map + chart |
| g-a1-5-ct | A1-S7 | Connecticut map: Bridgeport pin, "WORST SINCE 1938", water rising up a station silhouette "STATION FLOODED / 4 TO 5 FT"; Hartford pin inland, clock chip "4:30 PM TO 7:30 PM", three gust ticks past a 100 MPH line | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html`; gauge from `library/inhouse/then-now-scale.html` | nothing: full-frame designed map |
| g-a1-6-delaware | A1-S8 | NWS Jackson KY 25 Nov 1950 surface chart, slow push toward the coast, onshore arrows into New Jersey and up Delaware Bay; crossfade to a Delaware River map: tide line climbs to Philadelphia "10.8 FT · RECORD" over a faint "FLOODING STARTS 10.2 FT" line; Delaware Bay pin "RECORD TIDE" | deep | Opus 5.5 | image-in-comp push from `references/editing-patterns/ep5-terrain-map.html`; `library/inhouse/master-map-us-canada.html` | the chart still `A1-S8_c1_nws-jkl-surface-1950-11-25.jpg`, mounted inside the comp (then the designed map) |
| g-a1-7-newlondon | A1-S9 | Bar chart "NEW LONDON, CT · TOP FOUR TIDES IN 100 YEARS": three hurricane bars (no values, open tops) above the 1950 bar "7.58 FT · WINTER STORM"; then NY State map with chip "$20 MILLION · NY STATE WIND DAMAGE (1950 $)" | standard | Sonnet 5.5 high | `library/inhouse/ranked-bars.html`, `library/inhouse/master-map-us-canada.html` | nothing: full-frame designed card, then map |
| g-a1-8-toll | A1-S11 | Grey New Jersey and New York outlines: "NEW JERSEY 34" counts up with tag "WHOLE-STORM COUNT", then "NEW YORK 36" with its southwest corner shaded snow-white, tag "INCLUDES SNOW SIDE" | standard | Sonnet 5.5 high | `library/inhouse/numbers-rollup.html` (counter) + `library/inhouse/master-map-us-canada.html` | nothing: full-frame designed map |
| g-a1-9-split | A1-S12 | Split screen: left Newark pin wind-blue "108 MPH"; right Columbus pin under falling snow, clock chip "NOON / SAT, NOV 25", chips "10°F" and "SNOWING"; nothing joins the halves | standard | Sonnet 5.5 high | `library/inhouse/master-map-us-canada.html`; right half must equal `briefs/a2/g-a2-1-columbus.md` frame 0 | nothing: full-frame designed split map |

Count: 9 graphics. Deep 5 (Opus 5.5): g-a1-2, -3, -4, -5, -6. Standard 4 (Sonnet 5.5 high): g-a1-1, -7, -8, -9.
No segment in A1 is "Paul on camera", so no Paul clip and no date/place popfig in this act. No sourced footage sits under any A1 comp (picks.md: every beat is self-made except the S8 chart, which is mounted inside g-a1-6).

## Section-wide decisions (each brief repeats the part it needs)
- **Cues.** Seconds from the segment's own start, on the spoken word (quoted as Whisper wrote it). Host data-start = segment start; host duration = wav length + 0.40 s gap (no index.html yet; the orchestrator replaces the gap with the real data-start differences). Wav lengths (s): S1 16.602, S2 9.610, S3 12.438, S4 12.959, S5 17.018, S6 13.047, S7 20.399, S8 18.250, S9 17.864, S11 9.109, S12 12.989.
- **Whisper slips, words only.** a1-s5 writes "its own record 2" for "too" (13.18); a1-s11 "Eastside". Cue times stand; never put those words on screen.
- **Corner circle.** Act 1 is narration with the circle on wherever the corner is free. Every comp keeps x >= 1600, y >= 680 free of labels, numbers, pins, bars and highlighted shapes for its whole window.
- **L1 stays closed.** No comp draws a storm track, a low ("L"), a front or a line joining the coast to the snow side. The only arrows in the act are g-a1-6's onshore arrows at the coast (the Picture line asks for them); they never point at or start from the chart's low. Act 3 owns the mechanism.
- **Popfig rule.** Every A1 beat is a card or map comp, so there is no red Abril popfig in A1 (popfigs sit only over footage). Picture-line "chips" are glass chips or the chart's own value labels.
- **One fact, one instance per frame.** A number that is a bar's value label is not repeated in a chip in the same frame: the S2 chip "140 MPH" IS the Bear Mountain bar's value label.
- **Source lines.** Every comp carries its Picture-line source as a corner credit: "Source: ..." Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 60 (never the right corner). On map comps "Basemap: Natural Earth" takes bottom 60 and the source goes on the line above (bottom 90).
- **One map, one coordinate system** (same as `briefs/intro/_list.md` and `briefs/a2/_list.md`): map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213); screen px = (map unit - frame top-left) × s. North up. Computed by script 28 Oct 26; compute any new point with the formula, never by eye.

| place | lat, lon | map units (x, y) |
|---|---|---|
| Newark NJ | 40.7357, -74.1724 | (89893.2, 32871.1) |
| Bear Mountain NY (summit) | 41.3109, -74.0068 | (90529.3, 29658.6) |
| Central Park NY | 40.7812, -73.9665 | (90684.1, 32617.0) |
| Albany NY | 42.6526, -73.7562 | (91491.9, 22165.2) |
| Allentown PA | 40.6023, -75.4714 | (84903.8, 33616.1) |
| Bridgeport CT | 41.1792, -73.1894 | (93668.9, 30394.1) |
| Hartford CT | 41.7658, -72.6734 | (95650.9, 27118.0) |
| New London CT | 41.3557, -72.0995 | (97855.2, 29408.4) |
| Philadelphia PA | 39.9526, -75.1652 | (86079.9, 37244.7) |
| Greenwich NJ (see g-a1-6 open item) | 39.3893, -75.3349 | (85428.1, 40390.7) |
| Cape May NJ | 38.9351, -74.9060 | (87075.5, 42927.4) |
| Columbus OH | 39.9612, -82.9988 | (55991.0, 37196.7) |
| Buffalo NY | 42.8864, -78.8784 | (71817.5, 20859.4) |

| frame | used by | s | anchor at screen px | frame top-left (map units) | points on screen (px) |
|---|---|---|---|---|---|
| A1-N | g-a1-2, g-a1-4 (map panel x 0 to 820) | 0.058 | Albany (560, 140) | (81836.7, 19751.4) | Albany (560,140), Bear Mtn (504,575), Central Park (513,746), Newark (467,761), Allentown (178,804); Hudson: Battery (501,773), Yonkers (528,698), Tappan Zee (532,653), Bear Mtn Bridge (509,572), Newburgh (503,513), Poughkeepsie (519,449), Kingston (515,374) |
| A1-E | g-a1-3 (second half) | 0.028 | Hartford (760, 820) | (68508.0, -2167.7) | Hartford (760,820), Springfield (769,768), Worcester (854,743), Providence (896,812), New Haven (733,891), Boston (934,727), Concord NH (882,594), Burlington (702,396), Portland ME (1020,524), Bridgeport (705,912), New London (822,884) |
| A1-C | g-a1-5 | 0.18 | Bridgeport (640, 800) | (90113.4, 25949.7) | Bridgeport (640,800), Hartford (997,210), New London (1394,623) |
| A1-D | g-a1-6 (second half) | 0.13 | Philadelphia (900, 240) | (79156.8, 35398.5) | Philadelphia (900,240), Greenwich NJ (815,649), Cape May (1029,979), Trenton (1100,46, not labelled) |
| A1-Y | g-a1-7 (second half) | 0.03 | Albany (1000, 500) | (58158.5, 5498.5) | Albany (1000,500), Buffalo (410,461), Burlington (1063,195), Newark (952,821) |
| A1-T | g-a1-8 | 0.03 | Newark (1000, 620) | (56559.9, 12204.4) | Newark (1000,620), Albany (1048,299), Buffalo (458,260), Philadelphia (886,751), Cape May (915,922) |
| A1-W | g-a1-9 left half | 0.10 | Newark (480, 560) | (85093.2, 27271.1) | Newark (480,560) |
| A2-C +480 | g-a1-9 right half (= g-a2-1 frame 0) | 0.10 | Columbus (1180, 560) | (44191.0, 31596.7) | Columbus (1180,560) |

## The gust ladder (shared by g-a1-2 and g-a1-4; one scale, slots fixed from frame 0, no reflow)
Panel: x 860 to 1824, full height, ground `#04070c`; the map panel (x 0 to 820) fades into it with a 120 px gradient. Bars are horizontal rungs: origin x 900, scale 3.5 px per mph (computed: 160 mph = 560 px, ends x 1460), bar height 34 px, radius 4. Each row: name line (Arial 700 22 px `#93a3b2` tracking 3, baseline 14 px above the bar top), bar, value label at bar end + 18 px (Arial Black 900 52 px `#f2f5f8`, vertically centred on the bar). Header at top-left of the panel: "PEAK GUSTS · MPH" Arial 700 26 px `#93a3b2` tracking 8, left 900, top 70.

| row | bar centre y | value (mph) | bar end x | name line | value label | colour |
|---|---|---|---|---|---|---|
| Mount Washington (footnote) | 190 | 160 | 1460 | `MOUNT WASHINGTON, NH · SUMMIT *` | `160` | `#93a3b2` at 45 % (dimmed, never the wind blue) |
| divider | 250 | | | dashed 2 px `rgba(255,255,255,.14)` x 900 to 1700; small tag right under it at left 900: `* ONE MOUNTAINTOP STATION` Arial 700 19 px `#93a3b2` | | |
| Bear Mountain | 330 | 140 | 1390 | `BEAR MOUNTAIN, NY` | `140 MPH` | `#7fb2e5` |
| Newark | 440 | 108 | 1278 | `NEWARK, NJ` (+ `· ITS RECORD` amber `#d8a13a` from S5) | `108 MPH` | `#7fb2e5` |
| New York City | 550 | 94 | 1229 | `NEW YORK CITY · NWS JACKSON` | `94` | `#7fb2e5` |
| Central Park | 640 | 70 | 1145 | `CENTRAL PARK · NWS MOUNT HOLLY · PARK RECORD` | `70` | `#7fb2e5` |
| Allentown | 750 | 88 | 1208 | `ALLENTOWN, PA` | `88` | `#5a768f` until landed, then `#7fb2e5` |
| Albany | 860 | 83 | 1190 | `ALBANY, NY · ITS RECORD` | `83` | same |
Value labels: "MPH" only on the Bear Mountain and Newark labels (the Picture line's chips); every other label is the bare number, the header carries the unit. Rows at y >= 680 end their text left of x 1600 (Allentown label ends about 1400, Albany about 1340): the circle corner stays clear.

## Open items for the orchestrator (each brief repeats its own)
1. g-a1-6: the 25 Nov chart shows the low (an "L" near the Virginia coast, image px about 840, 398 of 1156 x 759). A push toward the coast keeps it in frame. Decide whether that pre-pays L1; the brief starts the push already framed on New Jersey with the low at the left edge, never labelled or pointed at.
2. g-a1-6: research tags "Greenwich Piers" (PHI, 8.8 ft) as Delaware Bay, southern New Jersey. A "Greenwich Piers" gauge also exists on the Philadelphia waterfront (Greenwich Point). The brief pins Greenwich, NJ (Cumberland County) per the research row and puts no number on it; confirm the place before build.
3. g-a1-7: no research row gives the tide heights of the 1938 hurricane, Carol or Sandy at New London, or their order. The brief draws those three bars without values, equal height, open-topped, in date order (no rank implied). A sourced table (NOAA 8461490 New London top-ten) would let them be drawn to scale.
4. g-a1-9 vs g-a2-1: g-a2-1's frame 0 has its clock chip at left 110, top 90 (the left half). In A1-S12 the left half is Newark, so g-a1-9 puts the Columbus clock chip in the right half (left 1010, top 90). A chapter blackout sits between the two comps; re-match g-a2-1's frame-0 chip position or accept the jump.
5. g-a1-5: "4:30 PM TO 7:30 PM" and the three gust ticks are on screen but not spoken (narration says only "gusts of a hundred miles an hour"); factcheck a1-r1 row 29 confirms them (secondary, NBC CT quoting the Weather Bureau report). Kept per the locked Picture line.
