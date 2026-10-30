# g-a2-2-thermo: Columbus, Thanksgiving night, 39°F to 8°F (A2-S2)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/stat-timeline.html` (time steps with a value per step); thermometer is self-drawn SVG. Prefix `t2-`.
Sits over: nothing. Full-frame designed card on track 2, background `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` on from frame 0.

CUE WARNING: `audio/a2-s2.words.json` is null bytes (unreadable). The cues below come from a scratch faster-whisper base.en word pass on the accepted `audio/a2-s2.wav` (12.12 s), 28 Oct 26. The orchestrator re-transcribes a2-s2 with the pipeline and replaces any cue that moves more than 0.1 s before dispatch.

## 0. Claim
The cold came in fast: Columbus fell from 39°F at 8 pm Thanksgiving night (Thu 23 Nov) to 20°F by midnight and 8°F by 7 am Friday.

## 1. Source
`research/nws-facts.md` §3 ILN "Columbus, Thursday night | 39F at 8 pm to 20F by midnight; 8F at 7 am Friday" (P). `factcheck/a2-r1.md` rows 4, 5 CONFIRMED (ILN: "temperatures fell from 39 degrees in Columbus at 8 PM EST on Thursday evening, to 20 (F) by midnight"; "By 7 AM EST Friday morning ... 8 (F) above zero"). Thanksgiving 1950 = Thu 23 Nov (row 4).

## 2. Datum, scale, orientation
Thermometer scale 0°F to 50°F, 10.4 px per °F: 0°F at y 880, 50°F at y 360 (520 px). Values: 39°F top at y 474.4, 20°F at y 672, 8°F at y 796.8 (computed: 880 - 10.4 × T).

## 3. Geometry (px, 1920 x 1080)
- Headline (title zone, replaces the edit_script popfig: popfigs never sit on a card): "THANKSGIVING NIGHT" Arial Black 900 58 px `#f2f5f8`, left 110, top 104. Eyebrow above it "COLUMBUS, OHIO · 1950" Arial 700 22 px `#93a3b2` tracking 6, left 110, top 70.
- Thermometer (centre-left): tube x 560 to 620 (60 px wide), y 340 to 880, radius 30, stroke 3 px `#5a768f`, fill `#0b1016`; bulb circle centre (590, 920) r 48 (bulb bottom 968, inside the 1026 limit). Ticks every 10°F on the left of the tube, x 520 to 552, labels "0°" "10°" "20°" "30°" "40°" "50°" Arial 700 22 px `#93a3b2`, right-aligned at x 510.
- Liquid: rect x 572 to 608, from y 880 up to the value; colour tween with the value: 39°F `#d8a13a` (mild, amber) to 20°F `#7fb2e5` to 8°F `#5a768f`. Moves by `scaleY` on a fixed full-height rect, transformOrigin bottom (never tween height).
- Clock face (right of the thermometer): circle centre (1060, 600) r 180, stroke 4 px `#93a3b2`, 12 tick marks, no numerals; hour hand (length 100) and minute hand (length 150), `#f2f5f8` 6 px / 4 px, pivot via `svgOrigin="1060 600"`. Hour hand rotates 8 → 12 → 7 (240°, then 210°), minute hand stays on 12 (it turns full turns: 4 then 7 turns; or keep it on 12 if the turn rate reads as noise: builder's call after a frame read).
- Time/value readout, right of the clock (x 1300, left-aligned): big value Arial Black 900 84 px `#f2f5f8` ("39°F" / "20°F" / "8°F", text-state swap: old y 0 to -20 autoAlpha 0, new y 20 to 0, 0.35 s each); label above it Arial 700 26 px `#93a3b2` tracking 4 ("THU 8 PM" / "MIDNIGHT" / "FRI 7 AM"). Readout block y 480 to 640. Right edge <= 1600 (circle corner is below y 680 anyway).
- Source line "Source: NWS Wilmington OH" Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 60.
- Tiers: 84 / 58 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Liquid tops land at y 474 (39°F), 672 (20°F), 797 (8°F) ±4 px; the drop 39 to 20 is 19 units (198 px), 20 to 8 is 12 units (125 px).
2. The bar only drains (never rises) and goes from amber to blue: the cold arrives.
3. Readout pairs exactly: THU 8 PM / 39°F, MIDNIGHT / 20°F, FRI 7 AM / 8°F (edit_script strings "THU 8 PM · 39°F", "MIDNIGHT · 20°F", "FRI 7 AM · 8°F", split into label + value).
4. Clock hour hand points at 8, then 12, then 7 when each value is spoken.
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (seconds from A2-S2 start; scratch transcript, see warning)
Text: `COLUMBUS, OHIO · 1950` · `THANKSGIVING NIGHT` · `0°` `10°` `20°` `30°` `40°` `50°` · `THU 8 PM` · `39°F` · `MIDNIGHT` · `20°F` · `FRI 7 AM` · `8°F` · `Source: NWS Wilmington OH`
- 0.00 "And": ground, empty thermometer, clock at 8 o'clock, source line on. `/* AND @0.00 */`
- 1.16 "fast": eyebrow + headline in (y 24 to 0, autoAlpha, 0.4 s). Note: the narration says "Thanksgiving night" at 2.88; the headline lands slightly earlier as the scene title. If the orchestrator prefers it on the word, move it to 2.88.
- 2.22 "8": label "THU 8 PM" in. `/* 8 @2.22 */`
- 5.14 "39": liquid rises 0 to 39°F (0.8 s, power3.out), "39°F" in. `/* 39 @5.14 */` (the only rise: it fills from empty)
- 7.06 "midnight": hour hand 8 to 12 (0.6 s), label swap to "MIDNIGHT". `/* MIDNIGHT @7.06 */`
- 7.66 "20": liquid drains to 20°F (0.7 s, power2.inOut), colour to `#7fb2e5`, value swap "20°F". `/* 20 @7.66 */`
- 8.52 "7": hour hand 12 to 7 (0.6 s), label swap "FRI 7 AM". `/* 7 @8.52 */`
- 9.70 "8,": liquid drains to 8°F, colour `#5a768f`, value swap "8°F". `/* 8 @9.70 */`
- 10.38 to exit: frost glints drift on the tube (3 small white sparks, y float ±6 px, sine yoyo, finite repeats) so the hold moves.
- Exit: last 0.6 s: whole card group `to` x -980, autoAlpha 0, 0.6 s, power3.in.
Host: data-start = A2-S2 start, duration = 12.12 + 0.40 = 12.52 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
