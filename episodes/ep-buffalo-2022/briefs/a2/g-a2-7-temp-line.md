# g-a2-7-temp-line · A2-S5 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: official block `mk-line-graph` (`library/catalog-index.json`; it lands in `library/official/`, copy it into the episode and retune to tokens.md; drop its fonts and colours).

## 0. What this graphic claims
The airport's air temperature fell all Friday morning, from 38°F at 7:24 AM to 12°F at 12:54 PM: down 26°F in about 5.5 hours, crossing freezing early (about 8:14). The people who left at 7:00 drove into the start of it.

## 1. SOURCE
- 38°F at 7:24 AM, 12°F at 12:54 PM, 26°F in about 5.5 h: `research/nws.md` 3.4 (PRIMARY derived); `factcheck/a2-r1.md` rows 17 and 20 (CONFIRMED: "38 - 12 = 26; 7:24 to 12:54 = 5 h 30 min").
- 33.0°F at 8:06 and 28.9°F at 8:39: `factcheck/a2-r1.md` rows 10 and 13 (ASOS). Plotted as dots, not labelled.
- Crossing of 32°F: linear between 8:06 (33.0) and 8:39 (28.9) = 8:14 (computed here: 66 + 33 x 1.0/4.1 = 74.05 min after 7:00). The voice says "about a quarter past eight" in A2-S3.
- Readings between 8:39 and 12:54 are NOT in research: that stretch is a dashed straight line with no dots (it says "fell from here to there", not the path).
- Chip text changed from the Picture's "−26°F IN ~5.5 HRS" to "DOWN 26°F IN ~5.5 HRS": "−26°F" reads as a temperature of minus 26.
- Source line "Buffalo airport ASOS, IEM archive".

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed graphic, channel ground on the root from frame 0.
- x: 7:00 AM at x 260 to 1:00 PM at x 1300, 2.8889 px per minute (x = 260 + minutes after 7:00 x 1040/360).
- y: 40°F at y 260 to 10°F at y 740, 16 px per °F (y = 260 + (40 - T) x 16).

## 3. GEOMETRY (px)
- Axes: x axis 1 px `rgba(255,255,255,.25)` at y 740 from x 260 to 1300; y axis 1 px same at x 260 from y 260 to 740.
- x tick labels, Arial 700 19 px `#93a3b2`, centred under ticks, glyph box y 756 to 780: "7 AM" 260 · "8" 433.3 · "9" 606.7 · "10" 780 · "11" 953.3 · "12 PM" 1126.7 · "1 PM" 1300. Ticks 6 px.
- y tick labels, Arial 700 19 px `#93a3b2`, right-aligned at x 244: "40°F" y 260 · "30°F" y 420 · "20°F" y 580 · "10°F" y 740.
- Freezing line: 2 px `#c0392b` (Danger red 1), y 388, x 260 to 1300; label "32°F" Arial 700 22 px `#c0392b`, left 1312, centre y 388.
- Data dots (8 px radius `#f2f5f8`) and line (4 px `#f2f5f8`):
  | point | x | y |
  |---|---|---|
  | 7:24 AM, 38°F | 329.3 | 292 |
  | 8:06 AM, 33.0°F | 450.7 | 372 |
  | 8:39 AM, 28.9°F | 546.0 | 437.6 |
  | 12:54 PM, 12°F | 1282.7 | 708 |
  Solid line through the first three; dashed (14/10) from 8:39 to 12:54. Line colour turns `#7fb2e5` (Cold blue 2) below y 388 (gradient stop at the crossing, or two paths).
