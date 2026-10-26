# g-intro-2-toll-chips · H1-S2 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
PROVISIONAL hook: if the owner picks another hook shape, this graphic is redone. This chip is the family base for `g-intro-5-wind-chips`: build it first.

## 0. What this graphic claims
At last count 46 people lost their lives in Erie County; 12 were without power or heat; the biggest group, 18 of the 46, were found outside; 4 more in their cars. The beat breaks the viewer's "stuck at home" belief: 18 beats 12.

## 1. SOURCE
- `research/deaths.md` section 1 row "final" and section 2: 46 Erie County; 18 outside, 12 no power or heat, 7 delayed EMS, 4 vehicles, 4 shoveling, 1 hotel pool; Poloncarz via WIVB, SECONDARY: https://www.wivb.com/weather-news/buffalo-blizzard-2022/erie-county-medical-examiner-confirms-three-more-blizzard-related-deaths-bringing-total-to-47/amp/
- `research/nws.md` row 7.1 and 7.2 (18 of 46 = 39 %, the largest group, NOT a majority).
- Fact check: `factcheck/intro-r3.md` row 8 (all four chips and the source line CONFIRMED), `factcheck/intro-r2.md` rows 2, 3, 6 ("at last count" hedge, three cases pending; never "at home", never "final").

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on footage. Lower-third anchor `left:110px; bottom:110px` (tokens.md "Canvas"). Presenter circle may be on: nothing in x >= 1600, y >= 680. No scale (no bars).

## 3. GEOMETRY (px)
- Four chips, each its OWN glass card (`rgba(10,16,24,.55)`, `backdrop-filter: blur(18px) saturate(1.15)`, 1 px `rgba(255,255,255,.14)` border, radius 28, tokens.md "Surfaces"). Only one chip visible at a time.
- Chip box: `position:absolute; inset:auto; left:110px; bottom:110px;` padding 22 px 34 px, hugs its text (`display:table` or inline-flex, never fixed width). Height about 128 (84 px numeral + padding): y about 842 to 970.
- Inside each chip, one line, baseline-aligned: numeral span (Arial Black `font-weight:900`, 84 px, line-height 1) then a 16 px gap, then the label span (Arial 700, 30 px, `#dfe7ee`, letter-spacing 1).
  - C1: "46" `#f2f5f8` + "IN ERIE COUNTY". Width about 112 + 16 + 300 + 68 = about 500, so x 110 to about 610.
  - C2: "12" `#f2f5f8` + "WITHOUT POWER OR HEAT". About x 110 to 720.
  - C3: "18" in `#e74c3c` (Danger red 2) + "OF 46 FOUND OUTSIDE". About x 110 to 690. A 4 px `#e74c3c` rule under the word "OUTSIDE" (drawn at its cue).
  - C4: "+4" `#f2f5f8` + "IN THEIR CARS". About x 110 to 560.
- Source pill: glass surface as above, radius 14, padding 5 px 12 px, `left:110px; bottom:54px;` Arial 400 19 px `#c8d3e0`, one line, about x 110 to 980, y about 996 to 1026. Text-safe bottom margin 54 respected.
- Type tiers: 84 (big), 30 (mid), 19 (small).
- Nothing right of x = 1100 in this comp.

## 4. MUST BE TRUE IN THE PICTURE
1. One chip on screen at a time; their order is 46, 12, 18, 4, matching the voice.
2. The strings read exactly as section 5 (numerals on screen, words in the voice). No "at home", no "final", no "most".
3. The 18 is the visual peak: the only red numeral, and its chip is never smaller than the 12 chip's numeral.
4. Each numeral is fully readable at its spoken word (landed within 0.45 s of the cue), and each chip is gone before the next numeral is spoken.
5. The source line is on screen from C1 to the exit and is never covered by a chip.
6. Over the DVIDS photo, every chip reads (glass card, white text); the orchestrator checks the soldier and door are not under the chip in the settled frame. If they are, the whole stack moves to the right of the frame centre, still clear of x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from H1-S2 start, `audio/h1-s2.words.json`)
Strings: `46` `IN ERIE COUNTY` · `12` `WITHOUT POWER OR HEAT` · `18` `OF 46 FOUND OUTSIDE` · `+4` `IN THEIR CARS` · source `Erie County Executive Mark Poloncarz, last reported count (3 cases pending), via WIVB`
| t (s) | spoken word | action |
|---|---|---|
| 1.32 | "46" @1.32 | C1 in: `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; numeral counts up on a leaf span 1 -> 46 in 0.9 s power4.out (fast, then slow into 46). Source pill in with it: `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power2.out)` |
| 3.18 | "Erie County." @3.18 | label "IN ERIE COUNTY" brightens to `#ffffff`, 0.25 s |
| 3.95 to 4.30 | gap before "12" | C1 out: `to(x:-80, autoAlpha 0, 0.35, power3.in)` |
| 4.36 | "12" @4.36 | C2 in (same tween as C1, no count-up; numeral `fromTo(scale 0.8 -> 1, 0.4, back.out(1.6))`) |
| 7.55 to 7.90 | "But the biggest group" @6.76 to 7.20 | C2 out (same exit) |
| 7.96 | "18," @7.96 | C3 in; numeral `fromTo(scale 1.3 -> 1, 0.45, power4.out)` |
| 9.18 | "outside" @9.18 | red rule under "OUTSIDE": `fromTo(scaleX 0 -> 1, 0.5, power2.out, transformOrigin left center)` |
| 11.05 to 11.40 | after "snow." @10.36 | C3 out |
| 11.44 | "Four" @11.44 | C4 in (as C2) |
| whole window | | the visible chip floats `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats (never `repeat:-1`) |
| host end - 0.6 to host end (12.9 to 13.5 at the default) | after "cars." @12.44 | C4 and source out: `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
Comp duration 13.5 s. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-intro-2-toll-chips.html`, root `<div id="g-intro-2-toll-chips-root" data-composition-id="g-intro-2-toll-chips" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-intro-2-toll-chips"]`. Ids prefixed `tc-`; classes `tc-chip`, `tc-num`, `tc-lab`, `tc-src` (never `.lt`, `.glasscard`, `.srclab`: index.html uses them). Root transparent. Start-hidden in CSS too. Count-up writes only a leaf span. Everything else: `references/mg-quickref.md`.
Footage under it (mounted by the orchestrator on a lower track for the whole host window): DVIDS 7576030, NY Guard soldier knocking at a door for welfare checks, Buffalo, 30 Dec 2022, courtesy photo, https://www.dvidshub.net/image/7576030/ny-national-guard-troops-respond-buffalo-blizzard (`research/response.md` section 7 row 3). File not yet in `media/`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-2-toll-chips`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-2-toll-chips`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame per chip composited over the DVIDS still once it is mounted.

## 8. RECEIPT
As the template.
