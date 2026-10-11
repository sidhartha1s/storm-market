# 06 · I1-S3 · back to the show, and not a cloud in the sky (comp `g-i1s3-cloud`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 7, 9.
**Spoken (I1-S3):** "Stations cut in with a warning, then went back to their shows. People looked outside, and there was not a cloud in the sky."
**One look:** the WEATHER BUREAU card flips back to the ordinary picture; then the study's own page, one sentence underlined: "There was not a cloud in the sky."

## 0. What this graphic claims
Stations interrupted with a warning and then returned to their programmes. The 1966 study records that people looked out and "There was not a cloud in the sky."

## 1. Source
`edit_script.md` I1-S3, Rows [C22] · [C22]. Page: the 1966 study, printed p. 37, sentence `There was not a cloud in the sky.` **Waits for the study scan, printed p. 37** (the scan is not a row of `research/picture-inventory.md` and its rights line is unread; it needs a `provenance.csv` row before it is mounted).

## 2. Datum, scale, orientation
Page scale = 1460 / text column width in page px (design sheet section 9). The builder measures the sentence's line box or boxes on the page image and records them in page px. Crop: the sentence's line with two lines above and two below, full column width.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| Television | box x 600 to 1320, y 200 to 776, screen x 648 to 1109, y 248 to 632 (comp 05's numbers) |
| Document card | left 96, top 116, 1480 x 450 (right 1576, bottom 566) |
| Underline | Crimson 6 px under the sentence's line box or boxes |
| Quote strip | left 96, top 606, 1480 x 220: `"There was not a cloud in the sky."` Georgia 52 px, Caption dark, left 150, top 640; attribution `Disaster Research Center, 1966` Arial 700 22 px, Caption dark sub, left 152, top 756 |

## 4. Must be true in the picture
1. Frame 0 is comp 05's last frame: the television in the same place with the Break-in card on.
2. The screen returns to the Programme state on "went back", by a hard switch. It never shows a dog, a figure, a title or the word "Lassie" (S5).
3. The underlined words are the page's own. The strip repeats them letter for letter, with the page's capital and full stop.
4. The attribution reads `Disaster Research Center, 1966`.
5. The crop shows no county name lit; if the study's "County A" or "County B" stands in the crop it is under the unlit page (S1).
6. No sky, sun or cloud is drawn in this comp: the page says it.
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` (on the screen, from frame 0) · `"There was not a cloud in the sky."` · `Disaster Research Center, 1966`. Page words are the image.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "Stations") | | television with the Break-in card; its frame line pulses once on "warning" |
| 1 | cue: "went" | | screen hard switches to the Programme state; bars drift |
| 2 | cue: "People" | | television slides out left (`x:-1400`, 0.5, power3.in); document card slides in from the right (`x:660 to 0`, 0.7, power3.out) |
| 3 | cue: "not" | | unlit page fades in; underline draws (0.7 s) to end on "sky" |
| 4 | cue: "sky" (last word) | | quote strip rises; hold 1.2 s; a 3 px float on card and strip carries it |
| 5 | exit | | card and strip slide out right (`x:1900`, 0.6, power3.in) into the hard cut to 07 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s3-cloud.html`, id prefix `cloud-`, root id `cloud-root`.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (page crop, unlit page, lit sentence) and `library/inhouse/quote-card.html` (beige quote with attribution).
