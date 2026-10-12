Host: id=g-a4s09-clock file=compositions/g-a4s09-clock.html start=726.83 duration=21.86 s (timeline-map.md tables 1 and 5, read 12 Oct 26, 19:33; the mount in index.html wins; last sound at 20.86) track=2

# g-a4s09-clock · A4-S9, A4-S10 · the clock ran to 8:07 PM, then every light went out (wave 3, county chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 8, 9. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a4s02-countyb.md` (read it first: this comp opens on that chain).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). The study's hidden county is labelled `County B` only; `County A` never appears in this comp, and no real county, town or person name appears in it (rule 8). No page crop holds past about 8 s without a visible change (rule 7): the page window is on for 13.0 s and changes at 11.50, 12.38 and, around it, at 14.78, 15.82, 16.26, 16.92 and 19.82. A flash is a stroke or fill change, never a scale pop (rule 12). Beat counts were held against the spoken windows when this brief was written (rule 13): the clock's run is 37 one-minute steps in 3.02 s (0.082 s a step), and the closest two lights-out beats are 0.44 s apart, each a 0.3 s stroke change.
**Spoken (A4-S9):** "So the clock ran. The tornado hit the county seat at eight oh seven, about thirty five minutes after he first radioed the police."
**Spoken (A4-S10):** "The county's sheriff learned of it when it was going over. "We didn't have any warning at all," the sheriff said. As it went through, power to the stations and the public was cut, and city police communication was out for about an hour."
**One look:** County B's chain stuck on the police desk with its red stop mark; the clock beside it runs from about 7:30 to 8:07 and an amber arc grows round its face; the sheriff's page line comes up underneath; then the chain's lights go out one by one, the police desk last.

## 0. What this graphic claims
In County B the warning stayed at the city police desk while the clock ran: the tornado hit the county seat at 8:07 PM, which the study puts at about 35 minutes after the civil defense director first radioed the police. The county's sheriff said "We didn't have any warning at all." As the tornado went through, power to the stations and the public was cut and city police communication was out for about an hour.

