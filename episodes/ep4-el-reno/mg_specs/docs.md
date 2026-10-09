# mg_specs/docs.md: the "documents" family (ep4-el-reno), 10 comps

Builder brief on `references/mg-brief-template.md`, sections 0 to 5, written before drawing (10 Oct 26).

## 0. What the family claims
The weather service's own pages say it: a table of 21 lines for the night of May 31, 2013 (8 in vehicles in the El Reno
tornado's path, 1 in a vehicle in flood water, 12 sheltering in a drainage ditch), with ages and no names; Finding 6 and
Recommendation 6; a paragraph that puts a Spanish-speaking family and thin non-English warning resources side by side
without linking them; a 1 PM safety message that treated a car as a choice; the 4 June upgrade to EF5; and the Moore
finding about predetermined shelters. Every page is shown as the page, every quote as an attributed card.

## 1. Source (read by eye, 10 Oct 26; file names under `media/docs/`)
| Thing | Exact words or value | Source |
|---|---|---|
| Table header | DATE · SEX · AGE · LOCATION/CIRCUMSTANCES (no name column) | `sa-p60-...first-page.png` |
| May 31 rows, first page (8) | M 67 "Vehicle, driving from El Reno to Chickasha"; M 35, M 55, M 24, M 45 "Vehicle, storm chasing"; F 26 and M 17 days "Vehicle, parked along I-40"; M 32 "Vehicle" | same page; the May 19 and May 20 rows are cropped out |
| May 31 rows, second page (13) | M 65 "Vehicle, flash flood"; M 8 "sheltering in drainage ditch - flash flood"; eleven rows "Sheltering in drainage ditch, flash flood" (M 4, M 33, F 34, M 4, F 7, F 34, M 21, F 3, F 4, M 3, F 5 months) | `sa-p61-...second-page.png` |
| Finding 6 | "Interviews with the public indicated the broadcast media focused on the tornadoes and not the flooding during the May 31 event." | `sa-p54-...list.png` |
| Recommendation 6 | "The NWS needs to provide specific educational material to the broadcast media partners on how to manage warning dissemination for multiple severe weather hazards." | same page |
| Section 4.5 paragraph | "...was a Guatemalan family whose primary language was Spanish. In interviews with EMs and broadcast meteorologists, they acknowledged that there are insufficient forecast and warning resources for those who do not speak English." Next paragraph: "Only a few radio and television stations broadcast in Spanish, ..." | `sa-p47-...paragraph.png` (printed page 38) |
| 1 PM message | "TORNADO SAFETY: If you choose to flee in your car, plan for and anticipate traffic jams and blocked roads, hail, heavy rain and flooding." ("At 1 p.m. on May 31, WFO Norman tweeted") | assessment PDF page 21, read from the PDF text |
| Moore finding | "survived above ground in predetermined shelters. Shelters ranged from interior closets and bathrooms to safe rooms." | `sa-p41-...predetermined-shelters.png` (printed page 32) |
| 4 June statement | "WITH THIS INVESTIGATION... THE TORNADO HAS BEEN UPGRADED TO AN EF5 TORNADO BASED ON VELOCITY DATA FROM THE RESEARCH MOBILE RADAR DATA ..." header "PUBLIC INFORMATION STATEMENT...CORRECTED / NATIONAL WEATHER SERVICE NORMAN OK / 1206 PM CDT TUE JUN 4 2013" | `nws-oun-pns-2013-06-04-el-reno-ef5.txt` |
| 295 mph | "The RaXPol radar data shows winds of at least 295 mph very close to the surface." | `nws-oun-events-20130531.html` (not in the 4 June statement) |
| Enma Aguilar | "...they just thought it was going to be a tornado, not a flooding." | `edit_script.md` A4-S4 (News 9), `fact_check.md` |
| Names | News 9 spellings in the Z1-S1 Picture note; Corey Don Johnson, three (N9, `fact_check.md` A4-S6) | `edit_script.md`, `fact_check.md` |
| El Reno track, city tracks 10, 13, 14, 15 and tornado 7 | metro px | `media/data/tracks.json`, `mg_specs/maps.md` section 2 |
| 6:03 PM touchdown | START TIME 6:03 PM CDT | 4 June statement |

## 2. Datum, scale, orientation
Page images are 1700 x 2200 px. A page is shown as crops of that image at one scale per comp; marks are placed in page px
and multiplied by the scale. Table: x 361 to 1329; columns DATE 363-518, SEX 521-606, AGE 609-760, circumstances 764-1327.
First page: header row y 341-388, May 31 rows y 1578-1979 (first row is two lines, 1578-1657; then 7 rows of 45.8).
Second page: 13 rows y 200-799, pitch 45.85. Section 4.5 page: heading y 1205-1237; lines at y 1284, 1322, 1360, 1399,
1437, 1475, 1514 (paragraph one) and 1590, 1629, 1667 (paragraph two), each 30 px tall; on the line at 1437 "a Guatemalan"
starts at x 383, "Spanish." ends at x 1176, "In" starts at x 1197.
Maps (I1-S2, A5-S1, Z1-S1): metro frame, x = (lon + 98.20) * 1920, y = (35.70 - lat) / 0.46 * 1080, north up.

