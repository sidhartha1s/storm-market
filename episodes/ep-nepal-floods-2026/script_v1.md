# ep-nepal-floods-2026 · script v1 (29 Sep 26)

**Episode.** The late-September 2026 Nepal disaster (27 Sep Kali Gandaki collapse + Himlung Himal base camp
avalanche), told against August's Langtang collapse. Target 13 to 14 min. Enderlin format. First draft; nothing locked.

**Working titles** (all ≤ 52 chars, "Nepal" + "2026" in the first 10 chars; lengths by python)
1. Nepal 2026: The Mountain That Fell in 3 Seconds (47)
2. Nepal 2026: One Month Later, It Fell Again (42)
3. Nepal 2026: The Rain That Came Back After Langtang (50)

**Thumbnail concept.** One frame from `wion-mountain-crashes-kaligandaki.mp4` at the moment the green slope breaks
into brown dust over the river (graded, credited), cropped tight on the falling face. Big white "3 SECONDS" top-left,
a red timer ring "0:03" beside it, small "NEPAL 2026" under it. Bottom-right, a small inset of a snowy peak with one
yellow tent, the base camp thread. No faces, no toll number (the hook pays the "3 seconds" in its first sentence).

**Word count.** 2,289 narration words (python, `[verify]`/loop/tag markers and Picture lines stripped). Per section:
H 19 · HT 34 · I 294 · A1 332 · A2 444 · A3 383 · A4 384 · A5 153 · CTA 0 · A6 168 · Z 78.
**Estimated runtime.** 13:23 at the owner's measured 171 narration words per runtime minute (Enderlin). Not yet
checked by `word_budget.py` (needs probe wavs). Every `[verify]` line the fact desk cuts pulls it under; the two
`{NAME}` lines add about 20 words if a name is published.

**CTA hinge.** A5 "Thirty two days" ends on the tease (21 words): "Across both months, Nepal's warning system measured
one thing well, and it was the thing that moved last." → CTA (15.1 s file + two 1.0 s dips) → A6 "After the rain"
opens with the payoff: "It measured rivers." CTA start estimated 11:57, 89.3 % of runtime (python, words before CTA
2,043 / 2,289).

**Open for the orchestrator / owner**
- Named human thread: no verifiable name exists in my inputs (`notes.md` was not on disk). The A3 and Z name lines are
  `{NAME}` slots with a CUT instruction if the fact desk finds no published name.
- A1's frame-by-frame beats are written blind; frame-check the clip and rewrite them to what it shows.
- `wion-hillside-collapse-mustang.mp4` is still a `.part` download; no `provenance.csv` exists yet for any clip.
- Close rule conflict: `script-quickref.md` says "no sign-off line"; the brief asked for the Enderlin signature
  "This was The Warning Hour." The brief won; flag for the owner.
- Clip filenames `lallantop-...-24-dead` and `republicworld-5-horrifying-visuals` contain flag words; they are internal
  file names only and must never appear as on-screen text or credits (credit "The Lallantop", "Republic World").
- Gates: my regex scan of narration found 0 flag-word hits, 0 em dashes, 0 question marks, 0 banned words. The repo's
  `flag_words.py` / `homograph_scan.py` read `edit_script.md`, which does not exist yet, so their PASS is vacuous.
- Homographs used (scan list): "lives" ×6 (noun), "close" ×3 (check sense: "close to" = /kloʊs/), "winds" ×1 (noun),
  "read" ×1 ("nothing to read", present). Probe before any respelling.
- Facts competitors lack: Kali Gandaki gorge vs Grand Canyon; Oso, Washington 2014 as the same glacial-sediment
  mechanism; the 27 to 28 Sep 2024 Kathmandu floods on the same dates; the displaced-per-family arithmetic that
  exposes mismatched counts; the gauge-vs-slope warning gap as the hinge.

