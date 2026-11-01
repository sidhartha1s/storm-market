# g-a2-11-rsi: NCEI Regional Snowfall Index, #1 of 232 in the Ohio Valley (A2-S11)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/ranked-bars.html` (bar rise, value chip) and `library/inhouse/quote-card.html` (attributed quote card). Prefix `r11-`.
Sits over: nothing. Full-frame designed card on track 2, channel radial background on from frame 0.

## 0. Claim
NCEI's snowfall index has scored 232 Ohio Valley storms; this one is #1, Category 5, RSI 34.7, and NWS Charleston calls it "objectively the worst winter storm on record to affect the Ohio Valley".

## 1. Source
`research/nws-facts.md` §2 "RSI | Ohio Valley Cat 5 value 34.7 (worst of 232)" (NCEI, P) and "Ohio Valley rank | "objectively the worst winter storm on record to affect the Ohio Valley"" (RLX, P). `factcheck/a2-r1.md` rows 36 (NCEI: "worst of the 232 Ohio Valley storms"; "RSI value of 34.7 securely cements its first-place rank"; Category 5), 37 (quote matches RLX). The other 231 storms' values are NOT in research (only a secondary #2 of 24.6): they are not drawn as values.

## 2. Datum, scale, orientation
- Row of 232 dots, one per scored storm: x 170 to 1550 (1380 px), pitch 1380 / 231 = 5.974 px, dot diameter 4 px, y 800. Dot positions computed in a loop from the count, never typed.
- The 1950 storm is dot #1 at the LEFT end (x 170; rank order left to right, so "#1" reads first). Its bar rises from y 800 on a value scale: 0 at y 800, 15 px per RSI unit, 34.7 = 520.5 px (top y 279.5). Axis ticks at 0, 10, 20, 30 (y 800, 650, 500, 350) on a 2 px `#4a5560` axis at x 140, labels Arial 700 22 px `#93a3b2` right-aligned at x 130 (two-digit labels start about x 104, inside the 96 px margin).
- The other 231 dots carry no value and no bar. Under the row: "231 OTHER OHIO VALLEY STORMS · ALL RANKED LOWER" Arial 700 22 px `#93a3b2` tracking 3, centred under x 210 to 1550, y 830.

## 3. Geometry (px, 1920 x 1080)
- Title (title zone): eyebrow "NCEI REGIONAL SNOWFALL INDEX" Arial 700 22 px `#93a3b2` tracking 6, left 110, top 70; headline "OHIO VALLEY · 232 STORMS SCORED" Arial Black 900 52 px `#f2f5f8`, left 110, top 104. (edit_script board title "NCEI REGIONAL SNOWFALL INDEX · OHIO VALLEY" split eyebrow/headline; "232 STORMS SCORED" names the row the voice counts.)
- Dots `#4a5560` (diagram grey); dot #1 `#f2f5f8`.
- 1950 bar: x 162 to 178 (16 px wide), `#f2f5f8`, `scaleY` from origin bottom; a white glow under it.
- Chip beside the bar top: glass card left 200, top 260, "CATEGORY 5" Arial Black 900 58 px `#f2f5f8`, line 2 "RSI 34.7 · #1 OF 232" Arial 700 26 px `#d8a13a` tracking 2. (edit_script "CATEGORY 5 · 34.7 · #1 OF 232", same figures, "RSI" names the 34.7.) A 2 px leader from the bar top to the card's left edge.
- Quote card (second state, right half, beige cite card over the dark board): `rgba(232,222,200,.90)`, radius 18, left 760, top 240, width 840 (right 1600), padding 34 x 44, bottom about 600. Text `#2a2622`: quote Georgia italic 44 px, line-height 1.25: "“Objectively the worst winter storm on record to affect the Ohio Valley.”"; attribution Arial 700 22 px `#6b6257` tracking 4: "NWS CHARLESTON, WV". (Quote words exactly as the RLX page and factcheck row 37; capital O and the closing period are typographic only.)
- Source line "Source: NOAA NCEI; NWS Charleston WV" Arial 700 19 px `#c8d3e0`, left 110, bottom 60.
- Tiers: 58 / 52 / 44 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Exactly 232 dots (count asserted in a script line and stated in the receipt).
2. Bar height 520.5 px ±2 on the 15 px-per-unit scale: the top sits between the 30 tick (y 350) and where 35 would be (y 275).
3. No value, bar or height on any of the other 231 dots; nothing implies their values.
4. The quote is in quotation marks and attributed to NWS Charleston, WV.
5. Chip and quote card never overlap; the quote card does not cover the 1950 bar (bar x 162 to 178, card starts x 760).
6. Nothing in x >= 1600, y >= 680 (dot row ends x 1550; the caption line ends <= 1550).

## 5. Panel text (exact) and cues (`audio/a2-s11.words.json`, seconds from A2-S11 start; Whisper dropped the opening "The", first word "government" at 0.00)
Text: `NCEI REGIONAL SNOWFALL INDEX` · `OHIO VALLEY · 232 STORMS SCORED` · `0` `10` `20` `30` · `231 OTHER OHIO VALLEY STORMS · ALL RANKED LOWER` · `CATEGORY 5` · `RSI 34.7 · #1 OF 232` · `“Objectively the worst winter storm on record to affect the Ohio Valley.”` · `NWS CHARLESTON, WV` · `Source: NOAA NCEI; NWS Charleston WV`
- 0.00 "government": ground on, source line on. `/* GOVERNMENT @0.00 */`
- 0.80 "scale": eyebrow in. `/* SCALE @0.80 */`
- 2.32 "snowfall": axis draws bottom-up (0.5 s). `/* SNOWFALL @2.32 */`
- 4.06 / 5.34 / 6.64 ("fell", "spread", "people"): the axis glints once on each (keeps the 5 s explanation moving; no text).
- 8.14 "Ohio": headline in. `/* OHIO @8.14 */`
- 9.72 "232": dots stagger in left to right (each autoAlpha + scale 0 to 1, total 1.2 s, ease none), caption line in at the end. `/* 232 @9.72 */`
- 12.80 "top,": dot #1 turns white; bar rises 0 to 34.7 (`scaleY`, 0.9 s, power3.out). `/* TOP @12.80 */`
- 13.74 "Category": chip in (`fromTo` x -60 to 0, autoAlpha, 0.5 s), leader draws. `/* CATEGORY 5 @13.74 */`
- 14.74 "worst": quote card slides in (`fromTo` x 660 to 0, autoAlpha, 0.7 s, power3.out); dots 2 to 232 dim to 50 %. `/* WORST @14.74 */`
- 16.10 "there." to 20.34: attribution in at 16.10; then the card floats y 0 to -6 and the bar glow breathes (sine) through the Northeast line (voice only, no text: one idea per frame).
- Exit: last 0.6 s: quote card `to` x 980, autoAlpha 0; chip `to` x -980, autoAlpha 0 (0.6 s, power3.in).
Host: data-start = A2-S11 start, duration = 20.74 + 0.40 = 21.14 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
