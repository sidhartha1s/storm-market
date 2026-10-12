Host: id=g-a3s13-battery file=compositions/g-a3s13-battery.html start=587.64 (timeline-map.md table 1; the mount in index.html wins) duration=21.23 s (wavs 20.46 s plus their gaps) track=2

# g-a3s13-battery · A3-S13, A3-S14 · the sets go dark with the lights; one radio on batteries; one family in Fort Wayne (wave 3, living room)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 10, 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md` ("Ground under the television", "Television screen").
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). Design sheet S5: no real person is drawn, and no frame, title, logo, performer or name of a real show appears.
**Spoken (A3-S13):** "In many houses the sets went dark with the lights. Unless a family owned a battery powered transistor radio, it couldn't get any later warning."
**Spoken (A3-S14):** "In Fort Wayne, Kathy Selzer Miller remembers watching Ed Sullivan, with Herman's Hermits on, when the TV signal was lost. Then the power went out, she remembers, for three days."
**One look:** an evening living room that goes dark except for one small amber radio dial; then another room, a set that cuts out, and the light going after it.

## 0. What this graphic claims
When the power failed, the television and the plug-in radio in a house went dark with the lights; only a family with a battery radio could still get a later warning. One woman in Fort Wayne remembers exactly that order: the television signal was lost first, then the power went out.

## 1. Source
- `edit_script.md` A3-S13, Row [D; study printed p. 25]. Source line from the Picture note: `Disaster Research Center, 1966, p. 25`.
- `edit_script.md` A3-S14, Row [E, families; the Weather Service page, read by the fact check: "the Ed Sullivan Show with the Herman's Hermits performing and the tv signal was lost"; "then the power went out for 3 days"]. Name card and small line from the Picture note: `Kathy Selzer Miller · Fort Wayne`, `a recollection published by the National Weather Service`.
- The room: design sheet section 7 "Living room", as built in `compositions/g-i1s1-house.html` (the `house-room` layer: wall, floor band, window, armchair, television, side table, table radio). The screen states: `media/drawings/README.md` "Television screen".

## 2. Datum, scale, orientation
Two rooms, one after the other, never on screen together.
- **Room 1 (A3-S13)** is the intro's room as built: floor line y 820, window at the left, television in the middle, the side table and radio at the right.
- **Room 2 (A3-S14)** is the same drawing mirrored left to right about x 828 (one wrapper `<g transform="translate(1656 0) scale(-1 1)">`), without the side table and without the radio, so it reads as another family's room: window at the right, television left of centre.
- **Evening** is a scrim, not a new drawing. One full-frame Panel dark `<div>` sits above the wall and the floor band and below the furniture SVG. Evening level: opacity 0.62. Lights out: opacity 0.86. The furniture then reads by its own Label grey and Body light lines.
- The table radio's dial is the one Amber 2 thing in room 1 and it never goes out.
Camera (the room layer only; the name card, source line and scrim do not ride it): room 1 scale 1.00 to 1.12 about (1380, 646), ease none, from 0.00 to 9.24; room 2 scale 1.00 to 1.06 about (1200, 610), ease none, from 9.24 to 21.23. By script the floor line's right end stays at x 1581.6 in both, left of x 1600.

## 3. Geometry (screen px, before the camera)
Both rooms: wall Beige polaroid full frame; floor band `#e8dec8` (as built) from y 820 to 1080; floor line 4 px Panel dark, y 820, x 96 to 1560; the evening scrim above them.

