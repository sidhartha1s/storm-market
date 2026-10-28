# g-a1-4-erie-fetch-map · A1-S4 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/master-map-us-canada.html` (real Natural Earth basemap, US-Canada boundary, camera move, `logZoom` in `library/inhouse/snippets/helpers.js`) and the built `compositions/g-intro-4-morning-map.html` (same episode: Lake Erie to Buffalo already framed and styled; reuse its projection, land and water colours and the Buffalo pin so the two maps read as one place). Route fitting: `references/editing-patterns/ep3-map-route-fit.html`.

## 0. What this graphic claims
Buffalo sits at the downwind (northeast) end of Lake Erie. The forecast low would pass north into southern Ontario and "likely" set low pressure records there; the southwest winds would be strongest on Lake Erie, straight down its length, onto Buffalo; and the lake was almost entirely open water (0.5 % ice), so the wind picked up moisture all the way.

## 1. SOURCE
- Low track and records: AFD FXUS61 KBUF 211824, 1:24 PM Wed 21 Dec 2022: "setting low pressure records once it passes north of the border" (`research/nws.md` row 5.2, PRIMARY; `factcheck/a1-r1.md` row 18). Track: AFD 200951 "track from Indiana north-northeast to southern Ontario by late Friday"; AFD 211824 "roughly 990mb ... late Thursday night ... 982mb over southernmost Ontario Friday morning" (`factcheck/a1-r1.md` row 19). No mb value goes on the map (pressure lives on the dial in g-a1-3 only).
- Wind: AFD FXUS61 KBUF 221008 (5:08 AM Thu 22 Dec): "particularly Lake Erie where the southwest winds will be the strongest" (`factcheck/a1-r1.md` row 20; observed BUF wind 220 to 250 deg all Friday).
- Buffalo at the eastern tip, lake axis WSW to ENE: `factcheck/a1-r1.md` row 21.
- Ice: NOAA GLERL daily Lake Erie ice cover, 2022-23 column, 22 Dec 0.5 %, 23 Dec 0.5 %: https://www.glerl.noaa.gov/data/ice/glicd/daily/eri.txt (`factcheck/a1-r1.md` row 22, PRIMARY). NOTE: no `research/nws.md` row holds 0.5 % yet (fact-check lists it under "New evidence for research"); the orchestrator adds it.
- Places (WGS84): Buffalo 42.886 N, 78.878 W (pin at the city, east tip of the lake); Toledo 41.654 N, 83.537 W (west tip; framing only, no label); Lake Erie western basin start for the arrow about 41.75 N, 83.20 W; arrow end at Buffalo. Track points: entering the frame from the southwest edge on a line from Indiana (40.0 N, 86.0 W), through 42.3 N, 82.6 W (near Lake Erie / Lower Michigan, "late Thursday night"), to 43.4 N, 80.6 W (southernmost Ontario, "Friday morning"), ending there. The track is SCHEMATIC (a forecast, three named regions, not a plotted best track) and is labelled so.

## 2. DATUM, SCALE, ORIENTATION
North up. Equirectangular or the basemap's own projection (keep g-intro-4's). Frame bounds about 84.6 W to 77.2 W and 40.7 N to 44.5 N, fitted so that Toledo sits near x 260 and Buffalo near x 1380, y 430 (never in the corner x >= 1600, y >= 680). State the fitted px-per-degree (lon and lat) in the receipt; every point above is placed by script from that fit, never by eye. Corner x >= 1600, y >= 680: only map ground (water/land fill, no label, no pin, no arrow) may sit there.

## 3. GEOMETRY (px)
- Basemap layer `ef-map`: land `#15202b`, water `#0b1016` with a faint `#2a3644` shoreline 1.5 px, US-Canada boundary 1 px dashed `#4a5560`. Ground on from frame 0.
- Top rail `ef-rail`: x 0 to 1920, y 0 to 220, `linear-gradient(180deg, rgba(6,9,13,.92) 60%, rgba(6,9,13,0))`; the chips sit on it (no chip over open map).
- Labels (Arial 700 22 px letter-spacing 3, proper caps as given): "LAKE ERIE" `#93a3b2` centred on the water at about 42.15 N, 81.4 W, rotated to the lake axis (about -15 deg, measure from the fitted shoreline); "ONTARIO" `#93a3b2` at about 43.35 N, 81.6 W (on land, clear of the track); "BUFFALO" Arial Black `font-weight:900` 30 px `#f2f5f8`, left of and above the pin (text box ends >= 12 px from the pin, never under the arrow head).
- Pin: circle r 9 `#f2f5f8` + pulse ring (r 9 -> 28, opacity .6 -> 0, every 1.4 s, finite repeats).
- Low: letter "L" Arial Black 900 56 px `#e74c3c` in a 64 px circle stroke 3 `#e74c3c`, moving along the track by per-leg `attr`/x-y tweens (MotionPathPlugin not bundled); the track behind it a 3 px dashed `#e74c3c` line drawn by strokeDashoffset as it moves. Track label "FORECAST TRACK · SCHEMATIC" Arial 400 19 px `#93a3b2` beside the track's middle leg, on land.
- Wind arrow: a tapered band (start width 18 px, end 36 px) from the arrow start point to the pin, along the lake's long axis (it may bend gently to stay over water), fill `linear-gradient(along path, rgba(127,178,229,.3), #7fb2e5)`, drawn by a mask/strokeDashoffset; arrow head 60 px at Buffalo, stopping 14 px short of the pin. Flow dashes inside it moving toward Buffalo at 120 px/s.
- Moisture streaks: 30 small particles (3 x 14 px `#dfe7ee` at .5) rising off the water along the arrow and drifting with it toward Buffalo.
- Chip 1 "SETTING LOW PRESSURE RECORDS": Arial Black `font-weight:900` 52 px `#e8c56a`, left 200, top 96; its source "NWS Buffalo, 21 Dec 2022" Arial 400 19 px `#c8d3e0`, left 200, top 162. Chip 2 "LAKE ERIE ICE · 0.5%" and source "NOAA GLERL" in the same two slots, after chip 1 has left.
- Type tiers: 52 (chips), 22 to 30 (labels), 19 (sources, track tag).

