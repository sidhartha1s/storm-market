# g-a1-8-toll: what the east side cost in lives (A1-S11)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/numbers-rollup.html` (counter), `library/inhouse/master-map-us-canada.html` (basemap). Prefix every id and class `tl8-`.
Sits over: nothing. Full-frame designed map on track 2. No photos of people.

## 0. Claim
New Jersey lost 34 people and New York 36 in this storm (whole-storm state tallies); New York's count includes the snowy southwest of the state. Closes loop A1c.

## 1. Source
`factcheck/a1-r1.md` row 47 (SECONDARY): usdeadlyevents.com quoting AP, 29 Nov 1950, "Storm deaths reported by states included New York 36; New Jersey 34" (whole-storm, no cause split). Row 48: New York's tally includes the snowy southwest (ALY "20+ inches"); the cause split is UNVERIFIED, so nothing on screen says "wind deaths". Source line "Source: Associated Press, 29 Nov 1950, via usdeadlyevents.com".

## 2. Datum, scale, orientation
Frame A1-T, s 0.03, frame top-left (56559.9, 12204.4), north up. Newark (1000,620), Albany (1048,299), Buffalo (458,260), Philadelphia (886,751), Cape May (915,922). Southwest New York shading box (clip to the NY outline): lon -79.76 to -77.7, lat 42.0 to 42.9 = screen x 356 to 594, y 257 to 408 (computed with the formula).

## 3. Geometry (px, 1920 x 1080)
- Basemap: land `#0b1016`, water `#04070a`; NJ and NY outlines 2 px `#93a3b2` with fill `#15202b` (neutral grey family, never wind blue `#7fb2e5`); neighbours 1.5 px `rgba(255,255,255,.14)`, no fill. No city pins, no city names.
- NJ chip (glass card, left 1120, top 470, ends x <= 1560, y <= 660): "34" Arial Black 900 84 px `#f2f5f8` beside "NEW JERSEY" Arial 700 30 px `#dfe7ee` tracking 3; tag under "WHOLE-STORM COUNT" Arial 700 19 px `#93a3b2` tracking 4. A 2 px `rgba(255,255,255,.3)` leader from the card's left edge to NJ's centre (about (960, 680)).
- NY chip (glass card, left 1180, top 140): "36" Arial Black 900 84 px + "NEW YORK" Arial 700 30 px; tag "INCLUDES SNOW SIDE" Arial 700 19 px `#e8c56a` tracking 4. Leader to NY's centre (about (860, 330)).
- Snow shading: the southwest box clipped to the NY outline, fill `rgba(242,245,248,.55)` with 30 slow flakes (2 to 4 px) falling inside it (finite repeats, seeded positions).
- Source line left 110, bottom 90; "Basemap: Natural Earth" bottom 60.
- Tiers: 84 / 30 / 19.

## 4. Must be true in the picture
1. Counters land on 34 (NJ) and 36 (NY), New Jersey first.
2. Only the southwest part of New York is snow-white, not the whole state and not New Jersey.
3. No word "wind" on screen; no photo or silhouette of a person; no per-cause number.
4. Nothing in x >= 1600, y >= 680 (NJ card ends y 660, x 1560).

## 5. Panel text (exact) and cues (`audio/a1-s11.words.json`, seconds from A1-S11 start)
Text: `34` · `NEW JERSEY` · `WHOLE-STORM COUNT` · `36` · `NEW YORK` · `INCLUDES SNOW SIDE` · `Source: Associated Press, 29 Nov 1950, via usdeadlyevents.com` · `Basemap: Natural Earth`
- 0.00: map on, outlines draw (0.8 s); slow drift scale 1 to 1.03 (ease none). Sound: the bed drops to a hush (editor). `/* THE @0.00 */`
- 2.08 "New Jersey": NJ fill brightens (`#15202b` to `#2a3644`, 0.4 s); NJ card in (`fromTo` x 60 to 0, autoAlpha, 0.5 s, power3.out). `/* NEWJERSEY @2.08 */`
- 2.82 "34": counter 0 to 34 on a leaf, opening on 1, 1.0 s, power4.out; tag in at 3.38. `/* 34 @2.82 */`
- 4.40 "New York": NY fill brightens; NY card in. `/* NEWYORK @4.40 */`
- 5.02 "36,": counter 0 to 36, 1.0 s, power4.out. `/* 36 @5.02 */`
- 7.34 "snowy": southwest shading fades in (0.6 s) and flakes start. `/* SNOWY @7.34 */`
- 7.68 "southwest": "INCLUDES SNOW SIDE" tag in. `/* SOUTHWEST @7.68 */`
- Hold to end: flakes fall, drift continues.
- Exit: last 0.6 s: both cards slide out (x 980, autoAlpha 0, power3.in). Cut to g-a1-9.
Host: data-start = A1-S11 start, duration = 9.109 + 0.40 = 9.51 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
