# g-a1-2-jet-section · A1-S2 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-a1-1-afd-scroll.html` (copy its panel, scroll stack and highlight; this comp's frame 0 IS that comp's last frame) for the document layer, and `library/inhouse/radar-beam.html` (full-frame SVG physics cross-section: ground line, a band in the air, labels on the thing) for the cross-section layer. Two layers that hand over: document, then cross-section, then document again. Deep because the cross-section is a claim about the air and the hand-offs must keep the card state exact.

## 0. What this graphic claims
The 20 Dec discussion led with wind: an "extraordinary 70-75 kt low level jet" for Thursday night, a ribbon of fast air up above the ground (about 81 to 86 mph), and it called the damage producing winds a "very real threat" before it got to the snow.

## 1. SOURCE
- AFD FXUS61 KBUF 200951 (as g-a1-1). `research/nws.md` row 6.5 (jet and "damage producing winds" lead, snow after; PRIMARY) and row 3.7; `factcheck/a1-r1.md` rows 7, 10, 11, 12; `factcheck/a1-r2.md` row 3 (the AFD gives NO jet height, so no height number or "few thousand feet" anywhere).
- Knots to mph: 70 kt x 1.15078 = 80.6, 75 kt = 86.3 (`factcheck/a1-r1.md` row 9; factor in `research/nws.md` fetch notes). Chip "~81 TO 86 MPH". Knots appear on the chip only.
- Rows B36 to B51 appended to the g-a1-1 stack (product line breaks, re-fetched from IEM 28 Oct 26):
```
B36
B37 In any case...a coupled jet found over the Lower Great lakes ahead
B38 of this powerful storm Thursday night will combine with divergent
B39 flow aloft to generate a half inch of rain over our region along
B40 with temperatures that will actually rise through the night after
B41 early evening mins. The concern Thursday night though will be the
B42 impacts of an extraordinary 70-75 kt low level jet within the warm
B43 advection. Normally these winds would be aloft abv a pronounced
B44 inversion...but in areas where the winds are perpendicular to sfc
B45 barriers (ie. ridges/plateaus)...downsloping can transport the winds
B46 to the sfc. This could be the case north-northeast of the Tug Hill
B47 plateau and to a lesser degree in this case the Chautauqua ridge.
B48 The strong southeasterly flow will also be funneled down the Black
B49 River valley...enhancing winds in that area as well. Headlines for
B50 these winds east of Lake Ontario will likely come as early as
B51 midday.
```
- The AFD's jet paragraph says the flow was "strong southeasterly", and the jet sat over the warm sector, NOT along the lake axis. The cross-section therefore carries no compass, no Buffalo marker and no direction claim (see section 4).

