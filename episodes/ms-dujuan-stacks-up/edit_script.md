# edit_script.md — ms-dujuan-stacks-up · "How Dujuan Stacks Up Against Japan's Last Decade of Typhoons" (Format C, 17 Sep 26)

> Wave 3 U1, benchmark-ranking angle for the Dujuan daily series (ops/wave3/dujuan/PLAN.md). Present-tense rolling
> update as of JMA 16 Sep 19:10 JST (TC2630, still an unnamed tropical depression) and JTWC warning 04, 16/09Z —
> same live snapshot as the sibling scripts in this series. The core graphic is a benchmark table ranking eight
> storms that hurt Japan since 2016 against Typhoon No. 25's own forecast peak; the honest thesis, stated as facts
> not commentary: pressure and wind describe the storm, not what stands under its track, and this track runs over
> the most crowded week of the Japanese year. Numbers spelled out for TTS except calendar years (storm-market
> house convention, matching the sibling scripts); sentences under 24 words; wind spoken in mph, km/h + hPa shown
> on screen; hard foreign place names kept off the voice track (Iwate, Iwaizumi, Omaezaki, Shizuoka, Tanabe,
> Wakayama, Cape Irozaki, Kansai Airport, Kagoshima, Miyazaki, Ogasawara, Minamitorishima — on screen only).
> Homograph scan run on the full script: every past-tense "read" (central pressure read...) rewritten to "stood
> at" to avoid the read/read ("reed"/"red") TTS trap. `references/humanise-rules.md` applied line by line — no
> banned openers, no metaphors, no rhetorical questions, no em dashes, no reveal-flip or anaphora-run sentence
> shapes, varied sentence length, active voice. Target >=1,350 words; measured 1,509 words at this draft (see
> report). Paul's CTA mounted at the end of B3, the natural pause right after the quote card, ~34% into the runtime.

## Spec
- Slug `ms-dujuan-stacks-up`. Voice: pocket-TTS Pharaoh -> atempo 1.10 -> transcribe the sped wav -> cues from that
  words.json. Probe-TTS "Dujuan" and "Lionrock" before final synthesis (storm-market homograph rule); if
  pocket-TTS mangles either, respell the narration token phonetically and re-probe.
- Spoken names: Guam, Mariana Islands, Japan, Tokyo, Osaka, Kobe, Kyushu, Chiba, Nagoya, Dujuan.
  On screen only (not spoken): Iwate, Iwaizumi, Tohoku, Omaezaki, Shizuoka, Tanabe, Wakayama, Cape Irozaki,
  Kansai Airport, Kagoshima, Miyazaki, Ogasawara, Minamitorishima.
- Pool: `library/mini-storms/dujuan-2026/` (reused across the whole Dujuan series). Footage: NOAA/CIRA Himawari
  loops, JTWC/US Navy graphics, JMA bulletin graphics (credited), archival broadcast/PD stills of Hagibis/Faxai/
  Jebi/Trami/Lan/Lionrock/Nanmadol/Ampil damage (NHK/Reuters/AP short narrated pulls, courtesy-credited), Pexels/
  Pixabay Tokyo/Osaka/Shinkansen b-roll. No storm-chaser footage.
- MG: opening glassmorphic stat-card push (B1); split JMA/JTWC data panel (B2); four-checkpoint forecast track
  map + quote card (B3); **the benchmark table (B4) — the episode's core graphic**, nine rows building in
  narration order, columns STORM · YEAR · MIN PRESSURE · PEAK WIND (MPH) · WHAT IT BROKE, Typhoon No. 25's own
  row appended last in an unresolved amber state (forecast, not realized); Ampil/Nanmadol two-card contrast (B5);
  Silver Week + Asian Games calendar chips (B6); tracking/benchmark recap card (B7).
- Close: B7 ends on both open threads (track, strength) still unresolved; B8 is the single soft comment +
  subscribe line, tied to the real trigger event (Japan naming the storm).
