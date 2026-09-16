# edit_script.md — ms-dujuan-jma-vs-nhc · "JMA vs. NHC: How Japan and America Rank the Same Storm" (mini-storms, evergreen, v1 16 Sep 26)

> Evergreen explainer for The Warning Hour's Dujuan series (idea #9, ideas-r3.md). Doubles as a 16 Sep update: every
> number is anchored to today's live JMA advisory for the still-unnamed tropical depression near the Mariana Islands.
> Reusable for any future Japan storm. Director's note: the storm has **not** been assigned the name "Dujuan" in JMA's
> own feed as of this advisory (facts-16sep.md §6), and per the hard-foreign-names rule below, it is never named in
> voice or on screen anyway — narration refers to it as "this storm" / "the storm" throughout. Numbers spelled out for
> TTS; `[fN]` per sentence group; sentences under 24 words; humanise-rules.md pass applied (no banned openers, no
> metaphors, no rhetorical questions, no em dashes). Target ≥1,350 words. Paul's CTA after B3 (~34% in, story break
> between "how Japan measures" and "how America measures").

## Spec
- Slug `ms-dujuan-jma-vs-nhc`. Voice: pocket-TTS Pharaoh → atempo 1.10–1.15 → transcribe the sped wav → cues from that
  words.json.
- **Hard foreign names OUT of voice and on screen (owner brief):** no storm name (JMA has not assigned one — see
  facts-16sep.md §6), no Japanese-script text, no untransliterated Japanese place names. Kept: Japan, Tokyo, Pacific,
  Mariana Islands, Gulf, Atlantic — common English geographic terms a 40+ American already knows.
- Numbers: spelled out in the voice; numerals on screen (popfigs/chips/cards). Wind: **mph in the voice**; m/s and
  km/h added on screen only.
- Pool: `library/mini-storms/dujuan-2026/` (reused across the Dujuan series). MG for this video: side-by-side scale
  ladder (JMA vs. Saffir-Simpson, built once in B4, referenced again in B6), JMA quote card (B3), JMA-vs-JTWC split
  forecast card (B6), Hagibis benchmark popfig (B8), tracking card (B9).
- Close: B9 ends on the tracking line (storm's next advisory); B10 is the single soft comment + subscribe line.

## Sources
- f1 — facts-16sep.md §4, JMA intensity scale (Strong/Very Strong/Violent Typhoon thresholds, Severe Tropical Storm,
  Tropical Storm), compiled via Wikipedia "Tropical cyclone scales" §Western Pacific citing RSMC Tokyo's own scale;
  JMA's own English classification page returned 404s this session, so the on-screen quote is corroborated via the
  Wikipedia-compiled RSMC Tokyo table, not fetched directly from jma.go.jp. `en.wikipedia.org/wiki/Tropical_cyclone_scales`
- f2 — facts-16sep.md §6, live JMA advisory fetched 16 Sep 2026: `targetTc.json` / `TC2630/specifications.json`
  (`jma.go.jp/bosai/typhoon/data/...`). Current analysis (18:00 JST): 15.9°N 149.1°E, 998 hPa, 15 m/s (30 kt)
  sustained, gust 23 m/s (45 kt). Longest forecast (+117h, 21 Sep 15:00 JST): Severe Tropical Storm, 30 m/s (55 kt)
  sustained, gust 40 m/s (80 kt), 975 hPa, "East of Japan." Storm not yet named.
- f3 — facts-16sep.md §5, Typhoon Hagibis (2019): 139 dead, 3 missing, US$17.3 billion damage, costliest typhoon on
  record in Japanese history, via Wikipedia "Typhoon Hagibis."
- f4 — ops/wave3/dujuan/PLAN.md storm-state summary: JTWC warning 04, peak forecast 65 kt (75 mph), 19–21 Sep, near
  35.7°N 142.7°E. Internal ops tracking note, itself sourced from JTWC's own bulletin text; no independent URL
  re-fetched this session.
- nhc — National Hurricane Center's published Saffir-Simpson Hurricane Wind Scale (Category 1: 74–95 mph / 64–82 kt;
  Category 2: 96–110 mph / 83–95 kt; Category 3: 111–129 mph / 96–112 kt; Category 4: 130–156 mph / 113–136 kt;
  Category 5: 157 mph+ / 137 kt+). Standard published NHC scale, not independently re-fetched this session — supplied
  directly in the team lead's content brief.

## B1 — COLD OPEN (0:00–0:35)

### B1-S1 — narration
> Right now, forecasters in Tokyo and Miami are tracking the same tropical system, and they do not agree on its strength. Today, September sixteenth, a tropical depression is spinning near the Mariana Islands in the open Pacific. Central pressure sits at nine hundred ninety eight hectopascals. Sustained winds run thirty three miles per hour, with gusts to fifty two. Japan's weather agency has not named this storm yet. It is still logged as a tropical depression on their own books. Their forecast already shows the storm strengthening steadily over the next five days, moving north toward Japan. Two countries are about to read that same strengthening wind field and publish two different numbers for it. Neither agency will be wrong. The gap between those numbers comes down to how each one measures wind, and it changes what a headline actually means. [f2]

