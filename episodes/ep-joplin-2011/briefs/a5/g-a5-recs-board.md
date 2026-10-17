# g-a5-recs-board · A5-S11 · STANDARD (Sonnet 5.5, high) · BASE for A6's recommendation board

Open numbers: none. This is the first appearance of the recommendation board; A6 copies this file and ticks tiles (structure.md: R7, R8, R13 ticked where adopted, which are NIST Recommendations 7, 8 and 13, facts rows R3, R5, R7). Build it so a tick can be added per tile without moving anything.
Full frame, ground on from frame 0. **Host start = a5-s11 0.00**, duration 6.80 s (wav 6.20 + 0.60). The bed drops out on "didn't."@5.72 (audio, not this comp). The A6 chapter blackout follows.

## 0. Claim
NIST wrote sixteen recommendations after Joplin; whether each was adopted is A6's to show, so here every tile is grey.

## 1. Source
R1: "NIST has developed 16 recommendations for improving tornado hazard characterization, for improving how buildings and shelters are designed, constructed, and maintained in tornado-prone regions, and for improving the emergency communications" (NIST NCSTAR 3, E.5).

## 2. Datum, scale, orientation
4 x 4 grid, tiles numbered 1 to 16 in reading order (row by row, left to right): tile n = NIST Recommendation n.

## 3. Geometry
- Tile: 180 x 120 px, radius 14, fill `#2a3644`, 1 px `#4a5560` edge; gap 24 px. Grid 792 x 552 px, left 380, top 250 (x 380 to 1172, y 250 to 802).
- Tile number: 30 px Arial 700 `#93a3b2`, top-left inside the tile, 16 px padding. Leave the tile's right half empty for A6's tick.
- Chip `16 RECOMMENDATIONS`: right of the grid, left 1220, top 250, 40 px; must end before x 1600 (measure; if it runs past, stack it as two lines `16` / `RECOMMENDATIONS`).
- Source line bottom-left.
- Nothing at x >= 1600, y >= 680.

## 4. Must be true in the picture
1. Exactly 16 tiles, numbered 1 to 16, none repeated or missing.
2. All tiles grey for the whole comp: no tick, no colour, no "adopted" mark in A5 (sources in A6 decide).
3. Tile numbers are recommendation numbers, so tile 7, 8 and 13 sit where A6 will tick them (row 2 col 3, row 2 col 4, row 4 col 1).

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| tiles land (scale 0.8 -> 1, autoAlpha, stagger 0.04 s from tile 1) | a5-s11 "16"@0.86 |
| chip `16 RECOMMENDATIONS` | a5-s11 "recommendations"@1.34 |
| source line `NIST NCSTAR 3 · E.5` | a5-s11 "recommendations"@1.34 |
| a light sweep (soft gradient band, x across the grid, 2.4 s) | a5-s11 "Some"@3.74 to 6.20 |
| exit: fade-through to the chapter blackout | 6.20 to 6.80 |
The source line is not on the Picture line; drop it if the orchestrator reads the line as complete. The tile numbers 1 to 16 are a base choice for A6, not on the Picture line.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
