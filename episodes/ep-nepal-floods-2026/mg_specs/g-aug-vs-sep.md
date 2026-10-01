# g-aug-vs-sep · I beat teaser (about 22.5 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (map + RHS rail with rows), counter idiom from
`library/inhouse/snippets/helpers.js` counterRollUp (leaf span, opens on its first tick).

## 0. Claim
Nepal was still counting the Aug 26 Langtang flood (1,451 lives lost, 5,745 missing as of Sept 21) when the Sept 27 Kali Gandaki
collapse happened, about 120 mi west.

## 1. Source
- factcheck-A row 10: Langtang collapse Aug 26; by Sept 21, 1,451 dead, 5,745 missing (Wikipedia infobox "as of 21 September 2026", NDRRMA).
- Kali Gandaki collapse Sept 27 near Lete (factcheck-C rows 1, 2). Coordinates: Langtang Lirung 28.2575 N 85.51583 E, Lete 28.62 N
  83.60 E (factcheck-C row 14); the Kali Gandaki pin sits on the river vertex nearest Lete (28.6288 N 83.6188 E).
- "The river below": the August flood ran down the Bhote Koshi and Trishuli, whose gauges at Rasuwagadi, Syabrubesi and Betrawati were
  destroyed (factcheck-C row 19). River geometry: OSM ways "Bhote Koshi", "Trishuli River", "Trishuli Ganga River" (ODbL).

## 2. Datum, scale, orientation
North up, same projection. Camera: world (3, -12) at screen (660, 540), **6 px per mile** (`translate(642,612) scale(6)`).
RHS rail (820 px gradient) from x 1100; rail text at x 1270. Drift 1.00 -> 1.03 about (660, 540).

## 3. Geometry (screen px at cam 1.00)
Kali Gandaki pin (320.6, 434.2); tag "Sept 27" (340, 426), label "Kali Gandaki" (340, 456).
Langtang pin (1012.4, 588.2); label "Langtang valley" centred (1012, 516), tag "Aug 26" centred (1012, 548).
Trishuli line from the border (961.8, 579.6) to Devighat (858.6, 753.6).
Rail: eyebrow (1270, 300) · "As of Sept 21" (1270, 342) · counter 1 top 388 · label · counter 2 top 538 · label.

## 4. Must be true
1. The Langtang pin is east of the Kali Gandaki pin, on the Tibet border line, and the river below it runs south from it.
2. Counters open on "0", roll on the spoken numbers and land exactly on 1,451 and 5,745; "As of Sept 21" is on screen with them.
3. The Kali Gandaki pin carries "Sept 27", Langtang carries "Aug 26"; neither pin carries the other's date.
4. Nothing in the presenter corner.

## 5. Text and cues (host starts at "Nepal hadn't finished counting" @est 0.0; 175 wpm)
Voice order puts the September event first ("when this began"), so the pins land in that order (the prompt's "second pin drops on
the Kali Gandaki" has no spoken cue after the counts; flagged in the receipt).
CUE "when this began" @est 2.4 Kali Gandaki pin + "Sept 27" · CUE "August twenty sixth" @est 3.8 Langtang pin + "Aug 26" + eyebrow ·
CUE "Langtang valley" @est 7.9 "Langtang valley" · CUE "flood down the river" @est 9.6 Trishuli draws south ·
CUE "By September twenty first" @est 11.3 "As of Sept 21" · CUE "one thousand four hundred" @est 13.4 counter 1 rolls (2.2 s) ·
CUE "lives lost" @est 15.8 label · CUE "Another five thousand" @est 17.5 counter 2 rolls · CUE "still missing" @est 20.9 label ·
rail exits 21.9 (x 980), duration 22.5 s; the g-insar-creep teaser takes "In August, satellite radar" @est 21.6.
Tiers: 84 counters · 30 date tags · 22 labels, eyebrow, 20 counter labels, 19 credit.
