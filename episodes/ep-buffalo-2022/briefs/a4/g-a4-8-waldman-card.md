# g-a4-8-waldman-card · A4-S7 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `.namecard` in `library/inhouse/snippets/cards.css` (type sizes) on the chip surface of the built `compositions/g-intro-2-toll-chips.html`; the inset map reuses the data, styling and projection of `g-a4-10-ems-pins` (build that first; if it is not built yet, take data and styling from the built `compositions/g-intro-4-morning-map.html`).

## 0. What this graphic claims
1. Who: Private First Class Matthew Waldman, 105th Military Police Company, New York Army National Guard.
2. Where the woman in labor was taken: Erie County Medical Center, Buffalo.
3. Her baby was born on Christmas Eve.
The photo under it is NOT Waldman (no photo of him exists in research): nothing in this comp points at a person.

## 1. SOURCE
- DVIDS news 436463, Staff Sgt. Matthew Gunther, 6 Jan 2023 (PRIMARY, public domain): Pfc. Matthew Waldman, 105th MP Co, "I had to wade through it to get to her door"; he and his mother's boyfriend went in a truck, "Then they made their way to Erie County Medical Center"; baby "born on Christmas Eve". `research/response.md` section 7 row 6; `factcheck/a4-r1.md` rows 26, 27, 28 (CONFIRMED; driver not named, no age).
- ECMC location: 462 Grider Street, Buffalo, about 42.926 N, 78.830 W (positioning only, not printed; confirm on OpenStreetMap and report the value used).
- Footage under it: DVIDS D2, 7572836, 107th Attack Wing Airmen helping motorists stuck in drifts near Buffalo, 25 Dec 2022 (`research/cc-clips-r2.md` row D2), soft focus applied on the index mount (not by this comp).

## 2. DATUM, SCALE, ORIENTATION
Overlay over the D2 still. Lower-third anchor `left:110px; bottom:110px`. Inset map: the `g-a4-10-ems-pins` projection (north up, cosine correction at 42.6° N, 1300 px per degree of latitude, 956.9 px per degree of longitude, datum (78.79° W, 42.77° N) = (960, 540)), unscaled, translated by (+577.9, +38.4) so ECMC (map (922.1, 336.6)) lands at screen (1500, 375). Presenter circle may be on: nothing in x >= 1600, y >= 680.

## 3. GEOMETRY (px)
- Name card (glass as g-intro-2, padding 22 px 34 px, `left:110px; bottom:110px`, hugs text, two lines, left-aligned): line 1 "PFC. MATTHEW WALDMAN" Arial Black `font-weight:900` 52 px `#f2f5f8`; line 2 "105TH MILITARY POLICE CO." Georgia italic 30 px `#e8c56a`, 8 px below. About x 110 to 830, y 800 to 970. No photo slot, no monogram, no arrow.
- Inset map card: x 1200 to 1800, y 150 to 600, radius 20, fill `rgba(11,16,22,.92)` with the glass border, `overflow:hidden` (clips the map). Inside, in the translated projection: land `#15202b`, water (Lake Erie, Niagara River) `#04070a` with 1.5 px `#5a768f` shoreline (Natural Earth 10m lakes / rivers), Erie County outline 1.5 px `#93a3b2` (Census `cb_2022_us_county_500k` 36029), City of Buffalo outline 2 px `#d8a13a` (Census `cb_2022_36_place_500k`, GEOID 3611000).
- ECMC pin at (1500, 375): 9 px `#e74c3c` dot + 2 px ring pulsing (scale 1 -> 2.2, opacity 0.6 -> 0, 1.2 s, finite repeats). Label "ERIE COUNTY MEDICAL CENTER", Arial 700 22 px `#f2f5f8`, letter-spacing 3, centred on x 1500, baseline y 430, on a 0.6-opacity `#0b1016` backing so it reads over the city line. Small "BUFFALO" label Arial 700 19 px `#d8a13a`, letter-spacing 3, inside the city outline near its centre (about map (893, 381) + translate = (1471, 419)), moved left or down until it is 12 px clear of the ECMC label; report its final spot.
- Chip (same slot and surface as the name card, after it leaves): "BORN" Arial Black 900 52 px `#f2f5f8` + " CHRISTMAS EVE" Arial Black 900 38 px `#e8c56a`. About x 110 to 700, y 842 to 970.
- Source pill: glass, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`.
- Type tiers: 52 (big), 30 and 38 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The name card names no one in the photo: it sits in the lower-third slot with no pointer, and the orchestrator checks it does not sit on or next to a single face (if it does, the index picks a still framing with no face near the lower left).
2. The ECMC pin is inside the City of Buffalo outline, north-east of downtown, within ±10 px of (1500, 375); the pin never appears over the photo itself, only inside the map card.
3. The name card and the chip are never on screen together; the map card and the name card are never on screen together.
4. "105TH" and the "Pfc." rank are as written; no age, no driver, no "young".

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S7 start, `audio/a4-s7.words.json`)
Strings: name `PFC. MATTHEW WALDMAN` / `105TH MILITARY POLICE CO.` (the Picture's "·" is this line break) · `ERIE COUNTY MEDICAL CENTER` · `BUFFALO` · chip `BORN CHRISTMAS EVE` · source `New York National Guard, DVIDS, 6 Jan 2023`

| t (s) | spoken word | action |
|---|---|---|
| 1.20 | "Private" @1.20 | name card in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`, line 1 first, line 2 at 1.68 ("Class") `fromTo(autoAlpha 0, y:10 -> 0, 0.35)`; source pill in at 1.20 |
| 5.20 to 5.55 | "He and" @5.52 | name card out `to(x:-80, autoAlpha 0, 0.35, power3.in)` |
| 6.48 | "got her" @6.48 | map card in `fromTo(x:60 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`, map drawn, no pin yet; BUFFALO label in at 6.70 |
| 7.02 | "hospital," @7.02 | ECMC pin `fromTo(scale 0 -> 1, 0.35, back.out(1.8))`, label `fromTo(autoAlpha 0, y:8 -> 0, 0.35)`; ring pulse starts |
| 8.62 | "born" @8.62 | chip in (as name card), "BORN" `fromTo(scale 1.25 -> 1, 0.4, power4.out)`; " CHRISTMAS EVE" span in at 9.10 ("Christmas") |
| whole window | | visible cards float `y 0 -> -3`, sine, finite repeats; pin ring pulse |
| 9.86 to 10.40 | after "Eve." @9.36 | map card, chip and pill out `to(x:980, autoAlpha 0, 0.54, power3.in)` |

Comp duration 10.40 s (wav 9.86 + land). The orchestrator starts S8 at least 0.55 s after the S7 wav ends; if it cannot, the cut into the S8 photo carries the cards off and the exit row is trimmed to fit.

## 6. CONTRACT
One file `compositions/g-a4-8-waldman-card.html`, root `<div id="g-a4-8-waldman-card-root" data-composition-id="g-a4-8-waldman-card" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-8-waldman-card"]`. Ids prefixed `wc-`; classes prefixed `wc-` (never `.namecard`, `.glasscard`, `.srclab`: index.html uses them). Root transparent. Map paths computed by a script from the named data. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-8-waldman-card`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-8-waldman-card`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: projection, translate and the ECMC point computed by a script; state them. Item 7: frames at 3.0 s and 9.0 s composited over DVIDS 7572836 in its soft-focus mount.

## 8. RECEIPT
As the template.