**Motion graphics wanted (18)**
g-collapse-3s (3-second frame breakdown) · g-map-kali-gandaki (valley + five districts, master map) ·
g-gorge-vs-grand-canyon · g-hydro-card (Kali Gandaki A, 144 MW, US homes) · g-himlung-height (vs Denali) ·
g-toll-counter (three outlets side by side) · g-aug-vs-sep (map, distances in miles) · g-insar-creep (Langtang 30 cm
radar creep) · g-pore-pressure (slope saturation) · g-monsoon-calendar · g-bay-of-bengal-track · g-rain-bars ·
g-sep-2024 (precedent card) · g-basecamp-diagram · g-rock-ice-mechanism · g-ledger (Established / Disputed / Unknown
board) · g-sensor-gap (river gauge vs slope) · g-outro. Plus non-MG cards: Oso map + USGS PD photo, glacial-debris
valley cutaway, social-post mock, text-only name card, USGS / ICIMOD source cards.

**Clips.** 9 files, 18 placements (about one every 45 s); re-used files use different segments, one exact re-use
(the viral shot in A1) carries `data-callback`.

**Verify tags (67).** Resolved by the fact desk, never by the writer; "(sentence before)" = the claim in that sentence.
H: 27 Sep date; "3 seconds" per LatestLY / Asianet · HT: CNN 27 Sep, UAE expedition due 1 Oct ·
I: gorge depth 5,571 m vs Grand Canyon 6,000 ft · NewsBytes 24/14 and scope · 1,500 / 747 / 143 source and scope ·
bridges, plant offline · 144 MW ≈ 108,000 to 115,200 US homes · Himlung 7,126 m vs Denali · CNN at least 4 ·
1,451 / 5,745 as of 21 Sep, official source ·
A1: frame-check viral clip, vantage · USGS landslide basics · landslide-dam mechanism · any blockage / lake report ·
plant at Mirmi, Syangja · commissioned 2002, largest until 2021 · shutdown reason (NEA) · Jomsom / Muktinath road
(sentence before) · trekking season dates ·
A2: DHM monsoon onset / withdrawal · Al Jazeera "Bay of Bengal depression" · name "Arnab" vs IMD; Yahoo · storm lost
its winds (sentence before) · 66.5 vs 7.6 mm, station, day · pore pressure (USGS) · valley glacial-debris geology ·
Oso: 43 lives, glacial sediment, rain · Oso comparison holds · Sep 2024 floods dates, about 244 ·
A3: Himlung location / border distance · "first big peak" (sentence before) · crews arrive early · CNN 27 Sep ·
named worker or CUT · rock-ice mechanism (ICIMOD / AGU) · 600 m / 1,200 m · Himlung ice / runout unpublished
(sentence before) · ICIMOD 30 cm in 3 to 4 weeks · sensors built for river floods · no pre-event radar published ·
A4: collapse after rain (sentence before) · viral clip provenance · Himlung established (sentence before) ·
Al Jazeera 12 / 56 · SANA 21 / 5 / 5 · NewsBytes + CNBC TV18 about 70 · census household 4.37 · collapse location,
WION "Mustang" · no glacier on failed slope · Langtang about 5,600 m · "rain landslide" type (sentence before) ·
Himlung closer to Langtang's type (sentence before) · lake / blockage unknown (sentence before) · 7NEWS Australians ·
A5: about 120 mi Langtang to Kali Gandaki (190 km, approximate coordinates) · about 75 mi to Himlung (124 km) ·
seasonal thaw · "wrong kind of disaster" framing ·
A6: DHM warning network · Langtang gauges swept away · InSAR precision · monsoon withdrawal, soil drying ·
trekking season now (sentence before) · climbing season, crews on peaks (sentence before) ·
Z: arrival date / cancellation · count and roles · name or CUT · DHM forecast.

**Reading notes.** `[loop …]`, `[verify …]` and `[RS] [VE] [Q] [PAY] [HOOK] [HUMAN]` are margin marks, stripped from
the TTS copy. Numbers, dates and years are spelled out in narration; Picture lines keep digits.

**Loop chain** in full after Z.

---

## H · Hook (0:00)
**Picture:** `wion-mountain-crashes-kaligandaki.mp4` from frame one, mid-slide (the viral shot), narrator from 0:00, clip
audio off · popfig "Sept 27, 2026 · Kali Gandaki, Nepal" inside the first second · g-collapse-3s runs as a thin
timer over the clip, "0.0 s" to "3.0 s", landing on "three seconds". [VE] [HOOK]

One month after the Langtang flood, a Nepal mountainside fell into the Kali Gandaki River in about three seconds.
`[verify: 27 Sep 2026; "vanishing in 3 seconds" per LatestLY / Asianet]` `[loop L0 open]`

