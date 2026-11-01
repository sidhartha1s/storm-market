Host: id=g-a4s11-farend file=compositions/g-a4s11-farend.html start=748.69 duration=22.43 s (timeline-map.md tables 1 and 5, read 12 Oct 26, 19:33; the mount in index.html wins; last sound at 21.43) track=2

# g-a4s11-farend · A4-S11, A4-S12 · a station the police never told, and the two other ways to a house (wave 3, county chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a4s02-countyb.md` (the county chain's station boxes). Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2): the strip, the chip and the desk's label fade in place, they do not slide out. The root is styled through its id and is never `id="root"` (rule 3). **The siren horn is never shown sounding** (rule 6): no sound lines, no pulse, no colour change on it, no siren audio. The study does not say which county this station was in, so neither `County A` nor `County B` appears in this comp (rule 8); its chip reads `a station · county not given in the study`. A flash is a stroke or fill change, never a scale pop (rule 12). Beats were held against the spoken windows when this brief was written (rule 13): the closest two are 0.58 s apart (A4-S12, "other" and "radio").
**Spoken (A4-S11):** "A station said later that local police had been told a tornado was headed its way. "We were not notified by the local police," it said, "so we couldn't prepare our listeners.""
**Spoken (A4-S12):** "There was little or no attempt to warn people any other way than radio and TV. The exceptions were a few fire sirens in a very few small communities, and police car speakers that could not reach everyone."
**One look:** a police desk goes amber, the dotted link to a dark microphone never lights, and the station's own words come up on paper; then the desk leaves, a house joins the microphone, and two grey dotted ways to the house are drawn, a horn on a pole that never changes and a police car that blinks amber once.

## 0. What this graphic claims
A station told the researchers that local police had been told a tornado was headed its way and did not notify the station, so it could not prepare its listeners. And there was little or no attempt to warn people by any means other than radio and TV: the exceptions were a few fire sirens in a very few small communities, and police car speakers that could not reach everyone.

