# g-a4-7-strand · A4-S4 8.70 to 18.96 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-a3-10-1875.html` (schematic building drawing), `library/inhouse/then-now-scale.html` (one measured axis).

## 0. Claim
Cline went to Strand Street and advised wholesale merchants to lift their goods three feet off the floor; one told him he had, and the wind blew his goods down anyway.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 18 to 20): "went down on Strand street and advised some wholesale commission merchants who had perishable goods on their floors ... to place them 3 feet above the floor. One gentleman has informed me that he carried out my instructions, but the wind blew his goods down." Building: SCHEMATIC (no pre-storm Strand photo, picks.md).

## 2. Datum, scale, orientation
Full-frame drawing, interior wall of a commission house, face on. Floor = y 880, x 96 to 1824. Vertical scale 80 px per ft for the 3 ft line: 3 ft = 240 px, line at y 640 (computed). Note bottom-left "Building: schematic · 80 px per ft" Arial 700 19 px `#93a3b2`, left 96, top 1000.

## 3. Geometry (px)
- Wall `#15202b`, brick courses as 1 px `#2a3644` lines; two tall arched windows (x 300 to 460, x 1360 to 1520, y 260 to 620).
- Goods: a stack of 6 crates (each 120 x 80 px, `#8e2020` sides with `#d8a13a` slat lines) and 4 sacks, starting on the floor (crate bottoms y 880), at x 620 to 1100.
- Platform: trestles that rise with the goods; at the cue the whole stack and a plank platform move up 240 px (y -240) so crate bottoms sit on y 640.
- 3 FT line: dashed `#d8a13a` 3 px across x 560 to 1160 at y 640; vertical measure bracket at x 1200 from y 880 to y 640 with end ticks; label "3 FT" Arial Black 900 52 px `#d8a13a` right of the bracket at (1230, 730).
- Label "Strand Street" as a chip (glass, main Arial Black 900 52 px) "STRAND STREET", left edge 96, top 140, tag "wholesale merchants".
- Tip: on the last beat the top three crates rotate and fall left (rotation to -35°/-60°, x -120, y +240, 0.7 s, power2.in), one sack slides; dust puffs `#93a3b2` opacity 0.4.
- Wind cue: 6 thin `#c8d3e0` streak lines (opacity 0.5) cross from the right window leftward at the tip.
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. After the lift, crate bottoms sit on the 3 FT line within 2 px (240 px above the floor).
2. "3 FT" label never overlaps the bracket or crates.
3. The stack tips after the voice says "wind" (17.48), not before.
4. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a4-s4.words.json, comp-local = word time - 8.70)
- 8.70 ("Isaac") /* STRAND @9.48 */: frame 0 shows the wall and goods on the floor; chip in at 9.48 ("Strand").
- 12.14 ("advised"): chip out by 12.60.
- 13.18 ("lift") /* LIFT @13.18 */: stack and platform rise 240 px (13.18 to 14.18, power2.inOut); 13.84 ("three") 3 FT line draws, bracket and label in at 14.18 ("feet").
- 16.54 ("had"): label pulses once.
- 17.48 ("wind") /* WIND @17.48 */: streaks; 17.70 ("blew") crates tip (to 18.40); dust.
- 18.96 segment end; land time to the cut.

## Motion for the whole window
Dust motes drift in the window light (6 dots, y float); after the lift the stack sways ±1° every 1.2 s until the tip.

## Exit
Cut to g-a4-8's page; the 3 FT label and line fade 0.4 s at the end (not a hard vanish: the cut follows).

## Footage under it
None: full-frame drawing (A4-S4_c1 is aftermath, rejected by the verifier).
