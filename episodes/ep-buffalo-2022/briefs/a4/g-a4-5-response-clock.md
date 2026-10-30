# g-a4-5-response-clock · A4-S5 (0 to 14.90 s) · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the ring of `mk-usage-arc` / `conic-progress-ring` (`library/catalog-index.json`, official; copy into the episode, never `npx hyperframes add` into it), retuned to the tokens below. Shares segment A4-S5 with `g-a4-6-relief-line`, which starts at 14.90.

## 0. What this graphic claims
In the city, emergency services took 22.72 hours on average to respond to a call (about 23): a call made at breakfast was answered the next morning, with a whole night in between.

## 1. SOURCE
- NYU Wagner report p.142: "throughout the city, it took 22.72 hours on average for emergency services to respond to a call", from 6,119 city 911 calls 23 to 26 Dec (`factcheck/a4-r1.md` row 18, PRIMARY); `research/response.md` section 2 (Firehouse citing NYU, SECONDARY). "Breakfast to next morning" is arithmetic on 22.72 h, illustrative (row 19).
- Schematic choices (not on screen as numbers): the call is placed at 8:00 AM; night is drawn from 4:40 PM (late-December Buffalo sunset, general knowledge, positioning only). No clock time is printed anywhere.

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground. A 24-hour ring: centre (960, 540), radius 300 (stroke centreline), 0 h (the call) at the top, clockwise. Scale 15° per hour. The arc spans 22.72 h = 340.8°. Presenter circle may be on: nothing in x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- Ground: channel radial gradient from frame 0.
- Track: circle r 300, stroke 28 px `#15202b`. Ticks: 24, outside the track from r 318 to r 330 (`#2a3644`, 2 px); every 6th tick (0, 6, 12, 18 h) from r 318 to r 342, `#93a3b2`, 3 px. No numerals on the dial.
- Arc: same centreline and width as the track, `#d8a13a`, round cap, drawn with stroke-dashoffset from 0 h to 340.8° (path length = ceil(2π x 300 x 340.8/360) + 1 = 1,785). Arc end point: (861.4, 256.7) = (960 + 300 sin 340.8°, 540 - 300 cos 340.8°).
- Start marker: 12 px `#f2f5f8` dot at (960, 240). Label "BREAKFAST", Arial 700 22 px `#f2f5f8`, letter-spacing 3, left edge x 1000, centre y 205.
- End marker: 12 px `#e8c56a` dot at (861.4, 256.7). Label "NEXT MORNING", Arial 700 22 px `#e8c56a`, letter-spacing 3, right edge x 840, centre y 215.
- Night span: the part of the arc from 8.67 h (130.0°) to 22.72 h (340.8°) is recoloured `#5a768f` at its cue (an overlay arc on top, its own dash draw). Moon icon (40 px crescent, `#7fb2e5`) at the night span's midpoint, outside the ring at r 380, angle 235.4°: (647.2, 755.8) = (960 + 380 sin 235.4°, 540 - 380 cos 235.4°).
- Centre chip (inside the ring, no card, designed ground): "AVG RESPONSE" Arial 700 22 px `#93a3b2`, letter-spacing 6, centred, baseline y 470; "~23 HRS" Arial Black `font-weight:900` 84 px `#f2f5f8`, centred, baseline y 585. The "~" stays (the true figure is 22.72).
- Source pill: glass (as `g-intro-2-toll-chips`), radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Serif sub "In the city", Georgia italic 30 px `#d8a13a`, centred, baseline y 640: the average holds for the city only, and the voice says "In the city" (brief-writer addition to the Picture's chip, so the chip is not read as county-wide).
- Type tiers: 84 (big), 30 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The arc ends 19.2° short of a full circle (340.8°): visibly almost, not quite, a full day. Arc end within ±10 px of (861.4, 256.7).
2. The arc starts at the BREAKFAST dot and ends at the NEXT MORNING dot; the two labels never touch each other or the ring.
3. The night recolour covers 130.0° to 340.8° only: the morning and afternoon part of the arc stays amber.
4. No clock time or hour numeral appears; the only number on screen is "~23".
5. The centre chip lands on "23" @3.84; the arc never moves before "breakfast" @8.38.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S5 start, `audio/a4-s5.words.json`)
Strings: `AVG RESPONSE` `~23 HRS` `In the city` · `BREAKFAST` · `NEXT MORNING` · source `NYU Wagner review, via Firehouse`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "In the city" @0.00 to 0.26 | ground on; "In the city" sub in at 0.26 `fromTo(autoAlpha 0, y:10 -> 0, 0.4)` |
| 2.24 | "emergency services" @2.24 | track and ticks draw: track `fromTo(scale 0.92 -> 1, autoAlpha 0 -> 1, 0.5, power3.out)`, ticks stagger 0.02; source pill in |
| 3.26 | "took" @3.26 | "AVG RESPONSE" in `fromTo(autoAlpha 0, y:10 -> 0, 0.3)` |
| 3.84 | "23" @3.84 | "~23 HRS" `fromTo(scale 1.3 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 8.38 | "breakfast" @8.38 | start dot + BREAKFAST label in `fromTo(scale 0 -> 1, 0.3, back.out(1.6))` / `fromTo(autoAlpha 0, x:-10 -> 0, 0.3)` |
| 8.38 to 10.02 | "with help arriving the next morning" | arc draws 0 -> 340.8°, `power1.inOut`, lands at 10.02 |
| 10.02 | "morning." @10.02 | end dot + NEXT MORNING label in (as the start) |
| 13.68 | "whole night" @13.68 | night overlay arc draws 130.0° -> 340.8° in 0.6 s power2.out; moon in `fromTo(autoAlpha 0, rotation:-20 -> 0, 0.5)`; ground radial darkens 10 % (overlay at opacity 0 -> 0.1) |
| whole window | | centre chip and labels float `y 0 -> -3`, sine, finite repeats; arc end dot pulses (scale 1 -> 1.4 -> 1, 1.2 s) from 10.02 |
| 14.30 to 14.90 | after "alone." @14.04 | whole comp fades through to ground: content `to(autoAlpha 0, 0.6, power2.in)`, the ground stays to the end (g-a4-6 starts on the same ground) |

Comp duration 14.90 s (host = A4-S5 start to start + 14.90).

## 6. CONTRACT
One file `compositions/g-a4-5-response-clock.html`, root `<div id="g-a4-5-response-clock-root" data-composition-id="g-a4-5-response-clock" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-5-response-clock"]`. Ids prefixed `rc-`; classes prefixed `rc-`. Inline SVG; dash lengths `ceil(len)+1` measured, never typed. Ground on from frame 0. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-5-response-clock`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-5-response-clock`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: arc end, night span and moon position computed by a script from section 2's numbers. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