## 3. Geometry per comp (screen px)
| Comp | Layout |
|---|---|
| g-i1s2-table | map at the west view (zoom 1.8), then the full metro frame, then back west for the cut; page crop 802 x 388 (scale 0.82) at left 760, top 96; rail left 96, top 64; tray left 96, top 872 |
| g-a4s7-table | rail 600 x 470, held at 1.75x in the centre (x 435 to 1485, y 19 to 842) until 11.36, then left 96, top 110; page crop 841 x 581 (scale 0.86) at left 740, top 110 |
| g-z1s1-table | page crop 782 x 860 (scale 0.80) at left 600, top 96; rail left 96, top 90; then names in two columns at x 140 and x 860 |
| g-a4s10-finding6 | root transparent; small card left 96, top 64; Finding 6 card left 96, top 290, 1180 x 400 |
| g-a4s11-page | page crop (x 170-1530, y 1185-1705) at scale 1.1 = 1496 x 572 at left 96, top 250; unlit page at blur 9 px |
| g-a4s13-clock | clock centre 400, 400, radius 210; message card left 760, top 150, 830 x 440 |
| g-a4s14-message | same card, slides 330 px left and grows to 1.35x (x 285 to 1405, y 73 to 667); lift cards left 140, top 380 |
| g-a4s15-rec6 | card left 96, top 120, 1100 x 470; then name cards left 96 (800 wide) and the note left 1000, 560 wide |
| g-a5s1-statement | full metro frame; rail left 96, top 64; statement card left 800, top 96, 790 x 500; readout left 96, top 740 |
| g-a5s7-quote | root transparent; stamp left 96, top 64; lifted word left 96, top 214; quote card left 96, top 360, 1300 x 320 |

## 4. Must be true in the picture
1. Table rows on screen are only rows dated May 31. Eight on the first page, thirteen on the second, twenty-one in all.
2. The eight first-page rows all begin with the word "Vehicle"; the underline sits under that word in each of the eight.
3. Twelve rows are lit as drainage-ditch rows; the "Vehicle, flash flood" row (M 65) is not one of them.
4. The table has four columns and no name column. No name is drawn on or beside any row, and no name column is added.
5. Every page word on screen is the page image itself. Retyped words are attributed cards: Finding 6, Recommendation 6, the 1 PM message, the Moore sentence, the 4 June statement, each with its source line, each copied from the page (not the narration).
6. Section 4.5: the two sentences are lit separately, in two colours, with a thin rule between them and no arrow or bracket joining them. The word "killed" on that line is never lit and stays unreadable (the unlit page is blurred).
7. Clock: starts at 6:03, runs backward, stops at 1:00; the gap reads "5 hours".
8. "295 mph" carries the event page as its source and the page's words "at least"; the 4 June statement card does not contain it.
9. The EF5 mark sits on the El Reno track (metro x 247 to 676, y 453 to 581).
10. A4-S15: the name cards are large glass cards; the 1 PM message is a small beige note with its condition ("If you choose") underlined. Different kind, different size.
11. Death words: "lost", "did not survive". Names are text only. No photographs of people.
12. Nothing appears before its spoken word; counts shown never exceed the count spoken so far.
13. No text or mark of ours in x >= 1600, y >= 680.
14. Only tracks with coordinates on disk are drawn as "other tornadoes" (5 of the 18); the number 18 and the 0 sit in the rail.

## 5. Text (exact) and cues (seconds from each segment's words.json)
The comp files are the record of final text and cue times (each cue carries its word and second in a comment).

