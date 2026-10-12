Host: id=g-a3s05-bremen file=compositions/g-a3s05-bremen.html start=508.47 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=19.92 s (last sound at 18.88) track=2

# g-a3s05-bremen · A3-S5, A3-S6 · 7:10 PM: Bremen cannot be reached by phone, so a broadcast is the only way in (wave 3, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`. Base: `mg_specs/briefs/g-a2s14-six.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read at both ends of the zoom (rule 20). This comp shows a real town from the Weather Bureau's public message, so `County A` and `County B` never appear in it (rule 8).
**Spoken (A3-S5):** "At seven ten a tornado was just west of Bremen, moving toward it, and Bremen couldn't be reached by phone. South Bend asked radio and TV stations to use their emergency warning devices."
**Spoken (A3-S6):** "That left a broadcast as South Bend's way into the town, for anyone there who was listening. And listening took electricity."
**One look:** a clock at 7:10, a town with a tornado mark beside it and a telephone line into it that goes dark, a red ring on the town; then a microphone far to the left, one dotted arc reaching toward the town, and a plug under the microphone and under a house.

## 0. What this graphic claims
At 7:10 PM South Bend's own message said a tornado was just west of Bremen and that "Bremen cannot be contacted by phone." It asked radio and TV stations to use their emergency warning devices. So a broadcast was the one way left into the town, and hearing it took electricity. The picture does not say anyone in Bremen heard it.

