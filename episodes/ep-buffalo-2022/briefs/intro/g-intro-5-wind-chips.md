# g-intro-5-wind-chips · I1-S2 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from the built `compositions/g-intro-2-toll-chips.html` (same chip, same anchor, same tiers); copy, rename ids/classes, retune text and cues.

## 0. What this graphic claims
Three facts, one per sentence: the airport logged gusts of 69 mph; the governor's office said hundreds of drivers were stranded; the state counted 37 straight hours of blizzard-like conditions in Erie County.

## 1. SOURCE
- 69 MPH: ASOS BUF peak gust in the hourly/special feed, 60 kt = about 69 mph at 12:54 PM EST Fri 23 Dec 2022 (`research/nws.md` 3.1, PRIMARY derived; IEM ASOS URL in its fetch notes). Never "peak gust" on screen: "GUSTS 69 MPH" only (`edit_script.md` I1-S2 rows: "logged" kept, never "peak").
- HUNDREDS STRANDED: governor.ny.gov, 26 Dec 2022, headline "... Leaving Hundreds of Motorists Stranded" (`research/response.md` section 1 row "Ban reaches hundreds of motorists stranded", PRIMARY): https://www.governor.ny.gov/news/governor-hochul-submits-request-federal-emergency-declaration-historic-winter-storm-continues
- 37 STRAIGHT HOURS: NYS DHSES release, 4 Aug 2023, "37 straight hours of blizzard-like conditions in Erie County" (`research/response.md` section 5, PRIMARY): dhses.ny.gov/node/16646
- Fact check: `factcheck/intro-r3.md` row 22 (chips and both dated source lines CONFIRMED; the photo is 26 Dec, illustration only), row 21 (37 kept as the conservative sourced figure).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on footage. Lower-third anchor `left:110px; bottom:110px`. Presenter circle may be on: nothing in x >= 1600, y >= 680. No scale.

## 3. GEOMETRY (px; identical to g-intro-2)
- Three chips, each its own glass card (tokens.md "Surfaces"), `position:absolute; inset:auto; left:110px; bottom:110px;` padding 22 px 34 px, hugging the text; height about 128 (y about 842 to 970). One visible at a time.
- Each chip one baseline-aligned line; the big span is Arial Black `font-weight:900` 84 px `#f2f5f8`, the label spans Arial 700 30 px `#dfe7ee` letter-spacing 1, 16 px gaps:
  - C1: "GUSTS" (30) + "69" (84) + "MPH" (30). About x 110 to 520.
  - C2: "HUNDREDS" (84) + "STRANDED" (30). About x 110 to 860.
  - C3: "37" (84) + "STRAIGHT HOURS" (30). About x 110 to 560.
- Source pill (glass, radius 14, padding 5 px 12 px), `left:110px; bottom:54px;` Arial 400 19 px `#c8d3e0`; one string at a time, swapped with its chip.
- Type tiers: 84, 30, 19. Nothing right of x = 1000.

## 4. MUST BE TRUE IN THE PICTURE
1. One chip at a time, in the voice's order: 69 MPH, HUNDREDS STRANDED, 37 STRAIGHT HOURS.
2. Each chip's source line is on screen with it, and only with it (the gust is never credited to the governor, the hours never to ASOS).
3. Strings exactly as section 5; no "peak", no "record", no "1.5 days" text (the voice carries "a day and a half").
4. Each figure is readable at its spoken word (landed within 0.45 s).
5. Over the DVIDS photo the chip never covers the ambulance or the soldiers' faces in the settled frame (orchestrator read); if it does, the stack moves right of centre, still clear of x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from I1-S2 start, `audio/i1-s2.words.json`)
Strings: `GUSTS` `69` `MPH` · `HUNDREDS` `STRANDED` · `37` `STRAIGHT HOURS` · sources `Buffalo airport ASOS, IEM archive` · `Office of the Governor, 26 Dec 2022` · `NYS DHSES, 4 Aug 2023`
| t (s) | spoken word | action |
|---|---|---|
| 1.28 | "gusts" @1.28 | C1 card in with "GUSTS" visible, numeral hidden: `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; ASOS source in |
| 1.94 | "69" @1.94 | "69" and "MPH" in: numeral counts up on a leaf span 40 -> 69, 0.8 s, power4.out |
| 4.58 | "blowing" @4.58 | C1 gets a sideways shove `fromTo(x:0 -> 10 -> 0, 0.5, power2.out)` (the wind word; no new text) |
| 1.9 to 7.8 | hold | float `y: 0 -> -4`, `sine.inOut`, finite yoyo |
| 7.85 to 8.20 | before "hundreds" | C1 + its source out: `to(x:-80, autoAlpha 0, 0.35, power3.in)` |
| 8.22 | "hundreds" @8.22 | C2 in; "HUNDREDS" `fromTo(scale 1.25 -> 1, 0.45, power4.out)`; governor source in |
| 9.20 | "stranded," @9.20 | "STRANDED" `fromTo(autoAlpha 0, x:-12 -> 0, 0.3)` |
| 10.55 to 10.90 | "and the state" @10.12 to 10.36 | C2 + source out |
| 10.94 | "37" @10.94 | C3 in; numeral counts up 1 -> 37, 1.0 s, power4.out; DHSES source in |
| 11.32 | "straight" @11.32 | "STRAIGHT HOURS" `fromTo(autoAlpha 0, x:-12 -> 0, 0.3)` |
| 14.60 | "which is a day and a half" @14.60 | numeral "37" pulse `scale 1 -> 1.08 -> 1, 0.5` (no text) |
| host end - 0.6 to host end (15.6 to 16.2 at the default) | after "half." @15.32 | C3 + source out: `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
Comp duration 16.2 s. Spoken time in a comment at each tween.

## 6. CONTRACT
One file `compositions/g-intro-5-wind-chips.html`, root `<div id="g-intro-5-wind-chips-root" data-composition-id="g-intro-5-wind-chips" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-intro-5-wind-chips"]`. Ids prefixed `wc-`, classes `wc-*` (not g-intro-2's `tc-`). Root transparent. Count-ups write a leaf span only. Everything else: `references/mg-quickref.md`.
Footage under it (mounted by the orchestrator for the whole host window): DVIDS 7572837, 827th Engineer Co clearing snow to recover an AMR ambulance, Buffalo, 26 Dec 2022, Eric Durr, https://www.dvidshub.net/image/7572837/new-york-national-guard-responds-christmas-snow-storm (`research/response.md` section 2 and section 7 row 1). File not yet in `media/`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-5-wind-chips`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-5-wind-chips`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame per chip over the DVIDS still once mounted.

## 8. RECEIPT
As the template.
