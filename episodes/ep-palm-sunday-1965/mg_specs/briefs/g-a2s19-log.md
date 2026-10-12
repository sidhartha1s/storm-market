Host: id=g-a2s19-log file=compositions/g-a2s19-log.html start=450.26 duration=12.55 s (timeline-map.md; wav 12.06 s plus its gaps) track=2

# g-a2s19-log · A2-S19 · three entries in twelve minutes: Plymouth, Bremen, Goshen (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3c. Map facts: `media/maps/README.md`. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No page crop holds past about 8 seconds without a visible change (rule 7). A flash is a stroke or fill change, never a scale pop (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). The 6:24 PM crop's card masks its bottom 4 px (rule 18, as ruled by the lead on 12 Oct 26). No map shows Alto; inlined map ids take this comp's prefix; the first frame read checks line weight (rule 20). The three log crops are 1460 px wide and their cards are sized from the files (rule 21).
**Spoken (A2-S19):** "South Bend kept typing as the sightings came in. In twelve minutes it reported, among others, a tornado west of Plymouth, one moving toward Bremen, and one three miles west of Goshen."
**One look:** the map of northern Indiana, a clock that steps 6:23, 6:24, 6:35, and three typed log entries stacking under it while three towns light.

## 0. What this graphic claims
Between 6:23 and 6:35 PM, twelve minutes, the South Bend office typed entries that reported, among others, a tornado west of Plymouth, one moving toward Bremen and one three miles west of Goshen. The entries are the office's own log, shown as typed.

## 1. Source
- `edit_script.md` A2-S19, Rows [A9; survey printed pp. 39-40: three of the four entries between 6:23 and 6:35] (twelve minutes is 6:23 to 6:35, confirmed by the fact check).
- The three crops (each has its `provenance.csv` row with its page box): `media/docs/survey-p39-623pm-crop.png` (printed p. 39: the 6:23 PM entry's time line and first line), `media/docs/survey-p40-624pm-crop.png` (printed p. 40: the 6:24 PM entry's time line and the 2 lines naming Bremen), `media/docs/survey-p40-635pm-crop.png` (printed p. 40: the 6:35 PM entry's time line and the 2 lines naming Goshen).
- Town positions: `media/maps/README.md` points table (US Census gazetteer). County outlines: `media/maps/indiana-counties.svg`.

## 2. Datum, scale, orientation
North is up. Map family state NORTH: BM-1 inlined in one SVG mounted at left 716, top 62, width 1080, height 450 with `viewBox="296 166 360 150"` (3.0 px per map unit; screen x = 3u - 172, screen y = 3u - 436). The camera does not move.
Cards: each crop at scale 1.0, its own 1460 px width, so the three stack in the lower band. Ink rows measured on the files (row projection, by script): the typed lines are 24 to 36 px tall at this scale, above the 19 px floor. Stack: 20 px of Beige polaroid border per card, 14 px between cards.
Clock angles, clockwise from 12 (by script): 6:23 is hour 191.5, minute 138; 6:24 is hour 192.0, minute 144; 6:35 is hour 197.5, minute 210.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `log-`; county lines 1.5 px, Indiana's outline 3 px (the file's `vector-effect="non-scaling-stroke"`). Every `pt-` group hidden except the four below. No county is filled |
| Town dots (screen, from the points table) | South Bend (1214.6, 129.5), Plymouth (1195.1, 311.3), Bremen (1259.6, 255.8), Goshen (1381.7, 186.5); each circle `r` 2 map units (6 px), fill Body light |
| Town labels, Arial 700 22 px, line-height 26 | `South Bend` Body light, left 1231, top 117. `Plymouth` right aligned to x 1179, top 298. `Bremen` left 1276, top 243. `Goshen` left 1398, top 174. The three sighting towns start hidden |
| Lit town | the dot's fill turns Amber 2 and a ring comes on around it (radius 14 px, 3 px Amber 2 at 0.45); its label is Headline white |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; eyebrow `WEATHER BUREAU`; place `South Bend, Indiana`; three pre-authored time lines toggled with `autoAlpha`: `6:23 PM`, `6:24 PM`, `6:35 PM` |
| Span chip | glass chip, left 96, top 316, height 46, padding 0 x 22, Arial 700 26 px, Body light: `12 minutes` |
| Card 1 (6:23) | Beige polaroid border 10 px, left 96, top 560, 1480 x 110 (bottom 670); crop `survey-p39-623pm-crop.png` 1460 x 90 inside at (106, 570) |
| Card 2 (6:24) | left 96, top 684, 1480 x 145 (bottom 829); crop `survey-p40-624pm-crop.png` at (106, 694) inside a window 1460 x 125 with `overflow:hidden`: the file's bottom 4 px (rows 125 to 128) are not shown |
| Card 3 (6:35) | left 96, top 843, 1480 x 148 (bottom 991); crop `survey-p40-635pm-crop.png` 1460 x 128 inside at (106, 853) |
| Card shadow | `0 18px 50px rgba(0,0,0,0.55)` (design sheet section 9) |
| Source line | not in the credit corner (the stack ends at y 983): left 96, top 376, Arial 700 22 px with the credit shadow: `Weather Bureau survey report, 1965, pp. 39-40` |

