Host: id=g-a2s14-six file=compositions/g-a2s14-six.html start=394.32 (timeline-map.md, 12 Oct 26; the mount in index.html wins) duration=10.39 s track=2

# g-a2s14-six · A2-S14 · the 6:00 PM warning: four counties, and the three places it named (wave 1, map family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 7 (this comp's row: the push in). Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; Donaldson and Plymouth get hand-placed labels; inlined map ids take this comp's prefix; line weight is read at both ends of the zoom (rule 20).
**Spoken (A2-S14):** "At six o'clock South Bend warned four counties to take emergency precautions for the next thirty to sixty minutes. That was just about when the tornadoes first started touching down."
**One look:** a clock at six, four counties lit, the warning's own typed lines under them; then the map moves in on one county and three marks stand where the warning said tornadoes already were.

## 0. What this graphic claims
At 6:00 PM South Bend warned St. Joseph, Marshall, Elkhart and Kosciusko counties to take emergency precautions "during the next 30 to 60 minutes". The same entry names confirmed tornadoes at three places only: Plymouth, Argos and Donaldson, all in Marshall County.

## 1. Source
- `edit_script.md` A2-S14, Rows [A8; survey printed p. 39] · [A8; study printed p. 14].
- Page crop `media/docs/survey-p39-600pm-crop.png` (PC-03, 1460 x 283, survey printed p. 39). Its seven lines, read on the file: `Issued at 6:00 PM EST.` / `Radio and TV stations are requested to use Emergency Warning Signal.` / `Confirmed tornadoes have been reported just north of Plymouth and from Marshall` / `to Argos Indiana. This last one was seen in the vicinity of Donaldson Indiana` / `just east of Hamlet on US 30 moving in a east northeast direction.` / `Persons in St Joseph Marshall Elkhart and Kosciusko Counties in the path of` / `these storms should take emergency precautions during the next 30 to 60 minutes.`
- The entry gives places, not coordinates. A mark stands at each named town's dot and claims no path, no width and no time of its own.
- Positions: `media/data/points.csv` (US Census gazetteer), map units: `pt-south-bend` (462.2, 188.5), `pt-plymouth` (455.7, 249.1), `pt-argos` (464.1, 269.6), `pt-donaldson` (439.9, 246.6). Counties: `media/maps/indiana-counties.svg`, boxes read from the file: `co-in-st-joseph` x 429.4 to 488.8, y 173.0 to 233.5; `co-in-marshall` x 437.0 to 489.4, y 224.9 to 281.8; `co-in-elkhart` x 488.4 to 540.3, y 173.0 to 233.2; `co-in-kosciusko` x 486.5 to 540.6, y 232.8 to 305.8.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-1 in a fixed CSS box; the camera is its `viewBox`. `preserveAspectRatio="xMidYMid meet"`; both viewBoxes are 2.4 to 1, the box's own shape.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| NORTH (family state: every later map comp starts or ends here) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | first sentence |
| MARSHALL (this comp's) | 716, 62, 1080, 450 | `373 216 180 75` | 6.0 (screen x = 6u - 1522, y = 6u - 1234) | second sentence |
NORTH to MARSHALL is a push of 2.0 times in 0.8 s (power2.inOut), a `viewBox` move with the numbers moved geometrically (the `logZoom` maths of `library/inhouse/snippets/helpers.js` on a proxy with `onUpdate`, as the wave 2 briefs do) and its end values set exactly. Why the push: Plymouth and Donaldson are 16.0 map units apart, 48 px in NORTH, and a tornado mark is 45 px wide; in MARSHALL they are 96 px apart.
The box's bottom edge is y 512 and the card's right edge x 1576: the presenter corner (x >= 1600, y >= 680) stays empty.
Underline box, measured on the crop by a row and column scan (13 words on the last line, words 7 to 13): `during the next 30 to 60 minutes.` is crop x 853 to 1425, line box y 239 to 267.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `six-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px (the file's `vector-effect="non-scaling-stroke"` keeps them). Every `pt-` group hidden except the four named below, each from its cue. Dot radius 6 px on screen: `r` 2 map units in NORTH, 1 in MARSHALL (tween `r` with the push); fill Body light |
| Clock stamp | design sheet section 8, as the built `compositions/g-t1s2-warning.html`: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `6:00 PM` / `South Bend, Indiana`; hour hand 180 degrees, minute hand 0 degrees (clockwise from 12) |
| South Bend (NORTH) | dot (1214.6, 129.5); label `South Bend`, Arial 700 22 px, Body light, left 1232, top 118 |
| Lit county | fill Amber 2 `#e8c56a` at `fill-opacity` 0.45 on `six-co-in-st-joseph`, `six-co-in-marshall`, `six-co-in-elkhart`, `six-co-in-kosciusko`. This is the family's lit value: wave 2 briefs copy it |
| County names (NORTH) | Arial 700 22 px, Headline white with the credit shadow, tracking 2, centred on each county's box centre: `ST. JOSEPH` (1205, 174), `ELKHART` (1371, 173), `MARSHALL` (1218, 324), `KOSCIUSKO` (1369, 372) |
| Document card | design sheet section 9, in the family's lower band: left 96, top 640, 1480 x 303 (bottom 943); Beige polaroid border 10 px, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`; the crop 1460 x 283 inside at (106, 650) |
| Underline | Popfig red 6 px under `during the next 30 to 60 minutes.`: screen x 959 to 1531, y 921 to 927 (4 px under the line box) |
| Unlit page | Panel dark at 45 % over the whole crop except the box x 951 to 1539, y 883 to 921, fading in over 0.4 s as the underline starts |
| Document source | under the card, right aligned at x 1560, top 957: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965, p. 39` |
| Town dots (MARSHALL) | `six-pt-plymouth` (1212.2, 260.6), `six-pt-donaldson` (1117.4, 245.6), `six-pt-argos` (1262.6, 383.6) |
| Tornado marks | `media/drawings/tornado-mark.svg` inline three times at 0.75 scale (45 x 60 px, line 4.5 px), group stroke Body light, never red, on a fixed overlay above the map. Each mark's lowest point is 12 px straight above its dot's centre: Plymouth point (1212.2, 248.6), box x 1189.7 to 1234.7, y 188.6 to 248.6; Donaldson point (1117.4, 233.6), box x 1094.9 to 1139.9, y 173.6 to 233.6; Argos point (1262.6, 371.6), box x 1240.1 to 1285.1, y 311.6 to 371.6. Clear gap between the Donaldson and Plymouth marks: 49.8 px |
| Town labels (MARSHALL), placed by hand | Arial 700 22 px, Body light. `Donaldson`: right aligned to x 1088, top 235 (west of its dot, clear of Marshall's west line at x 1100). `Plymouth`: left 1228, top 262 (east of its dot, 13 px under its mark). `Argos`: left 1279, top 380 (east of its dot, 8 px under its mark) |
Marshall County in MARSHALL is screen x 1100 to 1414, y 115 to 457: whole, inside the box. St. Joseph, Elkhart and Kosciusko run off the box's top and right edges, still lit; that is intended.

## 4. Must be true in the picture
1. Exactly four counties are lit and they are St. Joseph, Marshall, Elkhart and Kosciusko. Starke, LaPorte and every other county stay unlit.
2. The stamp reads `6:00 PM`: hour hand straight down, minute hand straight up.
3. The card is the page's own image; nothing on it is retyped. The underline sits under `during the next 30 to 60 minutes.` and under no other words.
4. Exactly three tornado marks, at Plymouth, Argos and Donaldson. All three stand inside Marshall County's outline. None in St. Joseph, Elkhart or Kosciusko County. No Alto, no fourth place.
5. No mark carries a time, a path, a track line or a toll. Marks are Body light, never red (red in this world means nobody was told; these people were being told).
6. The Donaldson and Plymouth marks do not touch (about 50 px clear) and each label is nearer its own dot than any other dot. `Donaldson` is west of its dot, `Plymouth` east of its own.
7. Line weights and dot sizes are the same at both ends of the push (read 6.60 and 7.48). County names and `South Bend` are gone before the map moves.
8. This comp shows real county names from the Weather Bureau's public warning, so `County A` and `County B` never appear in it.
9. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom. The crop is on screen about 7.9 s (2.54 to 10.39) and changes at 3.86 (underline and unlit page).
Beat check (rule 13): three marks 0.15 s apart, each 0.3 s, labels 0.1 s behind: the last label is settled by 8.20, 2.19 s before the comp ends.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `6:00 PM` · `South Bend, Indiana` · `South Bend` · `ST. JOSEPH` · `MARSHALL` · `ELKHART` · `KOSCIUSKO` · `Weather Bureau survey report, 1965, p. 39` · `Plymouth` · `Argos` · `Donaldson`. Page words are the image.
Cue words and times are from `audio/a2-s14.words.json` as it stood on 12 Oct 26 (wav 9.93 s). The wav starts 0.26 s before the comp (`mg_specs/timeline-map.md` table 5: wav start inside the composition -0.26, first sound 0.00, last sound 9.39), so t from comp start = t in segment - 0.26. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S14 | 0 | At | first sound 0.26 | 0.00 | first frame: ground and the map in NORTH, lines only: no dot, no fill, no label |
| 1 | A2-S14 | 1 | 6 | 0.38 | 0.12 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees onto the 12. The transcriber writes "6", "o", "'clock," as words 1 to 3 |
| 2 | A2-S14 | 4 | South | 1.22 | 0.96 | South Bend dot and label (0.3 s fade) |
| 3 | A2-S14 | 7 | four | 1.90 | 1.64 | St. Joseph, Marshall, Elkhart, Kosciusko fill in the entry's order, 0.12 s apart (0.3 s each), each with its name |
| 4 | A2-S14 | 10 | take | 2.80 | 2.54 | document card slides in from the right (`x: 660` to 0, 0.7 s, power3.out); the document source fades in after it |
| 5 | A2-S14 | 13 | for | 4.12 | 3.86 | unlit page fades in (0.4 s); the underline draws left to right (0.6 s) |
| 6 | A2-S14 | 20 | That | 6.68 | 6.42 | the four county names and `South Bend` fade (0.2 s); the fills stay |
| 7 | A2-S14 | 21 | was | 6.92 | 6.66 | push NORTH to MARSHALL (0.8 s, ends 7.46); dot `r` 2 to 1 in the same tween |
| 8 | A2-S14 | 26 | tornadoes | 7.76 | 7.50 | Plymouth, Argos, Donaldson in the entry's order, 0.15 s apart: the dot comes on, its mark drops in (`y: -14` to 0 with the fade, 0.3 s), its label 0.1 s later. Hold to the last frame (10.39) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s14-six.html` is the only file the builder writes; `data-composition-id="g-a2s14-six"`; id prefix `six-`; root `<div id="six-root" ...>` styled through `#six-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Style reference it matches:** the approved hook and intro set. For a map, `compositions/g-i1s2-station.html` (the one built graphic with our own Indiana outline, in the same coordinate space as BM-1: its outline colours and dot) and `compositions/g-i1s4-states.html` (label type and the stamp sitting over a map). Stamp, page card, underline and unlit page from `compositions/g-t1s2-warning.html`.
**Family base role (plan section 5, builder 1-a):** this is the map base, built before `g-a1s02-strip`. Later map comps copy from it the way BM-1 is inlined and prefixed, the NORTH box and viewBox, the lit-county fill, the county-name type, the stamp at top left and the paper card in the lower band: `g-a1s02-strip` (wave 1), `g-a1s09-forecasts`, `g-a2s01-radar`, `g-a2s08-first`, `g-a2s16-huffman`, `g-a2s19-log` (wave 2, already briefed against these numbers), `g-a3s05-bremen`, `g-a4s16-fortwayne` (wave 3), `g-a5s01-radar`, `g-a5s04-berne`, `g-a5s07-marion`, `g-a5s10-alert`, `g-a5s16-toledo` (wave 4), `g-z1s04-drill` (wave 5). Keep the map block, the camera helper and the lit-county rule in plain, separate blocks so a copy is a paste. Send this comp alone for a full-size read before any copy.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/docs/survey-p39-600pm-crop.png` (PC-03, 1460 x 283).
- `media/drawings/tornado-mark.svg` (DR-03, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined three times.
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136) inline, or the face of `compositions/g-t1s2-warning.html`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s14-six`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card (the scan's type beside ours): that is the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 7.06 (mid push) forward and backward and match the frames. Line 6: every dot, mark point and county-name centre of section 3 is computed from `media/data/points.csv` and the county paths by a script with the section 2 formulas and stated in the receipt; the three town labels are the only things placed by hand, and their boxes are measured in a frame.

## 8. Receipt
As template section 8, plus: the measured clear gap between the Donaldson and Plymouth marks, and whether a CSS-free `viewBox` push left the line weights alone (the map README asks for this answer).

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map lines only in NORTH, line weights as section 3. Then one settled frame per cue: 0.90 (stamp at 6:00), 1.40 (South Bend), 2.40 (four counties and names), 3.50 (card in, source under it), 4.80 (underline complete, unlit page), 6.60 (names gone, still NORTH: line weight, dot size), 7.48 (MARSHALL, before any mark: line weight, dot size), 8.60 (three marks, three labels, none touching), 10.30 (last frame).
