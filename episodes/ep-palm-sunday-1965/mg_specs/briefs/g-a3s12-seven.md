Host: id=g-a3s12-seven file=compositions/g-a3s12-seven.html start=580.05 (timeline-map.md table 1; the mount in index.html wins) duration=7.59 s (wav 7.04 s plus its gaps) track=2

# g-a3s12-seven · A3-S12 · named at 7:00, hit at 7:45 (wave 3, clock family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 8, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A3-S12):** "A station said its area wasn't named in the warnings until seven o'clock. Its transmitters were hit at seven forty five."
**One look:** two clocks side by side, 7:00 and 7:45, and the amber arc of the minutes between them.

## 0. What this graphic claims
A station told the researchers that its own area was not included in the warnings until 7:00 PM, and that its transmitters were hit at 7:45. Both times are the station's own, quoted.

## 1. Source
- `edit_script.md` A3-S12, Row [C8; study printed p. 25], with the writer's note: the study does not say whether this is the station of A3-S11, and gives no county.
- Quote strip words, from the Picture note: "our immediate vicinity was not included until 7:00 p.m. and our transmitters were hit at 7:45", attribution "media personnel · Disaster Research Center, 1966". The page is not shown.
- Clock face: `media/drawings/wall-clock.svg`. Card, time and place type: the clock family base `mg_specs/briefs/g-a2s06-headstart.md`.