- **g-i1s2-table**: page crop (header + 8 rows); "NWS SERVICE ASSESSMENT · APPENDIX C"; rail "8" "in the path of the El Reno tornado", "all 8 in vehicles", "18" "other tornadoes that day", "0" "lives lost in them"; "El Reno", "Oklahoma City"; tray "PLACE NOT GIVEN IN THE RECORD" "67" "32" "26" "17 days"; "GREY TRACKS: NWS NORMAN, STORM DATA · 5 OF THE 18 ARE IN THIS FRAME". Cues: page "table" 2.34 · AGE "age" 5.32 · circumstances "what" 6.10 · rows and rail "Eight" 7.80 · pins "path" 8.30 · "Vehicle" underlines "eight" 10.80 · page out 12.30 · "18" 12.80 · tracks "touched" 14.06 · "0" "None" 16.28.
- **g-a4s7-table**: "THE GROUP OF ELEVEN", "5" "of the 11 did not survive", "6" "did", "18" "went into 2 drains", "12" "did not survive", page crop (header + 13 rows), "NO NAME COLUMN", "NWS SERVICE ASSESSMENT · APPENDIX C", "Names: local reporters and the families". Cues: 5 dim "5" 2.36 · "6" 4.70 · "18" 6.30 · "12" 9.32 · page "table" 12.12 · twelve rows "12" 12.76 · underline "sheltering" 14.52 · ages "ages" 17.96 · no names "no" 19.12 · names line "names" 20.46.
- **g-z1s1-table**: page crop (header + 21 rows), "THE NIGHT OF MAY 31, 2013", "21" "lines", "ages", "no name column", "NWS SERVICE ASSESSMENT · APPENDIX C"; names "Richard Henderson", "Tim Samaras", "Paul Samaras", "Carl Young", "Samuel Cifuentes", "Florinda Santos", "Alex", "Yolanda Santos", "Cristofer", "Brandon", "Lesly", "Corey Don Johnson" "3 years old"; "Among them" over each of the three groups (the voice's words, 8.72, 13.80, 20.26); "NAMES FROM PRESS REPORTS · SPELLINGS AS NEWS 9 GAVE THEM". Cues: page "Weather" 0.52 · date "May" 2.12 · 21 "21" 4.86 · ages 6.40 · no names 7.24 · page out 8.20 · names 9.16, 10.56, 11.68, 12.54, 14.46, 15.40, 15.98, 16.96, 17.58, 18.84, 19.30, 21.34 · "3" 23.08.
- **g-a4s10-finding6**: "…they just thought it was going to be" / "a tornado, not a flooding." "ENMA AGUILAR, FAMILY MEMBER, TO NEWS 9"; "Finding 6" + the sentence in four lines; "NWS SERVICE ASSESSMENT". Cues: small card 0.20 · phrase lit "family's" 2.40 · Finding 6 "They" 5.52 · lines 5.52, 5.88, 7.90, 8.74.
- **g-a4s11-page**: page crop only; "NWS SERVICE ASSESSMENT". Cues: page "assessment" 0.52 · sentence one "a" 1.44 · rule "and" 5.06 · sentence two 8.98, 11.68, 14.98 · "Only a few" 17.80 · rule pulse "does not say" 22.28.
- **g-a4s13-clock**: "6:03 PM" "TOUCHDOWN", runs to "1:00 PM", "5 hours before the tornado"; card "TORNADO SAFETY:" "If you choose to flee in your car," "plan for and anticipate traffic jams" "and blocked roads," "hail," "heavy rain" "and flooding." "NWS NORMAN, 1 PM, MAY 31, 2013" "QUOTED IN THE NWS SERVICE ASSESSMENT". Cues: clock "clock" 2.78 · run back 3.96 to 5.30 · "five hours" 5.38 · card "weather office" 7.34 · lines 8.96, 10.86, 13.54, 14.48, 15.84, 16.54, 17.12.
- **g-a4s14-message**: the same card; lift cards "traffic jams", "flooding" with "NWS NORMAN, 1 PM". Cues: condition underline "car" 4.32 · source underline "office" 7.38 · root clears 12.20 · "traffic" 12.58 · "flood" 13.72.
- **g-a4s15-rec6**: "Recommendation 6" + the sentence in five lines, "NWS SERVICE ASSESSMENT"; "ON TELEVISION" "Mike Morgan" "KFOR" "Gary England" "KWTV, a competing station"; "POSTED AT 1 PM" + the 1 PM message + its source line. Cues: headline "recommendation" 1.38 · lines 2.32, 4.52, 5.00, 6.22, 6.50 · card out 8.00 · note "car" 9.70 · name cards "one man" 11.68.
- **g-a5s1-statement**: "June 4, 2013" "four days after the storm"; statement card (header lines, then the upgrade sentence) "NWS NORMAN · PUBLIC INFORMATION STATEMENT"; "EF5"; "El Reno", "Oklahoma City"; "WINDS OF AT LEAST" "295 mph" "VERY CLOSE TO THE SURFACE · RAXPOL RADAR" "NWS NORMAN EVENT PAGE". Cues: date "June" 0.40 · four days 2.54 · card "weather office" 4.30 · upgrade line "raised" 5.54, 6.46 · EF5 "EF" 6.84 · radar lines "because" 9.14 · 295 "295" 13.26.
- **g-a5s7-quote**: "May 20, 2013" "Moore" "EF5"; quote in three lines, "NWS SERVICE ASSESSMENT"; lifted word "predetermined" "THE ASSESSMENT'S WORD". Cues: date 0.30 · EF5 2.04 · Moore 3.00 · card "assessment" 10.30 · lines 11.74, 13.08, 14.72, 15.80, 16.58 · lift "pre" 18.86.

Transparent spans (footage or map beneath): g-a4s10-finding6 whole window; g-a5s7-quote whole window; g-a4s14-message 12.70 to 14.78.
