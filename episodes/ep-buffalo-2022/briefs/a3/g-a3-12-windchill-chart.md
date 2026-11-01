# g-a3-12-windchill-chart · A3-S10 · deep · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/stat-timeline.html` (rail, readouts, type) and the official `chart-story` block (`library/catalog-index.json`, "One chart builds from data"). The data is the table in §1: plot it with a script from the table, never by eye.

## 0. What this graphic claims
At the Buffalo airport the wind chill fell through zero late Friday 23 Dec, stayed below -10°F for more than a day (12:33 PM Fri to 2:45 PM Sat in the feed, about 26 h), and bottomed at about -24°F at 5:18 AM Sat 24 Dec (Christmas Eve). Anndel was waiting in her car through much of that stretch.

## 1. SOURCE
- `research/nws.md` Q3 row 3.5 (BUF ASOS "feel", PRIMARY derived): coldest about -24°F at 5:18 AM Sat 24 Dec (temp 4°F, wind 33 kt). Row 3.5's start time "about 11:43 AM Fri" is WRONG: 11:43 is where the feed first goes below zero (-4.8). See `_list.md` open item 1.
- ASOS feed re-pulled by the brief writer 28 Oct 26: https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=BUF&data=tmpf&data=sknt&data=feel&year1=2022&month1=12&day1=23&year2=2022&month2=12&day2=25&tz=America%2FNew_York&format=onlycomma&latlon=no&missing=M&trace=T&direct=no&report_type=3&report_type=4
- Plot data, every routine and special ob with a feel value, Fri 23 Dec 06:00 to Sat 24 Dec 16:00 local, feel rounded to whole °F (91 points; day hh:mm value). Unrounded where it decides a crossing: Fri 10:54 +0.6, 11:43 -4.8, 12:05 -8 (approx), 12:33 -10.9; Sat 14:06 -13, 14:45 -9.6; low Sat 05:18 -23.9.
  ```
  23 06:18 32 | 23 06:37 33 | 23 06:54 33 | 23 06:58 32 | 23 07:24 28 | 23 07:43 23 | 23 07:54 21 | 23 08:06 18 | 23 08:39 11 | 23 08:47 11
  23 08:54 11 | 23 09:20 8 | 23 09:54 2 | 23 10:01 5 | 23 10:10 2 | 23 10:20 2 | 23 10:23 1 | 23 10:28 2 | 23 10:54 1 | 23 11:29 1
  23 11:43 -5 | 23 11:54 -7 | 23 12:05 -8 | 23 12:33 -11 | 23 12:49 -11 | 23 12:54 -13 | 23 13:34 -14 | 23 13:54 -13 | 23 14:54 -14 | 23 15:46 -13
  23 15:54 -15 | 23 16:37 -17 | 23 16:54 -19 | 23 17:54 -16 | 23 18:44 -17 | 23 18:54 -17 | 23 19:25 -18 | 23 19:54 -18 | 23 20:25 -16 | 23 20:49 -14
  23 20:54 -15 | 23 21:11 -15 | 23 21:54 -15 | 23 22:30 -16 | 23 22:54 -16 | 23 23:49 -17 | 23 23:54 -19 | 24 00:54 -18 | 24 01:19 -16 | 24 01:54 -17
  24 02:39 -20 | 24 02:54 -20 | 24 03:05 -22 | 24 03:51 -20 | 24 03:54 -18 | 24 04:04 -20 | 24 04:54 -21 | 24 05:01 -22 | 24 05:10 -23 | 24 05:18 -24
  24 05:36 -21 | 24 05:54 -21 | 24 06:10 -23 | 24 06:44 -23 | 24 06:54 -21 | 24 07:17 -19 | 24 07:38 -17 | 24 07:43 -19 | 24 07:54 -19 | 24 08:22 -20
  24 08:30 -20 | 24 08:36 -19 | 24 08:49 -19 | 24 08:54 -19 | 24 09:14 -18 | 24 09:54 -19 | 24 10:13 -18 | 24 10:54 -16 | 24 11:09 -17 | 24 11:19 -17
  24 11:47 -12 | 24 11:54 -14 | 24 12:07 -14 | 24 12:25 -12 | 24 12:48 -14 | 24 12:54 -13 | 24 13:54 -13 | 24 14:06 -13 | 24 14:45 -10 | 24 14:54 -8
  24 15:54 -9
  ```
  (The "24 14:45 -10" point is -9.6, above the -10 line: plot -9.6.)
- After 16:00 Sat the feed dips below -10 again (16:20 to 19:54); the chart stops at 16:00 so the band reads as one span. Say so in the receipt.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `wc2-ground`, frame 0). Plot area x 220-1500, y 200-800.
- Time axis: Fri 23 Dec 06:00 at x 220 to Sat 24 Dec 16:00 at x 1500 = 34 h, 37.647 px per hour. x(t) = 220 + 37.647 × (hours since Fri 06:00).
- Value axis: +35°F at y 200 to -30°F at y 800 = 65 °F, 9.2308 px per °F. y(v) = 200 + 9.2308 × (35 - v).
- Corner x >= 1600, y >= 680 empty (plot ends x 1500).

