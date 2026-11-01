# g-a1-3-pressure-dial · A1-S3 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/ranked-bars.html` for the counted, scaled-instrument build order and masthead, and `library/inhouse/moves/moves.js` "measure-draw" for the arc that grows with the needle. No dial exists in the library; build the dial as one SVG from the numbers in section 3 (every angle is computed below, never placed by eye).

## 0. What this graphic claims
The low was forecast to fall from about 1000 mb (Thursday evening) to about 968 mb (Friday evening): 32 mb in about a day, clearing the textbook bar of 24 mb in 24 hours "easily". A deeper low means harder wind around it.

## 1. SOURCE
- AFD FXUS61 KBUF 200951, 451 AM Tue 20 Dec 2022 (IEM link in `research/nws.md` row 1.9): "The low will deepen from roughly 1000mb Thursday evening to roughly 968mb by Friday evening...easily meeting the definition of bombogenesis (24mb/24hrs)." `research/nws.md` row 5.1 (PRIMARY, forecast); `factcheck/a1-r1.md` rows 13 to 17 (CONFIRMED).
- "The deeper a low gets, the harder the wind blows around it": NWS Aberdeen, https://www.weather.gov/abr/HighWindsNovember18and19 (`acts/a1.md` S3 note, `factcheck/a1-r2.md`).
- These are FORECAST values; observed values (rows 5.4, 5.5) are not used. The word "bomb" never appears on screen (hard flag word; the chip describes the definition instead).

