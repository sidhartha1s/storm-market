# g-intro-3-asos-log · T1-S1 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
FAMILY BASE: `g-intro-4-morning-map` (Opus) reuses this card exactly (same panel, same rows, same px). Build this one first; the orchestrator reads it full size before g-intro-4 copies it. Do not change the section 3 numbers without saying so in the receipt.

## 0. What this graphic claims
The Buffalo airport's own weather log for Friday 23 Dec 2022 shows the morning turning in about 75 minutes: rain at 7:24, snow at half a mile by 8:06, heavy blowing snow at a quarter mile by 8:39, gusts climbing with it. No numbers are spoken in this segment; the log is the proof the narrator says he read.

## 1. SOURCE
- Buffalo Niagara International Airport ASOS (station BUF), IEM archive, local time (EST):
  https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=BUF&data=tmpf&data=sknt&data=gust&data=vsby&data=mslp&data=wxcodes&data=feel&year1=2022&month1=12&day1=22&year2=2022&month2=12&day2=27&tz=America%2FNew_York&format=onlycomma&latlon=no&missing=M&trace=T&direct=no&report_type=3&report_type=4 (`research/nws.md` fetch notes).
- Rows as read from that feed (re-fetched 26 Oct 26 by the brief writer), with research rows:
  | local time | wxcodes | vis (mi) | gust (kt) | research row |
  |---|---|---|---|---|
  | 07:24 | -RA BR | 5.00 | 21 | `research/nws.md` 2.2 (gust 21 kt, 38 F); rain: `factcheck/intro-r2.md` row 11. VIS 5 MI: live feed only, NO research row (flagged to the orchestrator) |
  | 08:06 | SN FG | 0.50 | 52 | `research/nws.md` 2.2 |
  | 08:39 | +SN BLSN | 0.25 | 58 | `research/nws.md` 2.3 |
