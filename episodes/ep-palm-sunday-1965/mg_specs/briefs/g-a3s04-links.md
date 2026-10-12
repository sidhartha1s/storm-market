Host: id=g-a3s04-links file=compositions/g-a3s04-links.html start=499.40 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=9.07 s (last sound at 8.07) track=2

# g-a3s04-links · A3-S4 · the list ran on telephone lines and electric power, and both were going down (wave 3, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a1s13-chain.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No county code and no film label belongs in this comp (rules 4 and 8). A flash or a flicker is a stroke change, never a scale pop (rule 12). Beat counts were held against the spoken window when this brief was written (rule 13): four line changes sit between 5.71 and 6.69, the closest two 0.28 s apart, each a 0.2 s stroke change.
**Spoken (A3-S4):** "A telephone list runs on telephone lines and electric power. The first tornadoes of the evening were taking both down ahead of the later ones."
**One look:** the chain, lit as far as the list; the two lines that carry South Bend's calls to the list are named, flicker, turn dotted and go dark one after the other; then the list and everything after it lose their light.

## 0. What this graphic claims
South Bend's telephone list depended on two things, telephone lines and electric power, and the evening's first tornadoes were taking both down before the later ones arrived. The break drawn here is between South Bend and the offices on its list. South Bend itself still has the message.

