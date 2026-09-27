# ep-enderlin-2025 · edit_script.md (TTS segment format, from script_v2.md, 27 Sep 26 -- verbatim)

Lane: documentary (`/storm-episode`). Narration converted verbatim from `script_v2.md` (owner-locked, fact-checked in
`fact_check.md`) into `scripts/tts_episode.py`'s segment format (`parse_segments` docstring). Superseded the old v1
chapter-plan `edit_script.md` (git keeps history).

## Section ID map
`tts_episode.parse_segments` IDs must match `[A-Z]\d+-S\d+` -- a single uppercase letter, not two. `script_v2.md`'s
section labels map onto that regex as:
| script_v2.md section | edit_script.md ID prefix | why |
|---|---|---|
| H · Hook | H1 | fits as-is (single letter + number) |
| HT · Hook tail | T1 | 'HT' is two letters, doesn't match the regex; mapped to T (tail) |
| I · The night | I1 | fits as-is |
| A1..A6 (six acts) | A1..A6 unchanged | already single letter + number |
| CTA · Storm-Ready Home | (none) | no narration under it -- `config.yaml channel.cta` file carries its own VO |
| Z · Close | Z1 | fits as-is |

## CTA hinge
Segment before: **A5-S10** ("...a scientist at a federal lab had already written down a change he thought the scale
needed."). CTA file (`config.yaml channel.cta`, 15.1 s, own VO) mounts here, ~20:48 (87.6% of a 23:45 runtime).
Segment after: **A6-S1** ("Tony Lyza's change was to lower the line between E F four and E F five, slightly.").

## Conversion notes
- Narration is verbatim from `script_v2.md`; wording is unchanged. Only removed: `` `[loop ...]` `` margin tags and
  the standalone italic timing notes (`*(... void/blackout/hold/outro tail)*`), which are kept here as plain notes
  between segments for the editor, not as TTS text.
- Long script_v2.md paragraphs (up to 147 words) are split at existing sentence boundaries into multiple segments so
  every segment stays at or under ~60 words for TTS stability. No sentence in the source ran over 24 words, so no
  sentence needed splitting at a comma/"and".
- Each section's `**Picture:**` line is kept as the visual intent, attached to the first segment born from that
  paragraph; a paragraph split into several segments carries the picture note on the first one only (same shot
  continues into the rest).
- Homographs respelled in the TTS copy only (CLAUDE.md Voice; script_v2.md "TTS copy notes"), wording/meaning kept:
  "wind"/"winds" (noun, every use) -> "wihnd"/"wihnds"; "lives" (noun) -> "lyvz"; "Valley News Live" -> "Valley News
  Lyve". None of "read/lead/tear/bass/close/present/record" occur as narration in this script (checked).
- Zero open verify-tag markers: script_v2.md carried three (bracket-tag) mentions are all in its front-matter/word-table notes
  about the *previous* draft process, not inline in the narration body -- confirmed by scan, none carried into this
  file.
- Segment count: 107 (Z1-S3 signature closing footnote added 27 Sep 26 after the owner's draft review). Hook segment (H1-S1) is exactly the owner's locked line.

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** the owner-approved H2 motion graphic (27 Sep 26), not footage: WebGL night wedge (library tornado template) lit by lightning; popfig "June 20, 2025 · Enderlin, N.D." inside the first second; a red "EF5" stamp slams in on the word "five", then a struck-through "EF3" settles under it on "three", the thumbnail's own plate. Narrator from 0:00; drone bed and stamp hits, no siren.
> The weather service changed it to E F five, four months after they called it E F three.


## T1 · Hook tail (0:05)  <!-- mapped from 'HT' -- tts_episode.py's ID regex is [A-Z]\d+-S\d+, a single uppercase letter only -->

### T1-S1 — narration
**Picture:** g-drought-timeline flash: "Moore 2013" mark, a bar runs "12 Years", "Enderlin 2025" lands. Hard cut to El Reno 2013 on a PD radar still or a map with its 2.6 mile width drawn over section roads; a stamp "EF3" lands and stays, unstruck. Split frame holds both stamps: "Enderlin · EF5" and "El Reno · EF3".
> The Enderlin tornado was the first E F five in America in twelve years. In twenty thirteen, the widest tornado ever measured came down near El Reno, Oklahoma. Radar caught wihnds far past the E F five line, and it is still an E F three.

*(no void: cut straight into The night. Channel post-mortem 27 Sep 26: black holds before 1:00 cost 20-35 points of retention)*


## I1 · The night (0:23)

### I1-S1 — narration
**Picture:** master map, the track draws northeast then north from a point south of town · popfig "11:02 PM" · g-clock starts.
> The Enderlin tornado came down a little after eleven on a Friday night, June twentieth, twenty twenty five. It touched the ground about four miles south of Enderlin, a small town in southeast North Dakota, about forty miles southwest of Fargo. For nineteen minutes it curved north across open farmland.

### I1-S2 — narration
> At its widest it was more than a mile across, about eighteen football fields laid end to end.

### I1-S3 — narration
**Picture:** map pin on Highway 46 · text-only name cards "Michael and Katherine Pfaff-Dehn · 73", then "Marcario Lucio · 89".
> Three miles east of town, on Highway forty six, it hit the home of a couple named Michael and Katherine. They were both seventy three, and neither of them survived. On another stretch of the path, it hit the farm of Marcario Lucio, who was eighty nine.

### I1-S4 — narration
> His wife, Roberta, made it through the night, and the storm took Marcario's life. No North Dakota tornado had taken that many lyvz since nineteen seventy eight.

### I1-S5 — narration
**Picture:** NWS survey b-roll (PD), a team walking a debris field · popfig "EF3" · then a North Dakota map where twenty four small tracks land one by one.
> Within days, surveyors from the weather office in Grand Forks walked the path and gave it a number. They called it an E F three, with wihnds of about a hundred and sixty miles an hour. That is a violent tornado but not a rare one, and North Dakota had twenty four tornadoes that same night.

### I1-S6 — narration
**Picture:** split card returns: "El Reno 2013 · EF3" left, "Enderlin 2025 · EF3" right, a day counter under the right stamp starts to run.
> So until October, Enderlin sat on the books with the same number as El Reno. El Reno had radar numbers far past the E F five line, and Enderlin had something stranger lying on its path. Then the office that wrote E F three put out a statement saying the number had been wrong.

### I1-S7 — narration
> Its first number came from the same method every American tornado is rated by, and that method has a limit built into it.

*(blackout 0.7 s)*


## A1 · How a tornado gets its number (1:53)

### A1-S1 — narration
**Picture:** NWS survey team b-roll (PD), tape measures, a snapped tree · a NEXRAD dome (PD) with its beam drawn rising over a curved ground line.
> Nobody measures the wihnd inside a tornado at the spot where it hits the ground. The instruments are rarely there, and the few that are there do not make it through. The weather service's radars are fixed in place, often many miles from the storm.

### A1-S2 — narration
> The farther a radar beam travels, the higher above the ground it runs, because the earth curves away beneath it. So radar shows the storm, but not the wihnd at ground level, and the rating comes afterwards, from what the wihnd left behind.

### A1-S3 — narration
**Picture:** g-ef-scale: the six ratings stack up, each with its wind band landing on the voice · popfig "1971" on Fujita's name.
> The scale in use today is the Enhanced Fujita scale. It was built on the one Ted Fujita, a University of Chicago scientist, drew up in nineteen seventy one. An E F three covers wihnds from a hundred and thirty six to a hundred and sixty five miles an hour. An E F five starts above two hundred.

### A1-S4 — narration
> A survey team walks the path, sometimes for days, and looks at every broken thing. They match it against a list of twenty eight kinds of damage the scale recognizes. The list runs from a barn to a school to a hardwood tree.

### A1-S5 — narration
> Each kind has steps, from a few shingles gone to nothing left, and each step carries a wihnd speed. The tornado gets the highest number the damage can prove. Engineers at Texas Tech University led the work of writing that list, and the weather service adopted it in two thousand seven.

### A1-S6 — narration
> Today the teams carry tablets, and every photo they take is pinned to a spot on a map. They add aerial pictures, satellite images and radar, but the number itself still comes from the damage.

### A1-S7 — narration
**Picture:** g-ef-scale zooms into one indicator, a tree; its steps climb and hit a lid drawn across the top. Then a house indicator: two slabs side by side, one with anchor bolts drawn, one with nails.
> That word, prove, is the whole problem, because every kind of damage has a ceiling. Once a tree has been stripped of its bark and snapped, the scale has nothing higher to give it, whatever the wihnd was. A farmhouse can go higher, but only if it was built to hold.

### A1-S8 — narration
> When a house is swept off its foundation, surveyors check how it was tied down. Bolted to the concrete, a clean slab can mean E F five. Held on by a few nails, the same empty slab only proves a strong E F three or a low E F four.

### A1-S9 — narration
> Surveyors photograph the bolts, the nails and the straps, because the difference can be two full ratings.

### A1-S10 — narration
**Picture:** El Reno 2013: PD radar still, then a mobile radar truck (PD or licensed still only) · the 2.6 mile outline over open section roads · a stamp "EF5" lands with a date "June 2013", then flips to "EF3", "August 2013".
> That ceiling is where El Reno's number came from. El Reno came down on May thirty first, twenty thirteen, eleven days after the last E F five. A mobile radar truck from the University of Oklahoma measured wihnds of nearly three hundred miles an hour inside it.

### A1-S11 — narration
> For almost three months, the weather service listed it as an EF five, based on that radar. Then, that August, they took it back down to E F three. The rating goes by damage, and a radar reading is not damage.

### A1-S12 — narration
> The wihnd speeds on the scale are a specific thing, a three second gust about thirty three feet above the ground. Radar measures wihnd higher up and over a bigger volume of air, so the two numbers do not line up. Across most of its path, El Reno crossed open fields with little on them that could prove more.

### A1-S13 — narration
> So El Reno went from E F five down to E F three, and twelve years later Enderlin went the other way. Enderlin had the same kind of path, and until October it had the same answer.

### A1-S14 — narration
**Picture:** master map v2: farmsteads spaced far apart, shelter belts, the Maple River, power towers; Sentinel-2 ground scar if the tile and licence clear.
> Now look at what the Enderlin tornado had to work with. There were farmsteads spread far apart, shelter belts of trees, power towers and a river bank. There was no town in its path, no school and no neighborhood of modern homes.

### A1-S15 — narration
> It stripped the trees along the Maple River down to bare wood, and the survey could only count them as trees. It swept farmhouses clean, and the survey had to ask how they had been fastened down.

### A1-S16 — narration
> So the surveyors wrote down what the damage could prove. In June, it could prove about a hundred and sixty miles an hour, near the top of E F three. That was an honest number, and it was also a ceiling rather than a measurement.

### A1-S17 — narration
**Picture:** NWS PD photo of derailed freight cars (check the credit line photo by photo) · the rail line on the master map pulses.
> But one piece of the damage did not fit anything on the list. South of town, the tornado had crossed a rail line, and thirty three freight cars were off the tracks. The scale had no entry for a train, so in June the train could not raise the number.

### A1-S18 — narration
**Picture:** g-drought-timeline teaser: the Moore 2013 mark, then a long empty bar, still drawing.
> That same ceiling, the one that held Enderlin at E F three, has a much bigger charge against it. A federal study says it is the likely reason America went twelve years without a single E F five.

*(blackout 0.8 s)*


## A2 · Twelve years (6:06)

### A2-S1 — narration
**Picture:** g-then-now: the old F scale and the new EF scale as two bars, the F5 band "261 to 318 MPH" sliding down to the EF5 band "Over 200 MPH" · popfig "Feb 2007".
> The Enhanced Fujita scale replaced the old Fujita scale in February, two thousand seven. The old scale had put F five wihnds between two hundred and sixty one and three hundred and eighteen miles an hour. Engineers decided those numbers were too high for the damage they described, so the new scale lowered them.

### A2-S2 — narration
> A house swept off a good foundation now meant wihnds above two hundred.

### A2-S3 — narration
**Picture:** g-drought-timeline from the start · marks land one by one with PD stills: Greensburg (FEMA), Parkersburg, the four of April 27, 2011, Joplin (FEMA).
> On May fourth, two thousand seven, three months after the switch, the new scale had its first E F five. That was Greensburg, Kansas, where the tornado destroyed about ninety five percent of the town and eleven people lost their lyvz.

### A2-S4 — narration
> A year later, on May twenty fifth, two thousand eight, Parkersburg, Iowa, got the second, and the toll there was nine.

### A2-S5 — narration
> Then came April twenty seventh, twenty eleven, when four E F fives touched down in Mississippi and Alabama on one day. No single day since the new scale began has matched that. About two hundred and sixteen tornadoes formed across the South that day. The one at Hackleburg and Phil Campbell, in Alabama, took seventy two lyvz.

### A2-S6 — narration
> On May twenty second, less than a month later, the Joplin tornado took a hundred and fifty eight lyvz in Missouri. No single American tornado had taken more since nineteen forty seven.

### A2-S7 — narration
**Picture:** the El Reno and Piedmont 2011 mark lands, then a thin line reaches forward to a second El Reno mark in 2013 stamped "EF3".
> Two days after Joplin, an E F five hit El Reno and Piedmont, in Oklahoma, and six people lost their lyvz. That was a different storm from the El Reno tornado two years later, the widest one. So one Oklahoma town has an E F five and an E F three, and the lower number belongs to the bigger storm.

### A2-S8 — narration
**Picture:** Moore 2013, FEMA PD footage of the Plaza Towers area · popfig "May 20, 2013" · then a small inset "Moore · May 3, 1999 · F5".
> Then, on Monday, May twentieth, twenty thirteen, an E F five crossed Moore, Oklahoma. Twenty four people lost their lyvz, and seven of them were children at Plaza Towers Elementary School. Moore had neighborhoods of modern homes in the path, and surveyors found some of them swept off their slabs.

### A2-S9 — narration
> The same city had been hit by an F five on May third, nineteen ninety nine. A mobile radar measured about three hundred and one miles an hour in that storm. It kept its five, because it had houses to prove it.

### A2-S10 — narration
**Picture:** the timeline keeps drawing past Moore with no marks; a day counter runs to "4,414 Days".
> That made nine E F fives in six years. From nineteen fifty to twenty thirteen, America averaged nearly one F five or EF five a year. So nine in six years was a little above the usual pace. After Moore, there were none.

### A2-S11 — narration
> The count ran for four thousand four hundred and fourteen days, from Moore to the night of Enderlin. It was the longest stretch without an F five or an E F five since official counts began in nineteen fifty.

### A2-S12 — narration
> The first storm that could have broken the gap was El Reno, eleven days after Moore, and its five was taken back. For twelve years, the worst tornadoes we saw on the news were all rated E F four or lower.

### A2-S13 — narration
**Picture:** four EF4 cards slide in, each with a PD NWS or FEMA damage still: "Mayflower–Vilonia 2014 · 190 MPH", "Rochelle–Fairdale 2015 · 200 MPH", "Mayfield 2021 · 190 MPH", "Rolling Fork 2023 · 195 MPH"; the EF5 line sits just above the tallest bar.
> Strong tornadoes kept coming in those years, and some of them started long arguments. Meteorologists argued over Mayflower and Vilonia in Arkansas in twenty fourteen, and over Rochelle and Fairdale in Illinois a year later. They argued over Mayfield, Kentucky, in twenty twenty one, and over Rolling Fork, Mississippi, in twenty twenty three.

### A2-S14 — narration
> The Mayfield storm stayed on the ground for about a hundred and sixty five miles, from Tennessee across western Kentucky, on a December night.

### A2-S15 — narration
> All four were rated E F four, and their final numbers sat near the line. Mayflower and Vilonia got a hundred and ninety miles an hour, and so did Mayfield. Rolling Fork got a hundred and ninety five. Rochelle and Fairdale got two hundred, one mile an hour short of an E F five.

### A2-S16 — narration
> That left meteorologists with a question they could not settle for years. Some said the ratings had grown too cautious, and others said the damage in those years had simply never reached E F five. Many said it was some of each. Underneath it all sat one plain question.

### A2-S17 — narration
> Either the most violent tornadoes had become rarer, or the way they were rated had changed.

### A2-S18 — narration
**Picture:** g-person Tony Lyza (text-only card, no photo slot) · "NOAA National Severe Storms Laboratory" · beige citation card: "Where Have the EF5s Gone?" Bulletin of the American Meteorological Society, 2025.
> Tony Lyza, a research meteorologist at NOAA's National Severe Storms Laboratory, set out to answer it. The American Meteorological Society published his study in twenty twenty five. It was called "Where Have the E F Fives Gone?" He looked at the gap with statistics, and he concluded that a real drop in tornado strength was highly unlikely.

### A2-S19 — narration
> The likelier cause, he found, was how surveys and ratings had shifted after the switch to the new scale.

### A2-S20 — narration
**Picture:** the ceiling lid from A1 slides over the whole drought bar · then the master map, the track glowing.
> So the ceiling behind the twelve years was the same ceiling the Enderlin survey hit in June. And the proof that Enderlin had gone past it was lying somewhere on a twelve mile path through Ransom and Cass counties.

*(blackout 0.8 s)*


## A3 · Nineteen minutes (10:23)

### A3-S1 — narration
**Picture:** SPC watch map (PD) · popfig "3:45 PM" · GOES satellite loop (NOAA PD) of storms building over eastern Montana.
> At three forty five that afternoon, forecasters put out a severe thunderstorm watch for southwest and south central North Dakota. The storms behind it were building over eastern Montana. At eight fifteen, the Storm Prediction Center sent out a mesoscale discussion, which is a short bulletin about one patch of the map.

### A3-S2 — narration
**Picture:** the discussion as a beige text card, key words lifting on the voice: "surface based", "Red River Valley" · then a cross-section MG: a storm riding on a cool layer, then its inflow reaching down to the ground.
> It said the storms in eastern North Dakota were becoming surface based as they moved toward the Red River Valley. It said that raised the tornado threat. Storms at night on the Plains often ride on top of a cooler layer of air near the ground. That layer tends to keep their spin from reaching the surface.

### A3-S3 — narration
> A surface based storm pulls its air from the ground itself, and that is the air tornadoes form in.

### A3-S4 — narration
**Picture:** popfig "120 to 150 MPH" over the discussion card.
> The same bulletin put the strongest tornado wihnds at a hundred and twenty to a hundred and fifty miles an hour. That was the forecast for the night, and the number the Enderlin tornado ended up with sits far above it.

### A3-S5 — narration
**Picture:** g-radar, a self-made Level II velocity re-plot (NEXRAD open data); two supercells labelled as they cross the state · popfig "24 Tornadoes".
> That night, North Dakota had twenty four tornadoes, many from two supercells, the rotating kind of thunderstorm. Most supercells never make a tornado at all. A night with that many is rare, and the Enderlin tornado was one of the twenty four. It was part of a larger outbreak that ran from June nineteenth to June twenty second.

### A3-S6 — narration
> A derecho, a long line of damaging straight wihnds, came through in the middle of it.

### A3-S7 — narration
**Picture:** g-clock at 11:02 · master map zooms to the touchdown point on 58th Street SE, Ransom County.
> At two minutes past eleven, it touched down along Fifty Eighth Street Southeast, in Ransom County. From there, it had nineteen minutes and twelve miles of farm country ahead of it. That works out to about thirty eight miles an hour across the ground. It came down after dark.

### A3-S8 — narration
> A two thousand eight study found night tornadoes about two and a half times as likely to take lyvz as daytime ones.

### A3-S9 — narration
**Picture:** g-radar: the self-made Level II re-plot, velocity panel with the couplet ringed, then the correlation coefficient panel with the debris signature ringed; timestamps from the data, not from the script.
> At that hour, radar gave the clearest view anyone had of it. On the Grand Forks radar, wihnds rushing toward the dish and away from it sat side by side. That is the mark of a tight rotation. Then the radar picked up a debris signature, a patch of lofted debris the radar can tell apart from rain.

### A3-S10 — narration
> The radar could see what the storm was lifting, but not how hard the wihnd blew at the ground.

### A3-S11 — narration
**Picture:** master map: the rail line pulses south of town · NWS PD photo of tipped grain cars (credit checked) · popfig "33 Cars".
> Enderlin began as a railroad town, and the story told about its name is that it marked the end of the line. South of Enderlin, the path crossed a rail line where freight cars stood on the tracks. When the survey team got there, thirty three cars were off the rails.

### A3-S12 — narration
> Nineteen were grain cars, still loaded, and fourteen were empty tanker cars. A loaded grain car like those weighs nearly three hundred thousand pounds. The final survey puts the rail cars where the tornado was at its strongest. One of the tankers was lying almost five hundred feet from the track.

### A3-S13 — narration
> In June, that was one strange detail on a long list, and it took months to turn it into a number.

### A3-S14 — narration
**Picture:** PD or credit-cleared photos of the Maple River woods, the trunks stripped pale · slow push, no hold over 6 s.
> Farther on, the tornado crossed the Maple River and flattened the woods along the bank. The trees that stayed standing were stripped of their bark, which surveyors call sandpapering. It looks like the worst thing a tornado can do to a tree. On the scale, even a tree stripped that bare can only prove so much.

### A3-S15 — narration
**Picture:** Highway 46 on the map · a PD or credit-cleared photo of a downed transmission tower · pins for the homes near town.
> East of Enderlin, it crossed Highway forty six. It knocked down four electrical transmission towers there, and about ten homes near town were damaged. This was the stretch where Michael and Katherine had their home.

### A3-S16 — narration
**Picture:** the track enters Cass County; NWS PD photo of a swept foundation (credit checked) · text on the voice: "Swept Clean".
> In Cass County, it ran across farmsteads along County Road thirty eight and the roads around it. Several farmhouses there were wiped off their foundations, and the survey described the debris as swept clean. Swept clean can mean EF five, but only if the house was bolted down.

### A3-S17 — narration
> That is the question the June survey had to answer, one farm at a time.

### A3-S18 — narration
**Picture:** g-clock hits 11:21 · the track ends five miles southwest of Alice · the full Enderlin track at scale, then the El Reno outline ghosts in beside it at the same scale.
> At twenty one minutes past eleven, it lifted about five miles southwest of Alice. Its path ran just over twelve miles, and at its widest it measured one point oh five miles. El Reno, at its widest, was two point six miles, more than twice as wide.

### A3-S19 — narration
> So the narrower tornado ended up with the higher rating, and the reason sat on that rail line south of town.

### A3-S20 — narration
**Picture:** NWS survey b-roll (PD) · the EF3 stamp from I, holding · g-person Carl Jones (text-only card) slides in.
> The survey logged no injuries on the whole path. The Grand Forks office is run by Melinda Beerends, its meteorologist in charge, and within days it had its E F three. The rating could have stayed there for good. Carl Jones, a meteorologist in that office, explained later why it did not.

*(blackout 0.8 s)*


## A4 · The second look (14:39)

### A4-S1 — narration
**Picture:** beige quote card, words land in narration order: "This particular set of damage that we saw kind of stood out as unique. We wanted to investigate further." · Carl Jones, NWS Grand Forks, MPR News, Oct 8, 2025.
> He said, and this is a direct quote, "This particular set of damage that we saw kind of stood out as unique." Then he added, "We wanted to investigate further." The damage he meant was on the rail line. And nothing in the scale's list of twenty eight could turn a freight car into a wihnd speed.

### A4-S2 — narration
**Picture:** g-ef-scale returns: the house indicator with its steps and wind speeds, then an empty row labelled "Freight Car" with no steps in it.
> For a barn or a house, the scale says how much wihnd it takes to lift the roof or push over the walls. For a freight car there was no such entry, so the office had to find one somewhere else. A re-survey means going back to the path, sometimes months later, and measuring again.

### A4-S3 — narration
> Along the way, the question moved from the houses to the rail cars. It became a question of how much wihnd it takes to throw a tank car.

### A4-S4 — narration
**Picture:** no drone footage (chaser footage, no licence); the master map with survey points appearing, and an attributed text card "Drone Video · Aaron Rigsby".
> Part of the second look came from the air. A storm chaser named Aaron Rigsby had flown a drone over the damage, and his video ran about thirteen minutes. The office went through that footage as part of the review. An aerial view shows a whole debris field at once, which a team on foot cannot see.

### A4-S5 — narration
**Picture:** map pulls north across the border · text card "Northern Tornadoes Project · Western University, Canada".
> The office also brought in help from Canada. Engineers from the Northern Tornadoes Project, at Western University, joined the re-survey as wihnd damage experts. The project was started in twenty seventeen to find and survey every tornado that touches down in Canada.

### A4-S6 — narration
> Their team, which includes Greg Kopp of Western University, is credited with the forensic side of the work.

### A4-S7 — narration
**Picture:** a Canada map, a pin at Elie, Manitoba · popfig "June 22, 2007" · a stamp "F4" struck through by "F5", dated "September 2007".
> Canada knows about late upgrades. Its only F five came down at Elie, Manitoba, on June twenty second, two thousand seven. It was first rated F four, and that September it was raised to F five.

### A4-S8 — narration
**Picture:** g-mechanism, first half: a grain car side-on, a wind arrow on its broad side, a pivot marked at the far rail, the car rolling over it.
> Part of the estimate came from the grain cars. To tip a car over, the wihnd has to push on its broad side hard enough to lift it over the far rail. A loaded grain car is so heavy that tipping one takes a strong wihnd before anything flies at all.

### A4-S9 — narration
> That set a floor under the estimate, and the tanker set a much higher one.

### A4-S10 — narration
**Picture:** beige citation card: Miller et al., Monthly Weather Review, 2024, "Estimating Wind Speeds in Tornadoes Using Debris Trajectories of Large…" · g-person Connell Miller (text-only).
> The biggest piece came from a paper published in twenty twenty four, the year before Enderlin. Its first author was Connell Miller, a former wihnd researcher with the Northern Tornadoes Project. He now directs the Northern Mesonet Project. The paper came out in Monthly Weather Review.

### A4-S11 — narration
> It showed how to estimate a tornado's wihnd from how far it carried large objects.

### A4-S12 — narration
**Picture:** g-mechanism, second half: a tanker silhouette, a weight arrow pointing down, a wind arrow pushing sideways, an arc to a landing mark; a ruler on the ground marked "50 m · about 160 ft".
> Wind pushes on a car, the car's weight pulls it down, and the car only leaves the ground when the push wins. The farther a heavy, compact object travels through the air, the stronger that push had to be. The paper drew a line at fifty meters, which is about a hundred and sixty feet, or half a football field.

### A4-S13 — narration
> A large, compact object carried farther than that generally means wihnds at the E F five level. The rule counts objects that flew through the air, not ones that rolled or slid along the ground.

### A4-S14 — narration
**Picture:** master map rail segment · the tanker's arc draws to "almost 500 ft", the 160 ft line flashes about a third of the way along · popfig "About 3×".
> The Enderlin tanker weighed about seventy thousand pounds, empty, which is about as heavy as a dozen full size pickup trucks. It had gone almost five hundred feet, more than one and a half football fields, and nearly three times the line.

### A4-S15 — narration
> So the scale finally had something to measure besides houses and trees, and it pointed well past E F three.

### A4-S16 — narration
**Picture:** split card returns: "El Reno · Radar" left, "Enderlin · Tanker Car" right.
> El Reno had its radar, and Enderlin had a tanker car in a field, and only the tanker became a rating.

### A4-S17 — narration
**Picture:** quote card, one line only.
> Miller said the case "exemplifies the importance of integrating engineering analysis and scientific research into operational meteorology." He also called it, in his words, "a powerful new tool for rating storms that produce extreme yet unconventional damage." Okay, so a train is about as unconventional as damage gets. By early October, the Grand Forks office had its new number ready.

### A4-S18 — narration
> It was the number the whole country had gone twelve years without.

*(blackout 0.8 s)*


## A5 · October 6 (18:18)

### A5-S1 — narration
**Picture:** beige citation card, NWS Grand Forks statement, Oct 6, 2025 (PD) · popfig "Oct 6, 2025" · the EF3 stamp struck through, red EF5 lands.
> On Monday, October sixth, twenty twenty five, the Grand Forks office put out its revised rating. The Enderlin tornado was now an E F five, with peak wihnds estimated at more than two hundred and ten miles an hour. The rating rested on the train rather than on a house, which is rare for an E F five.

### A5-S2 — narration
**Picture:** g-then-now: a wind ladder with three rungs landing on the voice: "8:15 PM Forecast · 120 to 150", "June Survey · 160", "October · 210+".
> At eight fifteen that night, forecasters expected the strongest tornadoes to reach a hundred and twenty to a hundred and fifty. In June, the survey said about a hundred and sixty. In October, it said more than two hundred and ten. Nothing about the storm changed between June and October, but the survey found a way to prove more.

### A5-S3 — narration
**Picture:** g-drought-timeline closes: the counter stops at 4,414, the Enderlin mark lands, the long bar turns from grey to red · then a US map with every EF-era EF5 dot; Enderlin sits far north of the rest.
> It was America's first E F five since Moore, and the twelve year gap was over. Within days, the upgrade was on Valley News Lyve, Minnesota Public Radio and Fox Weather. It went onto the official list of American E F fives, the same list the twelve years had been counted from.

### A5-S4 — narration
> A change like this also goes into Storm Data, the federal database of every tornado, which the National Centers for Environmental Information keeps. Every future study of American EF fives will count Enderlin, because it is now in that database. Moore's E F five had been put at about two hundred and ten miles an hour.

### A5-S5 — narration
> Enderlin's estimate is more than that. It also sits farther north than any other EF five since the new scale began.

### A5-S6 — narration
**Picture:** a North Dakota map, a Fargo pin · popfig "June 20, 1957".
> North Dakota had seen the top of the scale before. At Fargo, on June twentieth, nineteen fifty seven, an F five came down, sixty eight years to the day before Enderlin. That storm took at least ten lyvz in Fargo.

### A5-S7 — narration
**Picture:** the El Reno split card, both stamps flipping in opposite directions with their dates.
> El Reno lost its five in August, twenty thirteen, and Enderlin gained one in October, twenty twenty five. Both times, the reason was the same rule, that the rating goes by what the damage can prove.

### A5-S8 — narration
**Picture:** a PD survey photo of an empty farmhouse slab (credit checked), slow push · then a FEMA safe room diagram (PD, FEMA P-361) · popfig "250 MPH".
> The new number did not change the path, the twelve miles, or the three people the storm took. It did not change what anyone knew at eleven o'clock that night either, because a rating always comes after the storm. But it did put a figure on what a building there would have had to stand up to.

### A5-S9 — narration
> FEMA builds its guidance for tornado safe rooms around wihnds of two hundred and fifty miles an hour. If you have a safe room built to that standard, it is rated above what the survey gave Enderlin.

### A5-S10 — narration
**Picture:** the four EF4 cards from A2 return, each with a small "?" pulsing beside the EF4.
> It took a hundred and eight days from the storm for Enderlin to move up two full steps. That put the same question back on every high end E F four since Moore, including Mayfield and Rolling Fork. Months earlier, a scientist at a federal lab had already written down a change he thought the scale needed.


## CTA · Storm-Ready Home (20:48)  <!-- no narration under the CTA -- config.yaml channel.cta file carries its own VO; no ID segment needed -->


## A6 · The open case (21:07)

### A6-S1 — narration
**Picture:** real footage first (PD NWS survey b-roll), then g-then-now: a bar with the EF4 and EF5 bands and the line between them sliding down a notch; g-person Tony Lyza returns.
> Tony Lyza's change was to lower the line between E F four and E F five, slightly. His study argued that a small move would line up the new scale with the old Fujita scale used before two thousand seven. A lower line would pull the top of the E F four range into E F five.

### A6-S2 — narration
> That is where the arguments over Mayfield and Rolling Fork have always sat. Enderlin was rated on the scale as it stands, with the line where it has been since two thousand seven.

### A6-S3 — narration
**Picture:** text card "Wind Speed Estimation in Tornadoes · ASCE / AMS standard" over survey b-roll.
> Engineers and meteorologists are also writing a new standard for estimating tornado wihnds. It adds more kinds of damage and more ways to measure, including radar and thrown objects. The work runs under the American Society of Civil Engineers and the American Meteorological Society.

### A6-S4 — narration
**Picture:** g-mechanism returns small: the tanker arc, then the same arc over an empty field with nothing to throw.
> The Enderlin method has a limit of its own. It needs a large, heavy object in the path, thrown far enough to measure, and most tornadoes never cross a train. El Reno had radar and open fields, and it still has its E F three.

### A6-S5 — narration
**Picture:** a map of Oklahoma with an Enid pin · text card "Enid, Oklahoma · 2026".
> In twenty twenty six, a tornado at Enid, Oklahoma, landed in the same argument over whether it reached E F five. The ratings matter past any one town, because they are the data scientists use to ask whether violent tornadoes are becoming rarer.

### A6-S6 — narration
> That is the question Lyza's study put to the twelve years, and the Enderlin rating ended the gap without settling it. If surveys shifted in two thousand seven, the counts before and after that year cannot be compared straight across.

### A6-S7 — narration
**Picture:** the tanker arc from A4 replays small in a corner of the survey b-roll · the Miller citation card returns.
> What Enderlin did change is the toolkit. The weather service has now used a debris flight to rate a tornado, and Miller said that use matters for future tornado assessments. When a survey next finds something large thrown far from where it stood, a published method can turn that distance into wihnd.

### A6-S8 — narration
**Picture:** PD NWS warning graphic (polygon over a county map) · then the survey b-roll, a team walking at dawn.
> For anyone in tornado country, the number that matters on the night is the warning, and it comes before any survey. For most of us, a rating is a number in a news story days later. For the surveyors, it is weeks of work on foot, and at Enderlin it took months.

### A6-S9 — narration
> On the Enderlin path, one part of what they found was never going to change with any rating.

*(hold 3 s, the master map at dawn, bed only under a moving picture)*


## Z1 · Close (23:14)

### Z1-S1 — narration
**Picture:** the master map, the track fading to a single line · text-only names card, each name landing on the voice · slow push on a PD survey photo of the path (credit checked) · g-outro.
> The storm that came through Enderlin on June twentieth was rated an E F three. A hundred and eight days later, it became an E F five. Three people lost their lyvz on its path, and the Cass County Sheriff's Office released their names on Sunday, June twenty second.

### Z1-S2 — narration
> Michael and Katherine, both seventy three, were in their home on Highway forty six, three miles east of town. Marcario Lucio was eighty nine, and his wife, Roberta, survived the storm that took him.

### Z1-S3 — narration
**Picture:** the channel title card (DESIGN.md "Signature closing footnote": it IS the outro).
> Tornadoes don't ask permission. But they do send warnings, even in the dark. Learn what yours sounds like, so when it comes, you already know what to do. This was The Warning Hour.

*(outro tail 4 s, g-outro, bed out)*

