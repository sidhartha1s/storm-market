# g-a6-1-board · A6-S1 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (which points at `briefs/intro/_list.md` "Shared rules"). Exemplars: official `lt-stack-bars`; `episodes/ep-galveston-1900/compositions/g-intro-7-clines.html` (this episode's lower-third); `library/inhouse/bulletin-typewriter.html` (paper sheet ground).

## 0. Claim
After 1900 the city called in a board of three engineers, who drew up a two-part plan (a seawall and raising the city) to keep the water out.

## 1. Source
- Rosenberg Library, "Galveston's Seawall" (sources-a6.md §1): "Brigadier General Henry Martyn Robert, Alfred Noble, and H. C. Ripley, drafted plans for the Seawall and grade raising"; board sat "From September 1901 to January 1902".
- ASCE landmark page (sources-a6.md §1): "A three-member board of engineers" (Henry Martyn Robert, Alfred Noble, Henry Clay Ripley); report presented "on January 25, 1902".
- Robert's Rules of Order: NOT fetched, never on screen.

## 2. Datum, scale, orientation
No measured axis. The sheet is a designed ground: blueprint paper `#0f1d2c` with a 48 px grid of 1 px lines `#5a768f` at opacity 0.18, a 2 px border inset 64 px from each edge `#93a3b2` at opacity 0.35.

## 3. Geometry (px, 1920 x 1080)
- Photo (track 1 under the comp, 0 to 4.40 s): `media/candidates/a6/A6-S1_c1_ruins-searching-for-dead.jpg`, ONE half of the stereo card (crop to the left frame; measure the card's split on the file and state it in the receipt), cover-fit, slow push scale 1.00 to 1.05 `ease:none`.
- Sheet: full-frame div inside the comp, hidden until 3.58, then opacity 0 to 1 over 0.8 s (the ruins fade to the sheet).
- Lower-third (one glass card, intro shared spec, `left:110px; bottom:110px`): three name lines stacked, Arial Black 900 44 px `#f2f5f8`, 10 px apart: "HENRY MARTYN ROBERT", "ALFRED NOBLE", "HENRY CLAY RIPLEY"; then the tag line Arial 700 24 px `#f5d98b` tracking 3: "BOARD OF ENGINEERS · 1901 TO 1902". Card width = longest line + 2 x 32 px padding.
- Sheet items (centred column on x 960, upper half):
  - "1 · SEAWALL" Arial Black 900 64 px `#f2f5f8`, top 230; under it a 600 px wide schematic wall-profile icon (curved face, 90 px tall), 4 px `#7fb2e5` stroke drawn by strokeDashoffset.
  - "2 · RAISE THE CITY" Arial Black 900 64 px `#f2f5f8`, top 470; under it a row of 5 house glyphs (40 x 34 px, `#4a5560`, roof `#93a3b2`) that rise 30 px as a block.
- Chip "REPORT · JAN 25, 1902": glass chip (main line "REPORT", tag "JAN 25, 1902" per the shared chip spec is too small for the date; use one line Arial Black 900 40 px), right edge at x 1824, top 140.
- Source line top-left: "Rosenberg Library · American Society of Civil Engineers".

## 4. Must be true in the picture
1. Exactly three names, in the order Robert, Noble, Ripley, spelled as here; no rank or title added.
2. The tag reads 1901 TO 1902 and the chip JAN 25, 1902: two different facts (board's sitting, report date), never merged.
3. The sheet shows two items only, named as the narration's "two-part plan" (seawall, raising the city). No figures on the sheet (17 ft and 3.3 miles belong to S2).
4. The sheet items and the chip never overlap the lower-third (lower-third top is about y 700; sheet item 2 icon ends about y 600).
5. Three type tiers: 64 px items, 44/40 px names and chip, 24 px tag and source line.

## 5. Text and cues (a6-s1.words.json, 8.617 s; host 0.00 to 8.617)
- 0.00: photo push running; source line in at 0.20.
- 2.26 ("three") /* THREE @2.26 */: lower-third card in; name lines at 2.26, 2.46, 2.66 (fromTo y 18 -> 0, autoAlpha 0 -> 1, 0.4 s); tag at 2.82 (after "engineers" 2.52).
- 3.58 ("They") /* SHEET @3.58 */: sheet fades in over the photo, 0.8 s.
- 4.24 ("two") /* TWO-PART @4.24 */: "1 · SEAWALL" in; its icon draws 4.24 to 4.90.
- 4.70 ("plan"): "2 · RAISE THE CITY" in; houses rise 4.90 to 5.60, back.out.
- 5.20: lower-third out (slide left, 0.6 s).
- 6.02 (after "out." 5.82): chip in.
- 6.68 ("Nobody") /* HOLD? @6.68 */: both sheet icons dim to opacity 0.55; the wall icon stroke pulses opacity 0.55 to 0.9 (sine, 1.2 s yoyo, finite repeats to host end): the open question.

## Motion for the whole window
0 to 4.40 the photo push. After 3.58 the sheet grid drifts x 0 to -40 px over the rest of the host (`ease:none`, 8 px/s). Chips and the lower-third float per shared rules. Something moves in every second.

## Exit
Chip slides out right over the last 0.6 s; the sheet stays to the cut (A6-S2 opens on its own picture).

## Footage under it
`A6-S1_c1_ruins-searching-for-dead.jpg` (picks.md pick; backup `A6-S1_c2_ruins-twisted-house.jpg`) on track 1 from 0 to 4.40; read its `provenance.csv` row before mounting. Presenter circle: may show 0 to 3.58 over the photo; off once the sheet is up (the corner holds the sheet border only, so the orchestrator may keep it after a frame read).
