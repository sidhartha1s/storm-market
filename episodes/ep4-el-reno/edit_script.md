# ep4-el-reno · edit_script.md (v4b: act outline, hook, intro, acts 1 and 2; acts 3 to 5 not written yet)

Lane: documentary (`/storm-episode`). Built on the angle the owner locked on 9 Oct 26 (`angle.md`). Facts from
`research/angle-facts-2026-10-09.md` (wins where it disagrees) and `research/facts.md`. Status: DRAFT, nothing locked;
hook and intro wait on the fact-check fan-out, the grader and the owner.

## A. Header
- **Title (owner, verbatim):** El Reno 2013: The Safest Place Was Home
- **Target runtime:** 20 to 25 min; planned at 23:00 until `word_budget.py` sizes it from a probe at the shipping tempo.
- **Claim (locked, copied):** On the night of May 31, 2013, 21 people lost their lives around Oklahoma City, and not one of them was inside a building.
- **Dominant question:** the viewer keeps watching to find out why, on a day of nineteen tornadoes across Oklahoma, every one of the twenty-one lives was lost outside a building and none inside one.
- **Architecture:** Detective, with one Explanation-with-a-twist act (A2).
- **Scope held in every act:** "that night" or "on May 31". The weather office counts one more flood loss on the morning of June 1 in Okfuskee County; it is outside the Claim and outside the 21 pins.

## Section ID map
`tts_episode.parse_segments` IDs must match `[A-Z]\d+-S\d+`.
| Section | ID prefix |
|---|---|
| Hook (Paul on camera) | H1 |
| Hook tail | T1 |
| Intro, the night and the count | I1 |
| Acts one to five | A1..A5 |
| Book ad | (none: the `config.yaml channel.cta` file carries its own VO) |
| Close | Z1 |

## B. Act outline
Times are planning numbers for a 23:00 cut. Shares are of the full runtime.

