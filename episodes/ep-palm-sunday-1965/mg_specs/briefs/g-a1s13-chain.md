Host: id=g-a1s13-chain file=compositions/g-a1s13-chain.html start=227.35 duration=5.75 s (timeline-map.md tables 1 and 5; last sound at 4.75) track=2

# g-a1s13-chain · A1-S13 · the two forecasts reached the local offices in time (wave 1, chain family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county code and no film label belongs in this comp (rules 4 and 8 have nothing to label here). A flash is a stroke or fill change, never a scale pop (rule 12): the intro's 1.04 scale pulse on the list is not copied. Six beats sit in a 4.2 s spoken window, the closest two 0.52 s apart, and no entrance runs longer than 0.5 s (rule 13, checked when this brief was written).
**Spoken (A1-S13):** "The study found those two afternoon forecasts gave the local Weather Bureau offices enough notice."
**One look:** the intro's five-station chain, dark; the teletype lights, the light runs one link to the telephone, a pen tick lands over each, and the study's three words come up on paper. Nothing past the telephone lights.

## 0. What this graphic claims
The 1966 study found that the two afternoon forecasts from Kansas City gave the local Weather Bureau offices enough notice. The first link of the chain worked: forecasters to the local office. The picture makes no claim about the list, the announcer or the family.

## 1. Source
- `edit_script.md` A1-S13, Rows [study printed pp. 9-10: "at 2:00 and 5:20 p.m. SELS gave adequate forewarning to the local WS's"]. The Picture note's paper card: "gave adequate forewarning", source line "Disaster Research Center, 1966, pp. 9-10".
- No crop of study pp. 9-10 is on disk (`mg_specs/acts-plan.md` section 3c lists none), so the three words are retyped on a paper strip, the lift of design sheet section 9. Nothing else from the page is retyped.
- The chain: design sheet section 6 "Intro version" and the built `compositions/g-i1s9-chain.html` (read it: station markup, link paths, the `run()` light and the `draw()` tick are copied from it).

