# g-map-kali-gandaki-a1b · A1 hydro pin + route beat (about 39 s, two paragraphs)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (pin + ring, route draw like its Fargo leader).
Spans the A1 hydro paragraph ("Downstream, the river feeds a dam...") and the route paragraph ("The same valley carries...").
If the editor keeps the Republic World shot over the hydro paragraph, mount this comp from local 17.5 s instead (the route
part stands alone). The g-hydro-card (another builder) owns the house grid; this map owns only the dam pin.

## 0. Claim
The Kali Gandaki feeds the 144 MW Kali Gandaki A plant downstream (it shut down); the same valley carries the road north to Mustang and
Muktinath, and the Annapurna trails run above it.

## 1. Source
- 144 MW installed (factcheck-A row 7); plant at Mirmi, Syangja district (factcheck-A row 14); plant stopped generating (factcheck-A row 6).
  Pin at the Wikipedia coordinate 27.9791 N 83.5805 E (MediaWiki API); it falls on the Natural Earth Gandak line within 1 px here.
- Road to Jomsom/Mustang and Muktinath, a Hindu and Buddhist pilgrimage site (factcheck-A row 17). Autumn trekking season on the
  Annapurna trails (factcheck-A row 18, factcheck-B row 1). The Annapurna Circuit runs Manang, Thorung La, Muktinath, Jomsom (factcheck-A row 17).
- Towns: Pokhara 28.2083 N 83.9889 E, Kushma 28.23 N 83.69 E, Baglung 28.2667 N 83.60 E, Beni 28.35 N 83.5667 E, Jomsom 28.7833 N
  83.7306 E, Muktinath 28.8171 N 83.8717 E (Wikipedia API). The route is drawn through these towns and 7 px east of the river between
  Beni and Jomsom: **route line approximate** (no road geometry used), labelled so.

## 2. Datum, scale, orientation
North up, same projection. Camera: world (-48, -15) at screen (620, 540), **10 px per mile** (`translate(1100,690) scale(10)`).
Right third (x >= 1280) kept empty for the hydro card. Drift 1.00 -> 1.04 about (620, 540).

## 3. Geometry (screen px at cam 1.00)
Dam pin (541.1, 842.6) · Pokhara (789.4, 684.2) · Kushma (607.7, 669.3) · Baglung (553, 643.9) · Beni (532.7, 586.4) · Jomsom (632.4, 287) ·
Muktinath (718.1, 263.6) · Dhaulagiri (489.4, 347.2) · Annapurna I (686.9, 416.3). Trekker walks the Jomsom-Muktinath leg of the route,
(629.4, 279.6) -> (718.1, 263.6).

## 4. Must be true
1. The dam pin sits on the river, downstream (south) of Beni and Baglung.
2. The route starts at Pokhara and ends at Muktinath, north of Jomsom; it never crosses to the west bank.
3. The trekker stays on the drawn route segment at start, middle and end of its walk.
4. No text or pin at x >= 1280; nothing in the presenter corner.

## 5. Text and cues (host starts at "Downstream" @est 0.0; route paragraph starts at local 17.5; 175 wpm)
CUE "a dam and power plant" @est 1.4 dam pin + "144 MW" + "Kali Gandaki A dam" · CUE "plant shut down" @est 15.1 pin greys, "Shut down" ·
route paragraph: dam labels dim 17.5 · CUE "north to Mustang" @est 19.9 route draws, "Pokhara", "Beni", "Jomsom", "Mustang" ·
CUE "a temple" @est 21.6 temple mark + "Muktinath temple" · CUE "Annapurna trails" @est 28.1 peaks, trekker walks, "Annapurna trails" ·
CUE "supposed to be ending" @est 36.7 (end of paragraph 38.1) · duration 39.3 s, ends on the drift.
Tiers: 52 "144 MW" · 40 "Mustang" · 26 "Muktinath temple", "Annapurna trails", "Shut down" · 22 towns and peaks · 19 note, credit.
