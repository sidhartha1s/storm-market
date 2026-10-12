Host: id=g-z1s02-row file=compositions/g-z1s02-row.html start=1135.63 (timeline-map.md table 1; the mount in index.html wins) duration=20.39 s track=2

# g-z1s02-row · Z1-S2, Z1-S3 · the row that was never on the list, and the phone that is (wave 5, list and chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 1, 5, 6, 7, 10 and 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a rows DR-10 and DR-11. Times: `mg_specs/timeline-map.md` tables 1 and 5. Bases: the built `compositions/g-t1s3-list.html` (the sheet) and `mg_specs/briefs/g-a1s13-chain.md` (links, the travelling light).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). The study's hidden counties are "County A" and "County B" only (rule 8): this comp carries neither chip. The teletype room photograph is not used (rule 9). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (Z1-S2):** "The family was never a row on that list. Reaching them was mostly left to an announcer who might not have been told, and that evening it stopped on a police desk."
**Spoken (Z1-S3):** "Today a tornado warning from the National Weather Service goes out through the phone carriers to the cell phones in the warned area. Nobody is on a list, and nobody has to sign up."
**One look:** the list with its empty ninth row; under it the old chain, stopped at a police desk; then one light goes round all of it, to a tower, to a phone, and the house window turns amber for the first time in the film.

## 0. What this graphic claims
The family was never a row on the 1965 telephone list. Today a tornado warning from the National Weather Service goes through the phone carriers to the cell phones in the warned area, with no list and no sign-up.

## 1. Source
- `edit_script.md` Z1-S2, Rows [A6; study printed p. 14] and [C12; study printed p. 35; C5; study printed p. 22]. Z1-S3, Rows [NWS, weather.gov WEA pages: "sent directly to your phone by authorized government alerting authorities through your mobile carrier"; FEMA IPAWS].
- The sheet is design sheet section 5. The chain's stations are the drawings of `media/drawings/` with the mount rules of `media/drawings/README.md`.

