# ep-mayfield-2021 fact sheet (21 Oct 26)

Built from `facts-nws.tsv` (44 rows, NWS Service Assessment read in full), `facts-workplaces.tsv` (34 rows) and
`footage-inventory.tsv` (91 rows). The orchestrator re-read the lines marked (re-read) in the Service Assessment text
itself (`sources/NWS_SA_Dec10-11_2021.pdf`, pdftotext, 21 Oct 26). Row ids in brackets point at the TSVs.

SA = NWS Joint Regional Service Assessment, "The Historic December 10-11, 2021 Tornado Outbreak", dated 1 June 2023,
https://www.weather.gov/media/publications/assessments/NWS_Joint_Regional_Service_Assessment_Dec_10-11_2021.pdf
(PDF page = printed page).

## Toll and scale
- 71 tornadoes, eight states, 89 direct tornado fatalities; "the deadliest December tornado event on record since
  1950", passing Vicksburg, Mississippi, 5 Dec 1953 (38). SA p4 (re-read) [F01-F05]. No indirect count in the SA.
  Never say a state count: SA p4 says eight, its own Appendix C (p59-61) lists ten state codes (fc-slice-b.tsv).
  The 71 ran from Friday evening into Saturday (Bowling Green 1:09 AM Sat), so not "that Friday, seventy-one".
- Long-track tornado: EF4, 190 mph, 165.6 miles, from near Woodland Mills, Tennessee, 8:49 PM CST to Falls of Rough,
  Kentucky, 11:47 PM CST; the longest tracked December tornado on record. SA p3, p4, p59 [F06, F19]. Max width 1.13
  miles, 57 deaths on this tornado, 508 to 533 injured, 24 deaths in Graves County: NWS Paducah event page [F19b, F19c].
- A second long-track EF4, Bay, Arkansas to Samburg, Tennessee, 80.3 miles, 170 mph; SA calls them "a pair of
  long-track, violent EF-4 tornadoes" (p12) [F20].
- Edwardsville tornado: EF3, 150 mph, 3.65 miles, Madison County, Illinois (SA p4, p59) [F21].
- Economic impact over $4.3 billion (SA p4) [F06].

## The forecast, in order (all CST)
- Fri 3 Dec, 3:20 AM: SPC Day 4-8 outlook text first mentions severe storms for Friday 10 Dec, on Day 8 (SA p7,
  re-read) [F09a]. Honesty guard: no risk area was drawn in Day 4-8 (SA p8, Finding 1) [F09e].
- Mon 6 Dec, 3:36 PM: NWS Memphis Area Forecast Discussion, first mention: "Friday we should be well into the 70s with
  some warm air advection showers possible. Guidance points to a front moving through the region sometime in the
  Friday/Saturday time frame. This looks like it could be another severe weather threat. We will have to watch this
  over the next several days to monitor the trends and evolution of this system." (SA p14, re-read; IEM archive
  `sources/iem_AFDMEG_2021-12-06.txt`, issuance "336 PM CST Mon Dec 6 2021", re-read) [F07]. The same line runs in the
  5:46 PM, 9:24 PM and 11:35 PM issuances. The 5:02 AM and 11:50 AM issuances that day do not carry it.
  **That is four days before Friday, not five.** The hook's "five days" is wrong [F08].
- Mon 6 Dec: WFO Paducah holds its first partner conference call (SA p14) [F10a].
- Wed 8 Dec, 2:15 AM: SPC Day 3, Slight Risk from northern Louisiana to western Kentucky and southern Indiana, about
  60 hours before the first reports (SA p7, re-read) [F09b].
- Thu 9 Dec, 12:58 AM: SPC Day 2, Enhanced Risk, 10 % tornado with a significant-tornado hatched area (SA p7) [F09c].
- Fri 10 Dec, 10:18 AM: SPC Day 1, Moderate Risk, 15 % tornado and hatched area, sent 12 minutes early "to get the
  word out" (SA p7, re-read) [F09d]. Public Severe Weather Outlooks 10:27 AM and 2:01 PM.
- Fri 10 Dec, 3:00 PM: Tornado Watch 552 (the first of eleven), mentions intense tornadoes; 6 h 25 min before the
  Mayfield tornado (SA p9, re-read) [F22].
- Fri 10 Dec, 5:20 PM: Tornado Watch 553, central Missouri and west-central Illinois; about 3 hours before the
  Edwardsville touchdown (SA p9, re-read) [F15b].
- ECMWF Extreme Forecast Index flagged the setup at Day 7 (SA p45) [F10c].
- Finding 3a: some offices waited until Day 1 or 2 "in part due to established playbooks"; Recommendation 3: say what
  you know when you know it (SA p15) [F10d].

## The warnings that night
- Edwardsville: the Amazon delivery station hit about 8:27 PM; warning and information "approximately 25 minutes
  prior to the warehouse being hit" (SA p29, re-read) [F15]. WFO St. Louis staff themselves sheltered 7:45 to 7:53 PM
  (SA p26) [F28].
- Mayfield: Graves County tornado warning 9:05 PM; Tornado Emergency for Mayfield 9:26 PM, Graves County emergency
  manager called directly (SA p29, p47, re-read) [F23]. Lead about 20 minutes is derived, not an SA figure.
- WFO Paducah lost commercial power about 9:25 PM and its backup generator failed (SA p30) [F28].
- Whole outbreak: 136 tornado warnings, 96.4 % probability of detection, average lead 19.28 min; 8 tornado
  emergencies (SA p32, p46) [F24, F25]. SPC issued a record 28 mesoscale discussions in the evening shift (p12) [F29].