| Section | Planned time | Share | What it proves toward the Claim | Loop | Named person it follows |
|---|---|---|---|---|---|
| H1, T1, I1 | 0:00 to 2:10 | 9.4 % | States the Claim, the count (8 in vehicles, 12 in drains, 1 in a flooded vehicle) and the roster. | Opens L1 (episode) and L2 (the two crews). | Mike Bettes and Tim Samaras, named only. |
| A1 · A city in its cars | 2:10 to 5:30 | 14.5 % | The 21 were where they were because a city left its houses: a Friday rush hour, Moore eleven days earlier, people told they could not survive above ground, advice to drive south. The advice is given in the assessment's own sentence, no one named yet. | Opens and pays L3 (what made people leave solid houses). Ends by opening L4 (the tornado they drove toward was not one tornado). | Richard Henderson, the amateur chaser who left his home near El Reno and sent a photo at 6:05 PM: the first pin on the map. |
| A2 · The tornado inside the tornado | 5:30 to 9:00 | 15.2 % | The danger was not the 2.6 mile circulation, which nearly stopped. It was small vortices inside it, moving at up to about 175 miles an hour. Here "widest ever recorded" and "about 295 miles an hour" arrive as facts. Both crews drove in on the weak side and may not have known they were inside. | Pays L4. Keeps L2 open with the radar picture the viewer now needs. | Joshua Wurman, lead author of the 2014 radar study (mechanism chapter: one researcher, one institution). |
| A3 · Two vehicles, minutes apart | 9:00 to 13:10 | 18.1 % | Two crews inside the same tornado on two roads, US-81 and Reuter Road. The SUV met a small vortex crossing fast; about four minutes later the car met it sitting nearly still for about twenty seconds. The two facts sit side by side and the script never says "this is why". The TV crew's own footage runs here as one sequence under narration. | Pays L2 (open question one). Last segment opens L5, the `cta-hinge`. | Mike Bettes and driver Austin Anderson; Tim Samaras, Paul Samaras and Carl Young; Dan Robinson as the last man to see the Cobalt. |
| Book ad | 13:10 | starts at 57.2 % | Sits between the tease and its payoff. | Inside L5. | none |
| A4 · The twelve and the warning gap | 13:30 to 18:30 | 21.7 % | Twelve people, eight of them aged eight or under, went into two storm drains to hide from tornadoes that were E F zero and E F one in the city, and water took them. The family of seven left their house near NW 26th and Meridian when the sirens sounded, went "only a few feet away" into a drainage ditch and hid under a table carried from the house (News 9, confirmed). Enma Aguilar's sentence that they thought the ditch "was the safest spot" runs as attributed text on screen, never as a voice. The assessment names the lack of Spanish-language warnings beside the family of seven; the script says it sits beside them, never that it caused their choice. Then the fairness block at about 15:45 to 17:10 (68 to 75 %): "the problem with that story is" the weather office's own 1 PM tweet about fleeing by car, set next to the broadcast advice. | Pays L5 in its first sentence (open question two). Opens and pays L6 (who told the city to drive). Ends by opening L7 (all 21 pins on one map, and what is missing from it). | Samuel Cifuentes, who walked his family out of the house; Yolanda Santos and her three children; Enma Aguilar (attributed text); Deputy Fire Chief Marc Woodard; Mike Morgan and Gary England in the fairness block. |
| A5 · The map with 21 pins | 18:30 to 22:20 | 16.7 % | The answer. The strongest winds sat in small vortices that crossed no structure, which is also why the rating ended at E F three after the weather office raised it to E F five on June 4, 2013 (statement confirmed; the date it went back still needs its source); every tornado that entered the city was E F zero or E F one; the water went to the lowest ground. The pins sit on roads and in drains, and no pin sits on a building. | Pays L7, then L1 (open question three) in the last 30 to 60 s. | The weather office surveyors in Norman; Harold Brooks of NOAA on "get underground or you will not survive" messaging. |
| Z1 · Close | 22:20 to 23:00 | 2.9 % | One fact with a dated forward window, then the signature line. | none | none |

Each act changes what the viewer understood: A1 the city went out to meet the storm; A2 the wide tornado was not the threat; A3 minutes and yards decided between two crews, and no source names the cause; A4 the largest group was hiding, not driving; A5 the facts every other video opens with turn out to be the answer.

### Loop registry
| Loop | Opens | Closes |
|---|---|---|
| L1 episode: why nobody lost their life indoors | H1-S1, T1-S1 | A5, last 30 to 60 s |
| L2: why one crew survived (facts side by side, no cause stated) | I1-S8 | A3 |
| L3: what made people leave solid houses | A1, first segment | A1 |
| L4: what was inside the wide tornado | A1, last narration segment | A2 |
| L5 `cta-hinge`: who the twelve were | A3, last segment (Paul) | A4-S1, first sentence |
| L6: who told the city to drive | A4, after the family of seven | A4, fairness block |
| L7: what is missing from the 21-pin map | A4, last segment | A5 |

### Book-ad hinge
- **Segment before:** the last segment of A3, Paul on camera, 25 words at most. It is the line that the home was the safe place, and it teases the twelve who left theirs.
- **Book ad:** mounts at about 13:10, 57.2 % of a 23:00 runtime, inside `config.yaml channel.cta.window` [0.40, 0.60]. 20 s is budgeted until the file's length is read.
- **Segment after:** A4-S1. Its first sentence is the payoff, first three words if possible: the family of seven and how far they went from their own door ("only a few feet away", News 9, confirmed).

### Paul on camera (besides the hook), position and job only
1. About 5:25, last line of A1: the owner's hook callback at the act seam; names the hook's claim and points at what was inside the tornado.
2. About 7:10, middle of A2: the turn from how wide it was to what was inside it; names "the tornado inside the tornado" and defines it in twelve words or fewer.
3. About 11:40, A3, after both vehicles have been struck: sets the two strikes side by side in one breath, two facts and no cause.
4. About 13:00, last segment of A3: the `cta-hinge` tease, 25 words at most.
5. About 21:30, A5, at the full 21-pin map: the answer line that returns to the hook's claim, before the close.