## 4. MUST BE TRUE IN THE PICTURE
1. Geography is real: Lake Erie's shoreline, Buffalo at its east tip, Toledo end at the west, Ontario north of the lake, all from the basemap; the fit puts Buffalo's pin within 10 px of 42.886 N, 78.878 W.
2. The low passes NORTH of the lake into southern Ontario and stops there; it never passes over Buffalo. No pressure number on the map.
3. The wind arrow runs southwest to northeast down the lake's long axis and lands on Buffalo; it stays over water for its length.
4. "LAKE ERIE ICE · 0.5%" appears only with its "NOAA GLERL" source under it; "SETTING LOW PRESSURE RECORDS" only with "NWS Buffalo, 21 Dec 2022".
5. The track carries "SCHEMATIC"; the arrow claims a direction only (no speed number).
6. No label sits under the arrow, the track, the low or another label at any frame, including the first half second of each entrance.
7. Corner x >= 1600, y >= 680 holds only map ground; text within the 96 / 54 px margins at every point of the push-in (labels that would leave the margin fade first).

## 5. TEXT (exact) and CUES (seconds from A1-S4 start, `audio/a1-s4.words.json`)
Strings: `LAKE ERIE` · `ONTARIO` · `BUFFALO` · `L` · `FORECAST TRACK · SCHEMATIC` · `SETTING LOW PRESSURE RECORDS` · `NWS Buffalo, 21 Dec 2022` · `LAKE ERIE ICE · 0.5%` · `NOAA GLERL`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The wind led" @0.00 to 0.36 | map on at frame 0 at scale 1.06; slow pull to 1.0 over 0.0 to 2.6 (camera, `power2.out`) |
| 1.28 | "Buffalo" @1.28 | pin `fromTo(scale 0 -> 1, 0.4, back.out)` + pulse starts; "BUFFALO" `fromTo(autoAlpha 0, y:10 -> 0, 0.4)` |
| 2.84 | "Wednesday afternoon," @2.84 to 3.16 | "LAKE ERIE" and "ONTARIO" in (autoAlpha, 0.5) |
| 5.14 to 9.20 | "the low would ... into Ontario." @5.14 to 9.20 | low enters from the SW frame edge and runs the track to southern Ontario, per-leg tweens, `power1.inOut`; dashed track draws behind it; track tag in at 6.4 |
| 6.88 | "records" @6.88 | chip 1 + its source `fromTo(autoAlpha 0, y:-20 -> 0, 0.5, power3.out)` |
| 9.20 to 10.24 | | low ring pulses (scale 1 -> 1.15 -> 1) twice |
| 10.84 | "southwest" @10.84 | wind arrow starts drawing from the SW end |
| 12.64 | "Lake Erie," @12.64 | "LAKE ERIE" brightens to `#f2f5f8`, 0.3 s |
| 13.54 to 14.68 | "straight down the length of the lake." | arrow draws to its head at Buffalo by 15.68 (`power2.inOut`); flow dashes start at 13.54 |
| 15.68 | "Buffalo sits" @15.68 | arrow head lands; pin flash (scale 1 -> 1.6 -> 1, 0.5) |
| 17.20 | | chip 1 and source `to(autoAlpha 0, y:-20, 0.4, power3.in)`; low and track dim to 0.35 |
| 18.62 | "open water" @18.62 to 19.00 | chip 2 + "NOAA GLERL" in like chip 1; water fill brightens a step (`#0b1016` -> `#12202e`, 0.6 s) |
| 20.36 to 22.16 | "every mile ... more moisture." | moisture particles rise off the water along the arrow and drift to Buffalo (continuous to the end) |
| 23.12 to 28.54 | "The forecasters could see ... on the roads." | camera push toward the pin, `logZoom` 1.0 -> 1.6, 23.12 to 28.9; at 25.42 ("They could not") chip 2, source, track tag, "ONTARIO" and the low fade (0.5 s) before they reach the margin; "BUFFALO" and pin stay |
| 28.90 to 29.50 | tail | fade-through to black, 0.6 s, `power2.in` |
Comp duration 29.5 s. The pin pulse, flow dashes and particles keep motion through every hold.

## 6. CONTRACT
One file `compositions/g-a1-4-erie-fetch-map.html`, root `id="g-a1-4-erie-fetch-map-root"`, `data-composition-id="g-a1-4-erie-fetch-map"`, PAUSED timeline at `window.__timelines["g-a1-4-erie-fetch-map"]`. Ids and classes prefixed `ef-`. The basemap data is inlined or loaded from `media/` (episode-root relative). HUD text (chips, sources) on a fixed layer that does not ride the push; map labels on the map layer fade before leaving the margin. Everything else: `references/mg-quickref.md`.

## 7. TOOLS / 7a. DONE LINE / 8. RECEIPT
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a1-4-erie-fetch-map`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a1-4-erie-fetch-map`. All seven items of template 7a; item 6: the projection fit and every placed point (pin, track points, arrow ends, label anchors) computed by script from section 1's coordinates and stated in the receipt. Item 3: frame 0 shows the map ground (no dark frame). Receipt as the template.
