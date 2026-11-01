# g-a3-2-swirl: warm air in from the Atlantic, arctic air down from Canada (A3-S2)
Builder: Opus 5.5, high effort. Depth: deep (multi-layer flow explainer). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (chart camera C1), then this brief.
Start from: g-a3-1's finished file (copy its chart, dim, scan line, track and ghost; prefix every id and class `a3w-`) plus the warm/cold arrow style of `references/editing-patterns/ep2-met-explainer.html`; arrow travel along curves by per-leg `attr` tweens (`arc-motion-path` idea; MotionPathPlugin is not bundled).
Sits over: nothing underneath; chart still `media/a3/A3-S1_c1_nws-jkl-surface-1950-11-25.jpg` inside the comp, same camera C1. Frame 0 = g-a3-1's last frame (chart, complete red track, ghost at .3, "OHIO" label).

## 0. Claim
Wind turns counterclockwise round a low: on this storm's east side warm, wet Atlantic air was pulled northwest inland; on its west side arctic air was dragged south out of Canada.

## 1. Source
- `research/maps-forecast.md` §3 M3 (NWS Jackson, fetch summary): "arctic air wrapped around the low while warm Atlantic air was drawn northwest" (SECONDARY).
- `maps-forecast.md` §2 Kistler et al.: "a very cold air mass over southwestern Canada" (origin of the arctic air).
- Counterclockwise flow round a Northern Hemisphere low: textbook (factcheck a3-r1 row 6).
- The arrows are SCHEMATIC: no wind field was read off the chart.

