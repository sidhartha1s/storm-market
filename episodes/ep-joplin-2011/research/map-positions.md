# map-positions · Table 4-3 named buildings (Open 4) · 18 Oct 26

Projection = g-intro-map master P(): equirectangular, x scaled by cos(37.08°), s = 46.132 px/mi, TIGER 2010 "Joplin city" (GEOID 2937592) outline bbox centred on (850, 485); bbox centre lon0 = -94.511495, lat0 = 37.084029; M = 69.1674 mi/deg (= 570 px / (s × lat span 0.178637°)). x = 850 + (lon − lon0) · cos(37.08°) · M · s; y = 485 − (lat − lat0) · M · s.

Check of the rebuilt P(): the TIGERweb Census 2010 outline (tigerweb.geo.census.gov, tigerWMS_Census2010 layer 34) lands on the master's city path at a median of 0.37 px (max 1.89 px, 564 vertices). The master's Somerset address point (2001 Connecticut Ave) comes back 0.41 px from its value.

Worked example (Pizza Hut, 37.070143, -94.477776): x = 850 + 0.033719 × 0.797619 × 69.1674 × 46.132 = 935.8; y = 485 + 0.013887 × 69.1674 × 46.132 = 529.3. The master's NAIP footprint marker sits 1.1 px away, at (936.85, 528.85).

Addresses come from NIST NCSTAR 3 (https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf; PDF page given per row). Lat/lon come from the US Census geocoder, benchmark Public_AR_Current (https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=<address>, Joplin, MO&benchmark=Public_AR_Current&format=json), one match per address. Points are address-range interpolations on the street front. Where the master's l-places already has a NAIP 2010 footprint marker, that marker is the position used (noted per row). "Inside path" tests the true point against the re-traced master path (g-master-map-path, 18 Oct 26).

| building | Table 4-3 count | address or lat/lon | source URL | projected x,y | inside path (yes / flag) |
|---|---|---|---|---|---|
| Walmart (Store #59) | 3 | 1501 S Range Line Rd · 37.074106, -94.477620 | NIST p99 (Sec. 3) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1501+S+Range+Line+Rd%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 936.2, 516.7 | yes (3.0 px inside the north edge) |
| Home Depot | 8 | 3110 E 20th St · 37.069592, -94.475984 | NIST p193 (Fig. 3-42 text) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=3110+E+20th+St%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 940.4, 531.1 | yes |
| Pizza Hut | 5 | 1901 S Range Line Rd · 37.070143, -94.477776 | NIST p336 (Sec. 4.4.8) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1901+S+Range+Line+Rd%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 936.85, 528.85 (master NAIP marker; geocode 935.8, 529.3) | yes |
| Full Gospel Church | 4 | 1828 Michigan Ave · 37.071123, -94.500958 | NIST p329 (Sec. 4.4.5) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1828+Michigan+Ave%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 876.8, 526.2 | yes |
| Harmony Heights Baptist Church | 3 | 2025 Indiana Ave · 37.069034, -94.504478 | NIST p329 (Sec. 4.4.5) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=2025+Indiana+Ave%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 867.9, 532.8 | yes |
| St. John's Regional Medical Center | 12 | 2727 McClelland Blvd · 37.060844, -94.532039 | NIST p298 (reference list) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=2727+McClelland+Blvd%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 800.55, 559.15 (master NAIP marker; geocode 797.7, 559.0) | yes |
| Greenbriar Nursing Home | 19 | 2502 S Moffet Ave · 37.063190, -94.520264 | NIST p251 (Sec. 3) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=2502+S+Moffet+Ave%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 827.7, 551.5 | yes |
| Meadows Healthcare facility | 2 | 1805 W 32nd St · 37.055457, -94.536421 | NIST p356 (Sec. 4.4.12) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1805+W+32nd+St%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 786.5, 576.2 | flag: 0.7 px (about 80 ft) outside the south edge. This fits NIST, which puts the two Meadows deaths below the EF-3 band (Sec. 4.5). |
| AT&T store | 1 | 1702 S Range Line Rd · 37.071844, -94.477854 | NIST p332 (Sec. 4.4.6) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1702+S+Range+Line+Rd%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 935.6, 523.9 | yes |
| Elks Lodge #501 | 4 | 1802 W 26th St · 37.062584, -94.535869 | NIST p320 (Sec. 4.4.1) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1802+W+26th+St%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 788.0, 553.4 | yes |
| Stained Glass Theater | 3 | 1318 W 26th St · 37.062417, -94.528317 | NIST p325 (Sec. 4.4.3) https://nvlpubs.nist.gov/nistpubs/NCSTAR/NIST.NCSTAR.3.pdf ; https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=1318+W+26th+St%2C+Joplin%2C+MO&benchmark=Public_AR_Current&format=json | 805.95, 555.30 (master NAIP marker; geocode 807.2, 554.0) | yes |

Sum of counts: 64 (Table 4-3, base 154). UNSOURCED rows: none.

## Drawn in g-intro-map-dots-v2.html (layout, not geography)
Each group is a grid at a 12 px pitch inside its own marker, sized to fit. A greedy search (largest group first, 0.1 px radius steps, 5° angle steps, no RNG) found the nearest spot where markers stay 4 px apart and clear the 90 existing dots by 4 px. Several true points sit within 6 to 15 px of each other: Range Line holds 4 groups, and the 26th St / SJRMC area holds 5. At 12 px pitch the markers cannot sit on their true points without overlapping, so they were moved off them:

| group | marker centre drawn | shift from true point |
|---|---|---|
| Greenbriar | 827.7, 538.9 | 12.6 px (0.27 mi) |
| SJRMC | 768.6, 559.1 | 31.9 px (0.69 mi) |
| Home Depot | 940.4, 520.3 | 10.8 px (0.23 mi) |
| Pizza Hut | 899.4, 525.6 | 37.6 px (0.82 mi) |
| Full Gospel | 876.8, 496.5 | 29.7 px (0.64 mi) |
| Elks | 780.1, 524.1 | 30.4 px (0.66 mi) |
| Walmart | 936.2, 485.3 | 31.4 px (0.68 mi) |
| Harmony Heights | 847.7, 497.9 | 40.4 px (0.88 mi) |
| Stained Glass | 811.0, 497.8 | 57.7 px (1.25 mi) |
| Meadows | 808.4, 623.0 | 51.7 px (1.12 mi) |
| AT&T | 910.2, 502.5 | 33.2 px (0.72 mi) |

Open problem: g-intro-map-dots(.html and -v2.html) still carries the path from before the 18 Oct re-trace. Its polygon is about 60 px south of the master's, so 0 of the 64 named dots fall inside the drawn path. Only 3 of the 90 schematic dots fall inside the master path.
