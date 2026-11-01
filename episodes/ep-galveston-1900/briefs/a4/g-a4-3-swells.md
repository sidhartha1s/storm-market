# g-a4-3-swells · A4-S2 0 to 6.90 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass card over footage), catalog `mk-usage-arc` (arc that draws while counting).

## 0. Claim
About 5 a.m. Saturday, Cline stood on the beach watching heavy swells roll in and timed them.

## 1. Source
MWR Sept 1900 p. 372 (factcheck/a4-r1.md rows 6, 7): "About 5 a. m. of the 8th ... I drove to the Gulf, where I timed the swells"; "heavy swells" from the p. 372 telegram (row 12). The interval (one to five minutes) is NOT on screen here (cut from the voice).

## 2. Datum, scale, orientation
Overlay, root transparent, over A4-S2_c1 surf (graded down per picks.md). Watch card centre-right, chip under it; source line top-left.

## 3. Geometry (px)
- Watch card: glass circle-backed card 360 x 360 at left 1300, top 200 (right edge 1660, bottom 560: clear of the corner). Inside: pocket-watch face drawn in SVG, r 150, rim `#d8a13a` 6 px, face `#0b1016`, 60 minute ticks `#93a3b2` (12 majors 18 px, minors 8 px), crown at top. Second hand `#d0121f` 3 px, length 130, sweeping 6°/s (one tick per second, stepped `rotation`, ease steps). A gold arc `#e8c56a` 8 px on the rim draws from 12 o'clock as a "stopwatch lap" (strokeDashoffset) and resets on each swell crest cue.
- No numerals on the watch face (no hour is claimed beyond "five that morning").
- Chip (glass, shared spec, main Arial Black 900 52 px) "TIMING THE SWELLS", centred x 1480, top 600, tag "5 AM · Saturday".
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 372".

## 4. Must be true in the picture
1. Second hand moves 6° per second exactly (receipt: angle at 2 times).
2. Watch card and chip never cover the brightest crest band of the clip (frame read over the real clip; move the card to the left side, left 260, if the clip's surf runs right).
3. No interval figure on screen.
4. Nothing in x >= 1600, y >= 680 (chip box right edge must stay at or under 1600 below y 680: chip bottom about 710, so its right edge is capped at 1600; centre it at x 1380 if wider than 440).

## 5. Text and cues (a4-s2.words.json)
- 0.56 ("five") /* FIVE @0.56 */: watch card in (scale 0.9 to 1, autoAlpha, 0.5, back.out).
- 4.50 ("swells") /* SWELLS @4.50 */: lap arc resets and draws; 5.00 ("rolling") second reset.
- 6.02 ("timed") /* TIMED @6.02 */: chip in.
- 6.30 to 6.90: card and chip exit.

## Motion for the whole window
Second hand ticks every 1 s; card float y ±4 px.

## Exit
Card and chip slide out `x:980, autoAlpha 0, 0.6, power3.in` 6.30 to 6.90; cut to g-a4-4's dial at 6.90.

## Footage under it
A4-S2_c1_beach-waves-shore.mp4 (Pexels, verified Y; warm macro surf, grade down), the whole host window.