## HT · Hook tail (0:06)
**Picture:** g-map-kali-gandaki flash: the river drawn north to the Tibet border, a pin lands on "Himlung Himal" ·
cut on "base camp" to `wion-climbers-guides-missing-avalanche.mp4` (tents / high camp shot, muted).

The same storm was dropping snow on Himlung Himal, a peak near the Tibet border. A crew of Sherpas and cooks was
up there, building a base camp for climbers due on October first. `[verify: CNN 27 Sep, UAE expedition due 1 Oct]`
`[loop L1 open]`

*(no void, no title card: straight into I, same valley on screen)*

## I · What fell (0:18)
**Picture:** g-map-kali-gandaki full: the river runs south out of the Himalaya, five district labels land on the
voice (Manang, Myagdi, Baglung, Parbat, Palpa) · inset g-gorge-vs-grand-canyon: a gorge profile beside a Grand
Canyon profile at the same scale, "about 18,000 ft" against "about 6,000 ft". [RS]

The Kali Gandaki runs south out of the high Himalaya through one of the deepest gorges on Earth. From the river up to
the summit of Dhaulagiri beside it, the drop is about eighteen thousand feet, roughly three times the depth of the
Grand Canyon in Arizona. `[verify: gorge depth 5,571 m river to Dhaulagiri summit; Grand Canyon about 6,000 ft]`
After days of heavy rain, a huge section of one of those valley walls gave way on Sunday, September twenty seventh.

**Picture:** `lallantop-flood-landslide-24-dead.mp4` (river and rescue b-roll, muted, graded) · g-toll-counter,
state one: "24 lives lost · 14 missing · NewsBytes, Sept 28". [VE]

By the next day, the outlet NewsBytes counted twenty four people who did not survive the storm, with fourteen more
missing. `[verify: NewsBytes 24 / 14; scope: Kali Gandaki districts or all Nepal]` About one thousand five hundred
people had to leave their homes, and one hundred and forty three houses were gone.
`[verify: 1,500 displaced, 747 families, 143 houses; outlet and scope]` `[loop L5 open]`

**Picture:** g-hydro-card: the Kali Gandaki A plant as a glass card, "144 MW", a power meter falling to zero, then
a US house icon grid filling to "about 100,000 homes" · `khojsamachar-manang-parbat-nationwide.mp4` (a broken
bridge shot if the clip has one, muted).

Bridges went down along the valley, and the Kali Gandaki A hydropower plant stopped generating.
`[verify: bridges, count if published; plant offline]` It produces one hundred and forty four megawatts, enough in
American terms for roughly a hundred thousand homes. `[verify: 144 MW; 750 to 800 US homes per MW gives 108,000 to 115,200]`

**Picture:** `wion-climbers-guides-missing-avalanche.mp4` (a second cut, the peak) · g-himlung-height: two bars,
"Himlung Himal · 23,379 ft" and "Denali · 20,310 ft", the gap labelled "about 3,000 ft". [VE]

Up north, the same weather brought an avalanche of snow and rock down onto that camp on Himlung Himal. The peak
rises about twenty three thousand four hundred feet, roughly three thousand feet higher than Denali, the tallest
mountain in North America. `[verify: Himlung 7,126 m = 23,379 ft; Denali 20,310 ft]` CNN reported at least four
people lost their lives there, and others were still missing. `[verify: CNN 27 Sep, at least 4]`

**Picture:** g-aug-vs-sep teaser: a pin at Langtang Lirung, "Aug 26", counters "1,451 lives lost · 5,745 missing ·
as of Sept 21"; a second pin drops on the Kali Gandaki, "Sept 27". [RS]

Nepal had not finished counting its August disaster when this began. On August twenty sixth, a rock and ice
collapse on Langtang Lirung sent a debris flood down the Trishuli River. By September twenty first, Nepal counted one
thousand four hundred and fifty one lives lost and five thousand seven hundred and forty five people still missing.
`[verify: 1,451 / 5,745 as of 21 Sep; official source behind the Wikipedia figure]`

**Picture:** g-insar-creep teaser: a radar strip over Langtang Lirung, a displacement counter starting to climb,
freezing before it finishes.

Scientists had watched the Langtang slope moving on satellite radar in the weeks before it failed. That is why the
September collapse raises a harder question, about what anyone could see on the Kali Gandaki before it moved.
`[loop L4 open]`

