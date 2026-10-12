Host: id=g-a1s09-forecasts file=compositions/g-a1s09-forecasts.html start=196.15 (timeline-map.md table 1; the mount in index.html wins) duration=31.20 s (wavs 30.67 s plus their gaps) track=2

# g-a1s09-forecasts · A1-S9 to A1-S12 · two afternoon forecasts, seven counties, and the office that did not pass it on (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 7 to 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3e rows PT-05 and PT-06, section 6 item 10. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page holds past about 8 s without a visible change (rule 7). Two type sizes on a page card are by design (rule 10). A flash is a stroke or fill change (rule 12). Map geometry comes from the file (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read at both ends of every zoom (rule 20).
**Spoken (A1-S9):** "At two that afternoon a second forecast went out, for parts of Wisconsin, Iowa and Illinois, with the words "one or two tornadoes.""
**Spoken (A1-S10):** "Then at five twenty came Severe Weather Forecast Number Sixty Nine. It named parts of northern Indiana, and it used the words "a tornado or two.""
**Spoken (A1-S11):** "It covered most of the northern half of the state. South Bend passed it on ten minutes later and named seven counties."
**Spoken (A1-S12):** "The Weather Bureau office in Fort Wayne didn't pass this one on. Remember Fort Wayne."
**One look:** a clock, the forecast's own typed sheet, and a map that closes in step by step: three states, then Indiana's northern half, then seven named counties, then one unlit teletype in Fort Wayne.

## 0. What this graphic claims
Forecast 68 (2:00 PM EST) named parts of Wisconsin, Iowa and Illinois and used the words "one or two tornadoes"; Indiana was not in it. Forecast 69 (5:20 PM EST) named portions of northern Indiana with "a tornado or two". South Bend passed it on at 5:30 PM and named seven counties. The Fort Wayne office did not pass on the 5:20 forecast.

