# g-a5-9-ban-card · A5-S8 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-a5-4-tally-final.html` (mini tally: same colours and block style, smaller pitch; build g-a5-4 first), `library/inhouse/quote-card.html` (card panel and line build) and the chip of the built `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
Three beats, one at a time: (1) the 22 of 46 found outside or in cars returns as the episode's answer; (2) the next winter, on 13 Jan 2024, the full travel ban for all of Erie County started at 9 p.m. Saturday, before the worst of the snow; (3) this winter, November to March, Buffalo is inside its lake snow season again.

## 1. SOURCE
- 22 of 46: as `g-a5-4-tally-final` §1 (`research/deaths.md` sections 1 and 3; WIVB, SECONDARY). No new fact (`edit_script.md` A5-S8 rows).
- Ban: governor.ny.gov, 13 Jan 2024, "a full travel ban for passenger vehicles will be in effect for all of Erie County beginning at 9 p.m. Saturday", https://www.governor.ny.gov/news/governor-hochul-and-local-authorities-announce-full-travel-ban-erie-county-beginning-9-pm (PRIMARY): `factcheck/a5-r1.md` rows 22 to 25 ("before the worst of the snow": row 24).
- Window: NWS Buffalo defines winter November through March; lake snow "can start as early as mid November, peaks in December", https://www.weather.gov/buf/BUFclifo: `factcheck/a5-r1.md` row 30. "THIS WINTER" assumes the Dec 2026 upload (`edit_script.md` publish target).

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `bn-ground`, frame 0). Three scenes, one reading target each. Mini tally scale: 1 block = 1 person, 46 blocks, pitch 24 px, width 18, x 411-1509, y 520-600; halfway datum x 960 (between block 22 and 23). Corner x >= 1600, y >= 680 empty in every scene.