## 2. Datum, scale, orientation
Camera C1, static. The swirl centre is the low as printed on this 25 Nov chart, the "L" at screen (1284, 576) (corrected value from g-a3-1's receipt), not the track's Ohio end. On 25 Nov the low sat near the Virginia/Carolinas coast, so Pittsburgh (1078, 364) lies north-west of it (cold side) while Buffalo (1132, 224) and the Newark coast (1380, 296) lie north of it, where the warm air wraps; that is what g-a3-3 pins. North up. This reading of "around the low's center" is the brief writer's, reported to the orchestrator: centring on the Ohio end would put Pittsburgh on the warm side and contradict g-a3-3's Picture line.

## 3. Geometry (px)
- Warm arrows (3), `#d8a13a`, 10 px stroke ending in a 26 px arrowhead, opacity .9, glow `drop-shadow(0 0 8px rgba(216,161,58,.5))`. Each starts over the ocean east of the low and curls counterclockwise across the low's north side toward the north-west:
  - W1: (1560, 640) → (1520, 420) → (1360, 300) → (1180, 250)
  - W2: (1580, 520) → (1480, 330) → (1300, 220) → (1120, 200)
  - W3 (short, comes ashore): (1590, 600) → (1500, 420) → (1410, 320) → (1385, 305), arrowhead on the Newark coast
- Cold arrows (3), `#7fb2e5`, same stroke spec, blue glow. Start top-left (Canada side) and pour south down the low's west side, curling south-east under it:
  - C1: (820, 110) → (960, 260) → (1060, 380) → (1120, 520)
  - C2: (680, 160) → (860, 330) → (1000, 470) → (1100, 640)
  - C3: (960, 90) → (1040, 220) → (1100, 330) → (1160, 440)
  Pittsburgh's station (1078, 364) sits between C1 and C3; Buffalo's (1132, 224) sits on W2. After correcting the chart points, the builder nudges the curves (never the stations) so this stays true.
- Flow motion: each arrow is a dashed conveyor (dash 40 30) whose `strokeDashoffset` runs continuously after it draws on (finite repeats to the host end), so the air visibly moves along each curve.
- Rotation cue: a counterclockwise ring round the low, radius 110 px about (1284, 576), 3 px `#dfe7ee` at .35, three short arrowheads on it, rotating -360° over 8 s (finite repeats, `svgOrigin` at the centre). It draws on at "counterclockwise".
- The red track and dim ghost stay as g-a3-1 left them; "OHIO" label stays.
- Chips (glass chip, radius 14, padding 10 x 18, Arial Black 900 40 px):
  - "WARM OCEAN AIR" `#d8a13a`, box left x 1430, top y 110 (right edge <= 1824).
  - "ARCTIC AIR" `#7fb2e5`, box left x 130, top y 330.
- Headline (title zone, glass card left 110, top 90): "WIND TURNS COUNTERCLOCKWISE" Arial Black 900 52 px `#f2f5f8`; it exits before "ARCTIC AIR" lands so one reading target holds.
- Source line "Source: NWS Jackson, KY · arrows schematic" left 110, bottom 60 (Arial 700 19 px `#c8d3e0`).
- Tiers: 52 / 40 / 19.

## 4. Must be true in the picture
1. Every arrow turns counterclockwise around the printed low: warm arrows enter from the east/south-east over the ocean and curl to the north-west across its north side; cold arrows enter from the north-west and curl south then south-east down its west side. No arrow turns clockwise anywhere.
2. Pittsburgh's station is among the blue arrows and touched by no orange one; Buffalo's station is on an orange arrow; W3's head ends on the coast at Newark.
3. The red track and the "OHIO" label stay visible and unchanged; no arrow covers the label or a chip.
4. Warm chip lands on "warm," (8.14), cold chip on "Arctic" (14.80), never before.
5. No arrow, chip or ring in x >= 1600, y >= 680.
6. No numbers on screen.

## 5. Panel text (exact) and cues (`audio/a3-s2.words.json`, seconds from A3-S2 start)
Text: `WIND TURNS COUNTERCLOCKWISE` · `WARM OCEAN AIR` · `ARCTIC AIR` · `Source: NWS Jackson, KY · arrows schematic`
- 0.00 frame 0 = g-a3-1 last frame; scan line running. `/* NOW @0.00 */`
- 0.82 "line": red track one bright pass (a 0.8 s highlight dash running from the Carolinas pin to the Ohio end). `/* LINE @0.82 */`
- 1.76 "air": a soft halo (radius 160, `#dfe7ee` at .12) breathes in round the printed low. `/* AIR @1.76 */`
- 3.70 "counterclockwise": headline in (y 24 to 0, autoAlpha, 0.45 s, power3.out); rotation ring draws on (0.8 s) and starts turning. `/* COUNTERCLOCKWISE @3.70 */`
- 4.88 "below." (Whisper for "a low."): halo pulses once. `/* A LOW @4.88 */`
- 6.24 "east": W1 draws on (1.0 s, power2.out), conveyor starts. `/* EAST @6.24 */`
- 8.14 "warm,": W2 draws on; chip "WARM OCEAN AIR" in (scale .9 to 1, back.out(1.4), 0.4 s). `/* WARM @8.14 */`
- 9.82 "Atlantic": W3 draws on to the Newark coast. `/* ATLANTIC @9.82 */`
- 11.20 "northwest,": the three warm arrowheads pulse once (scale 1 to 1.25 to 1, 0.4 s). `/* NORTHWEST @11.20 */`
- 13.20 "west": C1 draws on; warm chip dims to .35; headline exits (`to` x -60, autoAlpha 0, 0.5 s, power3.in). `/* WEST @13.20 */`
- 14.80 "Arctic": C2 draws on; chip "ARCTIC AIR" in. `/* ARCTIC @14.80 */`
- 16.32 "Canada.": C3 draws on (0.5 s). `/* CANADA @16.32 */`
- Exit: none. Hold to host end with conveyors and ring moving; in the last 0.5 s both chips go to autoAlpha 0 (g-a3-3 opens on chart + track + arrows + ring, no chips).
Host: data-start = A3-S2 start, duration = 16.56 + 0.40 = 16.96 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
