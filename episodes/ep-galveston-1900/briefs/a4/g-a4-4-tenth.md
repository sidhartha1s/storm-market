# g-a4-4-tenth · A4-S2 6.90 to 11.14 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `compositions/g-a3-5-barometer.html` (the same measured dial: copy its face, needle and 135° per inch scale; this is a family member, so the viewer recognises the instrument).

## 0. Claim
At the office the barometer stood only one-tenth of an inch lower than at the 8 p.m. reading the night before: almost no fall.

## 1. Source
MWR Sept 1900 p. 372 (factcheck/a4-r1.md rows 8, 10): "barometer was only one-tenth of an inch lower than it was at the 8 p.m. observation of the 7th". No absolute reading for either time is in research: the dial shows the difference only.

## 2. Datum, scale, orientation
- Full-frame dial on the tokens gradient. Dial centre (760, 560), r 330, 270° sweep, 135° per inch (g-a3-5's scale). 0.1 in = 13.5° (computed).
- Reference mark "8 PM FRI" at angle -90° (12 o'clock, a neutral placement since no absolute value is claimed); needle lands 13.5° anticlockwise of it, at -103.5°.
- The dial face carries ticks every 0.1 in (13.5° apart) but NO inch numerals (Change 2 in `_list.md`).

## 3. Geometry (px)
- Face `#0b1016`, rim `#5a768f` 4 px, 21 ticks every 13.5° across the 270° sweep, majors every 5th tick 28 px, minors 14 px, `#93a3b2`.
- Reference mark: amber `#d8a13a` triangle 18 px outside the rim at -90°, label "8 PM FRI" Arial 700 26 px `#d8a13a` outside it at (760, 196).
- Needle `#f2f5f8` 6 px, length 290, hub 22 px `#d8a13a`; rotates on a group with transform-origin at the centre.
- Second mark at -103.5°: `#f2f5f8` triangle, label "5 AM SAT" Arial 700 26 px `#f2f5f8` placed outside the rim up-left at about (560, 210) so it does not touch "8 PM FRI" (labels at least 40 px apart; receipt gives both boxes).
- A small bracket arc `#e74c3c` 4 px on the rim between the two marks, radius 350, drawn by strokeDashoffset.
- Chip (glass, main Arial Black 900 52 px) "ONLY 0.1 IN LOWER", left edge 1180, top 420, tag "than 8 PM the night before" Arial 700 22 px `#93a3b2`.
- Unit "BAROMETER" Arial 700 22 px `#93a3b2` tracking 4 centred at (760, 700).
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 372".

## 4. Must be true in the picture
1. The needle's travel is 13.5° ±0.5° (receipt prints both angles).
2. No inch number anywhere on the dial.
3. The fall reads as tiny: the needle moves slowly and stops; no shiver larger than ±0.5°.
4. Nothing in x >= 1600, y >= 680 (chip right edge 1180 + ~560 = 1740 at bottom about 530: above 680, fine).

## 5. Text and cues (a4-s2.words.json, comp-local = word time - 6.90)
- 6.90 ("At") /* OFFICE @6.90 */: frame 0 shows the dial, the 8 PM FRI mark, needle on it.
- 7.98 ("barometer") /* BAROMETER @7.98 */: needle creeps from -90° to -103.5° (7.98 to 9.30, power1.inOut); 5 AM SAT mark and label in at 9.24 ("tenth").
- 9.24 ("tenth") /* TENTH @9.24 */: bracket arc draws (0.5 s).
- 10.02 ("lower") /* LOWER @10.02 */: chip in.
- 11.14 segment end; land time to the cut.

## Motion for the whole window
Needle creep, then a ±0.3° settle wobble every 1.2 s; chip float.

## Exit
Chip slides out `x:980` in the last 0.6 s; cut to A4-S3's page.

## Footage under it
None: full-frame dial.