Visual: open on Himawari satellite loop of the depression near the Marianas; glassmorphic stat cards land on cue:
"998 hPa" · "33 MPH · GUSTS 52" · "NOT YET NAMED"; news bug "STORM WATCH · WESTERN PACIFIC."

## B2 — TWO AGENCIES, THREE RULEBOOKS (0:35–1:25)

### B2-S1 — narration
> Japan's weather agency is called the Japan Meteorological Agency. Inside Japan, everyone just says JMA. The United States tracks Pacific storms through two separate offices, and that split confuses even frequent travelers. Its National Hurricane Center issues the public warnings Americans see on the nightly news and the hurricane tracking apps. A second office, the Joint Typhoon Warning Center, is run by the U.S. Navy. It issues a separate set of numbers built for military ships and aircraft crossing the Pacific. All three agencies, Japanese and American, can watch the identical storm and publish three different wind speeds on the same day. None of them made an error. You may have read a Japanese news story about a typhoon. The number probably looked smaller than the American hurricane you remember. This is why. Each agency uses a different clock to measure the wind, and that clock changes the final number before anyone talks about damage. [f1, f2, nhc]

Visual: three-way label card: "JAPAN METEOROLOGICAL AGENCY" · "NATIONAL HURRICANE CENTER" · "JOINT TYPHOON WARNING CENTER (U.S. NAVY)"; Himawari loop continues under the cards.

## B3 — HOW JAPAN MEASURES (1:25–2:20)

### B3-S1 — narration
> Japan's agency measures wind as a ten minute average. Forecasters clock the wind speed continuously for ten full minutes and report that average, not the strongest gust inside the window. On that scale, a tropical storm runs thirty eight to fifty five miles per hour. A severe tropical storm runs fifty five to seventy three. Once the ten minute average passes seventy three miles per hour, Japan calls the storm a typhoon. Above that line, Japan adds three more grades, each one a full step up in violence. A strong typhoon runs seventy four to ninety six miles per hour. A very strong typhoon runs ninety eight to one hundred nineteen. A violent typhoon starts at one hundred twenty one miles per hour, with no upper limit written into the scale. Those exact bands come from the agency's own published wind classification, the same table Japanese broadcasters read from every typhoon season. [f1]

Visual: **quote card (the one named official quote on screen):** "Strong Typhoon: 33–<44 m/s (64–84 kt) · Very Strong
Typhoon: 44–<54 m/s (85–104 kt) · Violent Typhoon: ≥54 m/s (≥105 kt)" — attributed "Japan Meteorological Agency,
tropical cyclone intensity scale." Chip below: "10-MINUTE SUSTAINED WIND." Glasscard under the quote.

