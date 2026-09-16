# edit_script.md — ms-dujuan-alert-levels · "Japan's Five-Level Evacuation Alert System, Explained for Americans" (mini-storms, evergreen, v1 17 Sep 26)

> Evergreen civics/hazard-communication explainer for The Warning Hour's Dujuan series, doubling as a 17 Sep
> update. Every live-storm number is anchored to JMA's 16 Sep 19:10 JST advisory for the still-unnamed tropical
> depression near the Mariana Islands (facts-16sep.md §6 / fact-pack-16sep.md), which was still the governing
> forecast as of this write. The core subject — Japan's five-level Alert Level system (Cabinet Office, revised 20
> May 2021) and JMA's matching Warning/Advisory tiers — is fetched fresh this session directly from bousai.go.jp
> and jma.go.jp (see Sources). Numbers spelled out for TTS except years and dollar figures; sentences under 24
> words; wind spoken in mph, km/h added on screen only; humanise-rules.md pass applied line by line (no banned
> openers/words/phrases, no metaphors, no rhetorical questions, no em dashes, no reveal-flip or mirrored-callback
> endings). No hard-to-pronounce untransliterated Japanese names required this episode. Target >=1,350 words.

## Spec
- Slug `ms-dujuan-alert-levels`. Voice: pocket-TTS Pharaoh -> atempo 1.10 -> transcribe the sped wav -> cues from
  that words.json (probe-TTS before final synthesis per the storm-market homograph rule; scan narration for
  read/lead/live/wind/close/present/record before TTS — this draft avoids "read," "present," and "record" as
  verbs entirely and uses "wind" only as the meteorological noun, so no respelling is expected to be needed, but
  the probe-and-listen step still applies).
- Spoken names: Japan, Tokyo, Kanto, Guam, Mariana Islands. No untransliterated Japanese place names or storm
  name needed — the storm is still unnamed in JMA's own feed this session, so narration says "this storm"
  throughout, matching the ms-dujuan-jma-vs-nhc precedent.
- Pool: `library/mini-storms/dujuan-2026/` (reused across the Dujuan series). Footage: NOAA/CIRA Himawari loops,
  JMA bulletin graphics, Cabinet Office (bousai.go.jp) poster graphic recreated as an in-house MG (source
  material is a static translated poster, not licensable stock — rebuild the ladder as an original graphic,
  crediting Cabinet Office/Government of Japan on screen), NWS/NHC graphics, Japan travel/Silver Week b-roll if
  in pool. No storm-chaser footage.
- MG: opening Himawari loop + stat-card push (B1); JMA/JTWC split data panel (B2); five-level ladder graphic,
  built once in B3, referenced again in B4-B7 with the active level highlighted (Cabinet Office sourced, redrawn
  in-house); "OLD SYSTEM -> NEW SYSTEM" two-column card (B3); quote card (B5, the one named official quote);
  US-side comparison chip row, hurricane watch/warning timeline (B7); ladder-with-marker "WHERE THIS STORM SITS
  TONIGHT" card (B8); tracking card (B9).
- Close: B9 ends on both open threads (track, strength) still unresolved, plus the live travel-season stake;
  B10 is the single soft comment + subscribe line.
- CTA: Paul's ebook CTA mounts at the end of B3 (approx 3:05 of ~9:50, 31% in), the natural pause right after the
  "old system retired" card and before the level-by-level breakdown begins. 0.5 s dip in/out, film layer off.

## Sources
- f1 — facts-16sep.md §6 / live JMA feed, TC2630 (`targetTc.json` -> `TC2630/specifications.json`), fetched 16
  Sep 2026, issue time 16 Sep 19:10 JST: still a tropical depression, position near the Mariana Islands, central
  pressure, current intensity, and the longest (+117h) forecast track/intensity, valid 21 Sep 15:00 JST, "East of
  Japan." `https://www.jma.go.jp/bosai/typhoon/data/targetTc.json`
- g1 — fact-pack-16sep.md / JTWC TD 24W warning 04, 16/0900Z: independent US Navy reading, current intensity and
  short-range forecast, cross-checked against f1.
- f3 — facts-16sep.md §2, Silver Week 2026 dates and significance (Metropolis Japan, 10 Sep 2026), used lightly
  in B9 for stakes, not re-explained in full (this episode stands alone; the Silver Week collision is the
  subject of a separate video in the series).
