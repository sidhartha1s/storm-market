Host: id=g-a2s03-chain file=compositions/g-a2s03-chain.html start=306.55 duration=21.92 s (timeline-map.md; wav sum 21.08 s plus its gaps) track=2

# g-a2s03-chain · A2-S3, A2-S4, A2-S5 · one link longer, office after office, at least ten minutes (wave 2, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 5, 6, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1, 3 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). While the training film shot is on screen its label `Civil defense training film, 1967` is the only chip, stamp or label in the frame (rule 4). A flash is a stroke or fill change, never a scale pop (rule 12). The film cut is mounted in `index.html` under this comp; the comp draws the ground with the 4:3 window, the frame and the label (rule 15). The list sheet is never numbered and never shown as the whole system (design sheet S2).
**Spoken (A2-S3):** "So the office that started the telephone list was already at the far end of somebody else's telephone line."
**Spoken (A2-S4):** "From there its warnings went out twice, once by teletype and once by telephone, office after office."
**Spoken (A2-S5):** "And between a warning being issued and radio or TV putting it on the air, the delay was generally at least ten minutes."
**One look:** the chain gains a radar scope feeding South Bend by telephone; a room of operators; the list fills the frame; back on the chain a clock arc grows while the light crawls toward the microphone.

## 0. What this graphic claims
South Bend had no radar of its own: its radar news came by telephone from other Weather Bureau offices, so the chain is one link longer than the intro drew it. South Bend's warnings went out by teletype and by telephone, to one office after another. Between a warning being issued and a station putting it on the air, the delay was generally at least ten minutes.