- Crossing marker: ring 14 px radius 3 px `#c0392b` at (473.9, 388), pulsing (scale 1 -> 1.6, opacity 0.7 -> 0, 1.2 s, finite repeats).
- Start label "38°F · 7:24 AM": Arial 700 22 px `#dfe7ee`, left 346, glyph box y 248 to 272.
- 38°F reference: 1 px dashed `rgba(216,161,58,.5)` at y 292 from x 329.3 to 1312.
- Drop arrow: 3 px `#d8a13a`, x 1312, from y 292 down to y 700, arrowhead 12 px at (1312, 708).
- Drop label, left 1340: "DOWN 26°F" Arial Black `font-weight:900` 52 px `#f2f5f8` glyph box y 440 to 500 (about x 1340 to 1680); "IN ~5.5 HRS" Arial 700 26 px `#dfe7ee` y 508 to 538.
- End label, left 1340, glyph box y 690 to 730, baseline-aligned: "12°F" Arial Black `font-weight:900` 38 px `#7fb2e5`, 10 px gap, "· 12:54 PM" Arial 700 22 px `#dfe7ee`; ends before x 1590 (corner x >= 1600 stays clear).
- Commute marker at 7:00: 4 px `#e8c56a` dashes over the y axis from y 260 to 740; label "LEFT FOR WORK AT 7:00" Arial 700 22 px `#e8c56a`, left 270, glyph box y 200 to 226.
- Title: eyebrow "BUFFALO AIRPORT AIR TEMPERATURE · FRI DEC 23" Arial 700 22 px `#93a3b2` letter-spacing 6, left 110, top 110.
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers 52 / 26 to 38 / 19 to 22.

## 4. MUST BE TRUE IN THE PICTURE
1. Every dot within ±2 px of the table; the line passes 32°F (y 388) at x 473.9 ±3, about a sixth of the way along the morning.
2. The arrow spans exactly 38°F to 12°F (y 292 to 708) = 26 x 16 = 416 px.
3. Only four dots; the 8:39 to 12:54 stretch is dashed and dotless.
4. "DOWN 26°F" never shows a minus sign.
5. Labels never sit on the line, the red line or the arrow (check the frame at 9.5 s).
6. Nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S5 start, `audio/a2-s5.words.json`; note the wav opens on "temperature" @0.00)
Strings: `BUFFALO AIRPORT AIR TEMPERATURE · FRI DEC 23` · tick labels · `32°F` · `38°F · 7:24 AM` · `DOWN 26°F` `IN ~5.5 HRS` · `12°F` `· 12:54 PM` · `LEFT FOR WORK AT 7:00` · `Buffalo airport ASOS, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0 | ground, axes, tick labels, freezing line and "32°F", title, source line visible; dots, line, labels hidden |
| 0.20 | "temperature" | 7:24 dot `fromTo(scale 0 -> 1, 0.3, back.out)`; start label in |
| 0.78 | "falling" @0.78 | line draws (strokeDashoffset, length ceil+1): solid part 0.78 -> 1.40, dots pop as the head passes them; crossing ring starts pulsing at 1.10 |
| 1.40 to 2.52 | "all morning. By" | dashed part draws to 12:54 (dash via a mask, so the dash pattern stays) |
| 2.52 | "1254" @2.52 | 12:54 dot pops |
| 5.42 | "12" @5.42 | end label "12°F · 12:54 PM" `fromTo(autoAlpha 0, x:-16 -> 0, 0.35, power3.out)` |
| 7.04 | "26" @7.04 | 38°F reference line draws left to right 0.4 s; arrow draws down 0.5 s, power2.in; "DOWN 26°F" `fromTo(autoAlpha 0, scale 1.15 -> 1, 0.4, power4.out)` |
| 8.58 | "five" @8.58 | "IN ~5.5 HRS" in |
| 10.74 | "left" @10.74 | commute dashes draw top to bottom 0.4 s; "LEFT FOR WORK AT 7:00" in |
| 12.92 | "start" @12.92 | first segment (7:00 to 8:14) of the line brightens: 2 px `#e8c56a` glow pass along it, 0.6 s |
| whole window | | crossing ring pulses (finite repeats); arrowhead bobs 3 px, sine, finite |
| 13.80 to 14.40 | after "it." @13.32 | exit fade-through: all but ground `to(autoAlpha 0, y:-16, 0.6, power2.in)` |
Comp duration 14.40 s.

## 6. CONTRACT
One file `compositions/g-a2-7-temp-line.html`, root `<div id="g-a2-7-temp-line-root" data-composition-id="g-a2-7-temp-line" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-7-temp-line"]`. Ids/classes `tl7-`. Point px computed from section 2's formulas in the script, not typed by eye. Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-7-temp-line`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-7-temp-line`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: print the four point px and the crossing x from the formulas in the receipt.

## 8. RECEIPT
As the template.