## 3. GEOMETRY (px) — compute block x from the formula with a script and print it in the receipt
Scene 1 (mini tally):
- Block i (0..45): x = 411 + 24 i, width 18, y 520, height 80, radius 4. Colours as g-a5-4: i 0-17 `#f2f5f8`, i 18-21 `#d8a13a`, i 22-45 `#2a3644` (no blue run here: one claim per frame). Lit run ends x 933.
- Halfway line: dashed 2 px `#e74c3c` at 60 %, dash 8 6, x 960, y 500-620; no tag.
- Chip "22 OF 46" (dark panel `#15202b` at 92 %, 1 px `rgba(255,255,255,.14)`, radius 20, padding 14 px 28 px), centred x 960, top 390 (about y 390-470): "22" Arial Black 900 52 px `#f2f5f8` + " OF 46" Arial Black 900 52 px `#93a3b2`.
- Sub-label under the bar, Arial 700 22 px `#93a3b2` tracking 6, centred x 960, top 630: "FOUND OUTSIDE OR IN THEIR CARS".
Scene 2 (release card):
- Card (`#15202b` at 94 %, border as above, radius 24, padding 48 px 64 px), centred x 960, x 420-1500, y 250-760 (right edge 1500 < 1600).
- Eyebrow "THE NEXT WINTER" Arial 700 22 px `#93a3b2` tracking 6, top 300, centred.
- "JAN 13, 2024" Arial Black 900 38 px `#d8a13a`, top 340, centred.
- Rule 2 px `rgba(255,255,255,.14)`, x 560-1360, y 410.
- "FULL TRAVEL BAN" Arial Black 900 84 px `#f2f5f8`, top 440, centred (about x 560-1360).
- "ALL OF ERIE COUNTY" Arial 700 38 px `#dfe7ee` tracking 4, top 550, centred.
- "9 PM SAT" Arial Black 900 58 px `#e8c56a`, top 620, centred.
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Office of the Governor, 13 Jan 2024".
Scene 3 (calendar chip):
- Chip (same panel, radius 20, padding 20 px 32 px), centred x 960, top 470 (about y 470-560): "THIS WINTER" Arial 700 30 px `#93a3b2` tracking 6 + " · " + "NOV TO MAR" Arial Black 900 52 px `#f2f5f8`.
- Season strip under it: track x 660-1260, y 600, height 8, radius 4, `rgba(255,255,255,.14)`; fill `#7fb2e5` `scaleX 0 -> 1` from left (no month labels: the chip carries them).
- Source (same zone as scene 2's, swapped): "NWS Buffalo climate pages".
- Type tiers: 84/58/52 big, 38/30 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Mini tally: exactly 46 blocks; 22 lit (18 white + 4 amber); the lit run ends at x 933, left of the halfway line x 960 (22 < 23: close to half, never half).
2. Card strings exactly as §5; the ban time is "9 PM SAT" and the date "JAN 13, 2024" (the same day, a Saturday). No snowfall totals, no "BEFORE THE SNOW" text (spoken only).
3. One scene visible at a time: scene 1 fully out before the card enters; card fully out before the calendar chip enters.
4. Only "NOV TO MAR" names the window; no year on the calendar chip.
5. The comp ends on the bare ground (no text), so the close card (`g-a5-10-close`) can cut in clean.
6. Nothing in x >= 1600, y >= 680; text 96 px from the edges.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S8 start, `audio/a5-s8.words.json`)
Strings: `22` · ` OF 46` · `FOUND OUTSIDE OR IN THEIR CARS` · `THE NEXT WINTER` · `JAN 13, 2024` · `FULL TRAVEL BAN` · `ALL OF ERIE COUNTY` · `9 PM SAT` · `Office of the Governor, 13 Jan 2024` · `THIS WINTER` · ` · ` · `NOV TO MAR` · `NWS Buffalo climate pages`
Note: Whisper heard "band" @2.88 for the spoken "ban" and "helped struggle" for "help struggled"; times are right, words are the script's.

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Many were out there" @0.00-0.82 | ground on frame 0; 46 blocks fill in place `scaleY 0 -> 1`, stagger 0.015, 0.0-0.8 (already coloured: a callback, not a rebuild) |
| 0.38 | "out there" @0.38-0.82 | chip "22 OF 46" `fromTo(scale 1.15 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)`; sub-label in at 0.80 |
| 1.28 | "morning commute had started before the ban did," @1.28-3.40 | halfway line draws `scaleY 0 -> 1`, 0.4 s, at 2.38 ("before") |
| 5.82 | "rescue trucks were stuck in the same snow." @5.82-7.74 | lit run sheen x 411 -> 933 (0.6 s) at 6.60 ("stuck") |
| 0.8 to 7.74 | | blocks 0-21 and the chip float y 0 -> -3 (sine, yoyo, finite) |
| 7.80 to 8.30 | after "snow." @7.74 | scene 1 out `to(autoAlpha 0, y:-14, 0.5, power2.in)` |
| 8.36 | "The next winter," @8.24-8.92 | card in `fromTo(y:30 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`, empty; eyebrow at 8.54 |
| 9.30 | "January 2024," @9.30-10.54 | "JAN 13, 2024" `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)`; rule draws at 9.70; source in at 9.70 |
| 11.34 | "a big lake storm came back." @11.20-12.74 | card floats; a soft snow drift layer (40 small `#dfe7ee` dots at 30 %, drifting down 30 px/s) fades in behind the card, finite |
| 13.82 | "full travel ban" @13.82-14.70 | "FULL TRAVEL BAN" `fromTo(scale 1.15 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 14.96 | "all of Erie County" @14.96-15.82 | "ALL OF ERIE COUNTY" `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)` |
| 16.42 | "9 on a Saturday night." @16.42-17.84 | "9 PM SAT" `fromTo(scale 1.25 -> 1, autoAlpha 0 -> 1, 0.4, power4.out)` |
| 18.68 | "before the worst of the snow." @18.68-20.12 | snow drift layer thickens (dot opacity 30 % -> 60 %, speed 30 -> 60 px/s) behind the card after the ban line has landed: the snow comes after the ban |
| 20.12 to 20.62 | "Between now" @20.12 | card and drift out `to(autoAlpha 0, y:-16, 0.5, power2.in)`; source swaps to "NWS Buffalo climate pages" at 20.62 |
| 20.82 | "now and the end of March," @20.82-22.04 | calendar chip in `fromTo(y:20 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; strip fills `scaleX 0 -> 1`, 1.2 s, at 21.36 ("end of March" lands as it completes at 22.56) |
| 22.64 | "Buffalo is inside its lake snow season again." @22.64-24.98 | chip floats; strip glow pulses once at 23.94 ("snow season") |
| 25.10 to 25.90 | after "again." @24.98 | everything fades out `to(autoAlpha 0, 0.8, power1.in)` toward the bare ground ("fade toward the title card") |

Comp duration 25.90 s (0.71 s past the wav end; the close card follows on the ground; trim to the real gap).

## 6. CONTRACT
One file `compositions/g-a5-9-ban-card.html`, root `id="g-a5-9-ban-card-root"`, `data-composition-id="g-a5-9-ban-card"`, PAUSED timeline `window.__timelines["g-a5-9-ban-card"]`. Prefix `bn-` (never `tf-` or `ty-`). Blocks by `tl.set` from the formula. Snow dots: positions seeded and fixed in the file (no `Math.random` at runtime), moved by finite tweens. Repeat notes: "22 OF 46" also appears in `g-a5-4-tally-final` (another comp, about 90 s earlier) and the index mount carries `data-callback="the episode answer returns at the close"`. Rest: `references/mg-quickref.md`. Footage: none. Wind bed down to a whisper is the orchestrator's audio work.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-9-ban-card`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-9-ban-card`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print every mini block's x and the lit run end from the page. Read settled frames at 5.0 s, 18.0 s and 23.5 s.

## 8. RECEIPT
As the template.
