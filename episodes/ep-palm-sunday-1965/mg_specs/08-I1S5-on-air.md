Host: id=g-i1s5-onair file=compositions/g-i1s5-onair.html start=77.02 duration=4.64 track=2

# 08 · I1-S5 · the stations' row and the ON AIR lamp (comp `g-i1s5-onair`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 5. Built as a copy of comp 03's sheet (`g-t1s3-list`): same world, Close state, never the Everything state. Revised 12 Oct 26 to the fact-checked line.
**Spoken (I1-S5):** "The stations on that list were the ones expected to pass the warning to the public."
**One look:** the same typed list; one row, the radio and TV stations, lights up, and an ON AIR lamp beside it.

## 0. What this graphic claims
Of the organizations on the list, the radio and television stations were the ones expected to pass the warning to the public.

## 1. Source
`edit_script.md` I1-S5, Rows [A6; study printed p. 9: interviewees "said it was the responsibility of radio and TV stations to pass on such information"]. The page for p. 9 is not in `media/docs/` and is not shown.
Ground: `media/stills/a3-teletype-operators.jpg` (1370 x 1080, inventory row A3).

## 2. Datum, scale, orientation
Design sheet section 5, Close state: s 1.6, tx 147.6, ty -66. The stations' row (slot 6) centre on screen: y 660.4.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | A3 `<img>`, `object-position:50% 40%`, scale 1.00 to 1.05, `.dim-heavy` scrim from frame 0 |
| Sheet | x 250 to 1466, y 30 to 974; eight rows in the Plain state (all Caption dark); **no tick and no tick box anywhere**; the blank ninth row with its rule, cursor not blinking in this comp |
| Lit band | behind the stations' row: x 290 to 1430, y 625 to 696, Amber 2 at 35 % |
| ON AIR lamp | world box x 660 to 790, y 436 to 472; on screen x 1203.6 to 1411.6, y 631.6 to 689.2; rounded rect radius 6 world px; `ON AIR` Arial Black 900, 18 world px (28.8 on screen), centred |
| Source line | left 96, bottom 60: `Disaster Research Center, 1966, p. 14` |
The lamp ends at x 1411.6: clear of the corner.

## 4. Must be true in the picture
1. Only the row `Specified radio and TV stations` lights. No other row changes in any frame ("nothing else on the list moves").
2. No tick, tick box, number or arrow is on the sheet (S2).
3. The lamp is on the paper, on that row's own line. It carries the words `ON AIR` and no station name, call letters or frequency (S4).
4. **The lamp says "expected to", not "did".** Rest state is an outline: 3 px Popfig red line, Popfig red letters, no fill. It fills Popfig red with Headline white letters once, for 0.5 s, on the word "public", then returns to the outline. The last frame shows the outline.
5. No microphone, house or dotted line in this comp.
6. The sheet's title is "Organizations notified included:".
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: the sheet's text as design sheet section 5 · `ON AIR` · the source line.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "The") | 0.00 | ground and sheet on, in the Close state |
| 1 | cue: "stations" | 0.07 | lit band wipes across the row (`scaleX` 0 to 1, 0.5 s, left origin) |
| 2 | cue: "expected" | 1.55 | lamp outline draws on (0.4 s) |
| 3 | cue: "public" (last word) | 3.21 | lamp fills for 0.5 s, then back to the outline (0.3 s) |
| 4 | hold | 3.64 | 1.0 s; the lit band breathes between 30 % and 38 % (finite repeats) and the ground pushes |
| 5 | exit | 4.64 | sheet slides down out of frame (`y:1100`, 0.6, power3.in) into the hard cut to 09 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s5-onair.html`, id prefix `air-`, root id `air-root`. Built only after comp 03's base has had its full-size read.
**Closest library exemplar:** this episode's `compositions/g-t1s3-list.html` (the base); for the lit row, the official catalog block `inline-highlight` (a marker band scaled in behind text).
