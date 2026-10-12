Host: id=g-a4s15-chain file=compositions/g-a4s15-chain.html start=793.58 duration=9.92 s (timeline-map.md tables 1 and 5, read 12 Oct 26, 19:33; the mount in index.html wins; last sound at 8.92) track=2

# g-a4s15-chain · A4-S15 · the Weather Bureau sent it; the system broke down on the receiving end (wave 3, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a1s13-chain.md` (read it first: stations, links, light).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county code belongs in this comp: this is the whole system, not County A or County B (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12): the intro's 1.04 scale pulse on the list is not copied. Beats were held against the spoken window when this brief was written (rule 13): the closest two actions start 0.40 s apart ("Weather" at 0.85 and "sent" at 1.25; the desk's pulse for "offices" is held to 5.90, 0.43 s after the strip starts) and no light run is longer than 0.4 s.
**Spoken (A4-S15):** "In most cases the Weather Bureau sent the warning, and the system tended to break down on the receiving end. Key offices and the public often got it late, or not at all."
**One look:** the intro's whole chain; the light runs teletype, telephone, list, reaches the desk and stops there under a red mark; the microphone and the house stay dark; the study's sentence comes up on paper.

## 0. What this graphic claims
In most cases the Weather Bureau did send the warning. The system tended to break down on the receiving end: key offices and the public often got it late, or not at all. The picture is the intro's chain again, with the first three stations lit and the stop at the desk.

## 1. Source
- `edit_script.md` A4-S15, Rows [C11; study printed p. 34: "Crucial organizations and the general public often did not receive the warnings in time or at all"]. The Picture note's quote strip: "the system tended to break down on the receiving end", source line "Disaster Research Center, 1966, p. 34".
- No crop of p. 34 is on disk, so the words are retyped on a paper strip (design sheet section 9). Nothing else from the page is retyped.
- The chain: design sheet section 6 "Intro version" and the built `compositions/g-i1s9-chain.html`, whose last frame this comp rebuilds (stations 1 to 5, the desk at x 840, the stop mark `chn-stop`), without its eyebrow, its two claim rows, its ticks and its headline.