## 1. Source
- `edit_script.md` A3-S4, Rows [D; study printed p. 16: "knocked out numerous electric power and telephone lines"; study printed p. 25]. Its Picture note: "The solid links between South Bend and the list flicker, turn dotted, then go dark one at a time. The list and everything after it lose their light."
- The chain: design sheet section 6 "Intro version", the built `compositions/g-i1s9-chain.html`, and `mg_specs/briefs/g-a1s13-chain.md` section 3 (every station, link and label number below is that brief's).
- No page crop and no source line: the Picture note asks for none.

## 2. Datum, scale, orientation
The chain's line is y 520 and the warning travels left to right. Stations 1 to 5 stand exactly where the intro placed them. SCHEMATIC, NOT TO SCALE: who depends on what.
The Picture note's "links between South Bend and the list" are two lines here, because the narration names two things: the intro's own link at y 520 is the telephone line (it does not move), and a second line 20 px under it, y 540, is electric power. Both run x 460 to 540.
No desk is drawn (as the base).
Colours (the built intro's hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; dark line `#55606b`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient with the intro's faint sweep band, on from frame 0 |
| Station 1, teletype | `media/drawings/teletype.svg` inline, `translate(96 450)`, scale 1 (box x 96 to 236, y 450 to 590). Lit from frame 0 to the last frame: lines Headline white, paper Amber 2, bars Caption dark |
| Station 2, telephone | `media/drawings/telephone-lifted.svg` inline, `translate(316 519.6) scale(1.6)`, `stroke-width="2.5"` (box x 316 to 460, handset top y 433). Lit from frame 0 to the last frame: lines Headline white, dial Amber 2, holes Caption dark |
| Station 3, list | the miniature list sheet of `g-i1s9-chain.html`: Beige polaroid 260 x 300 at x 540 to 800, y 350 to 650, eight Caption dark sub bars 170 x 10, nine row rules. Opacity 1 at frame 0; 0.36 at the end |
| Station 4, microphone | `media/drawings/microphone.svg` inline, `translate(1170 420) scale(0.85)`, `stroke-width="4.7"` (box x 1170 to 1272, y 420 to 616). Lines Label grey at frame 0, `#55606b` at the end; lamp Panel dark always |
| Station 5, house | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, aerial to y 407). Lines Label grey at frame 0, `#55606b` at the end; windows Panel dark always |
| Station labels | Arial 700 22 px, line-height 28, Label grey, top 676, as the base: `Kansas City forecasters` (left 96, width 140), `Weather Bureau · South Bend` (left 293, width 190), `the list` (left 540, width 260), `an announcer` (left 1121, width 200), `a family` (left 1388, width 200) |
| Link 1 | y 520, x 236 to 316, 6 px, Amber 2, solid, round caps, first frame to last |
| Telephone line | y 520, x 460 to 540, 6 px, round caps. Amber 2 and solid at frame 0 |
| Power line | y 540, x 460 to 540, 6 px, round caps, Amber 2, solid; drawn on at step 3 |
| Dotted links | y 520, 4 px, `stroke-dasharray="0.1 14"`, x 800 to 1170 and x 1272 to 1400. Label grey at frame 0, `#55606b` at the end |
| Label `telephone lines` | Arial 700 22 px, Body light, centred on x 500, top 296 (box x 400 to 600); leader 2 px Label grey from (500, 330) to (500, 508) |
| Label `electric power` | same type, centred on x 500, top 744; leader 2 px Label grey from (500, 552) to (500, 738). It passes between the two station labels (x 483 and x 540) |

## 4. Must be true in the picture
1. Stations 1 and 2 and link 1 keep their light to the last frame. The break is after South Bend, never before it.
2. Two lines join South Bend to the list and each is named once. They go dotted and then dark one at a time, in the spoken order: telephone first, power second. Neither comes back.
3. The list dims only after both lines are dark; the microphone and the house go dark after the list. The order on screen is the chain's order.
4. No tornado, no town, no county, no time and no count is drawn: the picture says what the list ran on and that it was failing, nothing more.
5. Nothing is red. Red in this world means nobody was told, and this beat has not reached that.
6. Stations 1 to 5, link 1 and the two dotted links sit within 2 px of the base's numbers. No desk, no tick, no stop mark.
7. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680. No label under a line or a leader, including during the flicker.

## 5. Text (exact) and cues
Text: `Kansas City forecasters` · `Weather Bureau · South Bend` · `the list` · `an announcer` · `a family` · `telephone lines` · `electric power`.
Cue words and times are from `audio/a3-s4.words.json` (25 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S4 -0.39) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S4 | 0 | A | 0.39 | 0.00 | first frame: the chain, stations 1 and 2 lit, link 1 and the telephone line Amber 2, the list at full strength, microphone, house and dotted links Label grey. No power line, no callout label |
| 1 | A3-S4 | 2 | list | 0.92 | 0.53 | the list's eight bars turn Caption dark and back to Caption dark sub (0.3 s each way) |
| 2 | A3-S4 | 5 | telephone | 1.78 | 1.39 | the telephone line's stroke goes Headline white and back to Amber 2 (0.3 s, yoyo); its leader and the label `telephone lines` fade in (0.3 s) |
| 3 | A3-S4 | 8 | electric | 2.72 | 2.33 | the power line draws on from x 460 to x 540 (`strokeDashoffset`, 0.3 s); its leader and the label `electric power` fade in |
| 4 | A3-S4 | 12 | tornadoes | 4.76 | 4.37 | both lines flicker: `stroke-opacity` 1, 0.25, 1, 0.25, 1 in five steps of 0.08 s (a stepped tween, seek-safe) |
| 5 | A3-S4 | 17 | taking | 6.10 | 5.71 | the telephone line turns dotted (`stroke-dasharray` to `0.1 14`) and Label grey (0.2 s) |
| 6 | A3-S4 | 18 | both | 6.38 | 5.99 | the power line turns dotted and Label grey (0.2 s) |
| 7 | A3-S4 | 19 | down | 6.70 | 6.31 | the telephone line goes dark: stroke `#55606b` at `stroke-opacity` 0.5 (0.2 s); `telephone lines` and its leader go to `#55606b` |
| 8 | A3-S4 | 20 | ahead | 7.08 | 6.69 | the power line goes dark the same way; `electric power` and its leader go to `#55606b` |
| 9 | A3-S4 | 23 | later | 7.74 | 7.35 | the list dims to opacity 0.36 (0.4 s); 0.15 s later the microphone's lines and the first dotted link go to `#55606b`, 0.15 s after that the house's lines and the second dotted link (0.3 s each). Hold to 9.07 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s04-links.html` is the only file the builder writes; `data-composition-id="g-a3s04-links"`, `data-duration="9.07"`; id prefix `lnk-`; root `<div id="lnk-root" ...>` styled through `#lnk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Family base it copies:** `compositions/g-a1s13-chain.html` (wave 1), after it has passed its read: one group per station, one path per link, re-prefixed `lnk-`. It does not copy the ticks, the travelling light or the paper strip. `compositions/g-a3s15-desks.html` (third part) and `compositions/g-a6s05-wires.html` take this comp's last frame, the chain with its dark links, as their starting state.
**Assets (paths from the episode folder, read on disk 12 Oct 26):**
- `media/drawings/teletype.svg` (object 140 x 140, viewBox -6 -6 152 152, line 4; lit state as `media/drawings/teletype-lit.svg`).
- `media/drawings/telephone-lifted.svg` (viewBox -6 -58 102 106, line 3).
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4).
All inlined, ids under `lnk-`; mount rules in `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s04-links`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill; the chain band is the content and the sweep band carries the ground. Line 4 here: capture 4.55 (mid flicker) and 6.15 (one line dotted, one dark) both ways; the flicker is a stepped tween, never a `repeat` with `yoyo` that a backward seek can land inside differently. Line 5 here: the two callout labels and their leaders are read at 2.80 against the handset (top y 433), the list (left x 540) and the station labels.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): chain lit to the list, one line between South Bend and the list. Then: 0.90 (list bars back to grey ink), 1.80 (`telephone lines` and its leader), 2.80 (power line drawn, `electric power`, both labels clear), 4.55 (mid flicker), 5.85 (telephone line dotted, power solid), 6.15 (both dotted), 6.50 (telephone dark), 6.95 (both dark, list still full), 8.20 (list at 0.36, microphone, house and dotted links dark, stations 1 and 2 still lit), 9.00 (last frame).
