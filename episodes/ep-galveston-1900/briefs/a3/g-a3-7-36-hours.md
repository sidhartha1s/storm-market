# g-a3-7-36-hours · A3-S6 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `ep-1974-super-outbreak/compositions/g-cite-paper.html` (lit line), `library/inhouse/stat-timeline.html` (time bar). Coast part uses the g-intro-4 plate and projection.

## 0. Claim
Galveston was warned on the morning of Friday the 7th, nearly 36 hours before the disaster; that same day the warning was extended all along the Texas coast. So the island had nearly a day and a half.

## 1. Source
MWR Sept 1900 p. 376 (Boston Herald, 17 Sept 1900; factcheck/a3-r1.md rows 23, 25, 26): "on the morning of the 7th, nearly thirty-six hours before the disaster, warned the people of Galveston of its coming, and during that day extended its warnings all along the Texas coast". 7 Sept 1900 was a Friday. The "moderate storm" line is CUT (factcheck/a3-r3.md): nothing on this comp says moderate or names the warning's wording.

## 2. Datum, scale, orientation
- Part A (0.00 to 6.04): page panel, `media/candidates/a3/A3-S6_c1_mwr-sept1900-p376_boston-herald-evening-sun.png`, column crop, whole lines, box 1240 px centred x 900.
- Part B (6.04 to 10.06): Texas coast on the g-intro-4 plate, camera V-TX cx 420, cy 1350, s 0.9. Coast stroke = the Natural Earth Texas coastline from Sabine Pass (-93.87, 29.73) = (551.7, 1171.5) to the Rio Grande mouth (-97.15, 25.96) = (256.5, 1563.4). Galveston (468.0, 1216.2). Screen (checked 28 Oct 26): Sabine (1079, 379), Rio Grande mouth (813, 732), Galveston (1003, 420).
- Part C (10.06 to end): time bar, full frame. Bar from x 260 to x 1460 (1200 px) at y 560, height 28. Scale 36 h = 1200 px, 33.33 px per hour. Left end "FRI MORNING", right end "SAT EVENING". NO clock hours on it: the source gives "morning" and "nearly thirty-six hours", no hour.

## 3. Geometry
- Part A band: amber `#d8a13a` opacity 0.28 behind "nearly thirty-six hours before the disaster" (boxes measured on the scan; receipt lists them).
- Chip C1 "NEARLY 36 HOURS" centred x 960, top 150 (in Part A, over the page's top margin, page box starts at top 260).
- Part B: the coastline stroke lights `#d8a13a` 6 screen px with glow, drawn from Galveston outward both ways (strokeDashoffset on two sub-paths: Galveston to Sabine, Galveston to the Rio Grande). No station pins (the source names none). Galveston pin `#f2f5f8` 14 px, label "Galveston" Arial Black 900 34 px right of the pin. Label "TEXAS COAST" Arial 700 26 px `#e8c56a` tracking 3 on the HUD at screen (560, 520).
- Part C: bar track `#15202b`, fill `#d8a13a` from left; a white tick at the fill head. Labels Arial 700 24 px `#93a3b2` under each end. Chip C2 "NEARLY A DAY AND A HALF" centred x 860, top 300.
- Source line top-left: "Boston Herald, Sept. 17, 1900, reprinted in Monthly Weather Review, Sept. 1900, p. 376".

## 4. Must be true in the picture
1. No clock hour anywhere; "FRI MORNING" and "SAT EVENING" only.
2. No "moderate", no quote of the warning text.
3. Coast lights as one continuous line; no invented station pins.
4. Bar full length = exactly 1200 px for 36 h; it fills to 100 % only at the freeze, and "NEARLY" stays on both chips.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a3-s6.words.json, segment 12.04 s)
- 0.00 ("Galveston"): page in, source line.
- 1.20 ("Friday") /* FRIDAY @1.20 */: push starts toward the lit line.
- 3.26 ("nearly") /* 36 HOURS @3.52 */: band draws 3.26 to 5.00; C1 in at 3.52.
- 6.04 ("That same day") /* COAST @6.04 */: C1 out, cut to Part B; Galveston pin on.
- 7.38 ("warning") to 9.22 ("coast"): coastline lights outward.
- 10.06 ("so") /* DAY AND A HALF @11.40 */: dissolve to Part C; bar fills 10.06 to 11.82, power1.inOut; C2 in at 11.40 ("day").
- 11.82 ("half"): fill freezes; tick flashes once.
- Host 0.00 to 12.04 plus land time (cap 13.0). Next: the act's cut to A3-S7's beach (the Picture's "quiet Galveston street" has no footage: see `_list.md` open items).

## Motion for the whole window
Page push, then coast draw, then bar fill; text cards drift.

## Exit
Fade-through, root to 0 over the last 0.4 s.

## Footage under it
Part A: the MWR p. 376 scan inside the comp. B and C: full-frame designed.
