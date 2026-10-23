# g-a6-board-half · DEEP (Opus 5.5, high) · a6-s4 1.68 to 8.66

Open numbers: N6 (source line "FEMA Recovery Advisory 1 · NIST news, Jul 2024 · ICC 2024 IBC, 423.4" is held; the comp carries "NIST Impacts page" only).
Base: the A5-S11 recommendation board, in the lifted state built by g-a6-board-r7 (copy that file; tile 7 at centre (960, 500), scale 2.4, others at 0.25). Build after g-a6-board-r7.
Full-frame graphic. It enters over the footage under g-a6-cmt-mandatory as that card exits.

## 0. Claim
Of Recommendation 7's four building types, only schools have a shelter rule in the model code; nothing listed requires shelters in stores or apartment buildings.

## 1. Source
- R3, NIST NCSTAR 3 Sec. 5.2.2 Recommendation 7: "tornado shelters be installed in new and existing multi-family residential buildings, mercantile buildings, schools and buildings with assembly occupancies".
- R13, NIST web Impacts page: "tornado shelters are now required per the International Building Code (IBC) in new schools and emergency response facilities across parts of 22 states". R14 (same page) calls the school-campus change "Joplin Recommendation #7".
- "Nothing listed" for stores and apartments: R13 names schools and emergency response facilities only; the script's other sources (FEMA, NIST news, ICC, edit_script A6-S4 Rows) are not facts.md rows (N6).

## 2. Datum, scale, orientation
As g-a6-board-r7 §2 and §3: lifted tile 7 box x 600 to 1320, y 296 to 704 (720 x 408), centre (960, 500). Sub-rows inside the lifted tile, left-aligned at x 660, centre lines y 426, 488, 550, 612 (computed: tile top 296 + 130 + 62 per row).

## 3. Geometry
- Frame 0: the lifted state (board dim at 0.25, tile 7 at 2.4x with its Amber 1 border and numeral). No "TORNADO SHELTERS" label this time; the sub-rows replace it.
- Four sub-rows, each a 28 px square status mark at x 660 plus a label at x 708 (row-value tier, 30 px):
  - y 426 "APARTMENTS": grey (mark Diagram grey 2 `#2a3644`, label `#93a3b2`)
  - y 488 "STORES": grey
  - y 550 "SCHOOLS": lit (mark Amber 1 `#d8a13a` filled with a tick, label Headline white `#f2f5f8`)
  - y 612 "ASSEMBLY": grey, never pulsed (R13 does not list it; the script names only stores and apartments)
  The numeral "7" moves to the tile's top-right corner (x 1240, y 340) to make room; scale stays 2.4 on the tile, labels are authored at screen size inside an unscaled HUD layer that tracks the tile box (text never rides a scale tween).
- "Half lit": the tile's border stays Amber 1 on its left half and turns Diagram grey 2 on its right half (two 4 px border paths).
- Chip (glass chip, row-value tier): "STORES, APARTMENTS: NOTHING LISTED", centred x 960, centre y 790 (below the tile's bottom 704, clear of the corner).
- Source line: "NIST Impacts page", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Exit: the tile and chip slide out `x:980, autoAlpha:0, 0.6, power3.in` from 8.06, the board fades with them; gone by 8.66, onto the West Tower photograph.

## 4. Must be true in the picture
1. Exactly four sub-rows, in R3's order of building types (apartments, stores, schools, assembly), and only SCHOOLS is lit.
2. No tile other than 7 is lit or ticked.
3. The chip names stores and apartments only.
4. No label rides the tile's scale; every label stays inside the tile box.
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues (a6-s4.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Lifted board in (cross-fade 0.4 s from the comment card's footage) | none | "nothing" @ 1.68 |
| Four sub-rows land, stagger 0.15, fromTo autoAlpha 0, y 24 to 0 | APARTMENTS / STORES / SCHOOLS / ASSEMBLY | "nothing" @ 1.68 |
| SCHOOLS mark fills and ticks | none | "says" @ 1.88 |
| Chip | STORES, APARTMENTS: NOTHING LISTED | "storm" @ 3.14 |
| Source line | NIST Impacts page | "storm" @ 3.14 |
| STORES mark pulses (scale 1 to 1.15 to 1) | none | "stores" @ 4.30 |
| APARTMENTS mark pulses | none | "homes" @ 4.76 |
| Hold with float (y 6 px) | none | to 8.06 |
| Exit | none | 8.06 to 8.66 ("Remember" @ 8.66) |
Note: s4 says "homes"; the pulse lands on APARTMENTS because that is Recommendation 7's residential type (R3). Single-family homes are not in Recommendation 7 and get no row.

## 6 to 8
Template §6 to §8, COMPID `g-a6-board-half`.
