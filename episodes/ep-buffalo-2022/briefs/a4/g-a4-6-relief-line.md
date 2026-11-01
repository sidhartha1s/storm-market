# g-a4-6-relief-line · A4-S5 (14.90 s to end) · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, `references/editing-patterns/ep3-map-route-fit.html`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/master-map-us-canada.html` (real Natural Earth basemap, its land/water/line styling); use the same data sources and map styling as the built `compositions/g-intro-4-morning-map.html` so the episode's maps match. Follows `g-a4-5-response-clock` in the same segment and opens on the same ground.

## 0. What this graphic claims
Erie County's dispatchers were worn out, so Dutchess County, in the Hudson Valley at the other end of New York State, sent four of its own dispatchers to the Erie County 911 center in Cheektowaga, Friday to Monday (30 Dec to 2 Jan), the weekend after Christmas.

## 1. SOURCE
- dutchessny.gov County Executive page 44052, posted Thu 29 Dec 2022 (PRIMARY): four Public Safety Dispatchers to the Erie County 911 Communication Center, Town of Cheektowaga, Friday through Monday, requested by Erie County so its dispatchers could rest. `research/response.md` section 2; `factcheck/a4-r1.md` rows 14 and 16 (dates derived: 30 Dec to 2 Jan; "FRI TO MON" is printed, the dates are not).
- Map geometry (public domain; land the data in `episodes/ep-buffalo-2022/media/map/` or inline the paths, never a path outside the repo):
  - New York and neighbouring states, Ontario, the US-Canada border: Natural Earth 10m `ne_10m_admin_1_states_provinces`; Lakes Erie and Ontario: `ne_10m_lakes`.
  - Dutchess County (GEOID 36027) and Erie County (GEOID 36029): US Census `cb_2022_us_county_500k`.
  - Cheektowaga pin: the interior point of the Town of Cheektowaga, Census `cb_2022_36_cousub_500k` (expected about 42.909 N, 78.747 W). Dutchess label anchor: the county's interior point (expected about 41.755 N, 73.739 W). Report the values you used.

