# g-a4-3-day-chip · A4-S3 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-intro-2-toll-chips.html` (copy one chip, the source pill and the float exactly). This chip is the family base for `g-a4-11-door-quote`'s grey chip.

## 0. What this graphic claims
The photo is Monday 26 December 2022, the fourth day of the storm (23, 24, 25, 26 Dec): Guard engineers digging out an ambulance so it could move.

## 1. SOURCE
- DVIDS 7572837, 827th Engineer Co clearing snow to recover an AMR ambulance, Buffalo, taken 26 Dec 2022, Eric Durr (caption also says courtesy photo), public domain: `research/response.md` section 2 and section 7 row 1, https://www.dvidshub.net/image/7572837/new-york-national-guard-responds-christmas-snow-storm (PRIMARY).
- "DAY 4": storm began Fri 23 Dec; 26 Dec = day 4, computed: `factcheck/a4-r1.md` row 10 (CONFIRMED).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on footage. Lower-third anchor `left:110px; bottom:110px`. Presenter circle may be on: nothing in x >= 1600, y >= 680. No scale.

## 3. GEOMETRY (px)
- Chip: glass surface as g-intro-2 (`rgba(10,16,24,.55)`, blur 18 px saturate 1.15, 1 px `rgba(255,255,255,.14)` border, radius 28), `left:110px; bottom:110px`, padding 22 px 34 px, hugs its text. One baseline: "DEC 26" Arial Black `font-weight:900` 52 px `#f2f5f8`, then " · " 38 px `#93a3b2`, then "DAY 4" Arial Black 900 38 px `#e8c56a`. About x 110 to 610, y 860 to 970.
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`. About x 110 to 420.
- Type tiers: 52 (big), 38 (mid), 19 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The chip reads exactly "DEC 26 · DAY 4"; no year, no weekday.
2. The chip never covers the ambulance (the push in the index holds close on it; the orchestrator checks a settled frame at 3.0 s; if the ambulance sits lower-left, the chip moves to `left:auto; right:400px`, still clear of the corner).
3. Chip and pill land by "Guard" @0.44 and are gone before the S4 cut.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S3 start, `audio/a4-s3.words.json`)
Strings: chip `DEC 26 · DAY 4` · source `New York National Guard, DVIDS`

| t (s) | spoken word | action |
|---|---|---|
| 0.05 | "National Guard" @0.00 / 0.44 | chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; pill in `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power2.out)` |
| 2.42 | "ambulance" @2.42 | "DAY 4" `fromTo(scale 1.25 -> 1, 0.35, power4.out)` (the day lands as the ambulance is named) |
| whole window | | chip and pill float `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats |
| 6.80 to 7.40 | after "anyone." @7.02 | chip out `to(x:-80, autoAlpha 0, 0.6, power3.in)`; pill stays |
| 11.66 to 12.26 | after "in." @11.92 (host end - 0.6) | pill out `to(autoAlpha 0, y:10, 0.6, power3.in)` |

Comp duration 12.26 s (wav length). The chip leaves at 7.4 so "the calls kept coming in" plays over the clean photo.

## 6. CONTRACT
One file `compositions/g-a4-3-day-chip.html`, root `<div id="g-a4-3-day-chip-root" data-composition-id="g-a4-3-day-chip" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-3-day-chip"]`. Ids prefixed `dc-`; classes `dc-chip`, `dc-src` (never `.lt`, `.glasscard`, `.srclab`). Root transparent. Start-hidden in CSS too. The photo, its push and its `data-callback="A4 names what I1 only showed"` belong to the index mount, not this comp.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-3-day-chip`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-3-day-chip`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame at 3.0 s composited over DVIDS 7572837 at its pushed framing.

## 8. RECEIPT
As the template.
