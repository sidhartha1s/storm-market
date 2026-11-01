Host: id=g-a4s13-duty file=compositions/g-a4s13-duty.html start=771.12 duration=13.98 s (timeline-map.md tables 1 and 5, read 12 Oct 26, 19:33; the mount in index.html wins; last sound at 12.97) track=2

# g-a4s13-duty · A4-S13 · nobody on the list saw backing up radio and TV as its job (wave 3, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 5, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 6 item 14. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a1s18-list.md` (the list in its Beside state).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county label of any kind is in this comp (rule 8): the study ties this police chief to no county. The ground is the canvas gradient, not the teletype room photograph, which is held to its three uses (rule 9). The typed sheet uses two type sizes by design, as the opening's sheets do (rule 10). A flash is a stroke or fill change, never a scale pop (rule 12). Beats were held against the spoken windows when this brief was written (rule 13): seven row pulses 0.10 s apart end at 9.74, before the next spoken beat at 10.23.
**Spoken (A4-S13):** "Police weren't the only ones. Back when only the forecast was out, one police chief said informing the public was never their primary duty. No office the researchers asked saw backing up radio or TV as its job."
**One look:** the telephone list on the right; an amber band sits on the city police row while a chief's words come up on paper, then the band jumps to the stations row; the paper changes to the study's own sentence, a pulse runs down every other row and leaves, and only the stations row is still lit.

## 0. What this graphic claims
Asked about alerting the public when only the forecast was out, one police chief said "I never felt that it was our primary duty to inform the public." And of the forecast the study says no member of any organization interviewed saw backing up radio and TV as their responsibility. So on the list, the job of telling the public sat with one row only: the stations.

