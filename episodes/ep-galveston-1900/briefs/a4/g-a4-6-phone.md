# g-a4-6-phone · A4-S4 0 to 8.70 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `compositions/g-a3-10-1875.html` (schematic line-drawing style on the tokens ground).

## 0. Claim
With storm warnings flying, the Weather Bureau office kept one man on the telephone constantly, and hundreds who could not get through came in person.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 15 to 17): "made it necessary to keep one man constantly at the telephone giving out information. Hundreds of people who could not reach us by telephone came to the Weather Bureau office seeking advice." No flag type is given (sources-cline.md §6): no flag drawn. Room layout: SCHEMATIC (no office image sourced, picks.md).

## 2. Datum, scale, orientation
Full-frame line drawing on the tokens gradient: an office wall seen face on. Floor line y 860, x 96 to 1824. Door frame on the right (x 1280 to 1480, y 420 to 860). Wall telephone on the left (centre (520, 470)). Note bottom-left "Office: schematic" Arial 700 19 px `#93a3b2` at left 96, top 1000.

## 3. Geometry (px)
- Lines `#93a3b2` 3 px, fills `#15202b`. Wall phone: period wooden wall set, box 120 x 220 at x 460 to 580, y 360 to 580, two bells (r 18) at its top, crank at the right, earpiece on a cord. A seated figure silhouette `#5a768f` at the phone, (600 to 720, y 560 to 860), receiver at its head.
- Ring: the bells shake (rotation ±8°, 0.06 s, 6 cycles per burst) and three arc "ring" strokes `#e8c56a` 3 px flash out from the bells (scale 0.6 to 1.2, autoAlpha 1 to 0, 0.4 s).
- Door: open door frame; outside it a queue of 9 standing silhouettes (`#4a5560`, 40 x 120 px each, 56 px apart) from x 1490 rightward to x 1938 (the last ones run off the right edge: they are shapes, not text), filing toward the door; the first steps through.
- Chip (glass, main Arial Black 900 52 px) "ONE MAN ON THE PHONE", left edge 96, top 140 (tag "storm warnings flying · Sat. morning").
- Second chip (same zone after the first leaves) "HUNDREDS CAME IN PERSON", left edge 96, top 140, tag "could not get through".
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".

## 4. Must be true in the picture
1. Exactly one figure is at the phone.
2. No flag shape anywhere.
3. The two chips never together; neither covers the phone or figure (chip bottom about 250 < phone top 360).
4. Queue silhouettes are below y 680 only where x < 1600 matters: the queue sits in the corner zone x >= 1600, y >= 680; it is a figure group, so the circle goes off for this window (state in receipt) OR the queue is shifted left to x 1490 to 1590 with 4 figures visible: builder picks the first and reports.

## 5. Text and cues (a4-s4.words.json)
- 0.00: frame 0 shows the wall, phone and figure; first ring burst at 0.12.
- 2.86 ("kept") /* ONE MAN @3.12 */: chip 1 in at 3.12 ("one"); ring bursts every 1.2 s from 0.12 to 8.40.
- 5.54 ("Hundreds") /* HUNDREDS @5.54 */: chip 1 out; queue walks in from the right (x +300 to 0, 1.2 s, power2.out); chip 2 in at 5.98 ("people").
- 7.22 ("came"): the first figure steps through the door (x -60, 0.6 s).
- 8.10 to 8.70: chip 2 exits.

## Motion for the whole window
Ring bursts every 1.2 s; queue shuffle (each figure y ±3 px, staggered).

## Exit
Chip slides out `x:980, autoAlpha 0, 0.6, power3.in` 8.10 to 8.70; cut to g-a4-7 at 8.70.

## Footage under it
None: full-frame drawing (no office footage found, picks.md).