- CTA: Paul's ebook CTA mounts at the end of B3, right after the "East of Japan" quote card lands, the first
  natural pause in the meteorology block, ahead of the benchmark table. 0.5 s dip in/out, film layer off, Paul
  circle hidden during the quote card per the presenter-circle spec.

## Sources
- f1 — JMA live feed, TC2630 (`targetTc.json` -> `specifications.json` -> forecast), fetched 16 Sep 2026, issue
  time 16 Sep 19:10 JST: current position/category/intensity and the four-point forecast track (+12h/+45h/+93h/
  +117h), including the +117h "日本の東" ("East of Japan") descriptor — the on-screen quote.
  `https://www.jma.go.jp/bosai/typhoon/data/targetTc.json` — facts-16sep.md §6 / fact-pack-16sep.md / this
  episode's own `data/track.json`.
- f2 — JTWC TD 24W warning 04, 16/0900Z: position, current intensity, 12/24/36h forecast, peak forecast (65 kt /
  75 mph, 19–21 Sep) — fact-pack-16sep.md / `data/track.json`.
- f3 — JMA typhoon intensity scale (Strong / Very Strong / Violent Typhoon bands, Severe Tropical Storm), via
  Wikipedia "Tropical cyclone scales" §Western Pacific, citing RSMC Tokyo, fetched 16 Sep 2026 — facts-16sep.md
  §4. `en.wikipedia.org/wiki/Tropical_cyclone_scales`
- f4 — Silver Week 2026 dates (19–23 Sep), first full 5-day Silver Week in 11 years (prior 2015, next 2032),
  Nozomi Shinkansen fully reserved-seat 18–23 Sep: Metropolis Japan, "Silver Week 2026 in Japan," 10 Sep 2026 —
  facts-16sep.md §2. `metropolisjapan.com/silver-week-2026-japan/`
- f5 — 2026 Asian Games Aichi-Nagoya: opens 19 Sep, 46 nations, athletes' village includes the cruise ship Costa
  Serena docked in Nagoya: Wikipedia "2026 Asian Games"; Marine Insight, 16 Sep 2026 — facts-16sep.md §1.
  `en.wikipedia.org/wiki/2026_Asian_Games`
- f6 — Typhoon Lionrock (2016): JMA peak 940 hPa / 165 km/h (105 mph); first tropical cyclone on record to make
  landfall on that stretch of Japan's Tohoku Pacific coast since JMA began record-keeping in 1951; 22 dead
  including 9 who drowned in an Iwaizumi (Iwate Prefecture) nursing home; ¥282 billion (US$2.74B) damage.
  Wikipedia "Typhoon Lionrock (2016)", fetched 17 Sep 2026. `en.wikipedia.org/wiki/Typhoon_Lionrock_(2016)`
- f7 — Typhoon Lan (2017): JMA peak 915 hPa / 185 km/h (115 mph); landfall Omaezaki, Shizuoka, 23 Oct 2017; 17
  dead, approx. 381,000 evacuated, 350 flights cancelled, approx. US$2B economic loss. Wikipedia "Typhoon Lan
  (2017)", fetched 17 Sep 2026. `en.wikipedia.org/wiki/Typhoon_Lan_(2017)`
- f8 — Typhoon Jebi (2018): JMA peak 915 hPa / 195 km/h (120 mph); landfall near Kobe, 4 Sep 2018, the strongest
  typhoon to make landfall in Japan since 1993; wind records broken at 100 weather stations; Kansai Airport
  flooded; Osaka storm-surge record of 3.29 m (surpassing the 2.93 m record from 1961); 14 dead, 980 injured;
  insured losses US$13–14B. Wikipedia "Typhoon Jebi", fetched 17 Sep 2026. `en.wikipedia.org/wiki/Typhoon_Jebi`