- j1 — Cabinet Office, Government of Japan, "Evacuation Information (Revised Version)" — official English-
  language poster (translation of the original Japanese), effective from 20 May 2021, fetched via curl 17 Sep
  2026: the five-level Alert Level ladder, the retired two-tier "Recommendation / Instruction (Emergency)"
  system it replaced, and Notes 1-3 on Levels 3-5.
  `https://www.bousai.go.jp/oukyu/hinanjouhou/r3_hinanjouhou_guideline/pdf/EN_omote.pdf`
- j2 — Japan Meteorological Agency, "Emergency Warning System" (English page), fetched via curl 17 Sep 2026: the
  Level 2 Advisory / Level 3 Warning / Level 4 Urgent Warning / Level 5 Emergency Warning tiers for heavy rain,
  flood, landslide, and storm surge; the exact-quote guidance for Levels 3 and 4; and the note that JMA
  reorganized these Warnings/Advisories by disaster type in 2026, printing the Alert Level number directly into
  the warning's own name. `https://www.jma.go.jp/jma/en/Emergency_Warning/ew_index.html`
- n1 — NOAA National Hurricane Center / National Weather Service, "Hurricane and Tropical Storm Watches,
  Warnings, Advisories and Outlooks," fetched via curl 17 Sep 2026: Hurricane Watch (issued 48 hours before
  anticipated tropical-storm-force winds), Hurricane Warning (issued 36 hours before), and the Extreme Wind
  Warning (extreme sustained winds of a major hurricane, 115 mph or greater, expected within the hour; take
  immediate shelter). `https://www.weather.gov/safety/hurricane-ww`

## B1 — COLD OPEN (0:00–0:52)

### B1-S1 — narration

> Right now, a tropical depression sits near Guam, and Japan's weather agency has already mapped this storm's path for the next five days. Central pressure holds at nine hundred ninety eight hectopascals. Sustained winds run thirty four miles per hour, gusting to fifty one. If this storm strengthens the way that forecast shows, Japanese officials will not call it a hurricane watch, and they will not call it a hurricane warning. Japan runs its own five-level alert system for exactly this moment, built after an older version confused too many people at the worst time. One of its five levels tells only the elderly and people with disabilities to leave first. Another exists for the moment leaving home becomes more dangerous than staying inside it. Tonight, that ladder, not the wind speed by itself, decides what Japanese officials tell millions of residents to do next. [f1]

Visual: audio-first open on a NOAA/CIRA Himawari loop of the depression near Guam. Glassmorphic stat-card push over the loop: "998 hPa" · "34 MPH · 55 KM/H" · "GUSTS 51 MPH · 83 KM/H". News bug: "JAPAN'S ALERT LEVELS · EXPLAINED FOR AMERICANS." Popfig "5 LEVELS."

## B2 — WHERE THE STORM STANDS RIGHT NOW (0:52–1:45)

### B2-S1 — narration

> At the latest advisory, the storm sits near the Mariana Islands, moving north-northeast at nine miles per hour. The United States Navy's Joint Typhoon Warning Center tracks the same system independently and puts its sustained winds at thirty five miles per hour, gusting near forty six. Neither agency calls this a typhoon yet. Japan's own forecast has the storm crossing the tropical storm threshold within twelve hours, becoming this year's twenty fifth named system once it does. Ocean water beneath the storm sits near eighty five degrees Fahrenheit, warm enough to keep feeding it. That same forecast, run all the way out to its five-day limit, still keeps the storm in open water east of Japan, not over any city. That single detail already matters for which Japanese alert level applies here, because right now, none has been issued. [f1, g1]

Visual: split data panel, JMA card ("998 hPa · 34 MPH · 55 KM/H") beside JTWC card ("35 MPH · 56 KM/H · GUSTS 46 MPH · 74 KM/H"); motion arrow "9 MPH · 15 KM/H · NNE"; countdown chip "TS THRESHOLD: 12H." Meteorology chip: "SST 85°F." Status chip, bottom corner: "NO ALERT LEVEL ISSUED YET."

## B3 — THE SYSTEM JAPAN BUILT (1:45–3:05)