## 4. Must be true in the picture
1. Each card is the scan itself at its own size: nothing retyped, nothing cropped inside a line, except card 2's ruled 12 px mask.
2. The cards land in time order, 6:23, 6:24, 6:35, and the stamp's time matches the card that has just landed.
3. Each town's dot sits on its position from the points table within 2 px, and lights on its own spoken name: Plymouth, then Bremen, then Goshen. No other town lights. Donaldson, Nappanee and Elkhart are hidden.
4. No county is filled amber (in this family an amber county is a warned county) and no tornado mark is drawn: the entries report sightings, the picture places only the towns they name.
5. `12 minutes` is the span from the first card's time to the third's. No count of entries is printed ("among others").
6. Every card's right edge is x 1576 and the stack ends at y 983: nothing of ours in x >= 1600, y >= 680. Nothing appears before its spoken word.
7. Read the bottom edge of card 2 in a frame. Measured on the file: the next line's sliver is rows 126 to 128; the third typed line's own ink runs to row 123, so the ruled 12 px mask also trims rows 117 to 123 (descenders). If a letter reads as cut, report it; do not change the mask.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `6:23 PM` · `6:24 PM` · `6:35 PM` · `South Bend, Indiana` · `12 minutes` · `South Bend` · `Plymouth` · `Bremen` · `Goshen` · `Weather Bureau survey report, 1965, pp. 39-40`. The cards' words are the images.
Cue words and times are from `audio/a2-s19.words.json` as re-transcribed on 12 Oct 26 (17:45 to 17:50). t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S19 -0.23) plus the word's time; the first word uses the table's "first sound". Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S19 | 0 | South | 0.23 | 0.00 | first frame: ground, the county map, the South Bend dot and its label |
| 1 | A2-S19 | 3 | typing | 1.08 | 0.85 | clock stamp slides in from the left (0.6 s, power3.out) reading `6:23 PM`, hands 191.5 and 138; source line fades in |
| 2 | A2-S19 | 10 | 12 | 3.72 | 3.49 | chip `12 minutes` lands (0.3 s, `y:16` to 0 with the fade) |
| 3 | A2-S19 | 17 | tornado | 6.34 | 6.11 | card 1 rises into place (`y:60` to 0 with the fade, 0.4 s, power3.out) |
| 4 | A2-S19 | 20 | Plymouth, | 7.24 | 7.01 | Plymouth lights: dot Amber 2, ring on, label in (0.3 s) |
| 5 | A2-S19 | 21 | one | 8.12 | 7.89 | card 2 rises into place; the stamp's time cuts to `6:24 PM` and the hands step to 192.0 and 144 (0.2 s) |
| 6 | A2-S19 | 24 | Bremen | 8.90 | 8.67 | Bremen lights |
| 7 | A2-S19 | 26 | one | 9.90 | 9.67 | card 3 rises into place; the stamp's time cuts to `6:35 PM` and the minute hand sweeps to 210, the hour hand to 197.5 (0.5 s, power3.out) |
| 8 | A2-S19 | 31 | Goshen. | 11.32 | 11.09 | Goshen lights. Hold to 12.55 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s19-log.html` is the only file the builder writes; `data-composition-id="g-a2s19-log"`; id prefix `log-`; root `<div id="log-root" ...>` styled through `#log-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (wave 1; brief `mg_specs/briefs/g-a2s14-six.md`) for the way BM-1 is inlined, prefixed and mounted in state NORTH, and for the paper card in the lower band; the clock stamp of the built `compositions/g-t1s2-warning.html`.
**Assets (paths from the episode folder):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880), inlined.
- `media/docs/survey-p39-623pm-crop.png` (1460 x 90), `media/docs/survey-p40-624pm-crop.png` (1460 x 129, shown 1460 x 117), `media/docs/survey-p40-635pm-crop.png` (1460 x 128): each an `<img>` at its own size.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s19-log`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the four dot positions (from `media/data/points.csv` by the section 2 formula), the six hand angles and the three card boxes are computed by a script and stated in the receipt. `graphics_qc` flat-type on a comp of typed page crops is the accepted by-design case (plan rule 10): report it, do not restyle the scans.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map, South Bend dot and label, line weights as section 3. Then settled frames: 1.70 (stamp at 6:23 PM), 4.00 (chip), 6.70 (card 1), 7.50 (Plymouth lit), 8.50 (card 2, stamp 6:24 PM, bottom edge of card 2 read), 9.20 (Bremen lit), 10.40 (card 3, stamp 6:35 PM), 11.60 and 12.50 (Goshen lit, three cards, three towns).
