# g-a2-5-two-offices · A2-S4 (whole) · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (the shared map, pins, wires, chips). Exemplars: `compositions/g-intro-4-wire-map.html` (plate, camera, wires, HUD discipline), `compositions/g-intro-8-track.html` (a copy of that base), official `us-map-flow` (an arc that draws from origin to destination). This comp is the BASE of the a2 map family (g-a2-7 and g-a2-8 copy its extended plate, pins and wire layer): send it alone for a full-size read first.

## 0. Claim
After the 1898 war the Weather Bureau moved its hurricane warning center from Jamaica to Havana. Its office there (Stockman) kept the islands and ships informed. Havana now had two weather offices, and only the Bureau's answered to Washington; the Washington line was the one Galveston listened to.

## 1. Source
- Move Jamaica to Cuba after the war: sources-cuba.md §2 (AOML "the United States Weather Bureau (USWB) moved its hurricane warning center from Jamaica to Cuba"); factcheck/a2-r1.md rows 17 (date the war, NOT the move), 18 (MWR heads the district "HAVANA, CUBA, FORECAST DISTRICT"), 22.
- Stockman: row 19 (MWR "W. B. Stockman, Forecast Official").
- Islands and ships: sources-cuba.md §2 (MWR Sep 1900 "Stations in Cuba, Jamaica, Haiti, Turks Island, Santo Domingo, and Porto Rico and shipping interests were fully informed"); row 20. The picture draws the four the Picture line names plus a ships glyph; Turks Island is left out (Picture line), not denied.
- Two offices, one answering to Washington: row 21. Washington to Galveston: sources-cuba.md §3 (MWR "Warning messages were received from the Central Office at Washington").

## 2. Datum, scale, orientation
- Plate and formula: `_list.md` "The shared map". EXTEND the drawn basemap box east and south: lon -110 to -50, lat 5 to 46 (X -900 to 4500, Y -520 to 3742). g-intro-4's box stops at lon -62 and V-ALL's right edge reaches plate X 4046, V-CARIB's 3576: without the extension the land polygon's edge shows. Same Natural Earth source and one-shot transform as g-intro-4's header; name the files in the receipt.
- Camera states (screen points computed by script 28 Oct 26):
  - V-CARIB: cx 2376, cy 2204.5, s 0.8. Havana (328, 262); Kingston (730, 690); Port-au-Prince (1051, 644); Santo Domingo (1224, 650); San Juan (1499, 650); Ships (1219, 232).
  - V-ALL: cx 1760, cy 1305, s 0.42. Galveston (417, 503); Washington (1089, 84); Havana (887, 772); Kingston (1098, 996); Port-au-Prince (1266, 972); Santo Domingo (1357, 976); San Juan (1502, 976); Ships (1355, 756).
  - V-CARIB to V-ALL is a 1.9x pull-out: `logZoom`.

## 3. Geometry
- Pins (Shared rules colours): Havana `#d8a13a` with a `#7fb2e5` outer ring once the Bureau is named (both offices share one map point); Jamaica, Haiti, Santo Domingo, Puerto Rico 10 px `#93a3b2`; Washington `#7fb2e5`; Galveston starts `#93a3b2` 10 px (unlit) and lights to `#f2f5f8` 14 px.
- Warning-center arrow (plate units, camera layer): quadratic from Kingston (2088.9, 2391.9) to Havana (1585.8, 1857.6), control (1990, 1990), `#7fb2e5` 7 px, round cap, 32 px arrowhead at Havana, drawn by strokeDashoffset from ceil(len)+1.
- Island lines (plate units): straight from Havana (1585.8, 1857.6) to Kingston, Port-au-Prince, Santo Domingo, San Juan and Ships, `#7fb2e5` 3 px, opacity 0.85.
- Ships glyph: a 34 px side-view steamer silhouette `#93a3b2` at the Ships point, bobbing y +-3 px.
- Wires (V-ALL): Havana to Washington and Washington to Galveston, lit wire style (Shared rules). A pulse (40 px `#f2f5f8` dash) runs Washington to Galveston on its cue.
- HUD labels in V-CARIB (Arial 700, stroke as Shared rules): "Havana" 30 px `#e8c56a`, left x 352, baseline 270; "Jamaica" 24 px `#93a3b2`, centred x 730, baseline 730; "Haiti" 24 px, centred 1051, baseline 620; "Santo Domingo" 24 px, centred 1224, baseline 692; "Puerto Rico" 24 px, centred 1499, baseline 626; "Ships" 24 px, left x 1248, baseline 240.
- Inset card "two offices, one city" (HUD, glass surface radius 20): x 120 to 560, y 400 to 640, with a 2 px `#c8d3e0` leader from the Havana pin (328, 262) to the card's top edge at (340, 400). Inside: eyebrow "Havana" (Arial 700 22 px `#93a3b2` tracking 6) at top 418; row 1 at y 480: 18 px pin `#7fb2e5` at x 160, name "US Weather Bureau" (Arial 700 30 px `#7fb2e5`) left x 190, sub "Stockman" (Arial 700 22 px `#93a3b2`) under it; row 2 at y 580: 18 px pin `#d8a13a` at x 160, name "Belen" (Arial 700 30 px `#e8c56a`) left x 190. No street, coast or block shapes inside the card (positions in the city are not sourced: `_list.md` change 3).
- HUD labels in V-ALL: "Washington" 30 px `#7fb2e5`, left x 1112, baseline 96; "Galveston" Arial Black 900 40 px, right edge 395, baseline 515; "Havana" 26 px `#e8c56a`, right edge 865, baseline 782.
- Chip 1 "1898: SPANISH-AMERICAN WAR" and chip 2 "WARNING CENTER: JAMAICA → HAVANA" (tag line "US Weather Bureau"): centred x 960, top 120 (below the source line, above every pin in V-CARIB).
- Source line (top-left): "NOAA AOML, 2015 · Monthly Weather Review, September 1900".

