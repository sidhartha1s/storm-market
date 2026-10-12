Host: id=g-a3s09-jam file=compositions/g-a3s09-jam.html start=545.63 (timeline-map.md table 1; the mount in index.html wins) duration=10.26 s (wav 10.10 s plus its gaps) track=2

# g-a3s09-jam · A3-S9 · everyone phones at once and nobody gets through (wave 3, drawing)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). The house count and every stagger are checked against the spoken window (rule 13).
**Spoken (A3-S9):** "People who lost their power tried to phone for more information. So many were calling that they couldn't get through, and offices trying to reach each other hit the same jam."
**One look:** five dark houses, five lifted telephones, five lines running to one point that says busy; then two offices whose own line dies at the same point.

## 0. What this graphic claims
People whose power had failed turned to the telephone for information. So many called at once that the calls did not get through, and the offices that needed to reach each other were stopped by the same overload.

## 1. Source
- `edit_script.md` A3-S9, Rows [D; study printed p. 25] and [D; study printed p. 17].
- Source line, from the Picture note: `Disaster Research Center, 1966, pp. 17 and 25`.
- No figure is drawn from: the study gives no count of calls, homes or offices. **Schematic, not to scale:** five houses and two desks stand for "many" and "offices".

## 2. Datum, scale, orientation
Houses in one row along the bottom, left to right, 220 px apart. Every line climbs to one busy mark at upper right, centre (1060, 300). The two offices stand to the right of the mark, on its far side from the houses. The lines are straight and do not cross (by script: the lowest clearance of any line over a later telephone's lifted handset is 76.7 px).
| House | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| House box x (y 755 to 880, aerial to y 738) | 96 to 226 | 316 to 446 | 536 to 666 | 756 to 886 | 976 to 1106 |
| Telephone `translate` x (y 670.8, scale 0.6) | 134 | 354 | 574 | 794 | 1014 |
| Line start (above the lifted handset) | (161, 636) | (381, 636) | (601, 636) | (821, 636) | (1041, 636) |
| Line end (dot under the mark) | (1000, 351) | (1030, 351) | (1060, 351) | (1090, 351) | (1120, 351) |
| Line length, px (by script) | 886.1 | 708.8 | 540.3 | 391.9 | 295.7 |

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Houses (5) | `media/drawings/house.svg` inline, `translate(<x> 755) scale(0.5)` with x from the table (each 130 x 125), `stroke-width="6"` on the group (3 px lines). Lit (first frame): lines Body light, windows (`dw-win`) Amber 2 at `fill-opacity` 0.3. Dark: lines `#55606b` (Label grey at 55 %, pre-mixed), windows Panel dark |
| Telephones (5) | `media/drawings/telephone-lifted.svg` inline (handset raised), `translate(<x> 670.8) scale(0.6)` with x from the table (body about 52 px wide, base y 697, lifted handset top y 638), `stroke-width="4"` on the `dw-phone` group (2.4 px lines); lines Body light. Each sits 41 px above its house's aerial and does not touch it |
| Call lines (5) | straight, 3 px, round caps, from the table's start to its end; Body light while running, Label grey once stopped. Each ends in a filled dot of radius 6 at its end point |
| Busy mark | a shape of ours, no brand: rounded rect x 985 to 1135, y 255 to 345 (150 x 90, radius 12), fill Panel dark, 4 px Body light stroke. Inside, three bars 26 x 10 px, radius 5, centred at (1024, 300), (1060, 300), (1096, 300), Label grey at rest. A blink is one bar turning Headline white for 0.25 s, the three in turn |
| Mark label | `line busy`, Arial 700 22 px, Label grey, centred on x 1060, top 215 |
| Office desks (2) | `media/drawings/desk.svg` inline, scale 0.85 (255 x 128 each): desk 1 `translate(1290 150)` (box x 1290 to 1545, y 150 to 278, top surface y 184), desk 2 `translate(1290 420)` (box y 420 to 548, top surface y 454); lines Body light |
| Desk labels | `an office`, Arial 700 22 px, Label grey, centred on x 1417, top 290 and top 560 |
| Office line | from desk 1, (1290, 184), to the mark's right side, (1141, 285): 180.0 px, 3 px, Body light, ending in a dot of radius 6 at (1141, 285). The second leg, (1141, 315) to desk 2 at (1290, 454), 203.8 px, is dotted Label grey (`stroke-dasharray="0.1 14"`, round caps) and never lights |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, pp. 17 and 25` |

## 4. Must be true in the picture
1. Every house has its own telephone and its own line, and all five lines end under the one busy mark. No line reaches past the mark.
2. The offices' line comes from the far side and ends at the same mark. The leg to the second desk stays dotted and grey: the offices do not reach each other.
3. The busy mark is not the stop mark of the police desk: it has no red and no cross, and it reads `line busy`. Nothing in this comp is Popfig red.
4. No light travels a line and arrives anywhere. A line that has stopped turns Label grey.
5. Five houses and two desks are not counts from the study: no number is printed, and no house, office, town or county is named. No person is drawn; the lifted handsets are the only sign of a caller.
6. The houses' windows are lit only in the first 0.88 s and are dark from "power" to the last frame.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680 (the houses end at x 1106, the desks at x 1545 and y 548).
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `line busy` · `an office` (twice) · `Disaster Research Center, 1966, pp. 17 and 25`.
Cue words and times are from `audio/a3-s9.words.json` as it is on disk on 12 Oct 26 (19:32). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S9 -0.52) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S9 | 0 | People | 0.52 | 0.00 | first frame: ground, the five houses with lit windows |
| 1 | A3-S9 | 4 | power | 1.40 | 0.88 | the windows go dark house by house, left to right, 0.12 s apart (a fill change, 0.1 s each), and each house's lines fall to the dark stroke with them |
| 2 | A3-S9 | 7 | phone | 2.30 | 1.78 | the five telephones draw on above the houses, handsets raised (0.3 s each, 0.1 s apart); source line fades in |
| 3 | A3-S9 | 10 | information. | 2.94 | 2.42 | the five call lines draw from the telephones to their end points (0.6 s each, 0.15 s apart, ease none; the last ends at 3.62), each end dot appearing as its line arrives |
| 4 | A3-S9 | 12 | many | 4.62 | 4.10 | the five end dots turn Headline white in turn and back, 0.1 s apart: the calls are piling up |
| 5 | A3-S9 | 17 | couldn't | 5.74 | 5.22 | the busy mark comes in over the pile (0.2 s fade, no scale) with `line busy`; its three bars blink once in turn (0.75 s); the five lines turn Label grey |
| 6 | A3-S9 | 21 | offices | 7.04 | 6.52 | the two desks draw on (0.5 s each, 0.2 s apart) with their labels |
| 7 | A3-S9 | 24 | reach | 7.90 | 7.38 | the office line runs from desk 1 to the mark (0.5 s, ease none) and stops in its dot; the dotted leg to desk 2 fades in, grey |
| 8 | A3-S9 | 30 | jam. | 9.30 | 8.78 | the bars blink once more in turn (0.75 s) and the office line turns Label grey. Hold to 10.26 |
Beat check (rule 13, by script): windows dark by 1.46 (four gaps of 0.12 s plus 0.1 s), before "phone" at 1.78; lines whole by 3.62, before "So" at 3.92; the second blink ends at 9.53, before the comp ends at 10.26.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s09-jam.html` is the only file the builder writes; `data-composition-id="g-a3s09-jam"`; id prefix `jam-`; root `<div id="jam-root" ...>` styled through `#jam-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** no single base (the plan's "Reuses" cell is "none"). Links, dots and the dotted style follow the chain family base `compositions/g-a1s13-chain.html` (wave 1; brief `mg_specs/briefs/g-a1s13-chain.md`); the house's lit and dark states follow `media/drawings/README.md`. No later comp copies this one.
**Assets (paths from the episode folder):** `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4; lit state values as `media/drawings/house-lit.svg`), `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106, line 3), `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, line 4, telephone 3): inlined, ids under `jam-`. The plan row lists `media/drawings/telephone.svg`; the handsets are raised from their first frame, so only the lifted file is mounted on the houses (the desks carry the cradled telephone inside `desk.svg`).

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s09-jam`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 5 here: read 5.30 and 5.50 for `line busy` against the incoming lines and dots. Line 6: the five house positions, line ends and lengths of section 2 are computed by script from one pitch (220 px) and one end spacing (30 px) and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): five lit houses. Then settled frames: 1.60 (all windows dark), 2.30 (telephones, handsets up, source line), 3.00 (lines part drawn, none crossing), 3.80 (five lines and dots), 4.30 (dots mid pile), 5.60 (busy mark and label, bars mid blink), 6.20 (lines grey), 7.30 (two desks and labels), 8.10 (office line stopped at the mark, dotted leg), 9.10 (bars mid blink), 10.20 (hold: everything stopped).
