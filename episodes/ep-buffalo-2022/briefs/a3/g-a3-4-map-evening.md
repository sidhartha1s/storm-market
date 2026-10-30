# g-a3-4-map-evening · A3-S3 0.00-10.80 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `compositions/g-a3-2-six-min-map.html` AFTER it passed its full-size read. Copy it, rename prefix `sm-` to `me-`, keep every position. Only the changes below.

## 0. What this graphic claims
Her last video came in the early hours of Christmas Eve; that evening, Saturday 24 Dec, a man reached her car and she had lost her life. Her outcome is shown once, quietly: the car pin turns grey. No graphic detail.

## 1. SOURCE
- `research/deaths.md` section 4 (last video early 24 Dec; a man found no pulse that evening; CBS/CNN, SECONDARY), URL as g-a3-1.
- Relatives located the car that Christmas Eve: `factcheck/a3-r1.md` row 20; order "later that morning": `factcheck/a3-r2.md` row 9.
- 24 Dec 2022 was a Saturday.

## 2. DATUM, SCALE, ORIENTATION
Same as g-a3-2: full-frame ground, schematic grid, "SCHEMATIC · NOT TO SCALE" label at `left:96px; top:54px`. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
Identical to g-a3-2 for ground, grid, both pins, "HER CAR", "HOME", route (drawn, full) and "ABOUT 6 MINUTES". Opening state (frame 0) = g-a3-2's settled state minus the "STRANDED DRIVERS" chip.
- New: date chip "SAT · DEC 24 · EVENING": glass chip, `left:110px; bottom:110px`, Arial Black 900 52 px `#f2f5f8` (x about 110-800, y about 862-970).
- New: grey car state: car pin fill `#4a5560`, "HER CAR" colour `#93a3b2`, ring pulses stop.
- Route dash crawl stops when the pin greys (the line stays, static, `#93a3b2`). Motion after that: the whole map layer `me-map` drifts `scale 1 -> 1.03` (linear is fine under 1.5x) from 9.66 to host end; "SCHEMATIC" label and chip sit on a fixed HUD layer outside `me-map`.
- Source pill "CNN via CBS News, 28 Dec 2022" `left:110px; bottom:54px`.
- Type tiers: 52, 30/22, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. Frame 0 matches g-a3-2's last settled frame (same pin, label, route positions within 2 px).
2. The car pin turns grey on "lost her life", never earlier, and nothing else signals death (no cross, no flatline, no red).
3. The date chip reads exactly "SAT · DEC 24 · EVENING" and enters on "That evening".
4. No text rides the scale drift: HUD layer only.
5. "SCHEMATIC · NOT TO SCALE" visible throughout.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S3 start, `audio/a3-s3.words.json`)
Strings: as g-a3-2 (`HER CAR`, `HOME`, `ABOUT 6 MINUTES`, `SCHEMATIC · NOT TO SCALE`) + `SAT · DEC 24 · EVENING` + `CNN via CBS News, 28 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Her last video" @0.00 | map settled on from frame 0; car ring pulses every 1.2 s (finite) and route dash crawl run |
| 2.68 | "Christmas Eve." @2.68 | car pin single flash (scale 1 -> 1.12 -> 1, 0.4 s) |
| 4.98-5.92 | "relatives tracked her phone" @4.98 | a thin `#7fb2e5` locator ring closes on the car pin: circle r 120 -> 26 at (620, 578), 1.0 s, power2.in, then fades |
| 6.36 | "found the car." @6.36 | locator ring holds r 26 for 0.6 s, out 0.3 s |
| 7.42 | "That evening," @7.42 | date chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` |
| 9.66 | "had lost her life" @9.66-10.22 | car pin and "HER CAR" colour to grey over 1.2 s, sine.inOut; pulses and crawl end; map drift starts |
| 10.20-10.80 | before "Her mother" @10.82 | chip and pill out `to(x:-80, autoAlpha 0, 0.6, power3.in)`; map fades to ground 0.6 s (cut to g-a3-5) |
Comp duration 10.80 s.

## 6. CONTRACT
One file `compositions/g-a3-4-map-evening.html`, root `id="g-a3-4-map-evening-root"`, `data-composition-id="g-a3-4-map-evening"`, PAUSED timeline `window.__timelines["g-a3-4-map-evening"]`. Prefix `me-`. Colour change by tweening `fill`/`color`, not by swapping nodes in callbacks. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-4-map-evening`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-4-map-evening`. Repeat check: "ABOUT 6 MINUTES" and the pins repeat g-a3-2 by design (callback to the same map): the orchestrator declares `data-callback` on the host if `lint_timeline.py` asks.

## 7a. DONE LINE
All seven items of the template 7a.

## 8. RECEIPT
As the template.