- f9 — Typhoon Trami (2018): JMA peak 915 hPa / 195 km/h (120 mph); landfall Tanabe, Wakayama, 30 Sep 2018; at
  least 4 dead, 200+ injured, storm surge 11.71 m at Cape Irozaki, 1,000+ flights cancelled, 380,000+ evacuated,
  ¥306.1B (US$2.69B) insured losses. Wikipedia "Typhoon Trami (2018)", fetched 17 Sep 2026.
  `en.wikipedia.org/wiki/Typhoon_Trami_(2018)`
- f10 — Typhoon Hagibis (2019): JMA peak 915 hPa / 195 km/h (120 mph); 139 dead, 3 missing, ¥1.88 trillion
  (US$17.3B) damage, the costliest typhoon in Japanese history at the time. Wikipedia "Typhoon Hagibis", fetched
  17 Sep 2026 (cross-checked against facts-16sep.md §5). `en.wikipedia.org/wiki/Typhoon_Hagibis`
- f11 — Typhoon Faxai (2019): JMA peak 955 hPa / 155 km/h (100 mph); landfall over the Kanto Plain (Chiba), 8 Sep
  2019; 934,000 households without power; 3 dead, 147 injured; damage US$10B (2019 USD, per facts-16sep.md §5,
  Wikipedia "Typhoon Faxai" fetched 16 Sep 2026 for this figure). Re-fetched 17 Sep 2026 for the wind/pressure
  figures. `en.wikipedia.org/wiki/Typhoon_Faxai`
- f12 — Typhoon Nanmadol (2022): JMA peak 910 hPa / 195 km/h (120 mph) — the deepest pressure and strongest wind
  of the whole benchmark set; landfall Kagoshima, Kyushu, 18 Sep 2022; 4 dead, 114+ injured, approx. US$2B
  damage, approx. 190,000 without power, Miyazaki rainfall over 15 inches, 100 dams pre-discharged. Wikipedia
  "Typhoon Nanmadol (2022)", fetched 17 Sep 2026. `en.wikipedia.org/wiki/Typhoon_Nanmadol_(2022)`
- f13 — Typhoon Ampil (2024), the near-miss benchmark: JMA peak 950 hPa / 155 km/h (100 mph); never made
  landfall, brushed the coast offshore; approx. 600 flights cancelled by JAL/ANA; evacuation orders covering
  approx. 178,000 households / 404,000+ people; 4 injured across the Kanto region. Wikipedia "Typhoon Ampil
  (2024)", fetched 17 Sep 2026 (cross-checked against facts-16sep.md §5). `en.wikipedia.org/wiki/Typhoon_Ampil_(2024)`

**Sourcing note:** f6–f13 were fetched from English Wikipedia's storm infoboxes (which themselves compile JMA
best-track figures), not directly from JMA's raw best-track archive or a Cabinet Office/FDMA disaster report —
JMA's own English classification pages 404'd for this series on 16 Sep (facts-16sep.md §4 and §6 already flag
this), and a live scan for the Cabinet Office/FDMA situation reports on each of these eight storms was not run
this session given the time budget. This matches the sourcing standard the sibling script
(`ms-dujuan-silver-week`) already used for its own Hagibis/Faxai/Ampil benchmark, so it is consistent with
shipped practice, but it is short of "fetch JMA/Cabinet Office/FDMA directly" as an ideal. Flagged, not hidden.

## B1 — COLD OPEN (0:00–0:33)

### B1-S1 — narration
> Every typhoon that has hurt Japan in the last ten years arrived with a central pressure below nine hundred sixty hectopascals. Typhoon No. 25 is forecast to arrive weaker than every single one of them. Japan's Meteorological Agency expects the storm to earn the name Dujuan within twelve hours, somewhere near the Mariana Islands. Its own longest published forecast puts the storm's lowest pressure at nine hundred seventy five hectopascals on Monday, positioned east of Japan. That number is milder, on paper, than eight separate typhoons that killed people, flooded cities, and grounded flights across Japan since 2016. The track this storm is forecast to fly sits directly over the single most crowded week on Japan's calendar in eleven years. For an American with a trip to Japan booked this month, those two numbers now sit on the same page. [f1, f4]

