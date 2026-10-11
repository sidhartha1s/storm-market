Host: id=g-i1s3-cloud file=compositions/g-i1s3-cloud.html start=58.21 duration=8.74 track=2

# 06 · I1-S3 · back to the show, a clear sky, and the study's sentence (comp `g-i1s3-cloud`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 7, 9. Revised 12 Oct 26 to the fact-checked line and the page scan.
**Spoken (I1-S3):** "TV stations cut in with a warning, then went back to their shows. Some people looked outside, and there was not a cloud in the sky."
**One look:** the station's card flips back to the ordinary picture; then a plain clear sky, and on it the study's own page with one sentence underlined: "There was not a cloud in the sky."

## 0. What this graphic claims
TV stations interrupted with a warning and then resumed their programmes. The 1966 study writes, in its own voice: "There was not a cloud in the sky." It is the study's sentence, not a quoted person.

## 1. Source
`edit_script.md` I1-S3, Rows [C22; study printed p. 36] · [C22; study printed p. 36].
Page image: `media/docs/study-pdf-38-orig.png` (2656 x 3370, printed page number 36, read by eye 12 Oct 26). The five lines the crop holds read:
"clues. TV stations interrupted usual programming to issue warnings, but then / resumed their normal schedules. This tended to discount the possible serious- / ness of the situation. Other individuals looked outside for adverse weather / conditions which create tornadoes, but found none. There was not a cloud in / the sky. Not finding additional clues, most people continued their daily routine"
So the same crop also carries the page's words for the first spoken sentence.

## 2. Datum, scale, orientation
Crop box, page px: x 360 to 2440, y 2355 to 2895 (2080 x 540), saved as `media/docs/study-p36-cloud-crop.png` at 1460 x 379 (scale 0.7019). Line pitch on the card is about 80 px.
| Line box | Page px (x0 to x1, y0 to y1) | Px inside the 1460 crop |
|---|---|---|
| "There was not a cloud in" | 1730 to 2352, 2715 to 2759 | x 962 to 1398, y 253 to 284 |
| "the sky." | 387 to 583, 2826 to 2878 | x 19 to 157, y 331 to 367 |
| "TV stations interrupted ... but then" (not underlined) | 597 to 2410, 2373 to 2427 | x 166 to 1439, y 13 to 51 |
| "resumed their normal schedules." (not underlined) | 391 to 1227, 2488 to 2540 | x 22 to 609, y 93 to 130 |
The builder confirms each box within 10 px on the cut file.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground A (television part) | canvas gradient |
| Television | the big television (design sheet section 7): box x 480 to 1440, y 150 to 918; screen x 544 to 1158, y 214 to 726; first frame in the Station card state with comp 05's four lines |
| Ground B (sky) | full frame, one flat field: Cold blue 2 at the top easing to Cold blue 2 at 70 % over Headline white at the bottom. No sun, no cloud, no horizon, no bird, no shadow, no amber: nothing that gives a time of day |
| Document card | left 96, top 116, 1480 x 399 (right 1576, bottom 515); crop inside at (106, 126) |
| Underline | Popfig red 6 px under the two line boxes of the table's first two rows |
| Quote strip | left 96, top 560, 1480 x 220 (bottom 780): `"There was not a cloud in the sky."` Georgia 52 px, Caption dark, left 150, top 596; attribution `Disaster Research Center, 1966, p. 36` Arial 700 22 px, Caption dark sub, left 152, top 712 |

## 4. Must be true in the picture
1. Frame 0 is comp 05's last frame: the big television in the same place with the Station card on.
2. The screen returns to the Programme state on "went back", by a hard switch. It never shows a dog, a figure, a title or the word "Lassie" (S5).
3. The sky gives no time of day (the script: "no time of day shown").
4. The underlined words are the page's own. The strip repeats them letter for letter, with the page's capital and full stop.
5. The attribution is the study, with its page: `Disaster Research Center, 1966, p. 36`. No person's name and no "said" is attached to the sentence.
6. The crop names no county and no town.
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: the Station card's lines (from frame 0, as comp 05) · `"There was not a cloud in the sky."` · `Disaster Research Center, 1966, p. 36`. Page words are the image.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "TV") | 0.00 | television with the Station card; its frame line pulses once on "warning" |
| 1 | cue: "went" | 2.27 | screen hard switches to the Programme state; bars drift |
| 2 | cue: "Some" | 4.21 | television slides out left (`x:-1500`, 0.5, power3.in); the sky rises over the canvas (`y:1080 to 0`, 0.6, power3.out), then drifts `y` 0 to -24 px to the end |
| 3 | cue: "outside" | 4.87 | document card slides in from the right (`x:660 to 0`, 0.7, power3.out) |
| 4 | cue: "not" | 6.21 | unlit page fades in; underline draws on "There was not a cloud in" (0.5 s), then on "the sky." (0.25 s), ending on "sky" |
| 5 | cue: "sky" (last word) | 7.05 | quote strip rises; hold 1.2 s; a 3 px float on card and strip carries it |
| 6 | exit | 8.74 | card and strip slide out right (`x:1900`, 0.6, power3.in) into the hard cut to 07 |
Option for the lead, not built unless asked: on step 3 the page's own "TV stations interrupted usual programming to issue warnings, but then resumed their normal schedules." can stay bright for a second before the unlit page covers it; its boxes are in section 2.

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s3-cloud.html`, id prefix `cloud-`, root id `cloud-root`.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (page crop, unlit page, lit sentence) and `library/inhouse/quote-card.html` (beige quote with attribution).
