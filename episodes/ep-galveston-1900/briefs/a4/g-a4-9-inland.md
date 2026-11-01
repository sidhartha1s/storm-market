# g-a4-9-inland · A4-S5 8.20 to 15.12 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (ISLAND PLATE). Base: `compositions/g-a4-2-half-city.html` (copy its plate: projection, polygon, grid, pin; drop its flood fill, buggy and chips).

## 0. Claim
Thousands near the beach or in small houses moved their families into the centre of the city; Cline's own family stayed home.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 23 to 25): "thousands of people who lived near the beach or in small houses moved their families into the center of the city"; house at "Rosenberg avenue (Twenty-fifth street) and Q street". "Stayed home": inference from the report (row 24; A3-S10). Dot count and paths: SCHEMATIC, no number on screen.

## 2. Datum, scale, orientation
Island plate exactly as g-a4-2 (north up, Gulf at the bottom, grid x 320 to 1600, y 324 to 824, rows from the Gulf). "Centre of the city" = rows 4 and 5 (y 410 to 566), columns 4 to 9 (x 644 to 1276): an amber outline `#d8a13a` 3 px box, label "City centre" Arial 700 26 px `#f2f5f8` inside the box at its top-left (660, 420).

## 3. Geometry (px)
- Family dots: 30 dots, 10 px `#f2f5f8`, starting in rows 1 and 2 (the beach blocks, y 668 to 824) spread across all 12 columns; each moves along the streets (first up the nearest north-south street, then across) into the centre box. Paths are 2-leg `x`/`y` tweens (no MotionPathPlugin). Staggered 0.08 s.
- Faint trails `#93a3b2` 1 px dashed behind 8 of the dots.
- Cline pin: g-a4-2's pin at (1014, 617) (row 3, outside the centre box: it is not inside rows 4 and 5, so "stayed home" reads as the one that did not move), label "25th St & Q". A ring pulse on it at "stayed".
- Chip (glass, main Arial Black 900 52 px) "THOUSANDS MOVED INLAND", left edge 96, top 130, tag "from the beach blocks · p. 373".
- Second chip (same zone after the first exits) "ISAAC'S FAMILY STAYED HOME", tag "25th St & Q".
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. No dot starts inside the centre box; every moving dot ends inside it.
2. The Cline pin never moves.
3. No number on screen (no count in the source beyond "thousands").
4. Chips one at a time; pin label not covered by a dot at rest (dots end inside the centre box, which excludes row 3).

## 5. Text and cues (a4-s5.words.json, comp-local = word time - 8.20)
- 8.20 ("Thousands") /* THOUSANDS @8.20 */: frame 0 shows the plate with the 30 dots in the beach rows and the pin; chip 1 in at 8.20.
- 8.94 ("beach"): beach rows tint `#7fb2e5` at 0.2.
- 10.56 ("moved") /* MOVED @10.56 */: dots travel to the centre (10.56 to 12.66, power2.inOut, stagger); centre box outlines at 12.26 ("center").
- 13.10: chip 1 out.
- 13.62 ("Isaac's") /* STAYED @14.50 */: chip 2 in at 13.62; pin ring pulses at 14.50 ("stayed") and every 1.2 s after.
- 15.12 segment end; land time to the cut.

## Motion for the whole window
Dots move 10.56 to 12.66; before and after, all dots breathe (scale 1 to 1.2, 1.2 s yoyo, staggered); water ripple from the plate.

## Exit
Chip 2 slides out `x:980` in the last 0.6 s; cut to A4-S6's rain footage.

## Footage under it
None: full-frame map.
