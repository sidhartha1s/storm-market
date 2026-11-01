# g-a3-4-port-eads · A3-S4 0.00 to 8.06 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Plate and projection from `g-intro-4-wire-map` (`X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`, its Natural Earth land file).

## 0. Claim
The Cromwell Line steamer Louisiana left New Orleans on the morning of September 5; the warning flag was up at Port Eads as she ran out past the river's mouth.

## 1. Source
MWR Sept 1900 p. 374, Halsey's account (factcheck/a3-r1.md rows 13, 14): "We left New Orleans at 9:20 a.m. of September 5"; "passed the bar at 5:22 p. m. ... The warning flag was up at Port Eads as we ran out".

## 2. Datum, scale, orientation
- 0.00 to 3.84: no steamer photo exists (sourcer: none found). Use the MWR p. 374 scan `media/candidates/a3/A3-S4_c1_mwr-sept1900-p374_halsey-louisiana.png` as a page panel, whole lines, slow push toward Halsey's first lines. (Change from the Picture line: steamer photo replaced by the page.)
- 3.84 to 8.06: map, camera V-RIVER cx 935, cy 1195, s 3.2 (New Orleans to the Gulf mouth fills the frame). Pins by formula: New Orleans (-90.07, 29.95) = (893.7, 1148.6); Port Eads (-89.17, 29.02) = (974.7, 1245.3). Screen (checked 28 Oct 26): New Orleans (828, 392), Port Eads (1087, 701).
- River: Natural Earth 1:10m rivers (Mississippi) if fetched, stroke `#5a768f` 3 px; else no river line and the route is a straight dashed line labelled nothing.

## 3. Geometry
- Pins 14 px `#f2f5f8`; labels on the HUD: "New Orleans" Arial Black 900 34 px left of its pin; "PORT EADS" Arial 700 26 px `#e8c56a` tracking 3 left of its pin (keep x < 1600).
- Storm flag icon: a small mast 60 px with a red square flag `#c0392b` 34 x 34 px and a black square centre 12 px (the period storm-warning flag), raised up the mast at its cue, beside the Port Eads pin (left side).
- Ship: a small hull glyph 36 x 14 px `#f2f5f8` moving New Orleans to Port Eads along the river (or the straight line), past-track dashed `#f2f5f8` 3 px behind it.
- Source line top-left: "Captain Halsey, in Monthly Weather Review, September 1900, p. 374".

## 4. Must be true in the picture
1. Pins within 10 px of the formula.
2. The flag is up when the ship passes Port Eads (it is "already up"): raised before the ship arrives.
3. No time printed (the 9:20 a.m. and 5:22 p.m. are not spoken; the voice carries "morning of the 5th").
4. Nothing in x >= 1600, y >= 680. Port Eads sits at screen (1087, 701), left of x 1600: keep its label and flag left of the pin.

## 5. Text and cues (a3-s4.words.json, segment 14.20 s; this comp 0.00 to 8.06)
- 0.00: page panel, source line.
- 1.16 ("Louisiana") /* LOUISIANA @1.16 */: amber band (opacity 0.28) behind the line naming the Louisiana, drawn 1.16 to 1.80 (box measured on the scan).
- 3.84 ("The warning flag"): dissolve to map 0.4 s; ship already at New Orleans.
- 3.98 ("warning") /* FLAG @4.26 */: flag raises 3.98 to 4.56.
- 5.40 ("Port Eads") /* PORT EADS @5.40 */: Port Eads label in; ship runs 5.40 to 7.34 ("mouth") down to Port Eads and out past it.
- 8.06 ("Then"): handover to g-a3-5-barometer (cut).

## Motion for the whole window
Page push, then flag raise and ship movement; camera drift s 3.2 to 3.3.

## Exit
Hard cut at 8.06 to g-a3-5-barometer.

## Footage under it
The MWR p. 374 scan inside the comp for 0 to 3.84; then full-frame map.
