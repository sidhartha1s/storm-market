# MG spec: family `roads` (ep4-el-reno), 6 comps, 10 Oct 26

Built on `references/mg-brief-template.md`. Sections 0 to 5 are the meaning layer; each comp then has its claim, text and cues.

## 0. What the family claims
Two chase crews met the El Reno tornado on two different roads, minutes apart: The Weather Channel S U V southbound on US-81 (6:19 PM), the research car eastbound on Reuter Road (headlights last seen 6:22:15 PM, struck 6:23:35 PM). The tornado was 2.6 miles wide at its maximum (more than 45 football fields), its core about 1.25 miles, and a car could cross the wide circulation at about 45 mph and come out.

## 1. SOURCE (quoted from `fact_check.md` and `research/angle-facts-2026-10-09.md`)
- Width: PNS "PATH WIDTH /MAXIMUM/: 2.6 MILES", measured "AFTER THE TORNADO PASSED EAST OF US HIGHWAY 81"; maximum size 6:24 to 6:26 PM CDT (OUN). So the 2.6 mile ring is the maximum, not the 6:19 PM size.
- Fields: "2.6 x 1760 / 100 = 45.8 fields of 100 yards" (fact_check A2-S2). Script says "more than forty five".
- Core: W14 "about 2 km across (1.24 miles) at its core flow where the cars entered it"; script "about a mile and a quarter".
- Weak side: W14 both vehicles "penetrated the weak side of the MVMC/tornado, so they may have been unaware that they were inside."
- US-81: OUN "crossing US-81 near Reno Road at 6:19 PM CDT". W14: "A Weather Channel vehicle driving southward on US-81 penetrated into the tornado/MVMC in an attempt to traverse to the southern side"; winds "transported the vehicle to the east side of US-81". Thrown about 200 yards (`facts.md`, weather.com).
- Reuter Road: research car "eastbound on Reuter Road just behind Dan Robinson at about 6:21 to 6:22 PM CDT. Robinson was doing about 20 m/s (44.7 mph); the research car fell behind. Its headlights are last seen at 6:22:15 PM CDT." (W14). Struck "about 530 m (580 yards) west of the Reuter and Radio roads intersection" (W14).
- Robinson, quoted in the Service Assessment: "Other than the TWISTEX Cobalt and a red pickup truck parked along Highway 81, there were no other vehicles in our immediate vicinity."
- Slow loop: OUN "the loop north of the interstate from 6:27 to 6:35 PM CDT at less than 10 mph".
- Road grid: OpenStreetMap, queried 10 Oct 26 (NOT in fact_check; the fact files give no road spacing). US-81 lon -97.937, Alfadale Road -97.9193 (0.997 mi east), Radio Road -97.9016 (1.994 mi east of US-81); Reuter Road lat 35.479, Reno Road 35.4645 (1.00 mi south), Jensen Road 35.4935 (1.00 mi north); Interstate 40 meets US-81 at lat 35.502 to 35.504 (1.59 to 1.75 mi north of Reuter Road), drawn at 1.7 mi and marked approximate.

## 2. DATUM, SCALE, ORIENTATION
North is up in all six. One scale per comp, scale bar on screen. Datum = the US-81 / Reuter Road crossing (x81, yReuter).

| Comp | px per mile | x81 | Alfadale x | Radio x | yReuter | Reno y | I-40 y | 2.6 mi ring r | core r (1.25 mi) |
|---|---|---|---|---|---|---|---|---|---|
| g-i1s6-roads | 520 | 700 | 1246 | 1760.8 | 330 | 850 | off frame | not drawn | not drawn |
| g-a2s2-fields | 384 | no roads | | | | | | 499.2, centre (1020, 540) | 240 |
| g-a2s3-ring | 220 | 700 | 931 | 1148.8 | 760 | 980 | 386 (approx) | 286 | 137.5 |
| g-a3s1-roads | 300 | 760 | 1075 | 1372 (under the panel from 8.7 s) | 330 | 630 | off frame | 390 | not drawn |
| g-a3s6-reuter | 640 | 130 | 802 | 1435.6 | 620 | off frame | off frame | not drawn (frame is inside it) | not drawn |
| g-a3s7-cars | 400 | 980 | 1400 | 1796 | 380 | 780 | off frame | not drawn | not drawn |

Fix round, 10 Oct 26: Alfadale Road is 1.05 mi and Radio Road 2.04 mi east of US-81 in every comp (x = x81 + 1.05 x ppm, x81 + 2.04 x ppm), matching the replot family. The first build drew them on whole miles.