### Open items the later acts must tag (from angle-facts "Still open")
Fact check 9 Oct 26 (`fact_check.md`): the radar paper reads as ONE interior sub-vortex striking both vehicles, racing across US-81 at the S U V and nearly stopped over Reuter Road at the car about four minutes later. A2 and A3 are written to that, never as two different vortices, and the sentence carries a verify tag until the paper's authors' wording is matched line by line.
Richard Henderson's age; the date the rating went back to E F three (the June 4 upgrade statement is confirmed); the pairing of the press names with the table rows (the News 9 report on the family of seven is read and confirmed); the News 9 report of June 9 on the last recovery; one spelling for the family's names, which differ between Fox and News 9 (Christopher and Leslie against Cristofer and Lesly, Floridalma against Florinda); the exact broadcast words; Joshua Wurman's institution; the June 1 flood loss. Each gets a verify tag where it is written, or stays out.

## Writer notes
- Narration numbers follow the shipped Enderlin copy: spelled out, no hyphen ("twenty one"). H1-S1 is the owner's line verbatim, hyphen included.
- "wind" does not occur in the hook, tail or intro. No homograph is respelled here; respelling waits for a TTS probe (`references/homographs.md`).
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- A1 and A2 also avoid "wind" and "record" as a noun ("the air inside them", "ever recorded"), so no homograph waits on a probe there.
- A Paul slot is a heading with a Job and a Budget line and no blockquote; `parse_segments` skips it until his line is written.
- The estimated times on the section headings come from the word counts at the Enderlin intro's shipped pace. They are estimates until a probe at this episode's tempo.

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** Paul on camera, full frame, frame one, speaking this line and nothing else. Popfig "May 31, 2013 · Oklahoma City" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> Twenty-one people lost their lives that night, and not one of them was inside a building.

*([loop L1 open]: why nobody lost their life indoors. Closes in A5.)*


## T1 · Hook tail (0:05)

### T1-S1 — narration
**Picture:** hard cut on the first word to mid-action footage, never black: a real clip of the evening sky and loaded highways around Oklahoma City on May 31 (news or public domain; no chaser footage without a licence). A counter "19 tornadoes in Oklahoma · National Weather Service" lands on "nineteen". On "Twelve of the twenty one": twenty-one small markers appear in a row and twelve of them light. One bed swell under the last clause, no siren.
> On May thirty first, twenty thirteen, the weather service counted nineteen tornadoes across Oklahoma. Twelve of those twenty one people had taken shelter from the tornadoes, and no tornado took their lives.

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The night and the count (0:18, runs to about 2:12)

### I1-S1 — narration
**Picture:** the master map opens: central Oklahoma, Oklahoma City labelled, El Reno marked to its west. Popfig "6:03 PM" and the g-clock starts. A real clip of the tornado over open fields (public domain or licensed news). A bar marked "2.6 miles" draws across the section roads on the last sentence.
> It was a Friday, and the storms arrived around rush hour, when many people were already in their cars. At six oh three PM, a tornado touched down in open farmland near El Reno, a town west of Oklahoma City. It stayed on the ground for about forty minutes and grew to two point six miles wide.

### I1-S2 — narration
**Picture:** the weather service's assessment on screen, Appendix C, cropped to the table rows. The "Circumstance" column is read down: eight rows highlight and the word "Vehicle" underlines in each. On the map eight pins drop along the El Reno track. Eighteen other small tracks draw in grey, each with a "0". A soft hit on each group, not on each pin.
> The National Weather Service later published a table of every life lost that night, with each person's age and what they were doing. Eight were in the path of the El Reno tornado, and all eight were in vehicles. Eighteen other tornadoes touched down that day. None took a life.

