# g-map-kali-gandaki-a4 · A4 "settled" beat (about 13.5 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map-a4.html` (regional fills, halo labels), retuned to Nepal districts.

## 0. Claim
The collapse video was filmed near Lete in Mustang district; this week's lives were lost across districts of the province
(Manang, Myagdi, Baglung, Parbat, Palpa), which is a toll footprint, not a dispute about where the wall fell.

## 1. Source
- factcheck-C row 8: the five districts (plus Dhanusha) are where the week's combined flood/landslide toll was recorded (OnlineKhabar);
  the viral collapse is placed only near Lete, Mustang. Dhanusha (1 life, far east) is outside this map: the legend reads
  "Lives lost this week", not "all districts".
- Lete 28.62 N 83.60 E (factcheck-C row 14). Himlung 28.771948 N 84.422121 E (factcheck-C row 15), in Manang (factcheck-B row 12).
- District polygons: geoBoundaries gbOpen NPL ADM2 (public domain, 75 pre-2015 districts, simplified release). Nepal, border: Natural
  Earth 10m. River: OSM + Natural Earth (credit on screen).
- Picture-line note: Manang is NOT downstream of Lete (it drains to the Marsyangdi, east of the Annapurna massif). The districts are shown
  as a lit set, never as "downstream".

## 2. Datum, scale, orientation
North up, same projection. Camera: world (-45, -17) at screen (640, 540), **7 px per mile** (`translate(955,659) scale(7)`).
Drift 1.00 -> 1.03 about the Lete pin.

## 3. Geometry (screen px at cam 1.00)
Lete pin (572.1, 455.9); it sits on the simplified Mustang/Myagdi line (geoBoundaries simplified, about 1 mi off), so it straddles the edge.
Himlung mark (921.9, 382.4). District labels at shapely representative points: Mustang (685.6, 281.2), Manang (813, 365, moved up from
391.8 to clear the Lete label, still inside Manang), Myagdi (519.8, 470.5), Baglung (388.3, 566), Parbat (617.6, 639.2), Palpa (583.1, 837.9).
"Lete, Mustang" (598, 470) 52 px. Legend swatch (96, 904) + text (136, 922).

## 4. Must be true
1. Mustang is lit in amber (the video's district), the five toll districts in red; Mustang is not red.
2. Every district label sits inside its own polygon; none overlaps another label.
3. No arrow or wording implies the districts are downstream.
4. Nothing in the presenter corner.

## 5. Text and cues (host starts at "The video is from that day" = paragraph @est 7.5; local = paragraph - 7.5; 175 wpm)
map in 0.0-0.6 · CUE "Lete" @est 3.8 pin + "Lete, Mustang" · CUE "Mustang district" @est 4.5 Mustang fills amber + label ·
CUE "Himlung camp" @est 6.9 Himlung mark + label · CUE "lost their lives there" @est 10.0 five districts fill red, staggered 0.25 s,
labels + legend "Lives lost this week" · hold to 13.5 (the next paragraph opens on g-toll-counter). Duration 13.5 s.
Tiers: 52 "Lete, Mustang" · 26 district labels, legend · 22 "Himlung" · 19 credit.