Room 1, A3-S13 (copy the markup of the built `house-room` layer; change only what is listed):
| Element | Px |
|---|---|
| Window | frame rect x 180 to 520, y 220 to 600, one vertical bar at x 350, one horizontal at y 410, 4.4 px Panel dark; panes filled Panel dark (night outside), not the intro's sky |
| Armchair | as built, `translate(420 600) scale(1.1)` (box x 420 to 640, y 600 to 820), empty |
| Television | `media/drawings/television.svg` as built, `translate(760 460) scale(1.5)` (box x 760 to 1210, y 460 to 820; screen x 790 to 1078, y 490 to 730, radius 36), screen Idle with its reflection arc |
| Side table | as built: top x 1260 to 1500 at y 700, legs to y 820 |
| Table radio | as built, `translate(1290 592) scale(1.2)` (box x 1290 to 1470, y 592 to 700); lines Label grey at rest |
| Radio dial | circle centre (1424.4, 646), radius 26.4, fill Amber 2 at `fill-opacity` 0.55 from the first frame; the pointer runs from the centre to (1438.8, 629.2) and turns about the centre |
| Light patch | the built `house-patch` polygon is not drawn |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 25` |

Room 2, A3-S14 (the mirrored room):
| Element | Px |
|---|---|
| Window | x 1136 to 1476, y 220 to 600; panes Amber 2 at `fill-opacity` 0.3 (the room's light, design sheet section 7) until its cue, then Panel dark |
| Armchair | x 1016 to 1236, y 600 to 820, empty |
| Television | box x 446 to 896, y 460 to 820; screen x 578 to 866, y 490 to 730, radius 36 |
| Screen, Programme | a `<div>` over the screen area, clipped to its radius: Amber 2 at 22 % over Panel dark, four soft bars (Headline white at 10 %) 80 px apart, each 26 px tall, all moving down 80 px in 2.667 s, ease none, `repeat: 2` (three passes, 8.0 s, longer than the 6.56 s it is on screen). No figure, no stage, no title, no text |
| Screen, Idle | the drawing's own screen: Panel dark with the reflection arc |
| Name card | glass plate as `compositions/g-i1s2-station.html` `.stn-card` (same fill, blur, border, radius 28): left 96, top 96, 760 x 170 (right 856, bottom 266). Name `Kathy Selzer Miller`: Arial Black 900 52 px, Headline white, left 138, top 118. Sub `Fort Wayne`: Georgia italic 30 px, Amber 2, left 140, top 198. Measure the name's width in a frame and state it; it must end left of x 816 |
| Source line | same place and type: `a recollection published by the National Weather Service` |

## 4. Must be true in the picture
1. In room 1 the screen is idle from the first frame and nothing is ever shown on it. The radio's dial is amber from the first frame to the cut and is the only amber in the room after "lights".
2. The radio stands for a battery set by staying lit when the room goes dark. No battery, cord, plug or brand is drawn on it, and no words come out of it.
3. Room 2 is plainly another room: mirrored, no radio, no side table. It never appears before the first sound of A3-S14 (9.24).
4. In room 2 the order is the recollection's own: the screen cuts from Programme to Idle on "lost", and only then, on "out", does the window light go. Never both at once, never the other way round.
5. The switch from Programme to Idle is a hard cut with one 0.1 s flash of Headline white at 30 % over the screen area. Never a fade.
6. **No show.** The Programme state is the plain frame of the intro. The words "Ed Sullivan" and "Herman's Hermits" are never on screen, and no stage, singer, band, logo or title card is drawn (design sheet S5).
7. No person is drawn in either room; both armchairs are empty. The name card is the only sign of Kathy Selzer Miller, and it carries `Fort Wayne` and nothing else: no age, no street, no date.
8. No number of days is printed. "Three days" is her memory, spoken, and the picture does not turn it into a record.
9. Each source line shows only with its own room. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680: the floor line's right end is at x 1581.6 at the end of each push.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Disaster Research Center, 1966, p. 25` · `Kathy Selzer Miller` · `Fort Wayne` · `a recollection published by the National Weather Service`.
Cue words and times are from `audio/a3-s13.words.json` and `audio/a3-s14.words.json` as they are on disk on 12 Oct 26 (19:32). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S13 -0.22, A3-S14 8.98) plus the word's time; a segment's first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S13 | 0 | In | 0.22 | 0.00 | first frame: room 1 in the evening (scrim 0.62), window dark, screen idle, dial amber; the push starts |
| 1 | A3-S13 | 4 | sets | 1.24 | 1.02 | the television's inner lines rise from Label grey to Body light (0.2 s): the eye goes to the set. Source line fades in |
| 2 | A3-S13 | 6 | dark | 1.64 | 1.42 | the television's inner lines and reflection arc fall to `#55606b` (0.3 s) |
| 3 | A3-S13 | 9 | lights. | 2.36 | 2.14 | lights out: the scrim goes from 0.62 to 0.86 (0.25 s). The dial does not change |
| 4 | A3-S13 | 10 | Unless | 3.46 | 3.24 | the radio's lines rise from Label grey to Body light (0.3 s) |
| 5 | A3-S13 | 15 | battery | 4.70 | 4.48 | the dial's fill goes from 0.55 to full Amber 2 (0.2 s) and stays |
| 6 | A3-S13 | 18 | radio, | 5.86 | 5.64 | the dial's pointer turns 40 degrees clockwise and 20 back (0.6 s in all): someone is tuning it |
| 7 | A3-S13 | 20 | couldn't | 6.94 | 6.72 | the window, armchair and television fall to opacity 0.5 (0.4 s); the radio and its table do not. Hold on the push to 9.24 |
| 8 | A3-S14 | 0 | In | 0.26 | 9.24 | hard cut to room 2: scrim back at 0.62, window lit, screen on Programme with its bars moving; room 1 and its source line are gone; the second push starts |
| 9 | A3-S14 | 3 | Kathy | 1.56 | 10.54 | the name card slides in from the left (0.6 s, power3.out; `x:-860` set at 0, to 0), name then sub 0.15 s apart |
| 10 | A3-S14 | 6 | remembers | 2.34 | 11.32 | source line `a recollection published by the National Weather Service` fades in |
| 11 | A3-S14 | 7 | watching | 2.76 | 11.74 | the television's inner lines rise to Body light (0.3 s) |
| 12 | A3-S14 | 19 | lost. | 6.82 | 15.80 | the screen cuts from Programme to Idle with the 0.1 s flash |
| 13 | A3-S14 | 24 | out, | 8.66 | 17.64 | the window panes go Panel dark and the scrim goes from 0.62 to 0.86 (0.2 s) |
| 14 | A3-S14 | 28 | three | 10.50 | 19.48 | no new element: the dark room and the name card hold on the push to 21.23 |
Beat check (rule 13, by script): the Programme bars are on screen from 9.24 to 15.80, 6.56 s, inside three passes (8.0 s, ending 17.24); the state `<div>` is hidden at the cut, so no bar is seen after 15.80.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s13-battery.html` is the only file the builder writes; `data-composition-id="g-a3s13-battery"`; id prefix `batt-`; root `<div id="batt-root" ...>` styled through `#batt-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0 (the wall, the floor band and the scrim).
**Family base it copies:** the living room of the built `compositions/g-i1s1-house.html` (`house-room` layer, copied with ids renamed under `batt-`); the Programme and Idle screen states and the cut between them from `compositions/g-a2s11-backup.html` view 3 (wave 2; brief `mg_specs/briefs/g-a2s11-backup.md`) and `media/drawings/README.md`; the name card from the built `compositions/g-i1s2-station.html` as used in `mg_specs/briefs/g-a2s16-huffman.md`. No later comp copies this one.
**Assets (paths from the episode folder):** `media/drawings/television.svg` (object 300 x 240, viewBox -3 -3 306 246, line 2): inlined, ids under `batt-`. The armchair, side table and table radio have no file: they are the inline shapes of `compositions/g-i1s1-house.html`, copied as they stand.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s13-battery`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 is the evening room, not a black frame, and 9.24 is room 2 complete. Line 4: seek to 16.5 forward, then seek 0, 20.0 and back to 16.5; the screen must be Idle and the window still lit in both captures. Line 6: the mirrored boxes and both push end points are computed by script and stated in the receipt.
Read at the lights-out level in both rooms: the armchair, the television and the window frame must still separate from the wall. If they do not, lower the 0.86 to the highest value that keeps them apart and state it in the receipt; the evening level and the order of the changes do not move.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): room 1, evening, dial amber, screen idle. Then settled frames: 1.30 (set's lines bright, source line), 1.90 (set dark), 2.60 (lights out, dial the only amber), 3.80 (radio lines bright), 4.90 (dial full), 6.00 (pointer mid turn), 7.40 and 9.10 (room dimmed round the radio; floor line end left of x 1600). Room 2: 9.24 and 9.28 (cut complete, window lit, bars on the screen), 11.20 (name card, name inside its plate), 11.60 (second source line), 12.20 (set's lines bright), 15.70 (Programme, last frame before the cut), 15.85 (flash), 16.50 (Idle, window still lit), 18.00 (window dark, lights out, furniture still readable), 21.10 (hold, floor line end left of x 1600).