## 3. GEOMETRY (px, from the numbers above)
- 200 yards = 0.1136 mi: 59.1 px at 520 (i1s6), drawn east from US-81 (W14: east side).
- Research car strike point, 530 m = 0.3293 mi west of Radio Road (that point is 1.71 mi east of US-81): x 1589.6 at 520 (i1s6); x 1224.8 at 640 (a3s6, the car stays west of it: the window ends near 6:22:15 PM, 80 s before the strike).
- Field: 100 yards = 21.818 px at 384; 45 outlines = 981.8 px from the ring's west edge (x 520.8 to 1502.6); ring east edge x 1519.2, so 16.6 px (0.76 field) stays open: "more than 45". Outline height 11.6 px (53.3 yards, standard field width, a drawing proportion only).
- a2s3 speeds share one time compression: Robinson 60 px/s for about 45 mph, so under 10 mph is under 13.4 px/s; the ring creeps at 9 px/s. The move to the 6:27 PM position is a time skip, drawn as a fast dashed-trail glide.
- Speed bars in a2s3: 8 px per mph: 45 mph = 360 px, 10 mph = 80 px.

## 4. MUST BE TRUE IN THE PICTURE
1. North up; US-81 vertical, Reuter Road horizontal; Alfadale Road 1.05 miles and Radio Road 2.04 miles east of US-81; Reno Road 1.00 mile south of Reuter Road.
1a. No ring line, road line, field line, pulse ring or rain streak crosses a label. Where a tag riding a marker would be crossed by a ring (a2s3 "DAN ROBINSON", a3s1 "THE WEATHER CHANNEL"), the name is fixed outside the ring in the marker's colour.
2. The scale bar length equals the comp's px per mile (or the stated fraction).
3. 2.6 mile ring diameter = 2.6 x ppm; core ring diameter = 1.25 x ppm; ratio 2.08.
4. 45 field outlines, each 1/17.6 mile long, end to end from the ring's west edge; they stop short of the east edge by less than one field.
5. US-81 event first (6:19 PM), Reuter Road after (6:22:15 PM); never the same road. S U V moves south; the two cars move east; Robinson ahead of the Cobalt; the gap grows.
6. The "200 yards" line is 0.1136 mile at scale and points east.
7. Research car never east of the strike point (530 m west of Radio Road) in a3s6 or i1s6.
8. Vehicles are rectangles or dots with text tags. No photo, no vehicle art, no people. Robinson is a marker only.
9. Every figure carries "about" / "under" as the source does: "about 200 yards", "about 45 mph", "about 1.25 miles", "under 10 mph", "more than 45".
10. Every comp with a marker or ring whose place is not given by a number prints "positions approximate".
11. Presenter corner x >= 1600, y >= 680 holds no text.

## 5. Per comp: claim, text, cues (seconds, from `audio/<seg>.words.json`)

### g-i1s6-roads (window 16.79 s, 520 px/mi)
Claim: two crews, two roads; the S U V was thrown about 200 yards.
Text: eyebrow "SOUTH OF EL RENO, OKLAHOMA"; road labels "US-81", "REUTER ROAD", "ALFADALE ROAD", "RADIO ROAD", "RENO ROAD"; tags "CHASE CREW · 3 PEOPLE" x2; "WEATHER CHANNEL SUV"; name "Mike Bettes" / "The Weather Channel"; "about 200 yards"; "1 MILE"; "N"; "VEHICLE POSITIONS APPROXIMATE".
| Cue word | t | What lands |
|---|---|---|
| Not | 0.00 | roads draw, labels in |
| Two (of the vehicles) | 2.86 | marker 1 on US-81, marker 2 on Reuter Road |
| crews | 6.28 | tag 1 "CHASE CREW · 3 PEOPLE" |
| three | 7.24 | tag 2 "CHASE CREW · 3 PEOPLE" |
| Weather | 9.66 | tag 1 becomes "WEATHER CHANNEL SUV" |
| Mike | 12.16 | name "Mike Bettes" / "The Weather Channel" |
| threw | 14.38 | marker 1 thrown east, line draws |
| 200 | 15.06 | "about 200 yards" |

