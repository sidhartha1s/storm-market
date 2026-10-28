# g-a1-5-watch-timeline · A1-S5 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/stat-timeline.html` (horizontal chronology rail, sequential beats) for the rail and `compositions/g-a1-1-afd-scroll.html` (built first) for the product text card style. FAMILY BASE for the "forecast desk timeline": `g-a1-6-warning-card`, `g-a1-7-travel-line`, `g-a1-9-update-card` and `g-a1-10-street-clock` copy this rail and card geometry unchanged. Send it alone for a full-size read before they are built.

## 0. What this graphic claims
At 2:22 PM Tue 20 Dec 2022 NWS Buffalo put Erie County under a Winter Storm Watch for Friday morning to Monday morning, about 2 days 17 hours before the storm; the watch said gusts could reach 65 mph and blowing snow could bring whiteouts and localized blizzard conditions.

## 1. SOURCE
- WWUS41 KBUF 201922 (WSWBUF), "222 PM EST Tue Dec 20 2022", VTEC WS.A.0016 NEW 221223T1200Z-221226T1200Z, zones incl. Northern and Southern Erie. `research/nws.md` rows 1.1, 1.4, 6.4 (PRIMARY); `factcheck/a1-r1.md` rows 24 to 30. IEM: https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=WSWBUF&sdate=2022-12-17T00:00Z&edate=2022-12-22T08:00Z&fmt=text&limit=200
- Lead time: 2:22 PM Tue to 7:00 AM Fri = 2 d 16 h 38 min, chip rounds to "2 DAYS 17 HRS AHEAD" (row 1.4, `factcheck/a1-r1.md` row 28).
- Card text, re-fetched 28 Oct 26, product line breaks kept (rows W0 to W8 are this brief's ids):
```
W0 222 PM EST Tue Dec 20 2022
W1 ...WINTER STORM WATCH IN EFFECT FROM FRIDAY MORNING THROUGH
W2 MONDAY MORNING...
W3
W4   strong winds, heavy lake effect snow and significant blowing
W5   and drifting snow will be possible. Winds could gust as high as
W6   65 mph Friday into Friday night. Localized blizzard conditions
W7   are possible.
W8 (gap row)
W9  Areas of blowing
W10   snow could significantly reduce visibility with whiteouts and
W11   localized blizzard conditions possible.
```
Correction to W9: on screen W9 is the WHOLE product line `  could be very difficult to impossible at times. Areas of blowing` (never a partial line). W4 to W7 are whole product lines from the end of the "* WHAT..." bullet. W3 and W8 are gap rows (no text).

## 2. DATUM, SCALE, ORIENTATION (the family's shared numbers)
Time axis: Tue 20 Dec 00:00 at x 160 to Fri 23 Dec 12:00 at x 1540 = 84 h, 16.4286 px per hour. Computed by script (state it in the receipt):
| event | hours from Tue 00:00 | x |
|---|---|---|
| Tue 00:00 / Wed / Thu / Fri midnight ticks | 0 / 24 / 48 / 72 | 160.0 / 554.3 / 948.6 / 1342.9 |
| WATCH 2:22 PM Tue | 14.367 | 396.0 |
| WARNING 3:54 AM Thu | 51.900 | 1012.6 |
| UPDATE 6:48 PM Thu | 66.800 | 1257.4 |
| IN EFFECT 7:00 AM Fri | 79.000 | 1457.9 |
Rail y 900. Corner x >= 1600, y >= 680 empty (rail ends x 1540).

## 3. GEOMETRY (px)
- Ground: channel radial gradient `wt-ground`, on from frame 0.
- Rail: 4 px `#4a5560` line x 160 to 1540, y 900. Midnight ticks 2 x 16 px `#4a5560`. Day labels "TUE", "WED", "THU", "FRI": Arial 700 22 px `#93a3b2` letter-spacing 3, left = tick x + 12, top 914.
- In-effect tick at x 1457.9: 4 x 28 px `#c0392b` (drawn in this comp, labelled in g-a1-6).
- Product cards on the rail (lower lane): 380 x 104, radius 20, glass-dark fill `linear-gradient(180deg, #15202b, #0b1016)`, 1 px `rgba(255,255,255,.14)` border, top 760, centred on the event x; stem 2 px `#93a3b2` from card bottom (864) to the rail (900); a dot r 7 on the rail. Watch card centred 396 -> x 206 to 586. Line 1 "WINTER STORM WATCH" Arial Black `font-weight:900` 30 px `#f2f5f8`; line 2 "TUE DEC 20 · 2:22 PM" Arial 700 22 px `#d8a13a`; both left 24 px inside the card, tops +18 and +62.
- (Family: warning card centred 1012.6 -> x 822.6 to 1202.6, lower lane; update card centred 1257.4 -> x 1067.4 to 1447.4 in the UPPER lane, top 640, stem 744 to 900, passing right of the warning card's edge at 1202.6.)
- Lead bracket: the rail segment x 396.0 to 1457.9 thickens to 8 px `#d8a13a` (scaleX from left), dashes inside it flowing right at 40 px/s.
- Chip "2 DAYS 17 HRS AHEAD": Arial Black `font-weight:900` 52 px `#e8c56a`, left 200, top 110.
- Text card `wt-text`: x 170 to 1530, y 190 to 620, radius 28, fill as the g-a1-1 panel. Rows Courier New 700 28 px `#dfe7ee`, `white-space:pre`, left 230, pitch 44, first row (W0, 26 px `#93a3b2`) top 214, W1 top 258 ... W11 top 258 + 10 x 44 = 698? NO: W8 is a half row. Use tops: W0 214, W1 258, W2 302, W4 358, W5 402, W6 446, W7 490, W9 546, W10 590? That overflows y 620. So drop W8 and W3 gaps to 12 px: tops W0 212, W1 252, W2 292, W4 340, W5 380, W6 420, W7 460, W9 512, W10 552, W11 592 with pitch 40 and card y 190 to 640. Card bottom 640 is above the upper lane (640): give the card y 186 to 632 and the upper lane top 648 (family numbers then: upper lane 648 to 752, stem 752 to 900).
- Highlights (amber `#e8c56a` rect behind, text turns `#04070c`): H1 "Winds could gust as high as" on W5 + "65 mph" on W6; H2 "whiteouts and" on W10 + "localized blizzard conditions" on W11. Measure x from glyph boxes (Courier 16.8 px advance).
- Source line "NWS Buffalo, WWUS41 KBUF 201922, IEM archive": Arial 19 `#c8d3e0`, left 96, bottom 54 (y about 1007 to 1026; the day labels end y 936).
- Type tiers: 52, 22 to 30, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. The watch card's dot sits at x 396.0 (2:22 PM Tue) and the in-effect tick at 1457.9 (7 AM Fri) on one linear scale; the bracket spans exactly those two.
2. Card rows are the product text character for character with the product's breaks; no row cut at either card edge.
3. Highlights cover only "Winds could gust as high as 65 mph" and "whiteouts and localized blizzard conditions".
4. The chip says 2 DAYS 17 HRS AHEAD (rounded from 2 d 16 h 38 min) and appears only once the bracket is drawn.
5. Corner x >= 1600, y >= 680 empty; margins kept.

## 5. TEXT and CUES (seconds from A1-S5 start, `audio/a1-s5.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "That Tuesday note" @0.00 | ground on; rail draws `scaleX 0 -> 1`, 0.05 to 0.9, `power3.out`; day labels stagger in 0.6 to 1.2 |
| 1.64 | "watches" @1.64 | in-effect tick `fromTo(scaleY 0 -> 1, 0.3)` (unlabelled until g-a1-6) |
| 4.14 | "They did." @4.14 to 4.32 | rail dot at 396 pops (scale 0 -> 1, back.out) |
| 5.14 to 6.44 | "At 2.22 that same afternoon," | watch card drops `fromTo(y:-60 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` at 5.14; stem draws 5.5 to 5.8 |
| 7.48 | "the office" @7.48 | text card `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`, rows W0 to W2 in; source line in |
| 9.18 to 9.74 | "winter storm watch." | W1/W2 brighten to `#f2f5f8` |
| 10.64 to 12.66 | "It ran from Friday morning to Monday morning." | rows W4 to W11 in, `fromTo(autoAlpha 0, x:-16 -> 0, 0.3)` stagger 0.15 |
| 13.46 to 16.06 | "That was about two days and 17 hours before the storm." | bracket draws 396 -> 1457.9, 13.46 to 15.24 (`power2.inOut`); chip in at 14.84 ("17") |
| 17.42 to 19.70 | "gusts could reach 65 miles an hour" @17.42 to 19.70 | H1 rects `scaleX 0 -> 1` ease none (W5 part 17.42 to 18.54, W6 part 18.54 to 19.18) |
| 23.42 to 25.22 | "whiteouts and localized blizzard conditions." | H2 rects, same way |
| 26.36 to 28.72 | "If you lived in Erie County, that watch named you." | watch card border glows `#d8a13a` (0.4 s) and pulses at 28.46 ("named") |
| 31.42 | "whiteouts" @31.42 | H2 rects pulse `scaleY 1 -> 1.1 -> 1`, 0.5 |
| 34.38 to 35.4 | tail | hold; the bracket dashes keep flowing |
Comp duration 35.4 s. NO exit: the last frame (rail, watch card, bracket, chip, text card with H1/H2) is g-a1-6's frame 0. Motion through every hold: bracket dashes flow from 13.46; before that the beats sit under 4 s apart (check 0.9 to 1.64 to 4.14: gap 2.5 s, fine).

## 6. CONTRACT
One file `compositions/g-a1-5-watch-timeline.html`, root `id="g-a1-5-watch-timeline-root"`, `data-composition-id="g-a1-5-watch-timeline"`, PAUSED timeline at `window.__timelines["g-a1-5-watch-timeline"]`. Ids and classes prefixed `wt-`. Everything else: `references/mg-quickref.md`.

## 7. TOOLS / 7a. DONE LINE / 8. RECEIPT
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a1-5-watch-timeline`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a1-5-watch-timeline`. All seven template 7a items; item 6: the axis table above computed by script, stated in the receipt. Receipt as the template.
