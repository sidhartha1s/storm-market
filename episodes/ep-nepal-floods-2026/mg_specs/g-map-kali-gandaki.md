# g-map-kali-gandaki · I beat, full map (about 20 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html`; basemap paths shared with `g-map-kali-gandaki-ht` (same 8 px/mi scale).

## 0. Claim
The Kali Gandaki runs south out of the high Himalaya through a gorge between Dhaulagiri and Annapurna I; a wall of that gorge gave way
(near Lete, Sept 27).

## 1. Source
- Gorge: river to Dhaulagiri summit relief 5,571 m = 18,278 ft (factcheck-A row 3). The depth figure lives in the other builder's inset
  (g-gorge-vs-grand-canyon); this map does not repeat it (one fact, one instance per frame).
- Collapse near Lete, Mustang, Sept 27 (factcheck-C rows 1, 2, 8). Lete 28.62 N 83.60 E (factcheck-C row 14); the pin sits on the river
  at the OSM river vertex nearest Lete, 28.6288 N 83.6188 E (1.3 mi from the rounded village coordinate).
- Peaks: Dhaulagiri 28.6961 N 83.4953 E, Annapurna I 28.5961 N 83.8203 E (Wikipedia coordinates via the MediaWiki API, 29 Sep 26).
- Basemap and river: as g-map-kali-gandaki-ht (Natural Earth 10m, OSM ways + Natural Earth Gandak; credit on screen).

## 2. Datum, scale, orientation
North up, same projection as the HT flash. Camera: world (-35, -20) at screen (640, 540), **8 px per mile** (`translate(920,700) scale(8)`).
The right third (x >= 1280) carries no labels or pins: the g-gorge-vs-grand-canyon inset lands there at "three times" (@est 10.3).
Outer cam push 1.00 -> 1.04 about the collapse pin.

## 3. Geometry (screen px at cam 1.00)
Collapse pin (491.5, 463) · Dhaulagiri triangle (431.5, 426) · Annapurna I triangle (589.5, 481) · gorge pinch arrows at x 470 and 513, y 463 ·
labels: title "Kali Gandaki River" (96, 118) · "Dhaulagiri" end (415, 432) · "Annapurna I" (606, 500) · "Kali Gandaki Gorge" end (455, 482) ·
"High Himalaya" (680, 460) · "Collapse · Sept 27" (512, 440).

## 4. Must be true
1. The river draws from its north end (upper Mustang) to its south end (Devghat): "runs south".
2. The gorge pinch sits between the two 8,000 m peaks, Dhaulagiri west of the river, Annapurna I east.
3. The collapse pin sits on the river line (within 6 px).
4. No text or pin at x >= 1280 (inset space); nothing in the presenter corner.

## 5. Text and cues (host starts at the I-beat paragraph "The Kali Gandaki runs south", @est 0.0; 175 wpm)
title 0.3 · CUE "runs south" @est 1.0 river draws south 1.0-3.4 · CUE "high Himalaya" @est 2.7 peaks + "High Himalaya" ·
CUE "deepest gorges" @est 4.8 gorge pinch + "Kali Gandaki Gorge" · CUE "summit beside it" @est 9.3 Dhaulagiri pulses ·
CUE "valley walls gave way" @est 17.5 collapse pin + "Collapse · Sept 27" · exit on CUE "Bridges went down" @est 18.9: title slides out,
map holds its push; duration 19.9 s. Tiers: 52 title · 26 "High Himalaya", collapse label · 22 peaks and gorge, 19 credit.
