# g-a5-5-city-bars · A5-S4 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/split-shared-scale.html` (two quantities on one shared scale) and `library/inhouse/then-now-scale.html` (then vs now pairing); bar fill per `library/inhouse/ranked-bars.html`.

## 0. What this graphic claims
City of Buffalo only: the 1977 blizzard took 11 lives in the city; in 2022 the city alone lost 35. Same scale, so 2022's bar is a bit over three times 1977's. The wider 1977 tolls (29 by the NWS tally, 23 in western New York by the Army Corps count) sit on a chip, never on the bar scale, because they cover a wider area.

## 1. SOURCE
- 1977: "23 total storm-related deaths in western New York, with 11 in the City of Buffalo" (US Army Corps of Engineers report, via Wikipedia, https://en.wikipedia.org/wiki/1977_Blizzard); NWS lists 29: `research/deaths.md` section 6 (SECONDARY; USACE and NWS pages not read); `factcheck/a5-r1.md` rows 16 and 17; `factcheck/a5-r2.md` row 1 (29 has no clear regional scope: never label it "western NY").
- Poloncarz, 26 Dec 2022: 1977 "is blamed for 29 deaths", the toll could surpass it: `research/deaths.md` section 6 (AP via The Peninsula, SECONDARY); `factcheck/a5-r1.md` row 15.
- 2022: 35 in Buffalo, 11 in the suburbs, of 46: `research/response.md` section 5 "Where people were found" row "Buffalo vs suburbs" (WIVB, SECONDARY); `factcheck/a5-r1.md` row 18. 35 / 11 = 3.18.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `cb-ground`, frame 0). Horizontal bars, shared origin x 160. Scale 31.429 px per life (1100 px = 35). Bar 1977 = 11 x 31.429 = 345.7 px; bar 2022 = 1100.0 px. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Title zone: eyebrow "CITY OF BUFFALO ONLY" Arial 700 22 px `#93a3b2` tracking 6, `left:96px; top:96px`; headline "TWO BLIZZARDS, ONE CITY" Arial Black 900 52 px `#f2f5f8`, left 96, top 132 (about x 96-830, y 132-196).
- Bar rows (track = 1 px `rgba(255,255,255,.14)` outline, 1100 x 80, radius 6, visible from the start so the frame is never empty):
  - Row 1977: label "BUFFALO 1977" Arial 700 26 px `#93a3b2` tracking 4, left 160, top 340; track x 160-1260, y 380-460; bar fill `#5a768f`, x 160-505.7; value "11" Arial Black 900 84 px `#dfe7ee`, left edge x 530, vertically centred on the bar (box about y 370-470).
  - Row 2022: label "BUFFALO 2022" Arial 700 26 px `#f2f5f8` tracking 4, left 160, top 540; track x 160-1260, y 580-660; bar fill `#c0392b`, x 160-1260; value "35" Arial Black 900 84 px `#f2f5f8`, left edge x 1290 (box about x 1290-1400, y 570-670).
  - Bar text layout: label line and value combine as the Picture's "BUFFALO 1977 · 11" / "BUFFALO 2022 · 35": the label sits above the bar, the value at the bar's end.