## 1. Source
- `edit_script.md` A4-S13, Rows [C10; study printed p. 9: asked about "alerting the public to the fact that tornadoes could develop"; the study ties this chief to no county] and [C9; study printed p. 9: "in response to a tornado forecast"]. Both quotes and both attributions on screen are the Picture note's, word for word.
- Both statements are about the **forecast**, not the warnings. Each attribution says so (`asked about the forecast`, `said of the forecast`); nothing on screen ties either quote to a warning, to County B or to the evening's tornadoes.
- The list: design sheet section 5 (the study's sentence on printed p. 14, our typed setting of it) and the built `compositions/g-t1s3-list.html`. No crop of p. 9 is on disk, so the quotes are retyped on a paper strip (design sheet section 9).

## 2. Datum, scale, orientation
The list sheet keeps the world coordinates of design sheet section 5 under one camera transform (origin top left; screen = s x world + t), in the **Beside** state that `mg_specs/briefs/g-a1s18-list.md` defines: s 1.1, tx 669.6, ty 44; sheet on screen x 740 to 1576, y 110 to 759; row text 28.6 px, eyebrow 20.9 px, title 33 px. The camera does not move in this comp.
Row centres on screen, slots 1 to 9 (by script): 279.4, 332.2, 385.0, 437.8, 490.6, 543.4, 596.2, 649.0, 701.8. Row box 48.4 px tall. A band runs x 775.2 to 1540.8 (world x 96 to 792). Row text left edge 834.6.
The two rows that matter: slot 3 `City Police Departments` (centre y 385.0) and slot 6 `Specified radio and TV stations` (centre y 543.4).
Colours (the built hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`; Amber 2 `#e8c56a`; Body light `#dfe7ee`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the faint sweep band of the chain family (520 px wide, Label grey at 6 %, drifting left to right, ease none) to carry the holds |
| List sheet | design sheet section 5, all nine slots, Beside state: sheet x 740 to 1576, y 110 to 759. Eyebrow `SOUTH BEND WEATHER BUREAU · BY TELEPHONE`, title `Organizations notified included:`, the telephone glyph, the rule, eight rows in the **Plain** state (all eight in Caption dark), the ninth slot with its row rule and nothing on it. No number, letter, tick, tick box, red line or cursor |
| Lit band | design sheet "Lit": Amber 2 at 35 % behind a row, x 775.2 to 1540.8, 48.4 px tall on the row's centre, `scaleX` 0 to 1 from the left (`transformOrigin:"left center"`, set at timeline 0). One band element per row that is ever lit (slots 3 and 6) |
| Pulse band | design sheet "Pulse": Amber 2 at 25 %, same box, wipes across a row and leaves (scaleX 0 to 1 from the left in 0.12 s, then opacity to 0 in 0.13 s); nothing stays. One per slot 1, 2, 3, 4, 5, 7, 8 |
| Paper strip | Beige polaroid, left 96, top 250, 604 x 344 (right 700, bottom 594), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2. It clears the sheet's left edge (740) by 40 px |
| Quote area | inside the strip, left 124, top 278, 548 x 208, `overflow:hidden` (the mask for the line swap). Georgia 40 px, line-height 52, Caption dark |
| Quote 1 | three lines: `“I never felt that it was` / `our primary duty` / `to inform the public”` |
| Quote 2 | four lines: `“No member of any` / `organization interviewed` / `saw it as their` / `responsibility”` |
| Attribution | Arial 700 22 px, line-height 28, Caption dark sub, tracking 2, left 124, top 506, width 548, two lines. With quote 1: `a police chief, asked about the forecast ·` / `Disaster Research Center, 1966, p. 9`. With quote 2: `said of the forecast · p. 9` |
| List source | credit corner, left 96, bottom 60, source-line type (design sheet section 10): `Disaster Research Center, 1966, p. 14`. On from frame 0; it fades out as the strip arrives, so one source is on screen at a time |

## 4. Must be true in the picture
1. The sheet is the study's "included" list: title `Organizations notified included:`, eight rows in the sentence's order, a blank ninth slot. No row count, no numbering, no tick box, nothing that reads as a call order or as the whole warning system.
2. The Lit band is on `City Police Departments` first and on `Specified radio and TV stations` second. From the jump to the last frame the stations row is the only row with a band that stays.
3. Quote 1 and quote 2 are the note's words, exactly, in quotation marks. Quote 1's attribution carries `asked about the forecast`; quote 2's carries `said of the forecast`. The word "warning" is not on the strip.
4. No county chip, no `County A`, no `County B`, no town, no name. The chief is `a police chief`.
5. The pulses of the third sentence touch slots 1, 2, 3, 4, 5, 7 and 8 and leave nothing behind: after 9.74 those seven rows are plain Caption dark on bare paper.
6. The strip and the sheet never touch (40 px of ground between them), and the strip never covers a row.
7. One source at a time: the list's source line is gone before the strip's attribution is readable.
8. Nothing of ours in x >= 1600, y >= 680: the sheet's right edge is x 1576. No label under a band edge; the bands sit behind the type.
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `SOUTH BEND WEATHER BUREAU · BY TELEPHONE` · `Organizations notified included:` · rows `State Police` · `Sheriffs' Departments` · `City Police Departments` · `Indiana and Michigan Electric Company` · `Red Cross` · `Specified radio and TV stations` · `Flying services` · `Airlines` · `“I never felt that it was our primary duty to inform the public”` · `a police chief, asked about the forecast · Disaster Research Center, 1966, p. 9` · `“No member of any organization interviewed saw it as their responsibility”` · `said of the forecast · p. 9` · `Disaster Research Center, 1966, p. 14`.
Cue words and times are from `audio/a4-s13.words.json` (38 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S13 -0.45) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S13 | 0 | Police | 0.45 | 0.00 | first frame: ground, the list in the Beside state with all eight rows plain, the list's source line. At 0.10 one Pulse band crosses `City Police Departments` (slot 3) and leaves |
| 1 | A4-S13 | 13 | police | 5.16 | 4.71 | the Lit band wipes onto `City Police Departments` (0.3 s) and stays |
| 2 | A4-S13 | 15 | said | 5.78 | 5.33 | the paper strip rises with quote 1 and its attribution (`y:60` to 0 with the fade, 0.4 s, power3.out); the list's source line fades out (0.3 s) |
| 3 | A4-S13 | 23 | duty. | 7.90 | 7.45 | the light jumps: the slot 3 band leaves to the right (`scaleX` to 0 with `transformOrigin:"right center"` set for that tween at build, 0.2 s) and the slot 6 band wipes onto `Specified radio and TV stations` (0.3 s, starting 0.1 s later) |
| 4 | A4-S13 | 24 | No | 9.10 | 8.65 | the strip changes: quote 1 slides up behind the mask (`y:-220`, 0.4 s, power3.inOut) while quote 2 rises into place from below; the attribution cross-fades to `said of the forecast · p. 9` (0.3 s) |
| 5 | A4-S13 | 25 | office | 9.34 | 8.89 | a Pulse band crosses slots 1, 2, 3, 4, 5, 7, 8 from top to bottom, 0.10 s apart, each 0.25 s; the last is gone at 9.74. The stations band does not move |
| 6 | A4-S13 | 32 | radio | 11.54 | 11.09 | the stations band's opacity goes 35 % to 55 % and back (0.3 s each way), once. Hold to 13.98: one lit row, quote 2 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s13-duty.html` is the only file the builder writes; `data-composition-id="g-a4s13-duty"`, `data-duration="13.98"`; id prefix `duty-`; root `<div id="duty-root" ...>` styled through `#duty-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Base it copies:** the list sheet markup, row states and bands of the built `compositions/g-t1s3-list.html` and `compositions/g-i1s5-onair.html` (the Lit band), in the Beside state of `compositions/g-a1s18-list.html` (wave 2) without that comp's photograph, scrim and stamp. The line swap inside the strip is the one in `compositions/g-i1s7-sheriff.html` (`q1` up behind the mask, `q2` rising). Nothing later copies this comp; `compositions/g-a6s03-announcer.html` and `compositions/g-z1s02-row.html` return to the same sheet.
**Assets:** none mounted from `media/`. The sheet, its telephone glyph (the drawn telephone of `media/drawings/telephone.svg`, 102 x 106 file, as `g-t1s3-list.html` inlines it at 60 px wide), the bands and the strip are built in the comp.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s13-duty`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type may name this comp, as it names the opening's three typed sheets (plan rule 10): state it in the receipt, do not restyle.

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 shows the list and its source line on the ground, no band. Line 4 here: every band's `scaleX` and `transformOrigin` are set at timeline 0; capture 7.60 (mid jump) and 9.20 (mid pulse run) both ways. Line 6 here: the nine row centres and the band box are computed from design sheet section 5 and the Beside transform by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the list, eight plain rows, the source line, no band, no strip. Then settled frames: 0.60 (the first pulse gone, rows plain), 5.20 (band on `City Police Departments`), 6.00 (strip with quote 1, three lines, attribution on two lines, list source gone), 7.90 (band on `Specified radio and TV stations` only), 9.20 (quote 2 in place, a pulse part way down the rows), 10.00 (seven rows plain, the stations row lit, attribution `said of the forecast · p. 9`), 11.40 (stations band at its brightest), 13.80 (hold).
