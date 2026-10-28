# g-a4-11-house-40 · A4-S7 0 to 8.86 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (HOUSE PLATE is defined there; this comp is its base: send it alone for a full-size read before g-a4-13, 16, 18 copy it). Exemplars: `compositions/g-intro-6-island.html` (sea-level datum, measured bracket), `ep6-katrina-2005/compositions/g-surge-ms.html`.

## 0. Claim
When Cline got home the water around his house was waist deep, and he brought in people who were not safely sheltered until forty or fifty were inside.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 32 to 34): "found the water around my residence waist deep. I at once went to work assisting people, who were not securely located, into my residence, until forty or fifty persons were housed therein." Ground 5.2 ft (p. 373). Floor 5.33 ft above ground: derived (factcheck/a4-r3.md row 6). House form and person height: drawing conventions, SCHEMATIC.

## 2. Datum, scale, orientation
HOUSE PLATE (`_list.md`): sea level y 960, 30 px per ft, ground y 804, floor y 644, house body x 760 to 1240, eave y 104, ridge y 60, steps and door on the left wall at x 760, gate at x 560. Waist-deep water for a 5.75 ft figure standing on the ground: water surface at ground + 3.4 ft = 8.6 ft = y 702 (computed).

## 3. Geometry (px)
- Ground band y 804 to 960 `#15202b`; sea-level datum line y 960 dashed `#5a768f`, label "Sea level" Arial 700 22 px `#93a3b2` at left 110, top 920.
- House: walls `#0b1016` with `#93a3b2` 3 px outline, piers under the floor x 780 to 1220 every 110 px from y 644 to 804, two window rows (lit `#e8c56a` at 0.6), roof to the ridge. Front steps from (700, 804) up to the door sill (760, 644). Door 60 x 210 at x 760 to 820, y 434 to 644.
- Water: fill from y 702 to 804 across x 96 to 1824 (behind the piers, in front of the ground), `#5a768f` 0.75, rippling surface line.
- Figure (Isaac) at the gate, feet on y 804, head y 632 (172 px), x 540 to 580; waist mark: a 2 px `#d8a13a` tick at y 702 on the figure.
- Filing figures: 10 silhouettes (same 172 px, `#4a5560`) wading from x 120 toward the steps, each climbing the steps and passing through the door (autoAlpha 0 at the door), staggered 0.45 s; a small door glow when each enters.
- Counter: chip (glass, main Arial Black 900 52 px) "40 TO 50", tag "people inside · his report", right edge 1824, top 130 (above the eave; chip box x about 1450 to 1824, y 130 to 240, clear of the roof at x <= 1240).
- Chip 0 (same spot, earlier) "WAIST DEEP", tag "around his house".
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373". Note bottom-left per plate.

## 4. Must be true in the picture
1. Ground line at y 804 and water surface at y 702 ±2 px (receipt measures both).
2. The water surface hits the figure's waist tick (within 4 px).
3. Floor (y 644) is above the water: the house interior stays dry in this comp.
4. "40 TO 50" is text, not a count-up through numbers (no precise count is claimed).
5. Nothing labelled in x >= 1600, y >= 680 (water there is unlabelled; circle per orchestrator).

## 5. Text and cues (a4-s7.words.json)
- 0.00 ("At home"): frame 0 shows datum, ground, house, water already at y 702, figure at the gate.
- 1.62 ("water") /* WAIST @2.52 */: chip 0 in at 2.52 ("waist"); tick pulses.
- 3.60 ("He started"): chip 0 out by 3.94; figures start filing at 3.94 ("bringing").
- 6.62 ("40") /* 40 TO 50 @6.62 */: chip "40 TO 50" in; filing continues to 7.84 ("inside"), last figure enters at 7.84.
- 8.26 to 8.86: chip exits.

## Motion for the whole window
Water ripple (1.2 s period), filing figures, window flicker; nothing idle.

## Exit
Chip slides out `x:980, 0.6, power3.in` 8.26 to 8.86; cut to g-a4-12.

## Footage under it
None: full-frame cutaway.
