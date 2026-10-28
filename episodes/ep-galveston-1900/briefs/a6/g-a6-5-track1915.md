# g-a6-5-track1915 · A6-S4 0.00 to 7.06 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `g-intro-8-track` (plate, projection, Galveston pin, storm ring and past-track style); copy it only after it passed its frame read. Exemplar: `episodes/ep6-katrina-2005/compositions/g-track.html`.

## 0. Claim
In August 1915 another big hurricane came ashore about 30 miles southwest of Galveston.

## 1. Source
- NWS Houston/Galveston, Upper Texas Coast Tropical Cyclones in the 1910s (sources-a6.md §4): "made landfall 30 miles southwest of Galveston".
- Rosenberg Library: "the hurricane of August 16, 1915" (sources-a6.md §4).
- TRACK HAS NO RESEARCH ROW. Take the 1915 Galveston hurricane from NOAA HURDAT2 (confirm its id, expected AL031915 or nearby, by name/date: landfall 16 to 17 Aug 1915 on the upper Texas coast), list each lon/lat and plate px in the receipt, and check the landfall point is 30 mi (48 km) ±5 mi SW of the Galveston pin. If HURDAT2 is not fetched: a single schematic arrow from the SE Gulf to the landfall point, and the source line adds "Track: schematic".

## 2. Datum, scale, orientation
Plate and projection exactly as g-intro-4/g-intro-8: `X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`; Galveston (468.0, 1216.2). Camera: centred on Galveston, scale chosen so 30 miles reads: 30 mi SW of Galveston ≈ lon −95.15, lat 29.0 (compute from the pin with 1° lat = 69 mi, 1° lon = 60.4 mi at 29.3° N; state the point in the receipt). Use screen = 960 + (X − cx)·s, 540 + (Y − cy)·s with cx, cy = midpoint of Galveston and the landfall point, s chosen so the two points sit about 300 px apart on screen.

## 3. Geometry (px, screen)
- Galveston pin and label from the base ("Galveston").
- Track: past-track line `#f2f5f8` 5 px drawn by strokeDashoffset behind a storm ring (base's ring, 96 px), entering from the lower right (SE Gulf), ending ON the coast at the landfall point.
- Distance bracket: a 2 px `#d8a13a` line between the landfall point and the Galveston pin, end ticks 20 px, label "30 MILES" diagram tier Arial 700 28 px `#d8a13a`, placed on the inland side of the bracket midpoint, 24 px off the line.
- Rail chip (top-left of the map, glass): "AUGUST 1915", Arial Black 900 52 px, left edge x 120, top 150. (Change 4 in `_list.md`: popfigs never sit over a map comp.)
- Source line top-left: "National Weather Service Houston/Galveston · Rosenberg Library" (+ "Track: schematic" if no HURDAT2).

## 4. Must be true in the picture
1. Landfall point is southwest of the Galveston pin (down-left on a north-up map) and its distance by the projection is 30 ±5 mi.
2. The ring stops on the coast at the landfall point, never on Galveston.
3. No storm name, wind speed or category on screen (none spoken, none in the rows).
4. The ring and pin stay out of x >= 1600, y >= 680 or the circle goes off; state which in the receipt.

## 5. Text and cues (a6-s4.words.json, 19.403 s; host 0.00 to 7.06)
- 0.00: plate on, Galveston pin on; source line in at 0.20.
- 0.46 ("August") /* AUG 1915 @0.46 */: rail chip in (lands by 0.96 "1915,").
- 2.40 ("another") /* TRACK @2.40 */: ring enters from the SE and moves along the track, 2.40 to 3.90 (`power1.inOut`), the past-track line drawing behind it; ring reaches the coast at 3.70 ("ashore," 3.70).
- 4.62 ("about") /* 30 MILES @4.80 */: bracket draws from the landfall point to the pin 4.62 to 5.20; "30 MILES" label in at 5.20 ("miles").
- 5.56 ("southwest"): landfall point pulses once (ring scale 1 to 1.15 to 1).
- 6.46: chip and label out; root holds to 7.06 for the cut to g-a6-6.

## Motion for the whole window
Ring rotation (slow spin on its stroke dash, continuous) and the camera drifting 1.00 to 1.03 linear the whole host.

## Exit
Cut to g-a6-6 at "The" 7.06: root fades to 0 over the last 0.3 s.

## Footage under it
None: full-frame map.