## 1. Source
- `edit_script.md` A2-S3 (Rows [H], the writer's reading of A2-S1 and A2-S2: study printed p. 13 and National Weather Service, Northern Indiana), A2-S4 (Rows [A6; study printed p. 14, said of the warnings in general]), A2-S5 (Rows [A6; study printed p. 14]: "at least ten minutes").
- The chain: design sheet section 6 "Intro version" and the built `compositions/g-i1s9-chain.html`. The list sheet: design sheet section 5 and the built `compositions/g-t1s3-list.html`.
- Film: `media/films/cuts/a14-13-operators.mp4` (shot 14-13 of the 1967 training film: women in headsets on telephones). It stands for telephone operators of the time, not a South Bend room.

## 2. Datum, scale, orientation
The chain's line is y 520. Stations 1 to 5 stand exactly where the intro placed them (section 3); the warning travels left to right. The new radar station feeds South Bend from above, on a vertical link: no intro station moves.
Clock angles are clockwise degrees from 12 (by script): 5:43 is hour 171.5, minute 258; 5:53 is hour 176.5, minute 318. Ten minutes is 60 degrees of the minute ring.
Film window: x 480 to 1440, y 150 to 870 (960 x 720, 1.5 times the 640 x 480 cut).

## 3. Geometry (screen px)
Chain view (A2-S3 and A2-S5):
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Station 1, teletype | `media/drawings/teletype.svg` inline, `translate(96 450)`, scale 1 (box x 96 to 236, y 450 to 590); label `Kansas City forecasters`, left 96, width 140, top 676 |
| Station 2, telephone | `media/drawings/telephone-lifted.svg` inline, `translate(316 519.6) scale(1.6)` (box x 316 to 460, handset top y 433); label `Weather Bureau · South Bend`, left 293, width 190, top 676 |
| Station 3, list | miniature list sheet as built in `g-i1s9-chain.html`: Beige polaroid 260 x 300 at x 540 to 800, y 350 to 650, eight Caption dark sub bars, a ninth row rule; label `the list`, left 540, width 260, top 676 |
| Station 4, microphone | `media/drawings/microphone.svg` inline, `translate(1170 420) scale(0.85)`; dark (lines Label grey at 55 %, lamp Panel dark); label `an announcer`, left 1121, width 200, top 676 |
| Station 5, house | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`; dark; label `a family`, left 1388, width 200, top 676 |
| Labels | Arial 700 22 px, Label grey, centred in their boxes, line-height 28 |
| Links, y 520, 4 px, Label grey | solid 236 to 316 and 460 to 540; dotted (4 px dots, 14 px gap) 800 to 1170 and 1272 to 1400. No desk is drawn in this comp |
| Radar scope (new) | `media/drawings/radar-scope.svg` inline, `translate(316 206) scale(0.72)` (box x 316 to 460, y 206 to 350); set `stroke-width="5.6"` on the `dw-` group so lines draw 4 px; `dw-sweep` turns about screen (388, 278); `dw-glow` shown |
| Scope link (new) | vertical, x 388, y 350 to 428, solid 4 px Label grey |
| Scope label | `radar at other Weather Bureau offices`, Arial 700 22 px, Label grey, centred on x 388, top 160 |
| Clock (A2-S5) | `media/drawings/wall-clock.svg` inline, `translate(886 150) scale(1.6)` (box x 886 to 1084, y 150 to 348; centre (985.2, 249.2)), `stroke-width="3.5"` on the group; hands at 5:43 |
| Arc (A2-S5) | circle arc, centre (985.2, 249.2), radius 113, from 258 to 318 degrees, Amber 2, 10 px, round caps, grown with `strokeDashoffset` |
| Arc label | glass chip, left 1120, top 222, height 54, padding 0 x 22, Arial Black 900 30 px, Amber 2: `at least 10 minutes` |
| Travelling light | an Amber 2 run, 60 px long, 6 px, on the dotted link from x 800 to x 1170 |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 14` (A2-S5 only) |

Film view (A2-S4, comp 6.14 to 11.85):
| Element | Px |
|---|---|
| Ground with window | the canvas gradient drawn as four opaque panels around a transparent hole at x 480 to 1440, y 150 to 870; nothing of this comp covers the hole while the window is on |
| Frame | 4 px Body light rectangle on the hole's edge |
| Film label | glass chip, left 480, top 886, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Civil defense training film, 1967` |
| Film under the hole | mounted by the orchestrator in `index.html` (track 1, class `filmwin`, left 480, top 150, 960 x 720): mount `v-a2s4-operators`, starts at comp second 6.14, media start 0, 7.84 s mounted (to comp 13.98). The comp shows it from 6.14 to 11.85 and is opaque over it after that |

List view (A2-S4 end, comp 11.85 to 13.98): the list sheet of design sheet section 5 in the Close state (s 1.6, tx 147.6, ty -66: sheet x 250 to 1466, y 30 to 974), all eight rows Plain (Caption dark), the blank ninth row with its rule and no cursor, no tick, no number. Markup and world coordinates as built in `compositions/g-t1s3-list.html`.

## 4. Must be true in the picture
1. The scope is not at South Bend. Its label says `other Weather Bureau offices`, it stands apart from station 2, and the link between them is a telephone line (solid, drawn like the other telephone links). No ring or scope is drawn on South Bend's own station.
2. Stations 1 to 5 sit where the intro placed them, within 2 px. The chain has one more link than `g-i1s9-chain.html` and no fewer.
3. While the film window is open the only text on screen is `Civil defense training film, 1967`: no station label, no source line, no clock, no place name.
4. The list is the eight typed rows in the study's order, no numbering, no tick boxes, no count. The row pulse runs top to bottom and leaves nothing behind: it is "office after office", not a call order claim, so no row is marked first or last.
5. The clock starts at 5:43 and the arc spans 60 degrees of the minute ring. No end time is printed: the words are `at least 10 minutes`.
6. The light reaches the microphone only when the arc is complete. The microphone's lamp turns Popfig red then, not before. The house stays dark to the last frame.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `Kansas City forecasters` · `Weather Bureau · South Bend` · `the list` · `an announcer` · `a family` · `radar at other Weather Bureau offices` · `Civil defense training film, 1967` · the list sheet's eyebrow, title and eight rows exactly as design sheet section 5 · `at least 10 minutes` · `Disaster Research Center, 1966, p. 14`.
Cue words and times are from `audio/a2-s3.words.json`, `a2-s4.words.json`, `a2-s5.words.json` as re-transcribed on 12 Oct 26 (17:45 to 17:50). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S3 -0.28, A2-S4 5.85, A2-S5 13.78) plus the word's time; a segment's first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S3 | 0 | So | 0.28 | 0.00 | first frame: the chain at rest, stations 1 to 3 in Body light, 4 and 5 dark, all five labels, all links |
| 1 | A2-S3 | 2 | office | 0.70 | 0.42 | station 2's lines turn Amber 2 (0.3 s) and stay |
| 2 | A2-S3 | 7 | list | 2.16 | 1.88 | an Amber 2 run crosses the link 460 to 540 and the miniature list's edge turns Amber 2 for 0.6 s, then back |
| 3 | A2-S3 | 12 | far | 3.40 | 3.12 | the radar scope draws on (0.6 s), then its link from the scope down to station 2 (0.3 s), then the scope label fades in (0.3 s) |
| 4 | A2-S3 | 17 | telephone | 4.82 | 4.54 | the sweep turns one full turn (1.2 s, ease none, once); an Amber 2 run goes down the scope link into station 2 (0.4 s) |
| 5 | A2-S4 | 0 | From | 0.29 | 6.14 | hard cut to the film view: window open, frame and film label on. The chain is hidden |
| 6 | A2-S4 | 14 | office | 6.00 | 11.85 | hard cut: the window is covered, frame and film label off, the list sheet is on in the Close state |
| 7 | A2-S4 | 16 | office. | 6.74 | 12.59 | the Amber 2 pulse band (25 %) wipes across rows 1 to 8 in turn, 0.12 s apart, each 0.3 s, and leaves |
| 8 | A2-S5 | 0 | between | 0.20 | 13.98 | the sheet shrinks into station 3's box (`logZoom`, 0.7 s) while the chain and the scope fade back in (0.3 s); the clock fades in at 5:43; source line in |
| 9 | A2-S5 | 2 | warning | 0.84 | 14.62 | station 2 and the miniature list's edge turn Amber 2 (0.3 s) |
| 10 | A2-S5 | 4 | issued | 1.50 | 15.28 | the light leaves the list at x 800 and crawls along the dotted link toward x 1170 (ease none; it arrives at 20.34) |
| 11 | A2-S5 | 15 | delay | 4.92 | 18.70 | the arc grows from 258 to 318 degrees and the minute hand sweeps with it; the hour hand turns 171.5 to 176.5 (all ease none, done at 20.34) |
| 12 | A2-S5 | 18 | at | 5.72 | 19.50 | chip `at least 10 minutes` lands (0.3 s, `y:16` to 0 with the fade) |
| 13 | A2-S5 | 21 | minutes. | 6.56 | 20.34 | arc complete; the light reaches the microphone; its lines turn Body light and its lamp Popfig red (0.2 s). Hold to 21.92 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s03-chain.html` is the only file the builder writes; `data-composition-id="g-a2s03-chain"`; id prefix `chain3-`; root `<div id="chain3-root" ...>` styled through `#chain3-root` (plan rule 3 overrides the template's `id="root"`). The comp is opaque over the whole frame except the film window from 6.14 to 11.85.
**Family base it copies:** the chain family base `compositions/g-a1s13-chain.html` (wave 1; brief `mg_specs/briefs/g-a1s13-chain.md`) for the stations, links and the travelling light; the film window of `compositions/g-a1s15-offices.html` (wave 1; brief `mg_specs/briefs/g-a1s15-offices.md`); the list sheet of the built `compositions/g-t1s3-list.html`; the clock arc is shared with `compositions/g-a2s06-headstart.html` (wave 1).
**Assets (paths from the episode folder):**
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152), `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106), `media/drawings/microphone.svg` (object 120 x 230), `media/drawings/house.svg` (object 260 x 250), `media/drawings/radar-scope.svg` (object 200 x 200, viewBox -6 -6 212 212), `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136): all inlined, ids under `chain3-`.
- `media/films/cuts/a14-13-operators.mp4` (640 x 480, 15.21 s, no audio): not mounted by this comp; it sits under it in `index.html`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s03-chain`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the arc's two angles and the three clock pivots are computed by a script and stated in the receipt. Line 7 here: one frame at comp 9.00 composited over the film (the window shows the operators, the label is the only text).

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the chain at rest, no scope. Then settled frames: 1.00 (station 2 amber), 2.60 (list edge pulse over), 4.20 (scope, link and label), 5.60 (sweep done), 6.20 and 9.00 (film window, one label), 12.00 (list, Close state, rows plain), 13.40 (pulse left nothing), 14.90 (chain back, clock at 5:43), 17.00 (light part way), 19.90 (arc growing, chip on), 20.80 and 21.80 (arc complete, lamp red, house dark).
