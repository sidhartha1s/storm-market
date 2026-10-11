# 09 · I1-S6 · the study's sentence about police headquarters (comp `g-i1s6-page`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` section 9. Kept apart from comp 10 on purpose: this page is one county, comp 10's page is another, and the two never share a frame or a comp. Revised 12 Oct 26 to the page scan.
**Spoken (I1-S6):** "In one county, police headquarters did not tell their own officers until the first tornado hit."
**One look:** a real page of the 1966 study, one sentence underlined, the same sentence large beneath it, under the label "one Indiana county".

## 0. What this graphic claims
The study records, of one Indiana county it does not name: "Police headquarters did not notify other members of their own organization nor any other organization until after the first tornado hit the county."

## 1. Source
`edit_script.md` I1-S6, Rows [C2] (County A). The script names two files for printed pp. 19 to 20. Read by eye 12 Oct 26: **the whole sentence is on printed p. 20**, `media/docs/study-pdf-22-orig.png` (2684 x 3394). Page 19 (`study-pdf-21-orig.png`) ends "The City Police in the county's largest city had also" and carries the heading "County A."; it is not shown. The crop's four lines read:
"been monitoring the 5:50 p.m. State Police message, but did not take any / action at that time. Police headquarters did not notify other members of / their own organization nor any other organization until after the first tornado / hit the county."

## 2. Datum, scale, orientation
Crop box, page px: x 320 to 2350, y 370 to 800 (2030 x 430), saved as `media/docs/study-p20-police-crop.png` at 1460 x 309 (scale 0.7192). Line pitch on the card is about 83 px.
| Underline | Words | Page px (x0 to x1, y0 to y1) | Px inside the 1460 crop |
|---|---|---|---|
| U1 | "Police headquarters did not notify other members of" | 884 to 2220, 501 to 550 | x 406 to 1367, y 94 to 129 |
| U2 | "their own organization nor any other organization until after the first tornado" | 348 to 2322, 616 to 665 | x 20 to 1440, y 177 to 212 |
| U3 | "hit the county." | 347 to 706, 738 to 780 | x 19 to 278, y 265 to 295 |
U1 starts at "Police" (page x 884), after "action at that time." on the same line. The builder confirms each box within 10 px on the cut file.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| County label | glass chip left 96, top 54, height 46: `one Indiana county` Arial 700 26 px, Body light |
| Document card | left 96, top 116, 1480 x 329 (right 1576, bottom 445); crop inside at (106, 126) |
| Underlines | Popfig red 6 px, U1, U2, U3 |
| Quote strip | left 96, top 490, 1480 x 250 (bottom 740). Quote in Georgia 40 px, Caption dark, left 150, top 514, three lines, line height 50: `"Police headquarters did not notify other members of` / `their own organization nor any other organization` / `until after the first tornado hit the county."` Attribution `Disaster Research Center, 1966, p. 20` Arial 700 22 px, Caption dark sub, left 152, top 684 |
The strip's longest line is 51 characters; at Georgia 40 px it is checked on a frame to end before x 1530.

## 4. Must be true in the picture
1. The underline covers that sentence and no other word: it starts at "Police", not at "action".
2. The strip's words are the page's words, letter for letter, not the narration's ("notify", "organization", "the county").
3. The label reads `one Indiana county`. No county, town or department name is on screen. The crop is from p. 20 only, so the study's heading "County A." is not in it (S1).
4. Comp 10's label `a different county` and comp 10's page are not in this comp, and this comp has fully left before comp 10's first frame.
5. The crop's first line ("been monitoring the 5:50 p.m. State Police message...") stays under the unlit page: no second time is lit in this comp.
6. No badge, no police car, no drawing of an officer (S5).
7. The strip appears only after the underline is complete.
8. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `one Indiana county` · the quote in three lines as section 3 · `Disaster Research Center, 1966, p. 20`. Page words are the image.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "In") | | canvas ground; document card already sliding in (`x:660 to 0`, 0.7, power3.out) |
| 1 | cue: "one" | | county label drops in (`y:-30 to 0`, 0.3) |
| 2 | cue: "police" | | unlit page fades in; U1 draws (0.5 s) |
| 3 | cue: "officers" | | U2 draws (0.7 s) |
| 4 | cue: "tornado" | | U3 draws (0.25 s) |
| 5 | cue: "hit" (last word) | | quote strip rises; hold 1.5 s; a 3 px float on card and strip carries it |
| 6 | exit | | label, card and strip slide out right (`x:1900`, 0.6, power3.in); the frame is clear before the hard cut to 10 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s6-page.html`, id prefix `pol-`, root id `pol-root`.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (page crop, unlit page, a sentence lit line by line on the voice) and `library/inhouse/quote-card.html`.
