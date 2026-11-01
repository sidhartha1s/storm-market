# g-a2-9-sept4-map · A2-S8 (whole) · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (chips, source line, pin look). Exemplars: official `north-korea-locked-down` (a real map with a pop-up label), arrows drawn as in `compositions/g-intro-4-wire-map.html` (strokeDashoffset, round cap, arrowhead). g-a2-10 redraws this comp's two arrows at panel scale: send this comp for a full-size read before g-a2-10 is built.

## 0. Claim
On the Weather Bureau's own map for 4 September 1900 the storm sits over western Cuba. Washington's note had it heading for the south Florida coast; Belen read it going northwest, into the Gulf; Rubiera writes that Gangoiti told the Americans it would strengthen there.

## 1. Source
- The map: `media/candidates/a2/provenance.csv` row A2-S8_c1 (NOAA synoptic weather map, 4 Sept 1900, low "1005" over western Cuba, PD-USGov-NOAA, verified "Y"; picks.md: the only usable day).
- Washington's note: sources-cuba.md §3 (Roker: "A tropical disturbance was moving over western Cuba and heading for the south Florida coast", dated Washington 4 Sept, signed Moore; SECONDARY); factcheck/a2-r1.md row 49.
- Belen: sources-cuba.md §1 (AOML "the storm moved to the northwest and into the Gulf of Mexico"); row 50. Conflict 3: only "into the Gulf" is supported; Texas or San Antonio is secondary only.
- Rubiera: sources-cuba.md §1 (OnCuba, "se fortalecería", "mucha fuerza en el Golfo de México", SECONDARY, attributed aloud); row 51 (chip a fair gloss, so no quote marks: `_list.md` change 7).

## 2. Datum, scale, orientation
- Ground: `media/a2/noaa-map-1900-09-04-gulf.jpg`, staged by the orchestrator from `media/candidates/a2/A2-S8_c1_noaa-weather-map-1900-09-04.jpg` (2048 x 1452): crop scan x 400 to 1520, y 570 to 1200 (1120 x 630), resized to 1920 x 1080 (factor 1.7143, lanczos). Screen point = ((scan x - 400) x 1.7143, (scan y - 570) x 1.7143).
- The scan's own projection (a 1900 polar map, lines curved) is the datum: every mark is placed on a feature printed on the scan, measured on the staged crop, never by lon/lat. Approximate screen points from my read of the full scan (the builder measures each on the crop and states the measured value in the receipt; a difference over 30 px from these means the crop is not the one specified):
  - The printed "L" low centre: about (1157, 814).
  - Galveston station circle on the Texas coast: about (271, 343).
  - South Florida tip (the station near the printed "Miami"): about (1263, 410).
  - New Orleans (printed "Orleans"): about (842, 235), for checking only, not labelled.
- Darken the scan for contrast: `.dim` layer rgba(3,5,8,0.45) over it (tokens.md "Scrim"), whole comp. No camera move (labels would ride it): the scan is still.

## 3. Geometry (screen px, measured on the crop)
- Galveston pin: 14 px `#f2f5f8` dot with ring pulse on the station circle; label "Galveston" Arial Black 900 34 px `#f2f5f8` on a glass pill (radius 12, padding 4px 12px), left x 300, baseline 352.
- Storm ring: a 2 px `#c0392b` circle, radius 70, centred on the printed "L"; it breathes (scale 1 to 1.08, 1.6 s yoyo, finite).
- Washington arrow: from the low centre toward the south Florida tip, ending 30 px short of it; `#7fb2e5` 6 px, dashed 18/12, round cap, 30 px arrowhead; drawn by strokeDashoffset on a solid mask path (the dash pattern stays fixed).
- Belen arrow: from the low centre to about (800, 500) in the open Gulf (the builder confirms the head is over water on the scan), gentle curve, quadratic control about (1020, 700); `#d8a13a` 8 px, solid, 34 px arrowhead.
- Chips (Shared rules chip, one at a time, centred x 960, top 120), each with a 6 px colour bar on its left edge inside the card:
  - A: "WASHINGTON, SEPT 4: SOUTH FLORIDA" (bar `#7fb2e5`).
  - B: "BELEN: NORTHWEST, INTO THE GULF" (bar `#d8a13a`).
  - C: "RUBIERA: STRENGTHEN IN THE GULF" (bar `#d8a13a`).
  If a chip's main line measures over 1100 px, drop it to 40 px (mid tier stays) rather than wrap.
- Source line (top-left, two lines): "NOAA weather map, Sept. 4, 1900 · NOAA AOML, 2015 · Al Roker, HistoryNet (secondary) · José Rubiera, OnCuba, 2015". The chip top (120) must clear its bottom; if the source wraps lower, chips move to top 150.

## 4. Must be true in the picture
1. Every mark sits on the printed feature it names (within 12 px on the crop): the ring on the printed L, the Galveston pin on the Galveston station, the Washington arrowhead at the south Florida tip.
2. The Belen arrow points northwest into the open Gulf: its head is over water at least 250 px from any coast, and its straight extension does not pass within 120 px of the Galveston pin (Conflict 3; `_list.md` change 6). It never touches or aims at Galveston.
3. Washington's arrow is dashed (a note, not a track) and Belen's is solid; they leave the same point (the low).
4. Chip C has no quote marks.
5. No printed station text under a chip or label is needed for the claim (chips sit over the US interior; check the frame read).
6. Nothing enters x >= 1600, y >= 680 (the presenter circle may be on: the corner holds only scan; no mark goes there).

## 5. Text and cues (a2-s8.words.json; Whisper writes Gangoiti "gangoide")
- 0.00: scan and dim on (frame 0 is the scan, no dark frame), Galveston pin and label on, source line in.
- 0.72 ("reached" 0.72) /* CUBA @1.08 */: storm ring draws around the L (strokeDashoffset 0.72 to 1.08, landing on "Cuba." 1.08).
- 3.56 ("4th," 3.56) /* SEPT 4 @3.56 */: chip A enters.
- 5.84 ("toward" 5.84) /* SOUTH FLORIDA @5.84 */: Washington arrow draws 5.84 to 6.92 ("coast." 6.92), power2.inOut.
- 7.40 to 7.88: chip A exits; the Washington arrow stays at opacity 0.7.
- 8.00 ("Belen," 8.00): the low ring flashes amber once (colour to `#d8a13a` and back, 0.5 s).
- 10.16 ("northwest," 10.16) /* NORTHWEST @10.16 */: Belen arrow draws 10.16 to 11.82 ("Mexico." 11.82), power2.inOut.
- 11.10 ("into" 11.10): chip B enters.
- 12.40 to 12.80: chip B exits.
- 13.24 ("writes" 13.24) /* RUBIERA @13.24 */: chip C enters.
- 15.86 ("stronger" 15.86): Belen arrow thickens 8 to 11 px and its head scales 1 to 1.2 (0.5 s, back.out), holding.
- 17.904: end.
- Host: A2-S8 0.00 to 17.904.

## Motion for the whole window
Ring breathing and pin pulse for the whole comp; arrow draws; chips. Longest gap between beats 1.08 to 3.56, covered by the ring and pulse.

## Exit
Cut to Paul's clip (A2-S9): the whole root, scan included, fades to 0 over the last 0.35 s (17.554 to 17.904).

## Footage under it
The NOAA 4 Sept 1900 map crop is mounted inside this comp as its ground (a still; claim risk none by provenance.csv). Nothing under it on a lower track.
