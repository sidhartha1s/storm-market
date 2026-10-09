# MG brief: the 21-pin map family (ep4-el-reno, family `map21`, 12 comps)

## 0. What the family claims
On the night of May 31, 2013, 21 people lost their lives around Oklahoma City: 8 in vehicles in the El Reno tornado,
12 in two storm drains in the city, 1 in a vehicle in flood water. The map carries building icons and none ever lights:
no row of the table names a building.

## 1. Source
- NWS Service Assessment, Appendix C (the table: sex, age, circumstance; no names, no places). Counted in `fact_check.md` H1-S1, I1-S3.
- W14 (Wurman et al. 2014): research car about 530 m west of the Reuter Road and Radio Road intersection.
- News 9 (Stein, 8 Jun 2013 archive): family of seven, drainage ditch by the house near NW 26th Street and Meridian.
- News 9 (Torp, 3 Jun 2013): group of eleven in "a storm drain under S.W. 15th near the Dell plant"; five did not survive (table match, the film's inference).
- News 9 (Hertneky, 4 Jun 2013): Richard Henderson "drove down Highway 81". Road only, no point on it.

## 2. Datum, scale, orientation
Metro frame 1920 x 1080, north up. x = (lon + 98.20) * 1920; y = (35.70 - lat) / 0.46 * 1080. About 21 px per km.
Checks (computed by script): El Reno 470.4, 394.4 · downtown Oklahoma City 1313.3, 544.7.
Camera views are scale + translate on one wrapper; all text sits on a fixed layer outside it.

## 3. Geometry: pin table
Colour: amber = vehicle in the tornado; cold blue = flood water. Lit = filled; unlit = hollow ring.

| # | Table row (SA Appendix C) | Place | Source line | lon, lat used | px (x, y) |
|---|---|---|---|---|---|
| 1-3 | M 55, M 24, M 45 "Vehicle, storm chasing" | Reuter Road, 530 m west of Radio Road | W14, `fact_check.md` I1-S4 picture row | px from OpenStreetMap road geometry (team lead, 10 Oct 26) | 561.5, 518.9 (three in a row, 19 px apart, on the road line) |
| 4 | M 35 "Vehicle, storm chasing" | US-81: road only, spot approximate (the point along it is not given) | News 9 4 Jun 2013, `fact_check.md` "Henderson's road" | px on the US-81 line | 503.2, 493 (between the Interstate 40 interchange at y 467.2 and Reuter Road at y 518.9, touching neither) |
| 5-11 | 7 of the 12 "Sheltering in drainage ditch, flash flood" | drainage ditch near NW 26th and Meridian | News 9 (Stein), `fact_check.md` I1-S4 picture row | -97.601, 35.4964 | 1150.1, 478.0 (cluster of 7) |
| 12-16 | 5 of the 12 "Sheltering in drainage ditch, flash flood" | storm drain under SW 15th near the Dell plant | News 9 (Torp), same row; pairing is the film's inference | -97.579, 35.450 | 1192.3, 587.0 (cluster of 5) |

Tray, "PLACE NOT GIVEN IN THE RECORD" (fixed, bottom left, x 96 to 536, y 872 to 1012). Five pins, never on the map:

| # | Table row | Why in the tray |
|---|---|---|
| 17 | M 67 "Vehicle, driving from El Reno to Chickasha" | no point given |
| 18 | M 32 "Vehicle" | no place given |
| 19 | F 26 "Vehicle, parked along I-40" | no point on the interstate given |
| 20 | M 17 days "Vehicle, parked along I-40" | no point on the interstate given |
| 21 | M 65 "Vehicle, flash flood" | no place given |

Count: 16 placed + 5 in the tray = 21. Tornado 3 + 1 + 4 = 8. Water 7 + 5 + 1 = 13.
Coordinates of the four placed sites are the builder's reading of the street grid (section-line roads, the Dell campus on SW 15th);
they were not run through a geocoder.

Roads drawn (simple polylines): Interstate 40, US-81, Interstate 35, Interstate 44, Reuter Road (short, unlabelled). Rivers
drawn only as the water layer: the Oklahoma River and Deep Fork Creek (schematic corridors, not surveyed flood extent).
Building icons (house, store, school outlines, stroke only) are scattered over the towns by a seeded generator that skips
any spot within 46 px of a pin site, on a road, or under a place label. One named house outline sits 50 px west of the
NW 26th cluster.

## 4. Must be true in the picture
1. Counts are exactly 8 + 12 + 1 = 21; each state shows the count the narration has said by then, never more.
2. No pin, name or mark inside or on a building icon. No building icon is ever filled or brightened (a size bump only).
3. A pin sits on the map only at one of the four sourced places; the five others sit in the tray.
4. Names are text only, spelled as News 9 and the script give them. Death words: "lost" or the count alone.
5. Nothing on screen contradicts the sentence being spoken.
6. Text is a name, a count or a place.
7. Unlit pins are hollow; a pin fills only on the word that counts it.

Conflict reported (§4 wins over the Picture notes): A1-S7 asks for the "67" pin on a line to Chickasha, A1-S8 for the "26"
and "17 days" pins on the shoulder of Interstate 40, A2-S9 for all eight El Reno pins "on a road line". The record gives
no point for those four, so they land in the tray; the line toward Chickasha and Interstate 40 are still drawn.

## 5. Panel text and cues (seconds are comp-local = words.json)
Place labels on every state: "El Reno", "Oklahoma City". Tray title on every state that shows the tray.

### g-i1s3-pins (16.28 s) · transparent 2.6 to 6.4 s (footage of flooded streets beneath)
Starts on the El Reno side with the eight lit, slides east. Text: card "Oklahoma City area / the night of May 31, 2013";
rail "13 lost to flood water", "1 in a vehicle", "12 in drainage ditches and storm drains", "8 of the 12 were young children", "5 months the youngest".
The eight are counted in the rail only; no pin is marked as a child, because the table gives ages and not which drain.
| word | t | what lands |
|---|---|---|
| other | 0.42 | camera slides east |
| Oklahoma | 4.84 | glass card over footage |
| vehicle | 7.64 | blue tray pin, row "1" |
| 12 | 8.58 | twelve blue pins at the two drains, row "12" |
| eight | 11.96 | eight of twelve tick dots, row "8 of the 12" |
| five | 14.78 | row "Youngest 5 months" |

### g-i1s4-map21 (12.36 s)
Pulls out from the city to the full map, all 21 lit. Text: "House 0", "Store 0", "School 0", "Storm shelter 0",
"0 of 21 inside a building", "NWS SERVICE ASSESSMENT, APPENDIX C".
| house 2.06 | store 3.06 | school 3.70 | storm (shelter) 4.38 | By that count 5.82 | home 9.24 (house outlines bump, unlit) |

### g-a1s7-map21 (16.53 s) · El Reno view, starts with Henderson's pin lit
Text: "8 lost in the El Reno tornado", "NWS SERVICE ASSESSMENT, APPENDIX C", "3 crew of the white Cobalt", "4 of 8 storm chasing", tray "67", "to Chickasha".
| table 3.44 source line | Three 6.22 three pins on Reuter Road | four 9.28 "4 of 8" | 67 12.84 tray pin "67" | El Reno to Chickasha 14.46 dashed bearing line + "to Chickasha" |

### g-a1s8-map21 (10.32 s) · El Reno view, 5 lit at start
Text: tray "67", "32", "26", "17 days"; rail "8 lost in the El Reno tornado", "32 the table says only “Vehicle”", "2 parked along Interstate 40"; map label "Interstate 40".
| 32 1.20 tray pin | vehicle 3.36 the table's word | Interstate 5.56 I-40 draws, label | 26 7.36 tray pin | 17 8.42 tray pin |

### g-a2s9-map21 (11.34 s) · full map, no new text
All 21 hollow at the start; the eight fill on "eight" 8.02; El Reno road lines brighten on "vehicle" 10.22.

### g-a3s14-map21 (11.05 s)
El Reno view with eight lit; slides east 4.3 to 5.9; the twelve stay hollow. Text: "8 all in vehicles", "12 of the other 13", "sheltering".
| vehicles 2.90 | 12 6.16 | hide 9.72 |

### g-a4s2-names (12.45 s) · city view on the NW 26th ditch, seven hollow pins fill one by one
Text (News 9 spellings): "Samuel Cifuentes", "Florinda Santos · wife", "Alex · son", "Yolanda Santos · cousin", "Cristofer", "Brandon", "Lesly", "Yolanda's children", "NAMES AS REPORTED BY NEWS 9".
| him 0.00 | Florinda 1.90 | Alex 3.96 | Yolanda 6.84 | Cristofer 9.92 | Brandon 10.76 | Lesly 11.28 |

### g-a4s16-map21 (17.68 s)
Full map, 21 lit. Push in to the unlit house outline 5.2 to 8.6, pull out 10.9 to 12.5.
Text: "21 pins", "on roads", "in 2 drains", "House near NW 26th & Meridian", "7", "0 of 21 inside a building".
| 21 1.00 | roads 2.52 | two drains 3.44 | house 5.28 | seven 9.46 | houses 12.30 stores 13.12 schools 13.60 (outline bumps) | not one 14.46 |

### g-a5s9-layers (17.98 s)
Text: "Open roads 8", "sub-vortex", "Low ground 13", "21 on a road or in the water".
| tornado 4.44 roads draw amber | roads 5.40 row | sub 7.36 small circle crosses US-81 | water 11.10 blue corridors | lowest 12.52 row + flow into the drains | 21 15.12 total |

### g-a5s10-map21 (14.15 s)
Text: "21 for the night of May 31", "Okfuskee County · June 1" (a grey hollow marker at the east edge with an arrow off the map; not a pin).
| house 1.32 outline bump | that one night 7.94 | next morning 9.98 grey marker at the east edge | Okfuskee 12.54 label |

### g-a5s12-map21 (13.51 s)
Text: "0 of 21 inside a building", "NWS SERVICE ASSESSMENT, APPENDIX C", "Strongest winds crossed no building", "City tornadoes EF0 and EF1", "Water 13 lives", "12 sheltering".
| crossed 1.76 small circle crosses the road, no outline in its way | no building 2.12 | two lowest 5.98 | water 8.06 corridors | 13 8.72 | lowest 10.40 flow | 12 11.60 |

### g-z1s2-map21 (4.74 s)
The metro map shrinks into its place inside the outline of Oklahoma. Text: "May 31, 2027", "14 years".
| May 31 0.70 | 14 3.22 |

## Fix round (10 Oct 26, verifier rows A to E)
- A. Tray title: tracking 3 px to 1.5 px (type stays 19 px); it now ends about 44 px inside the tray border.
- B. g-a1s7 "to Chickasha": left of the dashed bearing line, clear of US-81; the Union City outlines beneath are not drawn.
- C. g-a5s10 "Okfuskee County · June 1": right edge at x 1824, y 384, with the grey marker under its end at 1800, 434;
  no outline is drawn in that zone. The view opens from the metro view to the whole map at 9.3 to 9.9 s so the east
  edge is open country when the marker lands.
- D. Metro view (scale 1.5, centre 890, 480) replaces the scale 1 map in g-i1s4, g-a2s9, g-a4s16, g-a5s9, g-a5s10
  (to 9.3 s) and g-a5s12. El Reno view is scale 2.4 with US-81 at x 1150. A pin key (the §3 colour code: "In a vehicle,
  in the tornado", "In flood water", "Building") sits top right on every map state except g-a2s9 (no new text; the key
  alone tripped the type-tier gate there), g-a4s2-names and g-z1s2.
- E. The window-long scan tween carries a literal duration, so sweep check 7 reads each timeline's length.
- Outlines hidden after generation (the rest keep their places): Union City, Calumet, the east-edge label zone.

## Build notes
- Shared layout (team lead, OpenStreetMap via Overpass, 10 Oct 26): US-81 x 503.2, Radio Road x 572.7, Reuter Road y 518.9,
  Interstate 40 y 467.2 where it meets US-81. Reuter Road and pins 1 to 3 use these px directly. Interstate 40 passes
  through 35.501 N at US-81 (y 467.2); its other vertices near El Reno are the builder's estimate, not measured.
  Pin 4 moved from y 476.6 to y 493: at 476.6 it sat on the Interstate 40 interchange once the interstate was at its
  measured place, and in g-a1s8 the amber interstate line ran through it (a pin on a line that must carry none).
- Views: full map (scale 1); El Reno view (scale 1.8, centre 520, 470); city view (scale 1.5, centre 1260, 540).
- Initial states are applied at build and repeated at 0 on the timeline (`s0`): a paused timeline does not render a
  set at 0, so the first frame of every window showed an empty map until this was added (found on the first contact sheets).
- `freeze_scan.mjs` reads every mounted comp file, so while other families were unbuilt the scans ran on a copy of
  index.html with only this family's hosts, in `.qc-tmp/map21-ep/` (gitignored).

## Not confirmed, left out
- A point for pins 17 to 21 (tray).
- Where on US-81 Henderson's pickup was: the pin sits on the road line, the spot along it is the builder's.
- Tracks of the city tornadoes (not drawn). Flood extent (corridors are schematic).
