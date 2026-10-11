# 12 · I1-S10 · the list once more: were police the only ones? (comp `g-i1s10-list`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 5. A copy of comp 03's sheet (`g-t1s3-list`): same world, Close state.
**Spoken (I1-S10):** "Were police the only ones who told nobody?"
**One look:** the typed list again. One row, city police, is marked in red. A question passes over every other row, one at a time, and leaves no mark.

## 0. What this graphic claims
In one Indiana county, city police heard and told nobody (comp 09). Whether any other office on the list did the same is an open question; nothing is shown as answered.

## 1. Source
`edit_script.md` I1-S10 (the question; no row) and I1-S6 Rows [C2] for the mark on row 3. Ground: `media/stills/a3-teletype-operators.jpg` (1370 x 1080, inventory row A3).

## 2. Datum, scale, orientation
Design sheet section 5, Close state: s 1.6, tx 147.6, ty -66. Row centres on screen: 276.4, 353.2, 430.0, 506.8, 583.6, 660.4, 737.2, 814.0, 890.8. Row 3 is at y 430.0.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | A3 `<img>`, `object-position:50% 40%`, scale 1.00 to 1.05, `.dim-heavy` scrim |
| Sheet | x 250 to 1466, y 30 to 974; eight rows typed; ticks on rows 1, 2, 3, 6; row 9 blank with its cursor blinking |
| Mark on row 3 | Crimson line 5 world px (8 on screen) under `City Police Departments`, world x 150 to 509, y 326 (16 world px under row 3's centre at 310); Crimson ring round row 3's tick box, 3 world px |
| Mark's tag | on the paper, world x 530, baseline of row 3: `in one Indiana county` Arial 700, 14 world px (22.4 on screen), Crimson; on screen it starts at x 995.6 |
| Pulse band | Amber 2 at 25 %, the row's full width (screen x 290 to 1430, 70 px tall), wipes left to right in 0.3 s and fades in 0.2 s |
| Source line | left 96, bottom 60: `Disaster Research Center, 1966 · list of offices the Weather Bureau telephoned` |

## 4. Must be true in the picture
1. Row 3 is marked from the first frame, and carries the tag `in one Indiana county`: the mark is about one county's police, not every city police department on the list (S1).
2. The pulse touches rows 1, 2, 4, 5, 6, 7, 8, one at a time, top to bottom, and never row 3 or row 9.
3. After the last pulse no row other than row 3 carries any mark, tint or red. A pulse is a question, not a finding.
4. The four ticks are rows 1, 2, 3 and 6, as in the hook. Row 3 keeps its tick: it was telephoned.
5. Row 9 stays blank with its cursor.
6. No microphone, house or lamp in this comp. No question mark glyph: the voice asks.
7. The sheet's wording stays inside S2.
8. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: the sheet's text as design sheet section 5 · `in one Indiana county` · the source line.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "Were") | | ground and sheet on in the Close state; row 3 marked and tagged; cursor blinking |
| 1 | cue: "police" | | row 3's mark thickens once (`scaleY` 1 to 1.6 to 1, 0.3 s) |
| 2 | cue: "only" | | pulses start: rows 1, 2, 4, 5, 6, 7, 8, one every 0.3 s |
| 3 | cue: "nobody" (last word) | | the last pulse has cleared by the end of this word; hold 1.0 s on the sheet; the bed drops out here (sound, orchestrator) |
| 4 | exit | | hard cut to the 0.7 s blackout the script places after I1-S10. No fade |
If the voice gives fewer than 2.1 s between "only" and the end of "nobody", the pulses run every 0.22 s; the order does not change.

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s10-list.html`, id prefix `lq-`, root id `lq-root`. Built only after comp 03's base has had its full-size read.
**Closest library exemplar:** this episode's `compositions/g-t1s3-list.html` (the base); official catalog blocks `inline-highlight` (the pulse band) and `hw-underline` (a drawn underline, for the red mark's shape only, without its jitter).