## 2. DATUM, SCALE, ORIENTATION
Dial centre C = (960, 580), face radius 300. Angle measured clockwise from 12 o'clock: angle(p) = -135 + (1008 - p) x 5.625 degrees (5.625 deg per mb; 1008 mb at -135, 960 mb at +135). Computed:
| mb | angle | | mb | angle |
|---|---|---|---|---|
| 1008 | -135.0 | | 980 | 22.5 |
| 1004 | -112.5 | | 976 | 45.0 |
| 1000 | -90.0 (9 o'clock) | | 972 | 67.5 |
| 996 | -67.5 | | 968 | 90.0 (3 o'clock) |
| 992 | -45.0 | | 964 | 112.5 |
| 988 | -22.5 | | 960 | 135.0 |
| 984 | 0.0 (12 o'clock) | | | |
Point at angle a, radius r: (960 + r sin a, 580 - r cos a). Pressure falls clockwise. Corner x >= 1600, y >= 680 empty (the dial's right edge is x 1260, labels end before x 1560).

## 3. GEOMETRY (px)
- Ground: channel radial gradient on `pd-ground`, on from frame 0.
- Face: circle r 300 fill `#0b1016`, 2 px bezel `rgba(255,255,255,.14)`; a bezel shimmer (a 30 deg arc of `rgba(255,255,255,.18)`, r 300, 4 px) rotating 20 deg/s for the whole comp (continuous motion).
- Ticks every 4 mb from 1008 to 960 (13 ticks): r 262 to 300, 3 px `#93a3b2`; ticks at 1000, 976 and 968 are 5 px `#f2f5f8`.
- Tick labels every 8 mb (1008, 1000, 992, 984, 976, 968, 960): Arial 700 26 px `#dfe7ee`, centred at r 228 (inside the ring). Computed centres: 1008 (798.8, 741.2); 1000 (732.0, 580.0); 992 (798.8, 418.8); 984 (960.0, 352.0); 976 (1121.2, 418.8); 968 (1188.0, 580.0); 960 (1121.2, 741.2).
- Unit: "PRESSURE · MB", Arial 700 22 px `#93a3b2` letter-spacing 3, centred (960, 700).
- Time tags outside the ring: "THU EVENING" Arial 700 22 px `#93a3b2` letter-spacing 3, right-aligned to x 630, top 568 (beside 1000 at 9 o'clock); "FRI EVENING" same style, left-aligned at x 1290, top 568 (beside 968 at 3 o'clock).
- Needle: line from C to r 270, 6 px `#f2f5f8`, round cap, hub circle r 16 `#f2f5f8`. Rotated with `rotation` and `svgOrigin:"960 580"`, set at angle -90 (1000 mb) at 0.
- Fall arc: arc r 300, 14 px stroke, from angle -90 to the needle's angle, drawn by strokeDashoffset tied to the needle (one tween drives both). Colour `#d8a13a` from 1000 to 976, `#e74c3c` from 976 to 968 (two arc paths, the second starts at 45 deg).
- 24 mb line: radial bar at angle 45 (976 mb), r 250 to 330, 10 px `#c0392b`; its label "24 MB IN 24 HRS" Arial 700 26 px `#e74c3c`, left-aligned at x 1240, top 290 (outside the ring past the bar's outer end (1193.3, 346.7)).
- Wind ring: 3 curved arrows, r 420 around C, each an 80 deg arc 4 px `#7fb2e5` with a head, spaced 120 deg, rotating COUNTERCLOCKWISE (northern-hemisphere low). Ring extent x 540 to 1380, y 160 to 1000 (clear of the chip, which ends y 166 and x about 800 where the ring is at y 192).
- Chip "32 MB IN ~24 HRS": Arial Black `font-weight:900` 52 px `#e8c56a`, left 200, top 110.
- Source line "NWS Buffalo forecast discussion, 20 Dec 2022 (forecast)": Arial 19 `#c8d3e0`, left 96, bottom 54.
- Type tiers: 52, 26, 19 to 22.

## 4. MUST BE TRUE IN THE PICTURE
1. The needle starts on 1000 and stops on 968, exactly on those ticks (angle -90 and +90): a half turn = 32 mb.
2. The red 24 mb line sits on 976 (= 1000 - 24, angle +45), so the needle visibly passes it by 8 mb (45 deg of arc).
3. 1000 and 968 appear once each on screen (as tick labels); no other readout repeats them.
4. Pressure falls clockwise and the arc fills from 1000 toward 968 only, never past 968.
5. The wind arrows turn counterclockwise and speed up only after "deeper"; no number rides them.
6. Nothing says "bomb". No observed value. The source line says "(forecast)".
7. Corner x >= 1600, y >= 680 empty; text inside the 96 / 54 px margins.

## 5. TEXT (exact) and CUES (seconds from A1-S3 start, `audio/a1-s3.words.json`)
Strings: `1008` `1000` `992` `984` `976` `968` `960` · `PRESSURE · MB` · `THU EVENING` · `FRI EVENING` · `24 MB IN 24 HRS` · `32 MB IN ~24 HRS` · source line.
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Behind" @0.00 | ground on; face `fromTo(scale 0.9 -> 1, autoAlpha 0 -> 1, 0.6, power3.out)` from 0.05; shimmer runs from 0.05 |
| 0.60 | "that wind" @0.30 to 0.54 | ticks draw in clockwise (stagger 0.04); tick labels fade up with them |
| 1.26 | "low" @1.26 | unit "PRESSURE · MB" in (y 12 -> 0, 0.4) |
| 2.68 | "pressure" @2.68 | needle and hub `fromTo(autoAlpha 0, scale 0.6 -> 1, 0.4, back.out)` on 1000; "THU EVENING" in (x:-20 -> 0, 0.4) |
| 3.96 to 6.04 | "fall 32 millibars in roughly a day." @3.96 to 6.04 | needle `rotation -90 -> 90`, `power2.inOut`; fall arc follows (amber then red past 45 deg) |
| 4.14 | "32" @4.14 | chip "32 MB IN ~24 HRS" `fromTo(autoAlpha 0, scale 1.2 -> 1, 0.4, power4.out, transformOrigin left center)` |
| 6.04 | "day." @6.04 | "FRI EVENING" in (x:20 -> 0, 0.4); needle hub pulse |
| 6.86 to 7.40 | "textbook bar" @6.86 to 7.26 | 24 mb bar `fromTo(scaleY 0 -> 1, 0.5, power3.out)` along its radius (origin at r 250) |
| 9.62 | "24" @9.62 | label "24 MB IN 24 HRS" `fromTo(autoAlpha 0, x:-16 -> 0, 0.4)` |
| 11.40 | "hours." @11.40 | amber arc (1000 to 976) brightens 0.3 s and settles |
| 13.46 to 13.82 | "clear it easily." | red arc (976 to 968) `scaleY`-free glow: stroke-width 14 -> 22 -> 14, 0.6 s; 968 label to `#e74c3c` |
| 14.76 | "deeper" @14.76 | wind ring `fromTo(autoAlpha 0 -> 1, rotation 0 -> -40, 0.6, power2.out, svgOrigin "960 580")` |
| 16.20 to 17.40 | "harder the wind blows around it." | ring rotation continues counterclockwise, accelerating: `rotation -40 -> -400`, `power2.in`, 16.20 to 18.20 |
| 18.20 to 18.80 | tail | exit: everything `to(scale 1.04, autoAlpha 0, 0.6, power2.in)` (fade-through) |
Comp duration 18.8 s. Between 7.40 and 9.62 and 11.70 to 13.46 the shimmer is the moving element (rotating at 20 deg/s, it never stops).

## 6. CONTRACT
One file `compositions/g-a1-3-pressure-dial.html`, root `id="g-a1-3-pressure-dial-root"`, `data-composition-id="g-a1-3-pressure-dial"`, PAUSED timeline at `window.__timelines["g-a1-3-pressure-dial"]`. Ids and classes prefixed `pd-`. SVG rotations use `svgOrigin`, never a static `transform=` on a mover. Everything else: `references/mg-quickref.md`.

## 7. TOOLS / 7a. DONE LINE / 8. RECEIPT
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a1-3-pressure-dial`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a1-3-pressure-dial`. All seven items of template 7a; item 6: the tick and label positions come from the angle formula in section 2 by script, stated in the receipt. Item 3: frame 0 is the ground with the face about to enter. Receipt as the template.