## A1 · Three seconds (2:02)
**Picture:** g-collapse-3s full: four stills pulled from the viral clip at 0.0, 1.0, 2.0 and 3.0 s, each stamped on
the voice, then `wion-mountain-crashes-kaligandaki.mp4` replays once at full speed (reuse,
`data-callback="frame-by-frame payoff"`). [RS] [VE]

The video that spread on September twenty seventh was filmed from the far side of the river. In the first second, a
strip of green hillside above the water starts to slide as one piece. By the second, the face beneath it breaks
into brown dust and rock. By the third, the whole section is in the river, and muddy water surges across the channel.
`[verify: frame-check the clip and rewrite these three beats to what it shows; vantage point]`

**Picture:** g-pore-pressure teaser: a slope cross-section, a thin blue line creeping upward inside it, a USGS
text card "U.S. Geological Survey · Landslide Hazards Program".

Landslides like this build for days and finish in seconds. The U.S. Geological Survey describes the pattern the
same way in every mountain range. Rain soaks in slowly, the pressure inside the slope climbs, and the last of the
friction holding it gives way all at once. `[verify: USGS landslide basics page]` The three seconds on camera were the
end of a failure that had been building since the rain began.

**Picture:** g-map-kali-gandaki zoom: the gorge narrows, an arrow shows debris entering the channel, then two
arrows, one upstream labelled "dam?" and one downstream labelled "surge". [Q]

A gorge this narrow turns one slope failure into a problem for the whole river. Debris that lands in the channel
can pile up into a natural dam and hold back a lake behind it. When that dam gives way, the stored water runs
downstream as a surge of mud. `[verify: landslide dam mechanism; ICIMOD or USGS]` Whether the September debris
blocked the Kali Gandaki, even for a few hours, had not been reported by the twenty ninth.
`[verify: any report of blockage or a temporary lake]`

**Picture:** `republicworld-5-horrifying-visuals.mp4` (a flooded-road or debris shot, muted, graded; the clip title
never appears on screen, credit line reads "Republic World") · g-hydro-card returns small: a dam pin downstream on
the map, "Mirmi, Syangja".

Downstream, the river feeds the Kali Gandaki A dam and power plant near Mirmi, in Syangja district.
`[verify: location Mirmi, Syangja]` When it opened in two thousand two, it was the largest hydropower plant in
Nepal. `[verify: commissioned 2002; largest until Upper Tamakoshi 2021]` A river carrying a mountainside of mud is
water a turbine cannot use, because the silt grinds down the blades. `[verify: stated reason for the shutdown; Nepal Electricity Authority]`

**Picture:** a route line on g-map-kali-gandaki runs north to "Jomsom" and "Muktinath"; a small trekker icon on
the Annapurna trail · `khojsamachar-manang-parbat-nationwide.mp4` (a road cut shot, second segment). [VE]

The same valley carries the main road north to Jomsom and Mustang, and to the temple at Muktinath, where Hindu and
Buddhist pilgrims both travel. `[verify]` Late September is also the start of the autumn trekking season on the
Annapurna trails above it, when visitors from America and Europe start to arrive. `[verify: season dates, Nepal Tourism Board]`
A collapse this size here cuts off more than a village. The rain that set it off arrived when Nepal's rainy season
is supposed to be ending. `[loop L2 open]`

*(chapter blackout)*

## A2 · The wrong end of the season (3:58)
**Picture:** g-monsoon-calendar: a June to October bar, "onset" mark in mid June, "normal withdrawal" mark in early
October, a red pin landing on "Sept 27" near the end. [VE]

Nepal gets most of its rain from the summer monsoon, which usually arrives in June and starts leaving in early
October. `[verify: Nepal DHM normal onset about 13 Jun, normal withdrawal date]` By late September, the hillsides
have been soaking for close to four months. They go into the last storms of the year holding more water than at any
other point in the year.

**Picture:** g-bay-of-bengal-track: a low pressure symbol forms over the Bay of Bengal, tracks north over India,
a rain shield spreads across the Nepal border · `news18bihar-cyclone-arnab-bagmati.mp4` (river in spate, muted).

