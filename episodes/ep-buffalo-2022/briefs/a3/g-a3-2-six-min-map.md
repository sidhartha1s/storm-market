# g-a3-2-six-min-map · A3-S1 11.60-15.20 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: pins and dashed route in `references/editing-patterns/ep3-map-route-fit.html`. FAMILY BASE for `g-a3-4-map-evening`: build this first, send it alone for a full-size read.

## 0. What this graphic claims
Her car stopped about six minutes from her house. The distance is a drive time, not a mapped place: the map is SCHEMATIC.

## 1. SOURCE
- "about six minutes from home", family's account: `research/deaths.md` section 4 (CBS/CNN wire, updated 28 Dec 2022, SECONDARY), URL as g-a3-1.
- "Stranded drivers": `research/response.md` section 5 (stranded drivers blocked routes, AP, SECONDARY); she is one of them (`deaths.md` 4).
- Her street, her house and where the car stopped are NOT in any source. No real street names, no real map, no compass.

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground: channel radial gradient (tokens.md "Canvas") on child layer `sm-ground`, on from frame 0. No scale: label "SCHEMATIC · NOT TO SCALE". Corner x >= 1600, y >= 680 holds only empty ground (the circle may stay on).

## 3. GEOMETRY (px)
- Street grid `sm-grid` (SVG 1920 x 1080): horizontal streets at y 300, 470, 600, 780; vertical at x 380, 620, 940, 1240, 1480. Stroke `#2a3644` 14 px (road bed) with a 2 px `#4a5560` centre line. Grid stays inside x 300-1560, y 240-840.
- Route `sm-route`: polyline (620,600) -> (940,600) -> (940,470) -> (1240,470). Length 320 + 130 + 300 = 750 px; dash path stroke `#f2f5f8` 5 px, `stroke-dasharray` 4 14 for the dots, draw-on with a mask path whose dash length is `ceil(750)+1` = 751 (compute from `getTotalLength()`, never typed beyond this check).
- Car pin `sm-car`: teardrop pin 44 x 60, tip at (620, 600), fill `#e8c56a` (Amber 2), with a car glyph inside (simple SVG, no text). Pulse ring `sm-car-ring`: circle r 22 -> 46 around (620, 578), stroke `#e8c56a` 3 px, opacity 0.8 -> 0.
- House pin `sm-home`: pin 44 x 60, tip at (1240, 470), fill `#f2f5f8`, house glyph inside.
- Labels (diagram label Arial 700 22 px tracking 3): "HER CAR" `#e8c56a`, right-aligned to x 584, top 556 (box about x 470-584, y 556-582), left of the car pin and above the y 600 road bed (593-607); "HOME" `#f2f5f8` centred above the house pin, top 372 (box about x 1205-1275, y 372-398; pin top 410).
- Route label "ABOUT 6 MINUTES": Arial Black 900 30 px `#f2f5f8`, tracking 1, centred at x 780, top 630 (box about x 640-920, y 630-662), under the first route leg (road bed ends y 607), clear of the vertical street at x 940 (bed 933-947). State the measured gaps in the receipt.
- Chip "STRANDED DRIVERS": glass chip as g-intro-2 `tc-chip`, `left:110px; bottom:110px`, Arial Black 900 52 px `#f2f5f8`, one line (x about 110-680, y about 862-970).
- "SCHEMATIC · NOT TO SCALE": Arial 700 19 px `#93a3b2` tracking 4, `left:96px; top:54px`.
- Source pill: "CNN via CBS News, 28 Dec 2022", as g-a3-1 `bn-src`, `left:110px; bottom:54px`.
- Type tiers: 52, 30/22, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. "SCHEMATIC · NOT TO SCALE" is on screen whenever the map is.
2. No street name, place name, compass rose or real map tile anywhere.
3. The route runs only along grid streets, from the car pin tip to the house pin tip (ends within 4 px of both tips).
4. "ABOUT 6 MINUTES" sits next to the route and touches no pin, label or road centre line it is not on.
5. The car pin is amber, the house pin white (g-a3-4 dims the car pin; keep the ids stable).
6. Nothing at x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (segment seconds, `audio/a3-s1.words.json`; host starts at 11.60, comp-local = t - 11.60)
Strings: `HER CAR` · `HOME` · `ABOUT 6 MINUTES` · `STRANDED DRIVERS` · `SCHEMATIC · NOT TO SCALE` · `CNN via CBS News, 28 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 11.60 | (before "The snow" @11.72) | ground + grid on from frame 0; grid fades 0.6 -> 1 over 0.4 s; SCHEMATIC label and source pill visible |
| 11.82 | "snow" @11.82 | car pin drops `fromTo(y:-40 -> 0, autoAlpha 0 -> 1, 0.45, back.out(1.6))`; "HER CAR" in at 12.00 |
| 12.06 | "stopped" @12.06 | chip "STRANDED DRIVERS" in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; car ring pulses start (every 1.2 s, finite repeats to host end) |
| 12.94 | "about" @12.94 | house pin drops (as car pin); "HOME" in at 13.10 |
| 13.42 | "six minutes" @13.42-13.98 | route draws car -> house, 0.9 s, power2.inOut |
| 13.70 | "minutes" @13.70 | "ABOUT 6 MINUTES" `fromTo(autoAlpha 0, y:12 -> 0, 0.4, power3.out)` |
| 14.32 | "house." @14.32 | house pin brightens (scale 1 -> 1.1 -> 1, 0.4 s) |
| whole window | | dash crawl on the route after draw (`strokeDashoffset` loop, finite), car ring pulse |
| 14.60-15.20 | after "house." ends @14.60 | chip, labels, pins out `to(autoAlpha 0, 0.6, power3.in)`, chip slides `x:-80`; ground stays to the last frame (cut to g-a3-3) |
Comp duration 3.60 s (host 11.60-15.20; it runs 0.60 s past the wav end into the segment gap: the orchestrator confirms the gap is at least 0.6 s or trims the exit to the gap).

## 6. CONTRACT
One file `compositions/g-a3-2-six-min-map.html`, root `id="g-a3-2-six-min-map-root"`, `data-composition-id="g-a3-2-six-min-map"`, PAUSED timeline `window.__timelines["g-a3-2-six-min-map"]`. Prefix `sm-`. Pins positioned by `tl.set` at 0, no static SVG `transform=` on movers. Rest: `references/mg-quickref.md`.
Footage: none (full-frame ground).

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-2-six-min-map`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-2-six-min-map`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: route length and label boxes printed from the page, not by eye.

## 8. RECEIPT
As the template.
