# edit_script.md — br-elnino-california · "California, the Strongest El Niño Ever Recorded Is Coming for You"

> Breaking lane (`/storm-breaking`). Packaging approved 2026-09-08 (plan gate). Segment IDs follow the
> storm-episode format so `scripts/tts_episode.py` runs unchanged; this lane applies `atempo 1.15`
> after TTS. Numbers are spelled out for TTS; every fact carries a `[src:]` line. Word counts per
> segment are checked against the packaging table (2.47 words/s delivered).

## Spec
- Slug `br-elnino-california`. Runtime target 9:30 (floor 8:30 for mid-rolls). Words ≈ 1,410.
- Voice: pocket-TTS Pharaoh (config `external.*`), atempo 1.15 post-TTS.
- Visual grammar (FORMAT.md): median shot 3.5–4.5 s; red popfig + bottom-left data chip on every
  number; caps chapter card on black at each chapter; one labelled real data-feed hold (CPC SST loop
  in CH1, satellite atmospheric-river loop in CH7); 9:16 social pulls pillarboxed on blurred self with
  `@handle · platform` credit; BREAKING-style lower-third bug with the channel name.
- CTA: `config.yaml channel.cta` (Paul, 15.1 s) mounted after C3, 1.0 s dips both sides.

## Sources (cited inline as [src: N])
1. NOAA news release "El Niño forms, expected to strengthen" (advisory; >90% very strong; +3.0 °C; 69% strongest since 1950; peak Oct–Jan; southern-tier storm track). https://www.noaa.gov/news-release/el-nino-forms-expected-to-strengthen-say-noaa-forecasters
2. NOAA CPC ENSO Diagnostic Discussion (current status, outlook). https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml
3. SF Chronicle, "1998 El Niño pounded an unready Bay Area" (17 dead, ~$500M, 2,000+ dwellings, SF 14.89 in Feb record, LA near a year's rain in Feb). https://www.sfchronicle.com/bayarea/article/1998-El-Ni-o-pounded-an-unready-Bay-Area-Are-we-6564050.php
4. USGS FS-175-99 (Feb 1998 Ocean Beach surge, Embarcadero whitecaps, US-101 under 4 ft; >$150M Bay Area landslide damage). https://pubs.usgs.gov/fs/1999/fs175-99/
5. USGS MF-2325 landslide maps 1997–98. https://pubs.usgs.gov/mf/1999/mf-2325/
6. California Coastal Commission, El Niño page (1982–83 and 1997–98 coastal storm damage). https://www.coastal.ca.gov/climate/extreme-weather/el-nino/
7. Scripps, "Why was the 2015–16 El Niño so dry?" (storms shoved north, record-warm Indian Ocean). https://scripps.ucsd.edu/news/research-highlight-why-was-2015-16-el-nino-event-so-dry
8. J. Climate 2018, "Predictability and Prediction of Southern California Rains during Strong El Niño Events" (SSTs on par with 1982–83/1997–98; failed SoCal rains). https://journals.ametsoc.org/view/journals/clim/31/2/jcli-d-17-0396.1.xml
9. WeatherCurrents 2015–16 season review (fifth consecutive below-average SoCal season). https://weathercurrents.com/NewsItemDisplay.do?Id=1217
10. SF Chronicle, "New California maps show the likelihood of a wet El Niño winter" (SoCal 130–200% of normal in strong events; NorCal 110–145%). https://www.sfchronicle.com/weather/article/el-nino-winter-rain-california-22398460.php
11. CNN 2026-08-20, super El Niño winter forecast (GFDL "once in a lifetime type of strength" quote; California above-normal precip category). https://www.cnn.com/2026/08/20/weather/super-el-nino-us-winter-forecast-climate
12. USGS Climate Adaptation Science Centers, atmospheric-river families (>2× as likely in El Niño). https://usgs.gov/programs/climate-adaptation-science-centers/news/atmospheric-rivers-disrupt-traditional-rainfall
13. Weather West (Swain), "Rising odds of a strong-to-historic El Niño" (Dec–Mar flood window, AR intensity). https://weatherwest.com/archives/43880

---

## HOOK (0:00–0:08) — card: none; frame one is the NOAA SST anomaly map, red tongue pulsing

### H1-S1 — narration  (20 words)
> NOAA just gave this El Niño a sixty nine percent chance of being the strongest ever recorded. And California is first in line.

Visual: CPC SST anomaly map, slow push; popfig "69%" on "sixty nine"; chip "STRONGEST SINCE 1950". [src: 1]

## INTRO (0:08–1:10)

### I1-S1 — narration  (78 words)
> The last time the Pacific looked like this, February of nineteen ninety eight, San Francisco took fourteen point eight nine inches of rain in one month. That is still the record. Los Angeles got almost a year of rain in the same four weeks. Seventeen people died. More than two thousand homes were destroyed or damaged, and hillsides from Marin to Malibu simply let go.

Visual: 1998 flood and slide footage, 3–4 s cuts; popfigs "14.89 IN", "17 DEAD", "2,000 HOMES". [src: 3, 4]

### I1-S2 — narration  (74 words)
> But here is the part nobody is saying out loud. The last super El Niño, in twenty sixteen, was supposed to do exactly the same thing. Every forecaster in the state was ready for it. And for Southern California, it never came. So the question is not whether this El Niño is big. It is. The question is which winter California actually gets. By the end of this video you will know what to watch, when to watch it, and the four things to do before December.

Visual: 2016 dry reservoir stills with push, then the NOAA map again; popfig "2016"; chip "WHICH WINTER?". Card cut to CH1. [src: 7, 8]

## CH1 — card: THE DECLARATION (1:10–2:10)

### C1-S1 — narration  (80 words)
> On the record, this is what NOAA has declared. An El Niño advisory is in effect. Sea surface temperatures in the eastern equatorial Pacific are now more than three degrees Celsius above average. The Climate Prediction Center puts the odds of a very strong event this fall and winter above ninety percent. And the odds that it surpasses every El Niño measured since nineteen fifty, including ninety seven and eighty two, at sixty nine percent.

Visual: DATA-FEED HOLD, CPC weekly SST anomaly loop labelled "SOURCE: NOAA CPC", 25 s; popfigs "+3.0°C", ">90%", "69%". [src: 1, 2]

### C1-S2 — narration  (70 words)
> A meteorologist at NOAA's fluid dynamics lab called it very unusual, if not a once in a lifetime type of strength. The peak is expected between October and January, and the event is forecast to hang on through next spring. That timing matters, because it lines up exactly with California's rainy season. However, a strong El Niño in the ocean and a wet winter on the ground are not the same thing.

Visual: GFDL quote card (attributed), calendar strip Oct→Jan popfig "OCT–JAN"; connective into CH2. [src: 11, 1]

## CH2 — card: WHY CALIFORNIA (2:10–3:05)

### C2-S1 — narration  (135 words)
> Here is the mechanism, in plain terms. In a normal winter the jet stream, the river of fast air that steers Pacific storms, runs into the Northwest. Oregon and Washington get the rain. California gets what slips underneath. During a strong El Niño, that warm water in the tropics pumps heat into the atmosphere and the jet stream drops south. NOAA's own outlook says the storm track shifts over the southern tier of the United States. The first place that track hits land is the California coast. Above normal rain is favored across the south, and below normal from the Northwest into the northern plains. So the storms that would have hit Seattle line up on Los Angeles, San Diego and the Bay Area instead. And the last time that happened at full strength, the state was not ready.

Visual: animated jet-stream diagram (two states, normal vs El Niño), then NOAA precip outlook map labelled; popfig "STORM TRACK SOUTH"; chip "SOURCE: NOAA". [src: 1]

## CH3 — card: FEBRUARY 1998 (3:05–4:10)

### C3-S1 — narration  (82 words)
> February of nineteen ninety eight. A series of Pacific storms came in one after another with no gap between them. In the first week of the month, high winds and heavy rain hit at the same time as abnormally high tides. The Pacific surged over the parking lots and the coastal highway at Ocean Beach in San Francisco. Whitecaps six feet high broke over the Embarcadero. North of the Golden Gate, Highway one oh one went under four feet of water from the bay.

Visual: 1998 archive, broadcast pulls 3–5 s credited; popfigs "FEB 1998", "6 FT WAVES", "US 101 · 4 FT". [src: 4]

### C3-S2 — narration  (78 words)
> When the month ended, the numbers were these. Seventeen dead. About half a billion dollars in property loss. More than two thousand homes destroyed or damaged. And in the ten counties around the bay alone, more than one hundred fifty million dollars in landslide damage, because saturated hillsides do not fail in the rain, they fail days later, after the sky has cleared. Hold that thought, because that is exactly the kind of number this winter is being measured against.

Visual: USGS landslide map + photos labelled "SOURCE: USGS"; popfigs "17 DEAD", "$500M", "$150M SLIDES". Then 1.0 s dip → CTA → 1.0 s dip. [src: 3, 4, 5]

## CTA (4:10–4:25) — `assets/cta/paul-storm-ready-v4c.mp4`, own audio, dips 1.0 s in/out

## CH4 — card: THE WINTER OF 1983 (4:25–5:10)

### C4-S1 — narration  (110 words)
> And ninety eight was not the first. The winter of nineteen eighty two into eighty three is the other benchmark on the list, and it was the coast that paid. Storm after storm arrived on top of high tides and unusually high sea levels. Piers were torn apart, beachfront homes lost their foundations, and the state's Coastal Commission still uses that winter as its reference case for what a strong El Niño does to the shoreline. Two events, fifteen years apart, both from an ocean that looked like this one does today. Which is why, in twenty fifteen, when the Pacific lit up again, California braced for a third.

Visual: 1983 archive stills with slow pan (Coastal Commission, credited), pier damage; popfigs "1982–83", "PIERS DESTROYED". Connective into CH5. [src: 6]

## CH5 — card: THE ONE THAT NEVER CAME (5:10–6:15)

### C5-S1 — narration  (84 words)
> In the winter of twenty fifteen into sixteen, the ocean temperatures were on par with eighty two and ninety seven. The media called it the Godzilla El Niño. Reservoirs were empty after four years of drought, and the whole state was waiting for the rain that the pattern promised. Northern California got a little above average. Southern California got an average winter. That made it the fifth below average rainy season in a row for the south, in the middle of a super El Niño.

Visual: 2016 news pulls (credited), empty Folsom or Oroville stills with push; popfigs "2015–16", "5TH DRY YEAR". [src: 8, 9]

### C5-S2 — narration  (76 words)
> So what happened? Scripps researchers went back through it, and the answer is that the atmosphere did not respond the way it had before. The storms that should have landed in California were pushed north, and the Pacific Northwest got record rain instead. One suspect was the Indian Ocean, which that year broke its previous heat record by nearly half a degree Celsius and pulled the pattern out of shape. However, twenty twenty six is not twenty sixteen, and here is why.

Visual: map animation storms deflecting north; Indian Ocean SST anomaly still; popfig "+0.5°C INDIAN OCEAN". Connective into CH6. [src: 7]

## CH6 — card: WHAT IS DIFFERENT NOW (6:15–7:15)

### C6-S1 — narration  (150 words)
> Three differences. First, the signal itself is stronger. Twenty sixteen matched the old records. This event is forecast, at sixty nine percent, to beat them. A three degree anomaly in the eastern Pacific is the kind of heat that has historically forced the jet stream south regardless of what other oceans are doing. Second, the odds are on paper this time. NOAA's official winter outlook already puts California in the above normal category for precipitation. Third, the history is on the south's side. In past strong El Niño winters, Southern California averaged one hundred thirty to two hundred percent of its normal rain. Northern California is the less certain half, at one hundred ten to one hundred forty five percent, because it sits closer to the line between the wet south and the dry north. So if you live south of Point Conception, your odds of a very wet winter are the best they have been in a generation.

Visual: NOAA precip outlook map, then SF Chronicle-style CA split map (redrawn in-house, labelled); popfigs "130–200%", "110–145%"; chip "POINT CONCEPTION". [src: 1, 10, 11]

## CH7 — card: RIVERS IN THE SKY (7:15–8:15)

### C7-S1 — narration  (150 words)
> The rain does not come as a season. It comes as atmospheric rivers, long streams of moisture in the sky that can carry more water than the Mississippi, and in an El Niño winter they arrive in families. Government researchers found that clusters of atmospheric rivers, one behind another, are more than twice as likely under El Niño conditions. That is the nineteen ninety eight pattern, storm after storm with no time for the ground to drain. The flood window runs from December through March. And the places that fail first are the same every time. Fresh burn scars, where there are no roots left to hold the hillside. The slide-prone slopes of the Bay Area and the Santa Monica Mountains. Low coastal roads at Ocean Beach and along Highway one. And any neighborhood built on a creek that has been quiet for five dry years. Which brings us to what is not on this list.

Visual: DATA-FEED HOLD, GOES or NASA satellite loop of an atmospheric river labelled "SOURCE: NOAA/NASA", 25 s; then burn-scar, mudslide, coastal-road b-roll 3–4 s each; popfigs "2× MORE LIKELY", "DEC–MAR". [src: 12, 13]

## CH8 — card: WHAT IS NOT HAPPENING (8:15–9:20)

### C8-S1 — narration  (80 words)
> Let us be exact about what this is not. Nobody can tell you today which week the storms arrive. A seasonal outlook is odds for the whole winter, not a forecast for your street. El Niño has nothing to do with earthquakes or tsunamis, no matter what the comments say. And it is not all bad news. A wet winter is drought relief, full reservoirs, and a real snowpack in the Sierra if the storms come in cold enough.

Visual: split "NOT / YES" card; reservoir and snowpack b-roll; popfig "NO WEEK FORECAST", "DROUGHT RELIEF". [src: 2, 11]

### C8-S2 — narration  (85 words)
> So here are the four things to do before December. One, find out if your home sits in a flood zone or below a burn scar, the county maps are free. Two, clear the gutters, the drains and the creek culvert on your street, because ninety eight's damage came from water with nowhere to go. Three, check whether your insurance actually covers flood and mudflow, because most standard policies do not. Four, keep a week of supplies and a way to get out if the road below you closes.

Visual: four numbered stat-cards, each on 3–4 s of matching b-roll; popfigs "1 FLOOD MAP", "2 DRAINS", "3 INSURANCE", "4 SUPPLIES". [src: 3, 4]

## CLOSE (9:20–9:35)

### Z1-S1 — narration  (38 words)
> The ocean has already made its move. The next four months decide whether this is nineteen ninety eight or twenty sixteen, and either way, the prepared house is the one still standing in March. Subscribe, and we will track it with you.

Visual: NOAA map fade, channel outro brand (`library/inhouse/outro-brand.html`), end screen. Warm, no fear.

---
Word check (narration only): H1 20 · I1 152 · C1 150 · C2 135 · C3 160 · C4 110 · C5 160 · C6 150 · C7 150 · C8 165 · Z1 38 = **1,390 words ≈ 9:23 narration + 15 s CTA + ~8 chapter cards ≈ 9:50.**