This storm began as a low pressure system over the Bay of Bengal, south of India, and moved north.
`[verify: Al Jazeera 27 Sep "Bay of Bengal depression"]` Indian channels named it Cyclone Arnab, and a Yahoo report
described the rain in Nepal as a cyclone's aftermath. `[verify: the name Arnab against India Meteorological Department records; Yahoo piece]`
By the time it reached the mountains it had lost its winds, and it still carried the moisture of the ocean it came from.
`[verify]`

**Picture:** g-rain-bars: two bars rising, "normal · 0.3 in" and "Sept 27 · 2.6 in", a multiplier tag "×8.75"
landing on "nine times". [RS]

Al Jazeera reported sixty six and a half millimeters of rain at one station, against a normal of about seven and a
half. That is about two and a half inches of rain where a third of an inch is normal, close to nine times as much.
`[verify: 66.5 mm vs 7.6 mm; which station, which day, one day or the event total]`

**Picture:** g-pore-pressure full: slope cross-section, soil grains as circles, blue water filling the gaps, small
arrows pushing grains apart, a "friction" bar dropping under a "weight" bar until the slope slips.

A slope stays up because of friction between the grains of soil and rock inside it. Rain fills the tiny gaps
between those grains, and the water pushes them apart from the inside. Geologists call that pore pressure, the push
of water trapped inside the ground. When pore pressure climbs high enough, the friction holding the slope drops below
the weight pulling it down. `[verify: USGS]` A soaked slope can fail without the biggest storm of the year. It needs
one heavy day on top of four wet months, and late September supplies that day. `[loop L2 closes]`

**Picture:** a cutaway of the Kali Gandaki valley wall: bedrock in grey, a loose tan layer of old glacial gravel
draped over it, labelled "glacial debris" · `lallantop-flood-landslide-24-dead.mp4` (second segment, a slope or
debris shot).

The Kali Gandaki adds two things to that math. Its walls are among the steepest in the Himalaya, and much of what
covers them is old glacial debris, the rock and gravel that ice dragged downhill and left behind when it melted.
`[verify: valley geology, a named source]` That material was never cemented into solid rock. Water moves through it
fast, and it gives way fast.

**Picture:** a Washington state map, a pin at Oso · popfig "March 22, 2014" · a USGS PD photo of the Oso slide
scar (credit checked) · text on the voice: "43 lives lost". [RS] [VE]

We have watched the same kind of ground fail at home. In March twenty fourteen, near Oso, Washington, a hillside of
old glacial sediment collapsed after weeks of heavy rain and took forty three lives.
`[verify: USGS Oso report; 43 lives; glacial sediment; rain in the weeks before]` The Oso hillside and the Kali
Gandaki wall were both loose glacial material on a steep slope, full of water. `[verify: comparison holds]`

**Picture:** g-sep-2024 card: "Sept 27–28, 2024 · Kathmandu Valley" with a count landing "more than 240 lives
lost", then a calendar showing both Septembers with the same dates circled.

Nepal has seen this late September calendar before. Two years earlier, on September twenty seventh and twenty
eighth, twenty twenty four, late season rain flooded the Kathmandu Valley and set off landslides that took more than
two hundred and forty lives. `[verify: 2024 Nepal floods dates and toll, about 244]` Two Septembers apart, on the same
dates. In the high valleys, the same kind of storm falls as snow, and on Himlung Himal that snow sat above a camp
full of people. `[loop L1 continues]`

*(chapter blackout)*

## A3 · Base camp (6:34)
**Picture:** g-basecamp-diagram: Himlung massif side-on, base camp tents at the foot, a fixed-rope line climbing to
"Camp 1", an avalanche path drawn down across the tents · `wion-climbers-guides-missing-avalanche.mp4` (third cut,
rescue or helicopter shot). [VE]

Himlung Himal stands in the far north of Manang district, in the Nar Phu valley, a few miles from Tibet.
`[verify: location; distance to the border]` Expedition companies sell it as a first big Himalayan peak, a training
climb before the eight thousand meter giants. `[verify]`

Every autumn climb starts with the people who arrive before the clients. Sherpa climbers carry up tents, fix ropes
along the route and set the high camps, while kitchen staff build the base camp the team will stay in for weeks.
`[verify: standard practice; source on crews arriving early]` That was the work under way at Himlung in late
September, for an expedition from the United Arab Emirates due on October first. `[verify: CNN 27 Sep]`