*(Paul's ebook CTA mounted here: 0.5 s dip in, 0.5 s out, film layer off. ~34% in, the story break between "how Japan
measures" and "how America measures.")*

## B4 — HOW AMERICA MEASURES (2:20–3:10)

### B4-S1 — narration
> America's National Hurricane Center uses a shorter clock. It measures the strongest one minute average inside the storm, not ten minutes. That single change in the clock moves every number that follows. On the Saffir Simpson scale, a category one hurricane starts at seventy four miles per hour and tops out at ninety five. Category two runs ninety six to one hundred ten. Category three runs one hundred eleven to one hundred twenty nine. Category four runs one hundred thirty to one hundred fifty six. Category five starts at one hundred fifty seven miles per hour with no ceiling above it. Category one begins at seventy four miles per hour, almost exactly where Japan's own typhoon line begins too. The starting point is close. The measuring stick behind it is not. [nhc]

Visual: **side-by-side scale graphic (built here, referenced again in B6):** left ladder = JMA grades (Tropical
Storm → Severe Tropical Storm → Typhoon → Strong → Very Strong → Violent), right ladder = Saffir-Simpson categories
one through five, both in mph, a connecting line drawn at the seventy-four-mph mark where the two ladders nearly
align; chip "1-MINUTE SUSTAINED WIND."

## B5 — WHY A THIRD SCALE EXISTS (3:10–4:05)

### B5-S1 — narration
> A third agency adds a third number to the same storm. The Joint Typhoon Warning Center is a U.S. Navy and Air Force command based in Hawaii. It exists because American ships, submarines, and aircraft operate across the entire Pacific, far outside the National Hurricane Center's own basin. The Joint Typhoon Warning Center tracks every typhoon near Japan. It uses the same one minute wind standard the National Hurricane Center uses for Atlantic hurricanes. That choice matters for this storm specifically. Japan's own agency publishes its wind speed on the ten minute scale you just heard. The U.S. Navy publishes its own independent number for the identical storm on the one minute scale. That number is built for a different purpose, keeping ships and aircrews away from danger rather than warning coastal residents. Two American numbers can exist for the same Pacific storm. One comes from the National Hurricane Center's public warnings, the other from the Navy's operational forecast. Japan adds a third. None of the three is copying the others. [f4, nhc]

Visual: map graphic, Joint Typhoon Warning Center's Hawaii base marked, dotted coverage arc across the whole Pacific;
chip "U.S. NAVY / AIR FORCE · HONOLULU, HAWAII."

## B6 — THE MATH BEHIND THE GAP, IN TODAY'S NUMBERS (4:05–5:15)

### B6-S1 — narration
> A one minute average almost always reads higher than a ten minute average of the same wind field. A short window catches gusty peaks that a longer window smooths out over time. The general rule of thumb runs close to twelve percent higher for the one minute number. Today's forecast for this storm shows that gap in real figures. Japan's longest range forecast has the storm peaking at a sustained sixty seven miles per hour. That is one step below typhoon, a grade Japan calls severe tropical storm. The U.S. Navy's Joint Typhoon Warning Center uses the one minute clock. It forecasts the same storm, at the same point in time, near seventy five miles per hour. Seventy five miles per hour crosses the Saffir Simpson line into category one hurricane strength. Same storm, same day, two different grades from two allied countries. The twelve percent conversion is a statistical rule of thumb, not an exact formula. Forecasters use it as an estimate, never as a fact. [f2, f4]

Visual: **glassmorphic stat cards, split screen:** left card "JMA FORECAST · 67 MPH (30 M/S · 108 KM/H) · SEVERE
TROPICAL STORM"; right card "JTWC FORECAST · 75 MPH (65 KT) · CATEGORY 1 RANGE"; popfig "12% HIGHER" between the two
cards; the side-by-side scale ladder from B4 reappears behind the cards with both forecast points marked on it.

## B7 — SAME ANIMAL, DIFFERENT NAME (5:15–6:20)

### B7-S1 — narration
> A typhoon and a hurricane are the same weather phenomenon. Meteorologists call it a tropical cyclone everywhere on Earth. The name changes only by ocean. In the western Pacific, including the waters near Japan, it is called a typhoon. In the Atlantic and the eastern Pacific, it is called a hurricane. In the Indian Ocean, it is called a cyclone. Same spinning storm, same physics, three regional names. So when a headline out of Japan says strong typhoon, an American reader can translate it directly. Strong typhoon means sustained winds of at least seventy four miles per hour on Japan's own ten minute scale. That is the same starting line as an American hurricane. Very strong typhoon means winds close to or above the top of category two on the American scale. Violent typhoon, Japan's highest grade, means winds well into category three territory and climbing. The word typhoon alone tells an American reader almost nothing about size. The grade attached to it does. Neither word, typhoon or hurricane, is a measurement on its own. [f1, nhc]

Visual: three-basin world-map chip: "PACIFIC: TYPHOON · ATLANTIC: HURRICANE · INDIAN OCEAN: CYCLONE"; translation
table card mapping JMA grade to US read (Strong→Cat 1 start, Very Strong→near Cat 2 top, Violent→into Cat 3).

## B8 — WHY IT MATTERS: THE BENCHMARK (6:20–7:15)

### B8-S1 — narration
> The stakes behind this classification gap are not abstract. Typhoon Hagibis struck Japan in October of twenty nineteen. Japan's agency reported one hundred thirty nine dead and three missing. The storm caused seventeen point three billion dollars in damage, the costliest typhoon on record in Japanese history. Hagibis stayed in living memory across Japan for exactly this reason. A storm graded severe tropical storm on Japan's own scale can still shut down trains and flood coastlines. It can force evacuations even below the typhoon threshold. A storm graded category one on the American scale is officially a hurricane. That is the same legal and safety threshold used for evacuation orders across the Gulf and Atlantic coasts. Neither number alone predicts the damage. Central pressure, forecast track, and rainfall totals matter as much as the category label attached to a storm. An American traveling in Japan this week should watch the grade, not the word typhoon by itself. [f3]

Visual: Hagibis archival popfig "139 DEAD · $17.3B" with source label "JMA, 2019"; two-line safety chip: "JP SEVERE
TROPICAL STORM: BELOW TYPHOON, STILL DISRUPTIVE" / "US CATEGORY 1: OFFICIALLY A HURRICANE."

## B9 — WHAT'S STILL OPEN TONIGHT (7:15–7:45)

### B9-S1 — narration
> This particular storm remains a tropical depression tonight. Japan's own agency has not yet assigned it a name. Its next scheduled advisory will say whether it strengthens on pace, slows down, or curves away from Japan entirely. That next advisory decides what happens, not tonight's forecast numbers. For anyone with travel plans in Japan this month, that next advisory is the number worth checking. [f2]

Visual: tracking card MG, single row highlighted: "NEXT: JMA'S NEXT ADVISORY"; return to the Himawari loop from B1.

## B10 — CLOSE (7:45–8:05)

### B10-S1 — narration
> Tell me in the comments which scale you trust more, the ten minute average or the one minute peak. Subscribe, and the next update reaches you the moment Japan's agency gives this storm its name.

Visual: close card ("Two scales. One storm." / soft line / brand), Paul circle hidden.