### B3-S1 — narration

> Japan changed this entire alert system in May of 2021. Before that, two separate advisories asked residents to leave: one called a Recommendation, one called an Instruction. Officials found that people often waited past the first advisory because the word sounded optional, not urgent. The new system retired both and replaced them with a single ladder, five levels, numbered one through five, issued by the local municipality rather than the weather agency alone. Levels one and two carry no evacuation order at all. Level one covers rising risk of bad weather over the coming days. Level two lines up with Japan's weather agency issuing a heavy rain, flood, or storm surge advisory, the same tier an American forecaster would simply call an advisory, not a watch. Neither level tells anyone to leave home. The ladder only starts giving evacuation orders at level three, and that is where the real differences with the American system begin. [j1, j2]

Visual: "OLD SYSTEM → NEW SYSTEM" two-column card: old = "Recommendation / Instruction (Emergency)," new = "5-Level Alert Ladder, 20 May 2021." Five-level ladder MG builds for the first time, levels 1-2 highlighted, 3-5 dimmed: "1 · RISING RISK" / "2 · ADVISORY ISSUED (JMA)." Credit line, small: "Source: Cabinet Office, Government of Japan."

*(Paul's ebook CTA mounted here: 0.5 s dip in, 0.5 s out, film layer off. Story break, approx 3:05, 31% in.)*

## B4 — LEVEL THREE: THE ELDERLY EVACUATE FIRST (3:05–4:00)

### B4-S1 — narration

> Level three is named Evacuation of the Elderly and Others. Japan's own guidance names the group directly: elderly residents, people with disabilities, and anyone who may need extra time to leave safely. The instruction tells that group to evacuate immediately, while everyone else in the area only prepares to leave. The United States has no matching national alert level for this. Some American counties issue an early, voluntary evacuation order ahead of a mandatory one, aimed at roughly the same population, but no federal system assigns that order a number the way Japan does. A Japanese level three during this storm would tell an American resident in Tokyo something specific and immediate: leave now if leaving quickly is hard for you, and get ready if it is not. [j1, j2]

Visual: ladder MG returns, level 3 highlighted, others dimmed: "3 · EVACUATION OF THE ELDERLY, ETC." Chip: "US EQUIVALENT: NO FEDERAL MATCH · SOME COUNTIES: EARLY VOLUNTARY ORDER." Silhouette icon row (elderly, wheelchair user, cane) per the source poster's own iconography, redrawn.

## B5 — LEVEL FOUR: EVERYONE EVACUATES (4:00–5:12)

### B5-S1 — narration

> Level four is called an Evacuation Instruction, and it fully replaced the old Recommendation. Japan's Cabinet Office states it in one line: evacuate before level four is even issued, not after. Japan's weather agency backs that instruction with its own Urgent Warning, and its guidance for that warning reads, in the agency's own words, quote, all residents should evacuate from dangerous areas, end quote. That line is the closest match anywhere in this system to an American mandatory evacuation order. The difference sits underneath the label. In Japan, the municipality's evacuation order and the weather agency's warning are built to trigger together, by policy. In the United States, the National Hurricane Center issues a hurricane warning as a wind forecast, thirty six hours before tropical-storm-force winds arrive, and a mayor or a governor issues the evacuation order on a separate, independent timeline. Two systems doing similar work, never formally linked to each other. [j1, j2, n1]

Visual: **quote card (the one named official quote on screen):** "All residents should evacuate from dangerous areas." — Japan Meteorological Agency, "Emergency Warning System," Alert Level 4 guidance. Glasscard under the quote. Ladder MG, level 4 highlighted: "4 · EVACUATION INSTRUCTION." Timeline chip: "US HURRICANE WARNING: 36H BEFORE TS-FORCE WINDS · EVACUATION ORDER: SEPARATE, LOCAL DECISION."

## B6 — LEVEL FIVE: WHEN LEAVING MAY NO LONGER BE SAFE (5:12–6:20)

### B6-S1 — narration

> Level five is called Emergency Safety Measures, and it means evacuation itself may no longer be safe. Japan's own Cabinet Office admits this level is rarely issued, because municipal officials often cannot confirm a disaster's exact severity in time, right when it matters most. Residents are told to leave before level five ever arrives, never to wait for it. America's closest match is not a hurricane watch or a hurricane warning at all. It is the National Weather Service's extreme wind warning, issued only once winds of a hundred fifteen miles per hour or higher are expected to begin within the hour. That warning tells people to shelter inside a sturdy building immediately, not to get in a car. Both countries land on the same conclusion from opposite directions. Once conditions turn this severe, moving becomes more dangerous than staying exactly where you are. [j1, n1]

Visual: ladder MG, level 5 highlighted, black/red treatment: "5 · EMERGENCY SAFETY MEASURES." Popfig: "RARELY ISSUED." US-side chip: "EXTREME WIND WARNING · 115 MPH · 185 KM/H · WITHIN THE HOUR · SHELTER, DON'T DRIVE."

## B7 — THE BIGGER DIFFERENCE: ONE LADDER VS. SEVERAL SYSTEMS (6:20–7:35)

### B7-S1 — narration

> Step back, and the largest difference is not any single level. It is how many separate systems America runs side by side to do the same job. A hurricane watch goes out forty eight hours before tropical-storm-force winds are expected. A hurricane warning follows at thirty six hours. Neither one carries an evacuation order by itself. A county or a state issues that order on its own schedule, sometimes before the warning, sometimes well after it. Japan built one number that carries both pieces at once. The weather trigger and the government order arrive under the same alert level, on the same day, from agencies required by policy to coordinate. An American reading a Japanese news alert that says level four should understand two things happening together: a warning tied to specific rainfall and wind thresholds, and an order to leave right now, issued as one package. No single American watch or warning does both jobs at once. [j1, j2, n1]

Visual: full five-level ladder MG, complete, alongside a parallel US-side stack: "HURRICANE WATCH (48H)" / "HURRICANE WARNING (36H)" / "LOCAL EVACUATION ORDER (SEPARATE TIMELINE)," connecting lines drawn showing the US stack as three uncoordinated pieces against Japan's single coordinated ladder.

## B8 — WHERE THIS STORM SITS ON THAT LADDER TONIGHT (7:35–8:35)

### B8-S1 — narration

> Right now, no Japanese municipality has issued any alert level for this storm, because it has not yet crossed the tropical storm threshold that starts the ladder moving at all. Japan's longest published forecast, five days out, places the storm east of the country's main islands, with sustained winds near sixty seven miles per hour and gusts to eighty nine. That position sits offshore, past any coastline, and it falls one full grade below the point where Japan even calls a system a typhoon. If the track holds exactly where that forecast shows it tonight, coastal Japan may never reach level three during this storm at all. If the track shifts west toward Kanto instead, that math changes inside a single advisory cycle. Nothing about which one happens is decided yet. [f1]

Visual: ladder MG with a marker pinned below level 1, labeled "TONIGHT: BELOW THE LADDER (STILL A TD)." Track map, JMA's +117h forecast point held: "975 hPa · 67 MPH · 108 KM/H · GUST 89 MPH · 144 KM/H" at map label "EAST OF JAPAN." Return to the live Himawari loop.

## B9 — WHAT'S STILL OPEN TONIGHT (8:35–9:25)

### B9-S1 — narration

> Two questions about this storm still have no answer tonight. The track could still bend toward Kanto, or keep sliding past it offshore, exactly as it has forecast for days now. The storm's own strength could still climb faster, or slower, than any current model shows. Millions of travelers are moving through Japan this week for one of its biggest holidays in more than a decade, checking a forecast that updates by the hour. Whichever alert level this storm eventually triggers, or never triggers at all, that number will tell them more than any single wind speed reading ever could. Japan's weather agency issues its next advisory within hours. [f1, f3]

Visual: tracking card MG, two rows: "TRACK — STILL OPEN" / "STRENGTH — STILL OPEN." Small travel chip, on screen only: "MILLIONS TRAVELING THIS WEEK." Return to the live Himawari loop from B1.

## B10 — CLOSE (9:25–9:42)

### B10-S1 — narration

> Tell me in the comments whether your own country uses anything like Japan's five levels, or nothing close to it at all. Subscribe, and the next update lands the moment this storm earns its name.

Visual: close card ("Five levels. One ladder. Explained." / soft line / brand), Paul circle hidden.
