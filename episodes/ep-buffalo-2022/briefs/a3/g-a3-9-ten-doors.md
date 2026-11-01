# g-a3-9-ten-doors · A3-S8 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: no close exemplar. Snow particles: `library/inhouse/moves/moves.js` and its demo (finite loops). Chip + source pill from `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
Jay Withey, stranded that Friday evening (23 Dec), knocked on the doors of 10 nearby homes just east of Buffalo and was turned away each time. Ten doors, in a blizzard, after dark. The houses are illustrations, not his street.

## 1. SOURCE
- `factcheck/a3-r1.md` row 46 and "New evidence": Global News citing NBC, https://globalnews.ca/news/9379230/buffalo-new-york-storm-heroes-jay-withey-craig-elston ("knocking on the doors of 10 nearby homes", offered $500 to sleep on a floor, "turned away each time", left about 6 p.m.; "just east of Buffalo"); CNN via WSB-TV also says 10 houses. SECONDARY, CONFIRMED. "that Friday evening": `factcheck/a3-r2.md` row 24.
- After dark: he set out about 6 p.m. 23 Dec; Buffalo sunset about 4:40 p.m. (`edit_script.md` A3-S8 row, NOAA solar calculator).
- The $500 is spoken but NOT shown (no chip requested; keep one fact per frame).

## 2. DATUM, SCALE, ORIENTATION
Full-frame night street (ground: channel radial gradient, layer `td-ground`, frame 0), snow falling across the whole frame. No scale; houses are schematic, all the same size. Corner x >= 1600, y >= 680 holds only ground and snow.

## 3. GEOMETRY (px)
- Snow bank / ground strip `td-snowline`: rect x 0-1920, y 660-1080, fill `linear-gradient(180deg, #2a3644, #0b1016)` at 60 % (a dark street under snow; no text on it except chip and source).
- 10 houses `td-h0`..`td-h9`, house i left x = 180 + 135 i (width 120, gap 15): row x 180-1515.
  - Body: rect y 500-660 (160 tall), fill `#15202b`, 1 px `rgba(255,255,255,.14)`.
  - Roof: triangle apex (x+60, 420), base (x-6, 500)-(x+126, 500), fill `#0b1016`; snow cap: a 10 px `#dfe7ee` stroke along both roof edges at 80 %.
  - Door `td-d<i>`: rect x+42 to x+78 (36 wide), y 590-660 (70 tall), fill `#2a3644`. Lit state: fill `#e8c56a` with a glow (`box-shadow`/SVG blur `#e8c56a` 40 %, radius 24). Dark state: back to `#2a3644`.
  - One window per house: 24 x 24 at (x+18, 530), fill `#04070a` (dark: nobody shown).
- Eyebrow name label, Arial 700 22 px `#93a3b2` tracking 6, `left:96px; top:96px`: "JAY WITHEY · FRIDAY EVENING". (Names the person spoken; not in the Picture line, kept to name him: drop on the orchestrator's call.)
- Chip "10 DOORS": glass, `left:110px; bottom:110px`, Arial Black 900 84 px `#f2f5f8` (x about 110-560, y about 842-970).
- Source pill `left:110px; bottom:54px`: "Jay Withey, to NBC, via Global News".
- Snow: about 120 flakes, 2-5 px `#dfe7ee` at 50-90 %, falling 120-220 px/s with x drift, finite repeats covering the host; from 18.52 ("blizzard") speed x1.6.
- Type tiers: 84 big, (houses carry no text), 22/19 small. Mid tier: the eyebrow is 22; add nothing. graphics_qc flat-type needs 4+ text nodes to fire; this comp has 3 text nodes (eyebrow, chip, source): state the count.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 10 houses and 10 doors, identical in size, evenly spaced.
2. Each door lights, holds, then goes dark: at most one door lit at any time, and never two in a row lit together.
3. All 10 doors are dark by the end of "each time" (15.88); none stays lit.
4. No people, no faces, no figure at a door, no street name, no house number.
5. "10 DOORS" appears only on "That's 10 front doors", after the knocking.
6. Night: no sun, no daylight sky; window rects stay dark.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S8 start, `audio/a3-s8.words.json`)
Strings: `JAY WITHEY · FRIDAY EVENING` · `10 DOORS` · `Jay Withey, to NBC, via Global News`
Door schedule: door i lights at T_i = 7.70 + 0.85 i (i = 0..9; T_9 = 15.35): `fill to lit 0.15 s`, hold 0.30 s, `fill to dark 0.25 s` (dark by T_i + 0.70; door 9 dark at 16.05, inside the pause between "time." @15.88 and "That's" @16.78).
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Walking had its own limit." | ground + snow from frame 0 |
| 0.94 | "limit." @0.94 | houses rise `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`, stagger 0.08 left to right (done by 2.16) |
| 3.52 | "Jay Withy" @3.52 | eyebrow in `fromTo(autoAlpha 0, x:-20 -> 0, 0.4)`; source pill in |
| 7.70 | "knocked" @7.70 | door 0 lights (schedule above) |
| 8.78 | "10 nearby homes" @8.78 | (door 1 lights at 8.55; schedule continues) |
| 15.08 | "turned away each time" @15.08-15.88 | last doors go dark per schedule |
| 16.98 | "That's 10 front doors" @16.98 | chip "10 DOORS" `fromTo(scale 1.2 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)`; all 10 door outlines flash `#e8c56a` stroke once together (stroke only, fills stay dark) 17.26-17.80 |
| 18.52 | "blizzard" @18.52 | snow speeds up x1.6 |
| 19.14-19.74 | after "dark." @19.42 | chip, eyebrow, pill out `to(autoAlpha 0, 0.6, power3.in)`; houses dim to 40 %; ground and snow stay |
Comp duration 19.74 s.

## 6. CONTRACT
One file `compositions/g-a3-9-ten-doors.html`, root `id="g-a3-9-ten-doors-root"`, `data-composition-id="g-a3-9-ten-doors"`, PAUSED timeline `window.__timelines["g-a3-9-ten-doors"]`. Prefix `td-`. Houses positioned by `tl.set` from the formula. Snow: finite repeats only. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-9-ten-doors`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-9-ten-doors`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print the 10 house x positions and the 10 door T_i from the page.

## 8. RECEIPT
As the template.
