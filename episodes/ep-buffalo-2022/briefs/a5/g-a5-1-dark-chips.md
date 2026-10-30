# g-a5-1-dark-chips · A5-S1 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-intro-2-toll-chips.html` (copy one chip, the source pill and the float exactly) and the in-place number swap of the built `compositions/g-a4-9-guard-tally.html`.

## 0. What this graphic claims
At the storm's peak more than 80,000 households had lost power; by the last reported count 12 of the people who lost their lives were listed without power or heat, and 4 more lost their lives shoveling or clearing snow. Three facts, one at a time, never two on screen together.

## 1. SOURCE
- 80,000+: "More than 80,000 households lost power at the storm's peak", NYS DHSES release, 4 Aug 2023, https://www.dhses.ny.gov/node/16646: `research/response.md` section 5 and section 6 row "Peak" (PRIMARY, FETCHED); `factcheck/a5-r1.md` row 4.
- 12 and 4: WIVB final-count page, Poloncarz: "12 died from no power or heat"; "4 died in snow-blowing or shoveling incidents": `research/deaths.md` section 1 row "final" (SECONDARY); `factcheck/a5-r1.md` rows 3 and 6. No place is given for the 12: never "at home".

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on footage (no ground of its own; root transparent). Lower-third anchor `left:110px; bottom:110px`. Presenter circle may be on: nothing in x >= 1600, y >= 680. Top-right corner (right 96, top 54) stays free for a footage credit the index may add (`_list.md` open item 2). No scale.

## 3. GEOMETRY (px)
- Chip (glass as g-intro-2: `rgba(10,16,24,.55)`, `backdrop-filter: blur(18px) saturate(1.15)`, 1 px `rgba(255,255,255,.14)` border, radius 28, padding 22 px 34 px), `left:110px; bottom:110px`, hugs its text, one baseline per state:
  - State A: "80,000+" Arial Black `font-weight:900` 52 px `#f2f5f8`, 16 px gap, "HOUSEHOLDS WITHOUT POWER" Arial Black 900 30 px `#dfe7ee`. About x 110 to 900, y 860 to 970.
  - State B: "12" (52 px, as above) + "WITHOUT POWER OR HEAT" (30 px). About x 110 to 720.
  - State C: "4" (52 px) + "SHOVELING" (30 px). About x 110 to 430.
  Each state is its own pre-authored leaf pair inside its own chip element (three chips stacked at the same anchor, only one visible at a time; no text written at runtime). The chip box resizes by swapping chips, never by tweening `width`.
- Source pill (glass, radius 14, padding 5 px 12 px), `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`. Two pre-authored pills at the same anchor: P1 "NYS DHSES, 4 Aug 2023"; P2 "Poloncarz via WIVB, last reported count".
- Type tiers: 52 (big), 30 (mid), 19 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. Only one chip and one pill are visible in any frame (cross-swap: the old one is at autoAlpha 0 before the new one passes 0.5).
2. P1 is shown only with chip A; P2 only with chips B and C.
3. Chip strings exactly as §5; "80,000+" keeps the comma and the plus; no "AT HOME", no year, no place name (the footage is stock, not Buffalo: no label may name a place).
4. Nothing in x >= 1600, y >= 680; nothing in the top-right credit slot.
5. Chip A lands on "80,000" @9.26, chip B on "12" @11.88, chip C on "Four" @16.08: numerals on screen, words in the voice.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S1 start, `audio/a5-s1.words.json`)
Strings: `80,000+` · `HOUSEHOLDS WITHOUT POWER` · `12` · `WITHOUT POWER OR HEAT` · `4` · `SHOVELING` · `NYS DHSES, 4 Aug 2023` · `Poloncarz via WIVB, last reported count`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 to 9.20 | "For the people who stayed home ... At the storm's peak," | nothing of this comp is visible; the footage plays clean. The timeline still carries an invisible keep-alive only if a gate demands it; the index's slow move on the footage carries the motion |
| 9.26 | "more than 80" @9.02 / 9.26 | chip A in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; "80,000+" `fromTo(scale 1.25 -> 1, 0.35, power4.out)`; P1 in `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power2.out)` at 9.40 |
| 11.88 | "12" @11.88 | chip A out `to(y:-20, autoAlpha 0, 0.25, power2.in)` at 11.70; chip B in `fromTo(y:20 -> 0, autoAlpha 0 -> 1, 0.35, power3.out)` at 11.88; P1 out / P2 in, same moves, at 11.88 |
| 14.54 | "power or heat" @14.54-15.56 | "WITHOUT POWER OR HEAT" leaf brightens `#dfe7ee -> #f2f5f8` (0.3 s) |
| 16.08 | "Four" @16.08 | chip B out at 15.90 (as chip A); chip C in at 16.08 (as chip B); P2 stays |
| 9.26 to end | | the visible chip and pill float `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats (no 4 s gap with nothing moving while they are up) |
| 18.15 to 18.75 | after "snow." @18.22-18.58 (host end - 0.6) | chip C out `to(x:-80, autoAlpha 0, 0.6, power3.in)`; P2 out `to(autoAlpha 0, y:10, 0.6, power3.in)` |

Comp duration 18.75 s (wav length). The host starts at S1 +9.10 if the gates object to a 9 s empty span (then shift every cue by -9.10 and say so in the receipt); the first 9 s are footage only on purpose.

## 6. CONTRACT
One file `compositions/g-a5-1-dark-chips.html`, root `<div id="g-a5-1-dark-chips-root" data-composition-id="g-a5-1-dark-chips" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a5-1-dark-chips"]`. Ids prefixed `dk-`; classes `dk-chip`, `dk-src` (never `.lt`, `.glasscard`, `.srclab`, never `#root`). Root transparent. Start-hidden in CSS too. Repeat note: "12" and "WITHOUT POWER OR HEAT" also appear in the intro chips (another comp, minutes earlier): a callback, not a per-frame repeat.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-1-dark-chips`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-1-dark-chips`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame at 10.5 s and one at 17.0 s composited over `media/a5/A5-S1_c1_snowy-suburban-street-night.mp4` (Pexels stock; `media/candidates/a5/provenance.csv`); the chip must not sit on the clip's street lamp.

## 8. RECEIPT
As the template.
