# 09 · I1-S6 · the study's sentence about police headquarters (comp `g-i1s6-page`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` section 9. Kept apart from comp 10 on purpose: this page is one county, comp 10's page is another, and the two never share a frame or a comp.
**Spoken (I1-S6):** "In one county, police headquarters did not tell their own officers until the first tornado hit."
**One look:** a real page of the 1966 study, one sentence underlined, the same sentence large beneath it, under the label "one Indiana county".

## 0. What this graphic claims
The study records, of one Indiana county it does not name: "Police headquarters did not notify other members of their own organization nor any other organization until after the first tornado hit the county."

## 1. Source
`edit_script.md` I1-S6, Rows [C2] (County A). Page: the 1966 study, printed pp. 19 to 20. **Waits for the study scan, printed pp. 19 and 20** (not a row of `research/picture-inventory.md`; rights line unread; needs a `provenance.csv` row).
The sentence may run across the page break. If it does, the card holds two crops, the foot of p. 19 above the head of p. 20, with a 14 px Panel dark gap and a small page tag at each crop's right edge (`p. 19`, `p. 20`, Arial 700 20 px, Caption dark sub).

## 2. Datum, scale, orientation
Page scale = 1460 / text column width in page px (design sheet section 9). The builder measures every line box of the sentence on the page image or images, in page px, with the x of its first and last word, and records them in the comp. Crop: the sentence's lines plus one line above and one below.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| County label | glass chip left 96, top 54, height 46: `one Indiana county` Arial 700 26 px, Body light |
| Document card | left 96, top 116, 1480 x 450 (right 1576, bottom 566) |
| Underline | Crimson 6 px, one segment per line box, from the sentence's first word to its last |
| Quote strip | left 96, top 606, 1480 x 220. Quote in Georgia 40 px, Caption dark, left 150, top 626, three lines, line height 50: `"Police headquarters did not notify other members of` / `their own organization nor any other organization` / `until after the first tornado hit the county."` Attribution `Disaster Research Center, 1966` Arial 700 22 px, Caption dark sub, left 152, top 788 |
The strip's longest line is 51 characters; at Georgia 40 px it is checked on a frame to end before x 1530.

## 4. Must be true in the picture
1. The underline covers that sentence and no other word, across every line box it occupies.
2. The strip's words are the page's words, letter for letter, not the narration's ("notify", "organization", "the county").
3. The label reads `one Indiana county`. No county, town or department name is on screen. If the study's code "County A" stands in the crop, it is under the unlit page and never underlined (S1).
4. Comp 10's label `a different county` and comp 10's page are not in this comp, and this comp has fully left before comp 10's first frame.
5. No badge, no police car, no drawing of an officer (S5).
6. The strip appears only after the underline is complete.
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `one Indiana county` · the quote in three lines as section 3 · `Disaster Research Center, 1966` · page tags if two crops. Page words are the image.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "In") | | canvas ground; document card already sliding in (`x:660 to 0`, 0.7, power3.out) |
| 1 | cue: "one" | | county label drops in (`y:-30 to 0`, 0.3) |
| 2 | cue: "police" | | unlit page fades in; underline starts on the first line box |
| 3 | cue: "officers" | | underline reaches the middle line box or boxes |
| 4 | cue: "tornado" | | underline completes on the last line box |
| 5 | cue: "hit" (last word) | | quote strip rises; hold 1.5 s; a 3 px float on card and strip carries it |
| 6 | exit | | label, card and strip slide out right (`x:1900`, 0.6, power3.in); the frame is clear before the hard cut to 10 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s6-page.html`, id prefix `pol-`, root id `pol-root`.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (page crop, unlit page, a sentence lit line by line on the voice) and `library/inhouse/quote-card.html`.
