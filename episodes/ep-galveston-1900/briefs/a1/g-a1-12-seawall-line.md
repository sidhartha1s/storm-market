# g-a1-12-seawall-line · A1-S8 (whole) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/stat-timeline.html`, `library/inhouse/event-timeline.html` (axis, ticks, marker).

## 0. Claim
When Cline's article ran (1891) Galveston had no seawall, and still had none in 1900; the first section was not finished until 1904.

## 1. Source
- Galveston History Center (Rosenberg Library) seawall exhibit: "The initial segment of the Seawall was completed July 29, 1904"; legislature 1901, contract 1902 (factcheck/a1-r1.md row 38; factcheck/a1-r2.md row 28; factcheck-A.md H1-S3). https://www.galvestonhistorycenter.org/archive/exhibits/seawall/index.html
- Beach photo: `media/candidates/a1/provenance.csv` row `A1-S8_c1_beach-hotel-galveston.jpg` (public domain; date "188x", to confirm; no year on screen over it).

## 2. Datum, scale, orientation
Full-frame designed until 7.12, then the photo. Axis: y 600, x 200 (1891) to 1560 (1904), 104.615 px per year (computed): 1891 x 200.0, 1900 x 1141.5, 1904 x 1560.0. Time runs left to right.

## 3. Geometry (px)
- Axis line `#93a3b2` 3 px, y 600, x 200 to 1560, drawn left to right.
- Ticks 20 px tall at 1891, 1900, 1904; year labels Arial 700 30 px `#dfe7ee` centred under 1891 and 1900 at baseline 652. 1904 has no year label (the chip carries the year; one fact, one instance per frame).
- Page thumbnail at 1891: the staged full page `media/a1/gdn-1891-p5-full.jpg` at 120 x 153, centred x 200, bottom y 570 (top 417), 1 px `rgba(255,255,255,.3)` border, shadow `0 10px 24px rgba(0,0,0,.5)`.
- Bar: `#c0392b` 14 px tall, y 593 to 607, x 200 to 1141.5, `scaleX 0 → 1`, left origin. Label "NO SEAWALL" Arial Black 900 52 px `#f2f5f8` centred over the bar at x 670, baseline 540 (right of the thumbnail: thumbnail ends x 260).
- 1904 marker: vertical `#d8a13a` 3 px line at x 1560 from y 470 to 600; chip (glass, Arial Black 900 44 px) "FIRST SECTION FINISHED · 1904", right edge 1824, top 360 (about 960 x 96, x ≈ 864 to 1824, bottom 456).
- Source line top-left: "Galveston History Center, seawall exhibit"; from 7.12 swaps to "Beach Hotel, Galveston · Wikimedia Commons".
- Tiers: 52 / 44, 30 / 19.

## 4. Must be true in the picture
1. Tick positions match the computed px ±2: 1900 sits 941.5 px right of 1891; 1904 418.5 px right of 1900 (ratio 9 : 4).
2. The red bar ends exactly at the 1900 tick, never past it (no seawall in 1900; the four years after are not "no seawall" claims either way).
3. "1904" appears once on screen (in the chip).
4. No year label sits over the Beach Hotel photo (its date is unconfirmed).
5. Nothing in x >= 1600, y >= 680; the chip's lower edge (456) is above the corner.

## 5. Text and cues (a1-s8.words.json, segment 10.311 s)
- 0.00 ("When"): axis draws 0.00 to 0.60; source line in. /* AXIS @0.00 */
- 0.60 ("article"): page thumbnail drops in at 1891 (y −20 → 0, autoAlpha, 0.4 s back.out), "1891" label with it. /* 1891 @0.60 */
- 1.84 ("Galveston"): 1900 tick and label in.
- 2.34 ("no"): bar draws 2.34 to 3.20; "NO SEAWALL" in at 2.58 ("seawall."). /* NO SEAWALL @2.34 */
- 3.60 ("first"): 1904 marker line draws up. 5.62 ("1904."): chip in. /* 1904 @5.62 */
- 7.12 ("So"): the timeline fades out 7.12 to 8.12 (opacity, plus scale 1 → 0.98) while the photo (orchestrator, lower track from 7.12) shows through; source line swaps at 7.62. /* PHOTO @7.12 */
- Host: A1-S8 0.00 to 10.311; from 8.12 only the source line is this comp's (the photo carries the frame).

## Motion for the whole window
Draws every 1 to 2 s to 5.62; 5.62 to 7.12 chip and labels drift ±4 px; after 8.12 the source line drifts and the photo's slow push (orchestrator's mount) moves under it.

## Exit
Source line fades over the last 0.3 s; A1-S9 cuts to Paul full frame.

## Footage under it
None to 7.12; then `media/a1/beach-hotel-galveston.jpg` (staged from `A1-S8_c1_beach-hotel-galveston.jpg`, scaled to 1920 x 1244 and cropped to 1920 x 1080 keeping the hotel and the sand, slow push), mounted 7.12 to 10.311.