## 4. Must be true in the picture
1. Every pin on its formula point within 10 px in both camera states (receipt lists them with one frame each).
2. The year 1898 is never on screen with the warning-center arrow: chip 1 is gone before chip 2 and the arrow appear (row 17: the war is dated, the move is not).
3. The arrow runs from Jamaica to Havana (head at Havana), never the other way.
4. The inset shows two separate pins in one card, Bureau and Belen, with no street map; the Bureau pin is blue (Washington's colour), Belen's is amber.
5. All lines are straight city-to-city lines (the arrow is the only curve); no relay towns, no routes.
6. In V-ALL the only line into Galveston is from Washington; there is no line from Havana or Belen to Galveston in this comp.
7. Nothing enters x >= 1600, y >= 680 in either state (San Juan is at x 1499 to 1502; its label stays left of x 1580).
8. Labels never ride the pull-out: every V-CARIB label and the inset are at opacity 0 before the camera moves at 19.30; V-ALL labels enter after it settles at 20.40.

## 5. Text and cues (a2-s4.words.json)
- 0.00: plate in V-CARIB, Havana and Jamaica pins pulsing, their labels on. Source line in. Camera drifts s 0.80 to 0.82 over 0 to 8.8 (ease none).
- 1.28 ("War" 1.28) /* WAR @1.28 */: chip 1 enters; it lands as "1898." is said at 2.20.
- 5.52 ("Cuba," 5.52): chip 1 exits 5.52 to 5.92.
- 7.72 ("Hurricane" 7.72) /* WARNING CENTER @7.72 */: chip 2 enters.
- 8.86 ("from" 8.86): arrow draws Jamaica to Havana 8.86 to 9.80, power2.inOut; arrowhead lands on "Havana." 9.80; the Havana pin gains its blue outer ring at 9.80.
- 10.24 to 10.64: chip 2 exits.
- 10.64 ("Its" 10.64): arrow dims to opacity 0.4; inset card and leader enter (autoAlpha 0 to 1, scale 0.94 to 1, 0.45 s, back.out(1.4)) with only the eyebrow shown.
- 12.38 ("Stockman," 12.38) /* STOCKMAN @12.38 */: inset row 1 (Bureau pin, "US Weather Bureau", "Stockman") in.
- 14.26 ("islands" 14.26) /* ISLANDS @14.26 */: island lines draw from Havana to Jamaica, Haiti, Santo Domingo, Puerto Rico, 0.15 s apart (each 0.5 s); each island label in as its line lands.
- 15.00 ("ships" 15.00): ships line draws, glyph and "Ships" label in.
- 17.40 ("two" 17.40) /* TWO OFFICES @17.40 */: inset row 2 (Belen pin, "Belen") in.
- 18.86 ("only" 18.86): Bureau pin in the inset flashes (scale 1 to 1.5 to 1, 0.5 s); then every V-CARIB label, the inset and the leader fade to 0, 18.96 to 19.30.
- 19.30 to 20.40: camera pulls V-CARIB to V-ALL with logZoom.
- 20.12 ("Washington." 20.12) /* WASHINGTON @20.12 */: Washington pin drops in at its moving point; Havana to Washington wire draws 20.12 to 20.80; Galveston pin (unlit) fades in at 20.40; V-ALL labels in at 20.40.
- 21.38 ("Washington" 21.38) /* WASHINGTON LINE @21.38 */: Washington to Galveston wire draws 21.38 to 22.20.
- 22.90 ("Galveston" 22.90) /* GALVESTON @22.90 */: pulse runs Washington to Galveston 22.90 to 23.62; Galveston pin lights (colour to `#f2f5f8`, 10 to 14 px, flash 1 to 1.6 to 1, glow on).
- Host: A2-S4 0.00 to 24.092.

## Motion for the whole window
Pin pulses throughout; drift 0 to 8.8; ships bob from 15.00; longest gap between beats 0.00 to 1.28 and 2.20 to 5.52 (covered by drift and pulses).

## Exit
Cut to the A2-S5 desk: the whole root fades to 0 over the last 0.35 s (23.742 to 24.092), after the Galveston light lands.

## Footage under it
None: full-frame designed map (coverage 100 %).
