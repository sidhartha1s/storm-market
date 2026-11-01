# g-a4-16-tide · A4-S10 0 to 25.04 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (HOUSE PLATE). Base: `compositions/g-a4-11-house-40.html`; 8.7 ft bracket style from `compositions/g-intro-6-island.html`.

## 0. Claim
On ground 5.2 ft above sea level, the water at Cline's house stood 10 ft above the ground (15.2 ft) by 7:30 p.m. and nearly 5 ft higher an hour later: a tide of about 20 ft, more than twice the island's highest ground (8.7 ft).

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 51, 52; a4-r2.md rows 9 to 13; a4-r4.md row 2): "a stage 10 feet above the ground ... The ground was 5.2 feet elevation, which made the tide 15.2 feet"; "between 7:30 and 8:30 p. m., nearly five feet additional, making a total tide in that locality of about twenty feet"; "on the bay or north side of the city did not obtain a height of more than 15 feet" (a4-r3.md row 2). 8.7 ft: NPS (sources-cline.md §5; a1-r1.md row 27). 1891 "spread over the low land to the north": a4-r3.md row 1. 8.7 / 20 = 0.435 (python3, 28 Oct 26).

## 2. Datum, scale, orientation
HOUSE PLATE: sea level y 960, 30 px per ft: ground 5.2 ft y 804; 8.7 ft y 699; 15.2 ft y 504; 20 ft y 360. Elevation axis on the left at x 300: ticks every 5 ft (0 at y 960, 5 at y 810, 10 at y 660, 15 at y 510, 20 at y 360) with labels "0", "5", "10", "15", "20 FT" Arial 700 22 px `#93a3b2` left of the axis (right-aligned to x 286). Axis title "Feet above sea level" at left 96, top 300.

## 3. Geometry (px)
- Plate as g-a4-11 at night (windows dark); water starts at y 624 (6 ft above ground, the 7:30 pre-rise level).
- Ground line chip (glass, main Arial Black 900 52 px) "5.2 FT ELEVATION", left edge 360, top 830 (below the ground line, over the ground band), with a `#d8a13a` 2 px tick to the ground line at x 600.
- 10 FT bracket: vertical `#d8a13a` 3 px at x 1300 from y 804 (ground) to y 504 (10 ft above ground), end ticks 30 px; label "10 FT ABOVE THE GROUND" Arial 700 30 px `#f2f5f8` (mid tier; 52 px would run past x 1824) on a small glass card at left 1330, top 610; axis value "15.2 FT" Arial Black 900 52 px `#d8a13a` at the axis, left 120, top 474 (beside the 15 tick: shift the "15" tick label off while 15.2 shows; `data-repeat-ok` not needed: different text).
- Water surface rises: y 504 (15.2 ft) then to y 360 (about 20 ft); the water covers the floor and climbs the house walls; windows go under in turn.
- 20 FT label: "ABOUT 20 FT" Arial Black 900 52 px `#f2f5f8` on a glass chip, left edge 1330, top 280, tag "his report, at his house".
- 8.7 ft line: dashed `#93a3b2` 3 px across x 300 to 1824 at y 699 (drawn left to right), label "ISLAND'S HIGHEST POINT 8.7 FT" Arial 700 26 px `#f2f5f8` at left 1300, top 712 under the line (it is under water then: put it on a small glass card so it reads through water). Measure brackets: a `#93a3b2` bracket x 1700 from y 960 to y 699 beside a `#d8a13a` bracket x 1760 from y 960 to y 360, so the two heights compare side by side (no text in the corner: the brackets are lines; circle off for this window if lines in the corner count, orchestrator).
- Chip "BAY SIDE · NO MORE THAN 15 FT", tag "Cline's report, p. 373", left edge 360, top 130 (in during the 1891 sentence, see cues).
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373; National Park Service".

## 4. Must be true in the picture
1. Heights on the plate within ±2 px: ground y 804, 15.2 ft y 504, 20 ft y 360, 8.7 ft y 699 (receipt measures each).
2. The 20 ft water bracket is 2.30x the 8.7 ft bracket from sea level (600 px vs 261 px).
3. "15.2 FT" appears only as an axis value, never as a second chip; "10 FT ABOVE THE GROUND" and "ABOUT 20 FT" never on screen with the bay-side chip.
4. The bay-side 15 ft is never drawn as a line on this house's water (it is another part of the city): chip only.
5. Nothing labelled in x >= 1600, y >= 680.

## 5. Text and cues (a4-s10.words.json)
- 0.00 ("Remember") /* GROUND @0.42 */: frame 0 shows the night plate and axis, water at y 624 (6 ft above ground, the 7:30 pre-rise level); ground tick and chip in at 0.42 ("ground"), chip settles by 2.06 ("5").
- 4.16 ("By") /* 7:30 @4.32 */: ground chip out; water jumps y 624 to y 504 (4.32 to 4.80, power3.out: the 4 ft rise); 6.48 ("10") /* 10 FT @6.48 */: bracket draws, label in; 15.2 FT axis value in at 7.70 ("ground").
- 8.54 ("An hour later") /* NEARLY 5 @9.88 */: bracket label out; water climbs y 504 to y 360 (9.24 to 10.54, steady).
- 11.62 ("Klein had said") /* NORTH @14.60 */: bay-side chip in at 13.36 ("over"), out at 16.28 ("hold").
- 17.06 ("By his own report") /* 20 @19.70 */: ABOUT 20 FT chip in at 19.70; orange bracket draws 19.70 to 20.40.
- 21.08 ("The highest") /* 8.7 @21.54 */: 8.7 ft line draws 21.54 to 22.24; label in at 22.24; grey bracket draws 23.68 ("less") to 24.24 ("half").
- 25.04 segment end; land time to the cut.

## Motion for the whole window
Water surface ripple throughout; windows going under flicker out; a slow 1.00 to 1.04 pull-out across the window (linear, small).

## Exit
Chips slide out `x:980` in the last 0.6 s; cut to A4-S11.

## Footage under it
None: full-frame cutaway.
