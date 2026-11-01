Host: id=g-a3s15-desks file=compositions/g-a3s15-desks.html start=608.87 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=17.34 s (last sound at 16.34) track=2

# g-a3s15-desks · A3-S15, A3-S16, A3-S17 · two police desks lose their radio, an alert comes 1, 10 or 30 minutes ahead, and the radio that still worked (wave 3, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3a rows DR-03 and DR-05. Times: `mg_specs/timeline-map.md` tables 1 and 5. Bases: `mg_specs/briefs/g-a1s13-chain.md`, `mg_specs/briefs/g-a4s02-countyb.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2): every label of a scene fades before its scene leaves. The root is styled through its id and is never `id="root"` (rule 3). No county label of any kind: the Picture note says "No county label", so neither `County A` nor `County B` appears (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). Beat counts were held against each spoken window when this brief was written (rule 13): the closest two beats are 0.36 s apart (A3-S16, "10" and "30") and each is a 0.25 s stroke change.
**Spoken (A3-S15):** "Two city police departments had no good back up power either, and lost full communication for a time."
**Spoken (A3-S16):** "Where an office in a tornado's path did get an alert, it came one, ten or thirty minutes ahead."
**Spoken (A3-S17):** "A warning could still move over the radios that police and civil defense used."
**One look:** two desks joined by an amber radio arc that goes dotted and dark, an empty generator outline beside each; then one desk at the end of a road, a tornado mark coming along it and three marks that light: 1, 10, 30 minutes out; then the dark chain, with one dotted amber arc between two desks as the only light.

## 0. What this graphic claims
Three facts from the study, one per segment. Two city police departments had no good back up power and lost full communication for a time. Offices in a tornado's path that did get an alert got it 1, 10 or 30 minutes ahead. A warning could still travel over the radios police and civil defense used. No office, town or county is identified.