## 2. DATUM, SCALE, ORIENTATION
Document layer: identical to g-a1-1 section 2 and 3 (row Bn top = 376 + n*44 - offset). Cross-section: SCHEMATIC, NOT TO SCALE, vertical exaggeration unstated; ground datum line y 800; no left/right compass meaning (flow drawn left to right for reading only). Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
Document states (offset = scroll offset of `as-stack`):
- D0 (frame 0): offset 1100, rects on B29/B30, other rows at 0.35. Exactly g-a1-1's last frame.
- D1: offset 1628 (row B42 top = 376 + 1848 - 1628 = 596). Highlight rect on B42 chars 14 to 50, "extraordinary 70-75 kt low level jet" (x about 465 to 1070; measure the glyph boxes).
- D2: offset 264 (row B11 top = 376 + 484 - 264 = 596). Highlight rect on B11 chars 10 to 53, "very real threat for damage producing winds". Grey underline 2 px `#93a3b2` under B13 chars 0 to 28, "heavy lake effect snow event" (y = row top + 36).
Cross-section (SVG, layer `js-xs`):
- Land left: rect x 200 to 420, y 800 to 860, fill `#2a3644`. Land right: x 1280 to 1500, same. Lake: x 420 to 1280, y 796 to 860, fill `#5a768f`, top edge a wave path drifting x 0 -> -40 continuously.
- Label "LAKE ERIE": Arial 700 22 px `#93a3b2` letter-spacing 3, centred x 850, top 818 (on the water).
- Jet ribbon: band x 200 to 1500, y 330 to 410, fill `linear-gradient(90deg, #c0392b, #e74c3c)` at 0.9; 12 streaks (2 px `#f2f5f8` at 0.6, 60 to 140 px long) inside the band moving x +480 px/s, wrapping (finite repeats to the comp end).
- Label "LOW LEVEL JET": Arial 700 22 px `#f2f5f8` letter-spacing 3, left 220, top 292 (just above the band, on the dark ground).
- Height bracket: vertical line x 1380 from y 414 to y 792, 2 px `#93a3b2`, arrowheads both ends, drawn with strokeDashoffset (dash = ceil(len)+1). No number, no label.
- Street-level wind: 5 arrows, 60 px long, 2 px `#93a3b2`, y 772, x 480, 640, 800, 960, 1120, drifting x +60 px/s (slow next to the ribbon).
- "SCHEMATIC, NOT TO SCALE": Arial 400 19 px `#93a3b2`, left 220, top 880.
Chips (top-left slot, one at a time): "70 TO 75 KNOTS" then "~81 TO 86 MPH", Arial Black `font-weight:900` 52 px `#e8c56a`, left 200, top 110. The chip row y 110 to 166 sits above the panel (y 200) and above the ribbon label (y 292).
Source line: "NWS Buffalo Area Forecast Discussion, FXUS61 KBUF 200951, IEM archive", Arial 19 `#c8d3e0`, left 96, bottom 54, on all comp long (carried over from g-a1-1, same product).
Type tiers: 52, 22 to 28, 19.

## 4. MUST BE TRUE IN THE PICTURE
1. Frame 0 matches g-a1-1's last frame pixel for pixel (offset 1100, B29/B30 highlighted, chip "TUE DEC 20 · 4:51 AM" present). That chip leaves at 0.3 to 0.8 (slide out left) before the knots chip enters.
2. Card rows are the product text character for character; no row cut at the window or panel edge, through both scrolls.
3. The ribbon sits clearly above the ground with a dark gap between them (gap >= 300 px): the jet is "up above the ground". No height number, no "feet", no altitude axis anywhere.
4. Nothing says which way the jet blows relative to the lake: no compass, no N/SW/NE, no Buffalo or Ohio marker on the cross-section.
5. Knots appear only on the "70 TO 75 KNOTS" chip; mph only on "~81 TO 86 MPH". Gusts 65 to 70 (spoken) get no number on screen.
6. Street-level arrows are visibly slower and shorter than the ribbon streaks (speed ratio about 1:8).
7. Highlight order follows the voice: jet line first, then "very real threat for damage producing winds", then the grey snow underline last.
8. Corner x >= 1600, y >= 680 empty. All text >= 96 px from left/right edges, >= 54 px from top/bottom.

