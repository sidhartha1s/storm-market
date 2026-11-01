# g-a4-4-dispatch-screen · A4-S4 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the Courier counter of `library/inhouse/numbers-rollup.html` and the panel surface of `library/inhouse/stat-panel.html`; match the look of the built `compositions/g-intro-3-asos-log.html` (same episode, same family of dark data cards).

## 0. What this graphic claims
1. Erie County's dispatch software could only show 25 calls at once: the screen fills to 25 rows and everything after that falls out of view.
2. By Saturday morning, Christmas Eve, 1,100 emergency calls were backed up.
The screen is an ILLUSTRATION of a queue, not a copy of the real software: rows carry no readable text.

## 1. SOURCE
- NYU Wagner report p.13: "County dispatch software that could only view 25 calls at once (sometimes duplicative)" (`factcheck/a4-r1.md` row 11, PRIMARY); `research/response.md` section 2 (Firehouse, Susan Nicol, citing NYU, SECONDARY).
- NYU p.139: "by the following morning [Sat 24 Dec], there was an 1,100-call backlog" (`factcheck/a4-r1.md` row 12, PRIMARY). Sat 24 Dec = Christmas Eve, computed.

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground, 1920 x 1080. The list viewport holds exactly 25 rows: viewport height 730 px / 25 = row pitch 29.2 px. Presenter circle may be on: nothing in x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- Ground: channel radial gradient (tokens.md "Canvas") from frame 0.
- Screen panel: x 120 to 1180, y 120 to 960, fill `#0b1016`, 1 px `#2a3644` border, radius 14. Header bar y 120 to 190, fill `#15202b`: "ERIE COUNTY DISPATCH QUEUE" Arial 700 26 px `#93a3b2`, letter-spacing 8, left x 160, centred in the bar; tag "ILLUSTRATION" Arial 700 19 px `#c8d3e0`, letter-spacing 4, right edge x 1150, same centre line.
- Viewport: x 140 to 1160, y 210 to 940, `overflow:hidden` (rows past y 940 are cut by the mask, never drawn below it).
- Row: 26 px tall, 3.2 px gap (pitch 29.2), full viewport width, fill alternating `#15202b` / `#0f1820`. Inside: a 10 px status pip at x 160 (`#e74c3c`), then three placeholder bars 10 px tall, `#2a3644`, at x 190, 470, 760 with widths taken from a fixed seeded list (between 120 and 240 px) so no two neighbouring rows match. No letters or digits in any row.
- New calls arrive at the TOP: each arrival moves the row column down one pitch (`y += 29.2`, 0.12 s power2.out) and the new row fades in at the top slot (y 210). Pre-author 70 rows; row k's arrival time is listed in section 5.
- Bracket: 3 px `#d8a13a` vertical line at x 1196 from y 210 to 940 with 12 px ticks at both ends pointing left; drawn with `scaleY 0 -> 1`, transformOrigin top.
- Chip "25 CALLS AT ONCE" (right column, glass surface as `g-intro-2-toll-chips`, padding 22 px 34 px): left x 1240, y 520 to 648. "25" Arial Black `font-weight:900` 84 px `#f2f5f8` + 16 px gap + "CALLS AT ONCE" Arial 700 30 px `#dfe7ee`, letter-spacing 1. About x 1240 to 1690.
- Counter (right column, top): glass card x 1240 to 1720, y 150 to 360. Value Courier New 700 84 px `#e74c3c`, left x 1280, top y 180; label "CALLS BACKED UP" Arial 700 20 px `#c8d3e0`, letter-spacing 6, left x 1280, baseline y 330. The value is the ONLY "1,100" on screen: the Picture's chip "1,100 CALLS BACKED UP" IS this counter and its label (one fact, one instance per frame).
- Highlighted call: the row that sits in slot 8 (y 210 + 7 x 29.2 = 414.4) at 13.72 gets a 2 px `#d8a13a` outline and its pip turns `#e8c56a` and pulses (scale 1 -> 1.6 -> 1, 0.8 s, finite repeats) to the end.
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Type tiers: 84 (big), 26 and 30 (mid), 19 and 20 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. At "25" @5.30 exactly 25 rows are fully inside the viewport, filling it top to bottom, and the bracket spans exactly those 25.
2. After 6.42 rows keep arriving and the oldest leave through the viewport's bottom edge: never more than 25 rows (plus the one entering or leaving) are visible.
3. No row shows a letter, digit, address or time: the screen is a schematic queue, tagged ILLUSTRATION.
4. "1,100" appears once, as the counter's final value, landed by 10.95; the 25 chip is gone before the counter starts.
5. The counter lands fast-then-slow on exactly 1,100 (comma kept) and never passes it.
6. The corner x >= 1600, y >= 680 is empty ground.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S4 start, `audio/a4-s4.words.json`)
Strings: `ERIE COUNTY DISPATCH QUEUE` · `ILLUSTRATION` · `25` `CALLS AT ONCE` · counter `1,100` `CALLS BACKED UP` · source `NYU Wagner review for the City of Buffalo, via Firehouse, 5 Jun 2023`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "A review" @0.00 | ground, empty panel, header and tag on from frame 0; source pill in at 0.10 `fromTo(autoAlpha 0, y:16 -> 0, 0.4)` |
| 1.92 to 5.30 | "found" @1.92 to "25" @5.30 | rows 1 to 25 arrive at `1.92 + (k-1) x 0.1408` (k = 1 to 25; row 25 at 5.30) |
| 3.32 | "dispatch" @3.32 | header text brightens to `#f2f5f8` 0.3 s, back by 4.2 |
| 5.30 | "25" @5.30 | bracket draws 0.4 s power2.out; chip in `fromTo(x:60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`, numeral `fromTo(scale 1.3 -> 1, 0.4, power4.out)` |
| 6.42 on | "once." @6.42 | rows 26 to 70 arrive every 0.24 s from 6.42 to 16.98 (overflow scroll; the column keeps moving to the end) |
| 7.00 to 7.35 | before "By Saturday" @7.34 | chip out `to(x:80, autoAlpha 0, 0.35, power3.in)`; bracket out with it |
| 9.70 | "backlog" @9.70 | counter card in `fromTo(y:-20 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; value counts from 1 on its first tick (leaf span, onUpdate) |
| 9.70 to 10.95 | "1,100" @10.60 to 10.86 | count to 1,100, `power4.out`, lands at 10.95 |
| 11.20 | "emergency calls" @11.20 | label "CALLS BACKED UP" brightens to `#f2f5f8` 0.3 s |
| 13.72 | "somebody" @13.72 | highlight on the slot-8 row (outline in 0.3 s, pip pulse starts) |
| 16.25 to 16.85 | after "then." @16.40 | counter card out `to(x:980, autoAlpha 0, 0.6, power3.in)`; pill out; panel stays to the cut |

Comp duration 16.85 s (wav length). Full-frame scene: it ends on the cut into `g-a4-5-response-clock`.

## 6. CONTRACT
One file `compositions/g-a4-4-dispatch-screen.html`, root `<div id="g-a4-4-dispatch-screen-root" data-composition-id="g-a4-4-dispatch-screen" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-4-dispatch-screen"]`. Ids prefixed `ds-`; classes prefixed `ds-`. Rows are pre-authored DOM (70), toggled and moved by the timeline, never created in onUpdate. Counter writes only a leaf span. Ground on from frame 0. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-4-dispatch-screen`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-4-dispatch-screen`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 4: seek check at 5.30 (25 rows) and 10.95 (1,100). Item 6: arrival times and row y computed by a script from section 5's formula. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