## 1. Source
- `edit_script.md` A3-S15, Rows [D; study printed p. 29]; A3-S16, Rows [C15; study printed p. 21]; A3-S17, Rows [A13; study printed p. 21: the civil defense director "radioed" the city police]. The three Picture notes are the only source of what is drawn.
- Source line, A3-S15 only (the Picture note's): `Disaster Research Center, 1966, p. 29`.
- The generator outline is `media/drawings/generator.svg`, the file drawn as "the one that is not there"; it is filled in A6-S9 by `compositions/g-a6s09-third.html`, which copies this comp's two desks and two outlines.
- The chain of the third part: design sheet section 6 "Intro version" and `mg_specs/briefs/g-a1s13-chain.md` section 3.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE, in all three parts, with one exception: the road of A3-S16 has a stated scale, 20 px per minute, measured west from the desk's left edge at x 1000. Its three marks are at 1000 - 20 x minutes, by script: 1 minute x 980, 10 minutes x 800, 30 minutes x 400. West is left: the tornado mark comes from the left and moves toward the desk.
The three parts are three scenes on one ground. A scene's own elements fade out before the next scene's come in; nothing is carried across except desk B (scene 1 to scene 2).
Colours (the built intro's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
Ground, all three scenes: canvas gradient with the intro's faint sweep band, on from frame 0.

Scene 1 (A3-S15, comp 0.00 to 6.40):
| Element | Px |
|---|---|
| Desk A | `media/drawings/desk.svg` inline, whole, `translate(300 470)`, scale 1 (box x 300 to 600, y 470 to 620, telephone rises to y 448, top surface y 510 to 522), lines Body light |
| Desk B | the same, `translate(1000 470)` (box x 1000 to 1300) |
| Radio arc | path `M450 440 Q800 200 1150 440` (apex (800, 320) by script), 4 px, round caps. Frame 0: Amber 2, solid. Then dotted (`stroke-dasharray="0.1 14"`), then `#55606b` at `stroke-opacity` 0.5 |
| Generator outlines | `media/drawings/generator.svg` inline twice, scale 1 (120 x 80), lines Label grey: beside desk A at `translate(150 540)` (box x 150 to 270, y 540 to 620), beside desk B at `translate(1330 540)` (box x 1330 to 1450) |
| Labels | Arial 700 22 px, Label grey, top 640, each centred on its object: `city police` (x 450 and x 1150), `back up power` (x 210 and x 1390) |
| Source line | design sheet section 10: left 96, bottom 60: `Disaster Research Center, 1966, p. 29` |

Scene 2 (A3-S16, comp 6.40 to 12.67):
| Element | Px |
|---|---|
| Desk | desk B, unmoved (box x 1000 to 1300), lines Body light; its label becomes `an office in the path`, centred on x 1150, top 640 |
| Road | one line, y 620, from x 1000 west to x 96, 4 px Body light, round caps |
| Marks on the road | three vertical lines, 4 px, y 604 to 636, at x 980, x 800 and x 400. At rest Label grey; lit Amber 2 |
| Mark labels | Arial 700 26 px, Amber 2, top 494, centred on their marks: `1` (x 980), `10` (x 800), `30 minutes out` (x 400). Hidden until lit |
| Tornado mark | `media/drawings/tornado-mark.svg` inline, scale 1 (60 x 80, line 6), stroke Body light, never red; its lowest point rides the road (y 620), so its box is y 540 to 620. Its point moves from x 130 to x 340 (ease none): the box's right edge ends at x 370, 30 px short of the 30 minute mark, and 16 px under that mark's label |

Scene 3 (A3-S17, comp 12.67 to 17.34):
| Element | Px |
|---|---|
| Chain | the base chain, every station dark: teletype `translate(96 450)`, telephone `translate(316 519.6) scale(1.6)`, list sheet x 540 to 800, y 350 to 650 at opacity 0.36, microphone `translate(1170 420) scale(0.85)`, house `translate(1400 430) scale(0.68)`; lines `#55606b`, bodies Panel dark, nothing amber. Labels top 676, Label grey, as the base |
| Chain's desk | `media/drawings/desk.svg` inline, whole, `translate(840 490) scale(0.85)`, `stroke-width="4.7"`, telephone 3.5 (box x 840 to 1095, y 490 to 617.5, the intro's desk), lines Label grey; label `police`, Arial 700 22 px, Label grey, centred on x 967.5, top 676 |
| Links, y 520, 4 px, `#55606b` | dotted (`stroke-dasharray="0.1 14"`): 236 to 316, 460 to 540, 800 to 840, 1095 to 1170, 1272 to 1400. Every link is dotted and dark |
| Second desk | `media/drawings/desk.svg` inline without its `dw-phone` group, `translate(840 250) scale(0.85)`, `stroke-width="4.7"` (box x 840 to 1095, y 250 to 377.5), lines Label grey; label `civil defense`, same type, centred on x 967.5, top 204 |
| Radio arc | path `M1095 300 Q1180 405 1095 510` (its middle is (1137.5, 405) by script, 32 px left of the microphone's box), 4 px Amber 2, dotted, round caps |
| The light | Amber 2 dot, radius 8, moved along the arc with `getPointAtLength` from a 0 to 1 proxy tween (seek-safe), then hidden |

## 4. Must be true in the picture
1. Scene 1: the arc is amber and whole in the first frame, dotted next, dark last, in that order. Both generator boxes are outlines with no fill. No desk carries a county, town or department name.
2. Scene 2: the three marks stand at 20 px per minute from the desk: 980, 800 and 400. They light in the spoken order, 1, then 10, then 30. The tornado mark stays west of all three and never reaches the desk. It is never red and has no time of its own.
3. Scene 2 shows one office and three possible lead times. Nothing says which office got which.
4. Scene 3: the dotted amber arc and its travelling dot are the only amber on screen. Every station, every link, both desks and the list are dark or grey. The arc joins the two desks and touches nothing else.
5. The civil defense desk has no telephone (he used a radio); the police desk has one, on its cradle. Nobody is drawn.
6. Scene 3's stations 1 to 5 and the chain's desk sit within 2 px of the intro's numbers. No stop mark, no tick.
7. One scene at a time: at 6.80 nothing of scene 1 except desk B is visible, and at 13.10 nothing of scene 2 is visible.
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom. No label under the arc, the road, a mark or the tornado mark.
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry. Ruled by the lead, 12 Oct 26: scene 2 (one strip at y 446 to 666, with 40.7 % of the frame empty above it and 37.8 % below, for 6.27 s) is accepted as a full-width chain row on a slow push 1.00 to 1.03, because desk B stays put across the scenes.

## 5. Text (exact) and cues
Text: `city police` (twice) · `back up power` (twice) · `Disaster Research Center, 1966, p. 29` · `an office in the path` · `1` · `10` · `30 minutes out` · `Kansas City forecasters` · `Weather Bureau · South Bend` · `the list` · `police` · `civil defense` · `an announcer` · `a family`.
Cue words and times are from `audio/a3-s15.words.json` (17 words), `audio/a3-s16.words.json` (19) and `audio/a3-s17.words.json` (14), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S15 -0.35, A3-S16 6.15, A3-S17 12.42) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 6.40, 12.67). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S15 | 0 | Two | 0.35 | 0.00 | first frame: ground, desk A and desk B, the amber arc whole between them. No label, no outline |
| 1 | A3-S15 | 2 | police | 0.76 | 0.41 | both `city police` labels and the source line fade in (0.3 s) |
| 2 | A3-S15 | 5 | no | 1.82 | 1.47 | the generator outline beside desk A draws on (0.4 s, `strokeDashoffset`) |
| 3 | A3-S15 | 7 | backup | 2.32 | 1.97 | the generator outline beside desk B draws on (0.4 s) |
| 4 | A3-S15 | 8 | power | 2.70 | 2.35 | both `back up power` labels fade in (0.3 s) |
| 5 | A3-S15 | 11 | lost | 3.96 | 3.61 | the arc turns dotted (0.2 s) |
| 6 | A3-S15 | 13 | communication | 4.54 | 4.19 | the arc goes dark (`#55606b`, `stroke-opacity` 0.5; 0.3 s); the two telephones' lines go `#55606b` |
| 7 | A3-S16 | 0 | Where | 0.25 | 6.40 | scene 1 leaves: its labels and source line fade (0.15 s), then desk A, the arc and both outlines (0.25 s). Desk B stays, its telephone back to Body light |
| 8 | A3-S16 | 2 | office | 0.52 | 6.67 | the label `an office in the path` fades in under desk B |
| 9 | A3-S16 | 5 | tornado's | 1.14 | 7.29 | the road draws west from the desk (0.5 s) with its three grey marks; the tornado mark fades in at point x 130 (0.3 s) and moves to x 340 (ease none, to 11.86) |
| 10 | A3-S16 | 10 | alert, | 2.42 | 8.57 | desk B's telephone lines go Headline white and back to Body light (0.3 s each way) |
| 11 | A3-S16 | 13 | 1, | 3.48 | 9.63 | the mark at x 980 turns Amber 2 and `1` fades in (0.25 s) |
| 12 | A3-S16 | 14 | 10 | 4.26 | 10.41 | the mark at x 800 turns Amber 2 and `10` fades in (0.25 s) |
| 13 | A3-S16 | 16 | 30 | 4.62 | 10.77 | the mark at x 400 turns Amber 2 and `30 minutes out` fades in (0.25 s) |
| 14 | A3-S17 | 0 | A | 0.25 | 12.67 | scene 2 leaves: labels fade (0.15 s), then the road, marks, tornado mark and desk B (0.25 s); the dark chain with its desk and labels fades in (0.35 s, complete by 13.25) |
| 15 | A3-S17 | 4 | move | 1.12 | 13.54 | the second desk draws on above the chain's desk (0.4 s) |
| 16 | A3-S17 | 7 | radios | 1.62 | 14.04 | the arc draws from the upper desk to the lower, dot by dot (0.5 s); the light then runs it once (0.6 s, ease none) and hides |
| 17 | A3-S17 | 9 | police | 2.26 | 14.68 | the label `police` turns Body light (0.2 s) |
| 18 | A3-S17 | 11 | civil | 2.72 | 15.14 | the label `civil defense` fades in (0.2 s). From 15.90 the arc's dots go Headline white and back to Amber 2 in one wave (0.6 s). Hold to 17.34 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s15-desks.html` is the only file the builder writes; `data-composition-id="g-a3s15-desks"`, `data-duration="17.34"`; id prefix `dsk-`; root `<div id="dsk-root" ...>` styled through `#dsk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Three scene groups (`dsk-sc1`, `dsk-sc2`, `dsk-sc3`), each hidden in CSS until its cue except scene 1. Do not edit `index.html`.
**Family base it copies:** `compositions/g-a1s13-chain.html` (wave 1) for scene 3's stations, links and labels, set dark; `compositions/g-a4s02-countyb.html` (wave 1) for the radio arc and its light, and for a desk drawn without its telephone. `compositions/g-a6s09-third.html` (wave 5) copies scene 1's two desks and two outlines and fills the outlines; `compositions/g-a6s05-wires.html` (wave 5) copies scene 3's dark chain.
**Assets (paths from the episode folder, read on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, line 4, telephone 3), inlined four times.
- `media/drawings/generator.svg` (DR-05, object 120 x 80, viewBox -6 -6 132 92, line 4, bolt and hub 3), inlined twice. Not `generator-filled.svg`.
- `media/drawings/tornado-mark.svg` (DR-03, object 60 x 80, viewBox -6 -6 72 92, line 6).
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152, line 4).
- `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106, line 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4).
All inlined, ids under `dsk-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s15-desks`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill for each scene separately. Line 4 here: capture 6.55 and 12.85 (the two scene changes) both ways; every scene group's `autoAlpha` is set at timeline 0. Line 6 here: the three road marks (20 px per minute from x 1000), the two arc middles and the tornado mark's end box are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): two desks and the whole amber arc. Then: 0.90 (labels and source line), 1.90 and 2.40 (one outline, then two), 2.80 (`back up power` twice), 3.90 (arc dotted), 4.70 (arc dark), 6.80 (scene 1 gone but desk B), 8.00 (road, three grey marks, tornado mark at the west end, new label), 9.95 (`1` lit), 10.70 (`10` lit), 11.20 (all three lit, tornado mark west of the 30 mark, label clear of it), 13.30 (dark chain with its desk, nothing amber), 14.00 (second desk), 14.70 (arc drawn, light on it), 15.50 (both desk labels), 17.20 (last frame: the arc is the only light).
