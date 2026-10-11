# 05 · I1-S2 · South Bend on the map, the boy's name, the break-in (comp `g-i1s2-breakin`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 2, 3, 7.
**Spoken (I1-S2):** "In South Bend, Indiana, an eleven year old was watching Lassie when the Weather Bureau broke into the show."
**One look:** a pin on South Bend, a name and an age, then a television whose picture is replaced by the words WEATHER BUREAU.

## 0. What this graphic claims
In South Bend, Indiana, Ron Przybylinski, age 11, was watching television when the Weather Bureau broke into the show. He recalled it in 2014.

## 1. Source
`edit_script.md` I1-S2, Rows [E]: name card text "Ron Przybylinski · age 11 · South Bend · recalled in 2014"; "facts.md states an age and no gender". No photograph of him and no frame of the show exists that we may use. Needs no file from `media/stills/`.
Map: our own, from `library/inhouse/master-map-us-canada.html` (Natural Earth state outlines). South Bend is placed by the basemap's own projection at 41.68 N, 86.25 W.

## 2. Datum, scale, orientation
North up. Indiana's outline is fitted into the box x 230 to 650, y 150 to 930 by one uniform scale from the basemap (the builder states px per degree in the receipt). The pin must land in the top fifth of the outline, close to the northern border; if it does not, the projection is wrong.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| Indiana | fill Panel dark, outline 3 px Body light; neighbouring states outline only, Label grey at 40 %, clipped to x 96 to 760 |
| Pin | circle radius 9, Amber 2, with one ring pulse (radius 9 to 34, finite, 2 repeats); label `South Bend` to its right, Arial 700 26 px, Headline white |
| Name card | glass card left 800, top 300, 700 x 230 (right 1500, bottom 530). Eyebrow `RECALLED IN 2014` Arial 700 22 px Label grey tracking 6 at top 330; name `Ron Przybylinski` Arial Black 900 52 px Headline white at top 366; sub `age 11 · South Bend` Georgia italic 30 px Amber 2 at top 446. No photo slot, no monogram |
| Television | design sheet television x 2.4: box x 600 to 1320, y 200 to 776 (cabinet bottom y 680, legs to 776); screen x 648 to 1109, y 248 to 632 |
| Break-in card | `WEATHER` / `BUREAU`, Arial Black 900 64 px, Headline white, centred on the screen (461 px wide screen; the longer word is about 330 px) |
The television box is the shared number with comp 06 and comp 10.

## 4. Must be true in the picture
1. The pin is on South Bend, in northern Indiana, inside the state outline. No county outline is drawn and no other town is labelled (S1).
2. The name is spelled `Ron Przybylinski`; the age is 11; the year is 2014.
3. Text only for the person: no photograph, silhouette, monogram or drawn child (S5).
4. The word "Lassie" is never on screen and the Programme state shows no dog, no figure and no title (S5).
5. The break-in card reads `WEATHER BUREAU` and nothing else: no time, no "tornado", no map, no county.
6. The switch to the card is a hard cut with one flash, on the word "broke", not before.
7. The map and name card have left the frame before the television is drawn: one reading target at a time.
8. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `South Bend` · `RECALLED IN 2014` · `Ron Przybylinski` · `age 11 · South Bend` · `WEATHER BUREAU`. The label `South Bend` on the pin and in the card sub line are one place named on two things: declare `data-repeat-ok="pin label and card sub line"` on the pin label's leaf only if overlap_check reports it (it carries no digit, so it should not).
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (hard cut from 04, word "In") | | Indiana and neighbours on; a slow `y` float of 4 px on the map group for the whole map hold |
| 1 | cue: "South" | | pin drops (`y:-40 to 0`, 0.3, back.out), ring pulses, label in |
| 2 | cue: "eleven" (whisper may write "11") | | name card slides in (`x:660 to 0`, 0.7, power3.out); eyebrow, name, sub 0.15 s apart |
| 3 | cue: "watching" | | map exits left (`x:-980`), name card exits right (`x:980`), 0.5 s; television draws on (0.8 s), screen Off |
| 4 | cue: "Lassie" | | screen to Programme state (hard switch, one flash); bars drift |
| 5 | cue: "broke" | | screen to Break-in card (hard switch, one flash) |
| 6 | cue: "show" (last word) | | hold 0.8 s; the card's frame line pulses once |
| 7 | exit | | hard cut to 06, which opens on this television in this state |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s2-breakin.html`, id prefix `brk-`, root id `brk-root`.
**Closest library exemplar:** `library/inhouse/master-map-us-canada.html` (the basemap and its projection) and El Reno `compositions/g-i1s1-map.html` (a state map with one pin and a card beside it); name card from `library/inhouse/snippets/cards.css` `.namecard`, values baked in under the comp's own class.
