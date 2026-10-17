# g-a6-board-r7 · DEEP (Opus 5.5, high) · a6-s1 0.00 to 6.30

Open numbers: none used.
Base: the recommendation board first built for A5-S11 (`briefs/a5/`). Copy that file; do not redraw. If A5 fixed tile px that differ from §3, A5 wins and the §4 relations still hold.
Full-frame graphic (opens act a6 after the chapter blackout); no footage beneath.

## 0. Claim
NIST made 16 recommendations; this act is about one of them, Recommendation 7.

## 1. Source
- R1, NIST NCSTAR 3 E.5: "NIST has developed 16 recommendations for improving tornado hazard characterization, ... how buildings and shelters are designed ... and ... the emergency communications".
- R3, NIST NCSTAR 3 Sec. 5.2.2 Recommendation 7: "(b) tornado shelters be installed in new and existing multi-family residential buildings, mercantile buildings, schools and buildings with assembly occupancies".

## 2. Datum, scale, orientation
Board grid, 4 x 4, tiles numbered 1 to 16 row-major from the top-left. Tile 300 x 170 px, gap 28 px. Grid box x 200 to 1484, y 158 to 922 (kept left of x 1600 so the presenter corner x >= 1600, y >= 680 stays empty). No scale: tiles are equal; nothing on the board is a quantity.

## 3. Geometry
- Opening state (frame 0): the A5-S11 end state, 16 tiles, all grey (Diagram grey 2 `#2a3644` fill, label grey `#93a3b2` numerals, Arial Black 900 52 px centred).
- Tile 7: box x 856 to 1156, y 356 to 526, centre (1006, 441).
- Lift: tile 7 moves to centre (960, 500), dx -46, dy +59, scale 1 to 2.4 (box x 600 to 1320, y 296 to 704); it gains a 4 px Amber 1 `#d8a13a` border. The other 15 tiles go to opacity 0.25 and scale 0.96 around their own centres.
- On the lifted tile, under its numeral: label "TORNADO SHELTERS" (diagram label tier, Body light `#dfe7ee`), centred at y 600. Inside the tile, not over its border.
- Exit: zoom-through. From s1 5.80 the lifted tile scales 2.4 to 6 around its centre with logZoom (`library/inhouse/snippets/helpers.js`; the move is over 1.5x) while the label fades out by 5.95 (before it reaches the text-safe edge); the comp ends on the tile's fill covering the frame at 6.30, cut to g-a6-doc-rec7.

## 4. Must be true in the picture
1. Exactly 16 tiles, numbered 1 to 16, one each (R1).
2. The tile that lifts is the 7th in reading order and reads "7" (R3).
3. Lifted tile is 2.4x the resting tile (720 x 408 vs 300 x 170) and is the only element at full opacity.
4. No text, tile or border inside x >= 1600, y >= 680 at any frame.
5. No tile carries a tick, colour or caption other than tile 7 (adoption status is not shown in s1).

## 5. Panel text and cues (a6-s1.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Board holds, slow drift (y float 6 px) | numerals 1 to 16 | from 0.00 "Of" |
| All 16 tiles pulse once (scale 1 to 1.04 to 1, stagger 0.03) | none | "16" @ 1.20 |
| Tile 7 lifts, others dim | "7" | "Recommendation" @ 4.44, landed by "7." @ 5.20 |
| Label on the lifted tile | TORNADO SHELTERS | "7." @ 5.20 |
| Zoom-through exit | none | 5.80, done 6.30 ("NIST" @ 6.30 starts g-a6-doc-rec7) |

## 6 to 8
Template §6 to §8, COMPID `g-a6-board-r7`. Hand the copied base to the orchestrator for a full-size read before the states are added (template 7a, "a family built on one base"). g-a6-board-half reuses this file's lifted state.