## 5. TEXT (exact) and CUES (seconds from A1-S2 start, `audio/a1-s2.words.json`)
Strings: rows B0 to B51 · `70 TO 75 KNOTS` · `~81 TO 86 MPH` · `LOW LEVEL JET` · `LAKE ERIE` · `SCHEMATIC, NOT TO SCALE` · source line.
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "The same note" @0.00 | frame 0 = D0 |
| 0.30 | | date chip `to(x:-40, autoAlpha 0, 0.5, power3.in)` 0.30 to 0.80 |
| 0.40 | "note started with the wind" @0.34 to 1.20 | B29/B30 rects `to(autoAlpha 0, 0.5)`; all rows `to(opacity 1, 0.5)` |
| 1.90 to 2.70 | "It forecast an" @2.02 to 2.38 | stack scroll offset 1100 -> 1628, `power2.inOut` |
| 2.68 to 4.04 | "extraordinary low-level jet" @2.68 to 4.04 | B42 rect `scaleX 0 -> 1`, ease none; other rows `to(opacity 0.35, 0.4)` at 4.04 |
| 4.04 | "jet" @4.04 | chip "70 TO 75 KNOTS" `fromTo(autoAlpha 0, scale 1.2 -> 1, 0.4, power4.out, transformOrigin left center)` |
| 5.30 to 5.90 | "night." @5.00 | panel `to(x:-1500, autoAlpha 0, 0.6, power3.in)` (state D1 kept inside it) |
| 5.74 | "That is a" @5.74 | ground line, land and lake `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.5, power3.out)`; wave drift starts |
| 6.24 | "ribbon" @6.24 | ribbon `fromTo(scaleX 0 -> 1, 0.8, power3.out, transformOrigin left center)`; streaks start |
| 6.90 | "air" @6.90 | "LOW LEVEL JET" `fromTo(autoAlpha 0, y:16 -> 0, 0.4)` |
| 7.16 to 7.78 | "up above the ground" @7.16 to 7.78 | height bracket draws (strokeDashoffset), 0.62 s |
| 8.20 | gap after "ground," @7.78 | "LAKE ERIE" and "SCHEMATIC, NOT TO SCALE" in (autoAlpha, y 12 -> 0, 0.4) |
| 8.60 | | knots chip `to(x:-40, autoAlpha 0, 0.35, power3.in)` |
| 8.98 | "81" @8.98 | chip "~81 TO 86 MPH" in as the knots chip did |
| 11.68 | "Down at street level" @11.68 to 12.32 | street arrows `fromTo(autoAlpha 0, x:-30 -> 0, 0.4)` staggered 0.12, then drift |
| 13.20 to 15.66 | "the warnings would later put gusts at 65 to 70" | ribbon streak speed holds; street arrows pulse `scaleX 1 -> 1.15 -> 1` at 14.82 and 15.66 |
| 15.70 to 16.30 | "70." @15.66 | cross-section and mph chip `to(autoAlpha 0, y:30, 0.6, power3.in)`; behind it the stack jumps to offset 264 while hidden (set at 16.00), B42 rect hidden |
| 16.00 to 16.60 | "The note" @16.38 | panel back `fromTo(x:-1500 -> 0, autoAlpha 0 -> 1, 0.6, power3.out)`, rows at full opacity |
| 17.10 to 19.44 | "damage-producing winds a very real threat," @17.10 to 19.44 | B11 rect `scaleX 0 -> 1`, ease none; other rows `to(opacity 0.35, 0.4)` at 19.44 except B13 |
| 20.56 to 21.02 | "snow came second." @20.56 to 21.02 | B13 grey underline `scaleX 0 -> 1, 0.5`; B13 opacity 0.7 |
| 21.32 to 22.5 | tail | panel float `y 0 -> -4`, sine; exit at 21.9 to 22.5: panel `to(y:-30, autoAlpha 0, 0.6, power3.in)`, source line with it |
Comp duration 22.5 s. Spoken time in a comment at each tween. The section's "8.20" row is not on a word: it fills the gap between "ground" and "81" so the frame reads before the number lands.

## 6. CONTRACT
One file `compositions/g-a1-2-jet-section.html`, root `<div id="g-a1-2-jet-section-root" data-composition-id="g-a1-2-jet-section" ...>`, PAUSED timeline at `window.__timelines["g-a1-2-jet-section"]`. Ids and classes prefixed `js-` (rename every `as-` copied from g-a1-1: ids must be unique across the episode). Streaks and wave are finite repeats sized to the comp, never `repeat:-1`. Everything else: `references/mg-quickref.md`.

## 7. TOOLS / 7a. DONE LINE / 8. RECEIPT
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a1-2-jet-section`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a1-2-jet-section`. All seven items of template 7a; item 3: frame 0 equals g-a1-1's last frame (submit both for a side-by-side read). Receipt as the template.
