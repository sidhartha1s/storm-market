# edit_script.md — br-elnino-texas · "Texas, This Winter Will Not Be Normal"

> Breaking lane (`/storm-breaking`), El Niño series #2. Same segment format as br-elnino-california.
> Numbers spelled out for TTS; every fact carries `[src: N]`. Delivered pace ≈ 158 wpm (measured on #1).

## Spec
- Slug `br-elnino-texas`. Runtime target 9:20 (floor 8:30). Words ≈ 1,400.
- Voice: pocket-TTS Pharaoh, native pace. CTA: `config.yaml channel.cta` (v5), after C3, 1.0 s dips.
- Visual grammar: FORMAT.md; popfig with local scrim (v3 CSS); news bug; no chapter cards; data-feed holds:
  CPC SST loop (C1), NOAA OND precipitation outlook (C2), NASA/NOAA satellite loop (C5).
- Pool: `library/breaking/el-nino-2026/` reused (reordered, never the California sequence) + Texas-specific pulls
  (Houston bayou floods, Garland 2015 aftermath, Hill Country low-water crossings, DFW ice) — provenance.csv rows.

## Sources
1. NOAA news release "El Niño forms, expected to strengthen" (advisory, +3.0 °C, >90 % very strong, 69 % strongest since 1950, peak Oct–Jan, southern-tier storm track). https://www.noaa.gov/news-release/el-nino-forms-expected-to-strengthen-say-noaa-forecasters
2. NOAA CPC Oct–Dec 2026 outlooks (Texas "Above" precipitation; temperature "Equal Chances"). https://www.cpc.ncep.noaa.gov/products/predictions/long_range/
3. NWS Houston/Galveston, Storm Signals vol. 47 (1997 Hobby 79.97 in, 3rd highest; IAH 131 % of normal; Jan 6 1998 flood 10–12 in; Lake Houston 47.48 ft vs 44.5 ft spillway; 300+ warnings Nov–Feb vs 540 all of 1997; "nearly 3 times as many warnings"). https://www.weather.gov/hgx/stormsignals_vol47
4. NOAA/NCEI, "The El Niño Winter of '97–'98" (winter 2nd warmest, 7th wettest since 1895; stronger subtropical jet across the southern tier). https://www.ncei.noaa.gov/monitoring-content/billions/reports/19971201-19980228-severe-storm/tr9802.pdf
5. NWS Fort Worth, "12/26/15 North TX Tornado Outbreak" (12 tornadoes, 13 dead, Garland–Rowlett EF4, #4 December outbreak by count). https://www.weather.gov/fwd/dec26tornadoes
6. Wikipedia / Tornado Talk, 2015 Garland tornado (first EF4 in Texas in December; 10 deaths on the EF4 track, 468 injured). https://en.wikipedia.org/wiki/2015_Garland_tornado
7. NOAA CPC ENSO status: 2015–16 was a strong El Niño winter (context for source 5). https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php
8. NWS "Turn Around Don't Drown" (low-water crossings; more than half of flood deaths are vehicle-related). https://www.weather.gov/safety/flood-turn-around-dont-drown

---

## HOOK (0:00–0:08)

### H1-S1 — narration
> Texas, this winter will not be normal. NOAA has just given the ocean behind it a sixty nine percent chance of being the strongest El Niño ever recorded.

Visual: CPC SST map push; popfig "69%" / "STRONGEST EVER". [src: 1]

## INTRO (0:08–1:05)

### I1-S1 — narration
> The last time the Pacific did this, the National Weather Service office in Houston wrote down what happened. From November to February, it issued more than three hundred severe weather, tornado and flash flood warnings. That was nearly three times a normal winter. And the winter before that scale of ocean heat, in December of twenty fifteen, a tornado outbreak north of Dallas killed thirteen people in a single night.

Visual: NWS warning map / Houston flood 1998 stills; Garland aftermath; popfigs "300+ WARNINGS", "13 DEAD · DEC 26". [src: 3, 5]

### I1-S2 — narration
> But here is what people get wrong about El Niño in Texas. They plan for a cold winter. The danger is not the cold. It is two things almost nobody plans for in December, and both of them come from the same shift in the sky. Stay with this, because by the end you will know which of the two your part of Texas gets, when the window opens, and the four things to do before it does.

Visual: jet-stream diagram teaser, DFW skyline storm; chip "TWO DANGERS · ONE SHIFT"; popfig "4 THINGS". [src: 1]

## CH1 — THE DECLARATION (1:05–2:00)

### C1-S1 — narration
> The facts on the record first. NOAA has an El Niño advisory in effect. Water in the eastern tropical Pacific is running more than three degrees Celsius above average. The Climate Prediction Center puts the odds of a very strong event this winter above ninety percent, and the odds it beats every El Niño measured since nineteen fifty at sixty nine percent. The peak is expected between October and January. And on NOAA's own outlook map for the end of this year, Texas sits inside the band marked above normal precipitation.

Visual: DATA-FEED HOLD, CPC weekly SST loop labelled; popfigs "+3.0°C", ">90%", "OCT – JAN"; then OND precipitation outlook hold, chip "TEXAS · ABOVE NORMAL RAIN". [src: 1, 2]

## CH2 — WHY TEXAS (2:00–2:55)

### C2-S1 — narration
> The mechanism is simple, and it is the same one that soaks California. In a strong El Niño, the subtropical jet stream, the river of fast air that steers Pacific storms, strengthens and drops south. NOAA describes it as fast moving storm systems coming off the Pacific and crossing the southern tier of states. Texas is the widest part of that tier. And Texas has something California does not: the Gulf of Mexico on its doorstep. Every Pacific storm that crosses the state can pull warm, wet Gulf air up ahead of it. Pacific energy, Gulf moisture. That combination is the whole story of this winter, and it is why the danger is not the cold.

Visual: animated jet-stream diagram (normal vs El Niño), Gulf moisture arrows; popfig "STORM TRACK SOUTH"; chip "PACIFIC ENERGY + GULF MOISTURE". [src: 1, 4]

## CH3 — THE WINTER OF 97–98 (2:55–4:00)

### C3-S1 — narration
> Take nineteen ninety seven. Houston Hobby airport measured seventy nine point nine seven inches of rain that year, the third wettest year in its history. Bush Intercontinental finished at one hundred thirty one percent of normal. Then, on January sixth of ninety eight, a cold front ran into tropical moisture and dropped ten to twelve inches in a day. Lake Houston crested at forty seven and a half feet, three feet over its spillway. Upstream, Lake Livingston peaked two feet above its normal pool and released sixty seven thousand cubic feet of water every second down the Trinity. The San Jacinto and the Navasota went over their banks in the same week. Subdivisions and roads went under across Harris, Montgomery and Liberty counties, and most rain gauges in the region finished the season at one hundred twenty to one hundred sixty percent of normal.

Visual: Houston flood archive, Lake Houston spillway stills, FEMA 1998 photos; popfigs "79.97 IN", "131%", "JAN 6 · 12 IN", "3 FT OVER". [src: 3]

### C3-S2 — narration
> And the number that matters most for this winter is the one the forecasters counted afterward. More than three hundred warnings between November and February, in a region that had issued five hundred forty for the entire previous year. Nearly three times the normal winter load. Nationally, that winter finished as the seventh wettest and the second warmest since eighteen ninety five. Wet and warm, not wet and cold. Remember that, because it is the key to the first danger.

Visual: warning count graphic, NCEI report card still; popfigs "300+ WARNINGS", "3× NORMAL", "7TH WETTEST"; connective into CTA dip. [src: 3, 4]

## CTA — `assets/cta/paul-storm-ready-v5-sep6.mp4`, dips 1.0 s

## CH4 — THE DECEMBER NOBODY EXPECTED (4:16–5:15)

### C4-S1 — narration
> December twenty sixth, twenty fifteen. The day after Christmas, in the middle of the last super El Niño winter. Warm, humid Gulf air had been sitting over North Texas for days. A strong Pacific trough came in behind it, with a one hundred knot jet overhead. By nightfall, twelve tornadoes were on the ground across the Dallas area. One of them crossed Interstate thirty between Garland and Rowlett as an EF four, with winds near one hundred eighty miles an hour. Thirteen people died that night, ten of them along that one track, and four hundred sixty eight were hurt. Most of the victims were in cars, on the interstate, in the dark, in December, when nobody in North Texas is listening for a tornado siren. It was the first EF four ever recorded in Texas in the month of December. That is the first danger. In an El Niño winter, tornado season does not wait for spring.

Visual: Garland/Rowlett aftermath (NWS survey photos PD, broadcast pulls credited), I-30 map, Dec 2015 radar still; popfigs "DEC 26, 2015", "12 TORNADOES", "EF4 · 180 MPH", "13 DEAD"; chip "FIRST DECEMBER EF4 IN TEXAS". [src: 5, 6, 7]

## CH5 — THE OTHER DANGER (5:15–6:10)

### C5-S1 — narration
> The second danger is quieter and kills more people. Flash flooding. When storms arrive every few days, the ground never drains. Houston's bayous, the Hill Country creeks, the low water crossings on ranch roads: they fill from the bottom up. More than half of flood deaths in this country happen in vehicles, most of them at crossings that looked passable. In a winter that sends a Pacific storm across the state every few days, the crossing that was dry on Tuesday is the one that takes a car on Thursday. And unlike a tornado, a flood at a crossing gives no siren, no radar signature and no five minute warning. It gives a road that looks wet. Which is why the question is not whether it rains this winter. It is which of these two dangers lands on your county.

Visual: DATA-FEED HOLD satellite loop (NASA SVS AR or GOES Gulf moisture), then low-water crossing footage, bayou flood; popfigs "HALF OF FLOOD DEATHS", "IN VEHICLES"; chip "TURN AROUND · DON'T DROWN". [src: 8]

## CH6 — WHAT IS DIFFERENT NOW (6:10–7:05)

### C6-S1 — narration
> Three things are different from twenty fifteen. First, the signal is stronger. That winter matched the old records. This one is forecast, at sixty nine percent, to beat them. Second, the odds are already on paper. NOAA's outlook has Texas in the above normal rain band for the end of the year, while the temperature map calls the state an even bet, not cold, not warm. Third, and this is the one to watch: wet plus near normal cold in North Texas is the ice storm recipe. The same storms that bring rain to Houston can arrive over Dallas as freezing rain when a shallow cold front is in place underneath. Ninety seven had it. Twenty sixteen had it. This winter has a bigger engine behind it.

Visual: SST loop callback, OND precip + temp outlook maps labelled, DFW ice archive; popfigs "69%", "ABOVE NORMAL RAIN", "ICE RECIPE". [src: 1, 2, 4]

## CH7 — WHO GETS HIT, BY REGION (7:05–8:05)

### C7-S1 — narration
> So by region. Houston and the Gulf coast: repeated heavy rain, bayou and river flooding, the January ninety eight pattern. Dallas, Fort Worth and North Texas: the tornado risk in December and January, and ice when the cold sneaks under the rain. The Hill Country, Austin to San Antonio: flash floods on the creeks and the low water crossings. The Panhandle: snow and ice from the same systems that are rain further south. The Rio Grande Valley: more rain than it has seen in years, which is the one piece of good news in this list. Same storm track, five different winters, depending on where you sleep. And the timing is the same for all five. NOAA expects the peak between October and January and the event to hold through next spring, so the window is not one bad week. It is the whole cold season.

Visual: Texas map with five regions lighting up in narration order (hand-built stat card over a NOAA map plate); popfigs per region; chip "ONE STORM TRACK · FIVE WINTERS". [src: 1, 2, 3, 5]

## CH8 — WHAT IS NOT HAPPENING (8:05–9:05)

### C8-S1 — narration
> Now the honest part. Nobody can tell you which week the first big storm arrives. A seasonal outlook is odds for the whole winter, not a forecast for your street. This is not a repeat of the twenty twenty one freeze; that was a different pattern, and the outlook does not favor a cold winter statewide. And a wet winter is drought relief for the reservoirs and the ranches, which most of the state badly needs.

Visual: split NOT / YES card; reservoir and ranch b-roll; popfigs "NO WEEK FORECAST", "NOT 2021", "DROUGHT RELIEF". [src: 2]

### C8-S2 — narration
> So, four things before December. One, learn your crossing. If your drive home has a low water crossing, decide now which road you take instead, because you will not decide well at night in the rain. Two, if you live north of Waco, put a weather radio or a warning app on before the first December storm, because the sirens you hear in May work in December too. Three, clear the drains and the ditch on your street. Four, check whether your policy covers flood, because most standard policies do not.

Visual: 4-row checklist card over footage; popfigs "1 YOUR CROSSING", "2 WARNINGS ON", "3 DRAINS", "4 INSURANCE". [src: 5, 8]

## CLOSE (9:05–9:20)

### Z1-S1 — narration
> The ocean has already made its move, and Texas is in the path. Two dangers, one shift in the sky, and the prepared house is the one still standing in March. Subscribe, and watch the California video next, because the same storms start there.

Visual: outro brand card; end screen pointer to the California video.
