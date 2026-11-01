# g-a3-5-barometer · A3-S4 8.06 to 14.20 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `library/inhouse/numbers-rollup.html` (stacking readings). A measured dial: the needle angle is computed from the reading, never placed by eye.

## 0. Claim
Captain Halsey's barometer fell: 29.87, then 29.60 at 6 a.m., 29.25 at 10 a.m., and 28.75 inches at 1 p.m. on September 6 (his own reading, no correction given).

## 1. Source
MWR Sept 1900 p. 374 (factcheck/a3-r1.md rows 15, 48): readings 29.87 (no hour given), 29.60 at 6 a.m., 29.25 at 10 a.m., "at 1 p. m. the barometer had fallen to the remarkable figure of 28.75". The reading is the captain's; keep it attributed (source line).

## 2. Datum, scale, orientation
- Full-frame designed dial on the root background (tokens.md radial gradient).
- Dial centre (760, 560), radius 330. Scale 28.50 to 30.50 in, 270° sweep, clockwise increasing: angle(p) = -225° + (p - 28.50) * 135° (0° = 3 o'clock, positive clockwise in screen space). So 28.50 at -225° (lower left), 30.50 at +45° (lower right).
- Needle angles (checked by formula): 29.87 = -40.05°; 29.60 = -76.50°; 29.25 = -123.75°; 28.75 = -191.25°.

## 3. Geometry
- Dial face: circle r 330, fill `#0b1016`, rim `#5a768f` 4 px. Ticks every 0.10 in (21 ticks), majors every 0.50 (28.5, 29.0, 29.5, 30.0, 30.5) 28 px long with labels Arial 700 26 px `#93a3b2` at radius 270; minors 14 px.
- Needle: `#f2f5f8` 6 px, length 290, hub 22 px `#d8a13a`. Rotation by GSAP `rotation` on a group whose transform-origin is the centre.
- Unit "INCHES" Arial 700 22 px `#93a3b2` tracking 4 centred at (760, 700).
- Reading stack (right column, left edge x 1180): rows 76 px apart from top 300, each one glass card 520 x 64: reading Arial Black 900 44 px `#f2f5f8` and hour Arial 700 24 px `#93a3b2` right-aligned in the card: "29.87" (no hour), "29.60 · 6 AM", "29.25 · 10 AM", "28.75 · 1 PM". The last row's reading turns `#d0121f`.
- Column bottom: 300 + 3*76 + 64 = 592 < 680; right edge 1700 is above y 680: fine.
- Source line top-left: "Captain Halsey, in Monthly Weather Review, September 1900, p. 374".

## 4. Must be true in the picture
1. Needle angle at each landed reading within 1° of the formula (receipt lists the four angles and a frame per landing).
2. Readings appear in Halsey's order and never skip ahead of the needle: a row lands only when the needle reaches it.
3. No date label beyond the hours (the voice carries "the next afternoon").
4. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a3-s4.words.json; comp-local = word time - 8.06)
- 8.06 ("Then") /* THEN @8.06 */: dial on (cut lands on a finished dial), needle at 29.87, row 1 in.
- 9.00 ("barometer"): needle shivers ±1°.
- 10.04 ("fall") /* FALL @10.04 */: needle to 29.60 (10.04 to 10.60), row 2; to 29.25 (10.76 to 11.38), row 3.
- 12.52 ("28") /* 28.75 @12.52 */: needle to 28.75 (12.52 to 13.30, power2.out), row 4 lands at 13.02 (".75"), red at 13.30.
- Host 8.06 to 14.20 plus land time to the cut (cap 15.2).

## Motion for the whole window
Needle always settling or shivering; cards drift.

## Exit
Cut to A3-S5's sea footage: cards slide out `x:980` in the last 0.6 s.

## Footage under it
None: full-frame designed dial.
