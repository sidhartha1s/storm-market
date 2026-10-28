# g-a4-19-barograph · A4-S11 14.20 to 20.54 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `ep-1974-super-outbreak/compositions/g-cite-paper.html` (published page on a card), catalog `svg-line-draw-loader` (a reveal that follows a line).

## 0. Claim
The barometer fell about an inch from noon (29.42 in) to its lowest, 28.48 in, at 8:30 p.m., the moment Cline's house went down: the station's own barograph trace shows the plunge.

## 1. Source
MWR Sept 1900 p. 373 text (factcheck/a4-r1.md rows 54, 58; a4-r4.md row 4): "fell rapidly from noon until 8:30 p. m. of the 8th, when it registered 28.48 inches, a fall of pressure of about one inch in eight and one-half hours. After 8:30 p.m. the barometer rose"; "at 8:30 p. m. my residence went down". Figure: MWR fig. 1, the barograph trace, on PDF page 2 of A4-S1_c1 (printed p. 372 per picks.md; sourcer and act say p. 373: CONFIRM on the page image before building, and the source line prints the confirmed page). Rasterise at 300 dpi to `media/a4/mwr-fig1.png`.

## 2. Datum, scale, orientation
- The trace is the scan, never a redrawn curve. Card: glass x 160 to 1500, y 170 to 900, the fig. 1 crop fitted inside with its own axis labels kept (whole figure, nothing cut).
- Measure on the scan (receipt lists them): the px x of noon and of 8:30 p.m. on the figure's time axis; the px y of 29.42 and 28.48 on its pressure axis; the trace's lowest point. The reveal and the pen dot use these measured points only.

## 3. Geometry (px)
- Reveal mask: a rect over the figure that uncovers it left to right (scaleX 0 to 1 from the left edge of the trace window), its right edge always at the pen dot's x.
- Pen dot: `#d0121f` 14 px with 4 px `#f2f5f8` ring, riding the trace: positions sampled from the scan (the builder traces the curve's centre line in the scan into a list of (x, y) points, at least one per 10 px of x, listed in the receipt; per-leg attr/x/y tweens, no MotionPathPlugin). It must sit on the ink within 3 px at three checked times.
- Noon marker: thin `#93a3b2` 2 px vertical at the noon x, label "NOON · 29.42" Arial 700 22 px `#93a3b2` above the card's plot area.
- Bottom marker: `#d0121f` 2 px vertical at the 8:30 x; chip (glass, main Arial Black 900 52 px) "8:30 PM · 28.48 IN", tag "lowest reading", left edge 1180, top 120? The card spans x 160 to 1500; put the chip outside the card at right: left edge 1540, top 300 (box to about x 1900: too wide). Use: chip inside the frame above the card, centred on the 8:30 x, top 60, with the card shifted down to y 230 to 960.
- "ABOUT 1 IN" bracket: a `#e74c3c` vertical bracket at the right of the plot from the 29.42 y to the 28.48 y, label "ABOUT 1 IN" Arial 700 30 px (mid) beside it.
- Black beat: after the chip lands, the whole comp fades to `#04070c` from 19.78 to 19.94 and holds black to 20.54 (0.6 s; blank_scan threshold is 0.75 s: keep it under).
- Source line top-left: "Monthly Weather Review, September 1900, p. 372, fig. 1" (page per the check in §1).

## 4. Must be true in the picture
1. The curve on screen is the scan's ink; no drawn line imitates it.
2. Pen dot within 3 px of the ink at noon, at the midpoint, and at the minimum (receipt frames).
3. The chip's 8:30 x matches the scan's 8:30 axis position (receipt).
4. The trace after 8:30 (the rise) is revealed only after the chip lands, or held masked: the voice says "hit bottom" and stops there; reveal stops at the minimum.
5. Black lasts 0.6 s ±0.05 (no frame of black past 0.75 s).
6. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a4-s11.words.json, comp-local = word time - 14.20)
- 14.20 ("The barometer") /* BAROMETER @14.36 */: frame 0 shows the card with the figure masked to the noon line; noon marker and label on; source line on.
- 14.96 ("fallen") /* FALL @14.96 */: pen dot rides from noon toward the minimum (14.96 to 17.46, ease none, following the ink); bracket draws at 15.48 ("an inch"), label in at 15.64.
- 17.46 (".30" of "8 .30") /* 8:30 @17.22 */: dot reaches the minimum at 17.46; bottom marker draws; 18.26 ("hit bottom") chip in.
- 19.56 ("went down") /* DOWN @19.56 */: a 0.2 s jolt on the card (y +6), then fade to black 19.78 to 19.94; black to 20.54 (the editor's low tone under it).
- 20.54 host end (g-a4-20 starts at "About").

## Motion for the whole window
Dot travel 14.96 to 17.46; before it the noon marker pulses; after it the dot ring pulses every 0.6 s until the fade.

## Exit
Fade through black (a full-frame scene ending on a fade, allowed); cut to g-a4-20.

## Footage under it
None; MWR fig. 1 scan inside the comp (A4-S1_c1, verified Y; PD 1900 US Weather Bureau).
