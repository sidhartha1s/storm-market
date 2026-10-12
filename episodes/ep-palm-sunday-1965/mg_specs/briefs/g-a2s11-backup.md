Host: id=g-a2s11-backup file=compositions/g-a2s11-backup.html start=371.61 duration=22.96 s (timeline-map.md; wav sum 22.01 s plus its gaps) track=2

# g-a2s11-backup · A2-S11, A2-S12, A2-S13 · County A's back up: told twenty minutes after, started too late, then the power (wave 2, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2). The root is styled through its id and is never `id="root"` (rule 3). The study's hidden county is labelled `County A` only, and `County B` never appears in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A2-S11):** "County A's civil defense director found out when a local police officer came to the director's home. That was twenty minutes after the tornado hit."
**Spoken (A2-S12):** "Civil defense there saw part of its job as the back up for radio and TV. Its plan started after the first tornado had already passed through."
**Spoken (A2-S13):** "And when the tornadoes knocked out the power there, anyone listening on a plug in set was cut off."
**One look:** a dark house with a clock that fills to twenty minutes; then the chain with a dotted back-up path that lights only after a tornado mark has crossed; then a living room where the screen and the window go dark.

## 0. What this graphic claims
In County A the civil defense director learned of the tornado at home, from a police officer, twenty minutes after it hit. Civil defense there counted itself the back up for radio and TV, and its plan began after the first tornado had passed. When the power failed there, anyone on a plug-in set lost the broadcast.

## 1. Source
- `edit_script.md` A2-S11 (Rows [C1; study printed p. 20]), A2-S12 (Rows [C3; study printed p. 20]), A2-S13 (Rows [D, County A row; study printed p. 19]). All three are County A.
- The two quote strips carry the Picture notes' words: `until twenty minutes after it hit` and `too late`, both attributed `Disaster Research Center, 1966, p. 20`. The page itself is not shown.
- Chain slots: design sheet section 6 "Intro version" and the built `compositions/g-i1s9-chain.html`. Living room: design sheet section 7 and the built `compositions/g-i1s1-house.html`.

## 2. Datum, scale, orientation
Three views in one comp. View 1 (A2-S11): the house large, ground line y 830. View 2 (A2-S12): the chain line y 520 with the microphone and the house in the intro's station 4 and 5 slots; the back up is a second path below the line. View 3 (A2-S13): the living room, floor line y 820.
The clock in view 1 counts elapsed time, not the hour: it has no hour hand, the minute hand starts at 12, and 20 minutes is 120 degrees clockwise.

## 3. Geometry (screen px)
All views: canvas gradient ground from frame 0. County chip: glass chip, left 96, top 96, height 46, padding 0 x 22, Arial 700 26 px, Body light: `County A`, on from the first frame to the last.

