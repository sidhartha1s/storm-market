# 05 · I1-S2 · the South Bend area, the name, the station's card (comp `g-i1s2-station`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 2, 3, 7. Revised 12 Oct 26 to the fact-checked line.
**Spoken (I1-S2):** "In the South Bend area, an eleven year old was watching Lassie on the local station. The station carried word from the Weather Bureau that there were too many tornado reports to keep track of."
**One look:** a soft ring on the north of Indiana, a name and an age, then a television whose ordinary picture gives way to a plain card of words.

## 0. What this graphic claims
In the South Bend area, Ron Przybylinski, age 11, was watching television on the local station. As he recalled in 2014, the station passed on word from the Weather Bureau of "so many tornado reports that it was hard to keep track of them".

## 1. Source
`edit_script.md` I1-S2, Rows [E] · [E]: "a 2014 recollection: the 'South Bend Indiana area', 'the local CBS station'; an age and no gender". Name card text from the Picture note: "Ron Przybylinski · age 11 · South Bend area · recalled in 2014". Card words from the Picture note: "so many tornado reports that it was hard to keep track of them", small line "as recalled in 2014". No photograph of him and no frame of the show exists that we may use. Needs no file from `media/stills/` or `media/docs/`.
Map: our own, from `library/inhouse/master-map-us-canada.html` (Natural Earth state outlines). The ring is centred by the basemap's own projection on 41.68 N, 86.25 W.

## 2. Datum, scale, orientation
North up. Indiana's outline is fitted into the box x 230 to 650, y 150 to 930 by one uniform scale from the basemap (the builder states px per degree in the receipt). The ring's centre must land in the top fifth of the outline, close to the northern border; if it does not, the projection is wrong.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| Indiana | fill Panel dark, outline 3 px Body light; neighbouring states outline only, Label grey at 40 %, clipped to x 96 to 760 |
| Area ring | circle radius 46, 3 px Amber 2 at 80 %, fill Amber 2 at 14 %; it breathes radius 46 to 52 (finite repeats). No dot at its centre: an area, not a point. Label `South Bend area` to its right, Arial 700 26 px, Headline white |
| Name card | glass card left 800, top 300, 720 x 230 (right 1520, bottom 530). Eyebrow `RECALLED IN 2014` Arial 700 22 px Label grey tracking 6 at top 330; name `Ron Przybylinski` Arial Black 900 52 px Headline white at top 366; sub `age 11 · South Bend area` Georgia italic 30 px Amber 2 at top 446. No photo slot, no monogram |
| Television | the big television (design sheet section 7): box x 480 to 1440, y 150 to 918; screen x 544 to 1158, y 214 to 726 |
| Station card | on the screen, Station card state: four lines, Arial 700 40 px, Headline white, centred on x 851, line tops 300, 352, 404, 456: `"so many tornado` / `reports that it was` / `hard to keep track` / `of them"`. Small line `as recalled in 2014`, Arial 700 22 px, Label grey, centred, top 560 |

## 4. Must be true in the picture
1. The ring is over the South Bend area, in northern Indiana, inside the state outline. It is a soft area, not a pin on a town. No county outline is drawn and no other place is labelled (S1).
2. The name is spelled `Ron Przybylinski`; the age is 11; the year is 2014; the place reads `South Bend area`, never `South Bend` alone.
3. Text only for the person: no photograph, silhouette, monogram or drawn child (S5).
4. The word "Lassie" is never on screen and the Programme state shows no dog, no figure and no title (S5).
5. **The card is the station's, not a Weather Bureau bulletin.** It carries the recalled words in quotation marks and `as recalled in 2014`, and nothing else: no heading "WEATHER BUREAU", no time, no "tornado warning", no map, no county, no station name or call letters, no network name.
6. The card's words are the Picture note's, letter for letter; the narration's paraphrase ("too many tornado reports to keep track of") is not what is typed.
7. The switch to the card is a hard cut with one flash, on the second sentence, not before.
8. The map and name card have left the frame before the television is drawn: one reading target at a time.
9. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `South Bend area` · `RECALLED IN 2014` · `Ron Przybylinski` · `age 11 · South Bend area` · the four card lines · `as recalled in 2014`. Two leaves carry "2014" (the name card's eyebrow, the screen's small line) but never in the same frame: the name card has left before the card is on.
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (hard cut from 04, word "In") | | Indiana and neighbours on; a slow `y` float of 4 px on the map group for the whole map hold |
| 1 | cue: "South" | | ring grows in (`scale 0 to 1`, 0.4, back.out), label in |
| 2 | cue: "eleven" (whisper may write "11") | | name card slides in (`x:660 to 0`, 0.7, power3.out); eyebrow, name, sub 0.15 s apart |
| 3 | cue: "watching" | | map exits left (`x:-980`), name card exits right (`x:980`), 0.5 s; television draws on (0.8 s), screen Idle |
| 4 | cue: "Lassie" | | screen to Programme state (hard switch, one flash); bars drift |
| 5 | cue: "carried" (second sentence) | | screen to Station card (hard switch, one flash); the four lines are on at once, as a broadcast card would be |
| 6 | cue: "reports" | | the card's frame line pulses once |
| 7 | cue: "of" (last word) | | hold 0.8 s |
| 8 | exit | | hard cut to 06, which opens on this television in this state |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s2-station.html`, id prefix `stn-`, root id `stn-root`.
**Closest library exemplar:** `library/inhouse/master-map-us-canada.html` (the basemap and its projection) and El Reno `compositions/g-i1s1-map.html` (a state map with one marked place and a card beside it); name card from `library/inhouse/snippets/cards.css` `.namecard`, values baked in under the comp's own class.
