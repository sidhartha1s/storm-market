# g-a3-6-tally-27dec · A3-S4 · deep · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `compositions/g-intro-6-count-tally.html` (same data family, same episode: match its type and colours so the two tallies read as one system) and `library/inhouse/ranked-bars.html` (fill animation). Not a copy: this is one bar of blocks, not ranked rails.

## 0. What this graphic claims
On the evening of Tue 27 Dec 2022 the county had sorted 31 people who lost their lives; 17 were found outside and 3 more in a vehicle. On that early count, outside alone (17) was more than half of 31.

## 1. SOURCE
- `research/deaths.md` section 1 row "27 Dec (evening)": 31; 17 outside, 7 lack of heat, 3 cardiac shovelling, 3 in vehicle, 1 EMS delay; county health department per NPR, https://www.kaxe.org/news/news/2022-12-27/at-least-31-people-have-died-in-buffalos-erie-county-due-to-destructive-winter-storm (27 Dec 2022, updated 8:32 PM ET), SECONDARY.
- `research/deaths.md` section 3: 17/31 = 55 %, CONFIRMED as reported.
- Other causes = 31 - 17 - 3 = 11 (7 + 3 + 1, same row). Not spoken; shown as unlabelled-by-number dim blocks named "OTHER CAUSES".
- Later counts (37, 39, 46) are NOT shown here (g-intro-6 has them).

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `ty-ground`, frame 0). Scale: 1 block = 1 person, 31 blocks, pitch 46 px. Bar runs left to right, x 250-1670, y 470-590. Halfway datum = bar midpoint x 960 (15.5 blocks). Corner x >= 1600, y >= 680 empty (the bar ends at y 590).

## 3. GEOMETRY (px) — compute block x from the formula with a script and print it in the receipt
- Block i (i = 0..30): rect x = 250 + 46 i, width 40, y 470, height 120, radius 6. Bar span x 250-1670 (31 x 46 - 6 = 1420).
- Colours, in order left to right: i 0-16 (17 blocks) `#f2f5f8` OUTSIDE; i 17-19 (3) `#d8a13a` IN A VEHICLE; i 20-30 (11) `#2a3644` OTHER CAUSES. Unfilled state: 1 px `rgba(255,255,255,.14)` outline, fill transparent.
- Run spans: OUTSIDE x 250-1026 (centre 638); IN A VEHICLE x 1032-1164 (centre 1098); OTHER x 1170-1670 (centre 1420).
- Run labels, Arial 700 26 px tracking 8 (section header tier), top 620, centred on their run: "OUTSIDE" `#f2f5f8`; "IN A VEHICLE" `#d8a13a` (width about 280, x about 958-1238: it must not touch the halfway line, see §4.4; if it does, set it at tracking 4 and state the box); "OTHER CAUSES" `#93a3b2` (x about 1260-1580).
- Halfway line `ty-half`: dashed, 3 px `#e74c3c`, dash 10 8, x 960, y 430-610 (crosses block 15, which spans 940-980). Tag "HALF" Arial 700 22 px `#e74c3c` tracking 6, centred x 960, top 396.
- Readout "17 OF 31": Arial Black 900 84 px, "17" `#f2f5f8`, " OF 31" `#93a3b2`; centred x 960, top 270 (box y 270-354). Over the line, as the Picture line asks.
- Date chip "TUE · DEC 27 · EVENING": eyebrow, Arial 700 22 px `#93a3b2` tracking 6, `left:96px; top:96px`; under it the headline "THE COUNTY'S EARLY COUNT" Arial Black 900 52 px `#f2f5f8`, left 96, top 132. (Headline names the thing; only these two lines top-left.)
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Erie County health department, via NPR/KAXE, 27 Dec 2022".
- Type tiers: 84/52 big, 26 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 31 blocks, equal size and pitch; 17 white, 3 amber, 11 dim. Count them on the settled frame.
2. White run ends at x 1026, right of the halfway line x 960: 17 > 15.5. The line visibly falls inside the white run (block 15).
3. The halfway line is at the bar's true midpoint (x 960 ± 2), not at the 16th block's edge.
4. No label touches the halfway line, a block or another label; "IN A VEHICLE" stays right of x 970.
5. No figure besides 17, 31 and the date on screen (no 55 %, no 46, no 39).
6. Numerals on screen, words in the voice; "17 OF 31" lands on "more than half", after the line.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S4 start, `audio/a3-s4.words.json`)
Strings: `TUE · DEC 27 · EVENING` · `THE COUNTY'S EARLY COUNT` · `OUTSIDE` · `IN A VEHICLE` · `OTHER CAUSES` · `HALF` · `17` · ` OF 31` · `Erie County health department, via NPR/KAXE, 27 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "She wasn't the only one" | ground on frame 0; 31 empty outlines fade in 0.0-0.6 (stagger 0.02) |
| 2.40 | "evening of December 27th" @2.40-3.14 | eyebrow date in at 2.86 `fromTo(autoAlpha 0, y:12 -> 0, 0.4)`; headline at 3.14 `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; source in |
| 5.84 | "31" @5.84 | all 31 blocks fill dim `#2a3644` left to right, `scaleY 0 -> 1` from bottom, stagger 0.03 (0.9 s total) |
| 8.40 | "17" @8.40 | blocks 0-16 recolour to white, left to right, stagger 0.04 (0.68 s), each `scale 1 -> 1.08 -> 1` |
| 9.28 | "outside." @9.28 | "OUTSIDE" `fromTo(autoAlpha 0, y:10 -> 0, 0.4, power3.out)` |
| 10.30 | "Three" @10.30 | blocks 17-19 recolour amber, stagger 0.08 |
| 11.12 | "vehicle," @11.12 | "IN A VEHICLE" in (as OUTSIDE); "OTHER CAUSES" in at 11.40 at 70 % opacity |
| 12.46 | "early count," @12.22-12.46 | halfway line draws top to bottom `scaleY 0 -> 1`, 0.5 s; "HALF" at 12.80 |
| 13.32 | "outside was" @13.32 | white run brightens (a sheen sweeps x 250 -> 1026, 0.6 s); "OUTSIDE" to `#ffffff` |
| 13.86 | "more than half." @13.86 | "17 OF 31" `fromTo(scale 1.2 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| whole window | | after each build step, the newest group floats y 0 -> -3 (sine, yoyo, finite); no 4 s gap without a tween |
| 14.90-15.50 | after "half." ends @14.46 | whole layer pulls back `scale 1 -> 0.96`, autoAlpha 0, 0.6, power3.in; ground stays |
Comp duration 15.50 s (1.04 s past the wav end; trim to the real gap).

## 6. CONTRACT
One file `compositions/g-a3-6-tally-27dec.html`, root `id="g-a3-6-tally-27dec-root"`, `data-composition-id="g-a3-6-tally-27dec"`, PAUSED timeline `window.__timelines["g-a3-6-tally-27dec"]`. Prefix `ty-`. Blocks positioned by `tl.set` from the formula (a loop over i is fine; the brief's table is the source). Repeat note: "OUTSIDE" and "17" also appear in g-intro-6 (another comp, minutes earlier), which is a callback, not a per-frame repeat. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-6-tally-27dec`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-6-tally-27dec`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print every block's x and the three run spans from the page.

## 8. RECEIPT
As the template.