## 1. Source
- `edit_script.md` A4-S11, Rows [C8; study printed p. 25], marked "not tied to County B". The quote on screen is the Picture note's: `were not notified by the local police so we couldn't prepare our listeners`, attribution `media personnel · Disaster Research Center, 1966, p. 25`. No crop of p. 25 is on disk, so the words are retyped on a paper strip (the lift of design sheet section 9).
- `edit_script.md` A4-S12, Rows [study printed p. 35: "little or no attempt by the system ... to use mechanisms other than radio and TV warnings"] and [study printed pp. 32-33: "In a very few small communities, Fire Departments did sound their fire engine sirens"; police car speakers "insufficiently powered to reach everyone"].
- The horn on a pole is the Picture note's drawing for "another way to a house". The study's sirens were fire engine sirens, so the horn carries the label `a few fire sirens` and nothing that says a town siren system sounded.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE. The chain's line is y 520; a message would run left to right. The police desk, the microphone and the house stand where `g-a4s02-countyb` puts County B's, so the family reads as one drawing, but this is not County B's chain and no county code is on it.
"Dark" and "grey" here: every unlit line is Label grey `#93a3b2`, bodies Panel dark (the county chain's unlit state). Amber 2 `#e8c56a` is used twice only: the police desk's lines (A4-S11) and one blink of the police car's body (A4-S12).
Colours (the built hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
Ground: canvas gradient, on from frame 0, with the family's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window.

Part A, the chain of three (A4-S11, comp 0.00 to 10.59):
| Element | Px |
|---|---|
| Police desk | `media/drawings/desk.svg` inline, whole (telephone on its cradle), `translate(582 490) scale(0.85)`, `stroke-width="4.7"`, telephone 3.5 (box x 582 to 837, y 490 to 617.5, centre x 709.5) |
| Dotted link | y 520, x 837 to 1068, 4 px Label grey, `stroke-dasharray="0.1 14"`, round caps. It never changes colour |
| Microphone | `media/drawings/microphone.svg` inline, `translate(1068 420) scale(0.85)`, `stroke-width="4.7"` (box x 1068 to 1170, y 420 to 615.5, centre x 1119); lamp (`dw-lamp`) Panel dark in every frame of the comp |
| Labels | Arial 700 22 px, line-height 28, Label grey, top 676, each 200 px wide and centred: `local police` (x 709.5), `a station` (x 1119) |
| Chip | glass chip (`.pol-chip` of `compositions/g-i1s6-page.html`), left 836, top 316, height 46, padding 0 x 22, Arial 700 26 px, Body light: `a station · county not given in the study` |
| Paper strip | as `.shf-strip` of `compositions/g-i1s7-sheriff.html`: Beige polaroid, left 96, top 800, 1480 x 226 (right 1576, bottom 1026), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2. Quote in Georgia 52 px, Caption dark, left 136: line 1 at top 816 `“were not notified by the local police`, line 2 at top 882 `so we couldn’t prepare our listeners”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 968: `media personnel · Disaster Research Center, 1966, p. 25`. Measure line 1's width in a frame and state it; it must end at least 40 px inside the strip |

Part B, the far end (A4-S12, comp 10.59 to 22.43). The microphone stays where it is:
| Element | Px |
|---|---|
| House | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, roof apex (1488.4, 433.4), aerial at x 1447.6 up to y 407, centre x 1488.5); windows Panel dark in every frame |
| The one link | y 520, x 1170 to 1400, 4 px Label grey, dotted as above |
| Labels | same type, top 676: `radio and TV` replaces `a station` under the microphone (x 1119); `a family` (x 1488.5). Keep each label's box as wide as its text, not 200 px, so the car's way passes it clear |
| Horn on a pole | `media/drawings/horn-pole.svg` inline, `translate(1200 150)`, scale 1 (box x 1200 to 1280, y 150 to 370), lines Label grey 4 px. Open the file and turn the horn's mouth toward the house (mirror the group about x 1240 if it faces left) |
| Horn's way | path `M1290 200 Q1460 200 1488 400`, 4 px Label grey, dotted (`stroke-dasharray="0.1 14"`). By script it passes (1366, 213), (1425, 250), (1465, 313), (1481, 362) and ends 33 px above the roof apex, 22 px right of the aerial's crossbars |
| Horn's label | Arial 700 22 px, Label grey, right aligned to x 1180, top 240: `a few fire sirens` |
| Police car | `media/drawings/police-car.svg` inline, `translate(1130 760)`, scale 1 (box x 1130 to 1370, y 760 to 850, roof speaker up to y 754), lines Label grey 4 px (windows and speaker 3), body (`dw-body`) Panel dark |
| Car's way | path `M1380 805 Q1570 805 1575 620`, 4 px Label grey, dotted. By script it passes (1463, 793), (1524, 759), (1561, 701), (1572, 655): it stays left of x 1600 and passes the `a family` label on its right |
| Car's label | Arial 700 22 px, Label grey, centred on x 1250, top 866: `police car speakers` |

## 4. Must be true in the picture
1. The link from the police desk to the microphone is dotted Label grey from the first frame to the moment it leaves. It never turns amber, white or solid. The microphone's lamp is Panel dark in every frame and its lines are never amber.
2. The chip reads `a station · county not given in the study`. Neither `County A` nor `County B` is on screen in any frame, and no station, town or county is named.
3. The strip carries the note's words in quotation marks, exactly: `“were not notified by the local police so we couldn’t prepare our listeners”`, with its attribution. No "We", no comma, nothing added.
4. The horn on a pole is Label grey and still from the frame it is drawn to the last frame. No arc, ring, line or dot comes out of it, it does not pulse, and its way is never lit.
5. The police car's body is Amber 2 once, for one blink of 0.3 s up and 0.3 s back, on the second sentence. Before and after it is Panel dark with Label grey lines. Its way never lights.
6. Both other ways are dotted and grey, and the house's windows stay Panel dark: the picture never says a siren or a car speaker reached this house.
7. The police desk has left before the house appears: part A and part B are never one chain of four.
8. Nobody is drawn; the car has no markings and no word on it.
9. Nothing of ours in x >= 1600, y >= 680 (the car's way peaks at x 1575). No label under a line, a way or another label.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `a station · county not given in the study` · `local police` · `a station` · `“were not notified by the local police` / `so we couldn’t prepare our listeners”` · `media personnel · Disaster Research Center, 1966, p. 25` · `radio and TV` · `a family` · `a few fire sirens` · `police car speakers`.
Cue words and times are from `audio/a4-s11.words.json` (32 words) and `audio/a4-s12.words.json` (38 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S11 -0.42, A4-S12 10.17) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 10.59). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S11 | 0 | A | 0.42 | 0.00 | first frame: the police desk, the dotted link and the microphone, all Label grey; the chip; the label `a station`. No desk label, no strip |
| 1 | A4-S11 | 5 | local | 1.60 | 1.18 | the label `local police` fades in (0.3 s) |
| 2 | A4-S11 | 9 | told | 2.58 | 2.16 | the police desk's lines turn Amber 2 (0.3 s) and stay |
| 3 | A4-S11 | 13 | headed | 3.64 | 3.22 | the microphone's lines go to Body light and back to Label grey (0.3 s, yoyo). No amber, and the link does not change |
| 4 | A4-S11 | 19 | notified | 5.86 | 5.44 | the paper strip rises with quote line 1 and the attribution (`y:60` to 0 with the fade, 0.4 s, power3.out) |
| 5 | A4-S11 | 26 | so | 8.44 | 8.02 | quote line 2 fades in (0.3 s). Hold: amber desk, grey link, dark microphone, the strip |
| 6 | A4-S12 | 0 | There | 0.42 | 10.59 | the strip, the chip, the police desk with its label and the 837 to 1068 link fade out in place (0.3 s). The label `a station` cross-fades to `radio and TV`. The house draws on (0.5 s) with its label and the 1170 to 1400 link fades in |
| 7 | A4-S12 | 10 | other | 2.66 | 12.83 | the horn on a pole draws on (0.5 s) and its dotted way draws toward the house (0.5 s); 0.25 s later the police car and its way do the same |
| 8 | A4-S12 | 13 | radio | 3.24 | 13.41 | the dots of the microphone to house link go to Body light and back to Label grey in a wave left to right (0.5 s) |
| 9 | A4-S12 | 22 | sirens | 6.48 | 16.65 | the label `a few fire sirens` fades in (0.3 s). The horn itself does not change |
| 10 | A4-S12 | 30 | police | 9.02 | 19.19 | the police car's body fills Amber 2 (0.3 s) and goes back to Panel dark (0.3 s), once; the label `police car speakers` fades in |
| 11 | A4-S12 | 35 | not | 10.24 | 20.41 | the dots of the car's way dim to Label grey at 55 % (0.4 s). Hold to 22.43: microphone, house, three dotted grey ways, two labelled |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s11-farend.html` is the only file the builder writes; `data-composition-id="g-a4s11-farend"`, `data-duration="22.43"`; id prefix `far-`; root `<div id="far-root" ...>` styled through `#far-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Base it copies:** `compositions/g-a4s02-countyb.html` (wave 1) for the police desk, the microphone, the house, the dotted links, the chip and the sweep band; build only after that base has passed its full-size read. The strip is `.shf-strip` of `compositions/g-i1s7-sheriff.html`. `compositions/g-a6s11-sirens.html` (wave 5) uses the same horn drawing and the same rule: the horn never changes.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, file 312 x 184, line 4, telephone 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, file 132 x 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, file 272 x 298, line 4).
- `media/drawings/horn-pole.svg` (object 80 x 220, viewBox -6 -6 92 232, file 92 x 232, line 4). Group stroke only; no sound lines, ever.
- `media/drawings/police-car.svg` (object 240 x 90 with the speaker up to y -6, viewBox -6 -14 252 114, file 252 x 114, line 4, windows and speaker 3). The amber blink is the `dw-body` fill.
All inlined, ids under `far-`; mount rules in `media/drawings/README.md`, which wins over any number here. Wheel hubs drawn as zero-length lines fade in, they take no draw-on.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s11-farend`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill for part A before the strip (0.0 to 5.4) and for part B. Line 4 here: capture 19.49 (the car at full amber) and 19.80 (back to dark) both ways. Line 6 here: the two ways' sample points, the gap from the car's way to the `a family` label and the horn's way to the aerial are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): three grey things and the chip, no amber. Then settled frames: 1.60 (`local police` label), 2.60 (desk amber, link still dotted grey), 3.60 (microphone grey again, lamp dark), 6.00 (strip with line 1), 8.50 (both quote lines, attribution), 11.20 (desk, chip and strip gone; microphone, house, one link, `radio and TV`), 13.70 (horn, car and both ways drawn, all grey), 17.00 (`a few fire sirens`; horn unchanged), 19.49 (car body amber), 19.90 (car dark again, its label on), 21.00 and 22.30 (hold: horn grey, no sound lines, house windows dark).