## 2. Datum, scale, orientation
Two faces on one line, centres (231.2, 290.2) and (1011.2, 290.2), each 1.6 times the file. Clock angles, clockwise from 12 (by script): 7:00 is hour 210.0, minute 0; 7:45 is hour 232.5, minute 270. The left hands start at 6:55 (hour 207.5, minute 330). The arc is drawn on the right face, on the minute ring: from 0 degrees (7:00) clockwise to 270 degrees (7:45), radius 113, 532.5 px long by script. It is the family's device (the delay arc of `g-a2s06-headstart`, the "20 minutes after" arc of `g-a2s11-backup`): an amber arc on a face is the minutes that passed.
Colours and the glass card: as `mg_specs/briefs/g-a2s06-headstart.md` section 2 (the stamp of `compositions/g-t1s2-warning.html`).

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Chip | glass chip, left 96, top 84, height 46, padding 0 x 22, Arial 700 26 px, Body light: `a station` |
| Left card | glass card, left 96, top 150, 700 x 280 (right 796, bottom 430) |
| Left clock | `media/drawings/wall-clock.svg` inline, `translate(132 191) scale(1.6)`, `stroke-width="3.5"` on the group (box x 132 to 330.4, y 191 to 389.4; centre (231.2, 290.2)); hands end at 210.0 and 0 |
| Left time | `7:00 PM`, Courier New 700 84 px, Amber 2, left 376, top 236 (352.8 px wide by script, ends x 729) |
| Left line | `named in the warnings`, Arial 700 26 px, Body light, left 378, top 334 (measure it in a frame: it must end left of x 776) |
| Right card | glass card, left 876, top 150, 700 x 280 (right 1576, bottom 430). Dim state: the whole card at opacity 0.35 |
| Right clock | the same drawing, `translate(912 191) scale(1.6)` (centre (1011.2, 290.2)); hands start at 210.0 and 0 (7:00) and end at 232.5 and 270 (7:45) |
| Arc | circle arc on the right face, centre (1011.2, 290.2), radius 113, from 0 to 270 degrees clockwise, Amber 2, 10 px, round caps, grown with `strokeDashoffset` behind the minute hand |
| Right time | `7:45 PM`, same type as the left time, left 1156, top 236 (ends x 1509) |
| Right line | `transmitters hit`, same type as the left line, left 1158, top 334 |
| Quote strip | Beige polaroid, left 96, top 560, 1480 x 190 (right 1576, bottom 750), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote in two lines, Georgia 40 px, line-height 52, Caption dark, left 136: line 1 top 580 `“our immediate vicinity was not included until 7:00 p.m.`, line 2 top 632 `and our transmitters were hit at 7:45”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 700: `media personnel · Disaster Research Center, 1966` |
| Source line | none: the strip's attribution is the frame's source (design sheet section 10) |

## 4. Must be true in the picture
1. The left face reads 7:00: hour hand on the 7 tick, minute hand on 12. The right face ends at 7:45: hour hand three quarters of the way from 7 to 8, minute hand on the 9 tick.
2. The arc runs clockwise from 12 to 9 on the right face, three quarters of the ring, and is complete only when the minute hand stops. No figure for the gap is printed anywhere: the script gives two times, not a number of minutes.
3. Each time lands on its own sentence. The right card is dim until the second sentence, and the second line of the quote is hidden until "forty five".
4. Both times read `PM`. The quote keeps its own `7:00 p.m.` and `7:45` exactly.
5. **Kept apart from `g-a3s11-onoff`:** no microphone, no ON AIR lamp, no blink, and no word such as "same" or "that station". The chip reads `a station` and nothing more. No county, no town, no call letters.
6. The two cards are two moments of one account and both carry the one attribution on the strip.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `a station` · `7:00 PM` · `named in the warnings` · `7:45 PM` · `transmitters hit` · `“our immediate vicinity was not included until 7:00 p.m.` · `and our transmitters were hit at 7:45”` · `media personnel · Disaster Research Center, 1966`.
Cue words and times are from `audio/a3-s12.words.json` as it is on disk on 12 Oct 26 (19:32). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S12 -0.25) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds. The transcript writes the spoken "seven" as `7` and "forty five" as `.45.`.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S12 | 0 | A | 0.25 | 0.00 | first frame: ground, both card shells (right one dim), the left face with its hands at 6:55, the right face with its hands at 7:00 inside the dim card |
| 1 | A3-S12 | 1 | station | 0.34 | 0.09 | chip `a station` comes in (0.3 s) |
| 2 | A3-S12 | 6 | named | 1.76 | 1.51 | left line `named in the warnings` comes in (0.3 s) |
| 3 | A3-S12 | 10 | until | 2.68 | 2.43 | the left hands sweep from 6:55 to 7:00 (0.34 s, power3.out), arriving on the next cue |
| 4 | A3-S12 | 11 | 7 | 3.02 | 2.77 | `7:00 PM` lands (0.2 s, `y:16` set at 0, to 0, with the fade). 0.30 s after this cue (3.07) the strip rises with line 1 only (`y:60` set at 0, to 0, with the fade, 0.4 s, power3.out) |
| 5 | A3-S12 | 14 | Its | 4.42 | 4.17 | the right card comes up from 0.35 to full (0.3 s) |
| 6 | A3-S12 | 17 | hit | 5.30 | 5.05 | right line `transmitters hit` comes in; the right hands start their run from 7:00 to 7:45 and the arc grows behind the minute hand (0.76 s, ease none) |
| 7 | A3-S12 | 19 | 7 | 5.68 | 5.43 | `7:45 PM` lands (0.2 s) |
| 8 | A3-S12 | 20 | .45. | 6.06 | 5.81 | the hands stop at 7:45 and the arc is whole; line 2 of the quote and the attribution fade in (0.3 s). Hold to 7.59 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s12-seven.html` is the only file the builder writes; `data-composition-id="g-a3s12-seven"`; id prefix `seven-`; root `<div id="seven-root" ...>` styled through `#seven-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the clock family base `compositions/g-a2s06-headstart.html` (wave 1; brief `mg_specs/briefs/g-a2s06-headstart.md`): the two glass cards, the clock mount, the time and line type, the arc's radius, weight and caps. Copy them once that base has passed its read. No later comp copies this one.
**Assets (paths from the episode folder):** `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136, line 4, ticks 3, hands 5; `dw-hour` and `dw-minute` turn about (62, 62)): inlined twice, ids under `seven-`. `svgOrigin` for each hand is set once at build, before any tween, in the comp SVG's own units: (231.2, 290.2) left, (1011.2, 290.2) right.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s12-seven`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 5.40 forward, then seek 0, 7.0 and back to 5.40; the minute hand and the arc's end must sit at the same angle in both captures. Line 6: the four hand angles and the arc length are computed by script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): both shells, left hands at 6:55, right card dim. Then settled frames: 0.50 (chip), 2.00 (left line), 3.00 (left hands at 7:00, `7:00 PM`), 3.60 (strip with line 1 only), 4.60 (right card full, hands at 7:00), 5.40 (hands mid run, arc behind the hand, `7:45 PM` not yet), 5.70 (`7:45 PM`), 6.30 (7:45, arc whole, line 2 and attribution), 7.50 (hold).
