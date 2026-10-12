Host: id=g-a2s09-countya file=compositions/g-a2s09-countya.html start=352.82 duration=18.79 s (timeline-map.md; wav sum 18.34 s plus its gaps) track=2

# g-a2s09-countya · A2-S9, A2-S10 · the report that ran the wrong way, and the air that came after (wave 2, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 6, 7, 8, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No page crop holds past about 8 seconds without a visible change (rule 7). The study's hidden county is labelled `County A` only, and `County B` never appears in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A2-S9):** "At five fifty, State Police in one county saw a tornado and phoned the Weather Bureau. It's the county whose city police were listening, and told nobody until the first tornado hit. The study calls it County A."
**Spoken (A2-S10):** "By the time stations put that report on the air, tornadoes were already touching down there."
**One look:** a telephone whose light runs back to the Weather Bureau's teletype; the intro's page returns small; then a microphone that goes red only after three marks have landed.

## 0. What this graphic claims
At 5:50 PM State Police in one county saw a tornado and telephoned the Weather Bureau: the message ran toward the Weather Bureau, the reverse of the telephone list. It is the same county whose city police told nobody until the first tornado hit, and the study calls it County A. By the time stations broadcast that report, tornadoes were already touching down there.

## 1. Source
- `edit_script.md` A2-S9 (Rows [A7; study printed p. 19] and [C2; study printed pp. 19-20], County A) and A2-S10 (Rows [A7; study printed p. 19], County A).
- Page: `media/docs/study-p20-police-crop.png` (1460 x 647, study printed pp. 19-20), the crop the intro's `compositions/g-i1s6-page.html` already mounts with its underline. The crop does not print the county's code.
- "County A" is the study's own code, not a place name. No town, no county outline and no map is drawn.

## 2. Datum, scale, orientation
The chain line is y 520. The Weather Bureau's teletype stands on the left and the State Police telephone on the right, so the light runs right to left: the wrong way down a chain that everywhere else runs left to right.
Clock angles, clockwise from 12 (by script): 5:50 is hour 175.0, minute 300.
Page card scale 0.45: the crop draws 657 x 291 px. It is a callback to a page the viewer has read, not a new reading: one lit sentence, the rest dimmed.

## 3. Geometry (screen px)
A2-S9:
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; eyebrow `STATE POLICE`; time `5:50 PM`; place `one Indiana county`; hands 175.0 and 300 degrees |
| County chip | glass chip, left 96, top 316, height 46, padding 0 x 22, Arial 700 26 px, Body light: `County A` followed by a second span ` · the study's own name for it` |
| Teletype (Weather Bureau) | `media/drawings/teletype.svg` inline, `translate(316 450)`, scale 1 (box x 316 to 456, y 450 to 590); lines Body light; its paper (`dw-lamp`) lights Amber 2 at step 5, bars (`dw-type`) Caption dark, as `media/drawings/teletype-lit.svg` |
| Label | `Weather Bureau · South Bend`, Arial 700 22 px, Label grey, centred on x 386, top 676 |
| Telephone (State Police) | `media/drawings/telephone-lifted.svg` inline, `translate(760 519.6) scale(1.6)` (box x 760 to 904, handset top y 433); lines Body light |
| Label | `State Police`, same type, centred on x 832, top 676 |
| Link | y 520, x 456 to 760, solid 4 px Label grey |
| Light | an Amber 2 run, 60 px long, 6 px, travelling from x 760 to x 456 |
| Page card | Beige polaroid border 10 px, left 899, top 96, 677 x 311 (right 1576, bottom 407), shadow as design sheet section 9; the crop inside at 657 x 291 |
| Underline and unlit page | the underline boxes and the 45 % Panel dark covers of `compositions/g-i1s6-page.html`, each number multiplied by 0.45; underline Popfig red 3 px |
| Page source | right aligned at x 1576, top 417: Arial 700 20 px, Body light with the credit shadow: `Disaster Research Center, 1966, pp. 19-20` |

