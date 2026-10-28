# g-a4-8-compass · A4-S5 0 to 8.20 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-a3-12-330.html` (p. 373 panel), `compositions/g-a3-9-swell.html` (the WIND arrow style).

## 0. Claim
Cline's report says the public was warned by telephone and in person that the wind would go by the east to the south and that the worst was yet to come.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 21, 22): "The public was warned, over the telephone and verbally"; "the wind would go by the east to the south and that the worst was yet to come". Start direction north: A3-S8's WIND: NORTH (the report's morning wind, factcheck/a3 rows used by g-a3-9) and the telegram's "opposing winds".

## 2. Datum, scale, orientation
Full-frame comp on the tokens gradient. Page panel left (x 140 to 820, y 180 to 940); compass right, centre (1300, 540), r 220, north up. Wind arrow convention: the arrow shows where the wind COMES FROM (meteorological), drawn from the rim toward the centre; label "Wind from" under the compass says so.

## 3. Geometry (px)
- Page panel: glass card, p. 373 crop around the warning paragraph (whole lines, measured), amber band behind "warned, over the telephone and verbally" then extended to "the worst was yet to come".
- Compass: ring `#5a768f` 4 px, cardinal letters N, E, S, W Arial Black 900 52 px `#f2f5f8` at r 270 (N at (1300, 220), E at (1570, 540), S at (1300, 860), W at (1030, 540)); 8 ticks.
- Wind arrow: `#7fb2e5` 10 px shaft from the rim to 40 px short of the centre, head 36 px; it rotates about the centre: N (0°) to E (90°) to S (180°), clockwise via east. A faint 6 px `#7fb2e5` arc at r 240 traces the swing path (strokeDashoffset).
- Label "Wind from" Arial 700 22 px `#93a3b2` tracking 3 centred at (1300, 920)? No: S letter sits at y 860; put "Wind from" at top 950 centred x 1300 (bottom 980 < 1026).
- Chip (glass, main Arial Black 900 52 px) "THE WORST WAS YET TO COME", centred x 1300, top 100 (above N at 220: chip bottom about 210; move N letter to r 250 if tight: receipt), tag "Cline's report, p. 373".
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. The arrow passes through east on its way to south (never swings via west).
2. The arrow starts at north and ends at south ±1°.
3. The chip quotes the report's words exactly ("the worst was yet to come").
4. Chip and the N letter do not touch; nothing in x >= 1600, y >= 680 (E letter right edge about 1600 at y 540: above 680, fine).

## 5. Text and cues (a4-s5.words.json)
- 0.00: frame 0 shows the page panel and compass with the arrow at N; source line on.
- 0.12 ("report") /* REPORT @0.12 */: band draws on "warned, over the telephone and verbally" (0.12 to 1.26); 1.74 ("telephone") and 2.66 ("person") pulse the band.
- 4.44 ("swing") /* SWING @4.44 */: arrow N to E (4.44 to 5.12, "east" at 5.12), E to S (5.12 to 5.60, "south" 5.60), power2.inOut; arc trace follows.
- 6.58 ("worst") /* WORST @6.58 */: chip in.
- 7.38 ("come") to 8.20: band extends over the worst-to-come line; at 7.60 chip and panel exit begin.

## Motion for the whole window
Arrow swing, then a ±2° gust wobble every 1.2 s; page panel push 1.00 to 1.03.

## Exit
Chip slides out `x:980`, 7.60 to 8.20; cut to g-a4-9's map at 8.20.

## Footage under it
None; MWR p. 373 scan inside the comp (A4-S1_c1, verified Y).
