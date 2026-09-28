# g-bay-of-bengal-track · A2 storm origin (about 20.1 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (dark land, labels with halo, RHS rail), retuned; the
moving low-pressure symbol and rain shield are new (no library comp carries a storm symbol).

## 0. Claim
The storm began as a low pressure system over the Bay of Bengal and moved north over India. Indian TV called it Cyclone Arnab,
but it never became an official cyclone. It lost its winds before the mountains and still carried ocean moisture into Nepal.

## 1. Source
- factcheck-B row 3 (CONFIRMED): Al Jazeera, 27 Sep 2026, "a depression over the Bay of Bengal moved inland and intensified rainfall
  across the region".
- factcheck-B row 4 (CORRECTED, partial): "Arnab" is on the WMO/ESCAP list; IMD tracked the system but it "never strengthened past
  'deep depression'", so "Cyclone Arnab" was never official; News18 Bihar Jharkhand used the name on air (The Week, 22 Sep 2026).
- factcheck-B row 5 (CONFIRMED): IMD 25 Sep bulletin, the system weakened from deep depression to depression over south interior
  Odisha/Chhattisgarh before pushing rain into Nepal.
- Geography: Natural Earth 10m admin 0 (land union, Nepal outline).
- **No real track points exist in the fact files.** The track is SCHEMATIC through the regions the bulletins name (Bay, Odisha
  coast, interior Odisha/Chhattisgarh, Bihar at the Nepal border) and is labelled so on screen.
- **Flag:** the script says the Bay of Bengal is "south of India". It lies east of peninsular India and south of Bangladesh and
  eastern India; the map simply shows where it is.

## 2. Datum, scale, orientation
North up. Equirectangular, statute miles, X = (lon - 86) * 69.093 * cos 20 deg, Y = -(lat - 20) * 69.093.
Camera: world (0, -69) at screen (700, 520), 0.7 px per mile (`translate(700,568.3) scale(0.7)`), fixed. The land is to scale; the
track is not measured.

## 3. Geometry (screen px)
Track points: P0 (790.9, 689.2) Bay, 17.5 N 88.0 E · P1 (668.2, 602.2) Odisha coast · P2 (581.8, 549.0) interior Odisha ·
P3 (590.9, 399.0) Chhattisgarh/Jharkhand · P4 (622.7, 268.4) Bihar, just south of the Nepal border. Track length 536.6 px.
Kathmandu (669.1, 195.4). Rain shield ellipse centre (632, 215), rx 170, ry 62, straddling the border.
Labels: "Bay of Bengal" (836, 786, middle) · "India" (382, 447) · "Nepal" (573, 140) · "Bangladesh" (895, 375) · "Kathmandu" (684, 201).
Rail (right, gradient 820 px), text at x 1270: eyebrow top 300, row 1 top 346, row 2 top 470, row 3 top 580 (bottom about 650, clear
of the presenter corner). Note "Track schematic" (96, 966); credit (96, bottom 54).

## 4. Must be true
1. The symbol starts over open water in the Bay, crosses the coast, and ends in India south of the Nepal border (P4 is in Bihar).
2. The track is labelled "Track schematic" for its whole life on screen.
3. "Cyclone Arnab" is shown as a name in quotes and is struck through with "Never official" on "never became"; the rail never calls
   it a cyclone without that qualifier.
4. At "lost its winds" the spiral arms stop and fade; at "moisture" the rain shield spreads across the Nepal border.
5. Nothing in the presenter corner (x >= 1600, y >= 680).

## 5. Text and cues (host starts at "This storm began" @est 0.0; 175 wpm)
CUE "low pressure" @est 1.7 symbol forms at P0 + rail row 1 "Low pressure" · CUE "Bay of Bengal" @est 3.4 bay label ·
CUE "south of India" @est 4.5 India, Bangladesh labels · CUE "moved north" @est 5.8 symbol travels P0 to P4 at constant speed
(ends 12.8), track draws behind it, "Track schematic" note · CUE "Cyclone Arnab" @est 7.9 row 2 "“Cyclone Arnab”" ·
CUE "never became" @est 9.3 strike-through + "Never official · IMD peak: deep depression" · CUE "reached the mountains" @est 12.3
Nepal lights, Kathmandu · CUE "lost its winds" @est 14.1 arms fade, row 3 "Lost its winds" · CUE "moisture" @est 16.5 rain shield
spreads, "Still carried ocean moisture" · rail exits 19.5 · duration 20.1 s.
Tiers: 56 "Low pressure" · 40 "Bay of Bengal", "India", "Nepal"; 30 rows 2 and 3 · 22 small labels, eyebrow · 19 notes, credit.
