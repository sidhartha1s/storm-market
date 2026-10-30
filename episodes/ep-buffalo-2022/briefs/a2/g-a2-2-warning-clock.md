# g-a2-2-warning-clock · A2-S1 (19.40 to 22.84) · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the glass-chip type pairing of BUILT `compositions/g-intro-2-toll-chips.html` (84 px numeral + 30 px label) and the clock icon of BUILT `compositions/g-intro-4-morning-map.html` (ban chip clock: ring + two hands), scaled up here.

## 0. What this graphic claims
The Blizzard Warning took effect at 7:00 AM; the 7:24 reading came 24 minutes into it. The clock face shows the 24 minutes as a filled wedge.

## 1. SOURCE
- Warning in effect from 7 AM Fri 23 Dec: `research/nws.md` 1.2 ("BLIZZARD WARNING IN EFFECT FROM 7 AM FRIDAY TO 7 AM EST SUNDAY", WSW 220854, PRIMARY).
- 7:00 to 7:24 = 24 min: `factcheck/a2-r1.md` row 3 (CONFIRMED, "Chip matches").
- Source line: "NWS Buffalo Blizzard Warning, 22 Dec 2022" (issued 3:54 AM Thu 22 Dec, `research/nws.md` 1.2).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, full-frame designed graphic, channel ground on the root from frame 0 (a full-frame scene, not over the stock: "WARNING IN EFFECT" names an event, 7a item 7). Clock: 12 o'clock is up; a minute is 6° clockwise.

## 3. GEOMETRY (px)
- Clock face centre (960, 430), radius 200: ring 6 px `#dfe7ee`, face fill `#15202b`, 12 hour ticks (4 px x 22 px `#93a3b2`, inner end at r 170), no numerals on the face.
- Elapsed wedge: from 12 o'clock (0°) clockwise, fill `rgba(216,161,58,.45)` (Amber 1), radius 192, sweeps 0° to 144° (24 min x 6°). Draw it as an SVG path whose end angle is tweened through a proxy written in the timeline's onUpdate (seek-safe, `tl.eventCallback('onUpdate', ...)`), or as a conic mask; it must read correctly when seeked to any time.
- Minute hand: 8 px x 170 px `#f2f5f8`, pivot (960, 430), rotation 0° (7:00) to 144° (7:24). Hour hand: 12 px x 110 px `#f2f5f8`, rotation 210° (7:00) to 222° (7:24). Centre cap 14 px radius `#d8a13a`. Hands use `svgOrigin` / transformOrigin at the pivot.
- Start tag "7:00 AM": Courier New 700 30 px `#e8c56a`, centred x 960, glyph box y 186 to 216 (just above the ring top at y 230).
- Label line (one line, baseline-aligned, centred on x 960, glyph box about y 700 to 784): "WARNING IN EFFECT" Arial 700 30 px `#dfe7ee` letter-spacing 1, 18 px gap, "24" Arial Black `font-weight:900` 84 px `#f2f5f8` (count-up leaf), 12 px gap, "MIN" Arial 700 30 px `#dfe7ee`. About x 560 to 1360.
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers 84 / 30 / 19. Nothing in x >= 1600, y >= 680.

## 4. MUST BE TRUE IN THE PICTURE
1. At the end state the minute hand points at the 24-minute mark (144°, between the 4 and 5 hour ticks, closer to the 5), and the wedge ends exactly under it.
2. The hour hand sits just past 7 (222°), never on 8.
3. The numeral reads 24 when the hand reaches 144°; the count and the hand finish together.
4. "7:00 AM" sits at the top of the clock, where the wedge starts.
5. The word "BLIZZARD" is not on screen (the Picture string is "WARNING IN EFFECT"; the voice says "Blizzard Warning").

## 5. PANEL TEXT (exact) and CUES
Strings: `7:00 AM` · `WARNING IN EFFECT` · `24` · `MIN` · `NWS Buffalo Blizzard Warning, 22 Dec 2022`
Times: segment seconds (`audio/a2-s1.words.json`) and comp-local seconds (comp starts at segment 19.40).
| seg t | local t | spoken word | action |
|---|---|---|---|
| 19.40 | 0.00 | frame 0 | ground on; clock hidden in CSS |
| 19.50 | 0.10 | "The" @19.50 | clock face + ticks + hands at 7:00 `fromTo(autoAlpha 0, scale 0.9 -> 1, 0.45, power3.out)`; "7:00 AM" tag in |
| 19.90 | 0.50 | "warning" @19.90 | "WARNING IN EFFECT" `fromTo(autoAlpha 0, y:16 -> 0, 0.35, power3.out)`; source line in |
| 20.64 | 1.24 | "effect" @20.64 | hands start: minute 0 -> 144°, hour 210 -> 222°, wedge 0 -> 144°, 1.0 s, power2.inOut |
| 21.10 | 1.70 | "24" @21.10 | "24" and "MIN" in; numeral counts 0 -> 24 on its leaf, 0.55 s, power3.out (lands at 2.25 with the hand) |
| 21.62 | 2.22 | "minutes." @21.62 | wedge edge pulse: ring `scale 1 -> 1.03 -> 1, 0.4` |
| 0.5 to 2.84 local | | hold | label line float `y: 0 -> -3`, sine.inOut, finite yoyo |
| 22.24 to 22.84 | 2.84 to 3.44 | after "minutes." ends @21.94 | exit fade-through: clock, label, source `to(autoAlpha 0, y:-20, 0.6, power2.in)`; ground stays |
Comp duration 3.44 s (host data-start = A2-S1 start + 19.40).

## 6. CONTRACT
One file `compositions/g-a2-2-warning-clock.html`, root `<div id="g-a2-2-warning-clock-root" data-composition-id="g-a2-2-warning-clock" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-2-warning-clock"]`. Ids/classes `wk-`. Count-up writes a leaf span only. Everything else: `references/mg-quickref.md`.
Footage: none (the stock clip ends at 19.40 in the index).

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-2-warning-clock`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-2-warning-clock`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 4: capture 2.25 local twice (seek forward, then seek 0 and back); the hand, wedge and "24" must match.

## 8. RECEIPT
As the template.
