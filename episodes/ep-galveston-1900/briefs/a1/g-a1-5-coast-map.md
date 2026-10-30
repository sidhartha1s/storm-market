# g-a1-5-coast-map · A1-S3 5.46 to A1-S4 1.64 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `compositions/g-intro-4-wire-map.html` (plate, projection, basemap, pins, HUD labels): copy the plate, do not edit it. `briefs/a2/_list.md` "The shared map" has the same pin and label spec.

## 0. Claim
Down the same coast from Galveston, the port of Indianola on Matagorda Bay was wrecked by a hurricane in 1875 (only 8 buildings left undamaged), wrecked again in 1886, and never rebuilt.

## 1. Source
- TSHA Indianola Hurricanes: began 15 Sept 1875; "only eight buildings were left undamaged"; "completely destroyed by a second hurricane that blew in on August 19, 1886" (factcheck/a1-r1.md row 13; factcheck/a1-r2.md rows 7, 8). https://www.tshaonline.org/handbook/entries/indianola-hurricanes
- TSHA Indianola TX: "By 1887 the site had been abandoned" (factcheck/a1-r2.md row 9). https://www.tshaonline.org/handbook/entries/indianola-tx
- Positions: Galveston from the shared plate (`briefs/a2/_list.md`). Indianola site lon −96.51, lat 28.53 and the Matagorda Bay label anchor lon −96.30, lat 28.42 are NOT from a research row: check both against the basemap (the pin must sit on the bay's west shore, the label over bay water) and state the values used in the receipt.

## 2. Datum, scale, orientation
- Projection exactly g-intro-4: `X = (lon + 100) * 90`, `Y = (41 − lat) * 103.95`, north up, Natural Earth 10m land `#15202b`, coast `#5a768f` 2 px. At s 3 the 0.025° simplification may lose Matagorda Bay's outline: use the unsimplified 10m coast for this window's box (lon −97.5 to −94.0, lat 27.8 to 30.0); if the bay still does not resolve, add "Schematic" to the source line.
- Plate points (computed): Galveston (468.0, 1216.2); Indianola (314.1, 1296.3); Matagorda Bay label (333.0, 1307.7).
- Camera `screen = (960 + (X − cx)·s, 540 + (Y − cy)·s)`, pure function of comp time:
  - C0 (frame 0 to 0.36): s 3.0, c (468.0, 1216.2): Galveston at (960, 540).
  - C1 (0.36 to 1.80, "coast," to settle): to c (391.0, 1256.2), s 3.0, power2.inOut. Then Galveston (1190.9, 419.9), Indianola (729.1, 660.1), bay label (785.9, 694.4).
  - C1 holds with drift s 3.0 to 3.12 (`ease:none`) to the host end.

## 3. Geometry (px, screen at C1)
- Pins: 14 px dot with a 2 px ring pulse (scale 1 → 2.2, opacity 0.8 → 0, 1.4 s, finite repeats). Galveston `#f2f5f8`; Indianola `#d8a13a` while it stands, then hollow (ring only, stroke `#93a3b2` 2 px, fill none) after "rebuilt".
- Labels (HUD layer, Arial 700, paint-order stroke `#04070c` 5 px): "Galveston" 30 px `#f2f5f8` left edge x 1215, baseline y 412; "Indianola" 30 px `#f2f5f8` right edge x 705, baseline y 652; "Matagorda Bay" 22 px `#93a3b2` tracking 3, italic none, centred (786, 700) over water. Labels enter only once the camera has settled.
- Chip (glass, Shared rules), `left:400px; top:760px`: main line Arial Black 900 44 px, pre-authored as two spans "1875" and " · 8 BUILDINGS UNDAMAGED"; about 870 x 96; right edge ≤ 1300.
- Source line top-left: "Texas State Historical Association · basemap: Natural Earth".
- Tiers: 44 / 30 / 22, 19. Add the big tier by setting the chip's "1875" span at 56 px (the beat's number), the rest of the chip line 44 px.

## 4. Must be true in the picture
1. Indianola is down the coast to the southwest of Galveston (screen: left and lower), on Matagorda Bay's shore; the bay label sits on water.
2. The chip's first span shows only after "1875" is spoken and the second only after "eight" (counts on screen in numerals: 8).
3. "1886" never appears on this map: it belongs to the photo window (g-a1-6).
4. After "rebuilt" the Indianola pin is hollow and its label greys to `#93a3b2`; no strike-through and no "abandoned" text (the narration carries it).
5. No wire, track or storm path is drawn: this map makes no claim about where either storm went.
6. Nothing in x >= 1600, y >= 680 (Gulf water only there).

## 5. Text and cues (a1-s3 then a1-s4 words.json; comp-local = S3 time − 5.46 inside S3)
- S3 5.46 ("Down"): map on at C0, Galveston pin and label already shown (it is where we were). /* COAST @5.46 */
- S3 5.82 ("coast,"): camera move C1 starts.
- S3 8.06 ("Indianola"): Indianola pin drops in (y −20 → 0, autoAlpha, 0.4 s back.out), label in 0.2 s later. /* INDIANOLA @8.06 */
- S3 8.82 ("1875."): chip in with span "1875". /* 1875 @8.82 */
- S3 10.62 ("eight"): span " · 8 BUILDINGS UNDAMAGED" in (autoAlpha, x −8 → 0, 0.3 s). /* EIGHT @10.62 */
- S3 12.60 to 13.00: chip out (map exit `y:-24`).
- S3 13.18 to 16.46: the 1886 photo covers this comp (orchestrator, upper track). The map keeps running (pin pulse, drift) underneath; nothing new happens.
- S3 17.42 ("Matagorda"): "Matagorda Bay" label in. /* MATAGORDA @17.42 */
- S3 20.66 ("never"): Indianola pin goes hollow (fill opacity 1 → 0, 0.5 s), pulse stops after its current cycle; label colour to `#93a3b2` by 21.00 ("rebuilt."). /* NEVER REBUILT @20.66 */
- S4 0.00 to 1.64 ("sentence,"): hold the Indianola pin (the act: "hold the Indianola pin"); drift continues.
- Host: A1-S3 5.46 to A1-S4 1.64 (including the S3/S4 gap from the mounts).

## Motion for the whole window
Camera drift, pin pulses (finite repeats sized to the host), labels drift ±4 px. Galveston pin pulses all window.

## Exit
Cut to the 1891 column (g-a1-7) at S4 1.64: root fades to 0 over the last 0.3 s.

## Footage under it
None (full-frame map). Above it, 13.18 to 16.46: the staged Indianola 1886 photo with g-a1-6.
