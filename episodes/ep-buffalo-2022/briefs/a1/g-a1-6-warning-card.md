# g-a1-6-warning-card · A1-S6 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, template `references/mg-brief-template.md`, and `briefs/a1/g-a1-5-watch-timeline.md` (family base: axis table, rail, lanes, card and text-card geometry are used unchanged here).
Start from: the built `compositions/g-a1-5-watch-timeline.html` (copy, rename every `wt-` to `wc-`). Frame 0 = g-a1-5's last frame.

## 0. What this graphic claims
At 3:54 AM Thu 22 Dec the Blizzard Warning went out, in effect 7 AM Fri: 27 hours' notice. It called for 1 to 3 feet of snow, gusts to 70 mph, and wind "frequently reducing visibilities to zero."

## 1. SOURCE
WWUS41 KBUF 220854 (WSWBUF), "354 AM EST Thu Dec 22 2022", VTEC BZ.W.0001 NEW 221223T1200Z-221225T1200Z, Northern and Southern Erie. `research/nws.md` rows 1.2, 1.3, 1.5, 6.3 (PRIMARY); `factcheck/a1-r1.md` rows 31 to 33, 36, 37. 27 h 06 min computed (row 1.3). Card rows (re-fetched 28 Oct 26, product breaks; R-ids are this brief's):
```
R0 354 AM EST Thu Dec 22 2022
R1 ...BLIZZARD WARNING IN EFFECT FROM 7 AM FRIDAY TO 7 AM EST
R2 SUNDAY...
R3 (gap)
R4 * WHAT...Blizzard conditions expected. Total snow accumulations of
R5   1 to 3 feet. Winds gusting as high as 70 mph Friday and Friday
R6 (gap)
R7 Strong winds will cause significant blowing and drifting snow,
R8 frequently reducing visibilities to zero. Travel is strongly
R9 discouraged.
```

## 2-3. DATUM and GEOMETRY
Axis, rail, lanes, cards, chip slot, text card and source slot: exactly g-a1-5 section 2 and 3. New here:
- Warning card, lower lane, centred x 1012.6 (x 822.6 to 1202.6), top 760; line 1 "BLIZZARD WARNING" Arial Black 900 30 px `#f2f5f8`, line 2 "THU DEC 22 · 3:54 AM" Arial 700 22 px `#d8a13a`; 3 px `#c0392b` left edge bar.
- In-effect label "IN EFFECT 7 AM FRI": Arial 700 22 px `#e74c3c` letter-spacing 2, centred on x 1457.9, top 866 (box about 1330 to 1586, right of the warning card, left of x 1600). Arrow: 3 px `#e74c3c` along the rail from 1012.6 to 1450, y 888, head at 1457.9, drawn by strokeDashoffset.
- Notice bracket: rail segment 1012.6 to 1457.9 thickens to 8 px `#e74c3c` with dashes flowing right 40 px/s (the watch bracket from g-a1-5 dims to 0.3).
- Chips (top-left slot, left 200, top 110, Arial Black 900 52 px `#e8c56a`): "27 HOURS' NOTICE"; later "1 TO 3 FT" at left 200 and "GUSTS TO 70 MPH" at left 560 (same row; measure so they sit 40 px apart).
- Text card rows R0 to R9 at the g-a1-5 row tops (R0 206, R1 246, R2 286, R4 334, R5 374, R7 422, R8 462, R9 502); card height may shrink to y 186 to 552.
- Highlights (amber rect, text to `#04070c`): "7 AM FRIDAY" (R1); "1 to 3 feet" (R5); "as high as 70 mph" (R5); "frequently reducing visibilities to zero." (R8).
- Source line "NWS Buffalo, WWUS41 KBUF 220854, IEM archive" replaces g-a1-5's at the text-card swap.

## 4. MUST BE TRUE
1. Warning dot at x 1012.6, in-effect tick at 1457.9; bracket spans exactly them (27.1 h on the shared scale).
2. Card rows are the product text character for character; no row cut at an edge.
3. The watch card stays where it was (x 206 to 586), dimmed to 0.5; nothing moves the axis.
4. Each chip appears on its spoken number, never before; dup-fact: no two leaves carry the same digit string.
5. Corner x >= 1600, y >= 680 empty; the in-effect label ends before x 1600.

## 5. TEXT and CUES (seconds from A1-S6 start, `audio/a1-s6.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Then," | frame 0 = g-a1-5 last frame |
| 0.20 to 0.70 | | chip "2 DAYS 17 HRS AHEAD" out (x:-40, autoAlpha 0, 0.4, power3.in); watch text card out (y:-30, autoAlpha 0, 0.4); watch bracket and card dim to 0.3/0.5 |
| 0.74 to 1.40 | "3.54" @0.74 to 1.00 | rail dot at 1012.6 pops; warning card drops (y:-60 -> 0, 0.5, power3.out); stem draws |
| 1.40 to 2.06 | "Thursday morning," | warning text card in (y:40 -> 0, 0.5), rows R0 to R2; source line swaps (old out 0.3, new in 0.3) |
| 3.24 | "blizzard warning," @3.24 | card left bar `scaleY 0 -> 1`; R1/R2 brighten |
| 4.42 to 5.60 | "effect from 7 o'clock" @4.42 to 5.22 | arrow draws 1012.6 -> 1457.9; "7 AM FRIDAY" highlight 4.84 to 5.22 |
| 5.56 | "Friday morning." @5.56 | "IN EFFECT 7 AM FRI" in (y:10 -> 0, 0.4) |
| 6.60 to 8.04 | "That's 27 hours of notice." | notice bracket draws 6.60 to 7.48; chip "27 HOURS' NOTICE" in at 6.88 (scale 1.2 -> 1, 0.4, power4.out) |
| 8.92 to 13.26 | "And 7 on the last Friday ... for work." | in-effect tick pulses at 9.10 ("7") and 11.68 ("people"); bracket dashes flow |
| 13.60 | | chip out (0.35); rows R4 R5 in (stagger 0.15) |
| 14.84 | "1" @14.84 | chip "1 TO 3 FT" in; highlight "1 to 3 feet" 14.84 to 15.54 |
| 17.28 | "70" @17.28 | chip "GUSTS TO 70 MPH" in; highlight "as high as 70 mph" 17.06 to 18.12 |
| 18.74 to 20.18 | "and the wind would blow that snow around," | rows R7 to R9 in (stagger 0.2) |
| 21.40 to 23.38 | "frequently reducing visibilities to zero." | R8 highlight `scaleX 0 -> 1` ease none on the phrase; at 23.38 chips dim to 0.5 |
| 23.60 to 24.6 | tail | hold, dashes flowing; NO exit (g-a1-7 opens on this last frame) |
Comp duration 24.6 s.

## 6-8
One file `compositions/g-a1-6-warning-card.html`, root `id="g-a1-6-warning-card-root"`, `data-composition-id="g-a1-6-warning-card"`, PAUSED timeline at `window.__timelines["g-a1-6-warning-card"]`, prefix `wc-`. Tools, done line (all seven 7a items; item 3: frame 0 equals g-a1-5's last frame, submit both) and receipt as the template.
