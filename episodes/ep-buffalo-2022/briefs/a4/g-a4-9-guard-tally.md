# g-a4-9-guard-tally · A4-S8 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the Courier counter of `library/inhouse/numbers-rollup.html` inside the chip surface of the built `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
The Guard's own tally, released 3 Jan 2023: 124 people rescued from stranded cars, 3,755 households checked, and 22 people who had lost their lives recovered by a 107th Attack Wing team.

## 1. SOURCE
- DVIDS news 436223, 3 Jan 2023 (PRIMARY): "124 people rescued from stranded cars"; "3,755 households visited during health and welfare checks"; a 107th Attack Wing Fatality Search and Recovery Team, "22 decedents". `research/response.md` section 4 final row; `factcheck/a4-r1.md` rows 29, 30, 31 (CONFIRMED).
- String change from the Picture line, for accuracy: the Picture's "CARS: 124" reads as 124 cars; the figure is 124 PEOPLE. Strings here: "124 RESCUED FROM CARS", "3,755 HOUSEHOLDS CHECKED", "22 RECOVERED". 22 is on screen only; A5 owns the only spoken twenty-two.
- Footage under it: DVIDS D5, 7576033, Guard soldiers and airmen doing welfare checks with Buffalo residents, 30 Dec 2022: `research/cc-clips-r2.md` row D5, https://www.dvidshub.net/image/7576033.

## 2. DATUM, SCALE, ORIENTATION
Overlay over the D5 still. Lower-third anchor `left:110px; bottom:110px`. No scale. Presenter circle may be on: nothing in x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- One counter card (glass as g-intro-2, padding 22 px 34 px, `left:110px; bottom:110px`), fixed width 700 px (x 110 to 810, so it does not jump between values), height about 132 (y 838 to 970). One baseline: value leaf, Courier New 700 84 px, then a 20 px gap, then the label leaf, Arial 700 30 px `#dfe7ee`, letter-spacing 1.
- Three pre-authored value/label pairs in the same spot, one visible at a time:
  - P1: "124" `#e8c56a` + "RESCUED FROM CARS".
  - P2: "3,755" `#e8c56a` + "HOUSEHOLDS CHECKED".
  - P3: "22" `#c8d3e0` (grey: a loss, not a win) + "RECOVERED".
- A 3 px `#e8c56a` progress tick under the value (width of the value glyphs) draws with each count-up; for P3 the tick is `#93a3b2` and does not draw (no flourish on the losses).
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Type tiers: 84 (big), 30 (mid), 19 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. Each value lands within 0.45 s of its spoken figure: 124 by 3.95, 3,755 by 7.85; "22" appears only on "recovered" @15.56, never before.
2. Exactly one pair visible at a time; values never count past their final figure; the comma in 3,755 is kept through the count.
3. P3 has no count-up, no pop and no colour flash.
4. The card does not cover the faces at the door in D5 (orchestrator checks a settled frame at 8.5 s; if it does, the card moves to `left:auto; right:400px`, still clear of the corner).

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S8 start, `audio/a4-s8.words.json`)
Strings: `124` `RESCUED FROM CARS` · `3,755` `HOUSEHOLDS CHECKED` · `22` `RECOVERED` · source `New York National Guard, DVIDS, 3 Jan 2023`

| t (s) | spoken word | action |
|---|---|---|
| 1.46 | "New Year's" @1.46 | source pill in `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power2.out)` |
| 3.14 | "rescued" @3.14 | card in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)` with P1; value counts on a leaf from 1 to 124, `power4.out`, lands 3.95 ("124" @3.52); tick draws `scaleX 0 -> 1, 0.5` |
| 6.60 | "checked" @6.60 | P1 out `to(autoAlpha 0, y:-12, 0.25)`; P2 in `fromTo(autoAlpha 0, y:12 -> 0, 0.25)`; value counts 1 -> 3,755, `power4.out`, lands 7.85 ("3,755" @7.10 to 7.40); tick redraws |
| 10.08 | "door" @10.08 | a soft knock pulse on the card: `scale 1 -> 1.02 -> 1`, 0.3 s, twice (10.08, 10.48) |
| 14.80 | after "job." @14.44 | P2 out `to(autoAlpha 0, 0.4, power2.in)` (card stays, empty value slot for 0.76 s) |
| 15.56 | "recovered" @15.56 | P3 in `fromTo(autoAlpha 0 -> 1, 0.6, power1.out)` |
| whole window | | card and pill float `y 0 -> -3`, sine, finite repeats |
| 17.60 to 18.20 | after "lives." @17.02 | card and pill out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |

Comp duration 18.20 s (wav 17.59 + land). The orchestrator leaves at least 0.6 s before S9 (a natural pause before "help came too late"); if not, the cut into the full-frame g-a4-10 carries the card off.

## 6. CONTRACT
One file `compositions/g-a4-9-guard-tally.html`, root `<div id="g-a4-9-guard-tally-root" data-composition-id="g-a4-9-guard-tally" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-9-guard-tally"]`. Ids prefixed `gt-`; classes prefixed `gt-`. Root transparent. Count-ups write only leaf spans (format with the comma in onUpdate). Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-9-guard-tally`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-9-guard-tally`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 4: seek check at 3.95, 7.85, 15.56. Item 7: one frame at 8.5 s composited over DVIDS 7576033.

## 8. RECEIPT
As the template.
