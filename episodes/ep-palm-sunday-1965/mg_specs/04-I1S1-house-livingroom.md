Host: id=g-i1s1-house file=compositions/g-i1s1-house.html start=37.60 duration=9.98 track=2

# 04 · I1-S1 · the house in the sun, the living room, both sets idle (comp `g-i1s1-house`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 2, 3, 7. Revised 12 Oct 26 to the fact-checked line.
**Spoken (I1-S1):** "April eleventh, nineteen sixty five, was the first nice spring day of the year. Many people were not listening to the radio or watching television."
**One look:** the same house, now in sunshine; through its window, a radio and a television with nobody at them and an empty chair.

## 0. What this graphic claims
April 11, 1965 was the first nice spring day of the year, and many people were not listening to the radio or watching television. The house is the family's house from the end of the list.

## 1. Source
`edit_script.md` I1-S1, Rows [C21; study printed p. 25] · [C21; study printed p. 25]. The p. 25 scan (`media/docs/study-pdf-27-orig.png`) is the fact's source and is not shown. No photograph: the inventory holds no picture of a home or a street that day, so this is a drawing (design sheet section 7). Needs no file from `media/stills/`.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE. Front elevation only. Ground line y 850 is the datum of the street view; floor line y 820 is the datum of the room. House at 2.2 scale; television at 1.5 scale.

## 3. Geometry (screen px)
Street view:
| Element | Px |
|---|---|
| Ground | canvas gradient, plus a sky wash: Amber 2 at 12 % at y 0 falling to 0 % at y 620 |
| Sun | disc radius 58, centre (330, 300), Amber 2 at 85 %, no rays |
| House | box x 674 to 1246, y 300 to 850 (design sheet house x 2.2); aerial top at y 225; lines Headline white, window fill Amber 2 at 30 % |
| Street line | y 850, x 96 to 1560, 4 px Body light |
| Title | `Palm Sunday` left 96, top 64, Arial Black 900 52 px, Headline white; `April 11, 1965` left 98, top 132, Georgia italic 26 px, Amber 2 |
| Left front window (the push target) | x 770.8 to 876.4, y 564 to 669.6; centre (823.6, 616.8) |
Room view: the design sheet "Living room" row as written (window x 180 to 520, y 220 to 600; armchair x 420 to 640, y 600 to 820; television x 760 to 1210, y 460 to 820; side table x 1260 to 1500, y 700 to 820; radio x 1290 to 1470, y 592 to 700; floor line y 820).
| Sun patch on the floor | parallelogram (560,820) (700,820) (640,900) (500,900), Amber 2 at 18 %, drifts `x` 0 to 40 px over the room hold |
Nothing in x >= 1600.

## 4. Must be true in the picture
1. The house is the hook's house: same roof, door, two windows, chimney and aerial, redrawn from the same numbers.
2. Sunshine reads at a glance: sun disc, sky wash, bright lines. No cloud, no rain, no funnel, no dark sky.
3. **The sets are idle, with no one at them.** The television screen is in the Idle state and the radio dial is unlit; the armchair is empty. Nothing says the sets were switched off: no switch, no plug pulled, no "OFF". No amber on either set, in any frame.
4. No person, no pet, no car, no street name, no house number, no town or county name (S1, S5).
5. The date reads `Palm Sunday` and `April 11, 1965`.
6. The title is gone before the camera moves (no text rides the push).
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `Palm Sunday` · `April 11, 1965`. No other text.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (hard cut from 03, word "April") | 0.00 | house, street line and sky wash on, already lit; sun at y 340 |
| 1 | cue: "April" | 0.00 | title `Palm Sunday` (`x:-60 to 0`, 0.4), then `April 11, 1965` 0.2 s later |
| 2 | cue: "nice" | 3.30 | sun rises `y:340 to 300` (1.2 s, power2.out); window fills step from 20 % to 30 % |
| 3 | cue: "year" | 4.38 | title slides out left (`x:-980`, 0.5, power3.in) |
| 4 | cue: "Many" | 5.60 | camera pushes into the left front window with `logZoom`, scale 1 to 9 about (823.6, 616.8), 1.1 s; at scale 9 the window's amber fills the frame and the room view is switched on beneath it (hard switch at full amber, then the amber clears in 0.3 s). The empty armchair is in the room from its first frame |
| 5 | cue: "radio" | 7.08 | radio outline flashes Headline white once (0.4 s) and settles to Body light; dial stays dark |
| 6 | cue: "television" (last word) | 8.24 | television outline flashes once the same way; screen stays Idle; hold 1.0 s; the sun patch drift carries it |
| 7 | exit | 9.98 | hard cut to 05 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s1-house.html`, id prefix `house-`, root id `house-root`.
**Closest library exemplar:** El Reno `compositions/g-a1s2-house.html` and `g-a5s8-closet.html` (a house and a room as flat line drawings with a camera move into them); `library/inhouse/snippets/helpers.js` `logZoom` for step 4.