## 1. Source
- `edit_script.md` A3-S5, Rows [A11; survey printed p. 41; study printed p. 17]; A3-S6, Rows [A11] (the writer's reading of the 7:10 message).
- The paper card's words are the survey's: `Bremen cannot be contacted by phone.`, source line `Weather Bureau survey, 1965, p. 41`. No image of survey p. 41 is on disk (`mg_specs/acts-plan.md` section 3c has none), so the six words are retyped on a quote strip, the lift of design sheet section 9, and are never dressed as a page.
- Positions: `media/data/points.csv` (US Census gazetteer), map units: `pt-south-bend` (462.2, 188.5), `pt-bremen` (477.2, 230.6). Map: `media/maps/indiana-counties.svg` (BM-1).
- "Just west" is the message's phrase. It gives no distance, so the mark's place is schematic: 60 px west of the dot (13.3 map units), on the dot's own latitude.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-1 in the family's fixed CSS box; the camera is its `viewBox` (both viewBoxes are 2.4 to 1).
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| NORTH (family state) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | first frame to step 2 |
| BREMEN (this comp's) | 716, 62, 1080, 450 | `392 178 240 100` | 4.5 (screen x = 4.5u - 1048, y = 4.5u - 739) | step 2 to the end |
NORTH to BREMEN is a push of 1.5 times in 0.8 s (power2.inOut), a `viewBox` move as the base does it (the `logZoom` maths on a proxy with `onUpdate`, end values set exactly). Dot radius 6 px on screen: `r` 2 map units in NORTH, 1.33 in BREMEN, tweened with the push.
In BREMEN, by script: South Bend (1031.9, 109.2); Bremen (1099.4, 298.7); Marshall County x 918.5 to 1154.3, y 273.1 to 529.1 (cut by the box's bottom edge, y 512); the Marshall and Elkhart county line stands near x 1150 beside Bremen.
Clock angles, clockwise from 12 (by script): 7:10 is hour 215.0, minute 60; the hands start at 7:05 (hour 212.5, minute 30).

## 3. Geometry (screen px; map elements are given in BREMEN)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `brm-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px. Every `pt-` group hidden except `brm-pt-south-bend` and `brm-pt-bremen`. No county is lit |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `7:10 PM` / `South Bend, Indiana`; hour hand 215.0, minute hand 60 degrees |
| South Bend | dot (1031.9, 109.2); label `South Bend`, Arial 700 22 px, Body light, left 1050, top 98. In NORTH the dot is (1214.6, 129.5) and the label left 1232, top 118, as the base; the label fades before the push and returns after it |
| Bremen | dot (1099.4, 298.7), fill Body light; label `Bremen`, Arial 700 22 px, Headline white, centred on x 1099, top 338 (under the dot; it clears the county line at x 1150 and the arc) |
| Telephone link | one 4 px line from (1035.3, 118.6) to (1092.7, 279.9), round caps (length 201 px less the two gaps). Beside its middle a telephone glyph: `media/drawings/telephone.svg` inline at 0.5 scale, `stroke-width="6"` (3 px lines), box left 1084, top 160, 51 x 53. Live: Body light. Dark: `stroke-dasharray="0.1 14"`, stroke `#55606b`, the glyph's lines `#55606b` |
| Tornado mark | `media/drawings/tornado-mark.svg` inline at 0.75 scale (45 x 60 px, line 4.5 px), stroke Body light, never red. Lowest point at (1039.4, 298.7): box x 1016.9 to 1061.9, y 238.7 to 298.7. It drifts 6 px east in all (box right edge 1067.9: 10 px clear of the link, 11.5 px clear of the ring) |
| Red ring | circle, centre (1099.4, 298.7), radius 20, 4 px Popfig red `#d0121f`, no fill, on a fixed overlay above the map |
| Quote strip (A3-S5) | Beige polaroid, left 96, top 700, 1100 x 124 (right 1196, bottom 824), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote, Georgia 52 px, Caption dark, left 136, top 712: `“Bremen cannot be contacted by phone.”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 782: `Weather Bureau survey, 1965, p. 41`. Measure the quote's width in a frame and state it; it must end at least 40 px inside the strip |
| Microphone | `media/drawings/microphone.svg` inline, `translate(330 340) scale(0.85)`, `stroke-width="4.7"` (box x 330 to 432, y 340 to 535.5), lines Body light, lamp (`dw-lamp`) Panel dark; label `radio and TV stations`, Arial 700 22 px, Label grey, centred on x 381, top 548 |
| Broadcast arc (A3-S6) | path `M432 400 Q760 440 1083 310.2`, 4 px Amber 2, dotted (`stroke-dasharray="0.1 14"`, round caps). By script it passes (563.0, 409.2), (758.8, 397.6), (1018.4, 334.5), (1050.7, 322.8): 113 px under the stamp, 24 px under the tornado mark, and it ends on the ring's lower left |
| House (A3-S6) | `media/drawings/house.svg` inline, `translate(1160 336) scale(0.4)`, `stroke-width="7.5"` (3 px lines; box x 1160 to 1264, y 336 to 436, aerial to y 322.4), lines Label grey, windows Panel dark; label `a home in the town`, Arial 700 22 px, Label grey, left 1276, top 376 |
| Plug under the microphone | `media/drawings/plug-cord.svg` inline, `translate(351 590)`, scale 1 (60 x 40; box x 351 to 411, y 590 to 630), stroke Body light |
| Plug under the house | the same file, `translate(1188 446) scale(0.8)`, `stroke-width="5"` (4 px lines; box x 1188 to 1236, y 446 to 478), stroke Body light |

## 4. Must be true in the picture
1. The stamp reads `7:10 PM`, hour hand between 7 and 8, minute hand on the 2.
2. The tornado mark is west of Bremen's dot (left of it, same height) and never touches the ring. It carries no path, time or toll and is never red.
3. The telephone link goes dark and stays dark. The red ring lands on Bremen only after the link is dark. The ring is the only red on the map: here red means the town could not be told by phone.
4. The strip carries the survey's six words in quotation marks and its attribution, and nothing else from the page. It is a strip, not a page: no page border, no typescript face.
5. The house's windows are never amber and its lines never turn white: the picture does not say the broadcast was heard. The arc is dotted from first to last.
6. The arc starts at the microphone and ends at the town's ring; it never passes through the stamp, the tornado mark or a label.
7. The microphone stands off the map (x 330 to 432) and carries no call letters; its label is `radio and TV stations`.
8. Line weights and dot sizes are the same at both ends of the push (read 0.90 and 1.90). `South Bend` is hidden while the map moves.
9. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom. No label sits on a county line: read `Bremen` and `South Bend` against the map at 5.00.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `7:10 PM` · `South Bend, Indiana` · `South Bend` · `Bremen` · `“Bremen cannot be contacted by phone.”` · `Weather Bureau survey, 1965, p. 41` · `radio and TV stations` · `a home in the town`.
Cue words and times are from `audio/a3-s5.words.json` (33 words) and `audio/a3-s6.words.json` (21 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S5 -0.47, A3-S6 11.72) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 11.98). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S5 | 0 | At | 0.47 | 0.00 | first frame: ground and the map in NORTH, lines only |
| 1 | A3-S5 | 1 | 7 | 0.60 | 0.13 | clock stamp slides in from the left (`x:-660` set at 0, to 0; 0.6 s, power3.out); the minute hand sweeps 30 to 60 and the hour hand 212.5 to 215.0. South Bend's dot and label fade in. The transcriber writes "7", ".10," as words 1 and 2 |
| 2 | A3-S5 | 4 | tornado | 1.46 | 0.99 | `South Bend` fades (0.1 s), then the push NORTH to BREMEN (0.8 s, done at 1.89); the label returns at its BREMEN place |
| 3 | A3-S5 | 9 | Bremen, | 2.70 | 2.23 | Bremen's dot and label (0.3 s fade); 0.15 s later the tornado mark drops in west of it (`y:-14` to 0 with the fade, 0.3 s) |
| 4 | A3-S5 | 10 | moving | 3.34 | 2.87 | the mark drifts 6 px east (ease none, to 4.45) and stops |
| 5 | A3-S5 | 14 | Bremen | 4.56 | 4.09 | the telephone link draws from South Bend to the town (`strokeDashoffset`, 0.3 s) with its glyph, Body light |
| 6 | A3-S5 | 15 | couldn't | 4.92 | 4.45 | the link turns dotted and `#55606b`, the glyph dark (0.25 s) |
| 7 | A3-S5 | 17 | reached | 5.34 | 4.87 | the red ring comes on round Bremen (fade 0.2 s) |
| 8 | A3-S5 | 19 | phone. | 5.78 | 5.31 | the quote strip rises (`y:60` to 0 with the fade, 0.4 s, power3.out) |
| 9 | A3-S5 | 23 | radio | 7.92 | 7.45 | the microphone draws on (0.6 s) and its label fades in; the lamp stays dark |
| 10 | A3-S5 | 30 | emergency | 10.10 | 9.63 | the microphone's lines go Headline white and back to Body light (0.3 s each way) |
| 11 | A3-S6 | 0 | That | 0.26 | 11.98 | the quote strip slides out left with its fade (`x:-1300`, 0.5 s, power3.in) |
| 12 | A3-S6 | 3 | broadcast | 0.88 | 12.60 | the lamp turns Popfig red (0.2 s); the arc draws from the microphone toward the town, dot by dot (0.9 s, done at 13.50) |
| 13 | A3-S6 | 10 | town | 2.82 | 14.54 | the arc's dots go Headline white and back to Amber 2 in a wave from left to right (0.6 s) |
| 14 | A3-S6 | 12 | anyone | 3.58 | 15.30 | the house draws on beside the town (0.5 s), dark, with its label |
| 15 | A3-S6 | 17 | And | 5.64 | 17.36 | the plug and cord draw on under the microphone (0.4 s) |
| 16 | A3-S6 | 20 | electricity. | 6.40 | 18.12 | the plug and cord draw on under the house (0.4 s). Hold to 19.92 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s05-bremen.html` is the only file the builder writes; `data-composition-id="g-a3s05-bremen"`, `data-duration="19.92"`; id prefix `brm-`; root `<div id="brm-root" ...>` styled through `#brm-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Family base it copies:** `compositions/g-a2s14-six.html` (wave 1), after it has passed its read: the inlined and prefixed BM-1 block, the NORTH box and viewBox, the camera helper, the stamp at top left, the tornado mark at 0.75 scale. The quote strip as `compositions/g-a1s13-chain.html` builds it. Nothing later copies this comp.
**Assets (paths from the episode folder, read on disk 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880), inlined.
- `media/drawings/tornado-mark.svg` (DR-03, object 60 x 80, viewBox -6 -6 72 92, line 6).
- `media/drawings/telephone.svg` (viewBox -6 -58 102 106, line 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4).
- `media/drawings/plug-cord.svg` (DR-08, object 60 x 40, viewBox -6 -6 72 52, line 4), inlined twice.
- The stamp's clock face: `media/drawings/wall-clock.svg` (DR-09, object 124 x 124, viewBox -6 -6 136 136) inline.
Mount rules: `media/drawings/README.md` and `media/maps/README.md`, which win over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s05-bremen`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 1.40 (mid push) forward and backward and match the frames. Line 5 here: read `Bremen`, `South Bend`, the glyph and `a home in the town` against county lines, the link and the arc at 5.00 and 16.00. Line 6 here: both dots, the link's two ends, the mark's box, the ring and the arc's sample points are computed from `media/data/points.csv` with the section 2 formulas by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus the measured width of the quote and the clear gap between the mark and the ring at 4.60.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map lines only in NORTH. Then: 0.90 (stamp at 7:10, South Bend, still NORTH: line weight, dot size), 1.90 (BREMEN: line weight, dot size, `South Bend` back), 2.80 (Bremen, the mark west of it), 4.35 (link and glyph live), 4.80 (link dark and dotted), 5.20 (red ring), 6.00 (strip, both lines read), 8.30 (microphone and label, lamp dark), 12.40 (strip gone), 13.60 (lamp red, arc complete, clear of stamp and mark), 16.00 (house and label, windows dark), 17.90 (plug under the microphone), 18.70 (plug under the house), 19.80 (last frame).