View 1, A2-S11:
| Element | Px |
|---|---|
| Ground line | y 830, x 96 to 1560, 4 px Label grey |
| House | `media/drawings/house.svg` inline, `translate(280 330) scale(2)` (box x 280 to 800, y 330 to 830, aerial to y 262), `stroke-width="3"` on the group (6 px lines); dark: lines Label grey at 55 %, windows Panel dark |
| Clock | `media/drawings/wall-clock.svg` inline, `translate(900 420) scale(1.6)` (box x 900 to 1098, y 420 to 618; centre (999.2, 519.2)), `stroke-width="3.5"`; `dw-hour` hidden; `dw-minute` at 0 degrees |
| Arc | centre (999.2, 519.2), radius 113, 0 to 120 degrees, Amber 2, 10 px, round caps |
| Clock label | glass chip, left 1130, top 492, height 56, padding 0 x 22, Arial Black 900 32 px, Amber 2: `20 minutes after` |
| Quote strip | Beige polaroid, left 96, top 870, 1480 x 120 (right 1576, bottom 990), shadow as design sheet section 9. Quote, Georgia 52 px, Caption dark, left 136, top 882: `“until twenty minutes after it hit”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 950: `Disaster Research Center, 1966, p. 20` |

View 2, A2-S12:
| Element | Px |
|---|---|
| House | the same element, moved to `translate(1400 430) scale(0.68)` (box x 1400 to 1577, y 430 to 600); `stroke-width` tweened to 5; still dark |
| Microphone | `media/drawings/microphone.svg` inline, `translate(1170 420) scale(0.85)`; lines Body light, lamp Panel dark |
| Chain link | y 520, x 1272 to 1400, dotted (4 px dots, 14 px gap), Label grey |
| Labels, Arial 700 22 px, Label grey, top 676 | `radio and TV` centred on x 1221; `a family` centred on x 1488 |
| Civil defense desk | `media/drawings/desk.svg` inline, `translate(840 770) scale(0.85)` (box x 840 to 1095, y 770 to 898; top surface y 804); lines Body light |
| Desk label | `civil defense`, same type, centred on x 967, top 912 |
| Back-up path | straight dotted line from (1095, 804) to (1488, 606), 4 px dots, 14 px gap, Label grey; it passes between the two labels at top 676 |
| Path label | `the back up`, Arial 700 22 px, Label grey, left 1110, top 820 (below the path's start) |
| Tornado mark | `media/drawings/tornado-mark.svg` inline, scale 2 (120 x 160 px), `stroke-width="3"`, stroke Body light, never red; it crosses left to right with its box at y 150 to 310, from x -140 to x 1940 |
| Path light | an Amber 2 run, 60 px long, 6 px, from the desk end to the house end; the path stays Amber 2 at 60 % behind it |
| Quote strip | Beige polaroid, left 96, top 200, 620 x 150. Quote, Georgia 52 px, Caption dark, left 136, top 216: `“too late”`. Attribution as above, left 136, top 296 |

View 3, A2-S13: the living room of design sheet section 7 exactly as built in `compositions/g-i1s1-house.html` (floor line y 820; window frame x 180 to 520, y 220 to 600; armchair; television `media/drawings/television.svg` at 1.5 scale, box x 760 to 1210, y 460 to 820; side table and table radio). Screen area at this scale: x 790 to 1078, y 490 to 730, corner radius 36. Programme state as `media/drawings/README.md` "Television screen", scaled by 1.5 / 3.2: four bars 80 px apart, each 26 px tall, all moving down 80 px in 2.667 s, ease none, finite repeats. Window fill Amber 2 at 30 % until its cue, then Panel dark.

## 4. Must be true in the picture
1. `County A` is on screen in every frame, in the same place, and is the only county label.
2. The view 1 clock has no hour hand and prints no time of day: it says `20 minutes after` and nothing else. The arc is 120 degrees.
3. The house in view 1 is dark and stays dark: no window lights when the director "found out". No person, no officer and no car is drawn.
4. In view 2 the tornado mark has left the frame before any amber shows on the back-up path. The path's light never reaches the house before the mark has gone.
5. The house and the microphone stay dark in view 2: the back up lit late and the strip says `too late`.
6. In view 3 the screen goes Programme to Idle in one hard cut (one 0.1 s flash at 30 %), then the window goes dark. The drawing shows no switch, plug or the word "off". The table radio's dial stays unlit here (the battery radio belongs to A3-S13).
7. Both quote strips carry their attribution. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `County A` · `20 minutes after` · `“until twenty minutes after it hit”` · `Disaster Research Center, 1966, p. 20` (twice) · `radio and TV` · `a family` · `civil defense` · `the back up` · `“too late”`.
Cue words and times are from `audio/a2-s11.words.json`, `a2-s12.words.json`, `a2-s13.words.json` as re-transcribed on 12 Oct 26 (17:45 to 17:50; the transcriber writes A2-S12's first word as "Sible", the spoken word is "Civil"). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S11 -0.16, A2-S12 7.98, A2-S13 16.96) plus the word's time; a segment's first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S11 | 0 | County | 0.16 | 0.00 | first frame: ground, ground line, chip `County A` |
| 1 | A2-S11 | 2 | Civil | 0.72 | 0.56 | the house draws on, dark (0.8 s) |
| 2 | A2-S11 | 12 | came | 3.40 | 3.24 | the clock draws on beside the house (0.5 s), minute hand at 12 |
| 3 | A2-S11 | 17 | That | 5.36 | 5.20 | the minute hand sweeps 0 to 120 degrees and the arc grows with it (0.8 s, ease none) |
| 4 | A2-S11 | 19 | 20 | 5.78 | 5.62 | chip `20 minutes after` lands (0.3 s, `y:16` to 0 with the fade) |
| 5 | A2-S11 | 24 | hit. | 7.20 | 7.04 | quote strip 1 rises (`y:60` to 0 with the fade, 0.4 s, power3.out) |
| 6 | A2-S12 | 0 | Sible | 0.32 | 8.30 | strip 1, the clock, its arc and label leave (0.4 s); the house moves to its chain slot (`logZoom`, 0.8 s); the ground line fades out |
| 7 | A2-S12 | 1 | Defense | 0.58 | 8.56 | the civil defense desk draws on (0.5 s), label `civil defense` |
| 8 | A2-S12 | 10 | backup | 2.62 | 10.60 | the back-up path draws from the desk to the house (0.6 s), Label grey; label `the back up` |
| 9 | A2-S12 | 12 | radio | 3.22 | 11.20 | the microphone draws on with its dotted link to the house (0.5 s); labels `radio and TV` and `a family` |
| 10 | A2-S12 | 18 | after | 5.86 | 13.84 | the tornado mark crosses the frame left to right (ease none; it is out of frame at 15.24) |
| 11 | A2-S12 | 23 | already | 7.26 | 15.24 | the mark has gone; nothing else changes yet |
| 12 | A2-S12 | 25 | through. | 7.88 | 15.86 | the light runs the back-up path, desk to house (0.5 s); 0.5 s after this cue (16.36) quote strip 2 rises |
| 13 | A2-S13 | 0 | And | 0.22 | 17.18 | the chain layer pushes in on the house's left window (`logZoom` 1 to 6 about screen (1446, 528), 0.5 s) and the living room fades in over the last 0.2 s: screen on Programme, window amber |
| 14 | A2-S13 | 5 | out | 1.44 | 18.40 | the screen cuts Programme to Idle (hard cut, one 0.1 s flash) |
| 15 | A2-S13 | 7 | power | 1.76 | 18.72 | the window's fill goes Amber 2 to Panel dark (0.2 s) |
| 16 | A2-S13 | 9 | anyone | 2.60 | 19.56 | a slow push on the television starts (scale 1 to 1.06 about its screen, ease none, to 22.96) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s11-backup.html` is the only file the builder writes; `data-composition-id="g-a2s11-backup"`; id prefix `backup-`; root `<div id="backup-root" ...>` styled through `#backup-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the chain family bases `compositions/g-a4s02-countyb.html` and `compositions/g-a1s13-chain.html` (wave 1; briefs `mg_specs/briefs/g-a4s02-countyb.md`, `mg_specs/briefs/g-a1s13-chain.md`) for the county chain, dotted paths and the travelling light; the living room and the push through the window of the built `compositions/g-i1s1-house.html`; the clock arc is shared with `compositions/g-a2s06-headstart.html` (wave 1). `g-a3s13-battery` copies view 3 from this comp.
**Assets (paths from the episode folder):** `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298), `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136), `media/drawings/microphone.svg` (object 120 x 230), `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184), `media/drawings/tornado-mark.svg` (object 60 x 80, line 6), `media/drawings/television.svg` (object 300 x 240, line 2): inlined, ids under `backup-`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s11-backup`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 5 here: read a frame at 14.50 to prove the crossing mark passes over no label. Line 6 here: the arc's 120 degrees, the clock pivot and the back-up path's two ends are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground line and chip. Then settled frames: 1.60 (house, dark), 4.00 (clock, hand at 12), 6.20 (arc at 120 degrees, chip on), 7.60 (strip 1), 9.30 (house in its chain slot, desk), 11.00 (back-up path, grey), 12.00 (microphone, labels), 14.50 (mark mid frame, path still grey), 15.50 (mark gone, path grey), 16.90 (path amber, strip 2, house dark), 17.90 (living room, Programme, window amber), 18.60 (screen Idle, window amber), 19.20 (window dark), 22.80 (last frame).