A2-S10:
| Element | Px |
|---|---|
| Microphone | `media/drawings/microphone.svg` inline, `translate(330 300) scale(2)` (box x 330 to 570, y 300 to 760), `stroke-width="3"` on the group (6 px lines); lines Body light; lamp (`dw-lamp`) Panel dark until step 13 |
| Label | `a station`, Arial 700 26 px, Body light, centred on x 450, top 790 |
| Ground strip | one line, y 760, x 700 to 1560, 4 px Label grey; nothing on it at first |
| Tornado marks | `media/drawings/tornado-mark.svg` inline three times, scale 2 (120 x 160 px), `stroke-width="3"` on each group (6 px lines), stroke Body light, never red. Boxes: x 800 to 920, x 1030 to 1150, x 1260 to 1380, all y 600 to 760 (each mark's point rests on the line) |
| County chip | the same chip in the same place, now reading `County A` alone |

## 4. Must be true in the picture
1. The light runs from the State Police telephone to the Weather Bureau's teletype, right to left, once. Nothing runs the other way in this comp.
2. The stamp reads 5:50 PM and names no town and no county: its place line is `one Indiana county`. The page prints neither.
3. `County A` lands on the spoken words "County A", not before, and never shares a frame with `County B`.
4. The page card is the scan itself, the same crop as the intro, with the same sentence underlined. Nothing on it is retyped.
5. The microphone's lamp is dark while the three marks land and turns Popfig red only after the third. Its label is `a station`: no call letters, no name.
6. The three marks carry no number and no label: they say "tornadoes", not a count for the county.
7. No person is drawn. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `STATE POLICE` · `5:50 PM` · `one Indiana county` · `County A` · ` · the study's own name for it` · `Weather Bureau · South Bend` · `State Police` · `Disaster Research Center, 1966, pp. 19-20` · `a station`. Page words are the image.
Cue words and times are from `audio/a2-s9.words.json` and `a2-s10.words.json` as re-transcribed on 12 Oct 26 (17:45 to 17:50). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S9 -0.31, A2-S10 12.71) plus the word's time; a segment's first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S9 | 0 | At | 0.31 | 0.00 | first frame: ground only |
| 1 | A2-S9 | 1 | 5 | 0.40 | 0.09 | clock stamp slides in from the left (0.6 s, power3.out); the minute hand sweeps its last 30 degrees; the time lands on "five fifty" |
| 2 | A2-S9 | 3 | state | 1.62 | 1.31 | the telephone draws on (0.6 s), label `State Police` fades in |
| 3 | A2-S9 | 12 | phoned | 3.90 | 3.59 | the link draws from x 760 to x 456 (0.3 s) and the teletype draws on at rest (0.5 s) with its label |
| 4 | A2-S9 | 14 | weather | 4.28 | 3.97 | the light leaves the telephone and runs to the teletype (0.6 s, ease none) |
| 5 | A2-S9 | 15 | bureau. | 4.46 | 4.15 | when the light arrives (4.57) the teletype's paper turns Amber 2 and stays |
| 6 | A2-S9 | 16 | It's | 5.64 | 5.33 | the page card slides in from the right (`x:700` to 0, 0.6 s, power3.out) with its source |
| 7 | A2-S9 | 25 | told | 8.02 | 7.71 | the unlit page covers fade in (0.4 s) and the underline draws under the page's sentence, line box by line box (0.8 s in all) |
| 8 | A2-S9 | 36 | County | 11.92 | 11.61 | the county chip lands (0.3 s, `y:16` to 0 with the fade), reading `County A · the study's own name for it` |
| 9 | A2-S10 | 0 | By | 0.48 | 13.19 | the stamp exits left, the card exits right, telephone, link, teletype and labels fade out (all 0.4 s); the chip's second span fades out so it reads `County A`; the ground strip draws left to right (0.5 s) |
| 10 | A2-S10 | 3 | stations | 0.90 | 13.61 | the microphone draws on (0.6 s), lamp dark, label `a station` |
| 11 | A2-S10 | 10 | tornadoes | 3.20 | 15.91 | mark one lands at x 800 to 920 (`y:-30` to 0 with a 0.3 s fade) |
| 12 | A2-S10 | 12 | already | 3.80 | 16.51 | mark two lands at x 1030 to 1150 |
| 13 | A2-S10 | 13 | touching | 4.10 | 16.81 | mark three lands at x 1260 to 1380 |
| 14 | A2-S10 | 15 | there. | 4.74 | 17.45 | the lamp turns Popfig red (0.2 s fill change). Hold to 18.79 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s09-countya.html` is the only file the builder writes; `data-composition-id="g-a2s09-countya"`; id prefix `cnta-`; root `<div id="cnta-root" ...>` styled through `#cnta-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the chain family base `compositions/g-a1s13-chain.html` (wave 1; brief `mg_specs/briefs/g-a1s13-chain.md`) for stations, link and travelling light; the page card, underline and unlit page of the built `compositions/g-i1s6-page.html`; the clock stamp of the built `compositions/g-t1s2-warning.html`; the lamp of the built `compositions/g-i1s5-onair.html`.
**Assets (paths from the episode folder):**
- `media/docs/study-p20-police-crop.png` (1460 x 647), mounted as an `<img>` at 657 x 291.
- `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106), `media/drawings/teletype.svg` (object 140 x 140; lit state as `media/drawings/teletype-lit.svg`), `media/drawings/microphone.svg` (object 120 x 230), `media/drawings/tornado-mark.svg` (object 60 x 80, viewBox -6 -6 72 92, line 6): inlined, ids under `cnta-`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s09-countya`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the scaled underline boxes (the built comp's numbers times 0.45) and the two hand angles are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground only. Then settled frames: 0.90 (stamp, 5:50 PM), 2.10 (telephone and label), 4.30 (light on the link, moving left), 4.90 (teletype paper amber), 6.10 (page card), 8.80 (underline complete, page dimmed), 12.10 (chip with both spans), 13.80 (strip and chip `County A`, old elements gone), 14.40 (microphone, lamp dark), 16.30, 16.75 and 17.20 (one, two, three marks; lamp still dark), 17.90 and 18.70 (lamp red).
