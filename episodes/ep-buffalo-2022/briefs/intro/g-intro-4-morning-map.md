# g-intro-4-morning-map · I1-S1 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, `references/editing-patterns/ep3-map-route-fit.html`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/master-map-us-canada.html` (real Natural Earth basemap + camera move) and the built `compositions/g-intro-3-asos-log.html` (copy its panel and rows exactly; it is the family base and is read full size before you copy it). Push uses `logZoom` from `library/inhouse/snippets/helpers.js` (the move is 2.4x).

## 0. What this graphic claims
1. Where: Buffalo sits at the east end of Lake Erie, in Erie County, western New York, and the weather log comes from its airport.
2. When: before dawn it was raining at about 38°F; by 8:39 AM visibility at the airport was down to a quarter mile; Erie County's driving ban took effect at 9:30 AM, 51 minutes later. The 51-minute gap between the whiteout and the ban is the beat.

## 1. SOURCE
- ASOS rows (7:24 rain 38 F; 8:06; 8:39 vis 1/4 mi, +SN BLSN): `research/nws.md` 2.1, 2.2, 2.3, IEM ASOS URL in its fetch notes; values and the mph conversion exactly as `briefs/intro/g-intro-3-asos-log.md` section 1 (VIS 5 MI and the mph gusts have no research row yet: flagged to the orchestrator).
- 38°F with rain before dawn: `research/nws.md` 2.1 (37 to 39 F, rain, midnight to 6 AM) and 2.2 (38 F at 7:24); `factcheck/intro-r2.md` row 11 ("7:24 rain, 38 F").
- Driving ban effective 9:30 AM Fri 23 Dec, Erie County: `research/response.md` section 1, WKBW https://www.wkbw.com/news/local-news/erie-county-driving-ban-effective-9-30-a-m-friday (SECONDARY).
- 51 minutes = 8:39 to 9:30 (`factcheck/intro-r3.md` row 17; `edit_script.md` I1-S1 rows).
- Fact check of every on-screen string: `factcheck/intro-r3.md` row 17 ("38°F · RAIN", "VIS 1/4 MI · 8:39 AM", "DRIVING BAN · 9:30 AM", map labels, sources CONFIRMED).
- Map geometry (public domain, drawn by you; land the data in `episodes/ep-buffalo-2022/media/map/` or inline the paths, never a path outside the repo):
  - Lakes Erie and Ontario: Natural Earth 10m `ne_10m_lakes`.
  - Land, US-Canada border, state lines (NY, PA, OH; Ontario): Natural Earth 10m `ne_10m_admin_0_countries` / `ne_10m_admin_1_states_provinces`.
  - Erie County, NY outline: US Census cartographic boundary `cb_2022_us_county_500k`, GEOID 36029 (includes Grand Island).
  - Buffalo Niagara International Airport (ASOS BUF): 42.9405 N, 78.7322 W (IEM station metadata for BUF; check it on the IEM station page and report the value you used).

## 2. DATUM, SCALE, ORIENTATION
- North up. Equirectangular with a cosine correction at 42.6° N (cos = 0.7357).
- Scale: 540 px per degree of latitude; 397.3 px per degree of longitude.
- Datum: map point (79.3° W, 42.6° N) = screen (960, 540) in the unpushed state.
- `x = 960 + (lon + 79.3) * 397.3`, `y = 540 - (lat - 42.6) * 540` (lon negative west). Frame spans 81.716° W to 76.884° W, 43.6° N to 41.6° N.
- Compute every path from data with a script and state the numbers in the receipt (7a item 6); never place a coastline by eye.

## 3. GEOMETRY (px, unpushed state unless stated)
- Ground: channel radial gradient (tokens.md "Canvas") on the root from frame 0. Land `#15202b`; water `#0b1016` with a 1.5 px `#5a768f` shoreline; state and border lines 1 px `#2a3644` (border dashed 6/6).
- Expected anchor points (hit within ±10 px):
  - BUF airport pin: (1185.6, 356.1). Pin = 9 px radius `#e74c3c` dot + a 2 px `#e74c3c` ring that pulses (scale 1 -> 2.2, opacity 0.6 -> 0, 1.2 s, finite repeats) for the whole time it is visible.
  - Buffalo City Hall (42.8864 N, 78.8784 W) = (1127.5, 385.3): the east end of Lake Erie sits just west and south of it.
  - Erie County bounding box: about x 956 to 1294, y 270 to 626 (data wins; report the computed box). Outline 3 px `#d8a13a`, fill `rgba(216,161,58,.08)`.
  - Lake Erie runs off the left edge of the frame (x = 0 is 81.7° W, mid-lake).
