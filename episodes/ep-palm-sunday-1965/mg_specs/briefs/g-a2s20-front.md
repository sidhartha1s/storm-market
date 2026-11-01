Host: id=g-a2s20-front file=compositions/g-a2s20-front.html start=462.81 duration=8.07 s (timeline-map.md; wav 7.72 s plus its gaps) track=2

# g-a2s20-front · A2-S20 · a warning can start anywhere: the chain's front end (wave 2, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 6, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county chip belongs in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A2-S20):** "A warning could start anywhere. A person sees a tornado and calls the police, and the police pass it to the Weather Bureau."
**One look:** a house, a lifted telephone, a police desk and one long link; the light runs the wrong way, toward the Weather Bureau.

## 0. What this graphic claims
A warning did not have to begin at the Weather Bureau. A person who saw a tornado could call the police, and the police would pass it on to the Weather Bureau: the message entered the chain at its far end and ran back up it.

## 1. Source
- `edit_script.md` A2-S20, Rows [study printed p. 12: a warning "can enter the system at any point"; "An individual may sight a tornado, call the police, who in turn will relay the message to the WB"].
- The chain's stations and line: design sheet section 6 "Intro version" and the built `compositions/g-i1s9-chain.html`.

## 2. Datum, scale, orientation
The chain line is y 520, as in the intro. The house stands in the intro's station 5 slot and the desk in the intro's desk slot, so the viewer sees the same chain from its other end. The Weather Bureau is to the left, where the intro put it; the light therefore runs right to left.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| House | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)` (box x 1400 to 1577, y 430 to 600, aerial to y 407); `stroke-width="5"` on the group (3.4 px lines); lines Body light, windows Panel dark |
| House label | `a person`, Arial 700 22 px, Label grey, centred on x 1488, top 676 |
| Telephone | `media/drawings/telephone-lifted.svg` inline, `translate(1166 537.2) scale(1.2)` (body x 1166 to 1274, base y 590, handset top y 472); lines Body light |
| Police desk | `media/drawings/desk.svg` inline, `translate(840 490) scale(0.85)` (box x 840 to 1095, y 490 to 618), its telephone on the cradle; lines Body light |
| Desk label | `the police`, same type, centred on x 967, top 676 |
| Links, y 520, 4 px, Label grey, solid | x 1274 to 1400 (house to telephone), x 1095 to 1166 (telephone to desk), x 420 to 840 (desk toward the Weather Bureau) |
| Link end | an arrowhead at x 400 pointing left: two 18 px strokes at 35 degrees to the line, 4 px, Label grey, meeting at (400, 520) |
| End label | two lines, right aligned at x 380: `Weather Bureau` top 490 and `South Bend` top 524, Arial 700 26 px, Body light, line-height 30 |
| "Anywhere" rings | three circles on the long link, y 520. Ring 1: centre x 700, on the long link and whole inside x 420 to 840: midway between ring 2 at x 560 and the link's end at x 840 (the spacing of rings 2 and 3 continued would land at x 960, past the link). This brief first said x 980, a slip: that is off the long link, and the words win (lead's ruling of 12 Oct 26). Rings 2 and 3: x 560 and x 760. Each ring: radius grows 0 to 18 px, 3 px Amber 2 stroke, each fades as it grows (0.5 s), once |
| Light | an Amber 2 run, 60 px long, 6 px, travelling along the links from the house to the arrowhead |
| Source line | design sheet section 10, left 96, bottom 60: `Disaster Research Center, 1966, p. 12` |

## 4. Must be true in the picture
1. The light starts at the house and ends at the Weather Bureau's label, right to left: house, telephone, desk, long link, arrowhead. It never runs left to right.
2. The house and the desk stand in the intro's own slots, within 2 px, so the frame reads as the same chain.
3. No person is drawn; the label `a person` is the only sign of one.
4. The desk carries no stop mark and no red: in this beat the police pass the message on.
5. No time, no county chip, no town other than `South Bend` in the end label. No list sheet and no microphone: this is the front end only.
6. Nothing appears before its spoken word, with one exception by the lead's ruling of 12 Oct 26: the end label `Weather Bureau` / `South Bend` is on from step 1 of the cue table (it is spoken at 6.34 s), because the label names the far end of the long link while the link draws. The cue table stands. Nothing of ours in x >= 1600, y >= 680 (the house label ends left of x 1600).
7. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry. As built and accepted by the lead, 12 Oct 26: the whole stage sits 80 px left and 50 px up until "pass" at 5.60 s; the empty block of 60.0 % from 0.10 to 2.46 s is accepted as under 3 s.

## 5. Text (exact) and cues
Text: `Weather Bureau` · `South Bend` · `a person` · `the police` · `Disaster Research Center, 1966, p. 12`.
Cue words and times are from `audio/a2-s20.words.json` as re-transcribed on 12 Oct 26 (17:45 to 17:50). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S20 -0.32) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S20 | 0 | A | 0.32 | 0.00 | first frame: ground only |
| 1 | A2-S20 | 1 | warning | 0.42 | 0.10 | the long link draws from x 420 to x 840 (0.6 s), the arrowhead and the end label fade in (0.3 s); source line in |
| 2 | A2-S20 | 4 | anywhere. | 1.24 | 0.92 | the three rings pulse in turn, 0.2 s apart: ring 1 at x 700 (on the long link; not 980), then x 560, then x 760 |
| 3 | A2-S20 | 6 | person | 2.78 | 2.46 | the house draws on (0.7 s), label `a person` |
| 4 | A2-S20 | 11 | calls | 4.20 | 3.88 | the telephone draws on with its link to the house (0.4 s); the light runs house to telephone (0.3 s) |
| 5 | A2-S20 | 13 | police, | 4.62 | 4.30 | the desk draws on with its link (0.5 s), label `the police`; the light runs telephone to desk (0.3 s) and the desk's lines turn Amber 2 for 0.4 s, then back |
| 6 | A2-S20 | 17 | pass | 5.92 | 5.60 | the light leaves the desk and runs the long link to the arrowhead (ease none; it arrives at 6.52) |
| 7 | A2-S20 | 22 | bureau. | 6.84 | 6.52 | the arrowhead turns Amber 2 and the end label turns Headline white (0.2 s). Hold to 8.07 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s20-front.html` is the only file the builder writes; `data-composition-id="g-a2s20-front"`; id prefix `front-`; root `<div id="front-root" ...>` styled through `#front-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the chain family base `compositions/g-a1s13-chain.html` (wave 1; brief `mg_specs/briefs/g-a1s13-chain.md`) for the links and the travelling light; station slots from the built `compositions/g-i1s9-chain.html`. Later comps that reuse this front end: `g-a5s12-spotters`, `g-a6s08-spotters`.
**Assets (paths from the episode folder):** `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298), `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106), `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184): inlined, ids under `front-`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s20-front`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the station positions are the intro's numbers, copied, and stated in the receipt beside the built comp's.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground only. Then settled frames: 0.80 (long link, arrowhead, end label), 1.20 and 1.50 (rings in turn, on the link), 2.20 (rings gone), 3.30 (house and label), 4.20 (telephone, light arrived), 5.00 (desk and label, desk back to Body light), 6.10 (light on the long link, moving left), 6.90 and 8.00 (arrowhead amber, end label white).