- Chip (dark-panel card, not glass: no footage under it; `#15202b` at 92 %, 1 px `rgba(255,255,255,.14)` border, radius 20, padding 20 px 28 px), right edge x 1824, top 230 (about x 1240-1824, y 230-350, clear above row 1977's track, which starts at y 380); two lines, left-aligned:
  - Line 1: "1977 · 29 (NWS)" Arial Black 900 38 px `#dfe7ee`.
  - Line 2: "23 WESTERN NY (ARMY CORPS)" Arial 700 22 px `#93a3b2` tracking 3.
  State the measured chip box; it must stay above y 370 and right of the headline (x > 860).
- Source (one zone, two pre-authored lines, one visible at a time), Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: S-A "US Army Corps of Engineers report, via Wikipedia; NWS tally"; S-B "Poloncarz via WIVB".
- Type tiers: 84/52 big, 38/26 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Both bars start at x 160 and use one scale: 2022 bar / 1977 bar = 1100 / 345.7 = 3.18 (±1 %). Measure both on the settled frame.
2. 29 and 23 never get a bar or a position on the scale; they sit only on the chip.
3. "29" is never labelled western New York; the chip lines read exactly as §5.
4. No "3x", "MORE THAN THREE TIMES" or percentage on screen.
5. Value "11" lands with the 1977 bar (never spoken: on screen only, by design, `grades/a5-r1.md` fix 5); "35" lands on the spoken "35".
6. Nothing overlaps; nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S4 start, `audio/a5-s4.words.json`)
Strings: `CITY OF BUFFALO ONLY` · `TWO BLIZZARDS, ONE CITY` · `BUFFALO 1977` · `11` · `BUFFALO 2022` · `35` · `1977 · 29 (NWS)` · `23 WESTERN NY (ARMY CORPS)` · `US Army Corps of Engineers report, via Wikipedia; NWS tally` · `Poloncarz via WIVB`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "On the day after Christmas," | ground on frame 0; both empty tracks fade in 0.0-0.6 |
| 0.66 | "Christmas," @0.66 | eyebrow in `fromTo(autoAlpha 0, y:12 -> 0, 0.4)`; headline at 0.90 `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)` |
| 3.42 | "blizzard of 1977." @3.42-4.86 | label "BUFFALO 1977" in at 3.42; bar 1977 grows `scaleX 0 -> 1`, `transformOrigin:"left center"`, 0.6 s, power3.out at 3.88; "11" `fromTo(autoAlpha 0, x:-12 -> 0, 0.35)` at 4.40; S-A in at 4.40 |
| 6.90 | "29 lives." @6.90-7.82 | chip in `fromTo(x:60 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; line 2 in at 7.30 |
| 8.46 | "He turned out to be right." @8.46-9.42 | chip settles to 80 % opacity (0.5 s) |
| 10.04 | "2022," @10.04-10.68 | label "BUFFALO 2022" in `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)` |
| 11.38 | "the city of Buffalo alone" @11.38-12.56 | eyebrow "CITY OF BUFFALO ONLY" pulses `scale 1 -> 1.06 -> 1` (0.5 s) |
| 12.56 | "lost 35." @12.56-13.28 | bar 2022 grows `scaleX 0 -> 1`, 0.75 s, power3.out at 12.56; "35" counts up on a leaf span 0 -> 35 (onUpdate, power4.out, opening on 1), lands at 13.31; S-A out / S-B in at 12.56 |
| whole window | | every visible element floats y 0 -> -3 (sine, yoyo, finite), staggered; no 4 s gap without a tween |
| 14.30 to 14.90 | after "35." @13.28 | all text and bars out `to(autoAlpha 0, y:-10, 0.6, power3.in)`, stagger 0.03; ground stays |

Comp duration 14.90 s (1.27 s past the wav end, the land time after the last beat; trim to the real gap, keeping at least 0.8 s after 13.31).

## 6. CONTRACT
One file `compositions/g-a5-5-city-bars.html`, root `id="g-a5-5-city-bars-root"`, `data-composition-id="g-a5-5-city-bars"`, PAUSED timeline `window.__timelines["g-a5-5-city-bars"]`. Prefix `cb-`. Bars tween `scaleX`, never `width`. Repeat note: "1977" appears in the row label and the chip: label "BUFFALO 1977" and chip line "1977 · 29 (NWS)" are two different facts about one year; declare `data-repeat-ok="year label on two different counts"` on the chip's line-1 leaf only after a frame read. "35" also appears in A3 (another comp): a callback. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-5-city-bars`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-5-city-bars`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print both bar widths and the ratio from the page.

## 8. RECEIPT
As the template.
