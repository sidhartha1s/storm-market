# g-a4-10-ems-pins · A4-S9 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, `references/editing-patterns/ep3-map-route-fit.html`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-intro-4-morning-map.html` (same data sources, land/water/line styling, pin and ring) at a closer scale, and `library/inhouse/master-map-us-canada.html`. This comp's projection and Buffalo geometry are reused by `g-a4-8-waldman-card`'s inset: build this one first.

## 0. What this graphic claims
1. In the end, the NYU review counted seven people in Erie County who lost their lives because of what officials called a delayed emergency response (backlogged calls, unplowed streets, stranded vehicles).
2. The last three confirmed were all heart emergencies, in date order: Cheektowaga on 24 Dec, Amherst on 25 Dec, Buffalo on 27 Dec. The pins mark the TOWN, never an address (no source gives one).

## 1. SOURCE
- NYU Wagner report p.13 and p.139 (PRIMARY): seven died "because of what officials have characterized as a delayed EMS response due to backlogged calls, unplowed streets, and stranded vehicles". `factcheck/a4-r1.md` rows 35, 36. Final county category "7 delayed EMS": `research/deaths.md` section 1 final row (WIVB, SECONDARY).
- Last three: WIVB, "all three ... due to a delayed EMS response during cardiac events": Cheektowaga 24 Dec, Amherst 25 Dec, Buffalo 27 Dec; dates are emergency dates. `research/deaths.md` section 2; `factcheck/a4-r1.md` row 34 (CONFIRMED). https://www.wivb.com/weather-news/buffalo-blizzard-2022/erie-county-medical-examiner-confirms-three-more-blizzard-related-deaths-bringing-total-to-47/amp/
- Map geometry (public domain; land the data in `episodes/ep-buffalo-2022/media/map/` or inline the paths, never a path outside the repo):
  - Erie County (36029) and Niagara County (36063): Census `cb_2022_us_county_500k`.
  - Town of Cheektowaga and Town of Amherst: Census `cb_2022_36_cousub_500k`; City of Buffalo: `cb_2022_36_place_500k` GEOID 3611000. Pins at each polygon's Census interior point (expected: Buffalo 42.8925 N, 78.8597 W; Cheektowaga 42.9089 N, 78.7472 W; Amherst 43.0109 N, 78.7566 W). Report the values you used.
  - Lake Erie, Niagara River, Ontario land: Natural Earth 10m `ne_10m_lakes`, `ne_10m_rivers_lake_centerlines`, `ne_10m_admin_1_states_provinces`.

## 2. DATUM, SCALE, ORIENTATION
- North up. Equirectangular with a cosine correction at 42.6° N (cos = 0.7361).
- Scale: 1300 px per degree of latitude; 956.9 px per degree of longitude.
- Datum: (78.79° W, 42.77° N) = screen (960, 540). `x = 960 + (lon + 78.79) * 956.9`, `y = 540 - (lat - 42.77) * 1300`.
- Erie County then spans about x 635 to 1276, y 111 to 969. Compute every path with a script and state the numbers in the receipt.
- No camera move in this comp.

## 3. GEOMETRY (px)
- Ground: channel radial gradient from frame 0. Land `#15202b`; Ontario and land outside Erie County `#0b1016`; water `#04070a` with 1.5 px `#5a768f` shoreline; county lines 1 px `#2a3644`.
- Erie County outline: 3 px `#d8a13a`, fill `rgba(216,161,58,.06)`, drawn with stroke-dashoffset. Town outlines (Buffalo, Cheektowaga, Amherst): 1 px `#4a5560`, no fill.
- Labels on the map: "LAKE ERIE", Arial 700 26 px `#7fb2e5`, letter-spacing 3, centred near (472, 761), wholly on water (move it along the lake until it is); "ERIE COUNTY", Arial 700 22 px `#d8a13a`, letter-spacing 3, centred near (1000, 700), inside the outline, clear of every pin label.
- Pins (expected, ±10 px): Buffalo (893.3, 380.8), Cheektowaga (1001.0, 359.4), Amherst (992.0, 226.8). Each pin: 9 px `#e74c3c` dot + 2 px ring pulsing (scale 1 -> 2.2, opacity 0.6 -> 0, 1.2 s, finite repeats).
- Pin labels (Arial 700 22 px, letter-spacing 3, each led by a heart-line icon: a 34 x 20 px ECG trace, 2.5 px stroke `#e74c3c`, 8 px before the text):
  - "CHEEKTOWAGA" `#f2f5f8` + " · DEC 24" `#e8c56a`: icon left edge x 1030, text after it, centre y 360 (to about x 1370).
  - "AMHERST" + " · DEC 25": icon left edge x 1021, centre y 227 (to about x 1260).
  - "BUFFALO" + " · DEC 27": placed LEFT of its pin, reading icon, "BUFFALO", " · DEC 27", right edge x 865, centre y 404 (left of and just below the pin, clear of its ring and of the Cheektowaga ring). It sits over the Niagara River / Ontario side: give it a 0.6-opacity `#0b1016` backing if the shoreline crosses it.