### g-a2s2-fields (20.91 s, 384 px/mi)
Claim: 2.6 miles is more than 45 fields; the core is about 1.25 miles; both crews came in on the weak side.
Text: "MAXIMUM WIDTH · NWS NORMAN"; "2.6 miles"; "MORE THAN"; "45"; "FOOTBALL FIELDS, END TO END"; "100 YARDS EACH"; "CORE · ABOUT 1.25 MILES"; "WEAK SIDE" / "Wurman et al. 2014"; "1 MILE"; "N"; "WIDTHS TO SCALE · POSITIONS APPROXIMATE".
| 2 | 0.00 | ring + "2.6 miles" |
| 45 | 2.00 | 45 outlines tile west to east, counter runs to 45 (done by 3.9 "end") |
| core | 5.12 | core ring draws |
| about (a mile and a quarter) | 7.90 | "CORE · ABOUT 1.25 MILES" |
| wrapped | 10.72 | rain fills the ring, edge fades |
| both (crews) | 14.74 | two markers enter the north half |
| weaker | 16.04 | "WEAK SIDE" / "Wurman et al. 2014" |

### g-a2s3-ring (21.43 s, 220 px/mi)
Claim: a car crossed the core at about 45 mph and came out; later the whole circulation moved at under 10 mph.
Text: marker tag "DAN ROBINSON"; panel "THROUGH THE CORE" / "about" "45" "mph"; "6:27 PM" / "WIDE CIRCULATION" "NORTH OF INTERSTATE 40" / "under" "10" "mph" / "NWS Norman"; road labels "US-81", "REUTER ROAD", "INTERSTATE 40"; "1 MILE"; "N"; "RING AND I-40 POSITIONS APPROXIMATE".
| but | 0.00 | map + ring in place, ring turning |
| Dan | 4.90 | Robinson marker + row label |
| core | 6.52 | marker enters the core ring (x 946 at 6.0, during "drove through") |
| 45 | 8.24 | "about 45 mph" + bar |
| out | 10.86 | marker leaves the core's far side (x 1214 at 10.47), leaves the ring at 12.97 |
| Later | 12.50 | "6:27 PM"; ring glides north of I-40 from 13.0 ("north" 13.22) |
| slowed | 15.64 | ring creeps |
| 10 | 17.00 | "under 10 mph" + short bar, "NWS Norman" |
| fast | 19.02 | small bright spot moves inside the ring |

### g-a3s1-roads (19.59 s, 300 px/mi)
Claim: 6:19 PM, the tornado on US-81; the S U V southbound on it with three named people, heading for the south side.
Text: "6:19 PM" / "NATIONAL WEATHER SERVICE"; road labels "US-81", "REUTER ROAD", "RENO ROAD"; tag "THE WEATHER CHANNEL"; panel (slides in at 8.7) "ABOARD THE SUV" + "Mike Bettes" / "meteorologist", "Austin Anderson" / "driver", "Brad Reynolds" / "camera"; "SOUTH SIDE"; "1 MILE"; "N"; "RING AT 2.6 MILE MAXIMUM" / "POSITIONS APPROXIMATE".
| The | 0.00 | ring arrives from the west |
| 6 (.19) | 3.42 | "6:19 PM" stamp; ring centre lands on US-81 near Reno Road (4.4), then drifts east-north-east at 4 px/s |
| Weather | 5.60 | marker + tag on US-81 |
| heading | 8.12 | marker moves south, arrow |
| Mike | 9.50 | "Mike Bettes" |
| Austin | 11.00 | "Austin Anderson" / "driver" |
| Brad | 12.72 | "Brad Reynolds" / "camera" |
| south (side) | 18.22 | dashed path to "SOUTH SIDE" (line starts 16.26 "they") |

### g-a3s6-reuter (20.87 s, 640 px/mi)
Claim: two cars eastbound on Reuter Road, Robinson ahead at about 45 mph, the Cobalt falling behind; its headlights last seen 6:22:15 PM.
Text: "Reuter Road" stamp / "HEADING EAST · INSIDE THE WIDE CIRCULATION"; tags "DAN ROBINSON", "WHITE COBALT"; "about 45 mph"; "6:22:15 PM" / "HEADLIGHTS LAST SEEN · WURMAN ET AL. 2014"; road labels "US-81", "ALFADALE ROAD", "RADIO ROAD"; "0.5 MILE"; "N"; "VEHICLE POSITIONS APPROXIMATE".
| On | 0.00 | road + stamp "Reuter Road" (0.48) |
| two (more cars) | 1.48 | both markers, moving east |
| Dan | 5.84 | tag "DAN ROBINSON" |
| white | 7.48 | tag "WHITE COBALT" |
| 45 | 11.02 | "about 45 mph" on Robinson |
| fell | 13.24 | Cobalt slows, gap opens |
| headlights | 16.68 | headlight dots start to fade |
| 6 (.22) | 18.92 | "6:22:15 PM" stamp, dots gone |

