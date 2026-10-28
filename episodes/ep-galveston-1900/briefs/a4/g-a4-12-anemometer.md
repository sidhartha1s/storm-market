# g-a4-12-anemometer · A4-S7 8.86 to 19.26 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: catalog `mk-usage-arc` (spin with a count), `beat-accent` (one impact sting).

## 0. Claim
At 6:15 p.m. the office anemometer recorded 84 mph (the greatest five-minute velocity), then blew away; Cline estimated the wind reached at least 120 mph before 8 p.m.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 35 to 37, 39): "The greatest velocity for five minutes was 84 miles per hour at 6:15 p. m. ... The anemometer blew away at this time, and it is estimated that prior to 8 p. m. the wind attained a velocity of at least 120 miles per hour."

## 2. Datum, scale, orientation
Full-frame drawing on a dusk gradient (tokens gradient with `#15202b` top): the office roof line across the bottom (y 820, x 96 to 1824), anemometer mast centred x 760 from y 820 up to y 420, cup rotor at the top (hub (760, 400)), seen from slightly below (rotor ellipse 260 x 70 px). Rain streaks diagonal.

## 3. Geometry (px)
- Mast `#93a3b2` 8 px; rotor: 4 arms, 4 cups (hemispheres 44 px, `#dfe7ee` outline), arms rotate as a group (rotation on the projected ellipse: animate each cup's x along the ellipse via attr tweens per quarter, or use a top-down rotor on a flat disc: builder's choice, stated in receipt).
- Spin rate: 1 rev per 0.6 s to 6.15 s cue, then 1 rev per 0.35 s.
- Tear-off: rotor detaches (x +900, y -300, rotation 540°, 0.9 s, power2.in) and leaves the frame on the right ABOVE y 680; mast whips (rotation ±6°, 3 cycles) and remains bare.
- Chip C1 (glass, main Arial Black 900 52 px) "84 MPH · 6:15 PM", tag "five-minute record", left edge 1180, top 200.
- Chip C2 same spot after C1 leaves: "AT LEAST 120 MPH", tag "Cline's estimate, before 8 PM".
- Rain: 40 streaks `#c8d3e0` opacity 0.35, slanting left to right, looping finite repeats.
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. C1 is on screen only while the rotor exists; C2 only after it is gone.
2. 120 never appears with a gauge reading look (it is an estimate: tag says so).
3. The rotor's path out stays above y 680 on the right (corner).
4. Chips do not cover the rotor at any point of its flight (rotor path y 100 to 400 passes chip zone x 1180+: start the throw upward to y 100 by x 1100, so it clears the chip top at 200; receipt shows the frame).

## 5. Text and cues (a4-s7.words.json, comp-local = word time - 8.86)
- 8.86 ("At") /* ROOF @8.86 */: frame 0 shows the roof, mast and spinning rotor.
- 8.98 ("6") /* 6:15 @9.22 */: spin speeds up from 9.22; 12.42 ("84") /* 84 @12.42 */: C1 in.
- 14.20 ("Then") C1 out; 14.90 ("blew") /* BLEW @14.90 */: rotor tears off (14.90 to 15.80), beat-accent flash 0.1 s.
- 17.58 ("least") /* 120 @17.78 */: C2 in at 17.78.
- 19.26 segment end; land time to the cut.

## Motion for the whole window
Rotor spin, then the mast whip, rain throughout.

## Exit
C2 slides out `x:980` in the last 0.6 s; cut to g-a4-13.

## Footage under it
None: full-frame drawing.
