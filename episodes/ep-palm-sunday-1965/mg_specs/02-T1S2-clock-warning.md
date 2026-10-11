# 02 · T1-S2 · 5:43 PM, the warning, the telephone (comp `g-t1s2-warning`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 7, 8, 9, 10.
**Spoken (T1-S2):** "At five forty three, the Weather Bureau in South Bend issued a tornado warning. It telephoned its warnings down a list."
**One look:** a clock at 5:43, the typed warning itself, then a telephone picked up.

## 0. What this graphic claims
At 5:43 PM the Weather Bureau in South Bend issued a warning whose first line reads "Severe thunderstorm and tornado warning." Separately, and not tied to 5:43, South Bend telephoned its warnings to a list of offices.

## 1. Source
- `edit_script.md` T1-S2, Rows [A6; survey printed p. 39] and [A6; study printed p. 14: South Bend "also telephoned several organizations", said of its warnings in general].
- Page image: `media/stills/b1-south-bend-warning-page-orig.png` (2550 x 3300, inventory row B1, opened 12 Oct 26). The page is headed `SOUTH BEND (Continued)`. Its first entry reads, line by line: `Issued at 5:43 PM EST.` / `Severe thunderstorm and tornado warning.` / `Radio and television stations are requested to use emergency frequencies.` / then the radar lines, which name Michigan City, Knox and the counties of LaPorte, Starke and Marshall.
- So the Picture note's "first line" is the entry's second line; the line above it is the page's own time stamp, which is kept lit beside the clock.
- Ground: `media/stills/a3-teletype-operators.jpg` (1370 x 1080, inventory row A3). It shows the Weather Bureau Communications Center about 1955, two operators from behind: not South Bend, not 1965.

## 2. Datum, scale, orientation
Crop (page px of the 2550 x 3300 file, read on the 835 px copy and multiplied by 3.054; the builder confirms each edge within 10 px on the file): x 290 to 1350, y 263 to 476. It holds three lines and no more: the heading `SOUTH BEND (Continued)`, `Issued at 5:43 PM EST.`, `Severe thunderstorm and tornado warning.` The crop is cut once to `media/stills/b1-warning-crop.png` (1060 x 213) and that file is what the comp mounts.
Scale on screen = 1460 / 1060 = 1.377. Line pitch on the page is about 47 px, so about 65 px on screen: large enough to read without a quote strip.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | A3 `<img>` cover, `object-position:50% 40%`, scale 1.00 to 1.06 over the window, `.dim` scrim (`rgba(3,5,8,0.45)`) |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `5:43 PM` / `South Bend, Indiana`; hands 171.5 and 258 degrees |
| Document card | left 96, top 340, 1480 x 314 (right 1576, bottom 654); Beige polaroid border 10 px; inner 1460 x 294 |
| Underline | Crimson 6 px under `Severe thunderstorm and tornado warning.` only (the crop's last line) |
| Unlit page | covers the heading `SOUTH BEND (Continued)` at 45 %; `Issued at 5:43 PM EST.` and the underlined line stay bright |
| Quote strip | not used: the line is about 65 px tall on screen |
| Photo caption | credit corner, left 96, bottom 60: `Weather Bureau Communications Center, about 1955 · NOAA` |
| Document source | on the card's lower border, right aligned at x 1560, y 668 to 690: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965` |
| Telephone | drawn telephone (design sheet section 7) at 4.0 scale, box x 760 to 1120, y 420 to 596, lines Body light 4 px on screen (stroke set after scaling, `vector-effect:non-scaling-stroke`), body fill Panel dark; two ring arcs each side, radius 40 and 64 from the handset ends |

## 4. Must be true in the picture
1. The clock reads 5:43 PM, hour hand between 5 and 6, minute hand between 8 and 9.
2. The underlined words are the page's own line `Severe thunderstorm and tornado warning.` Nothing on the card is retyped.
3. "South Bend, Indiana" is on the glass stamp, never bare on the photograph; the photograph's own caption says what it is (S8).
4. **The telephone is not at 5:43.** The clock stamp has left the frame before the telephone is fully drawn. No time is on screen with the telephone.
5. The crop ends under `Severe thunderstorm and tornado warning.` The lines that name Michigan City, Knox, LaPorte, Starke and Marshall are outside the crop and never on screen (S1). The page's `5:43 PM EST` and the stamp's `5:43 PM` agree; the stamp does not print "EST".
6. No list row, no count of offices and no office name appears in this comp. The list belongs to comp 03.
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `5:43 PM` · `South Bend, Indiana` · `Weather Bureau survey report, 1965` · `Weather Bureau Communications Center, about 1955 · NOAA`. Page words are the image.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (hard cut from 01, word "At") | | ground on, photo caption on |
| 1 | cue: "5:43" (whisper writes the digits; the spoken words are "five forty three") | | clock stamp slides in; minute hand sweeps its last 30 degrees; time lands on the word |
| 2 | cue: "South" | | place line `South Bend, Indiana` rises inside the stamp (`y:16 to 0`, 0.3 s) |
| 3 | cue: "issued" | | document card slides in from the right (`x:660 to 0`, 0.7, power3.out) |
| 4 | cue: "tornado" (first sentence) | | unlit page fades in over the heading, underline draws under `Severe thunderstorm and tornado warning.` (0.6 s) |
| 5 | cue: "It" (second sentence; the ring sound starts here) | | clock stamp exits left; document card exits right (`x:1900`, 0.6, power3.in) |
| 6 | cue: "telephoned" | | telephone draws on (0.6 s); handset lifts 26 px and turns -20 degrees (0.35 s, back.out); ring arcs pulse twice (0.4 s each, finite) |
| 7 | cue: "down" | | telephone slides left out of frame (`x:-1100`, 0.5, power3.in) |
| 8 | cue: "list" | | comp ends on this word; comp 03 starts on the same frame (match cut on the ground, scale 1.06) |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-t1s2-warning.html`, id prefix `warn-`, root id `warn-root`. Done line 6: the ground's end scale (1.06) is the shared number with comp 03.
**Closest library exemplar:** El Reno `compositions/g-a4s13-clock.html` (clock face, time, a card that follows it) for steps 1 to 4; El Reno `compositions/g-a4s11-page.html` for the page crop and lit line. In-house: `library/inhouse/bulletin-typewriter.html` is the fallback if the survey page never arrives (the warning's first line typed as an attributed bulletin, source line unchanged).
