Host: id=g-a4s14-eight file=compositions/g-a4s14-eight.html start=785.10 (timeline-map.md table 1; the mount in index.html wins) duration=8.48 s track=2

# g-a4s14-eight · A4-S14 · seven of eight counties had notice; one had none (wave 3, own drawing)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 10 and 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). The study's hidden counties are `County A` and `County B` only and never share a frame; this comp names neither (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13).
**Spoken (A4-S14):** "Seven of the eight counties in the study were in a Weather Bureau advisory before a tornado touched down there. Only one got no notice ahead of time."
**One look:** eight plain squares in a row; seven turn amber under a big 7, the last takes a red outline under a big 1.

## 0. What this graphic claims
Of the eight counties the 1966 study looked at, seven were named in a Weather Bureau advisory before a tornado touched down in them. One county had no notice ahead of time. The picture counts; it does not say which county is which.

## 1. Source
- `edit_script.md` A4-S14, Rows [C19; study printed p. 15].
- No page is shown. The numbers 8, 7 and 1 are the script's, from that row.

## 2. Datum, scale, orientation
A count, not a map and not a chart with an axis. Eight squares of 150 px with 40 px gaps fill the text-safe width exactly: 8 x 150 + 7 x 40 = 1480 px, x 96 to 1576. Square n (1 to 8) has its left edge at 96 + 190 x (n - 1): 96, 286, 476, 666, 856, 1046, 1236, 1426. The seven lit squares span x 96 to 1386 (centre x 741); the eighth is x 1426 to 1576 (centre x 1501). The squares are equal: no county is larger than another. The order is not a ranking and not a map: the eighth place is the last place and nothing more.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Squares | eight `<rect>` in one full-frame SVG, each 150 x 150, top 420 (y 420 to 570), left edges as section 2, corner radius 2; 4 px outline Body light (drawn inside the box), fill Panel dark. On from frame 0, all eight alike |
| Lit square (1 to 7) | fill Amber 2, outline Amber 2 |
| Marked square (8) | outline Popfig red, 6 px; fill stays Panel dark. It is never filled |
| Big `7` | Arial Black 900 (`font-weight:900`), 180 px, Amber 2, centred on x 741, top 190 (line box y 190 to 370) |
| Big `1` | same type, Popfig red, centred on x 1501, top 190 |
| Eyebrow | left 96, top 110, Arial 700 22 px, Label grey, tracking 6: `EIGHT COUNTIES IN THE 1966 STUDY` |
| Bracket | 4 px Amber 2 line, x 96 to 1386, y 590 to 594, drawn left to right (`scaleX` from the left) |
| Label A | glass chip, left 96, top 620, height 46, padding 0 x 22, Arial 700 26 px, Body light: `in a Weather Bureau advisory before a tornado touched down` |
| Label B | glass chip, right edge at x 1576, top 620, height 46, padding 0 x 22, Arial 700 26 px, Body light: `no notice ahead of time`. Its left edge must stay right of label A's right edge by 40 px or more (read on a frame) |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 15` |

## 4. Must be true in the picture
1. There are exactly eight squares, all the same size, in one row. Seven end amber and one ends with a red outline: 7 + 1 = 8, and the big figures read `7` and `1`.
2. No square has a name, a letter, a number or a chip. `County A` and `County B` are not on screen, and nothing ties the red square to either.
3. The red square is outlined, never filled, and the seven are never red.
4. The sheriff's words, the sheriff's page and any quote strip are absent: this frame never shares the screen with them.
5. The seven squares light in a run of seven beats, left to right, 0.08 s apart and 0.25 s each: the run ends 0.77 s in, inside "Seven of the eight counties" (which ends at 1.00 s).
6. The words on screen say "advisory" and "before a tornado touched down", as the line does; no word says "warning" or "in time".
7. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `EIGHT COUNTIES IN THE 1966 STUDY` · `7` · `1` · `in a Weather Bureau advisory before a tornado touched down` · `no notice ahead of time` · `Disaster Research Center, 1966, p. 15`.
Cue words and times are from `audio/a4-s14.words.json` as it stood on 12 Oct 26 at 19:30. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: -0.22) plus the word's time; the first word uses table 5's first sound (-0.01, so 0.00). Retime from the word index and the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S14 | 0 | Seven | 0.00 | 0.00 | first frame: ground and eight plain squares. From 0.04 the big `7` lands (`y:16` set at 0, to 0 with the fade; 0.3 s) and squares 1 to 7 fill Amber 2 one after another (0.08 s apart, 0.25 s each, a fill change) |
| 1 | A4-S14 | 3 | eight | 0.72 | 0.50 | the eyebrow fades in (0.3 s) |
| 2 | A4-S14 | 4 | counties | 0.94 | 0.72 | the source line fades in (0.3 s, `y:12` to 0) |
| 3 | A4-S14 | 8 | were | 1.84 | 1.62 | the bracket draws under the seven (0.5 s, power2.out) |
| 4 | A4-S14 | 11 | Weather | 2.32 | 2.10 | label A lands (`y:16` to 0 with the fade, 0.3 s) |
| 5 | A4-S14 | 20 | Only | 5.74 | 5.52 | the seven lit squares, the `7`, the bracket and label A drop to 45 % opacity (0.3 s) |
| 6 | A4-S14 | 21 | one | 5.92 | 5.70 | the eighth square's outline turns Popfig red and thickens to 6 px (0.3 s, a stroke change); the big `1` lands (0.3 s) |
| 7 | A4-S14 | 23 | no | 6.48 | 6.26 | label B lands (0.3 s). Hold to the cut at 8.48 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s14-eight.html` is the only file the builder writes; `data-composition-id="g-a4s14-eight"`; id prefix `eight-`; root `<div id="eight-root" ...>` styled through `#eight-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** none (acts-plan.md row: reuses none). Glass chips, source line and ground are the ones of the approved hook and intro set (`compositions/g-i1s9-chain.html` for chips on the canvas ground). `g-a1s07-tracks` (wave 2) uses plain county tiles too; these squares are larger and are not laid over a map. No later composition copies this one.
**Assets mounted:** none. No file under `media/` is used.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s14-eight`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; if it is under the quickref's floor, enlarge the two figures before anything else and say so. Line 4: seek to 0.40 (mid run) and 5.85 forward and backward and match the frames. Line 6: the eight left edges are 96 + 190 x (n - 1), computed by a script and stated in the receipt with the measured right edge of label A and left edge of label B.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00): eight plain squares, nothing else. The frame after it (0.04): the same, the `7` and the first fill just starting. Then one settled frame per cue: 0.40 (mid run: some squares amber, in order from the left), 0.90 (seven amber, `7`, eyebrow), 1.10 (source line), 2.20 (bracket complete), 2.60 (label A), 5.60 (seven dimmed), 6.10 (red outline on the eighth, `1`), 6.70 (label B, clear of label A), 8.40 (last look).