- Chip (top-left title zone, glass as `g-intro-2-toll-chips`, padding 22 px 34 px, `left:110px; top:110px`): "7" Arial Black `font-weight:900` 84 px `#f2f5f8` + 16 px gap + "LINKED TO DELAYED EMS" Arial Black 900 38 px `#dfe7ee`. About x 110 to 720, y 110 to 238 (over Ontario land on the Niagara peninsula, no label there).
- Source slot: glass pill, radius 14, padding 5 px 12 px, `left:110px; bottom:54px`, Arial 400 19 px `#c8d3e0`; two pre-authored strings (S-A NYU, S-B WIVB), one at a time.
- Snow: 30 slow-falling dots (2 to 3 px, `#dfe7ee` at 0.4), 14 px/s, finite repeats, the whole window (the sombre moving layer).
- Type tiers: 84 (big), 26 and 38 (mid), 19 and 22 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. All three pins are inside the Erie County outline, each inside its own town outline: Buffalo west, Cheektowaga east of Buffalo, Amherst north of both. Within ±10 px of section 3.
2. Pins land in date order on their spoken town names: Cheektowaga, then Amherst, then Buffalo. Each date appears on its spoken date.
3. Only three pins ever appear; the chip says 7; nothing on screen suggests the seven were at home or anywhere else (no house icons, no "at home").
4. No pin label touches another label, a ring, a pin or a county line; the corner x >= 1600, y >= 680 holds no label or pin.
5. One source string at a time: S-A (NYU) with the chip, S-B (WIVB) with the pins.

## 5. PANEL TEXT (exact) and CUES (seconds from A4-S9 start, `audio/a4-s9.words.json`)
Strings: `LAKE ERIE` · `ERIE COUNTY` · chip `7 LINKED TO DELAYED EMS` · `CHEEKTOWAGA · DEC 24` · `AMHERST · DEC 25` · `BUFFALO · DEC 27` · S-A `NYU Wagner review, via AP, 2 Jun 2023` · S-B `Erie County Medical Examiner, via WIVB`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "For some people" @0.00 | ground, water, land and snow on from frame 0 |
| 1.12 to 2.10 | "help came too late" @1.12 to 1.80 | Erie County outline draws (dashoffset, 1.0 s, power2.inOut); fill in after it |
| 2.30 | after "late." @1.80 | LAKE ERIE and ERIE COUNTY labels in `fromTo(autoAlpha 0, y:8 -> 0, 0.4)` |
| 5.32 | "seven" @5.32 | chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; "7" `fromTo(scale 1.3 -> 1, 0.4, power4.out)`; S-A in |
| 10.34 to 14.98 | "Officials blamed backlogged calls, unplowed streets and stranded vehicles" | chip holds; snow; the outline's fill breathes 0.06 -> 0.10 -> 0.06 (2 s, sine) |
| 15.70 | before "The last three" @15.90 | chip dims to opacity 0.5; S-A out, S-B in |
| 19.26 | "Cheek" @19.26 | Cheektowaga pin drops `fromTo(y:-40 -> 0, autoAlpha 0 -> 1, 0.45, bounce.out)`; icon draws (dashoffset 0.4 s); "CHEEKTOWAGA" in |
| 20.06 | "Christmas Eve" @20.06 | " · DEC 24" in `fromTo(autoAlpha 0, x:-8 -> 0, 0.3)` |
| 21.42 | "Amherst" @21.42 | Amherst pin, icon, "AMHERST" (as above) |
| 21.84 | "Christmas Day" @21.84 | " · DEC 25" in |
| 22.98 | "Buffalo" @22.98 | Buffalo pin, icon, "BUFFALO" |
| 23.68 | "27th" @23.68 | " · DEC 27" in |
| whole window | | snow; each landed pin's ring pulses |
| 24.32 to 24.90 | after "27th." | hold (land time); full-frame scene ends on the cut into the S10 photo |

Comp duration 24.90 s (wav 24.32 + land). The orchestrator leaves 0.6 s before S10 ("Wind bed drops low" here is a mix note for the orchestrator).

## 6. CONTRACT
One file `compositions/g-a4-10-ems-pins.html`, root `<div id="g-a4-10-ems-pins-root" data-composition-id="g-a4-10-ems-pins" data-width="1920" data-height="1080">`, PAUSED timeline at `window.__timelines["g-a4-10-ems-pins"]`. Ids prefixed `ep-`; classes prefixed `ep-`. No static SVG `transform=` on any mover; dash lengths measured. Ground on from frame 0. Everything else: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a4-10-ems-pins`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a4-10-ems-pins`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: projection, outlines and the three interior points computed by a script; state them. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
