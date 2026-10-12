Host: id=g-a6s09-third file=compositions/g-a6s09-third.html start=1085.71 (timeline-map.md table 1 as retimed 12 Oct 26, 19:13; the mount in index.html wins) duration=9.47 s track=2

# g-a6s09-third · A6-S9 · about a third of the offices changed something, and two police departments ordered generators (wave 5, drawing family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3a rows DR-05 and the desk. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county code and no film label belongs in this comp (rules 4 and 8). A flash is a stroke or fill change, never a scale pop (rule 12): the sector and the generators change by fill only. Beats are checked against the spoken window (rule 13; done in section 4).
**Spoken (A6-S9):** "Within three months, about a third of the offices the researchers asked had made changes or planned to. Two city police departments ordered new generators."
**One look:** a circle cut in three; one part fills amber. Then two desks, and under each the generator that was an empty outline in Act 3 fills in.

## 0. What this graphic claims
Within three months, about a third of the offices the researchers asked had made changes or planned to. Two city police departments ordered new generators. The picture claims no percentage, no count of offices and no place.

## 1. Source
- `edit_script.md` A6-S9, Rows [G; study printed pp. 28-29] · [G; study printed pp. 29-30]. The Picture note: "a circle drawn in three parts; one part fills amber on 'a third'. Then two small generator marks under two drawn desks. Small source line `Disaster Research Center, 1966, pp. 28 to 30`."
- The callback: in A3-S15 (`compositions/g-a3s15-desks.html`, wave 3) the viewer saw two police desks, each with a generator drawn as an empty outline. Here the same two drawings fill in. The callback is the drawing files and their two states, `media/drawings/generator.svg` then `media/drawings/generator-filled.svg`; the positions are this comp's own (the Picture note puts the generators under the desks).
- No page is shown: no crop of pp. 28 to 30 is on disk.

## 2. Datum, scale, orientation
Frame 1920 x 1080, one view, two blocks side by side. SCHEMATIC: the circle is a fraction, not a chart of counted offices.
| Block | Px | Holds |
|---|---|---|
| Left | x 96 to 1000 | the circle, its three labels |
| Right | x 1010 to 1555, y 398 to 730 | two desks, two generators, two labels |
| Presenter corner | x >= 1600 and y >= 680 | nothing of ours, ever |
The circle: centre (520, 420), radius 190. Three equal sectors of 120 degrees, cut by lines from the centre to (520, 230), (684.5, 515) and (355.5, 515): the 12 o'clock, 4 o'clock and 8 o'clock points (computed: x = 520 + 190 sin a, y = 420 - 190 cos a for a = 0, 120, 240). The sector that fills runs clockwise from 12 to 4 o'clock.
Drawings sit at 0.85 times their object box, the chain family's desk scale (`mg_specs/briefs/g-a1s13-chain.md`), with `stroke-width="4.7"` on each `dw-` group so a line is 4 px on screen (the telephone on each desk keeps the file's lighter line, 3 px at this scale with `stroke-width="3.5"`).
Colours (the built set's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Caption dark `#2a2622`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the chain base's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) to carry the holds |
| Circle | one inline SVG. Outline: circle centre (520, 420), radius 190, 4 px Body light, fill Panel dark. Three dividers, 4 px Body light, round caps, from (520, 420) to (520, 230), (684.5, 515), (355.5, 515) |
| Filled sector | path `M520 420 L520 230 A190 190 0 0 1 684.5 515 Z`, under the outline and dividers; fill Amber 2, `fill-opacity` 0 at rest and 0.9 when lit. The other two sectors never fill |
| Eyebrow | `WITHIN THREE MONTHS`, Arial 700 20 px, Label grey, tracking 6, centred on x 520, top 170 |
| Sector label | `about a third`, Arial 700 34 px, Headline white, left 730, top 284 (beside the filled sector, 45 px right of its edge) |
| Sector sub label | `had made changes or planned to`, Arial 700 26 px, Body light, left 730, top 334. Measure its right edge and state it; it must end left of x 1180 |
| Caption | `of the offices the researchers asked`, Arial 700 22 px, Label grey, centred on x 520, top 640 (30 px under the circle) |
| Desk 1 | `media/drawings/desk.svg` inline, `translate(1010 420) scale(0.85)`: object box x 1010 to 1265, y 420 to 547.5 (its telephone rises to y 401). Lines Body light, bodies Panel dark |
| Desk 2 | the same, `translate(1300 420) scale(0.85)`: object box x 1300 to 1555 |
| Generator 1 | `media/drawings/generator.svg` inline, `translate(1086.5 572) scale(0.85)`: object box x 1086.5 to 1188.5, y 572 to 640, centred under desk 1 (centre x 1137.5). At rest it is the outline state: lines `#55606b`, `dw-lamp` fills Panel dark. Filled state, as `media/drawings/generator-filled.svg`: lines Body light, `dw-lamp` fills Amber 2, `dw-ink` strokes Caption dark |
| Generator 2 | the same, `translate(1376.5 572) scale(0.85)`: object box x 1376.5 to 1478.5, centred under desk 2 (centre x 1427.5) |
| Desk label | `two city police departments`, Arial 700 22 px, Label grey, centred on x 1282.5, top 664 |
| Generator label | `ordered new generators`, Arial 700 26 px, Body light, centred on x 1282.5, top 696 (it ends near x 1430, left of the corner) |
| Source line | design sheet section 10: left 96, bottom 60, Arial 700 22 px, `rgba(244,240,232,0.88)`, `letter-spacing:0.04em`, the credit shadow: `Disaster Research Center, 1966, pp. 28 to 30` |

