# BRIEF · g-z1-board · "watch whether it asks for shelters in stores and apartment buildings" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, segment Z1-S3. Full-frame MG on the channel ground. Host `host-z1-board`: data-start 1152.187 (nx-z1-s3
start), data-duration 11.14 (wav 10.84 + the 0.30 s seam to ins-paul-6 at 1163.327). Comp-local time = z1-s3 word time.
It comes in on a cut from `g-z1-map`; the signature line (Paul full frame, ins-paul-6) follows on a cut.
Base: the recommendation board (`briefs/a5/g-a5-recs-board.md`) in the state `g-a6-board-half` holds before its exit: board dim at
0.25, tile 7 lifted to 2.4x at centre (960, 500), Amber 1 left half border and grey right half, numeral "7" top right, the four
sub-rows (APARTMENTS, STORES grey; SCHOOLS lit with its tick; ASSEMBLY grey). Copy `compositions/g-a6-board-half.html` and drop its
chip, its exit and its pulses. Build after `g-a6-board-half` passes its frame read.
O1 CLEARED 18 Oct 26: edit_script Z1-S3 row is CONFIRMED (ICC store page: the 2027 IBC is "available mid October"); draw the chip
and its source line. O2 CLEARED 18 Oct 26: z1-s3 is voiced (`audio/z1-s3.wav` 10.84 s, `audio/z1-s3.words.json`); times below.

## 0. What this graphic claims
Of Recommendation 7's four building types, only schools got a shelter rule; stores and apartment buildings are still not on the list
(R3, R13). The voice points at the next code edition; the picture shows what is still grey.

## 1. SOURCE
- R3, NIST NCSTAR 3 Sec. 5.2.2 Recommendation 7: "tornado shelters be installed in new and existing multi-family residential buildings, mercantile buildings, schools and buildings with assembly occupancies".
- R13, NIST web Impacts page: "tornado shelters are now required per the International Building Code (IBC) in new schools and emergency response facilities across parts of 22 states". R14 (same page) ties the school-campus change to "Joplin Recommendation #7".

## 2. DATUM, SCALE, ORIENTATION
As `g-a6-board-half.md` §2: lifted tile 7 box x 600 to 1320, y 296 to 704 (720 x 408), centre (960, 500); sub-row marks at x 660,
labels at x 708, centre lines y 426 (APARTMENTS), 488 (STORES), 550 (SCHOOLS), 612 (ASSEMBLY).

## 3. GEOMETRY
- Frame 0: the copied held state, complete (no build-in), with the source line "NIST Impacts page" (x 96, baseline 1010, Arial 700 20 `#c8d3e0`) already on.
- Float: tile and board y ±6 px over 4 s, whole host.
- Pulses: STORES mark, then APARTMENTS mark, scale 1 → 1.15 → 1 (0.5 s), and each label goes `#93a3b2` → `#f2f5f8` → `#93a3b2` with it. They stay grey; nothing ticks.
- Exit: fade-through to the ground over the last 0.6 s.
- Labels sit on the unscaled HUD layer that tracks the tile box, as the base; no text rides a scale tween.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly four sub-rows in R3's order, and only SCHOOLS is lit, in every frame.
2. STORES and APARTMENTS never fill, tick or turn amber: the pulse is a look, not an adoption.
3. The chip reads exactly "2027 BUILDING CODE" and appears once; the ICC source line sits under it as its own leaf.
4. No tile other than 7 is lit; nothing in x ≥ 1600, y ≥ 680.

## 5. PANEL TEXT (exact) and CUES (z1-s3, seconds from `audio/z1-s3.words.json` = comp-local time)
| element | text | cue |
|---|---|---|
| held state in on the cut, float starts | sub-row labels, "NIST Impacts page" | 0.00 |
| glass chip lands, centred x 960, y 96 to 166 (clear of the tile top 296) | "2027 BUILDING CODE" | "2027" 0.32 |
| ICC source line on, x 96 baseline 980 (above the NIST line), same style | "2027 International Building Code · ICC store page, Oct 2026" | "2027" 0.32 |
| grey right half of tile 7's border lifts `#93a3b2` → `#c8d3e0` and holds (the open half) | | "tornadoes" 5.58 |
| STORES pulse | | "stores" 8.76 |
| APARTMENTS pulse | | "apartment" 9.64 |
| hold on the last word, then fade-through to the ground | | "buildings." ends 10.36; fade 10.54 to 11.14 |
Longest gap with no new tween: 0.32 to 5.58 (5.26 s) while the voice reads the chip's own sentence; the float carries it.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a, §8. COMPID `g-z1-board`.
