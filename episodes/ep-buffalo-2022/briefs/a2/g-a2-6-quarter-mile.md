# g-a2-6-quarter-mile · A2-S4 (9.20 to 14.16) · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/moves/demo.html` and `moves.js` (camera rig, particles, counter; read `library/inhouse/moves/README.md`). Chip type pairing from BUILT `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
With a quarter mile of visibility, a driver at highway speed (60 mph) sees about 15 seconds ahead: the "1/4 MI" marker is right at the edge of the white.

## 1. SOURCE
- Visibility 1/4 mi at 8:39 AM: `research/nws.md` 2.3; `factcheck/a2-r1.md` row 13.
- 1/4 mile = 1,320 ft; 60 mph = 88 ft/s; 1,320 / 88 = 15.0 s: `acts/a2.md` A2-S4 rows ("computed"); `factcheck/a2-r1.md` row 14 (CONFIRMED arithmetic; "By 8:47 AM visibility was already 1/8 mile ... so the line is not overstated").
- "60 MPH" here is the driving speed the arithmetic assumes ("highway speed" in the voice), labelled "HIGHWAY SPEED" so it cannot be read as a gust.
- Source line: "Buffalo airport ASOS, IEM archive" (the quarter mile).

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed scene, driver's-eye view, channel ground on the root from frame 0. One-point perspective, vanishing point (960, 420). SCHEMATIC road (no distance scale drawn beyond the marker's meaning); the claim is the 15 s figure, carried by the stopwatch.

## 3. GEOMETRY (px)
- Road surface: polygon (420, 1080) - (960, 420) - (1500, 1080), fill `#15202b`. Edge lines 3 px `#93a3b2` at 0.6 along both sides. Centre dashes `#e8c56a` at 0.7 from (960, 1080) toward the VP, 6 dashes in perspective, scrolling toward the camera (continuous motion, ~1 dash period per 0.5 s, finite repeats).
- Right edge line passes x 1173 at y 680, so nothing of the road enters x >= 1600, y >= 680.
- Headlight cones: two trapezoids `rgba(245,217,139,.22)` (Amber time at low alpha), bottoms x 760 to 940 and x 980 to 1160 at y 1080, tops meeting the road near y 560 (x 900 to 1020); soft edges (blur 12 px).
- Whiteout haze: band `rgba(242,245,248, a)` over y 300 to 560 (full width), feathered top and bottom; `a` 0.25 at start, 0.75 by the end.
- Marker sign "1/4 MI" on the right shoulder: post 4 px `#93a3b2` from the road edge (1001, 470) up to the sign; sign box centred (1075, 430), 150 x 70 at scale 1, fill `#15202b`, 2 px `#f2f5f8` border, radius 6; text "1/4 MI" Arial Black `font-weight:900` 34 px `#f2f5f8`. The sign's group scales 0.85 -> 1.0 about its base over the window (slow approach) and its opacity follows the haze (0.9 -> 0.35): it dissolves but stays just legible.
- Snow particles: seeded, streaking outward from the VP toward the frame edges (snow hitting the windshield at speed), 1.5 to 3 px, `#f2f5f8` at 0.5 to 0.9. Excluded from: the HUD box (x <= 560, y <= 220), the chip box (x <= 520, y >= 820), and the corner x >= 1600, y >= 680.
- HUD top-left (fixed): eyebrow "HIGHWAY SPEED" Arial 700 22 px `#93a3b2` letter-spacing 6 at left 110, top 110; "60 MPH" Arial Black `font-weight:900` 52 px `#f2f5f8` at left 110, top 142.
- Stopwatch chip (glass card, tokens.md "Surfaces"): `left:110px; bottom:110px`, padding 22 px 34 px, hugs content; one baseline-aligned line: stopwatch icon 56 px (`#dfe7ee` ring 4 px, crown, one hand that sweeps with the count), 16 px gap, "15" Arial Black `font-weight:900` 84 px `#f2f5f8` (count-up leaf), 12 px gap, "SEC" Arial 700 30 px `#dfe7ee`. About x 110 to 470, y 842 to 970.
- Source pill (glass, radius 14, padding 5 px 12 px) `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Type tiers 84/52 big, 30/34 mid, 19 to 22 small.

## 4. MUST BE TRUE IN THE PICTURE
1. The counter ends on exactly 15 and holds; the stopwatch hand ends where 15 s sits on its dial (a quarter turn if the dial is 60 s: 90°).
2. "1/4 MI" sign is at the far edge of what is visible: inside the haze band, never in front of it, still readable at the end.
3. "HIGHWAY SPEED" is on screen whenever "60 MPH" is (never a bare 60 MPH after two gust scenes).
4. No text rides the camera: HUD and chip are fixed; only the road, sign, haze and particles move.
5. Corner x >= 1600, y >= 680 holds nothing but ground.

## 5. PANEL TEXT (exact) and CUES
Strings: `HIGHWAY SPEED` `60 MPH` · `1/4 MI` · `15` `SEC` · `Buffalo airport ASOS, IEM archive`
Times: segment seconds (`audio/a2-s4.words.json`) and comp-local seconds (comp starts at segment 9.20).
| seg t | local t | spoken word | action |
|---|---|---|---|
| 9.20 | 0.00 | frame 0 | ground, road, edge lines, dashes, headlights, haze at 0.25, particles moving; sign, HUD, chip hidden |
| 9.60 | 0.40 | "quarter" @9.60 | sign `fromTo(autoAlpha 0 -> 0.9, scale 0.8 -> 0.85, 0.4, power3.out)`; source pill in |
| 10.26 | 1.06 | "highway" @10.26 | HUD eyebrow then "60 MPH" `fromTo(autoAlpha 0, x:-24 -> 0, 0.4, power3.out)`, stagger 0.1 |
| 10.90 | 1.70 | "gives" @10.90 | chip `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)` with "0"; count 0 -> 15 on the leaf, 1.06 s, power2.out (lands at "seconds" 11.96); hand sweeps with it |
| 11.96 | 2.76 | "seconds" @11.96 | numeral pulse `scale 1 -> 1.08 -> 1, 0.4` |
| 12.58 | 3.38 | "see" @12.58 | haze thickens to 0.75 by 4.30 local; sign opacity to 0.35 |
| 9.20 to 13.6 | 0 to 4.4 | whole window | dashes scroll, particles stream, sign approaches (scale 0.85 -> 1.0, ease none) |
| 13.56 to 14.16 | 4.36 to 4.96 | after "ahead." @12.92 | exit: fade-through to white-grey wash then ground: everything `to(autoAlpha 0, 0.6, power2.in)` |
Comp duration 4.96 s (host data-start = A2-S4 start + 9.20).

## 6. CONTRACT
One file `compositions/g-a2-6-quarter-mile.html`, root `<div id="g-a2-6-quarter-mile-root" data-composition-id="g-a2-6-quarter-mile" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-6-quarter-mile"]`. Ids/classes `qm-`. Particles seeded and timeline-driven (canvas painted from `tl.eventCallback('onUpdate', ...)` if canvas). Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-6-quarter-mile`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-6-quarter-mile`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: state the 1,320 / 88 = 15.0 arithmetic in the receipt.

## 8. RECEIPT
As the template.