- Gust in mph = kt x 1.15078, rounded: 21 kt = 24 MPH, 52 kt = 60 MPH, 58 kt = 67 MPH (`research/nws.md` 3.1 itself gives 58 kt as 67 mph). Computed by the brief writer; not yet a fact-check row (flagged).
- Plain-word weather: -RA BR = light rain and mist, shown "RAIN"; SN FG = snow and fog, shown "SNOW"; +SN BLSN = heavy snow, blowing snow, shown "HEAVY SNOW, BLOWING SNOW".
- Fact check: `factcheck/intro-r3.md` rows 11 and 12 (rows 7:24, 8:06, 8:39; chip "FRIDAY · DEC 23"; source line CONFIRMED).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, full-frame designed graphic on the channel ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` (tokens.md "Canvas"). A table, no spatial scale. Corner x >= 1600, y >= 680 stays empty (the presenter circle may be on: a graphics-only scene with an empty corner keeps it).

## 3. GEOMETRY (px; shared with g-intro-4)
- Panel `lg-panel`: x 160 to 1560 (w 1400), y 170 to 760 (h 590), radius 28, fill `linear-gradient(180deg, #15202b, #0b1016)`, 1 px border `rgba(255,255,255,.14)`.
- Eyebrow: "BUFFALO AIRPORT WEATHER STATION", Arial 700 22 px `#93a3b2`, letter-spacing 6, left 220, top 206.
- Headline chip: "FRIDAY · DEC 23", Arial Black `font-weight:900` 52 px `#f2f5f8`, left 220, top 244 (glyph box about 244 to 300).
- Column headers, Arial 700 19 px `#93a3b2`, letter-spacing 4, top 340: "TIME" at x 220, "WEATHER" at x 470, "VISIBILITY" at x 1020, "GUST" at x 1300.
- Divider: 1 px `rgba(255,255,255,.14)`, x 220 to 1500, y 376.
- Rows, Courier New 700 34 px, line box 60 px, row pitch 100 px; time cells `#e8c56a` (Amber 2), other cells `#dfe7ee`:
  | row | top y | TIME (x 220) | WEATHER (x 470) | VISIBILITY (x 1020) | GUST (x 1300) |
  |---|---|---|---|---|---|
  | R1 | 400 | 7:24 AM | RAIN | 5 MI | 24 MPH |
  | R2 | 500 | 8:06 AM | SNOW | 1/2 MI | 60 MPH |
  | R3 | 600 | 8:39 AM | HEAVY SNOW, BLOWING SNOW | 1/4 MI | 67 MPH |
  Widest cell: "HEAVY SNOW, BLOWING SNOW", 24 characters at about 20.4 px = about 490 px, so x 470 to 960, clear of x 1020.
- Scan line `lg-scan`: 2 px, `#d8a13a` at 0.45 opacity, x 180 to 1540, travels y 380 to 700 (continuous motion).
- Source line: "Buffalo airport ASOS observations, IEM archive", Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers: 52 (big), 34/30-band mid (34), 19 to 22 (small).
- Frame coverage: the panel is 41 % of the frame on a designed full-frame ground; no black block.

## 4. MUST BE TRUE IN THE PICTURE
1. Three rows only, in time order top to bottom: 7:24 AM, 8:06 AM, 8:39 AM.
2. Visibility falls down the column 5, 1/2, 1/4 and gust rises 24, 60, 67: every value exactly as section 3, no other figures (no temperatures in this graphic; the falling temperature belongs to Act 2).
3. Every cell sits in its column (left edges within 10 px of the column x) and no cell touches the next column.
4. The chip reads "FRIDAY · DEC 23" (Friday 23 Dec 2022 is the day before Christmas Eve, as spoken).
5. Each row appears on its cue word, never before.
6. Nothing enters x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from T1-S1 start, `audio/t1-s1.words.json`)
Strings: `BUFFALO AIRPORT WEATHER STATION` · `FRIDAY · DEC 23` · `TIME` `WEATHER` `VISIBILITY` `GUST` · row cells per section 3 · `Buffalo airport ASOS observations, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0 | ground on; panel hidden (CSS opacity 0) |
| 0.54 | "Buffalo" @0.54 | panel in: `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`; source line `fromTo(autoAlpha 0, y:12 -> 0, 0.4)` |
| 0.84 | "Airport's" @0.84 | eyebrow `fromTo(autoAlpha 0, x:-20 -> 0, 0.4, power3.out)` |
| 1.42 | "weather" @1.42 | column headers stagger 0.06 `fromTo(autoAlpha 0, y:10 -> 0, 0.3)`; divider `scaleX 0 -> 1, 0.5, power2.out, transformOrigin left center` |
| 1.58 | "log" @1.58 | R1 cells type in left to right, stagger 0.08: `fromTo(autoAlpha 0, x:-16 -> 0, 0.3, power3.out)`; scan line starts: `fromTo(y:380 -> 700, 5.2 s, ease none)` (about 62 px/s) |
| 2.30 | "Friday," @2.30 | chip "FRIDAY · DEC 23" `fromTo(autoAlpha 0, scale 1.15 -> 1, 0.4, power4.out)` |
| 4.86 | "shows" @4.86 | R2 cells, same as R1 |
| 5.32 | "fast" @5.32 | R3 cells, same as R1 |
| 5.84 | "morning" @5.84 | R3 time cell `fromTo(scale 1 -> 1.08 -> 1, 0.4)` pulse (no colour change: g-intro-4 owns the 8:39 highlight) |
| 0.6 to 6.4 | whole hold | panel float `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats |
| 6.40 to 7.00 | after "turned." @6.06 | exit, fade-through: panel, rows, chip, source `to(autoAlpha 0, y:-20, 0.6, power2.in)`; ground stays |
Comp duration 7.0 s. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-intro-3-asos-log.html`, root `<div id="g-intro-3-asos-log-root" data-composition-id="g-intro-3-asos-log" data-width="1920" data-height="1080">` with the ground gradient on the root (full-frame host: ground on from frame 0). PAUSED timeline at `window.__timelines["g-intro-3-asos-log"]`. Ids prefixed `lg-`, classes `lg-*`. Cell text pre-authored per element, toggled with autoAlpha. Start-hidden in CSS too. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-3-asos-log`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-3-asos-log`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: column x and row y come from the table above; state them in the receipt.

## 8. RECEIPT
As the template.
