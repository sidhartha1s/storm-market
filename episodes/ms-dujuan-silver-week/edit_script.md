# edit_script.md — ms-dujuan-silver-week · "Typhoon No. 25 Dujuan Is Forming, Aimed at Japan's Biggest Holiday in 11 Years" (Format C, 16 Sep 26)

> Wave 3 U1, first video of the Dujuan daily series (ops/wave3/dujuan/PLAN.md). Angle = ideas-r3.md #1, Silver Week
> Collision, built to be honest under both open branches: the storm curving into Kanto, or sliding past offshore.
> Present-tense rolling update as of JMA 16 Sep 19:10 JST (TC2630, still an unnamed tropical depression) and JTWC
> warning 04, 16/09Z. Every number sourced to facts-16sep.md / fact-pack-16sep.md; nothing carries a [verify] tag.
> Numbers spelled out for TTS except years and dollar figures (humanise-rules.md); sentences under 24 words;
> wind spoken in mph, shown in km/h on screen; `[src]` per fact group. Target >=1,350 words at 1.10 tempo (8-min
> floor); measured at 1,374 words / approx 8:41 at the ms-kauai-lowell-day2 blended rate (158 wpm). Paul's CTA
> moved 17 Sep 26 (owner U1 comp fixes) to just before the close card, ~90% in, behind a new B8-S2 bridge line.

## Spec
- Slug `ms-dujuan-silver-week`. Voice: pocket-TTS Pharaoh -> atempo 1.10 -> transcribe the sped wav -> cues from
  that words.json. Probe-TTS "Dujuan" before final synthesis; if pocket-TTS doesn't land near "doo-jwan," respell
  the narration token phonetically and re-probe (storm-market homograph rule).
- Spoken names: Guam, Mariana Islands, Japan, Tokyo, Kanto, Nagoya, Yokosuka, Yokota, Dujuan.
  On screen only (not spoken): Ogasawara, Nozomi, Costa Serena.
- Pool: `library/mini-storms/dujuan-2026/` (built once in the main checkout, reused by every video in the series,
  per ops/wave3/dujuan/PLAN.md). Footage: NOAA/CIRA Himawari loops, JTWC/US Navy graphics, JMA bulletin graphics
  (credited), DVIDS Yokosuka/Yokota b-roll if available, short narrated broadcaster pulls (NHK/TBS/Reuters),
  Pexels/Pixabay Tokyo/Shinkansen/airport b-roll. No storm-chaser footage.
- MG: opening glassmorphic stat-card push + track map draw-on (B1/B2); meteorology explainer chip row (B2);
  four-checkpoint forecast track map (B3); quote card (B3); JTWC overlay + two labelled branch tracks (B4);
  Silver Week calendar + Nozomi/Asian Games chips (B5); US-bases Kanto map (B6); JMA-vs-NHC scale ladder graphic
  (B7); tracking/benchmark card (B8).
- Close: B8 ends on both open threads (track, strength) still unresolved; B9 is the single soft comment +
  subscribe line, tied to the real trigger event (Japan naming the storm), not an invented clock time.
- CTA: Paul's ebook CTA mounts at the end of B3 (approx 3:07, 36% in), right after the "East of Japan" quote card
  lands, the first natural pause in the meteorology block, ahead of the Silver Week pivot. 0.5 s dip in/out, film
  layer off, Paul circle hidden during the quote card per the presenter-circle spec.

## Sources
- f1 JMA live feed, TC2630 (targetTc.json -> specifications.json), fetched 16 Sep 2026, issue time 16 Sep 19:10
  JST: position, category (still TD), current intensity, and the four-point forecast track (+12h/+45h/+93h/+117h).
  https://www.jma.go.jp/bosai/typhoon/data/targetTc.json -- facts-16sep.md section 6.
- f2 JMA typhoon intensity scale (Strong / Very Strong / Violent Typhoon, Severe Tropical Storm band) and the
  10-minute-vs-1-minute sustained-wind conversion note, via Wikipedia "Tropical cyclone scales" citing RSMC
  Tokyo, fetched 16 Sep 2026 -- facts-16sep.md section 4.
- f3 Silver Week 2026 dates (19-23 Sep), first full 5-day Silver Week in 11 years (prior 2015, next 2032), 2026
  national-holiday count (16 to 17), Nozomi Shinkansen fully reserved-seat 18-23 Sep, peak congestion windows:
  Metropolis Japan, "Silver Week 2026 in Japan," 10 Sep 2026 -- facts-16sep.md section 2.
- f4 US Forces Japan: Fleet Activities Yokosuka (7th Fleet HQ) and Yokota Air Base (USFJ HQ) as established Kanto
  installations; approx 55,000 active-duty servicemembers at 15 bases Japan-wide; TCCOR readiness system
  (mechanism, not Dujuan-specific -- no TCCOR declared yet, storm still unnamed): Wikipedia "United States Forces
  Japan"; Stripes Japan TCCOR precedent -- facts-16sep.md section 3.
