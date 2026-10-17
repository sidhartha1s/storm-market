# BRIEF · g-z1-board · "watch whether it asks for shelters in stores and apartment buildings" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, segment Z1-S3. Full-frame MG on the channel ground. Host from the z1-s3 start to the z1-s3 wav end + 0.6 s.
It comes in on a cut from `g-z1-map`; the signature line (Paul full frame) follows on a cut.
Base: the recommendation board (`briefs/a5/g-a5-recs-board.md`) in the state `g-a6-board-half` holds before its exit: board dim at
0.25, tile 7 lifted to 2.4x at centre (960, 500), Amber 1 left half border and grey right half, numeral "7" top right, the four
sub-rows (APARTMENTS, STORES grey; SCHOOLS lit with its tick; ASSEMBLY grey). Copy `compositions/g-a6-board-half.html` and drop its
chip, its exit and its pulses. Build after `g-a6-board-half` passes its frame read.
Open numbers and items: **Z1** (all "2027" text: chip "2027 BUILDING CODE" and source line "2027 International Building Code · ICC store
page, Oct 2026"; no facts.md row, edit_script carries `[verify]`). Not drawn; the chip zone stays empty. **Z2**: `audio/z1-s3.words.json`
does not exist yet, so every cue below names its word from the script and its time is filled from words.json once Z1-S3 is voiced.

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
3. No "2027" and no ICC text anywhere until Z1 has a facts.md row; the chip zone is empty.
4. No tile other than 7 is lit; nothing in x ≥ 1600, y ≥ 680.

## 5. PANEL TEXT (exact) and CUES (z1-s3; times OPEN, Z2)
| element | text | cue (script word; time from z1-s3.words.json) |
|---|---|---|
| held state in on the cut, float starts | sub-row labels, "NIST Impacts page" | z1-s3 0.00 |
| (chip HELD, Z1) | ("2027 BUILDING CODE") | "Code" (first sentence), OPEN |
| STORES pulse | | "stores", OPEN |
| APARTMENTS pulse | | "apartment", OPEN |
| hold, then fade-through | | wav end − 0.0 to wav end + 0.6, OPEN |
Once the cue times exist, check the longest gap with no new tween is under 4 s; the float carries the hold.
When Z1 clears, the chip lands on the word "2027" as whisper spells it (digits), glass chip centred x 960, y 96 to 166 (clear of the tile top 296).

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a, §8. COMPID `g-z1-board`.