## 2. Datum, scale, orientation
The sheet keeps design sheet section 5's world at scale 1.0 with one transform, tx 516, ty -6: sheet screen x 580 to 1340, y 54 to 644; row text 26 px; the blank ninth row's centre is screen y 592.
The chain stands under it on one line, y 834, with everything left of x 1600:
| Station | Drawing and scale | Box (x, y) |
|---|---|---|
| Weather Bureau desk | `media/drawings/desk.svg` at 0.85, its telephone on the cradle | 96 to 351, 770 to 898 |
| Police desk | `media/drawings/desk.svg` at 0.85 | 520 to 775, 770 to 898 |
| Microphone | `media/drawings/microphone.svg` at 0.6 (72 x 138) | 960 to 1032, 760 to 898 |
| Cell phone | `media/drawings/cell-phone.svg` at 0.8 (48 x 88) | 1220 to 1268, 810 to 898 |
| Cell tower | `media/drawings/cell-tower.svg` at 0.9 (54 x 216) | 1290 to 1344, 682 to 898 |
| House | `media/drawings/house.svg` at 0.68 (177 x 170) | 1380 to 1557, 728 to 898 (aerial to y 705) |
All stations share the floor y 898. Set `stroke-width` on each group so a line is 3.5 to 4 px on screen (README, line weight by size).

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| List sheet | design sheet section 5 in the transform of section 2: eyebrow, title `Organizations notified included:`, eight rows plain, the blank ninth row with its cursor block blinking on finite repeats. On from frame 0 |
| Row pulse | an Amber 2 band at 25 % over the blank ninth row (row box 44 px tall, sheet width less its margins), wiped left to right and gone |
| Old links, y 834, 4 px, round caps | Weather Bureau desk to police desk, x 351 to 520, solid, `#55606b`; police desk to microphone, x 775 to 960, dotted (`stroke-dasharray="0.1 14"`), `#55606b`; microphone to house, x 1032 to 1380, dotted, `#55606b` (it passes behind the phone and the tower, which are drawn later and have Panel dark bodies) |
| Old light | an Amber 2 line, 6 px, growing from x 351 to x 520 on the first link, led by an Amber 2 dot of radius 8 that hides on arrival; the link stays Amber 2 |
| Stop mark | Popfig red rect 6 x 72 at x 778, y 798 (3 px right of the police desk's right edge, across the line), as `#chn-stop` of the built `compositions/g-i1s9-chain.html` |
| Station labels | Arial 700 22 px, Label grey, centred under each box, top 916: `Weather Bureau` · `a police desk` · `an announcer` · `a family` (under the house). The phone and the tower take no label |
| New path | one Amber 2 path, 6 px, round caps and joins: from the Weather Bureau desk's top (223, 770) up to y 712, right along y 712 to x 1290, then to the tower's top (1317, 682). It runs under the sheet (bottom y 644) and over the police desk and the microphone (tops y 770 and 760) and touches neither. Drawn with `strokeDashoffset`, led by a dot of radius 8 |
| Tower to phone | an Amber 2 line, 6 px, from (1317, 700) to (1244, 810) |
| Phone lit | the phone's screen (`dw-lamp`) to Amber 2, as `media/drawings/cell-phone-lit.svg` |
| House lit | lines to Headline white, windows (`dw-win`) to Amber 2 at 0.3, as `media/drawings/house-lit.svg` |
| Source line | fixed HUD, left 96, bottom 60: `Disaster Research Center, 1966, p. 14` in Z1-S2; in Z1-S3 a second pre-authored element in the same place: `National Weather Service` |

## 4. Must be true in the picture
1. Nothing is ever typed in the blank ninth row. No numbering, no tick, no tick box, no row count on the sheet.
2. In Z1-S2 the old light stops at the police desk; the stop mark is the only red; the microphone and the house stay dark.
3. In Z1-S3 the new path does not touch the sheet, the police desk or the microphone: it goes round them. It leaves from the Weather Bureau desk.
4. The house window turns Amber 2 only after the phone is lit, and it is the first amber house window in A1 to Z1.
5. No carrier, phone maker, app or logo is named or drawn. The phone's screen carries no text.
6. No county chip. Nothing in x >= 1600 and y >= 680 (the house ends at x 1557). Nothing appears before its spoken word.

## 5. Text (exact) and cues
Text: the sheet's text as design sheet section 5 · `Weather Bureau` · `a police desk` · `an announcer` · `a family` · the two source lines.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: Z1-S2 0.15, Z1-S3 9.56) plus the word's time; a segment's first word uses table 5's first sound. The comp starts on the cut out of Paul's clip, so the voice follows the picture.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | cut | | | | 0.00 | first frame: the sheet whole, cursor blinking in the blank row, source line on |
| 1 | Z1-S2 | 5 | row | 1.52 | 1.67 | the row pulse wipes across the blank ninth row (0.5 s) and leaves |
| 2 | Z1-S2 | 9 | Reaching | 3.22 | 3.37 | the chain draws on under the list, left to right: Weather Bureau desk, police desk, microphone, house, with their links and labels (0.3 s each, 1.2 s in all), all dark |
| 3 | Z1-S2 | 27 | stopped | 7.70 | 7.85 | the old light runs from the Weather Bureau desk to the police desk (0.5 s, `ease:"none"`) |
| 4 | Z1-S2 | 31 | desk. | 8.50 | 8.65 | the stop mark lands (`scaleY` 0 to 1 from its middle, 0.2 s) |
| 5 | Z1-S3 | 0 | Today, | 0.00 | 9.89 | the source line swaps to `National Weather Service` |
| 6 | Z1-S3 | 9 | goes | 2.92 | 12.48 | the new path starts from the Weather Bureau desk (1.3 s to the tower's top, `ease:"none"`) |
| 7 | Z1-S3 | 13 | phone | 3.66 | 13.22 | the cell tower draws on behind the house (0.5 s), before the light reaches it |
| 8 | Z1-S3 | 17 | cell | 4.60 | 14.16 | the cell phone draws on beside the house (0.3 s) |
| 9 | Z1-S3 | 18 | phones | 4.82 | 14.38 | the tower to phone line draws (0.25 s); the phone's screen lights |
| 10 | Z1-S3 | 21 | warned | 5.36 | 14.92 | the house lights: lines Headline white, windows Amber 2 (0.4 s) |
| 11 | Z1-S3 | 23 | Nobody | 6.92 | 16.48 | the list sheet fades to opacity 0.36 (0.5 s) |
| 12 | Z1-S3 | 29 | nobody | 8.56 | 18.12 | the phone's screen steps to Headline white and back to Amber 2 once (0.15 s each way) |
| 13 | end | | | | 20.39 | comp ends on the hold: amber window, grey list |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-z1s02-row.html` only. Id prefix `row-`, root id `row-root`. Bases it copies: the sheet of the built `compositions/g-t1s3-list.html`; the links, travelling light and labels of `compositions/g-a1s13-chain.html` (wave 1); `#chn-stop` of the built `compositions/g-i1s9-chain.html`. Assets mounted, all inline: `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg` (lit state as `media/drawings/house-lit.svg`), `media/drawings/cell-phone.svg` (lit state as `media/drawings/cell-phone-lit.svg`), `media/drawings/cell-tower.svg`. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. `graphics_qc` flat type: the typed sheet is one of the plan's rule 10 cases. Done line 5: read the first half second of the chain's entrance for a label under a link. Done line 6: every station box and the new path's four points are computed by a script from section 2 and stated in the receipt.

## 8. Receipt
As the template's section 8, plus: a frame at 13.60 showing the new path clear of the sheet, the police desk and the microphone, and the house's right edge measured on the last frame.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.90 (pulse); 4.70 (chain drawn, dark); 8.40 (old light at the police desk); 8.90 (stop mark); 10.20 (source swapped); 13.60 (new path mid way, tower drawn); 14.60 (phone lit); 15.40 (house lit); 17.10 (list grey); last frame 20.30.