**Picture:** text-only name card "{NAME} · {AGE} · {ROLE}, {VILLAGE}" slides in over the base camp shot. [HUMAN]

Then snow and rock came down onto the camp. One of the crew was {NAME}, {AGE}, a {ROLE} from {VILLAGE}.
`[verify: a named worker from CNN, The Himalayan Times, The Kathmandu Post or the operator's statement; if no name is published, CUT this line and the Z name card]`
`[loop L1 closes]` The crew had been there to make the mountain ready for other people, and the storm arrived before
the climbers did.

**Picture:** g-rock-ice-mechanism: a hanging slab of rock and ice on a steep face, a crack line, the slab falls,
ice fragments heat and turn to water, the mass spreads into a fast tongue that runs far past a plain rockfall line.
[RS]

Himlung was struck by an avalanche, and Langtang in August was struck by something heavier. A rock ice avalanche
is rock and glacier ice falling together, fast enough to flow. As it falls, friction melts some of the ice, and the
water turns the mass into a slurry that runs much farther than dry rock would.
`[verify: mechanism; ICIMOD or the AGU Landslide Blog]` Off Langtang Lirung, the slab was about two thousand feet
wide, and it dropped almost four thousand feet, close to three Empire State Buildings stacked on top of each other.
`[verify: 600 m wide, 1,200 m drop; ICIMOD / EOS]`

At Himlung, reports so far describe snow and rock. Whether glacier ice was part of it, and how far it ran below the
camp, had not been published by the twenty ninth. `[verify]` The Kali Gandaki video was already being shared online
as the same kind of event as Langtang. `[loop L3 open]`

**Picture:** g-insar-creep full: a Copernicus Sentinel radar strip over Langtang Lirung, a colour ramp, the
counter finishing its climb to "30 cm · about 12 in" across a "3 to 4 weeks" bracket · text card "ICIMOD ·
Kathmandu". [RS] [VE]

Langtang gave a warning, and someone measured it. ICIMOD, the mountain research center in Kathmandu, said
satellite radar showed the slope had moved as much as twelve inches in the three to four weeks before it failed.
`[verify: ICIMOD, 30 cm, 3 to 4 weeks]` That motion was visible from orbit. The warning sensors in the valley were
built for monsoon river floods, and none of them was pointed at a moving mountainside. `[verify: ICIMOD / CBC]`

**Picture:** `khojsamachar-manang-parbat-nationwide.mp4` (third segment, a hillside shot) · the radar strip
returns empty over a Kali Gandaki outline with a "?" stamp.

For the Kali Gandaki wall and the Himlung face, no agency had published radar from before September twenty seventh
by the twenty ninth. `[verify: search ICIMOD, ESA, NASA as of 29 Sep]` `[loop L4 continues]` The numbers from both
places, meanwhile, were running in different directions, depending on who was counting. `[loop L5 continues]`

*(chapter blackout)*

## A4 · Established, disputed, unknown (8:49)
**Picture:** g-ledger: a board with three columns, "Established", "Disputed", "Unknown"; each claim slides into its
column on the voice and stays for the rest of the act. [VE]

The claims from this week sort into three piles: what is established, what is disputed, and what is still unknown.
Established, a large section of valley wall fell into the Kali Gandaki on September twenty seventh, after days of
rain. `[verify]` Established, the video of it comes from that day. `[verify: provenance of the viral clip; rule out
recycled footage]` Established, an avalanche hit the Himlung base camp while the crew prepared for an October
expedition, and people lost their lives there. `[verify]`

**Picture:** g-toll-counter full: three counters side by side, each with outlet and date: "Al Jazeera · Sept 27 ·
12 Nepal / 56 India", "SANA · Sept 28 · 21 / 5 missing / 5 injured", "NewsBytes · 24 / 14 missing" · cut to
`cnbctv18-70-lives-india-nepal.mp4` (anchor or map shot, muted) on "about seventy". [RS]

Disputed, the toll. On September twenty seventh, Al Jazeera counted twelve lives lost in Nepal and fifty six across
the border in India. `[verify: Al Jazeera 27 Sep]` The next day, the Syrian state agency SANA reported twenty one in
Nepal, with five missing and five injured. `[verify: SANA 28 Sep]` NewsBytes put it at twenty four, with fourteen
missing, and the Indian channel CNBC TV18 added both countries together to reach about seventy.
`[verify: NewsBytes; CNBC TV18 clip, its figure and scope]` The counts cover different places and different hours,
and the missing move into the toll as searches go on. `[loop L5 closes]`