## 2. Datum, scale, orientation
The chain's line is y 520 and the warning travels left to right. Stations 1 to 5, the desk and the links stand exactly where the intro placed them (within 2 px). SCHEMATIC, NOT TO SCALE: who told whom.
"In most cases" is the study's hedge and is spoken; the picture is one schematic chain, not a count of cases, and carries no number.
The desk is the place the light stops. As in the intro it is never amber: its lines go from the dark line to Body light when the light reaches it. The telephone on it has its handset on the cradle.
Colours (the built intro's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Popfig red `#d0121f`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Station 1, teletype | `media/drawings/teletype.svg` inline, `translate(96 450)`, scale 1 (box x 96 to 236, y 450 to 590). At rest: lines `#55606b`, paper (`dw-lamp`) and body Panel dark, bars (`dw-type`) `#55606b`. Lit: lines Headline white, paper Amber 2, bars Caption dark |
| Station 2, telephone | `media/drawings/telephone-lifted.svg` inline, `translate(316 519.6) scale(1.6)`, `stroke-width="2.5"` (box x 316 to 460, handset top y 433). At rest: lines `#55606b`. Lit: lines Headline white, dial fill Amber 2, hub and finger holes Caption dark |
| Station 3, list | the miniature list sheet as built in `g-i1s9-chain.html`: Beige polaroid 260 x 300 at x 540 to 800, y 350 to 650, eight Caption dark sub bars 170 x 10, nine row rules. At rest opacity 0.36; lit opacity 1 |
| Desk | `media/drawings/desk.svg` inline, whole (telephone on its cradle), `translate(840 490) scale(0.85)`, `stroke-width="4.7"`, telephone 3.5 (box x 840 to 1095, y 490 to 617.5, top surface y 524). At rest `#55606b`; reached: Body light. Never amber. It has no label |
| Station 4, microphone | `media/drawings/microphone.svg` inline, `translate(1170 420) scale(0.85)`, `stroke-width="4.7"` (box x 1170 to 1272, y 420 to 616); lines `#55606b`, lamp Panel dark, in every frame |
| Station 5, house | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, aerial to y 407); lines `#55606b`, windows Panel dark, in every frame |
| Labels | Arial 700 22 px, line-height 28, Label grey, centred in their boxes, top 676: `Kansas City forecasters` (left 96, width 140, two lines), `Weather Bureau · South Bend` (left 293, width 190), `the list` (left 540, width 260), `an announcer` (left 1121, width 200), `a family` (left 1388, width 200) |
| Links, y 520, 4 px, `#55606b`, round caps | solid 236 to 316, 460 to 540 and 800 to 840; dotted (`stroke-dasharray="0.1 14"`) 1095 to 1170 and 1272 to 1400 |
| Travelling light | on the three solid links only: an Amber 2 line, 6 px, round caps, growing along the link, led by an Amber 2 dot of radius 8 (the base's `run(link, x0, x1, at, dur)`); a link stays Amber 2 once crossed |
| Stop mark | rect x 837, y 484, 6 x 72, fill Popfig red (`chn-stop` of the built intro), drawn top to bottom (`scaleY` 0 to 1, `svgOrigin:"840 484"` set at timeline 0, 0.25 s); with it one Amber 2 ring at (840, 520), radius 8 to 40, fading out (0.45 s), as the dot dies |
| Paper strip | Beige polaroid, left 96, top 780, 1360 x 124 (right 1456, bottom 904), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote, Georgia 44 px, Caption dark, left 136, top 796: `“the system tended to break down on the receiving end”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 862: `Disaster Research Center, 1966, p. 34`. Measure the quote's width in a frame and state it; it must end at least 40 px inside the strip's right edge (if it does not, drop to 40 px, never widen the strip past x 1576) |

## 4. Must be true in the picture
1. Three things light and no more: the teletype, the telephone and the list, in that order, each only after the light has reached it. The three solid links turn amber as the light crosses them.
2. The light stops at x 840, the desk's left edge. The stop mark is Popfig red, the only red in the comp, and it stays to the last frame. Nothing to the right of it is ever amber: not the desk, not the dotted links, not the microphone or its lamp, not the house or its windows.
3. The desk is never amber. Its telephone's handset is on the cradle. Nobody is drawn.
4. Stations 1 to 5, the desk and the five links sit where the intro placed them, within 2 px. The intro's eyebrow, claim rows, ticks and headline are not in this comp.
5. The strip carries the study's own words in quotation marks, `“the system tended to break down on the receiving end”`, and rises on the second sentence, after the words have been spoken. No "most cases" figure, no percentage, no count.
6. No county code, no town, no station name. The labels are the intro's five.
7. One source on screen: the strip's attribution. No second source line.
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680. No label under a line, the stop mark, the ring or the strip (labels end at y 704, the strip starts at y 780).
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `Kansas City forecasters` · `Weather Bureau · South Bend` · `the list` · `an announcer` · `a family` · `“the system tended to break down on the receiving end”` · `Disaster Research Center, 1966, p. 34`.
Cue words and times are from `audio/a4-s15.words.json` (33 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S15 -0.37) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds. The transcript writes word 18 as `receding`; the spoken word is "receiving" and the strip prints `receiving`.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S15 | 0 | In | 0.37 | 0.00 | first frame: the whole chain at rest. Five stations and the desk in the dark line, five links, five labels, the list at 0.36. No light, no stop mark, no strip |
| 1 | A4-S15 | 1 | most | 0.46 | 0.09 | station 1 lights (lines Headline white, paper Amber 2, bars Caption dark, 0.3 s) and the light runs link 1, x 236 to 316 (0.4 s, power2.inOut) |
| 2 | A4-S15 | 4 | Weather | 1.22 | 0.85 | station 2 lights (lines Headline white, dial Amber 2, 0.3 s) |
| 3 | A4-S15 | 6 | sent | 1.62 | 1.25 | the light runs link 2, x 460 to 540 (0.4 s); on arrival at 1.65 the list goes to opacity 1 (0.3 s) |
| 4 | A4-S15 | 8 | warning | 2.08 | 1.71 | the light runs x 800 to 840 (0.4 s) and reaches the desk at 2.11; the desk's lines go from `#55606b` to Body light (0.3 s). The dot waits at x 840, its fill breathing (`fill-opacity` 1 to 0.55, sine.inOut) |
| 5 | A4-S15 | 14 | break | 3.84 | 3.47 | the dot dies in one ring pulse and the stop mark draws top to bottom (0.25 s) |
| 6 | A4-S15 | 18 | receding | 4.56 | 4.19 | the microphone and the house pulse once to `#b4bcc3` (Body light at 80 %) and back to `#55606b` (0.3 s each way). No amber |
| 7 | A4-S15 | 20 | Key | 5.84 | 5.47 | the paper strip rises with the quote and its attribution (`y:60` to 0 with the fade, 0.4 s, power3.out) |
| 8 | A4-S15 | 21 | offices | 5.94 | 5.57 | at 5.90, once the strip is up, the desk's lines go to Headline white and back to Body light (0.3 s each way) |
| 9 | A4-S15 | 24 | public | 6.86 | 6.49 | the house's lines pulse to `#b4bcc3` and back (0.3 s each way); its windows stay Panel dark |
| 10 | A4-S15 | 30 | not | 8.66 | 8.29 | the stop mark's fill goes to Headline white and back to Popfig red (0.15 s each way). Hold to 9.92; the amber fills of stations 1 and 2 breathe from 2.20 (`fill-opacity` 1 to 0.55, 0.65 s, sine.inOut, yoyo, finite repeats) to carry it |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s15-chain.html` is the only file the builder writes; `data-composition-id="g-a4s15-chain"`, `data-duration="9.92"`; id prefix `ch15-`; root `<div id="ch15-root" ...>` styled through `#ch15-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Base it copies:** `compositions/g-a1s13-chain.html` (wave 1): the five station groups, the link paths and the `run()` light, unchanged in place. From the built `compositions/g-i1s9-chain.html`: the desk group at `translate(840 490)`, the ring `chn-ringp`, the stop mark `chn-stop` and the pulse of stations 4 and 5. Build only after `g-a1s13-chain` has passed its full-size read. The built intro comp carries this same picture: the timeline's author declares the repeat in `index.html` (`data-callback`), the builder does not. Nothing later copies this comp; `compositions/g-z1s02-row.html` (wave 5) returns to the chain with the stop mark.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152, file 152 x 152, line 4; lit state as `media/drawings/teletype-lit.svg`).
- `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106, file 102 x 106, line 3).
- `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, file 312 x 184, line 4, telephone 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, file 132 x 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, file 272 x 298, line 4).
All inlined, ids under `ch15-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s15-chain`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; the chain band and the strip are the content, the sweep band carries the ground. Line 4 here: each light line's `scaleX` with its `svgOrigin`, and the stop mark's `scaleY` with `svgOrigin:"840 484"`, are set at timeline 0, never only in a later tween's from vars; capture 1.45 (light on link 2) and 3.60 (stop mark part drawn) both ways. Line 6 here: the station boxes and link ends are read from the base and the built intro by a script and the largest difference is stated in the receipt (it must be 2 px or less).

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the whole chain dark with the desk, no light, no stop mark. Then settled frames: 0.70 (station 1 lit, link 1 amber), 1.20 (station 2 lit), 1.45 (light part way along link 2, list still dim), 2.00 (list at full paper), 2.60 (light at the desk, desk Body light, not amber), 3.90 (stop mark red, ring gone), 4.90 (microphone and house dark again), 6.30 (strip on, quote on one line, attribution under it), 7.20 (house dark, windows dark), 8.80 and 9.80 (hold: three lit stations, red stop mark, nothing amber right of x 840).