## 2. DATUM, SCALE, ORIENTATION
- North up. Equirectangular with a cosine correction at 42.75° N (cos = 0.7343).
- Scale: 200 px per degree of latitude; 146.86 px per degree of longitude.
- Datum: (75.8° W, 42.75° N) = screen (960, 540). `x = 960 + (lon + 75.8) * 146.86`, `y = 540 - (lat - 42.75) * 200` (lon negative west).
- New York then spans about x 378 (79.76° W) to 1539 (Long Island's east tip, 71.86° W) and y 88 (45.0° N) to 990 (40.5° N). Compute every path with a script and state the numbers in the receipt (7a item 6).

## 3. GEOMETRY (px)
- Ground: channel radial gradient from frame 0 (continues g-a4-5's ground). Land outside New York `#0b1016`; New York `#15202b`; water `#04070a` with 1.5 px `#5a768f` shoreline; state lines 1 px `#2a3644`; US-Canada border dashed 6/6 `#2a3644`.
- Erie County outline: 1.5 px `#93a3b2`, no fill.
- Cheektowaga pin (expected (527.2, 508.2), ±10 px): 9 px `#e74c3c` dot + 2 px ring pulsing (scale 1 -> 2.2, opacity 0.6 -> 0, 1.2 s, finite repeats) while visible. Label "ERIE COUNTY 911 CENTER", Arial 700 22 px `#f2f5f8`, letter-spacing 3, centred on x 527, baseline y 466 (above the pin, 37 px clear of the line).
- Dutchess County: fill `rgba(216,161,58,.25)`, outline 3 px `#d8a13a`; interior point expected (1262.7, 739.0). Label "DUTCHESS COUNTY", Arial 700 22 px `#d8a13a`, letter-spacing 3, right edge x 1220, baseline y 790 (below-left of the county, clear of the line). Sub "Hudson Valley", Georgia italic 26 px `#d8a13a`, right edge x 1220, baseline y 826.
- Relief line: quadratic Bezier from Dutchess (1262.7, 739.0) via control (895, 503) to Cheektowaga (527.2, 508.2); 4 px `#e8c56a`, round cap, drawn with stroke-dashoffset (length = ceil(measured) + 1). It is a gentle arc, NOT a road route: no route is sourced.
- Four headset icons (36 px, `#f2f5f8` outline, 2.5 px stroke) ride behind the line's head, spaced 0.06 of the path apart, moved by per-leg GSAP tweens through 20 sampled Bezier points (MotionPathPlugin is not bundled). On arrival they settle in a 2 x 2 cluster centred 50 px right of the pin: (562, 498), (598, 498), (562, 534), (598, 534) (no overlap with the label or pin ring).
- Chip (glass as `g-intro-2-toll-chips`, padding 22 px 34 px, `left:110px; bottom:110px`): "4" Arial Black `font-weight:900` 84 px `#f2f5f8` + 16 px gap + "DISPATCHERS" Arial Black 900 38 px `#dfe7ee`, then " · FRI TO MON" Arial 700 30 px `#e8c56a` (a separate span revealed later). About x 110 to 820, y 842 to 970 (over Pennsylvania, unlabelled land).
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Corner x >= 1600, y >= 680: Long Island and the Atlantic lie at x <= 1539; the corner holds only water and land fill, no label, no line.
- Type tiers: 84 (big), 26 to 38 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. Dutchess County sits in the Hudson Valley, south-east New York (x about 1263), Cheektowaga at the western end (x about 527): the line spans about 736 px of the state's 1,161 px width (about 267 miles straight line; that number is NOT printed).
2. The Cheektowaga pin is inside the Erie County outline, east of Buffalo, within ±10 px of (527.2, 508.2).
3. Exactly four headset icons; the chip's "4" and the icon count match.
4. The line starts at Dutchess and ends at the pin; the icons sit on the line head at three checked times (20.3, 20.8, 21.3 s) and never leave it.
5. "FRI TO MON" appears only from "weekend" @21.98; no calendar date is printed.
6. No label sits on the line, a county outline or another label; no text rides any move (there is no camera move in this comp).

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S5 start, `audio/a4-s5.words.json`; comp-local = S5 time - 14.90)
Strings: `ERIE COUNTY 911 CENTER` · `DUTCHESS COUNTY` · `Hudson Valley` · chip `4 DISPATCHERS · FRI TO MON` · source `Dutchess County Executive, 29 Dec 2022`

| S5 t (s) | local | spoken word | action |
|---|---|---|---|
| 14.90 | 0.00 | "The dispatchers" @14.90 / 15.00 | ground on from frame 0; map layers in `fromTo(autoAlpha 0 -> 1, scale 1.03 -> 1, 0.7, power2.out)` (start state hidden in CSS) |
| 15.30 | 0.40 | "dispatchers" @15.00 | Erie outline and Cheektowaga pin in (pin `fromTo(scale 0 -> 1, 0.35, back.out(1.8))`), label `fromTo(autoAlpha 0, y:8 -> 0, 0.35)` |
| 15.78 | 0.88 | "worn out" @15.78 | pin ring pulse starts |
| 17.16 | 2.26 | "Dutchess" @17.16 | Dutchess fill and outline in `fromTo(autoAlpha 0 -> 1, 0.4)`; label in; source pill in |
| 18.58 | 3.68 | "Hudson Valley" @18.58 | "Hudson Valley" sub in `fromTo(autoAlpha 0, x:10 -> 0, 0.35)` |
| 19.76 to 21.80 | 4.86 to 6.90 | "sent four of its own to cover for them" | line draws, `power1.inOut`; headsets ride it |
| 19.86 | 4.96 | "four" @19.86 | chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` with "4 DISPATCHERS" only; "4" `fromTo(scale 1.3 -> 1, 0.4, power4.out)` |
| 21.80 to 22.20 | 6.90 to 7.30 | "over the" @21.52 to 21.82 | headsets settle into the 2 x 2 cluster, 0.4 s back.out(1.4) |
| 21.98 | 7.08 | "weekend" @21.98 | " · FRI TO MON" span in `fromTo(autoAlpha 0, x:-10 -> 0, 0.35)` |
| whole window | | | pin ring pulse; headsets bob 2 px after landing, finite repeats; the map group drifts `scale 1 -> 1.02` over the window (small, linear) |
| 23.29 | 8.39 | wav end | full-frame scene ends on the hard cut into the S6 photo |

Comp duration 8.39 s (host = A4-S5 start + 14.90 to the end of the S5 wav).

## 6. CONTRACT
One file `compositions/g-a4-6-relief-line.html`, root `<div id="g-a4-6-relief-line-root" data-composition-id="g-a4-6-relief-line" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-6-relief-line"]`. Ids prefixed `rl-`; classes prefixed `rl-`. No static SVG `transform=` on any mover; dash length measured. Ground on from frame 0. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-6-relief-line`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-6-relief-line`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: projection, county paths, both anchor points and the Bezier samples computed by a script; state the anchor points in the receipt. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