## 1. Source
- `edit_script.md` A4-S9, Rows [C7; study printed p. 22] (County B), and A4-S10, Rows [C6; study printed p. 22] and [D, County B row; study printed p. 22]. The two Picture notes are the only source of what is drawn.
- Page crop: `media/docs/study-p22-sheriff-crop.png` (1460 x 642, ten typed lines, from `media/docs/study-pdf-24-orig.png`, study printed p. 22). Line boxes measured on the file by a row scan on 12 Oct 26: lines 4 and 5 are y 225 to 258 and y 263 to 298. The words `We didn't have any warning` sit at crop x 809 to 1293, y 225 to 257 and `at all` at x 198 to 286, y 263 to 296 (the two lit windows of the built `compositions/g-i1s7-sheriff.html`, `sA1` and `sA2`).
- The crop carries the study's code "County B" in a line that is not shown here; "County A" is not in it.
- The chain, the radio arc, the chip and the stamp with `about`: `mg_specs/briefs/g-a4s02-countyb.md` and its built comp. The stop mark: the built `compositions/g-i1s9-chain.html` (`chn-stop`), and `mg_specs/briefs/g-a4s06-died.md`, which lands it on this chain two comps earlier.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE. The chain's line is y 520 and the message runs left to right: civil defense desk, police desk, microphone, house. Every station box, link, label and the arc are the numbers of `mg_specs/briefs/g-a4s02-countyb.md` section 3, unchanged.
Clock angles, clockwise from 12 (by script): about 7:30 is hour 225.0, minute 180; 8:07 is hour 243.5, minute 42. The run is 37 minutes: the minute hand turns 222 degrees (180 to 402) and the hour hand 18.5 degrees.
**The label says 35, the hands say 37.** "About 35 minutes" is the study's figure and is printed as the study's (`the study says: about 35 minutes`). The hands show the two clock times the script gives. Neither number is corrected to the other and "37" is printed nowhere.
Page window scale 0.6: a typed line box of 34 to 36 px in the file is 20.4 to 21.6 px on screen, over the 19 px floor. At any smaller scale it falls under the floor, so the whole crop is not shown small: only its two quote lines are, with the words retyped under them.
Colours (the built hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b` (Label grey at 55 %); Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Popfig red `#d0121f`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
Ground: canvas gradient, on from frame 0, with the family's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window.

The chain, as `g-a4s02-countyb` at full size (copy its group):
| Element | Px and opening state |
|---|---|
| Civil defense desk | `media/drawings/desk.svg` inline without its `dw-phone` group, `translate(96 490) scale(0.85)`, `stroke-width="4.7"` (box x 96 to 351, y 490 to 617.5). Opens Amber 2 |
| Police desk | `media/drawings/desk.svg` inline, whole, `translate(582 490) scale(0.85)`, `stroke-width="4.7"`, telephone 3.5 (box x 582 to 837). Opens Amber 2 |
| Stop mark | rect x 837, y 484, 6 x 72, fill Popfig red, at the police desk's right edge where the dotted link starts. Opens on. If `mg_specs/briefs/g-a4s06-died.md` gives another box for it, that brief wins and this comp copies it |
| Microphone | `media/drawings/microphone.svg` inline, `translate(1068 420) scale(0.85)`, `stroke-width="4.7"` (box x 1068 to 1170, y 420 to 615.5). Opens Label grey, lamp Panel dark |
| House | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, aerial to y 407). Opens Label grey, windows Panel dark |
| Links, y 520, 4 px, dotted (`stroke-dasharray="0.1 14"`, round caps) | 837 to 1068 and 1170 to 1400, Label grey. The ghost of A4-S5 is gone (it faded in `g-a4s06-died`) |
| Radio arc | path `M224 508 Q425 300 626 508`, 4 px, dotted like the links. Opens Amber 2 |
| Labels | Arial 700 22 px, line-height 28, Label grey, top 676, each 200 px wide and centred on its station: `civil defense` (x 223.5), `city police` (x 709.5), `the radio station` (x 1119), `a family` (x 1488.5) |
| County chip | glass chip (`.pol-chip` of `compositions/g-i1s6-page.html`), left 836, top 316, height 46, padding 0 x 22, Arial 700 26 px, Body light: `County B`. On in every frame |

The clock (design sheet section 8, as `g-a4s02-countyb` builds it):
| Element | Px |
|---|---|
| Stamp card | glass card left 96, top 96, 590 x 200. On from frame 0 |
| Face | `media/drawings/wall-clock.svg` inline at `translate(129 134)` (centre (191, 196), radius 62). Opens at hour 225.0, minute 180 |
| `about` | Arial 700 26 px, Body light, left 286, top 108. Opens on; fades when the run starts |
| Time | Courier New 700 84 px, Amber 2, x 284, y 142. Opens `7:30 PM`; runs minute by minute (`7:31 PM` ... `7:59 PM`, `8:00 PM` ... `8:07 PM`) from a 0 to 37 proxy tween whose `onUpdate` writes the text (seek-safe); ends `8:07 PM`. Give the time a fixed width box so the card does not shift as digits change |
| Elapsed arc | circle arc, centre (191, 196), radius 74, from 180 degrees clockwise through 222 degrees to 42 degrees (from (191, 270) round the left and top to (240.5, 141.0); length 286.7 px), Amber 2, 6 px, round caps, no fill. Drawn with `strokeDashoffset` locked to the minute hand (same start, same duration, same ease) |
| Study label | glass chip, left 96, top 312, height 46, padding 0 x 22, Arial 700 26 px, Body light: `the study says: about 35 minutes` |

