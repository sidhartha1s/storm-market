# g-a2-11-both-lanes · A2-S10 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from the BUILT `compositions/g-a2-9-ban-bracket.html` (Opus): copy it, rename `bb-` to `bl-`, delete everything this brief does not list, retune cues. Lane px: `briefs/a2/g-a2-8-officials-clock.md` section 3; ban card, M3 and commute marker px: `briefs/a2/g-a2-9-ban-bracket.md` section 3. Change no px.

## 0. What this graphic claims
By the 9:30 ban, the morning commute (7:00 onward) was already behind most people: they had set out in rain at 38°F, and by 9:30 the pavement was ice under blowing snow with the wind still building.

## 1. SOURCE
- Most commuters out before 9:30: `factcheck/a2-r1.md` row 42 (ACS 2024 1-year, Erie County: 75.0 % leave before 9:00 a.m.; typical year, framing). No figure on screen.
- Rain at 38°F at 7:24 (and 37°F rain-snow at 6:58): row 43; M1 already shows "RAIN · 38°F".
- Ice, blowing snow, wind still building after 9:30: row 44 (NWS Winter Summary "flash freeze on area roads"; +SN BLSN from 8:39; sustained peak 39 kt at 9:54, PK WND 63 kt at 9:40, both after 9:30).
- Ban 9:30: `research/response.md` section 1 (WKBW); row 31.
- The Picture's 9:30 readout "1/4 MI · G58 KT · TEMP FALLING" is NOT used: there is no 9:30 observation in research, and visibility was already 1/8 mi by 8:47 (row 14), so "1/4 MI at 9:30" would be wrong. The readout uses the voice's own words, with no numbers.
- Source lines: "Erie County driving ban, WKBW" then "Buffalo airport ASOS, IEM archive".

## 2. DATUM, SCALE, ORIENTATION
As g-a2-8: x(t) = 200 + 5 px per minute after 5:30 AM (7:00 = 650, 9:30 = 1400). Full-frame designed, ground on the root from frame 0.

## 3. GEOMETRY (px)
- Frame 0 (opening state, all visible, a cut from g-a2-10): both lanes with labels, axes, hour labels; M1, M2, M4 (above the weather axis); M3 "8:15 AM / BELOW 32°F" (below it); SoE card; ban card (x 960 to 1400) with connector; commute marker "LEFT AT 7:00". Not present: dashed slot, 84 MIN bracket, 8:50 chip, 40 MIN, 10 AM marker, travel bar, lower third.
- Sweep: rectangle x 650 to 1400, y 200 to 700, fill `rgba(242,245,248,.10)` with a 40 px soft left edge (gradient), revealed right to left (`scaleX 0 -> 1`, transformOrigin right center). No hard leading-edge line (it would pass through labels).
- 9:30 readout (weather lane): tick 2 px `#f2f5f8` x 1400 from y 300 to 470; label block left 1412, top 300: "9:30 AM" Courier New 700 26 px `#e8c56a` (y 300 to 330), "ICE · BLOWING SNOW" Arial 700 24 px `#dfe7ee` (y 336 to 364), "WIND STILL BUILDING" Arial 700 24 px `#dfe7ee` (y 370 to 398). About x 1412 to 1700, all y < 680.
- Chip "ALREADY ON THE ROAD": Arial Black `font-weight:900` 52 px `#f2f5f8`, centred x 1025, glyph box y 790 to 850 (about x 690 to 1360), on the ground (no card), a 2 px `rgba(242,245,248,.35)` bracket above it from x 650 to 1400 at y 776 (ends ticked 8 px up) tying it to the swept span.
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`.
- Type tiers 52 / 24 to 26 / 19 to 22. Corner x >= 1600, y >= 680 empty.

## 4. MUST BE TRUE IN THE PICTURE
1. The sweep spans exactly 7:00 to 9:30 (x 650 to 1400 ±3), the commute marker at its left end and the ban card's right edge at its right end.
2. The 9:30 readout carries no number other than its time; no "1/4 MI", no knots, no mph.
3. Labels inside the sweep stay readable (the fill is 10 % white, under them).
4. One reading target at a time: the chip lands before the readout, the readout lines land on their words.
5. Nothing in x >= 1600, y >= 680, including during the push.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S10 start, `audio/a2-s10.words.json`; Whisper writes "band" for "ban" @14.68)
Strings: lane strings as g-a2-8/g-a2-9 · `9:30 AM` `ICE · BLOWING SNOW` `WIND STILL BUILDING` · `ALREADY ON THE ROAD` · `Erie County driving ban, WKBW` `Buffalo airport ASOS, IEM archive`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0, "So" | opening state; WKBW source line visible |
| 0.58 | ".30," @0.58 | ban card pulse `scale 1 -> 1.05 -> 1, 0.4` |
| 1.42 | "morning" @1.42 | sweep reveals right to left, 1.2 s, power2.inOut (ends 2.62) |
| 2.24 | "already" @2.24 | chip bracket draws (0.3 s), chip `fromTo(autoAlpha 0, y:16 -> 0, 0.4, power3.out)` |
| 5.16 | "7" @5.16 | "LEFT AT 7:00" pulse `scale 1 -> 1.1 -> 1, 0.4` |
| 7.06 | "38" @7.06 | M1 label pulse |
| 8.56 | "Now" @8.56 | source swaps to ASOS |
| 9.42 | "ice" @9.42 | readout tick draws up 0.3 s; "9:30 AM" and "ICE · BLOWING SNOW" `fromTo(autoAlpha 0, x:-12 -> 0, 0.3)`, stagger 0.1 |
| 12.20 | "building" @12.20 | "WIND STILL BUILDING" in |
| whole window | | lane float `y: 0 -> -3`, sine, finite yoyo; sweep fill breathes 0.10 <-> 0.14, finite |
| 13.92 | "Where" @13.92 | exit by push and fade: the whole scene group (lanes, cards, readout, chip) `to(scale 1.04, 2.48 s, ease none)` about (1025, 450) |
| 14.40 to 16.40 | "when the ban took effect?" | whole scene group and source line `to(autoAlpha 0, 2.0, power1.in)` (text moves at most about 21 px while fading; it never leaves the safe margin) |
Comp duration 16.40 s (the act's chapter blackout follows; index work).

## 6. CONTRACT
One file `compositions/g-a2-11-both-lanes.html`, root `<div id="g-a2-11-both-lanes-root" data-composition-id="g-a2-11-both-lanes" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-11-both-lanes"]`. Ids/classes `bl-`. The push is under 1.5x, so a linear scale is fine (no logZoom). Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-11-both-lanes`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-11-both-lanes`; `node scripts/overlap_check.mjs episodes/ep-buffalo-2022`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 3: frame 0 is the full opening state above (a cut from g-a2-10's ground).

## 8. RECEIPT
As the template.