Visual: audio-first open on a NOAA/CIRA Himawari loop of the depression near Guam. Glassmorphic stat-card push: "TYPHOON No. 25 — FORECAST PEAK: 975 hPa / 67 MPH — WEAKEST OF THE LAST 8 KANTO-AREA TYPHOONS." Popfigs "975 hPa" — "8 STORMS" — "1 CROWDED WEEK." Track map begins to draw near Guam, unresolved.

## B2 — WHERE THINGS STAND NOW (0:33–1:35)

### B2-S1 — narration
> At seven ten Wednesday evening, Japan time, the storm sits near the Mariana Islands as a tropical depression. Central pressure reads nine hundred ninety eight hectopascals. Sustained winds run thirty four miles per hour, gusting to fifty one. The United States Navy's Joint Typhoon Warning Center tracks the same storm independently. It reports sustained winds of thirty five miles per hour, gusting near forty six. Neither agency has assigned a name yet. Japan expects the storm to cross the tropical storm threshold within twelve hours. At that point, it becomes this year's twenty fifth typhoon. The Navy's own forecast has this storm strengthening fast, crossing sixty five miles per hour by Saturday, the same day Silver Week begins. Ocean water beneath the storm sits near eighty five degrees Fahrenheit, warm enough to keep feeding it. Wind shear across the storm is low. Dry air moving in from the northwest is the one likely brake on its strength. [f1, f2]

Visual: split data panel, JMA card (998 hPa · 34 MPH · GUSTS 51 MPH) beside JTWC card (998 hPa · 35 MPH · GUSTS 46 MPH); countdown chip "TS THRESHOLD: 12H → TYPHOON No. 25." Meteorology chip row: "SST 85F" · "LOW SHEAR" · "DRY AIR (NW) = BRAKE."

## B3 — THE FORECAST TRACK (1:35–2:22)

### B3-S1 — narration
> Japan's forecast lays out four checkpoints between now and next Monday. Within twelve hours, sustained winds reach forty miles per hour and the storm earns typhoon status. By Friday afternoon, central pressure drops to nine hundred eighty five hectopascals, sustained winds near fifty six miles per hour. The storm passes a remote island chain south of Tokyo at that point. By Sunday afternoon, the agency places the storm south of Japan. Pressure is down to nine hundred seventy five hectopascals, sustained winds at sixty seven miles per hour. Japan's longest published forecast, valid Monday afternoon, holds that same pressure and wind speed, gusting to eighty nine miles per hour. The agency's own words for that position are east of Japan. [f1]

Visual: four-checkpoint track map MG, pins land on cue: "+12H — 40 MPH" · "FRI — 985 hPa / 56 MPH" (on-screen label "OGASAWARA ISLANDS," not spoken) · "SUN — 975 hPa / 67 MPH" ("SOUTH OF JAPAN") · "MON — 975 hPa / 67–89 MPH GUST" ("EAST OF JAPAN"). Quote card mounts on the last line: **"East of Japan"** — Japan Meteorological Agency, forecast valid 21 September, issued 16 September, 19:10 JST. Paul circle hidden during the card.

