# g-a2-1-straits · A2-S1 0.00 to 5.32 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (map, placement, contract). Exemplar: `compositions/g-intro-4-wire-map.html`: copy its plate (BASEMAP block), projection, camera function and pin markup into this file; do not edit g-intro-4.

## 0. Claim
Havana sits across the water from Galveston, about a hundred miles south of Key West. The viewer leaves the Galveston pin from the hook and lands on Havana.

## 1. Source
- Distance: factcheck/a2-r1.md rows 1 and 2: Wikipedia Straits of Florida, "to cover the 106 miles (171 km) between Havana and Key West"; chip reads ABOUT 100 MILES (row 2, corrected from 90).
- Havana, Belen: sources-cuba.md §1 (NOAA AOML 2015). Positions: the plate formula (no figure traced; the basemap is Natural Earth, as g-intro-4).

## 2. Datum, scale, orientation
- Plate and formula: `_list.md` "The shared map". North up. Points used: Galveston (468.0, 1216.2), Havana (1585.8, 1857.6), Key West (1639.8, 1708.9).
- Camera states (screen points computed by script, 28 Oct 26):
  - V-GAL: cx 700, cy 1300, s 0.9. Galveston at screen (751, 465). Havana is off screen (1757, 1042).
  - V-STR: cx 1500, cy 1700, s 1.2. Havana (1063, 729), Key West (1128, 551). Galveston off screen left (-278, 360).
- V-GAL to V-STR is 1.33x: a plain tween on cx, cy, s is fine (under 1.5x), ease power2.inOut.

## 3. Geometry (screen px)
- Pins as Shared rules: Galveston `#f2f5f8`, Havana `#d8a13a`, Key West `#f2f5f8` at 10 px (a reference town, smaller, no pulse).
- Galveston label (V-GAL only): "Galveston" Arial Black 900 40 px `#f2f5f8`, right edge x 735, baseline y 477.
- Havana label (V-STR, HUD): "Havana, Cuba" Arial 700 30 px `#e8c56a`, left x 1090, baseline y 742.
- Key West label (V-STR, HUD): "Key West" Arial 700 26 px `#93a3b2` tracking 2, left x 1150, baseline y 560.
- Bracket: a straight line from the Havana pin to the Key West pin (plate length 158.2 px, 190 px on screen at s 1.2), `#f2f5f8` 3 px, 14 px end ticks square to the line, drawn by strokeDashoffset from ceil(len)+1. It lives in the camera layer (plate units) so it stays on both pins.
- Chip "ABOUT 100 MILES" (no tag line), glass card, right edge at x 1020, vertical centre y 640 (left of the bracket, clear of both labels). The chip is on the HUD; it enters only after the camera has settled.
- Source line (top-left): "NOAA AOML, 2015 · Self-made map".

## 4. Must be true in the picture
1. Every pin sits on its formula point within 10 px in both camera states; the receipt lists the three plate points and a frame of each.
2. The bracket starts on the Havana dot and ends on the Key West dot (within 6 px) in every frame after it is drawn.
3. Havana is south of Key West on screen (y larger) and Galveston is north-west of both: the map is north up, no rotation.
4. Nothing enters x >= 1600, y >= 680 in any frame (Havana at V-GAL is off screen; its pin is hidden until 1.76 and appears only once on screen inside x < 1600).
5. No label rides the pan: Galveston's label fades out before the pan moves it 10 px; Havana and Key West labels enter after the camera settles at 2.62.
6. The chip names a distance only: no scale bar, no second figure.

## 5. Text and cues (a2-s1.words.json)
- 0.00: plate in V-GAL, fully drawn, Galveston pin pulsing and its label on (frame 0 is the map, no dark frame after the act's chapter card). Source line in at 0.00.
- 0.16 ("cross" 0.16): Galveston label fades out 0.16 to 0.46; camera pans V-GAL to V-STR 0.16 to 2.62, power2.inOut. /* CROSS @0.16 */
- 1.76 ("Havana," 1.76) /* HAVANA @1.76 */: Havana pin drops in (y -30 to 0, back.out) at its moving camera point and starts pulsing; Key West dot fades in at 1.76 too (no label yet).
- 2.62 ("about" 2.62): camera settled; "Havana, Cuba" label in (autoAlpha 0 to 1, x -12 to 0, 0.35 s).
- 2.88 ("hundred" 2.88): bracket draws 2.88 to 3.40, power2.out.
- 3.14 ("miles" 3.14) /* MILES @3.14 */: chip ABOUT 100 MILES enters.
- 4.02 ("Key" 4.02): "Key West" label in.
- 4.18 to 5.32: hold; camera drifts s 1.2 to 1.23 (ease none) so something moves.
- Host: A2-S1 0.00 to 5.32 (comp duration 5.32).

## Motion for the whole window
Pan 0.16 to 2.62, pin pulses throughout, bracket draw, drift 4.18 to 5.32. No gap reaches 4 s.

## Exit
Cut to the Belen engraving at 5.32 ("Jesuit"): the last 0.35 s (4.97 to 5.32) fades the whole root to 0 (fade-through, mg-quickref "Exits"). The chip does not slide out first.

## Footage under it
None: full-frame designed map (coverage 100 %).