### g-a3s7-cars (17.42 s, 400 px/mi)
Claim: the roads were empty but for two cars and one red pickup parked along US-81.
Text: tags "DAN ROBINSON", "WHITE COBALT", "RED PICKUP · PARKED"; road labels "US-81", "REUTER ROAD", "ALFADALE ROAD", "RADIO ROAD"; quote "there were no other vehicles in our immediate vicinity" / "Dan Robinson, quoted in the NWS Service Assessment"; "1 MILE"; "N"; "VEHICLE POSITIONS APPROXIMATE".
| Robinson | 0.00 | map, Robinson marker + tag |
| cobalt | 4.76 | Cobalt marker + tag |
| red | 5.86 | red pickup + tag on US-81 |
| no (other vehicle) | 9.02 | quote card slides in (8.7), attribution line with it (9.5) |
| Assessment | 11.80 | attribution line pulses |
| traffic | 13.96 | sweep along the empty roads |

## Not confirmed, left off
- Where on US-81 the S U V and the red pickup were, and where on Reuter Road Robinson and the Cobalt were before the strike: no number in the sources. Drawn as approximate and labelled so.
- Which compass side is the weak side: not stated as a direction. Drawn as the north half because the S U V came in from the north (southbound, "to traverse to the southern side") and Reuter Road is 1 mile north of the 6:19 PM crossing near Reno Road.
- The ring's width at 6:19 PM (2.6 miles is the later maximum) and its centre at any time other than "US-81 near Reno Road, 6:19 PM".
- The Cobalt's speed: no readout.

## Build notes (10 Oct 26)
- Marker colours, same in all six: Weather Channel S U V cold blue #7fb2e5, research car / white Cobalt #f2f5f8, Dan Robinson amber #e8c56a, red pickup #c0392b.
- Initial positions that must hold on the first frame are set with an immediate `gsap.set` as well as `tl.set(..., 0)`: the scan's first frame showed a2s3's ring at 0,0 with only the timeline set.
- Road and scale furniture is on screen from the first frame; cues move the markers, rings and text.
- `freeze_scan.mjs` reads every mounted comp, so it could not run while other families' files were missing. The sheets were made from a scratch copy of the episode with only the six roads hosts (`.qc-tmp/roads-stage/`, gitignored). Re-run on the real episode once all comps exist.
- Sheets tile every 3 s, so reveals after the last tile (i1s6 "about 200 yards" 15.06, a3s1 "SOUTH SIDE" 18.22, a3s6 "6:22:15 PM" 18.92) were read from a second scan of scratch copies shifted 1.7 s. Two labels moved after that read: "about 200 yards" off the US-81 line (left 792, top 772), "SOUTH SIDE" inside the ring (y 950).
- Road grid cross-checked by the team lead's own Overpass geometry read (10 Oct 26): US-81 longitude -97.9379; Alfadale Road 1.05 mi and Radio Road 2.04 mi east of it; Reno Road 1.00 mi south of Reuter Road; research car 1.71 mi east of US-81. The lead's read puts Interstate 40 about 1.52 mi north of Reuter Road at US-81; a2s3 draws it at 1.7 mi (my read: 1.59 to 1.75), a 40 px difference at 220 px per mile, accepted at screen scale and covered by "RING AND I-40 POSITIONS APPROXIMATE". An earlier 1.80 mi figure for Radio Road came from a place centroid, not the road line, and is withdrawn.
- Fix round 2 (10 Oct 26), no cue time, figure, road position or direction changed. a3s7: the two white dots that ran the roads at 13.6 and 14.3 read as a third vehicle against the quote; each is now a thin cold-blue line across its road (2 px by 48 px, 60 % opacity), the one on US-81 starting at y 100, below the "US-81" label. a3s6: the title "Reuter Road" slides in from the right (x 220 to 170), so it is never under the US-81 line at x 130. a3s1: a swatch of the S U V mark's shape and colour (upright rounded bar, #7fb2e5) sits left of "THE WEATHER CHANNEL" and comes on with it; the name moved 24 px right with 1 px letter spacing so it still ends clear of the names panel (measured right edge x 1131).
