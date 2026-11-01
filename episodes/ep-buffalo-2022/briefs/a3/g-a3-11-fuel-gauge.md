# g-a3-11-fuel-gauge · A3-S9 6.70-15.30 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: no close exemplar; geometry below. Chip + source pill from `compositions/g-intro-2-toll-chips.html`.

## 0. What this graphic claims
A surgeon from Erie County Medical Center, stuck in a car with his elderly mother, was, in Hochul's words, "running out of fuel"; state fire teams got them out. Staying put had a limit. The gauge is illustrative: no fuel level was reported, so the needle never sits at a stated value and never reaches E.

## 1. SOURCE
- `research/response.md` section 2 row "ECMC surgeon chief rescued from car": "trapped in a vehicle with his elderly mother, and they're running out of fuel" (Hochul, 26 Dec 2022 briefing transcript, PRIMARY), URL as g-a3-10.
- Surgeon at ECMC: `factcheck/a3-r1.md` row 50 CONFIRMED.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient, layer `fg-ground`, frame 0), dashboard-dark. Gauge dial is a half circle, E on the left, F on the right, needle pivot at (960, 640). Angle convention for the needle (drawn pointing straight up at rotation 0): E = -90°, 1/2 = 0°, F = +90°. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Dial arc `fg-arc`: half circle centre (960, 640), radius 320, from (640, 640) through (960, 320) to (1280, 640); stroke `#93a3b2` 10 px, round caps.
- Low zone: the first 1/8 of the arc from E (-90° to -67.5°) restroked `#c0392b` 12 px.
- Ticks at -90, -45, 0, +45, +90 degrees: 6 px wide, 36 px long inward from the arc, `#dfe7ee`.
- Labels Arial Black 900 52 px: "E" `#c0392b` centred at (590, 640) baseline-centre; "F" `#dfe7ee` centred at (1330, 640). (Both outside the arc ends.)
- Needle `fg-needle`: tapered polygon from the pivot, length 290, base width 16, `#e74c3c`; hub circle r 26 `#15202b` with 2 px `#93a3b2` ring. Rotate with `svgOrigin:"960 640"`.
- Fuel pump icon `fg-pump` (SVG glyph, 56 px, no text) at (960, 520), `#d8a13a`, starts at 25 % opacity.
- Chip "RUNNING OUT OF FUEL": glass, `left:110px; bottom:110px`, Arial Black 900 52 px `#f2f5f8` (x about 110-800, y about 862-970). Its quote is Hochul's ("they're running out of fuel"): no quote marks on the chip, it labels the gauge.
- Source pill `left:110px; bottom:54px`: "Gov. Kathy Hochul, storm briefing, 26 Dec 2022".
- Small label "ILLUSTRATION" Arial 700 19 px `#93a3b2` tracking 4, `left:96px; top:54px`.
- Type tiers: 52 big, (mid: none — 3 text nodes besides E/F; state the count), 19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. The needle starts at -45° (a quarter tank) and ends at -80° (inside the red zone, clear of E at -90°); it never touches -90°.
2. No number on the gauge (no litres, gallons, percent, miles).
3. The needle moves on "running out of fuel", not before.
4. Nothing at x >= 1600, y >= 680; the dial ends at x 1280 and y 640.
5. "ILLUSTRATION" on screen the whole window.

## 5. PANEL TEXT (exact) and CUES (segment seconds, `audio/a3-s9.words.json`; host starts at 6.70, comp-local = t - 6.70)
Strings: `E` · `F` · `RUNNING OUT OF FUEL` · `ILLUSTRATION` · `Gov. Kathy Hochul, storm briefing, 26 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 6.70 | (before "He was stuck" @6.74) | ground on frame 0; dial, ticks, labels `fromTo(autoAlpha 0, scale 0.96 -> 1, 0.5, power3.out)` at 6.74; needle set at -45°; source pill and ILLUSTRATION in |
| 6.96 | "stuck in a car" @6.96 | needle idles: ±1.5° wobble around -45°, sine.inOut, 1.2 s period, finite repeats to 11.40 |
| 8.40 | "elderly mother," @8.00-8.40 | pump icon brightens 25 % -> 60 %, 0.4 s |
| 11.46 | "running out of fuel" @11.46-12.00 | needle `to(rotation:-80, 1.4, power2.inOut, svgOrigin 960 640)`; chip in at 11.64 `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; pump icon turns `#c0392b` and blinks 3 times (finite) |
| 12.94 | "State fire teams got them out." @12.94 | needle holds at -80° with ±0.8° wobble; chip label brightens to white |
| 14.70-15.30 | after "out." @14.04 | all out `to(autoAlpha 0, y:30, 0.6, power3.in)`; ground stays |
Comp duration 8.60 s.

## 6. CONTRACT
One file `compositions/g-a3-11-fuel-gauge.html`, root `id="g-a3-11-fuel-gauge-root"`, `data-composition-id="g-a3-11-fuel-gauge"`, PAUSED timeline `window.__timelines["g-a3-11-fuel-gauge"]`. Prefix `fg-`. Needle rotation set by `tl.set` at 0, no static SVG `transform=` on it. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-11-fuel-gauge`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-11-fuel-gauge`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: print the needle angle at 6.80, 11.40 and 13.50 from the page.

## 8. RECEIPT
As the template.
