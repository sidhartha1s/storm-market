# g-a4-15-four-seconds · A4-S9 0 to 20.94 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/then-now-scale.html` (one measured axis), catalog `mk-usage-arc` (the clock arc).

## 0. Claim
At about 7:30 p.m., standing at his partly open front door with about 8 inches of water on his raised floor, Cline saw the water rise about four feet in about four seconds, above his waist before he could move.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 46 to 50; a4-r3.md row 6): "front door, which was partly open, watching the water, which was flowing with great rapidity from east to west"; "about eight inches deep in my residence"; "a sudden rise of about four feet in as many seconds"; "brought it above my waist before I could change my position". Floor well above the ground outside (derived, a4-r3 row 6).

## 2. Datum, scale, orientation
Interior, looking out through the front door; the street (and the flow) beyond the door runs east to west = right to left on screen (stated on screen with a small "E" right / "W" left marker pair at the top of the door frame). Vertical scale 120 px per ft (computed): floor y 940; 8 in = y 860; 8 in + 4 ft = y 380; door 7 ft tall: lintel y 100; figure 5.75 ft: head y 250; waist 3.4 ft: y 532. Note bottom-left "Vertical scale 120 px per ft · house: schematic" Arial 700 19 px `#93a3b2`, left 96, top 1000 (it sits under the water once the rise lands: put it at top 54 right of the source line instead, x 1000, if the frame read shows it covered).

## 3. Geometry (px)
- Room: floorboards `#2a2622` lines on `#15202b`, walls `#0b1016`. Door frame x 760 to 1160, y 100 to 940, `#6b6257` 10 px; door leaf partly open (rotated panel 120 px wide on the hinge side, left).
- Outside through the door: water `#5a768f` with horizontal flow streaks `#7fb2e5` moving right to left (x tweens, 0.8 s loops, finite). Outside surface = inside surface: y 860 before the rise, y 380 after (the outside ground is about 5.33 ft below the floor, off frame; 6 ft of water over it stands 8 in above the floor).
- Inside water: sheet from y 860 to 940 across the room (8 in), `#5a768f` 0.6, ripple.
- Figure (Isaac) silhouette `#93a3b2` standing inside left of the door, x 560 to 660, feet y 940, head y 250; waist tick `#d8a13a` at y 532.
- Doorframe ruler: on the right jamb, ticks every 1 ft from the floor (y 940, 820, 700, 580, 460, 340, 220), labels "1 FT" to "5 FT" Arial 700 22 px `#93a3b2` right of the jamb at x 1180.
- Chip "8 IN" (glass, main Arial Black 900 52 px) on the floor area, left edge 1240, top 820, tag "on his floor".
- Clock: glass card circle r 110 at centre (1460, 330): an arc `#e8c56a` 10 px drawing 360° over 4.0 s with 4 tick marks at 90° steps, and a leaf "4 S" (Arial Black 900 52 px) in its centre counting 1, 2, 3, 4 (four pre-authored leaves toggled by autoAlpha, never text writes).
- Water bar: inside water and outside water rise together from y 860 to y 380 (480 px = 4 ft) over 4.0 s (ease power1.in, a surge: it accelerates).
- Chip "4 FT IN ABOUT 4 SECONDS" (glass), left edge 96, top 130.
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. Rise = 480 px ±4 (4 ft at 120 px/ft) and lasts 4.0 s ±0.05 (receipt: y and time at start and end).
2. After the rise the water surface (y 380) is above the waist tick (y 532).
3. Flow streaks move right to left (east to west) only.
4. The clock's 4 counts land 1.0 s apart in step with the rise.
5. Nothing labelled in x >= 1600, y >= 680 (8 IN chip right edge must stay <= 1600: chip x 1240 to about 1440).

## 5. Text and cues (a4-s9.words.json)
- 0.00 ("so they stayed"): frame 0 shows the room, door, outside water at y 860, flow moving.
- 1.50 ("7") /* 7:30 @1.50 */: no popfig (the clock time is spoken; chip zone stays free).
- 3.92 ("front door") /* DOOR @3.92 */: door leaf swings a little (rotationY-free: scaleX 1 to 0.9, 0.5 s); 5.12 ("partly").
- 6.80 ("current") /* CURRENT @6.80 */: flow streaks speed up x2.
- 12.20 ("8") /* 8 IN @12.20 */: inside water sheet brightens; 8 IN chip in.
- 13.80: 8 IN chip out.
- 14.02 ("Count") /* COUNT @14.02 */: clock in at 14.02, arc draws 14.02 to 18.02, counts 1 at 15.02, 2 at 16.02, 3 at 17.02, 4 at 18.02; water rises 14.02 to 18.02.
- 18.20 ("feet") /* 4 FT @18.20 */: chip in.
- 19.26 ("above") /* WAIST @19.76 */: waist tick flashes red `#d0121f` at 19.76.
- 20.94 segment end; land time to the cut.

## Motion for the whole window
Flow streaks throughout; ripple; clock arc 14.02 to 18.02.

## Exit
Chips slide out `x:980` in the last 0.6 s; cut to g-a4-16.

## Footage under it
None: full-frame cutaway (A4-S9_c1 rejected: modern traffic).