- The SA's own frame of the challenge: tornadoes at a time of year people do not associate with them, after sunset
  on a Friday (SA p6) [F26].

## The two workplaces
- Amazon delivery station, Edwardsville, Illinois: 6 lost their lives (House Oversight, 1 Apr 2022) [D1]. All six were
  contractors working at the building (five delivery drivers, one building-services worker), per OSHA: say "six people
  working at the building", not "six Amazon employees". Building: 1.1 million sq ft, tilt-up walls, no storm shelter;
  city code required 90 mph wind resistance (St. Louis Public Radio) [A6].
- OSHA on Amazon, 26 Apr 2022: Hazard Alert Letter, no citation, no penalty; procedures "met minimal federal safety
  guidelines for storm sheltering" (OSHA Chicago release) [A1, A2]. Reported details: the written plan did not name a
  shelter location; a megaphone meant to start shelter-in-place was locked in a cage; some workers could not recall
  drills (AP via Claims Journal) [A3-A5]. "Did not find any violations" is Amazon's spokesperson, not OSHA.
- Mayfield Consumer Products candle factory, Mayfield, Kentucky: 8 lost their lives (AP, 14 Dec 2021) [D2]. Other
  counts exist: 9 (Hop Town Chronicle, WPSD, DVIDS caption) and 6 (an OSHA accident-summary text). `[verify]` before
  any line: an official count (Graves County coroner or Kentucky state) is still unread.
- About 110 people were inside that night (Spectrum News) [W1]. Night shift for seasonal orders: unverified [W2].
- Kentucky's state OSHA program (Labor Cabinet; Kentucky is a state-plan state) cited the plant in 2022: 7 serious
  violations, $40,000 proposed: exit routes (1), emergency action plans (2), bloodborne pathogens (4). The company
  contested all seven; no outcome found through 2026 (Hop Town Chronicle 22 Aug 2022; LEX18) [R1-R6]. Say "cited" and
  "contested", never "fined". None of the seven is about a missing shelter.
- 2019, separate: a Kentucky inspection with 12 violations (electrical, first-aid-trained staff, emergency
  safeguards), settled for $9,810 (Scripps News) [S1, S2]. Never merge it with the 2022 citations.
- Allegations only: at least five workers told NBC News (14 Dec 2021) supervisors warned they would be fired for
  leaving [F1]; the company spokesman called the claims "absolutely untrue" [F2]. Lawsuits: rulings so far are
  procedural (US District Judge Beaton, Mar 2023; Kentucky Court of Appeals remand, 18 Jun 2026) [F5, F7].

## The guidance gap (the close)
- SA p33 (re-read): "a common theme was identified by WFOs in the post event of a gap in NWS safety outreach materials
  or resources for buildings with large footprints. This was identified as a result of damage and fatalities that
  occurred at large warehouse buildings during the event."
- WFO St. Louis after-action review, quoted in the SA p33-34 (re-read): "The NWS has very little outreach material to
  aid private companies in developing their severe weather plans ... (no official NWS/Occupational Safety & Health
  Administration (OSHA) recommendations for severe weather sheltering guidelines in the workplace, no guidance on what
  types of warnings to shelter for, no differentiation in shelters for businesses with large warehouse construction,
  etc.)". The "no guidance" words are this office's, quoted by the SA; attribute them to it.
- **Finding 6 (SA p34, re-read):** "Multiple offices identified a gap in NWS safety outreach and resources related to
  buildings with large footprints, such as warehouses." **Recommendation 6:** develop "materials with basic tornado
  safety guidelines for large facilities." Finding 6 itself says "gap", not "no guidance".
- OSHA: "OSHA does not have a standard that requires severe weather emergency plans but recommends them" (OSHA release
  26 Apr 2022) [G1].
- What changed: Illinois Warehouse Tornado Preparedness Act (HB 2987, signed Aug 2025): every warehouse needs a
  tornado plan, new warehouses a designated refuge area (St. Louis Public Radio) [G3]. No Kentucky law or OSHA rule
  found (absence unverified) [G4]. Whether NWS has since published the Recommendation 6 materials: unverified.

## Footage (licence risk flagged early)
- Public-domain spine per beat (SAFE-PD rows): forecast 13, Edwardsville 5, Mayfield factory 5, Mayfield town 14,
  Dawson Springs 5, aftermath 5, guidance 1. Thin: Edwardsville (no PD picture of the Amazon building), the factory
  interior (none), and night-of 911 or weather-radio audio (none found).
- Best PD: DVIDS/FEMA candle-factory stills (dvidshub.net/image/7018049, 25-image gallery); NASA MODIS track and VIIRS
  night-lights before/after; NWS Paducah survey photos; SPC and Memphis AFD archive pages and NEXRAD Level II for our
  own radar; Kentucky Guard and Army Corps Mayfield photos and video.
- NEVER or licence needed: Kyanna Parsons-Perez's Facebook Live from under the rubble (her written licence only);
  Brett Adair / Live Storms Media, Brandon Clement and 270 Drones aerials, even where NWS pages host and credit them;
  Fox 2's Amazon aerial (also on the NWS St. Louis page); Maxar Open Data (CC BY-NC); Beshear briefings (Kentucky state
  work, not automatically PD); the First National Bank of Mayfield CCTV; AP and Getty.
