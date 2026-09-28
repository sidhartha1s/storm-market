# g-map-kali-gandaki-ht · HT beat, quick map flash (about 10 s)

Library source: `episodes/ep-enderlin-2025/compositions/g-master-map.html` (cam group, scan line, halo labels, pin + ring), retuned.
`library/inhouse/examples/master-map-us-canada.html` named in the builder prompt does not exist on this branch or main (only `joplin-stat-panel.html`).

## 0. Claim
The Kali Gandaki runs north up to the Tibet border, and Himlung Himal sits on that border, east of the river.

## 1. Source
- Himlung Himal 28.771948 N 84.422121 E (factcheck-C row 15). Himlung "near the Tibet/China border", Nar Phu valley, Manang (factcheck-B row 12).
- River course: OpenStreetMap ways "Kali Gandaki" 371902681 ... 26948475 (Lo Manthang area 29.155 N south to Beni 28.375 N), then Natural Earth 10m
  "Gandak" centerline south to the Trishuli confluence at Devghat (27.740 N 84.422 E). Nepal and the Nepal-China border: Natural Earth 10m admin-0
  (public domain). OSM is ODbL: credit "Map data: OpenStreetMap contributors, Natural Earth" on screen and in the description.
- The OSM main stem ends at 29.155 N, about 12 mi short of the border line; the river is drawn "toward" the border, not claimed to touch it.

## 2. Datum, scale, orientation
North up. Equirectangular, units = statute miles: X = (lon - 84.5) * 69.093 * cos 28.4 deg, Y = -(lat - 28.2) * 69.093.
Camera: world (-30, -20) at screen (960, 540), **8 px per mile** (inner group `translate(1200,700) scale(8)`). Outer cam pushes 1.00 -> 1.05 about the Himlung pin.

## 3. Geometry (screen px at cam 1.00)
Himlung pin (1162, 384). River top (936, 172), river end at Devghat (1162, 954). Lete (762, 468), for reference only.
Labels: "Nepal" (1150, 760) · "Kali Gandaki River" end-anchored (726, 560) · "Himlung Himal" start (1186, 462) · "Tibet" (1330, 240).

## 4. Must be true
1. The river is drawn from the south end northward and stops north of Jomsom, below the dashed border.
2. Himlung pin sits at the dashed Nepal-China border line (within 20 px = 2.5 mi; factcheck-B gives 1.5 km, Natural Earth 10m border
   accuracy is about 1 km), east of the river.
3. "Tibet" sits north of the dashed border, "Nepal" south of it.
4. Nothing in the presenter corner (x >= 1600 and y >= 680) except basemap fill.

## 5. Text and cues (host starts at CUE "The same storm" @est 4.1 s into the HT paragraph; local seconds below)
Map in 0.0-0.5 · river draws north 0.2-2.6 · "Kali Gandaki River" 1.2 · "Nepal" 0.6 ·
CUE "Himlung Himal" @est 3.4 pin + ring + label · CUE "Tibet" @est 5.5 border brightens + "Tibet" ·
cut at CUE "base camp" @est 10.0 (WION avalanche clip). Duration 10.0 s. Ends on the camera push (cut).
