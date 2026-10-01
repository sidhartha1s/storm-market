# g-oso-map · A2 US comparison (about 20.7 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (US state outline, pin with leader-free label, RHS rail),
retuned to Washington state; rail rows as in this episode's `g-map-kali-gandaki-a1.html`.

## 0. Claim
In March 2014, near Oso, Washington, a hillside of old glacial sediment collapsed after weeks of heavy rain; 43 people lost their
lives. Oso and the Kali Gandaki wall share the same recipe: loose glacial material, a steep slope, full of water.

## 1. Source
- factcheck-B row 9 (CONFIRMED): USGS "Ten years after the Oso landslide" and "Five Years Later": 43 fatalities; slope of
  "unconsolidated landslide deposits and unconsolidated glacial deposits"; "intense three-week rainfall immediately preceded the event".
- factcheck-B row 10 (CONFIRMED): same structure in both cases, loose glacial material on a steep slope saturated by weeks of rain.
- Date March 22, 2014: factcheck-B row 9 claim line ("Oso 2014, March 22, 43 lives") marked CONFIRMED.
- Oso 48.27222 N 121.91917 W, Seattle 47.60389 N 122.33 W (Wikipedia coordinates). Outlines: Natural Earth 10m admin 1.
- **Picture-line conflicts (reported):** the Picture line asks for a popfig over the map; `references/mg-quickref.md` says a popfig
  never sits over a map comp and the map rail carries the number, so "March 22, 2014" is the rail headline in Abril popfig red.
  The USGS photo is dropped per the orchestrator (no photo, no photo slot).

## 2. Datum, scale, orientation
North up. Equirectangular, statute miles, X = (lon + 120.5) * 69.093 * cos 47.3 deg, Y = -(lat - 47.3) * 69.093.
Camera: world (0, 0) at screen (640, 540), 2.6 px per mile (`translate(640,540) scale(2.6)`), fixed. Scale bar 130 px = 50 mi.

## 3. Geometry (screen px)
Oso pin (467.1, 365.3) · Seattle dot (417.1, 485.4). Labels: "Oso" (490, 352, 40 px) · "Old glacial sediment" (490, 390) ·
"Seattle" (430, 492) · "Washington" (700, 600, middle) · "Oregon" (640, 900, middle) · "British Columbia" (560, 190, middle).
Rain cloud ellipse centre (450, 330), rx 110, ry 44; label "3 weeks of heavy rain" (450, 272, middle).
Rail text at x 1270: eyebrow top 250, date top 290, count row top 440 (bottom about 590); after 15.0 the recipe block, eyebrow top 300,
rows top 350 / 410 / 470, note top 530. All rail text ends above y 680, so the presenter corner stays empty.

## 4. Must be true
1. The pin sits on Oso's real position (from coordinates), inland of Puget Sound and north-east of Seattle.
2. "March 22, 2014" lands on "In March twenty fourteen"; "43" and "Lives lost" land on "Forty three".
3. The recipe rows land one by one on "loose glacial", "steep slope", "full of water".
4. No photo and no photo slot. No popfig over the map.
5. Nothing in the presenter corner.

## 5. Text and cues (host starts at "We've watched" @est 0.0; 175 wpm)
Map, state label from 0.2 · CUE "In March twenty fourteen" @est 3.4 date · CUE "Oso, Washington" @est 5.1 pin + "Oso" + eyebrow ·
CUE "glacial sediment" @est 7.2 "Old glacial sediment" · CUE "collapsed" @est 7.9 burst ring, "Hillside collapse" ·
CUE "weeks of heavy rain" @est 8.6 rain cloud + label · CUE "Forty three" @est 9.9 counter 0 to 43 + "Lives lost" ·
date and count slide out 15.0 · CUE "same recipe" @est 15.4 "Same recipe" · CUE "loose glacial" @est 16.1 row 1 ·
CUE "steep slope" @est 17.8 row 2 · CUE "full of water" @est 18.5 row 3 · rail exits 20.1 · duration 20.7 s.
Tiers: 96 counter, 64 Abril date · 40 "Oso", "Washington"; 30 recipe rows · 22 labels, eyebrows · 19 notes, credit.