- f5 Kanto typhoon benchmarks: Typhoon Hagibis 2019 (139 dead, 3 missing, US$17.3B damage); Typhoon Faxai 2019
  (934,000 households without power, 390,000+ evacuation calls); Typhoon Ampil 2024 (4 injured Kanto-wide,
  minimal Tokyo damage): Wikipedia "Typhoon Hagibis" / "Typhoon Faxai" / "Typhoon Ampil (2024)" -- facts-16sep.md
  section 5.
- f6 Japan drew 42.7 million international visitors in 2025, its highest total on record: nippon.com, 23 Jan
  2026 -- facts-16sep.md section 3.
- f7 2026 Asian Games Aichi-Nagoya: opens 19 Sep, 46 nations, athletes' village includes the cruise ship Costa
  Serena docked in Nagoya housing at least 4,000 participants: Wikipedia "2026 Asian Games"; Marine Insight,
  16 Sep 2026 -- facts-16sep.md section 1.
- g1 JTWC TD 24W warning 04, 16/0900Z: position (277 nm ENE of Guam), current intensity (30 kt, gusts 40 kt),
  12/24/36h forecast (40/50/50 kt) with the turn toward Japan, peak forecast (65 kt, 19-21 Sep), closest pass
  approx 270 km (168 mi) east of Tokyo on 21 Sep, SST 29-30C, low shear, dry-air brake to the NW, 14 ft seas,
  GDACS green: fact-pack-16sep.md.

## B1 -- COLD OPEN (0:00-0:48)

### B1-S1 -- narration
> Right now, a tropical depression is spinning up near Guam, and Japan's biggest holiday in eleven years starts in three days. Japan's Meteorological Agency expects the system to earn a name within twelve hours. That name is Dujuan. Central pressure already sits at nine hundred ninety eight hectopascals. Sustained winds run thirty four miles per hour, gusting to fifty one. The agency's own longest forecast keeps this storm moving past Japan's main islands. That happens during the same five days when millions of Japanese travelers take their first full Silver Week in eleven years. Two outcomes are still open tonight. One track curves the storm into Kanto, the region that holds Tokyo. The other slides it by, offshore, weakened but still felt. Both possibilities remain in tonight's forecast. [f1, f3]

Visual: audio-first open on a NOAA/CIRA Himawari loop of the depression near Guam (wind ambience under the first line). Glassmorphic stat-card push over the loop, counting up: "TYPHOON No. 25 - 998 hPa - 34 MPH (JMA) / 35 MPH (JTWC)". Popfigs "998 hPa" - "3 DAYS" (to Silver Week). Track map begins to draw: JMA point (blue) and JTWC point (red) near Guam; two branch lines sketch faintly and unresolved (Branch A toward Kanto, Branch B offshore). Name card "DUJUAN" stamps in on cue.

## B2 -- WHERE THINGS STAND NOW (0:48-2:19)

### B2-S1 -- narration
> At seven ten Wednesday evening, Japan time, the storm sits near the Mariana Islands. It is moving north at nine miles per hour, a slow crawl for a system this size. Central pressure reads nine hundred ninety eight hectopascals. Sustained winds run thirty four miles per hour, with gusts to fifty one. The United States Navy's Joint Typhoon Warning Center tracks the same storm independently, southeast of Guam. Its own reading calls sustained winds thirty five miles per hour, gusting near forty six. Neither agency has given the storm a name yet. Its forecast has the storm strengthening fast. Winds reach forty six miles per hour within twelve hours, then fifty eight within a day. They hold near fifty eight for a day after that, before the model turns the storm north, aiming it toward Japan's main islands. Japan expects a slower climb. Sustained winds cross the tropical storm threshold within twelve hours. At that point, the system becomes this year's twenty fifth typhoon. Ocean water under the storm sits near eighty five degrees Fahrenheit, plenty warm enough to fuel more strengthening. Wind shear across the storm is low, another factor that lets storms grow stronger. The one likely brake is dry air moving in from the northwest. Waves near the center already reach fourteen feet. No populated coastline sits inside the storm's strongest wind field yet. Global disaster trackers still rate this system green, their lowest alert tier. [f1, g1]

Visual: split data panel, JMA card (998 hPa - 34 MPH - GUSTS 51 MPH) beside JTWC card (998 hPa - 35 MPH - GUSTS 46 MPH); motion arrow "9 MPH - NNE"; countdown chip "TS THRESHOLD: 12H -> TYPHOON No. 25". Meteorology explainer chip row lands on cue: "SST 85F" - "LOW WIND SHEAR" - "DRY AIR (NW) = BRAKE" - "SEAS 14 FT". GDACS badge, bottom corner: "ALERT LEVEL: GREEN - NO POPULATION IN CAT-1 WINDS".

