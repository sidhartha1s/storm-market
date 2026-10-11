# 07 · I1-S4 · six states, then 11:45 AM in Kansas City (comp `g-i1s4-states`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 8, 10.
**Spoken (I1-S4):** "Tornadoes crossed six states that day. By eleven forty five that morning, forecasters in Kansas City had a tornado forecast out on the teletype."
**One look:** the day's track map with six state names lighting up; then a clock at 11:45 AM and paper coming off a teletype.

## 0. What this graphic claims
Tornadoes crossed six states on April 11, 1965: Iowa, Illinois, Wisconsin, Indiana, Michigan, Ohio. By 11:45 AM, forecasters in Kansas City had a tornado forecast out on the teletype.

## 1. Source
`edit_script.md` I1-S4, Rows [IWX page, six states confirmed by the checker 11 Oct 26] · [A1].
- Part A ground: `media/stills/b7-tornado-track-map.jpg` (1396 x 1046, inventory row B7, "Courtesy: Dr. Russell Schneider, SPC"; opened 12 Oct 26). White ground, grey county and state lines, red track lines with small rating numbers, Lake Michigan top centre. **It prints no state name**, so the six names are ours, set on it.
- Part B ground: `media/stills/a4-teletype-room.jpg` (1456 x 1080, inventory row A4; opened 12 Oct 26). A wide Weather Bureau teletype room about 1955: a row of machines, three people whose faces show, a wall clock right of centre. Not Kansas City, not 1965.
- No picture of the Kansas City forecast room is free (row A7 is Ask): none is used and none is drawn.

## 2. Datum, scale, orientation
The map is shown whole, north up, at one scale: 972 / 1046 = 0.9293, fitted into x 251 to 1549, y 54 to 1026 (centred on x 900, right edge clear of the corner). Screen x = 251.4 + 0.9293 x image x; screen y = 54 + 0.9293 x image y.
State chip centres (image px read by eye on the file, then the screen px they give; the builder moves a chip only to clear a red track, and keeps it inside its state):
| State | Image px | Screen px |
|---|---|---|
| Iowa | (80, 270) | (326, 305) |
| Illinois | (330, 560) | (558, 574) |
| Wisconsin | (320, 110) | (549, 156) |
| Indiana | (590, 660) | (800, 667) |
| Michigan | (880, 200) | (1069, 240) |
| Ohio | (900, 650) | (1088, 658) |
Only the east edge of Iowa is on this map (left of the river line near image x 160 to 230): its chip sits there and nowhere else.

## 3. Geometry (screen px)
Part A:
| Element | Px |
|---|---|
| Ground | canvas gradient; map on a Beige polaroid border 10 px, shadow as the document card |
| State chips | Beige polaroid chip with a 2 px Caption dark edge (the map is white), padding 8 x 18, Arial Black 900 30 px, Caption dark; one per state at its centre from section 2; a 3 px Crimson-free ring in Amber 2 (radius 30 to 70, one pulse) behind each as it lands. No chip covers a red track |
| Count | in the left margin, clear of the map (which starts at x 251): `6` Courier New 700 84 px Amber 2 at left 96, top 96; `states` Arial 700 26 px Body light at left 96, top 192 |
| Map credit | credit corner: `Courtesy: Dr. Russell Schneider, SPC` |
Part B:
| Element | Px |
|---|---|
| Ground | A4 `<img>` cover, scale 1.00 to 1.05, `.dim` scrim |
| Clock stamp | design sheet section 8: `FORECASTERS` / `11:45 AM` / `Kansas City`; hands 352.5 and 270 degrees |
| Paper strip | Beige polaroid, x 900 to 1420, rising from y 1080 to y 440 at 60 px/s, never stopping inside the window; typed lines are Caption dark sub bars 16 px tall, widths 300 to 440 px, every 44 px; no readable word |
| Label | glass card left 880, top 250, 640 x 150 (right 1520, bottom 400): `Tornado forecast` Arial Black 900 52 px Headline white at top 276; `out on the teletype` Georgia italic 26 px Amber 2 at top 350. Placed here so its blur sits over the photograph's wall clock (screen about 1174, 356) |
| Faces | the three faces in A4 fall near screen (158, 620), (30, 520) and (1870, 630) at cover: no card, stamp or strip is over them |
| Photo caption | credit corner: `Weather Bureau teletypewriters, about 1955 · NOAA` |
The strip's right edge is x 1420, clear of the corner.

## 4. Must be true in the picture
1. Exactly six names light, in the spoken order: Iowa, Illinois, Wisconsin, Indiana, Michigan, Ohio. No seventh state is labelled by us.
2. Each chip sits inside its own state on the map.
3. The count `6` is on screen only once the word "six" is spoken; the sixth chip lands before the word "day" ends.
4. The clock reads 11:45 AM: AM, hour hand just short of 12, minute hand on 9.
5. `Kansas City` is on the glass stamp, never bare on the photograph; the photograph's caption says what it is (S8).
6. The paper strip carries bars, not words: the forecast's text is not in the script, so none is typed.
7. The map keeps its courtesy credit for as long as it is on screen.
8. No Indiana county is singled out on the map by us (S1).
9. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: the six state names · `6` · `states` · `Courtesy: Dr. Russell Schneider, SPC` · `FORECASTERS` · `11:45 AM` · `Kansas City` · `Tornado forecast` · `out on the teletype` · `Weather Bureau teletypewriters, about 1955 · NOAA`.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "Tornadoes") | | map on, credit on; map pushes scale 1.00 to 1.03 |
| 1 | cue: "six" (whisper may write "6") | | count `6` lands; chips land one every 0.22 s in the order of truth 1, each with its ring |
| 2 | cue: "day" | | all six on; hold to the end of the sentence |
| 3 | cue: "By" | | hard cut to Part B: A4 ground and its caption |
| 4 | cue: "11:45" (spoken "eleven forty five") | | clock stamp slides in, minute hand sweeps into place |
| 5 | cue: "Kansas" | | place line `Kansas City` rises inside the stamp |
| 6 | cue: "forecast" (second, "tornado forecast") | | paper strip starts to rise; label card slides in (`x:-660 to 0`, 0.6, power3.out) |
| 7 | cue: "teletype" (last word) | | hold 1.0 s; the strip keeps rising |
| 8 | exit | | stamp and label slide out left (`x:-980`, 0.6, power3.in) into the hard cut to 08 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s4-states.html`, id prefix `st6-`, root id `st6-root`. Done line 7: the map label names six places, each a claim about the map under it.
**Closest library exemplar:** El Reno `compositions/g-i1s3-pins.html` (labels landing one by one on a map) for Part A; El Reno `compositions/g-a4s13-clock.html` for the stamp; `library/inhouse/bulletin-typewriter.html` for the feel of paper feeding (the motion only, not its green screen).