### I1-S3 — narration
**Picture:** the map slides east to Oklahoma City. Public domain footage of flooded city streets that night. Back to the table: one row "Vehicle, flash flood", then twelve rows "Sheltering in drainage ditch, flash flood" highlight together. The age column ticks eight of the twelve. Text card "5 months". Twelve pins land at two points in the city, one more for the vehicle. The bed thins to rain.
> The other thirteen were lost to flood water, as the same storms poured rain over the Oklahoma City area. One of them was in a vehicle. Twelve were sheltering in drainage ditches and storm drains, and eight of them were young children. The youngest was five months old.

### I1-S4 — narration
**Picture:** [RS] [VE] the full map, all twenty-one pins lit for the first time. Every pin sits on a road or a drain; the building icons on the map stay unlit. Text line "0 of 21 inside a building · NWS Service Assessment, Appendix C". Hold the map through the second sentence. Pin positions wait on sourcing [verify: a location for each of the 21 Appendix C rows, needed to place the pins; the table gives a circumstance, not a place].
> That table does not list a single house, store, school or storm shelter. By that count, the safest place around Oklahoma City that night was home, and many people had just left theirs.

### I1-S5 — narration
**Picture:** a real news aerial of a jammed highway that evening. Popfig "Moore · May 20, 2013 · EF5", then "11 days earlier". Study card "6 metro areas, 2011 to 2018 · Weather, Climate, and Society, 2022" over the traffic.
> Eleven days earlier, an E F five tornado had gone through Moore, Oklahoma. People later told the weather service that fear from that day led them to do things they normally would not. A twenty twenty two study compared tornado evacuations in six American metro areas, and this was the largest of them. Fear explains the traffic. It does not explain why not one life was lost inside a building.

