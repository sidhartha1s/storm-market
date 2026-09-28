# g-aug-vs-sep-a5 · A5 full map, to scale (about 10.8 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (Fargo leader line + label, glass cards), retuned.

## 0. Claim
The two disasters sit 32 days and about 120 mi apart (Langtang, Aug 26; Kali Gandaki, Sept 27); Himlung sits between them, about 75 mi
from Langtang.

## 1. Source
- factcheck-C row 14: Langtang Lirung 28.2575 N 85.51583 E to Lete 28.62 N 83.60 E = 191.6 km / 119.1 mi (haversine).
- factcheck-C row 15: Himlung 28.771948 N 84.422121 E; Langtang to Himlung 121.2 km / 75.3 mi.
- 32 days: python `date(2026,9,27) - date(2026,8,26)` = 32.
- Toll boxes: Langtang 1,451 lives lost, 5,745 missing as of Sept 21 (factcheck-A row 10); Kali Gandaki area, Nepal disaster agency
  Sept 27: 12 lives lost, 7 missing (factcheck-C row 4 and "Latest official toll"); Himlung: 16 at camp, 4 found, 12 missing by Sept 28
  (factcheck-D section 3).

## 2. Datum, scale, orientation (to scale)
North up. Equirectangular, statute miles, X = (lon - 84.5) * 69.093 * cos 28.4 deg, Y = -(lat - 28.2) * 69.093.
Camera: world (0, -20) at screen (820, 560), **7 px per mile** (`translate(820,700) scale(7)`). The camera does not move in this comp
(no drift), so the ratio holds on every frame. Scale bar 350 px = 50 mi.
Measured from the pasted endpoints (python): Langtang-Lete 833.7 px = 119.10 mi; Langtang-Himlung 527.7 px = 75.38 mi;
ratio 1.580 vs 119.1 / 75.3 = 1.5817 (-0.1 %; the equirectangular projection vs haversine).

## 3. Geometry (screen px)
Langtang pin (1252.2, 672.2) amber (August) · Lete pin (437.1, 496.9) red · Himlung pin (786.9, 423.4) red.
Line L-T from Langtang to Lete; label "About 120 mi" centred (838, 628) below it. Line L-H from Langtang to Himlung; label "About 75 mi"
centred (1060, 500) above it. Title "32 Days Apart" (96, 62). Cards (glass): Kali Gandaki left 110 top 540 w 380; Himlung left 620
top 180 w 360; Langtang left 1030 top 712 w 450 (right edge 1480 < 1600: presenter corner clear).

## 4. Must be true
1. Line lengths: L-T 833.7 px, L-H 527.7 px (ratio 1.58, within 1 % of 119.1/75.3).
2. Each line ends exactly on its pin centres; the camera never scales.
3. August is amber, September red; each card carries its own date and its own toll with its "as of" date.
4. "32 Days Apart" lands on "thirty two days", "About 120 mi" on "a hundred and twenty miles", "About 75 mi" on "seventy five miles".
5. Nothing in the presenter corner.

## 5. Text and cues (host starts at "On one map" @est 0.0; 175 wpm)
Langtang pin + card 0.2 · Kali Gandaki pin + card 0.9 · CUE "thirty two days" @est 2.4 title · CUE "a hundred and twenty miles" @est 4.1
line L-T draws Langtang -> Lete (0.9 s), label 4.6, scale bar 4.3 · CUE "Himlung sits between" @est 6.2 Himlung pin + card ·
CUE "seventy five miles" @est 7.9 line L-H draws, label 8.3 · cards and title slide out 10.2 · duration 10.8 s (a5b continues on the
same camera). Tiers: 52 title · 30 card dates · 26 line labels, 22 card tolls · 19 eyebrows, "as of" lines, credit.
