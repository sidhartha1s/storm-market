Host: id=g-a1s02-strip file=compositions/g-a1s02-strip.html start=122.93 (timeline-map.md, 12 Oct 26; the mount in index.html wins) duration=20.56 s track=2

# g-a1s02-strip · A1-S2, A1-S3 · the forecast's strip across the Midwest, then South Bend's 12:20 version of it (wave 1, map family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 6 item 8 (southern Porter). Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read at both ends of the zoom (rule 20).
**Spoken (A1-S2):** "It covered a strip from northeastern Missouri up to north central Indiana. A later study calls it general, with no immediate tornado threat to Indiana."
**Spoken (A1-S3):** "South Bend's Weather Bureau office sent it on. Its version named three Indiana counties, and said several tornadoes were expected between one that afternoon and seven that evening."
**One look:** a soft band laid across three states, with the study's cool verdict on a card; then the map moves in to the corner of Indiana where South Bend's own typed version put names and a number of hours on it.

## 0. What this graphic claims
The forecast covered a strip from northeastern Missouri to north central Indiana, and the study says it "did not indicate any immediate tornado threat to any portion of Indiana". South Bend's 12:20 PM version named Starke, southern Porter and Laporte counties and said "several tornadoes are expected".

## 1. Source
- `edit_script.md` A1-S2, Rows [A1; study printed p. 6] · [A1; study printed p. 6]. Card words, from the Picture note: `did not indicate any immediate tornado threat to any portion of Indiana`.
- `edit_script.md` A1-S3, Rows [A1; survey printed p. 37: "several tornadoes are expected ... 1 PM to 7 PM EST"; "Starke and southern Porter and Laporte Counties"].
- Page crop `media/docs/survey-p37-1220pm-crop.png` (PC-01, 1460 x 353, survey printed p. 37). Its nine lines, read on the file: `Issued at 12:20 PM EST.` / `Severe thunderstorm and tornado forecast.` / `Scattered severe thunderstorms with large hail and damaging winds and several` / `tornadoes are expected this Sunday afternoon and evening from 1 PM EST until` / `7 PM EST in an area 60 miles either side of a line from 60 miles west of` / `St. Louis Missouri to 40 miles north of Indianapolis Indiana. This area` / `includes portions of northeast and east central Missouri central Illinois` / `northwest and west central Indiana.` / `In this area this includes Starke and southern Porter and Laporte Counties.`
- **The band is schematic.** A1-S2 cites the study's two regions, and no file on disk draws the area's edge. The band is a soft stroke between one point in northeastern Missouri and one in north central Indiana (section 2). The survey's line-and-miles wording (lines 5 and 6 of the crop) is not drawn: it is on the card for the viewer to read, and this comp makes no claim about the band's edge, width or ends.
- **Southern Porter is schematic** (plan section 6 item 8): the county's southern half by its mid line, map y 227.6.
- Maps: `media/maps/midwest-states.svg` (BM-2) and `media/maps/indiana-counties.svg` (BM-1), one coordinate space. County boxes read from the file, map units: `co-in-starke` x 378.1 to 437.1, y 233.5 to 281.9; `co-in-laporte` x 377.8 to 434.5, y 173.1 to 269.8; `co-in-porter` x 341.0 to 378.2, y 182.4 to 272.9. `st-mo` x -745.5 to 102.5, y 384.9 to 1238.0; `st-in` x 229.8 to 650.7, y 173.0 to 909.9.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-2's states and, over them, BM-1's counties and Indiana outline (same units); the camera is its `viewBox` and its CSS box, tweened together. `preserveAspectRatio="xMidYMid meet"`; both states are 2.4 to 1.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| MIDWEST-STRIP (this comp's) | 96, 62, 1483, 618 | `-820 110 1500 625` | 0.9887 (screen x = 96 + 0.9887 x (u + 820), y = 62 + 0.9887 x (u - 110)) | A1-S2 |
| NORTH (family state, as `g-a2s14-six`) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | A1-S3 |
MIDWEST-STRIP to NORTH is a push of 3.03 times in 0.9 s (power2.inOut), box and viewBox in one move, the viewBox numbers moved geometrically (the `logZoom` maths of `library/inhouse/snippets/helpers.js` on a proxy with `onUpdate`, as `mg_specs/briefs/g-a1s09-forecasts.md` does), end values set exactly. The MIDWEST-STRIP box ends at y 680 and x 1579: the presenter corner (x >= 1600, y >= 680) stays empty. Missouri, Illinois and Indiana run off the bottom of that box; that is intended.
Band ends, map units: M = (-266.0, 498.3), which is 40.0 N, 92.0 W through the README's projection, checked inside `st-mo` by a point-in-path test and inside the state's north-east quarter (north of its mid y 811.5, east of its mid x -321.5); N = (440.2, 295.8), the middle of the north third of `st-in`'s box. Length 734.7 units, 726 px on screen. Width 180 units (178 px): wide enough that the centres of Starke (50 units from N), LaPorte (82) and southern Porter (93) lie in or at the band's soft end, as the 12:20 entry says they do.
Underline boxes, measured on the crop by a row and column scan: `several` is the last word of line 3, crop x 1283 to 1402, line box y 99 to 122; `tornadoes are expected` is the first three words of line 4, crop x 53 to 429, line box y 135 to 158. The phrase breaks across the two lines, so it takes two underlines.

## 3. Geometry (screen px)
A1-S2, state MIDWEST-STRIP:
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-2 group `map-states` inlined, ids prefixed `strip-`; outlines and fills as `media/maps/README.md` "Lines and colours to mount with" (the file's 2 px lines, `vector-effect="non-scaling-stroke"`). BM-2's `map-points` group is not shown: no town dot in this comp |
| Band | inside the map SVG, in map units so it rides the camera: one straight stroke from M (-266.0, 498.3) to N (440.2, 295.8), `stroke-width` 180 units (it must scale with the map, so no `non-scaling-stroke` on it), round caps, Amber 2 `#e8c56a` at 25 % (the family's forecast-area value, as `g-a1s09-forecasts`), edge softened by a 6-unit blur, no outline. On screen: from (643.7, 445.9) to (1341.9, 245.7), 178 px wide. Drawn from the Missouri end by a clip that grows along the line |
| State labels | fixed HUD, Arial 700 22 px, Label grey, tracking 2, centred: `MISSOURI` on (589, 586); `INDIANA` on (1342, 489). Both clear of the band (its lower edge is y 535 at the Missouri end and y 335 at the Indiana end) |
| Source card | quote strip as the built `compositions/g-i1s3-cloud.html` `.cloud-strip` (Beige polaroid, its shadow): left 96, top 740, 1100 x 200 (x to 1196, y to 940). Quote in two lines, Georgia 40 px, Caption dark: `“did not indicate any immediate tornado threat to any portion of Indiana”`. Attribution under it, Arial 700 22 px, Caption dark sub, tracking 2: `Disaster Research Center, 1966, p. 6` |
A1-S3, state NORTH:
| Element | Px |
|---|---|
| County lines | BM-1 groups `map-counties` and `map-state` inlined in the same SVG, ids prefixed `strip-`, hidden in A1-S2, fading in during the push; county lines 1.5 px, Indiana's outline 3 px. BM-1's `map-neighbours` and `map-points` are not inlined (BM-2 already draws the neighbours) |
| Clock stamp | design sheet section 8, as the built `compositions/g-t1s2-warning.html`: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `12:20 PM` / `South Bend, Indiana`; hour hand 10 degrees, minute hand 120 degrees (clockwise from 12). `12:20 PM` is eight characters: set it the way the built `compositions/g-i1s4-states.html` sets `11:45 AM` in the same card, and read its right edge in a frame |
| Lit counties | fill Amber 2 `#e8c56a` at `fill-opacity` 0.45 (the value of `g-a2s14-six`) on `strip-co-in-starke` and `strip-co-in-laporte`, whole |
| Southern Porter | a rect at the same fill clipped to `strip-co-in-porter` (clipPath), from map y 227.6 to 272.9 (screen y 246.8 to 382.7; the county is screen x 851 to 963, y 111 to 383). Its top 8 px fade to nothing (linear gradient mask): the split is schematic and shows no hard line. Northern Porter stays unlit |
| County names | Arial 700 22 px, Headline white with the credit shadow, tracking 2, centred on each county's area centroid, computed from the path by a script (the box centres, for a check: `LAPORTE` near (1046, 228), `STARKE` near (1051, 337)). Each name's box must lie inside its own county with no county line under it |
| `southern Porter` | the county is 111 px wide and the label about 175 px, so it sits over Lake Michigan (ground colour, no lines): same type, mixed case as written, centred on x 907, top 72. A 2 px Body light leader runs straight down from (907, 100) to (907, 290), ending 43 px inside the lit half; the builder's script checks that the whole leader lies inside `strip-co-in-porter` |
| Document card | design sheet section 9, lower band: left 96, top 600, 1480 x 373 (bottom 973); Beige polaroid border 10 px, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`; the crop 1460 x 353 inside at (106, 610). Top is 600, not the family's 640, because this crop is nine lines tall and the document source must clear the bottom margin |
| Underline 1 | Popfig red 6 px under `several`: screen x 1389 to 1508, y 736 to 742 |
| Underline 2 | Popfig red 6 px under `tornadoes are expected`: screen x 159 to 535, y 772 to 778 |
| Unlit page | Panel dark at 45 % over the whole crop except two boxes: x 1381 to 1516, y 703 to 736, and x 151 to 543, y 739 to 772; fades in over 0.4 s as underline 1 starts |
| Document source | under the card, right aligned at x 1560, top 987: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965, p. 37` |

## 4. Must be true in the picture
1. The band's Missouri end lies inside Missouri, in its north-east quarter; its Indiana end lies inside Indiana, north of the state's mid line; it crosses Illinois. It has no hard edge, no outline, no miles, no time.
2. The band is fully faded before any county line shows: no frame holds the band and a county edge together.
3. The source card's words are exactly the Picture note's quote, attributed to the study, and the card is gone before the stamp arrives.
4. The stamp reads `12:20 PM`: hour hand just past 12, minute hand on the 4. No part of the time is clipped by the card.
5. Lit: Starke whole, LaPorte whole, Porter south of its mid line only. Northern Porter, Lake, St. Joseph, Marshall and every other county stay unlit.
6. The Porter label reads `southern Porter`, never `PORTER` alone, and its leader ends inside the lit half.
7. The card is the page's own image; nothing on it is retyped. Underlines sit under `several` and `tornadoes are expected` and under no other words.
8. No town dot, no Alto, no tornado mark, no track in this comp.
9. This comp shows real county names from the Weather Bureau's own entry, so `County A` and `County B` never appear in it.
10. Line weights are the same at both ends of the push (read 9.65 and 10.62).
11. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680, entrances and exits included; all text at least 96 px from the sides and 54 px from top and bottom. The crop is on screen about 8.2 s and changes at 15.47 and 15.87 (underlines and unlit page).
Beat check (rule 13): the band draws for 2.0 s across the eight words that name its two ends. The source card is settled 4.99 to 9.39 (4.4 s, twelve words). Three counties 0.12 s apart, 0.3 s each: lit by 13.73.

## 5. Text (exact) and cues
Text: `MISSOURI` · `INDIANA` · `“did not indicate any immediate tornado threat to any portion of Indiana”` · `Disaster Research Center, 1966, p. 6` · `WEATHER BUREAU` · `12:20 PM` · `South Bend, Indiana` · `STARKE` · `southern Porter` · `LAPORTE` · `Weather Bureau survey report, 1965, p. 37`. Page words are the image.
Cue words and times are from `audio/a1-s2.words.json` and `audio/a1-s3.words.json` as they stood on 12 Oct 26 (wavs 9.17 and 10.87 s). Wav starts inside the comp, from `mg_specs/timeline-map.md` table 5: A1-S2 -0.25 (first sound 0.00, last 8.59), A1-S3 9.03 (first sound 9.39, last 19.56). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S2 | 0 | It | first sound 0.25 | 0.00 | first frame: ground and the map in MIDWEST-STRIP, state outlines only: no band, no label |
| 1 | A1-S2 | 5 | northeastern | 1.42 | 1.17 | the band starts to draw from the Missouri end (2.0 s, ease none, complete at 3.17) |
| 2 | A1-S2 | 6 | Missouri | 1.82 | 1.57 | `MISSOURI` fades in (0.3 s) |
| 3 | A1-S2 | 11 | Indiana. | 3.32 | 3.07 | `INDIANA` fades in (0.3 s) as the band reaches it |
| 4 | A1-S2 | 14 | study | 4.84 | 4.59 | source card rises in (`y: 60` to 0 with the fade, 0.4 s, power3.out) |
| 5 | A1-S3 | 0 | South | first sound 0.36 | 9.39 | source card leaves the way it came (`y: 0` to 60, opacity 1 to 0, 0.4 s, power3.in); `MISSOURI`, `INDIANA` and the band fade (0.3 s) |
| 6 | A1-S3 | 1 | Bend's | 0.66 | 9.69 | push MIDWEST-STRIP to NORTH (0.9 s, ends 10.59); county lines and Indiana's outline fade in during the move |
| 7 | A1-S3 | 4 | office | 1.58 | 10.61 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees onto the 4 |
| 8 | A1-S3 | 8 | its | 3.36 | 12.39 | document card rises in from below with a fade (`y: 80` to 0, opacity 0 to 1, 0.7 s, power3.out); the document source fades in after it |
| 9 | A1-S3 | 11 | Three | 4.16 | 13.19 | Starke, southern Porter, Laporte fill in the entry's order, 0.12 s apart (0.3 s each), each with its name; the leader draws with `southern Porter` |
| 10 | A1-S3 | 16 | several | 6.44 | 15.47 | unlit page fades in (0.4 s); underline 1 draws under `several` (0.2 s) |
| 11 | A1-S3 | 17 | tornadoes | 6.84 | 15.87 | underline 2 draws under `tornadoes are expected` (0.5 s). Hold to the last frame (20.56) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a1s02-strip.html` is the only file the builder writes; `data-composition-id="g-a1s02-strip"`; id prefix `strip-`; root `<div id="strip-root" ...>` styled through `#strip-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Style reference it matches:** the approved hook and intro set. For a map, `compositions/g-i1s2-station.html` (our Indiana outline in this coordinate space) and `compositions/g-i1s4-states.html` (labels over a map, the eight-character stamp). Stamp, page card, underline and unlit page from `compositions/g-t1s2-warning.html`; the source card from `compositions/g-i1s3-cloud.html`.
**Family base role (plan section 5, builder 1-a):** the second map base, built after `g-a2s14-six` and copying its map block, NORTH state, lit-county fill, county-name type, stamp and card. What later comps copy from this one: the Midwest map (BM-2 with BM-1 over it in one SVG) and the push from a Midwest view into NORTH: `g-a1s09-forecasts` (wave 2, already briefed against it), `g-a5s16-toledo` (wave 4), `g-a6s07-power` (wave 5); and a forecast area as a 25 % amber fill. Send this comp alone for a full-size read before any copy.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/midwest-states.svg` (BM-2, viewBox -980 -1280 2220 2560, 148,112 bytes), `map-states` inlined.
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), `map-counties` and `map-state` inlined.
- `media/docs/survey-p37-1220pm-crop.png` (PC-01, 1460 x 353).
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136) inline, or the face of `compositions/g-t1s2-warning.html`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s02-strip`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card (the scan's type beside ours): that is the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 10.14 (mid push) forward and backward and match the frames. Line 6: the band's two ends, the two county-name centroids, the Porter split and the leader are computed from the map files by a script with the section 2 formulas and stated in the receipt, with the point-in-path results for M, for each name and for the leader.

## 8. Receipt
As template section 8, plus: the measured right edge of `12:20 PM` inside the stamp card.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): state outlines only in MIDWEST-STRIP, line weights as section 3. Then one settled frame per cue: 2.20 (band part drawn from the Missouri end, `MISSOURI` on), 3.60 (band complete, both labels clear of it), 5.40 (source card), 9.65 (card, labels and band gone, still MIDWEST-STRIP: line weight), 10.62 (NORTH, county lines on, no band: line weight), 11.40 (stamp at 12:20, time not clipped), 13.10 (card in, source under it), 13.90 (Starke, southern half of Porter and LaPorte lit, three names, leader inside Porter), 15.80 (underline 1, unlit page), 16.50 (both underlines), 20.40 (last frame).