The sheriff's line (A4-S10), lower band:
| Element | Px |
|---|---|
| Paper strip | Beige polaroid, left 96, top 760, 1000 x 250 (right 1096, bottom 1010), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2 |
| Page window | a 876 x 47.4 px window at (116, 778) showing rows y 221 to 300 of `media/docs/study-p22-sheriff-crop.png`: the `<img>` is 876 x 385.2 (scale 0.6), `mix-blend-mode:multiply`, shifted up 132.6 px inside an `overflow:hidden` box. It shows the page's two lines whole, edge to edge |
| Unlit page | Panel dark at 45 % over the window, except two lit boxes, window px: `We didn't have any warning` x 485.4 to 775.8, y 2.4 to 21.6; `at all` x 118.8 to 171.6, y 25.2 to 45.0 |
| Underlines | Popfig red, 3 px, drawn left to right with `scaleX` (`transformOrigin:"left center"`): under box 1 at window y 23.6, under box 2 at window y 47.0 (it may sit on the window's bottom edge; extend the window box 4 px down for it, with no page ink in the extra rows) |
| Retyped quote | Georgia 52 px, Caption dark, left 136, top 846: `“We didn’t have any warning at all”` |
| Attribution | Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 942: `County B's sheriff · Disaster Research Center, 1966, p. 22` |

## 4. Must be true in the picture
1. The first frame is the chain as `g-a4s06-died` left it: civil defense desk amber, radio arc amber, police desk amber with the red stop mark at its right edge, microphone and house Label grey with lamp and windows dark. Nothing past the stop mark is amber in any frame.
2. The clock starts at 7:30 with `about` over the time and ends at `8:07 PM` with hands at 243.5 and 42 degrees and no `about`. The minute hand, the time text and the amber arc move together and stop together on the spoken "eight oh seven".
3. The arc spans 222 degrees, from the 6 to just past the 1. The chip under the stamp reads `the study says: about 35 minutes`; the number 37 is never printed.
4. The stop mark is Popfig red in every frame and never leaves. It is the only red on the chain. The two underlines on the page window are the only other red.
5. The page window shows the page's own two typed lines, not retyped, and nothing of the lines above or below. The underlined words are `We didn't have any warning` and `at all`, as in the intro.
6. `County B` is the only county label, and the attribution reads `County B's sheriff`. No `County A`, no real county, town, river or station name.
7. Lights go out in this order: the radio arc, the civil defense desk, then the microphone and the house drop from Label grey to the dark line, and the police desk last. In the last frame no line on the chain is amber; the stamp's time stays Amber 2 (it is the clock, not a light on the chain).
8. Nobody is drawn. The police desk's telephone stays on its cradle.
9. Nothing of ours in x >= 1600, y >= 680. No label under a line, the arc, a dot or another label: the strip's top (760) clears the station labels (bottom 704) by 56 px.

## 5. Text (exact) and cues
Text: `County B` · `about` · `7:30 PM` running to `8:07 PM` · `the study says: about 35 minutes` · `civil defense` · `city police` · `the radio station` · `a family` · `“We didn’t have any warning at all”` · `County B's sheriff · Disaster Research Center, 1966, p. 22`. Page words are the image.
Cue words and times are from `audio/a4-s9.words.json` (21 words) and `audio/a4-s10.words.json` (44 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S9 -0.51, A4-S10 7.86) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 8.35). Retime from the word, never from the seconds. The transcript writes "eight oh seven" as `807,` and "thirty five" as `35`.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S9 | 0 | So | 0.51 | 0.00 | first frame: the held chain (truth 1), chip `County B`, the stamp reading `about` over `7:30 PM` with hands at 225.0 and 180. No arc, no study label, no strip |
| 1 | A4-S9 | 3 | ran. | 1.00 | 0.49 | the clock runs: minute hand 180 to 402, hour hand 225.0 to 243.5, the time text steps a minute at a time, the amber arc grows with the minute hand (3.02 s, power1.inOut, all four on one tween start and duration); `about` fades out over the first 0.3 s |
| 2 | A4-S9 | 11 | 807, | 4.02 | 3.51 | the run ends on this word: `8:07 PM`, hands at 243.5 and 42. The time's fill goes to Headline white and back to Amber 2 (0.3 s each way) |
| 3 | A4-S9 | 13 | 35 | 5.40 | 4.89 | the study label `the study says: about 35 minutes` rises under the stamp (`y:16` to 0 with the fade, 0.3 s) |
| 4 | A4-S9 | 18 | radioed | 6.90 | 6.39 | the radio arc's dots go to Headline white and back to Amber 2 in a wave from left to right (0.5 s in all) |
| 5 | A4-S9 | 20 | police. | 7.46 | 6.95 | the stop mark's fill goes to Headline white and back to Popfig red (0.15 s each way) |
| 6 | A4-S10 | 2 | sheriff | 1.00 | 8.86 | the paper strip rises with the page window on it, unlit, and the attribution (`y:60` to 0 with the fade, 0.4 s, power3.out). No retyped quote yet |
| 7 | A4-S10 | 11 | We | 3.64 | 11.50 | lit box 1 opens and its underline draws (0.5 s); the retyped quote fades in (0.3 s) |
| 8 | A4-S10 | 16 | at | 4.52 | 12.38 | lit box 2 opens and its underline draws (0.25 s) |
| 9 | A4-S10 | 21 | As | 6.92 | 14.78 | the radio arc's stroke goes from Amber 2 to Label grey (0.4 s) |
| 10 | A4-S10 | 25 | power | 7.96 | 15.82 | the civil defense desk's lines go from Amber 2 to Label grey (0.3 s) |
| 11 | A4-S10 | 28 | stations | 8.40 | 16.26 | the microphone's lines drop from Label grey to the dark line `#55606b` (0.3 s); its label dims to 55 % |
| 12 | A4-S10 | 31 | public | 9.06 | 16.92 | the house's lines drop the same way (0.3 s); its label dims to 55 % |
| 13 | A4-S10 | 39 | out | 11.96 | 19.82 | the police desk's lines go from Amber 2 to Label grey (0.4 s), last. The stop mark stays red. Hold to 21.86: stamp `8:07 PM`, the arc on the face, the study label, the chip, the strip |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s09-clock.html` is the only file the builder writes; `data-composition-id="g-a4s09-clock"`, `data-duration="21.86"`; id prefix `clk9-`; root `<div id="clk9-root" ...>` styled through `#clk9-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`; the host is mounted by the timeline's author.
**Base it copies:** `compositions/g-a4s02-countyb.html` (wave 1): the county chain group, the radio arc, the chip, the stamp with `about` in the eyebrow slot, the sweep band. Build only after that base has passed its full-size read. The stop mark and its fill are `chn-stop` of `compositions/g-i1s9-chain.html`. The page window, unlit layer and underline code are those of `compositions/g-i1s7-sheriff.html` at scale 0.6. Nothing later copies this comp.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, file 312 x 184, line 4, telephone 3), inlined twice.
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, file 132 x 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, file 272 x 298, line 4).
- `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136, file 136 x 136, line 4, ticks 3, hands 5; `dw-hour` and `dw-minute` turn about (62, 62)).
- `media/docs/study-p22-sheriff-crop.png` (1460 x 642), mounted as an `<img>` at 876 x 385.2.
Drawings inlined, ids under `clk9-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s09-clock`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type may name this comp for the typed page line beside the Georgia quote; that is the opening's accepted pattern (plan rule 10): state it in the receipt, do not restyle.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: the hand rotations with their `svgOrigin`, the arc's dash offset and the time proxy are set at timeline 0; capture 2.00 (mid run) both ways and state the time text read in each (it must be the same minute). Line 6 here: the two end angles, the arc's length and end point, the window's offset and the four lit-box numbers are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the held chain with the red stop mark, `County B`, the stamp at `about` `7:30 PM`. Then settled frames: 2.00 (mid run: time between 7:30 and 8:07, arc part drawn, no `about`), 3.90 (`8:07 PM`, hands at 243.5 and 42, arc complete), 5.30 (study label, clear of the chip and the desk), 6.80 (arc dots amber again), 7.60 (stop mark red), 9.40 (strip up, window unlit, both typed lines whole and readable), 12.10 (box 1 lit and underlined, retyped quote on), 12.80 (both boxes), 15.30 (arc grey), 16.10 (civil defense desk grey), 16.70 and 17.40 (microphone, then house, dark), 20.40 and 21.80 (police desk grey, stop mark red, no amber on the chain).