### I1-S6 — narration
**Picture:** the map pushes in on the track. Two vehicle markers on two labelled roads, "US-81" and "Reuter Road", so the two roads read at a glance. A news still of the Weather Channel vehicle after the storm (licence check; the crew's own footage is held for A3). Name card "Mike Bettes · The Weather Channel". A "200 yards" line draws from the road into the field.
> Not everyone on those roads was leaving. Two of the vehicles inside the El Reno tornado carried storm chasing crews, with three people in each. One was a Weather Channel S U V carrying the meteorologist Mike Bettes. The tornado threw it about two hundred yards.

### I1-S7 — narration
**Picture:** the second marker lights on Reuter Road. Name cards "Tim Samaras · 55", "Paul Samaras · 24", "Carl Young · 45", text only. Two marks on the g-clock, minutes apart.
> The other was a white Chevrolet Cobalt carrying the researcher Tim Samaras, his son Paul, and Carl Young. It was struck minutes later, on a different road.

### I1-S8 — narration
**Picture:** split frame: left "3 of 3 survived" over the S U V marker, right "0 of 3" over the Cobalt marker. Then a self-made radar replot of the wide circulation with one small circle inside it, drawn at two positions, unlabelled [verify: one and the same sub-vortex at both vehicles; Wurman et al. 2014 read that way, see fact_check.md]. Hold on the two positions through the last sentence; the bed drops out on the last word.
> Everyone in the S U V survived. No one in the Cobalt did. A radar team led by Joshua Wurman later rebuilt both strikes, and the two vehicles were not struck the same way.

*([loop L2 open]: why one crew survived. Closes in A3 with the two strikes side by side, no cause stated.)*

*(blackout 0.7 s)*


## A1 · A city in its cars (about 2:15, runs about 3:14 with Paul's slot)

### A1-S1 — narration
**Picture:** place stamp "Oklahoma City · May 31, 2013 · evening". A real clip of a neighbourhood street under a dark sky, sirens audible in the clip's own sound, low. Then the assessment's cover page (public domain), the camera settling on the words "sheltering in place". The bed returns under the last sentence.
> The standing advice in central Oklahoma is to shelter in place when a tornado is coming. Afterward, a weather service team went back and asked people why so many had left instead. The fear from Moore was already there. But the team also wrote down two things people were told on May thirty first.

*([loop L3 open]: what made people leave solid houses. Closes in A1-S11.)*

### A1-S2 — narration
**Picture:** [RS] [VE] the assessment's sentence as attributed text, one line at a time: "...telling listeners they would be unable to survive if not underground · NWS Service Assessment". Then a plain cutaway drawing of a one-storey house on a slab, nothing below the floor line. One low hit when the floor line draws.
> The first was about where a person could survive. Some of the people giving warnings, the assessment says, told listeners they could not survive unless they were underground. Most houses in Oklahoma City have no basement and no storm cellar [verify: most Oklahoma City houses have no basement or storm cellar]. For a family with no cellar, that warning said home would not hold.

### A1-S3 — narration
**Picture:** the master map, Oklahoma City at centre, an arrow drawing south out of the city on "drive south". The word "atypical" lifts out of the assessment page and holds. No station logo, no face, no name on screen in this act.
> The second was about what to do instead. The assessment says people followed advice from the media to drive south at once, as storms were bearing down on Oklahoma City. Its word for that advice is atypical, meaning it was not what Oklahomans are normally told. By the assessment's account, that advice overrode the plans families already had.

### A1-S4 — narration
**Picture:** a real news aerial of stopped traffic on a city highway that evening, held with its own sound for two seconds before the voice. Then a split card: "Rita · 2005" beside "Oklahoma City · 2013", both over lines of tail lights.
> So at the hour when the highways were already full of people heading home, more cars pulled out to join them. The assessment says that choice, driving away in place of sheltering, led to the traffic jams and accidents that evening. It compares the evening to Hurricane Rita in two thousand five, when people who had just watched Katrina took to the roads.

### A1-S5 — narration
**Picture:** [HUMAN] the map slides west to El Reno. Text-only name card "Richard Henderson". Popfig "6:05 PM" on the g-clock, two minutes past the touchdown mark. A public domain or licensed shot of the tornado over fields; his own photograph is not used without a licence. His pin lights on the map; its place is one of the six still unsourced under the I1-S4 tag.
> West of the city, near El Reno, one man was driving toward the storm. Richard Henderson drove a truck for a living and chased storms as a hobby. He was thirty five [verify: Richard Henderson's age; Appendix C has an unnamed thirty five year old on a storm chasing line], and he had left his home nearby to see this one. At six oh five PM, two minutes after the tornado touched down, he sent a friend a photograph of it.

### A1-S6 — narration
**Picture:** the g-clock runs ten minutes forward and stops. The bed cuts to silence on "cut out" and stays out for one second. Then two small text cards, "Robbie" and "Wyatt". No assessment card here: its sentence on him carries a hard flag word, so it is paraphrased in the voice only.
> About ten minutes after his photograph, Henderson said he could hear debris hitting his pickup. Then his phone cut out. He left two sons, Robbie and Wyatt. The weather service's assessment gives him one sentence, as an amateur storm chaser who left his nearby home.

### A1-S7 — narration
**Picture:** the map holds on the El Reno track. Seven more pins light in three groups as they are spoken: three together for the Cobalt, one on a line drawn from El Reno toward Chickasha, labelled "67".
> Seven more people were lost in that tornado, and the weather service's table says what each was doing. Three were the crew of the white Cobalt, also chasing. One was a man of sixty seven, driving from El Reno to Chickasha.

### A1-S8 — narration
**Picture:** [HUMAN] Interstate 40 draws across the map. Two pins side by side on its shoulder, labels "26" and "17 days". Hold three seconds with the bed low. Then one last pin, label "32".
> Two were parked along Interstate forty, a woman of twenty six and a boy seventeen days old. For the last, a man of thirty two, the table says only vehicle.

### A1-S9 — narration
**Picture:** the full sixteen mile track over a land-use map: farmland pale, the few buildings as dots. Three roads light as they are named. Then the same traffic aerial, wider.
> The El Reno tornado ran sixteen miles, and most of that was open farmland. It damaged homes and a few businesses near El Reno, and the table lists no one lost inside them. It also crossed Highway eighty one, Reuter Road and Interstate forty. That evening, the roads were full.

### A1-S10 — narration
**Picture:** the track animates: a speed readout climbs "35 mph" to "50+ mph · NWS Service Assessment" and the path bends left. A riser ends on "difficult".
> And the roads had become hard to leave. As the tornado strengthened, the assessment says, its forward speed rose from about thirty five miles an hour to more than fifty. It also made a sharp left turn, and driving away from it became difficult.

### A1-S11 — narration
**Picture:** three words land in a row over the traffic, "fear", "underground", "drive south", then clear. Cut to a rain-streaked windshield view of a grey wall of rain (stock or public domain). On the last sentence a faint radar sweep crosses the frame.
> So fear, a warning about going underground, and advice to drive had put a great many people on the road. But the drivers nearest El Reno were up against something else. Radar recorded it, and a driver in that rain may never have seen it. What was turning inside that tornado?

*([loop L3 closes]: fear, the underground warning and the advice to drive. [loop L4 open]: what was inside the wide tornado. Closes in A2-S6.)*

### A1-S12 — Paul on camera, slot 1 (wording not written)
**Job:** the owner's hook callback at the act seam, the one affirming line after the exit question. It names the hook's claim (twenty-one lives, none inside a building) and points at what was inside the tornado.
**Budget:** 26 words at most, one clip of about 10 s, full frame. No new fact, no number that is not already spoken.

*(blackout 0.7 s)*


## A2 · The tornado inside the tornado (about 5:29, runs about 3:14 with Paul's slot, before picture holds)

### A2-S1 — narration
**Picture:** time stamp "6:19 PM". The map at road level: the circulation as a wide ring reaching Highway 81. A bar "2.6 miles" spans it. Then two outlines side by side, "Hallam, Nebraska · 2004" and "El Reno · 2013", the second wider. A real clip of the tornado, wide shot, licensed or public domain.
> At six nineteen PM, sixteen minutes after it touched down, the El Reno tornado crossed Highway eighty one. By then it was two point six miles from edge to edge. The weather service said it believed this was the widest tornado ever recorded in the United States. The mark it passed had stood since two thousand four, at Hallam, Nebraska.

### A2-S2 — narration
**Picture:** [VE] forty-five field outlines tile across the ring, end to end. An inner ring draws, "core · about 1.25 miles". Rain texture fills the ring until the edge cannot be seen. Two vehicle markers enter from the same side, marked "weak side · Wurman et al. 2014".
> Two point six miles is about forty five football fields laid end to end. Its core, where the two chase crews drove in, was about a mile and a quarter across. And it was wrapped in rain. The radar team led by Joshua Wurman found that both crews entered on its weak side. The team wrote that they may not have known they were inside it.

### A2-S3 — narration
**Picture:** a third marker, "Dan Robinson", crosses the inner ring on Reuter Road with a "45 mph" readout and leaves the far side. Then the whole ring drifts north of Interstate 40 and its readout falls to "under 10 mph · NWS Norman". The bed thins on the last sentence.
> But the wide circulation was the slow part of this storm. A chaser named Dan Robinson drove through its core on Reuter Road at about forty five miles an hour. He drove out the other side. A few minutes later, north of Interstate forty, the whole circulation slowed to less than ten miles an hour. The fast part was somewhere inside it.

### A2-S4 — narration
**Picture:** photographs of the two research radars on their trucks (licence check; government or university press images). Labels "University of Oklahoma" and "Doppler on Wheels". A beam draws low across a field toward the ring.
> Two kinds of research radar were near that tornado, and both could be driven up to a storm. One belonged to the University of Oklahoma. The others were the Doppler on Wheels radars that Joshua Wurman's team used. They measured the moving air itself, very near the ground.

### A2-S5 — Paul on camera, slot 2 (wording not written)
**Job:** the turn from how wide it was to what was inside it. He names "the tornado inside the tornado" and defines it in twelve words or fewer.
**Budget:** 26 words at most, one clip of about 10 s, full frame. The next segment opens on the scientists' word for it, so his line must not use "sub-vortex".

### A2-S6 — narration
**Picture:** [RS] [VE] the self-made radar replot: the wide ring, and one small bright circle turning inside it. Label "sub-vortex". A scale bar "300 to 750 feet" on the small circle, then one to two and a half field outlines laid on it, against the forty-five across the ring.
> Scientists call it a sub-vortex. The one Wurman's team tracked that evening was between about three hundred and seven hundred fifty feet across. That is one to two and a half football fields, inside a storm forty five fields wide.

*([loop L4 closes]: a small, fast vortex inside the wide circulation.)*

### A2-S7 — narration
**Picture:** the small circle moves inside the ring, changing direction. A readout runs up to "about 175 mph · Wurman et al. 2014". A field outline sweeps past once a second to show the pace. Then a second readout, "about 295 mph · National Weather Service". One hit on each readout.
> A sub-vortex does not keep one speed or one direction. Wurman's team clocked sub-vortices in this tornado crossing the ground at up to about a hundred and seventy five miles an hour. That is about two hundred and sixty feet every second. And the weather service says the air inside them was moving at about two hundred ninety five miles an hour.

### A2-S8 — narration
**Picture:** [RS] the 21-pin map returns for four seconds, only the eight El Reno pins lit, each on a road line. No new text. The bed holds one note.
> So the widest tornado ever recorded carried, inside it, air moving near three hundred miles an hour. And by the weather service's table, it took eight lives, every one of them in a vehicle.

### A2-S9 — narration
**Picture:** the replot widens. Faint circles appear and fade inside the ring. A small circle moves in from the northwest, "satellite tornado". To the east-southeast a second circle turns the other way, an arrow showing clockwise, "Marshall et al., damage survey and radar analysis".
> And the sub-vortex was not the only extra thing turning out there. The survey team's radar analysis shows one sub-vortex that lasted and others that came and went. It also shows a small satellite tornado moving in from the northwest, and a second tornado to the east-southeast spinning clockwise. Most tornadoes in this hemisphere spin the other way.

### A2-S10 — narration
**Picture:** road level again. The wide ring passes over Robinson's marker and leaves it on the road. Then the small circle crosses the same road in under a second. Popfig "about 30 seconds · Wurman et al. 2014".
> For a driver, that changes what the danger was. The wide circulation could surround a car, as it did Dan Robinson's, and leave it on the road. A sub-vortex a few hundred feet across could cross the same road faster than any car on it. Wurman's team put the possible warning for one of the two crews at about thirty seconds.

### A2-S11 — narration
**Picture:** the replot, one small circle only. It sits on the S U V marker on "US-81" at "6:19 PM", then on the Cobalt marker on "Reuter Road" about four minutes on. The same circle, drawn at two positions, never two circles. Hold on both positions; the bed drops out on the question.
> At six nineteen PM, by the radar team's account, one sub-vortex was turning inside the wide circulation, and it struck both vehicles [verify: one and the same sub-vortex at both vehicles, Wurman et al. 2014]. It reached the Weather Channel S U V on Highway eighty one. About four minutes later it reached the white Cobalt on Reuter Road. It was one small vortex on two roads, and only one crew survived it. What did it do in those four minutes?

*([loop L2 stays open], sharpened: one sub-vortex, two roads, one crew survives. Pays in A3.)*

*(blackout 0.7 s)*


*(A3 onward: not written. Outline in section B.)*