**Picture:** g-ledger, the displacement row: "1,500 people ÷ 747 families = 2.0 per family" beside "Nepal average
household · 4.37 · 2021 census". [RS]

The displacement figures have the same problem. One thousand five hundred people from seven hundred and forty seven
families works out to two people per family, and Nepal's average household has more than four.
`[verify: 2021 census average household size 4.37]` Those two numbers most likely come from different counts.

**Picture:** g-map-kali-gandaki, a disputed pin that hops between "Myagdi" and "Mustang" ·
`wion-hillside-collapse-mustang.mp4` (download is still a .part file, finish before wiring). [VE]

Disputed, exactly where the slope fell. Reports name five districts along the river, Manang, Myagdi, Baglung,
Parbat and Palpa, while the Indian broadcaster WION labeled its footage as Mustang, farther up the same valley.
`[verify: collapse location; WION clip title]`

**Picture:** a phone-frame mock of a social post, text blurred except "glacier collapse", a red "?" stamp · then
the g-rock-ice-mechanism slab beside a plain rain landslide cross-section, side by side. [RS]

Posts sharing the video called it another glacier collapse, a repeat of Langtang. The problem with that story is
what the reports describe. Every account of the Kali Gandaki collapse describes days of rain and a soaked valley
wall, and none mentions glacier ice on that slope. `[verify: collapse elevation; no glacier on the failed slope]`
Langtang began about eighteen thousand feet up, where rock and glacier ice broke away together.
`[verify: about 5,600 m, competitor V1; confirm with ICIMOD]` The Kali Gandaki collapse matches the rain landslide
that Nepal sees every monsoon, only larger and caught on camera. The Himlung avalanche, coming off a high face with
snow and rock, is the event closer to Langtang's type. `[verify]` `[loop L3 closes]`

**Picture:** `7news-australians-missing-landslide.mp4` (anchor or family shot, muted) · the "Unknown" column fills.

Unknown, whether the debris blocked the river and backed up a lake. `[verify]` Unknown, how many of the missing
were visitors. The Australian broadcaster 7NEWS reported Australians missing, and it was not yet clear which event
they were caught in. `[verify: 7NEWS; number; which event]` Unknown, whether any radar or sensor was watching either
slope before it moved. `[loop L4 continues]`

*(chapter blackout)*

## A5 · Thirty two days (11:03)
**Picture:** g-aug-vs-sep map full: Langtang pin "Aug 26", Kali Gandaki pin "Sept 27", Himlung pin; distance lines
labelled in miles ("about 120 mi", "about 75 mi"); each pin's toll box with its date · `republicworld-5-horrifying-visuals.mp4`
(second segment, aerial). [VE]

On one map, the two disasters sit thirty two days and about a hundred and twenty miles apart.
`[verify: straight-line Langtang Lirung to the Kali Gandaki collapse site, about 190 km computed from approximate coordinates]`
Langtang is on the Trishuli, north of Kathmandu, and Himlung sits between the two, about seventy five miles from
Langtang. `[verify: about 124 km computed from approximate coordinates]` In August the trigger was a high mountain
face. In September it was rain on a valley wall and snow on a high camp.

What joins them is the season and the ground. Four months of monsoon leave the slopes of the middle hills wetter
than at any other time of year, and the high faces carry fresh snow over ice that has thawed all summer.
`[verify: seasonal thaw timing; ICIMOD]` After Langtang, scientists said the warning network had been built for
the wrong kind of disaster. `[verify: ICIMOD / CBC "About That" framing]` A month later, the September rain tested
that network again, in three valleys at once.

**Picture:** g-sensor-gap teaser: a river gauge icon glowing green, a slope icon beside it greyed out.

Across both months, Nepal's warning system measured one thing well, and it was the thing that moved last.
`[loop L6 open · cta-hinge]` `[loop L0 continues]`

## CTA · Storm-Ready Home (11:57)
**Picture:** 1.0 s dip in · `config.yaml channel.cta` file (Paul, 15.1 s, its own VO) · 1.0 s dip out · hard cut
to real footage for the payoff. No narration under it.