## 1. Source
- `edit_script.md` A1-S9 [A2; study printed p. 6: Forecast 68, "ISSUED 1:00 P.M. CST (2:00 EST)"]; A1-S10 [A5; study printed p. 7; the scan reads "ISSUED 4:20 P.M. CST (5:20 EST)"]; A1-S11 [A5; study printed p. 7] · [A5; survey printed p. 38]; A1-S12 [A5; study printed p. 10].
- `media/stills/a9-sels-forecast-68.png` (702 x 914), read on the file. Its typed text runs from file y 9 to 299: `SEVERE WEATHER FORECAST NUMBER 68` / `ISSUED 100 PM CST APRIL 11 1965` / `U.S. WEATHER BUREAU TORNADO FORECAST FOR....` / `EXTREME SOUTHERN WISCONSIN` / `EXTREME EASTERN IOWA` / `PORTIONS OF NORTHERN ILLINOIS` / then the body, whose first two lines read `A FEW SEVERE THUNDERSTORMS WITH LARGE HAIL DAMAGING WINDS AND ONE OR TWO` / `TORNADOES ARE EXPECTED FROM 1 PM UNTIL 6 PM CST THIS SUNDAY AFTERNOON AND`.
- `media/stills/a9-sels-forecast-69.png` (672 x 872). Typed text from file y 11 to 322: `ALSYM A MKCC 112228` / `SEVERE WEATHER FORECAST NUMBER 69` / `ISSUED 420 PM CST APRIL 11 1965` / `U.S. WEATHER BUREAU TORNADO FORECAST FOR....` / `PORTIONS OF NORTHERN INDIANA` / `PORTIONS OF SOUTHERN MICHIGAN AND` / `PORTIONS OF NORTHWEST OHIO` / then the body, whose first line reads `SCATTERED SEVERE THUNDERSTORMS WITH A TORNADO OR TWO LARGE HAIL AND`.
- **Only the typed text of each scan is shown.** Below the text each file carries a map ("FIGURE 3", "FIGURE 4") with a forecast box and "REPORTED TORNADOES" triangles; `provenance.csv` records that the boxes and triangles were added later by the Weather Service page's author. On Forecast 69's figure they mark tornadoes that had not happened at 5:20 PM. The figure never enters the frame.
- Seven counties: the survey's 5:30 PM entry (printed p. 38), as listed in the Picture note. Fort Wayne: study printed p. 10, "but not the one at 5:20 p.m."
- Maps: `media/maps/midwest-states.svg` (BM-2), `media/maps/indiana-counties.svg` (BM-1), same coordinate space. Positions: `media/data/points.csv` (`pt-fort-wayne` map units (605.1, 297.0)).

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-2's nine state paths with BM-1's counties, state outline and points on top (BM-1's `map-neighbours` group is left out: BM-2's states take its place). The camera is the SVG's `viewBox` and its CSS box, tweened together; `preserveAspectRatio="xMidYMid meet"`.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| MIDWEST | 96, 320, 644, 680 | `-1011.2 -835.5 1818.4 1920` | 0.3542 | A1-S9, start of A1-S10 |
| INDIANA | 96, 320, 644, 680 | `71.1 151.5 738.7 780` | 0.8718 | A1-S10, first sentence of A1-S11 |
| NORTH (family state) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | A1-S11 second sentence, A1-S12 |
| FORTWAYNE | 716, 62, 1080, 450 | `440 216 240 100` | 4.5 (screen x = 716 + 4.5 x (u - 440), y = 62 + 4.5 x (u - 216)) | end of A1-S12 |
Moves: MIDWEST to INDIANA 2.46 times, INDIANA to NORTH 3.44 times (and the box moves to the right-hand top), NORTH to FORTWAYNE 1.5 times. Each is 0.9 s, power2.inOut, the viewBox numbers moved geometrically (the `logZoom` maths of `library/inhouse/snippets/helpers.js` on a proxy with `onUpdate`), end values set exactly.
Line and word boxes on the two scans were measured on the files by a row and column scan (file px, origin top left):
| Words | File | File px (x0 to x1, y0 to y1) |
|---|---|---|
| `ONE OR TWO` (last three words of the body's first line) | 68 | 590 to 678, 172 to 183 |
| `TORNADOES` (first word of the body's second line) | 68 | 47 to 123, 189 to 200 |
| `PORTIONS OF NORTHERN INDIANA` | 69 | 25 to 267, 142 to 153 |
| `A TORNADO OR TWO` (words 5 to 8 of the body's first line) | 69 | 339 to 478, 209 to 222 |
The scans' line pitch is 17 px, so the underline here is 3 px, 1 px under the line box (the design sheet's 6 px would cover the next line).
The band over "the northern half" is schematic: no source draws its edge (plan section 6 item 10).

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | states Body light 2 px, fill Panel dark; BM-1 counties 1.5 px Label grey and `st-in` 3 px, all non-scaling; ids prefixed `fc-`. The `map-counties` group is hidden (opacity 0) until the move to NORTH: at 0.35 and 0.87 px per unit its lines would grey Indiana in. Every `pt-` group hidden except Fort Wayne from its cue |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; face `media/drawings/wall-clock.svg` inline. Three states of its text and hands, below |
| Forecast card 68 | Beige polaroid border 10 px, page shadow: left 760, top 96, 722 x 332, `overflow:hidden`. Inside it the `<img>` at its own size 702 x 914, at (770, 106): the card shows file y 0 to 312 and no more |
| Forecast card 69 | same place: left 760, top 96, 692 x 354; `<img>` 672 x 872 at (770, 106): the card shows file y 0 to 334 and no more |
| Underlines | Popfig red 3 px, drawn left to right (`scaleX`, origin left). 68: `ONE OR TWO` screen x 1360 to 1448, y 290 to 293; then `TORNADOES` x 817 to 893, y 307 to 310. 69: `PORTIONS OF NORTHERN INDIANA` x 795 to 1037, y 260 to 263; `A TORNADO OR TWO` x 1109 to 1248, y 329 to 332 |
| Unlit page | Panel dark at 45 % over the card's image except the underlined word boxes (each padded 4 px), fading in over 0.4 s with the first underline of that card |
| Strip, A1-S9 | Beige polaroid, left 760, top 448, 816 x 124. Quote Georgia 52 px, Caption dark: `“ONE OR TWO TORNADOES”` (714 px wide). Attribution under it, Arial 700 22 px, Caption dark sub, tracking 2: `Severe Weather Forecast 68 · issued 1:00 PM CST (2:00 PM EST)` |
| Strips, A1-S10 | strip 1: left 760, top 470, 816 x 92, Georgia 40 px: `“PORTIONS OF NORTHERN INDIANA”` (732 px). Strip 2: left 760, top 578, 816 x 124, Georgia 52 px: `“A TORNADO OR TWO”` (573 px), attribution `Severe Weather Forecast 69 · issued 4:20 PM CST (5:20 PM EST)` |
| State fills, A1-S9 (MIDWEST) | `fc-st-wi`, `fc-st-ia`, `fc-st-il`: fill Amber 2 at `fill-opacity` 0.25. Labels, two lines each, Arial 700 22 px, line height 26, Headline white with the credit shadow, centred: `extreme southern` / `Wisconsin` on (457, 479); `extreme eastern` / `Iowa` on (297, 665); `portions of` / `northern Illinois` on (472, 809). Indiana (screen x 536 to 685, y 677 to 938) has no fill and no label |
| Northern band, A1-S10 (INDIANA) | Amber 2 at 25 %: a rect clipped to `fc-st-in` (clipPath), from the state's north edge (screen y 339) down to its mid line (screen y 660, map y 541.5), its lowest 40 px fading to nothing (linear gradient mask). Indiana on screen: x 235 to 602, y 339 to 981. Label on the band, Arial 700 22 px, Headline white with the credit shadow, centred on (418, 499): `portions of northern Indiana` (288 px) |
| Lit county, A1-S11 (NORTH) | fill Amber 2 at `fill-opacity` 0.45; if the passed base `compositions/g-a2s14-six.html` lights its counties with other values, use the base's and say so in the receipt |
| County names (NORTH) | Arial 700 22 px, Headline white with the credit shadow, tracking 2, centred: `PORTER` (907, 247), `LAPORTE` (1046, 228), `ST. JOSEPH` (1205, 174), `ELKHART` (1371, 173), `STARKE` (1051, 388), `MARSHALL` (1218, 324), `KOSCIUSKO` (1369, 372). `STARKE` sits low in its county because LaPorte's outline reaches down to y 373 beside it |
| Source line, A1-S11 | design sheet section 10, left 96, bottom 60: `Weather Bureau survey report, 1965, p. 38` |
| Fort Wayne | dot radius 6 px on screen (`r` 2 map units in NORTH, 1.33 in FORTWAYNE). NORTH: dot (1643.3, 455.0), label `Fort Wayne` Arial 700 22 px Body light, right aligned to x 1625, top 444. FORTWAYNE: dot (1459.0, 426.5), label right aligned to x 1441, top 415 |
| Teletype icon | `media/drawings/teletype.svg` inline, inside the map SVG so it rides the push: `translate(612 240) scale(0.25)` in map units (35 map units wide). NORTH screen box x 1664 to 1769, y 284 to 389 (105 px); FORTWAYNE x 1490 to 1647.5, y 170 to 327.5 (157.5 px). Lines Label grey, `stroke-width` 3 with `vector-effect="non-scaling-stroke"`, paper (`dw-lamp`) Panel dark: unlit |
| Paper strip, A1-S12 | Beige polaroid, left 96, top 640, 780 x 124. Quote Georgia 52 px, Caption dark: `“but not the one at 5:20 p.m.”` (683 px). Attribution: `Disaster Research Center, 1966, p. 10` |

Clock stamp states (design sheet section 8 positions; hand angles clockwise from 12):
| From | Eyebrow | Time | Place line | Hour hand | Minute hand |
|---|---|---|---|---|---|
| A1-S9 | `FORECASTERS` | `2:00 PM` | `Kansas City · Eastern time` | 60 | 0 |
| A1-S10 | `FORECASTERS` | `5:20 PM` | `Kansas City · Eastern time` | 160 | 120 |
| A1-S11 | `WEATHER BUREAU` | `5:30 PM` | `South Bend, Indiana` | 165 | 180 |
The Picture note's `EST` does not fit beside an 84 px time inside the 590 px card, so the zone is carried by the place line. A change of state: the hands sweep to the new angles (0.5 s, power3.out) and the text swaps at the sweep's mid point.

## 4. Must be true in the picture
1. Each clock shows its time: 2:00 (hour hand on 2, minute hand on 12), 5:20 (between 5 and 6, on 4), 5:30 (half way between 5 and 6, on 6). The sheets print Central time (`100 PM CST`, `420 PM CST`); each strip's attribution carries both zones so the stamp and the sheet agree on screen.
2. In A1-S9 exactly three states are filled: Wisconsin, Iowa, Illinois. Indiana has no fill and no label. Each label carries the sheet's own qualifier; no state is called whole.
3. Only the typed part of each sheet is ever in frame. No "FIGURE", no forecast box, no triangle, no "REPORTED TORNADOES".
4. Each underline is under the words in the section 2 table and no others. Each strip repeats the sheet's words exactly, in capitals.
5. The sheets are at their own size (702 and 672 px wide), never enlarged.
6. In A1-S10 the band covers Indiana's northern half only, fades out at the mid line and shows no county edge. Its label is the sheet's `portions of northern Indiana`.
7. In A1-S11 exactly seven counties light: Porter, LaPorte, St. Joseph, Elkhart, Starke, Marshall, Kosciusko. Lake, LaGrange, Noble, Fulton and Allen stay unlit.
8. Fort Wayne's dot is in the unlit county east of the seven. The teletype beside it is unlit from first to last frame: no amber on it, no pulse, no paper moving.
9. Line weights and the dot's size are the same at both ends of each move (read both frames).
10. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680 (the teletype at x 1647 is above y 328).
11. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: the three stamp states above · `extreme southern` / `Wisconsin` · `extreme eastern` / `Iowa` · `portions of` / `northern Illinois` · `“ONE OR TWO TORNADOES”` · `Severe Weather Forecast 68 · issued 1:00 PM CST (2:00 PM EST)` · `“PORTIONS OF NORTHERN INDIANA”` · `“A TORNADO OR TWO”` · `Severe Weather Forecast 69 · issued 4:20 PM CST (5:20 PM EST)` · `portions of northern Indiana` · the seven county names · `Weather Bureau survey report, 1965, p. 38` · `Fort Wayne` · `“but not the one at 5:20 p.m.”` · `Disaster Research Center, 1966, p. 10`. The sheets' words are the image.
Cue words and times are from `audio/a1-s9.words.json`, `a1-s10`, `a1-s11` and `a1-s12` as they stood on 12 Oct 26 at 17:50, after the voice conversion's re-transcription. Segment starts inside the comp are the wav lengths added up: A1-S9 0.00, A1-S10 8.61, A1-S11 18.04, A1-S12 24.74; total 30.67 s. The gaps `mg_specs/timeline-map.md` puts between segments (not on disk yet) are added to every later segment's rows. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S9 | 0 | At | 0.00 | 0.00 | first frame: ground and the map in MIDWEST (state outlines only) |
| 1 | A1-S9 | 1 | two | 0.36 | 0.13 | clock stamp slides in from the left (0.6 s, power3.out), state 2:00 PM; the minute hand sweeps its last 30 degrees into place |
| 2 | A1-S9 | 6 | forecast | 1.70 | 1.47 | forecast card 68 rises in from below with a fade (`y:358` set at 0, to `y:278`; 0.7 s, power3.out) and holds there, 278 px under its briefed place, until step 7. Corrected 13 Oct 26 to the file as saved at 00:14: this brief first slid the card in from the right, and that entrance crossed the presenter corner (8,281 px at 1.60 s) |
| 3 | A1-S9 | 12 | Wisconsin, | 3.54 | 3.31 | Wisconsin fills (0.3 s) with its label |
| 4 | A1-S9 | 13 | Iowa, | 4.54 | 4.31 | Iowa fills with its label |
| 5 | A1-S9 | 15 | Illinois, | 5.14 | 4.91 | Illinois fills with its label |
| 6 | A1-S9 | 19 | one | 6.54 | 6.31 | unlit page fades in on the card; underline `ONE OR TWO` (0.3 s), then `TORNADOES` (0.25 s) |
| 7 | A1-S9 | 22 | tornadoes. | 7.52 | 7.29 | the strip lifts in under the card (`y:60` set at 0, to 0, with the fade; 0.4 s, power3.out); on the same cue card 68 moves up to its briefed place (`y:278` to 0; 0.5 s, power3.out) |
| 8 | A1-S10 | 0 | Then, | 0.00 | 8.87 | strip and card 68 exit right (`x:1900` with the fade, 0.4 s, power3.in; both sit above y 680 by then, the strip's bottom at y 572, so the exit stays out of the corner); the three fills and labels fade (0.3 s) |
| 9 | A1-S10 | 2 | 5 | 0.68 | 9.15 | stamp goes to state 5:20 PM |
| 10 | A1-S10 | 5 | severe | 1.54 | 10.01 | forecast card 69 rises in from below with a fade (`y:347` set at 0, to `y:267`; 0.7 s, power3.out) and holds there until step 13. Corrected 13 Oct 26 to the file as saved at 00:14: not in from the right, which crossed the presenter corner (7,770 px at 10.15 s) |
| 11 | A1-S10 | 10 | It | 4.44 | 12.91 | map push MIDWEST to INDIANA (0.9 s) |
| 12 | A1-S10 | 12 | parts | 4.90 | 13.37 | unlit page on card 69; underline `PORTIONS OF NORTHERN INDIANA` (0.4 s) |
| 13 | A1-S10 | 15 | Indiana, | 5.66 | 14.13 | strip 1 lifts in and card 69 moves up to its briefed place on the same cue (`y:267` to 0; 0.5 s, power3.out); the northern band wipes down from the north edge (0.5 s) and its label fades in |
| 14 | A1-S10 | 21 | a | 8.04 | 16.51 | underline `A TORNADO OR TWO` (0.4 s) |
| 15 | A1-S10 | 24 | two. | 8.72 | 17.19 | strip 2 lifts in under strip 1 |
| 16 | A1-S11 | 5 | northern | 1.30 | 19.25 | the band's fill goes 25 % to 45 % and back (0.6 s): a fill change, no scale |
| 17 | A1-S11 | 10 | South | 3.24 | 21.19 | card 69 and both strips exit right (0.4 s); band and label fade (0.3 s); the map moves INDIANA to NORTH (0.9 s) and the county lines fade in during the move |
| 18 | A1-S11 | 15 | ten | 4.28 | 22.23 | stamp goes to state 5:30 PM, South Bend |
| 19 | A1-S11 | 20 | seven | 5.38 | 23.33 | the seven counties fill in the order Porter, LaPorte, St. Joseph, Elkhart, Starke, Marshall, Kosciusko, 0.1 s apart (0.25 s each), each with its name; the source line fades in |
| 20 | A1-S12 | 5 | Fort | 1.68 | 26.41 | Fort Wayne dot and label fade in (0.3 s) |
| 21 | A1-S12 | 7 | didn't | 2.24 | 26.97 | the teletype draws on beside it (0.5 s, `strokeDashoffset`), unlit |
| 22 | A1-S12 | 10 | one | 3.02 | 27.75 | the paper strip rises into the lower band (0.4 s); the `p. 38` source line fades out as it arrives (one source per frame) |
| 23 | A1-S12 | 12 | remember | 3.50 | 28.23 | county names and the Fort Wayne label fade (0.2 s, starting 0.2 s earlier); push NORTH to FORTWAYNE (0.9 s); the Fort Wayne label returns at its new place at 29.20. Hold to the end. The file's start for this word (3.50) takes in the pause before it; the word is heard near 4.3. The push may start in that pause: it shows nothing new |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.
Card 68 is on screen 6.9 s and changes at 6.54; card 69 is on screen 11.1 s and changes at 13.51 and 16.65: no stretch over 8 s without a change.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a1s09-forecasts.html` is the only file the builder writes; `data-composition-id="g-a1s09-forecasts"`; id prefix `fc-`; root `<div id="fc-root" ...>` styled through `#fc-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family bases `compositions/g-a2s14-six.html` (NORTH mount, lit counties, stamp top left) and `compositions/g-a1s02-strip.html` (the Midwest map and a push into Indiana), both wave 1, briefs in `mg_specs/briefs/`. Quote strip and unlit page from the built `compositions/g-i1s3-cloud.html`; stamp from the built `compositions/g-t1s2-warning.html`.
**Assets mounted (paths from the episode folder):**
- `media/maps/midwest-states.svg` (BM-2, viewBox -980 -1280 2220 2560, 148,112 bytes): its nine state paths, inlined.
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes): counties, `st-in` and points, inlined.
- `media/stills/a9-sels-forecast-68.png` (702 x 914) and `media/stills/a9-sels-forecast-69.png` (672 x 872), each at its own size, windowed by its card.
- `media/drawings/teletype.svg` (DR-01, object box 140 x 140, viewBox -6 -6 152 152), inlined. `media/drawings/teletype-lit.svg` is not used here.
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136), inlined for the stamp's face.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s09-forecasts`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page cards (rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: the three moves run on a proxy; seek to 13.5, 21.7 and 28.7 (mid move) forward and backward and match the frames. Line 6: the four state boxes, the seven name centres, the Fort Wayne dot and the teletype box are computed by a script from `media/maps/indiana-counties.svg` and `media/data/points.csv` and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the Midwest outlines only, no county mesh inside Indiana. Then one settled frame per cue: 1.20 (stamp 2:00 PM), 2.80 (card 68, typed text only), 4.20, 4.90 and 6.20 (the three fills, Indiana bare), 7.30 (both underlines), 8.30 (strip), 9.10 (cleared), 10.00 (stamp 5:20 PM), 11.20 (card 69, no figure), 13.00 and 14.10 (the two ends of the first push), 15.00 (strip 1, band, label), 17.20 (second underline), 18.00 (strip 2), 19.70 (band pulse), 21.20 and 22.25 (the two ends of the move to NORTH: line weight), 23.20 (stamp 5:30 PM), 24.60 (seven counties and names), 26.90 (Fort Wayne), 27.70 (teletype unlit), 28.20 (paper strip landed, one source line; also the last push's start frame), 29.20 (the last push's end frame: line weight, dot size, teletype still unlit), 30.60 (last frame).
