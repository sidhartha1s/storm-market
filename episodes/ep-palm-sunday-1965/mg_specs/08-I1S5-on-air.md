# 08 · I1-S5 · the stations' row and the ON AIR lamp (comp `g-i1s5-onair`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 5. Built as a copy of comp 03's sheet (`g-t1s3-list`): same world, Close state, never the Everything state.
**Spoken (I1-S5):** "The stations on that list were supposed to put the warning on the air."
**One look:** the same typed list; one row, the radio and TV stations, lights up, and an ON AIR lamp beside it.

## 0. What this graphic claims
The radio and television stations on South Bend's list were the ones meant to broadcast the warning. Only that row carries it to the public.

## 1. Source
`edit_script.md` I1-S5, Rows [A6]. The spoken line is under a fact check (what "use emergency frequencies" asked of the stations) and may change by a few words; the picture does not. Ground: teletype room photograph, **waits for inventory row A3**.

## 2. Datum, scale, orientation
Design sheet section 5, Close state: s 1.6, tx 147.6, ty -66. Row 6 centre on screen: y 660.4.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | A3 `<img>`, `object-position:50% 40%`, scale 1.00 to 1.05, `.dim-heavy` scrim from frame 0 |
| Sheet | x 250 to 1466, y 30 to 974; eight rows typed; rows 1, 2, 3, 6 ticked as the hook left them; row 9 with its tick box and rule, cursor not blinking in this comp |
| Lit band | behind row 6: x 290 to 1430, y 625 to 696, Amber 2 at 35 % |
| ON AIR lamp | world box x 660 to 790, y 436 to 472; on screen x 1203.6 to 1411.6, y 631.6 to 689.2; rounded rect radius 6 world px; `ON AIR` Arial Black 900, 18 world px (28.8 on screen), centred |
| Source line | left 96, bottom 60: `Disaster Research Center, 1966 · list of offices the Weather Bureau telephoned` |
The lamp ends at x 1411.6: clear of the corner.

## 4. Must be true in the picture
1. Only row 6 (`Specified radio and TV stations`) lights. No other row changes in any frame.
2. The lamp is on the paper, on row 6's own line. It carries the words `ON AIR` and no station name, call letters or frequency (S4).
3. **The lamp says "meant to", not "did".** Rest state is an outline: 3 px Crimson line, Crimson letters, no fill. It fills Crimson with Headline white letters once, for 0.5 s, on the word "air", then returns to the outline. The last frame shows the outline.
4. The four ticks are rows 1, 2, 3 and 6; no tick is added or removed.
5. No microphone, house or dotted line in this comp.
6. The sheet's wording stays inside S2.
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: the sheet's text as design sheet section 5 · `ON AIR` · the source line.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "The") | | ground and sheet on, in the Close state, ticks as listed |
| 1 | cue: "stations" | | lit band wipes across row 6 (`scaleX` 0 to 1, 0.5 s, left origin) |
| 2 | cue: "supposed" | | lamp outline draws on (0.4 s) |
| 3 | cue: "air" (last word) | | lamp fills for 0.5 s, then back to the outline (0.3 s) |
| 4 | hold | | 1.0 s; the lit band breathes between 30 % and 38 % (finite repeats) and the ground pushes |
| 5 | exit | | sheet slides down out of frame (`y:1100`, 0.6, power3.in) into the hard cut to 09 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s5-onair.html`, id prefix `air-`, root id `air-root`. Built only after comp 03's base has had its full-size read.
**Closest library exemplar:** this episode's `compositions/g-t1s3-list.html` (the base); for the lit row, the official catalog block `inline-highlight` (a marker band scaled in behind text).