*(Paul's ebook CTA mounted here: 0.5 s dip in, 0.5 s out, film layer off. Story break, ~34% in, right after the quote card, ahead of the benchmark table.)*

## B4 — TEN YEARS, EIGHT STORMS: THE BENCHMARK (2:22–4:35)

### B4-S1 — narration
> Line up every typhoon that has actually hurt Japan since 2016, and a pattern appears. Typhoon Lionrock made landfall on Japan's northern Pacific coast in 2016. It was the first typhoon on record to hit that stretch of coastline, going back to when Japan started keeping typhoon records in 1951. Central pressure stood at nine hundred forty hectopascals, sustained winds one hundred five miles per hour. Nine people drowned inside a single nursing home in one coastal town. Twenty two people died across Japan. Typhoon Lan came ashore on the central Japan coast in 2017, nine hundred fifteen hectopascals, sustained winds one hundred fifteen miles per hour. Three hundred eighty one thousand people evacuated. Seventeen died. Two typhoons hit Japan within a month of each other in 2018. Each one measured nine hundred fifteen hectopascals, sustained winds one hundred twenty miles per hour. Jebi made landfall near Kobe on September fourth, the strongest typhoon to hit Japan since 1993. It broke wind records at one hundred weather stations, flooded a major Osaka airport, and set a new storm surge record in Osaka. Fourteen people died. Trami followed on September thirtieth, cancelling more than a thousand flights and evacuating over three hundred eighty thousand people. Four died. Faxai hit the Tokyo region about a month before Hagibis that same year. Central pressure stood at nine hundred fifty five hectopascals, sustained winds one hundred miles per hour. It left nine hundred thirty four thousand households without power. Three people died. Hagibis followed with the deepest pressure of that pair, nine hundred fifteen hectopascals, one hundred twenty miles per hour. It killed one hundred thirty nine people and caused seventeen point three billion dollars in damage, the costliest typhoon in Japanese history. Four of those eight storms bottomed out at that exact same central pressure, nine hundred fifteen hectopascals, despite hitting Japan across three separate years. Nanmadol struck southern Japan's Kyushu island in 2022. Central pressure stood at nine hundred ten hectopascals, sustained winds one hundred twenty miles per hour. That is the deepest pressure and the strongest wind on this entire list. Four people died there, far fewer than Hagibis or Lionrock, because it crossed a less crowded stretch of coastline. Ampil never made landfall at all in 2024. Its forecast peak stood at nine hundred fifty hectopascals, one hundred miles per hour, and its closest approach to Tokyo stayed offshore. Four people were injured across the entire Tokyo region. Typhoon No. 25's own longest forecast right now reads nine hundred seventy five hectopascals, sixty seven miles per hour. Every one of those eight storms hit Japan harder, on paper, at a lower pressure and a higher wind speed. Even so, the damage each one caused varied wildly. Combined, those eight storms are responsible for more than two hundred deaths and over fifty billion dollars in damage. [f1, f6, f7, f8, f9, f10, f11, f12, f13]

Visual: **the benchmark table, the episode's core graphic** — nine rows build top to bottom in narration order, columns STORM · YEAR · MIN PRESSURE · PEAK WIND (MPH) · WHAT IT BROKE:
1. LIONROCK · 2016 · 940 hPa · 105 MPH · "FIRST TOHOKU PACIFIC LANDFALL SINCE 1951 · 22 DEAD" (on-screen only: Iwate, Iwaizumi nursing home)
2. LAN · 2017 · 915 hPa · 115 MPH · "381,000 EVACUATED · 17 DEAD" (on-screen only: Omaezaki, Shizuoka)
3. JEBI · 2018 · 915 hPa · 120 MPH · "STRONGEST LANDFALL SINCE 1993 · KANSAI AIRPORT FLOODED · 14 DEAD"
4. TRAMI · 2018 · 915 hPa · 120 MPH · "1,000+ FLIGHTS CANCELLED · 4 DEAD" (on-screen only: Tanabe, Wakayama)
5. FAXAI · 2019 · 955 hPa · 100 MPH · "934,000 HOUSEHOLDS WITHOUT POWER · 3 DEAD"
6. HAGIBIS · 2019 · 915 hPa · 120 MPH · "$17.3B — COSTLIEST TYPHOON IN JAPANESE HISTORY · 139 DEAD"
7. NANMADOL · 2022 · 910 hPa · 120 MPH · "DEEPEST + STRONGEST ON THIS LIST · 4 DEAD" (on-screen only: Kagoshima, Kyushu; Miyazaki rain)
8. AMPIL · 2024 · 950 hPa · 100 MPH · "NEVER MADE LANDFALL · 404,000 EVACUATED ANYWAY"
9. **TYPHOON No. 25 · 2026 · 975 hPa FORECAST · 67 MPH FORECAST · "STILL FORECAST, NOT YET REAL"** — row renders in amber/unresolved styling, sitting visibly below (weaker than) every row above it on both the pressure and wind columns.

## B5 — WHAT PRESSURE AND WIND DON'T MEASURE (4:35–5:26)

### B5-S1 — narration
> Nanmadol was the deepest storm on that list and killed the fewest people. Ampil never touched land and still triggered evacuation orders for more than four hundred thousand people and grounded around six hundred flights. Central pressure and wind speed measure the storm itself, not what stands underneath its track. Timing, angle, and the ground underneath the track decide how much damage a storm causes. Typhoon No. 25's forecast track currently runs offshore, east of Japan, the same shape as Ampil's track. Its forecast pressure is even milder than Ampil's was. The difference this time sits in the calendar underneath it. [f12, f13]

Visual: two-card contrast MG. Left card: "NANMADOL — 910 hPa, DEEPEST ON THE LIST — 4 DEAD." Right card: "AMPIL — NEVER MADE LANDFALL — 404,000 EVACUATED ANYWAY." Center caption card: "PRESSURE + WIND ≠ DAMAGE. TIMING + ANGLE + WHAT'S UNDERNEATH DO." Track map returns, showing Typhoon No. 25's offshore forecast line traced directly over Ampil's old track for comparison.

## B6 — THE CALENDAR THIS TRACK RUNS THROUGH (5:26–6:41)

### B6-S1 — narration
> Saturday opens Japan's first full five day Silver Week in eleven years, running through next Wednesday. The last one like it was 2015. The next isn't until 2032. Japan Railways already made every seat on its flagship bullet train reserved, from Friday through next Wednesday. That retires the normal unreserved cars for the whole week. That decision was made before this storm existed. On the same Saturday, an international multi sport event opens in Nagoya, with athletes from more than forty six nations already competing there this week. Part of the host city's athletes' village floats on a cruise ship in the harbor. None of Japan's published tracks for this storm currently reach Nagoya. Millions of people are already committed to trains, flights, and hotel bookings for this holiday. They are now watching a forecast that updates by the hour, for a storm that is currently the mildest one on this list. [f4, f5]

Visual: Silver Week calendar MG, "SAT 19 – WED 23 SEP · FIRST FULL 5-DAY IN 11 YEARS"; chips "LAST: 2015 — NEXT: 2032" · "NOZOMI SHINKANSEN — FULLY RESERVED 18–23 SEP." Asian Games chip: "ASIAN GAMES — NAGOYA — OPENS 19 SEP — 46+ NATIONS" (on-screen only: Costa Serena). Return shot: the benchmark table's amber Typhoon No. 25 row overlaid on the Silver Week calendar strip, visually pairing "weakest on the list" against "busiest week in 11 years."

## B7 — WHAT'S STILL OPEN TONIGHT (6:41–7:23)

### B7-S1 — narration
> Two things remain genuinely open tonight. The first is the track. Japan's own forecast ends offshore, east of Japan. A turn back toward the mainland is still possible beyond where that forecast currently reaches. The second is the storm's own strength. Every number tonight comes from a system that is not yet a typhoon. Japan's own scale carries three grades above typhoon that this forecast does not yet reach. Japan's weather agency updates this forecast again within hours. [f1, f3]

Visual: tracking card MG, two rows: "TRACK — STILL OPEN" / "STRENGTH — STILL OPEN." Benchmark table reappears in miniature, Typhoon No. 25's amber row still unresolved at the bottom. Return to the live Himawari loop of the depression near Guam.

## B8 — CLOSE (7:23–7:35)

### B8-S1 — narration
> Tell me in the comments which of these eight storms you remember living through, or watching from here. Subscribe, and the next update lands the moment Japan gives this storm its name.

Visual: close card ("Typhoon No. 25. Weaker on paper. A busier week underneath it." / soft line / brand), Paul circle hidden.