## 3. GEOMETRY (px) — computed from §2; print these from the page
- Gridlines 1 px `rgba(255,255,255,.08)` at v = +30, +20, +10, 0, -10, -20, -30 → y 246.2, 338.5, 430.8, 523.1, 615.4, 707.7, 800.0. Zero line 2 px `#93a3b2`. The -10 line: 3 px dashed `#7fb2e5`, dash 12 8.
- Value labels, Arial 700 22 px `#93a3b2`, right-aligned at x 200, vertically centred on each gridline: "30", "20", "10", "0", "-10", "-20", "-30". Axis title Arial 700 22 px `#93a3b2` tracking 3, left 96, top 160: "WIND CHILL, °F".
- Time ticks, 1 px `#4a5560` from y 800 to 812, labels Arial 700 22 px `#93a3b2` centred, top 820: "FRI 6 AM" x 220 (left-aligned at 220 instead, so it stays 96+ from the edge), "FRI 12 PM" x 445.9, "FRI 6 PM" x 671.8, "SAT 12 AM" x 897.6, "SAT 6 AM" x 1123.5, "SAT 12 PM" x 1349.4.
- Wind-chill line `wc2-line`: polyline through the 91 points, stroke `#f2f5f8` 5 px, round joins. Draw-on via dash, length `ceil(getTotalLength())+1`.
- Band `wc2-band`: rect x 466.6 (12:33 Fri, 6.55 h) to 1452.9 (14:45 Sat, 32.75 h), y 615.4-800, fill `rgba(127,178,229,.18)`; drawn `scaleX 0 -> 1` left origin.
- Low marker `wc2-low`: circle r 10 `#e74c3c` at (1097.2, 743.7) (05:18 Sat = 23.3 h; v -23.9); pulse ring r 10 -> 34.
- Annotation `wc2-ann` (chip 2): glass pill, radius 14, padding 8 px 18 px, left 1125, top 752 (box about x 1125-1575, y 752-798), Arial Black 900 30 px `#f2f5f8`: "-24°F · 5:18 AM SAT". Leader 2 px `#e74c3c` from the marker edge (1105, 748) to (1125, 772). Curve above it in that x span is at y 605-718: gap at least 34 px (verify).
- Chip 1: glass chip `left:110px; bottom:110px`, Arial Black 900 52 px `#f2f5f8`: "WIND CHILL BELOW -10°F" (x about 110-910, y about 862-970); a 14 x 14 swatch of the band colour leads the text so the chip names the band.
- Eyebrow, Arial 700 22 px `#93a3b2` tracking 6, `left:96px; top:96px`: "BUFFALO AIRPORT · FRI DEC 23 TO SAT DEC 24".
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Buffalo airport ASOS, IEM archive".
- Type tiers: 52 big, 30 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. The line passes through every table point within 2 px (spot-check 06:18 Fri, 12:33 Fri, 05:18 Sat, 15:54 Sat; print them).
2. The line crosses 0 between 10:54 and 11:43 Fri (x 404.5-435.2) and first sits below -10 at 12:33 Fri (x 466.6).
3. The band's left edge is at 12:33 Fri and its right edge at 14:45 Sat; the band is 26.2 h wide (986.4 px). Nothing on screen says "late morning".
4. The low marker is the lowest point of the line and sits at 05:18 Sat, -23.9 (rendered as -24).
5. No label sits under the line, the marker, the band edge or another label, including mid-draw.
6. Only two figures carry the beat as chips: "-10°F" and "-24°F"; axis labels are the scale. Declare `data-repeat-ok="axis scale label"` on the "-10" axis leaf after the frame read if overlap_check flags it with chip 1.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S10 start, `audio/a3-s10.words.json`; its first word is "outside" @0.00, "And" is not transcribed)
Strings: axis title, 7 value labels, 6 time labels, eyebrow, `WIND CHILL BELOW -10°F`, `-24°F · 5:18 AM SAT`, `Buffalo airport ASOS, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "outside the car" | ground on frame 0; gridlines, axes and labels fade in 0.0-0.6; eyebrow, axis title, source in at 0.3 |
| 1.18 | "airport's weather station" @1.18 | line draws Fri 06:00 -> 12:33 (x 220 -> 466.6), 1.18-3.62, power1.inOut (it passes 0 near 3.2) |
| 3.62 | "minus 10." @3.62-4.00 | -10 dashed line draws left to right 0.5 s; chip 1 in at 4.00 `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` |
| 5.44 | "from late Friday morning" @5.44 | band `scaleX 0 -> 1` 5.44-7.80, power1.inOut; line keeps drawing to the end (x 1500) over 5.44-8.20, its head kept at or ahead of the band edge |
| 8.34 | "more than a day." @8.34 | band brightens (.18 -> .28 -> .18, 0.8 s) |
| 9.84 | "At its coldest," @9.84 | chip 1 out `to(x:-80, autoAlpha 0, 0.4, power3.in)`; marker in `fromTo(scale 0 -> 1, 0.35, back.out(2))`, ring pulses every 1.2 s (finite to host end) |
| 10.96 | "5 in the morning on Christmas Eve" @10.96 | the "SAT 6 AM" tick label brightens to `#f2f5f8` 0.3 s |
| 13.38 | "24 below." @13.38 | leader draws 0.25 s; annotation `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)` at 13.50 |
| 15.06-20.32 | "The air itself ... bare skin." | line glints: a 60 px highlight travels along the line once (2.5 s), marker pulse continues |
| 20.78 | "Andal was waiting in her car" @20.78 | band pulses slowly twice (.18 -> .30), 1.2 s each |
| 23.12-23.72 | after "stretch." @23.38 | annotation, marker, line out `to(autoAlpha 0, 0.6, power3.in)`; ground stays |
Comp duration 23.72 s.

## 6. CONTRACT
One file `compositions/g-a3-12-windchill-chart.html`, root `id="g-a3-12-windchill-chart-root"`, `data-composition-id="g-a3-12-windchill-chart"`, PAUSED timeline `window.__timelines["g-a3-12-windchill-chart"]`. Prefix `wc2-` (not `wc-`: g-a3-7 uses it). Points as a JS array copied from §1; coordinates computed by the §2 formulas in the page. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-12-windchill-chart`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-12-windchill-chart`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print the band x edges, marker xy and the four spot-check points.

## 8. RECEIPT
As the template.