- Labels (map layer, Arial 700, letter-spacing 3 unless stated; every label sits next to what it names and on no line):
  - "LAKE ERIE": 26 px `#7fb2e5` (Cold blue 2), centred near (80.6° W, 42.3° N) = (443, 702); must sit wholly on water.
  - "WESTERN NEW YORK": 26 px `#93a3b2`, letter-spacing 8, left edge x 1320, centre y 460 (inside New York, right of the county outline, clear of it by 20 px or more).
  - "ERIE COUNTY": 22 px `#d8a13a`, inside the outline near its centroid (about 1120, 520), clear of the airport label. (Added to the Picture line's two labels so the outline is not unnamed; the voice says "Erie County" at 12.00.)
  - "BUFFALO AIRPORT": 22 px `#f2f5f8`, left edge at pin x + 20, centre y at pin y.
- Corner x >= 1600, y >= 680 holds no label (it is southern-tier New York, unlabelled land).
- Push (3.14 to 3.84): one `logZoom` on the map group from scale 1 to 2.4 with translate (-1125.4, -554.6), so the pin lands at screen (1720, 300). After the push the map group dims to opacity 0.3. All map labels are at autoAlpha 0 before the push starts (no text rides the move). The pin and its ring stay visible at (1720, 300).
- Card (after the push, HUD layer, does not move with the map): the panel, eyebrow, headline chip "FRIDAY · DEC 23", headers, divider and rows R1 to R3 at exactly the g-intro-3 px (panel x 160 to 1560, y 170 to 760; rows top 400, 500, 600; columns 220, 470, 1020, 1300). Rows R1 to R3 come in at opacity 0.45 (the card "returns").
- Link line: 1 px `#d8a13a`, from panel right edge (1560, 300) to the pin (1711, 300).
- R1 weather cell: the leaf "RAIN" is swapped (autoAlpha crossfade, two pre-authored leaves) for "38°F · RAIN" in `#d8a13a`, same position (x 470, row top 400). No other temperature anywhere.
- 8:39 highlight (the Picture's "VIS 1/4 MI · 8:39 AM" is the lit row itself, not a second chip, so the fact shows once): R3 at opacity 1; a 4 px `#e74c3c` rule at x 200, y 600 to 660; a glass box `rgba(255,255,255,.08)` with 1 px `rgba(255,255,255,.22)` border behind the VIS cell, x 1005 to 1165, y 592 to 668.
- Ban chip (NOT an airport observation, so it sits outside the panel, crimson, never styled as a row): x 640 to about 1310, y 800 to 880, fill `#8e2020` (Crimson), radius 10. Clock icon 56 px at centre (688, 840): `#f4f0e8` ring and two hands, hands set to 9:30. Text "DRIVING BAN · 9:30 AM", Arial Black `font-weight:900` 38 px `#f4f0e8`, left edge x 736.
- 51 connector: path `M 250 664 V 840 H 630`, 3 px `#d8a13a`, drawn with strokeDashoffset (length = ceil(measured)+1). Label "51 MIN", Courier New 700 36 px `#e8c56a`, left edge x 300, glyph box y about 786 to 822 (18 px above the horizontal leg; never on the line).
- Source slot: Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`, one string at a time.
- Type tiers: 52 (chip), 34/36/38 mid, 19 to 26 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Buffalo and the airport pin sit at the EAST end of Lake Erie; the lake runs off the left edge; Lake Ontario (unlabelled) is to the north. North is up.
2. The pin is inside the Erie County outline, north-east of Buffalo City Hall, within ±10 px of (1185.6, 356.1) before the push and of (1720, 300) after it.
3. Every map label is gone before the camera moves; no text rides the push.
4. Reading order on the card follows the voice: 38°F · RAIN (7:24 row), then the 8:39 row, then its 1/4 MI cell, then the crimson ban chip, then the 51 MIN connector.
5. The connector starts at the 8:39 row and ends at the ban chip, so the picture says 8:39 + 51 min = 9:30. The ban chip is visibly not part of the airport table.
6. Only one source line at a time; it names the thing on screen (ASOS for the card, WKBW once the ban chip lands).
7. Nothing in x >= 1600, y >= 680 except nothing: the corner stays empty (the pin at y 300 is outside it).
8. No value differs from g-intro-3's table, and no temperature other than 38°F appears.

## 5. PANEL TEXT (exact) and CUES (seconds from I1-S1 start, `audio/i1-s1.words.json`)
Strings: `LAKE ERIE` · `WESTERN NEW YORK` · `ERIE COUNTY` · `BUFFALO AIRPORT` · card strings exactly as g-intro-3 · `38°F · RAIN` · `DRIVING BAN · 9:30 AM` · `51 MIN` · sources `Buffalo airport ASOS, IEM archive` then `Erie County driving ban, WKBW`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Before" @0.00 | ground, land, water and lines on from frame 0 (land and water `fromTo(autoAlpha 0.6 -> 1, 0.5)`, map group `to(scale 1.0 -> 1.0)` none: the map does not drift before the push) |
| 0.30 | "dawn," @0.30 | "LAKE ERIE" `fromTo(autoAlpha 0, y:12 -> 0, 0.4, power3.out)` |
| 0.90 | "if" @0.90 | Erie County outline draws, strokeDashoffset, 0.9 s, power2.inOut; fill fades in after |
| 1.18 | "getting" @1.18 | "WESTERN NEW YORK" in (as LAKE ERIE) |
| 1.78 | "work" @1.78 | "ERIE COUNTY" in (as LAKE ERIE) |
| 2.16 | "Buffalo," @2.16 | pin drops `fromTo(y:-30 -> 0, scale 0.4 -> 1, autoAlpha 0 -> 1, 0.45, back.out(1.7))`; ring pulse starts; "BUFFALO AIRPORT" in at 2.30 |
| 2.95 to 3.14 | before "raining" | all four map labels `to(autoAlpha 0, 0.19)` |
| 3.14 to 3.84 | "raining" @3.14 | logZoom push to 2.4x, pin to (1720, 300); map dims to 0.3 during the last 0.3 s |
| 3.84 to 4.20 | | card in at row opacity 0.45: `fromTo(y:30 -> 0, autoAlpha 0 -> 1, 0.36, power3.out)`; link line `scaleX 0 -> 1`; source "Buffalo airport ASOS, IEM archive" in |
| 4.22 | "38" @4.22 | R1 to opacity 1; "RAIN" leaf out / "38°F · RAIN" leaf in, `fromTo(scale 1.2 -> 1, 0.4, power4.out)` |
| 6.00 | "8" @6.00 (Whisper "8 .39") | R1 back to 0.45; R3 to opacity 1; red rule `fromTo(scaleY 0 -> 1, 0.35, transformOrigin top)`; R3 time cell pulse scale 1 -> 1.08 -> 1 |
| 7.92 | "snow" @7.92 | R3 weather cell brightens to `#ffffff`, 0.3 s |
| 10.56 | "quarter" @10.56 | glass box behind the VIS cell `fromTo(autoAlpha 0, scale 0.9 -> 1, 0.35)`; "1/4 MI" to `#ffffff`, `fromTo(scale 1 -> 1.12, 0.3, power3.out)` then hold at 1.08 |
| 12.46 | "driving" @12.46 | ban chip in `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; clock hands `fromTo(rotation to 9:30 from 8:39 position, 0.6, power2.out)`; source swaps to "Erie County driving ban, WKBW" (old `to(autoAlpha 0, y:-8, 0.2)`, new `fromTo(autoAlpha 0, y:8 -> 0, 0.3)`) |
| 13.70 | "51" @13.70 | connector draws (strokeDashoffset, 0.7 s, power2.inOut) from the 8:39 row to the chip; "51 MIN" `fromTo(autoAlpha 0, y:10 -> 0, 0.35)` at 14.00 |
| 15.44 to 18.70 | "Anyone already on the road ... how long this would last." | hold; clock minute hand keeps turning `to(rotation +120, 3.3 s, ease none)` (time passing, no text); pin ring keeps pulsing; card float `y 0 -> -4`, `sine.inOut`, finite yoyo |
| 18.90 to 19.50 | after "last." @18.64 | exit, fade-through: everything `to(autoAlpha 0, 0.6, power2.in)` except the ground |
Comp duration 19.6 s. Spoken time in a comment at each tween. No gap of 4 s without motion (the ring pulse and clock carry the holds).

## 6. CONTRACT
One file `compositions/g-intro-4-morning-map.html`, root `<div id="g-intro-4-morning-map-root" data-composition-id="g-intro-4-morning-map" data-width="1920" data-height="1080">` with the ground on it. PAUSED timeline at `window.__timelines["g-intro-4-morning-map"]`. Ids prefixed `mm-`; classes `mm-*` (do not reuse g-intro-3's `lg-` names: both comps may be in the DOM). No static SVG `transform=` on anything GSAP moves; nested SVG pivots use `svgOrigin`. Map paths computed by a one-shot script from the data files (content-blind arithmetic, not committed), pasted as path data. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-4-morning-map`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-4-morning-map`. Read the contact sheet against section 4 first.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: projection, pin, county box, push translate and connector length printed by your script and stated in the receipt. Item 4 (seek order) at 4.22, 6.00, 10.56, 12.46, 13.70.

## 8. RECEIPT
As the template, plus the computed county box and the airport coordinate you used.