## B3 -- THE FORECAST TRACK (2:19-3:07)

### B3-S1 -- narration
> Japan's forecast lays out four checkpoints between now and next Monday. Within twelve hours, sustained winds reach forty miles per hour and the storm earns its typhoon status. By Friday afternoon, central pressure drops to nine hundred eighty five hectopascals. Sustained winds climb to fifty six miles per hour. The storm is passing a remote island chain south of Tokyo at that point. By Sunday afternoon, the agency places the storm south of Japan. Pressure drops to nine hundred seventy five hectopascals, sustained winds climb to sixty seven miles per hour. Japan's longest published forecast, valid Monday afternoon, holds that same pressure. Sustained winds stay at sixty seven miles per hour, gusting to eighty nine. The agency's own words for that position are east of Japan. [f1]

Visual: four-checkpoint track map MG, JMA data, pins land on cue: "+12H - 40 MPH" - "FRI - 985 hPa / 56 MPH" (map label "OGASAWARA ISLANDS," not spoken) - "SUN - 975 hPa / 67 MPH" (map label "SOUTH OF JAPAN") - "MON - 975 hPa / 67-89 MPH GUST" (map label "EAST OF JAPAN"). Quote card mounts on the last line: "East of Japan" -- Japan Meteorological Agency, forecast valid 21 September, issued 16 September, 19:10 JST. Paul circle hidden during the card.