## A6 · After the rain (12:14)
**Picture:** `news18bihar-cyclone-arnab-bagmati.mp4` (second segment, a river gauge or swollen river shot) ·
g-sensor-gap full: a river gauge line rises only after a slope icon has already fallen in; a timeline marks "slope
fails" then "gauge sees it". [PAY]

It measured rivers. `[loop L6 closes]` Nepal's flood warnings come from river and rain gauges, which report when
water rises and send alerts to the villages downstream. `[verify: Nepal DHM early warning network]` A slope that
fails in three seconds gives a river gauge nothing to read until the mud is already in the water. In August, the
gauges nearest Langtang were swept away before they could warn anyone below. `[verify: ICIMOD / CBC]`

**Picture:** g-insar-creep returns small: the Langtang counter at "30 cm", then an empty strip labelled "Kali
Gandaki · Sept".

The tool that did see Langtang moving was satellite radar, which can measure ground motion from orbit to a fraction
of an inch. `[verify: InSAR precision]` It works only when someone processes the images in time and has a way to warn
the valley when a slope speeds up. `[loop L4 closes]` `[loop L0 closes]`

**Picture:** g-monsoon-calendar returns: the red pin moves from "Sept 27" to "today", the "normal withdrawal" mark
still ahead · a trekking-season bar opening across October.

The monsoon normally leaves Nepal in October, and the slopes stay wet for weeks after the last storm.
`[verify: DHM withdrawal forecast; soil drying time]` Trekking season on the Annapurna trails is opening now, on the
roads through the Kali Gandaki valley. `[verify]` The climbing season on peaks like Himlung runs through October, and
crews are already on those mountains. `[verify]` At Himlung, the tents had been up for days. `[loop L7 open]`

*(hold 3 s, base camp diagram at dawn, bed only under a moving picture)*

## Z · Close (13:13)
**Picture:** g-basecamp-diagram fades to the single camp · text-only name card returns, landing on the voice ·
slow push on `wion-climbers-guides-missing-avalanche.mp4` (a fourth, still shot of the peak) · g-outro. [HUMAN]

The climbers from the United Arab Emirates were due at Himlung on Thursday, October first.
`[verify: arrival date; whether the expedition was cancelled]` The people who went up first to make the mountain
ready were Sherpa climbers and kitchen staff, and at least four of them did not come home. `[verify: count; roles]`
`[loop L7 closes]` {NAME} was {AGE}. `[verify: CUT with the A3 name line if unpublished]` Nepal's monsoon is
forecast to leave in October, and until it does, the walls of the Kali Gandaki hold the same rain that brought one
of them down. `[verify: DHM forecast]` This was The Warning Hour.

*(outro tail 4 s, g-outro, bed out)*

---

## Loop chain
L0 why a mountain fell a month after Langtang, and who could have seen it (H → A6) · L1 what happened at the Himlung
camp (HT → A3) · L2 why late September (A1 → A2) · L3 is Kali Gandaki the same event as Langtang (A3 → A4 debunk) ·
L4 was anyone watching these slopes (I → A6) · L5 which toll is right (I → A4) · L6 the one thing the warning system
measured (A5 → CTA → A6, the cta-hinge) · L7 the tents at Himlung (A6 → Z)

## TTS copy notes (not narration)
- `{NAME}`, `{AGE}`, `{ROLE}`, `{VILLAGE}` are unfilled slots, not TTS text. Fill from a published source or cut
  both lines (A3, Z).
- Names: Kali Gandaki "KAH-lee gun-DAH-kee", Himlung "HIM-loong", Langtang Lirung "LAHNG-tahng lee-ROONG", Trishuli
  "tri-SHOO-lee", Dhaulagiri "DOW-lah-GEE-ree", Myagdi "MYAHG-dee", Baglung "BAHG-loong", Parbat "PUR-but", Palpa
  "PAHL-pah", Manang "mah-NAHNG", Syangja "SYAHNG-jah", Mirmi "MEER-mee", Jomsom "JOM-sum", Muktinath "MOOK-tee-naht",
  Nar Phu "nar POO", ICIMOD "ICK-ee-mod", SANA "SAH-nah", Arnab "AR-nub". Probe each once; respell only by measurement.
- "Oso" = "OH-so". "U.S." reads as letters.