## 4. Must be true in the picture
1. The circle has three equal parts and exactly one is amber: the three divider angles are 120 degrees apart within 1 degree.
2. The label says `about a third`. No percentage, no "33", no count of offices is on screen.
3. The caption says whose offices: the ones the researchers asked. Nothing says "Indiana's offices" or "all offices".
4. Two desks and two generators, no more. Both generators are empty outlines until "generators" is spoken, then both are filled; neither is filled earlier.
5. The desks carry no name: no city, no county, no `County A`, no `County B`. The two departments are not placed on any map.
6. The sector and the generators change by fill and stroke colour only: no scale pop, no glow.
7. Lines are 4 px on screen (3 px on the telephones); no line under 3 px.
8. One source on screen, the source line. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom; no label under a line or another label.
Beat check (rule 13): first sentence, four beats in 3.65 s, the closest two 0.38 s apart, each entrance 0.3 s. Second sentence, three beats between 5.93 and 7.73; the desks' 0.6 s draw is complete at 6.53 and the generators' outlines at 6.93, 0.8 s before they fill. The last 1.29 s holds.

## 5. Text (exact) and cues
Text: `WITHIN THREE MONTHS` · `about a third` · `had made changes or planned to` · `of the offices the researchers asked` · `two city police departments` · `ordered new generators` · `Disaster Research Center, 1966, pp. 28 to 30`.
Cue words and times are from `audio/a6-s9.words.json` as on disk 12 Oct 26, 19:27 (wav 9.00 s). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A6-S9 -0.23) plus the word's time; the first word uses the table's "first sound" (-0.01, so 0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S9 | 0 | Within | first sound 0.22 | 0.00 | first frame: ground, the circle with its three dividers, no fill, no text |
| 1 | A6-S9 | 1 | three | 0.42 | 0.19 | the eyebrow fades in (0.3 s) |
| 2 | A6-S9 | 5 | third | 1.70 | 1.47 | the sector fills Amber 2 (`fill-opacity` 0 to 0.9, 0.3 s); `about a third` fades in with it (`y: 12` to 0) |
| 3 | A6-S9 | 8 | offices | 2.08 | 1.85 | the caption under the circle and the source line fade in (0.3 s) |
| 4 | A6-S9 | 13 | made | 3.88 | 3.65 | the sub label fades in (0.3 s, `y: 12` to 0) |
| 5 | A6-S9 | 18 | Two | 6.16 | 5.93 | the two desks draw on together (`strokeDashoffset`, 0.6 s, longest line first); from 6.53 the two generator outlines draw on (0.4 s) |
| 6 | A6-S9 | 20 | police | 6.56 | 6.33 | the desk label fades in (0.3 s) |
| 7 | A6-S9 | 24 | generators. | 7.96 | 7.73 | generator 1 then generator 2 turn to the filled state, 0.15 s apart (0.3 s each, fill and stroke colour only); the generator label fades in at 7.88. Hold to the last frame (9.47) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a6s09-third.html` is the only file the builder writes; `data-composition-id="g-a6s09-third"`, `data-duration="9.47"`; id prefix `thd-`; root `<div id="thd-root" ...>` styled through `#thd-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The host is mounted in `index.html`; do not edit `index.html`.
**Family base it copies:** the desks, their stroke and the draw-on from the chain family base `compositions/g-a1s13-chain.html` and the county chain base `compositions/g-a4s02-countyb.html` (briefs in `mg_specs/briefs/`); the generator's two states as `compositions/g-a3s15-desks.html` uses them (wave 3: if it has passed, copy its generator markup; its positions are not copied). Label type from the built `compositions/g-i1s9-chain.html`.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object box 300 x 150, telephone rises to y -22, viewBox -6 -28 312 184, line 4, telephone 3), inlined twice.
- `media/drawings/generator.svg` (DR-05, object box 120 x 80, viewBox -6 -6 132 92, line 4, bolt and hub 3), inlined twice; its filled state is `media/drawings/generator-filled.svg` (same viewBox and classes: `dw-lamp` fills, `dw-ink` strokes).
All inlined, ids under `thd-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a6s09-third`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; the two blocks are the content. Line 4: no fill's start value lives only in a deferred tween's from vars; seek to 1.60 and 7.80 forward and backward and match. Line 6: the three divider end points and the sector path are computed by a script from the centre, radius and the three angles and stated in the receipt, with the two generator centres against their desks' centres.

## 8. Receipt
As template section 8, plus the measured right edge of `had made changes or planned to`.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground and the empty circle in three parts, nothing else. Then settled frames: 0.60 (eyebrow), 1.90 (one sector amber, `about a third`), 2.30 (caption, source line), 4.10 (sub label; left block complete), 6.50 (desks drawn, generators not yet), 7.00 (two generator outlines, empty; desk label), 8.30 (both generators filled, generator label), 9.40 (last frame: corner empty).