*(Paul's ebook CTA mounted here: 0.5 s dip in, 0.5 s out, film layer off. Story break, approx 3:07, 36% in.)*

## B4 -- TWO WAYS TO READ THE SAME STORM (3:07-3:49)

### B4-S1 -- narration
> That position sits offshore, past Japan's eastern coast, not over Tokyo itself. The United States Navy's Joint Typhoon Warning Center forecasts a stronger peak, seventy five miles per hour sustained, sometime between Saturday and Monday. Its own model puts the closest pass about one hundred sixty eight miles east of Tokyo, on Monday. Those two numbers describe the same storm two ways, and neither one is a landfall forecast. One outcome still has this storm curving back toward Kanto, later than either agency's current forecast reaches. The other has it doing exactly what both agencies show right now. It slides past, offshore, while Kanto still gets wind, rain, and rough surf. [f1, g1]

Visual: return to the track map; JTWC overlay track (red) with peak badge "75 MPH - JTWC PEAK, 19-21 SEP" and distance chip "168 MI EAST OF TOKYO". Two branch lines draw fully and label: "BRANCH A - TOWARD KANTO" / "BRANCH B - OFFSHORE PASS," both left unhighlighted, still open.

## B5 -- SILVER WEEK COLLISION (3:49-5:14)

### B5-S1 -- narration
> This storm's arrival collides with Japan's calendar in an unusual way. Saturday opens Japan's first full five-day Silver Week in eleven years, running through next Wednesday. The last one like it was 2015. The next one isn't until 2032. This holiday also pushes Japan's national holiday count for the year from sixteen to seventeen. In the United States, the closest comparison is a storm approaching over a Fourth of July or Labor Day weekend. Roads and airports on those weekends already sit at capacity. Japan Railways already reserved every seat on its flagship bullet train between Friday and next Wednesday. That retires the normal unreserved cars for the week. Rail operators expect the worst outbound crowding Friday evening and Saturday morning, and the worst return crowding next Wednesday. That decision was made before this storm existed, for the holiday crowd alone. On Saturday, the same day Silver Week begins, an international multi-sport event opens in Nagoya. Athletes from more than forty six nations are already competing there this week. Part of the host city's athletes' village, at least four thousand people, floats on a cruise ship in the harbor. Nagoya sits outside every track Japan's weather agency has published for this storm. Millions of people, already committed to trains, flights, and hotel bookings for this holiday, now watch a forecast that updates by the hour. [f3, f7]

Visual: Silver Week calendar MG, "SAT 19 - WED 23 SEP - FIRST FULL 5-DAY IN 11 YEARS"; chips "LAST: 2015 - NEXT: 2032" - "HOLIDAYS THIS YEAR: 16 -> 17"; literal US-calendar comparison graphic (July 4th / Labor Day travel icon, no metaphor). Nozomi chip, on-screen name only: "NOZOMI SHINKANSEN - FULLY RESERVED - 18-23 SEP" + "PEAK OUTBOUND: FRI PM / SAT AM - PEAK RETURN: WED". Asian Games chip: "ASIAN GAMES - NAGOYA - OPENS 19 SEP - 46+ NATIONS" + on-screen-only "COSTA SERENA - 4,000+ ABOARD". Footage: Silver Week travel stock/broadcast pulls, Shinkansen platform b-roll if in pool.

## B6 -- WHAT IT MEANS FOR AMERICANS (5:14-6:31)

### B6-S1 -- narration
> For Americans, these numbers matter beyond the weather map. Every hurricane season, Americans navigate this same kind of shifting forecast at home. This week, the same uncertainty sits over a different ocean, aimed at a different coast. Anyone flying into or out of Japan for Silver Week is booking travel for the same five days. Those are the same five days this storm is forecast to be nearest the country. Japan drew forty two point seven million international visitors last year, its highest total ever. Americans already traveling in Japan for the holiday face the same rail and flight uncertainty Japanese travelers do. The forecast they're checking is written in a language most of them don't speak. This storm's possible path runs through the Kanto region, home to two of the largest American military installations overseas. Fleet Activities Yokosuka is home port to the Seventh Fleet. Yokota Air Base is headquarters for United States Forces Japan. Across Japan, the United States keeps about fifty five thousand active-duty service members at fifteen major bases. Both Kanto bases use a standard readiness system for approaching typhoons, but neither has issued a storm-specific alert for this system. The storm has not been named yet. [f3, f4, f6]

Visual: US-hurricane-season parallel graphic (calendar overlay, literal, no metaphor); travel chip "42.7M VISITORS - 2025 - HIGHEST ON RECORD". Kanto/US-bases map MG: pins "FLEET ACTIVITIES YOKOSUKA - 7TH FLEET HQ" / "YOKOTA AB - USFJ HQ"; badge "APPROX 55,000 ACTIVE-DUTY - 15 BASES - JAPAN-WIDE"; status chip "NO STORM-SPECIFIC ALERT ISSUED YET".

## B7 -- HOW TO READ JAPAN'S NUMBERS (6:31-7:29)

### B7-S1 -- narration
> Japan and the United States measure typhoon winds differently, and that difference matters here. Japan's agency reports a ten-minute average wind. American forecasters report a one-minute average, which runs roughly twelve percent higher for the same storm. Japan's scale has three bands above typhoon strength. Strong Typhoon runs seventy four to ninety eight miles per hour. Very Strong runs ninety nine to one hundred twenty one. Violent starts above that. Right now, Japan's own longest forecast keeps Dujuan below all three, in the Severe Tropical Storm range, one full band under Strong. Using that twelve percent conversion, the forecast's sixty seven miles per hour sustained becomes roughly seventy five miles per hour. That is the American one-minute standard. That number sits right at the entry threshold for a category one hurricane. That is a translation, not a promise. Japan has not called this storm a hurricane, because Japan does not use that word. [f2]

Visual: JMA-vs-NHC scale comparison graphic, 10-MIN bar vs 1-MIN bar. Scale ladder card: "STRONG 74-98 MPH - VERY STRONG 99-121 MPH - VIOLENT 121+ MPH," Dujuan's forecast marker sitting below the ladder in a "SEVERE TROPICAL STORM" band. Conversion popfig "~75 MPH (1-MIN EQUIV.)" beside a "CATEGORY 1 THRESHOLD" marker line; caption chip "APPROXIMATION, NOT AN EQUIVALENCE".

## B8 -- WHAT'S STILL OPEN (7:29-8:29)

### B8-S1 -- narration
> Two things remain genuinely open tonight. The first is the track. Japan's own forecast ends offshore, east of Japan. A turn back toward Kanto is still possible beyond where that forecast currently reaches. The second is the storm's own strength. Every number tonight comes from a system that is not yet a typhoon. Three past storms near Kanto show how differently this can end. In 2019, Typhoon Hagibis killed one hundred thirty nine people. It also caused seventeen point three billion dollars in damage, the costliest typhoon in Japanese history by that measure. That same year, Typhoon Faxai left nine hundred thirty four thousand households without power. It also prompted evacuation calls for more than three hundred ninety thousand people. In 2024, Typhoon Ampil brushed the same coast and injured four. All three are real outcomes for a storm approaching this region. Which one Dujuan resembles is not yet knowable. Japan's weather agency updates this forecast again within hours. [f1, f5]

Visual: tracking card MG, two rows: "TRACK - STILL OPEN" / "STRENGTH - STILL OPEN". Benchmark comparison chips: "HAGIBIS 2019 - 139 DEAD - $17.3B" - "FAXAI 2019 - 934,000 OUT - 390,000+ EVACUATED" - "AMPIL 2024 - 4 INJURED". Return to the live Himawari loop of Dujuan.

## B9 -- CLOSE (8:29-8:41)

### B9-S1 -- narration
> Tell me in the comments where you're watching from, in Japan or anywhere else this storm might reach. Subscribe, and the next update lands the moment Japan gives this storm its name.

Visual: close card ("Dujuan. Forming near Guam. Silver Week begins Saturday." / soft line / brand), Paul circle hidden.