## 2. Datum, scale, orientation
The chain's line is y 520. The warning travels left to right. Stations 1 to 5 stand exactly where the intro placed them. SCHEMATIC, NOT TO SCALE: who told whom.
No desk is drawn. The intro drew the desk on its last word as the place the light stopped; this act has not reached it, and the built family (`mg_specs/briefs/g-a2s03-chain.md`) carries one dotted line from x 800 to x 1170.
Colours (the built intro's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0. The intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) runs the whole window to carry the hold |
| Station 1, teletype | `media/drawings/teletype.svg` inline, `translate(96 450)`, scale 1 (box x 96 to 236, y 450 to 590). At rest: lines `#55606b`, paper (`dw-lamp`) and body Panel dark, bars (`dw-type`) `#55606b`. Lit: lines Headline white, paper Amber 2, bars Caption dark |
| Station 2, telephone | `media/drawings/telephone-lifted.svg` inline, `translate(316 519.6) scale(1.6)`, `stroke-width="2.5"` (4 px lines; box x 316 to 460, handset top y 433). At rest: lines `#55606b`. Lit: lines Headline white, dial fill Amber 2, hub and finger holes Caption dark |
| Station 3, list | the miniature list sheet as built in `g-i1s9-chain.html`: Beige polaroid 260 x 300 at x 540 to 800, y 350 to 650, eight Caption dark sub bars 170 x 10, nine row rules; held at opacity 0.36 from first frame to last |
| Station 4, microphone | `media/drawings/microphone.svg` inline, `translate(1170 420) scale(0.85)`, `stroke-width="4.7"` (box x 1170 to 1272, y 420 to 616); dark: lines `#55606b`, lamp Panel dark |
| Station 5, house | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, aerial to y 407); dark |
| Labels | Arial 700 22 px, line-height 28, Label grey, centred in their boxes, top 676: `Kansas City forecasters` (left 96, width 140, two lines), `Weather Bureau · South Bend` (left 293, width 190), `the list` (left 540, width 260), `an announcer` (left 1121, width 200), `a family` (left 1388, width 200) |
| Links, y 520, 4 px, `#55606b`, round caps | solid 236 to 316 and 460 to 540; dotted (`stroke-dasharray="0.1 14"`) 800 to 1170 and 1272 to 1400 |
| Travelling light | on link 1 only: an Amber 2 line, 6 px, round caps, growing from x 236 to x 316, led by an Amber 2 dot of radius 8; the dot hides on arrival and the link stays Amber 2 |
| Tick 1 | over station 1: path `M148 402 L160 417 L184 384`, 4 px Body light, round caps and joins, no fill (box x 148 to 184, y 384 to 417; 33 px above the teletype) |
| Tick 2 | over station 2: path `M370 402 L382 417 L406 384`, same stroke (16 px above the handset) |
| Paper strip | Beige polaroid, left 96, top 780, 780 x 124 (right 876, bottom 904), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote, Georgia 52 px, Caption dark, left 136, top 792: `“gave adequate forewarning”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 862: `Disaster Research Center, 1966, pp. 9-10`. Measure the quote's width in a frame and state it; it must end at least 40 px inside the strip's right edge |

## 4. Must be true in the picture
1. Only stations 1 and 2 light, and only link 1 carries the light. The light never passes x 316. The list stays at 0.36, the microphone and the house stay dark, and both dotted links stay grey to the last frame.
2. Stations 1 to 5 and the four links sit where the intro placed them, within 2 px. No desk, no stop mark, no headline from the intro.
3. The strip carries the study's own three words in quotation marks, `“gave adequate forewarning”`, and its attribution. No time, no forecast number and no "SELS" is printed: the Picture note asks for none.
4. Each tick is a pen tick in Body light, never red and never amber. There are two ticks, one per lit station, and none over the list.
5. Station 2 lights only after the light has arrived from station 1 (2.60), not before.
6. One source on screen: the strip's attribution. No second source line (design sheet section 10).
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680. No label under a line, a tick or the strip.

## 5. Text (exact) and cues
Text: `Kansas City forecasters` · `Weather Bureau · South Bend` · `the list` · `an announcer` · `a family` · `“gave adequate forewarning”` · `Disaster Research Center, 1966, pp. 9-10`.
Cue words and times are from `audio/a1-s13.words.json` (15 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A1-S13 -0.32) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S13 | 0 | The | 0.32 | 0.00 | first frame: the whole chain at rest. Five stations, four links, five labels, all dark; the list at 0.36. No tick, no strip, no light |
| 1 | A1-S13 | 4 | two | 1.14 | 0.82 | station 1 lights: lines to Headline white, paper to Amber 2, bars to Caption dark (0.3 s, power2.out) |
| 2 | A1-S13 | 6 | forecasts | 1.80 | 1.48 | tick 1 draws on with `strokeDashoffset` (0.25 s) |
| 3 | A1-S13 | 7 | gave | 2.42 | 2.10 | the light runs link 1 from x 236 to x 316 (0.5 s, power2.inOut); it arrives at 2.60 and the dot hides |
| 4 | A1-S13 | 9 | local | 2.94 | 2.62 | station 2 lights: lines to Headline white, dial to Amber 2, holes to Caption dark (0.3 s) |
| 5 | A1-S13 | 12 | offices | 3.70 | 3.38 | tick 2 draws on (0.25 s) |
| 6 | A1-S13 | 13 | enough | 4.20 | 3.88 | the paper strip rises (`y:60` to 0 with the fade, 0.4 s, power3.out). From 4.40 the two amber fills breathe (`fill-opacity` 1 to 0.55, 0.65 s, sine.inOut, yoyo). Hold to 5.75 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a1s13-chain.html` is the only file the builder writes; `data-composition-id="g-a1s13-chain"`, `data-duration="5.75"`; id prefix `ch13-`; root `<div id="ch13-root" ...>` styled through `#ch13-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The host is already mounted in `index.html` as `host-a1s13-chain`; do not edit `index.html`.
**It is a family base.** Later comps copy its stations, links and travelling light, so keep those three as plain, separately named blocks (one group per station, one path per link, one `run(link, x0, x1, at, dur)` helper): `compositions/g-a2s03-chain.html`, `compositions/g-a2s09-countya.html` and `compositions/g-a2s20-front.html` (wave 2, builder 2-c), `compositions/g-a2s11-backup.html` (wave 2), and the wave 3 to 5 chain comps after them. It is sent alone for a full-size read before anyone copies it (template 7a, last line).
**What it copies:** the built `compositions/g-i1s9-chain.html` (station markup, link paths, light, tick draw). It does not copy the eyebrow, the two claim rows, the desk, the stop mark or the headline.
**Assets (paths from the episode folder; all four confirmed on disk 12 Oct 26):**
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152, file 152 x 152, line 4; lit state as `media/drawings/teletype-lit.svg`).
- `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106, file 102 x 106, line 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, file 132 x 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, file 272 x 298, line 4).
All inlined, ids under `ch13-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s13-chain`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; the chain band and the strip are the content, the sweep band carries the ground. Line 4 here: the light's `scaleX` and its `svgOrigin` are set at timeline 0, never only in a later tween's from vars. Line 6 here: the two tick paths (station centre x 166 and x 388, the same offsets) are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the whole chain dark, nothing lit, no strip. Then settled frames: 1.30 (station 1 lit, paper amber), 1.90 (tick 1), 2.35 (light part way along link 1, station 2 still dark), 3.10 (link 1 amber, station 2 lit), 3.80 (tick 2), 4.50 (strip on, both lines read), 5.60 (hold: list dim, microphone and house dark, dotted links grey).
