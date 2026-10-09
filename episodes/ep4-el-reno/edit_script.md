# ep4-el-reno · edit_script.md (v4b: first full draft, hook to close; the grade's fix pass on acts 1 to 3 applied 9 Oct 26; nothing locked)

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
Times come from the voice probe of 9 Oct 26: 178.9 words a minute at tempo 0.94 (`audio/probe/`), Paul's slots at 10 s each, the book ad at 24.417 s, one-second blackouts. Predicted runtime 21:28. Shares are of the full runtime.

| Section | Planned time | Share | What it proves toward the Claim | Loop | Named person it follows |
|---|---|---|---|---|---|
| H1, T1, I1 | 0:00 to 2:19 | 10.9 % | States the Claim, the count (8 in vehicles, 12 in drains, 1 in a flooded vehicle) and the roster. | Opens L1 (episode) and L2 (the two crews). | Mike Bettes and Tim Samaras, named only. |
| A1 · A city in its cars | 2:19 to 5:24 | 14.4 % | The 21 were where they were because a city left its houses: a Friday rush hour, Moore eleven days earlier, people told they could not survive above ground, advice to drive south. The advice is given in the assessment's own sentence, no one named yet. | Opens and pays L3 (what made people leave solid houses). Ends by opening L4 (the tornado they drove toward was not one tornado). | Richard Henderson, the amateur chaser who left his home near El Reno and sent a photo at 6:05 PM: the first pin on the map. |
| A2 · The tornado inside the tornado | 5:24 to 8:24 | 13.9 % | The danger was not the 2.6 mile circulation, which nearly stopped. It was small vortices inside it, moving at up to about 175 miles an hour. Here "widest ever recorded" and "about 295 miles an hour" arrive as facts. Both crews drove in on the weak side and may not have known they were inside. | Pays L4. Keeps L2 open with the radar picture the viewer now needs. | Joshua Wurman, lead author of the 2014 radar study (mechanism chapter: one researcher, one institution). |
| A3 · Two vehicles, minutes apart | 8:24 to 12:46 | 20.4 % | Two crews inside the same tornado on two roads, US-81 and Reuter Road. The SUV met a small vortex crossing fast; between four and five minutes later the car met it sitting nearly still for about twenty seconds. The two facts sit side by side and the script never says "this is why". The TV crew's own footage runs here as one sequence under narration. | Pays L2 (open question one). Last segment opens L5, the `cta-hinge`. | Mike Bettes and driver Austin Anderson; Tim Samaras, Paul Samaras and Carl Young; Dan Robinson as the last man to see the Cobalt. |
| Book ad | 12:20 | starts at 57.5 % | Sits between the tease and its payoff. | Inside L5. | none |
| A4 · The twelve and the warning gap | 12:46 to 17:18 | 21.1 % | Twelve people, eight of them aged eight or under, went into two storm drains to hide from tornadoes that were E F zero and E F one in the city, and water took them. The family of seven left their house near NW 26th and Meridian when the sirens sounded, went "only a few feet away" into a drainage ditch and hid under a table carried from the house (News 9, confirmed). Enma Aguilar's sentence that they thought the ditch "was the safest spot" runs as attributed text on screen, never as a voice. The assessment names the lack of Spanish-language warnings beside the family of seven; the script says it sits beside them, never that it caused their choice. Then the fairness block at about 15:45 to 17:10 (68 to 75 %): "the problem with that story is" the weather office's own 1 PM tweet about fleeing by car, set next to the broadcast advice. | Pays L5 in its first sentence (open question two). Opens and pays L6 (who told the city to drive). Ends by opening L7 (all 21 pins on one map, and what is missing from it). | Samuel Cifuentes, who walked his family out of the house; Yolanda Santos and her three children; Enma Aguilar (attributed text); Deputy Fire Chief Marc Woodard; Mike Morgan and Gary England in the fairness block. |
| A5 · The map with 21 pins | 17:18 to 20:48 | 16.3 % | The answer. The strongest winds sat in small vortices that crossed no structure, which is also why the rating ended at E F three after the weather office raised it to E F five on June 4, 2013 (statement confirmed; the date it went back still needs its source); every tornado that entered the city was E F zero or E F one; the water went to the lowest ground. The pins sit on roads and in drains, and no pin sits on a building. | Pays L7, then L1 (open question three) in the last 30 to 60 s. | The weather office surveyors in Norman; Harold Brooks of NOAA on "get underground or you will not survive" messaging. |
| Z1 · Close | 20:48 to 21:28 | 3.1 % | One fact with a dated forward window, then the signature line. | none | none |

Each act changes what the viewer understood: A1 the city went out to meet the storm; A2 the wide tornado was not the threat; A3 minutes and yards decided between two crews, and no source names the cause; A4 the largest group was hiding, not driving; A5 the facts every other video opens with turn out to be the answer.

### Loop registry
| Loop | Opens | Closes |
|---|---|---|
| L1 episode: why nobody lost their life indoors | H1-S1, T1-S1 | A5, last 30 to 60 s |
| L2: why one crew survived (facts side by side, no cause stated) | I1-S8 | A3 |
| L3: what made people leave solid houses | A1, first segment | A1-S4 (a second act question, who the tornado's eight were, runs A1-S5 to A1-S7) |
| L4: what was inside the wide tornado | A1, last narration segment | A2 |
| L5 `cta-hinge`: who the twelve were | A3, last segment (Paul) | A4-S1, first sentence |
| L6: who told the city to drive | A4, after the family of seven | A4, fairness block |
| L7: what is missing from the 21-pin map (L1 asked aloud) | A4, last segment | A5 |

### Book-ad hinge
- **Segment before:** the last segment of A3, Paul on camera, 25 words at most. It is the line that the home was the safe place, and it teases the twelve who left theirs.
- **Book ad:** at the measured pace it starts at about 12:20, 57.5 % of a predicted 21:28, inside `config.yaml channel.cta.window` [0.40, 0.60]. Its length is 24.417 s (`config.yaml channel.cta.duration`).
- **Segment after:** A4-S1. Its first sentence is the payoff, first three words if possible: the family of seven and how far they went from their own door ("only a few feet away", News 9, confirmed).

### Paul on camera (besides the hook), position and job only
1. About 5:25, last line of A1: the owner's hook callback at the act seam; names the hook's claim and points at what was inside the tornado.
2. About 7:10, middle of A2: the turn from how wide it was to what was inside it; names "the tornado inside the tornado" and defines it in twelve words or fewer.
3. About 11:40, A3, after both vehicles have been struck: sets the two strikes side by side in one breath, two facts and no cause.
4. About 13:00, last segment of A3: the `cta-hinge` tease, 25 words at most.
5. About 21:30, A5, at the full 21-pin map: the answer line that returns to the hook's claim, before the close.

### Open items the later acts must tag (from angle-facts "Still open")
Fact check 9 Oct 26 (`fact_check.md`): the radar paper reads as ONE interior sub-vortex striking both vehicles, racing across US-81 at the S U V and nearly stopped over Reuter Road at the car between four and five minutes later. A2 and A3 are written to that, never as two different vortices, and the sentence carries a verify tag until the paper's authors' wording is matched line by line.
Richard Henderson's age; the date the rating went back to E F three (the June 4 upgrade statement is confirmed); the pairing of the press names with the table rows (the News 9 report on the family of seven is read and confirmed); the News 9 report of June 9 on the last recovery; one spelling for the family's names, which differ between Fox and News 9 (Christopher and Leslie against Cristofer and Lesly, Floridalma against Florinda); the exact broadcast words; Joshua Wurman's institution; the June 1 flood loss. Each gets a verify tag where it is written, or stays out.

## Writer notes
- Narration numbers follow the shipped Enderlin copy: spelled out, no hyphen ("twenty one"). H1-S1 is the owner's line verbatim, hyphen included.
- "wind" does not occur in the hook, tail or intro. No homograph is respelled here; respelling waits for a TTS probe (`references/homographs.md`).
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- A1 and A2 also avoid "wind" and "record" as a noun ("the air inside them", "ever recorded"), so no homograph waits on a probe there.
- A Paul slot is a heading with a Job, a Budget and his line as the blockquote (picked by the owner 9 Oct 26, `paul-lines.md`). `parse_segments` reads it as a segment, so the voice tool also makes a narrator take of each line: the audio-only fallback the owner asked for if a clip has a speech defect.
- The times on the section headings come from the voice probe of 9 Oct 26 (178.9 words a minute at tempo 0.94). They move when the wording moves.

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** Paul on camera, full frame, frame one, speaking this line and nothing else. Popfig "May 31, 2013 · Oklahoma City" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> Twenty-one people lost their lives that night, and not one of them was inside a building.

*([loop L1 open]: why nobody lost their life indoors. Closes in A5.)*


## T1 · Hook tail (starts about 0:05, measured pace)

### T1-S1 — narration
**Picture:** hard cut on the first word to mid-action footage, never black: a real clip of the evening sky and loaded highways around Oklahoma City on May 31 (news or public domain; no chaser footage without a licence). A counter "19 tornadoes in Oklahoma · National Weather Service" lands on "nineteen". On "Twelve of the twenty one": twenty-one small markers appear in a row and twelve of them light. One bed swell under the last clause, no siren.
> On May thirty first, twenty thirteen, the weather service counted nineteen tornadoes across Oklahoma. Twelve of those twenty one people had taken shelter from the tornadoes, and no tornado took their lives.

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The night and the count (starts about 0:16, measured pace)

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
**Picture:** split frame: left "3 of 3 survived" over the S U V marker, right "0 of 3" over the Cobalt marker. Then a self-made radar replot of the wide circulation with one small circle inside it, drawn at two positions, unlabelled. Hold on the two positions through the last sentence; the bed drops out on the last word.
> Everyone in the S U V survived. No one in the Cobalt did. A radar team led by Joshua Wurman later rebuilt both strikes, and the two vehicles were not struck the same way.

*([loop L2 open]: why one crew survived. Closes in A3 with the two strikes side by side, no cause stated.)*

*(blackout 0.7 s)*


## A1 · A city in its cars (starts about 2:19, runs to about 5:24, measured pace)

### A1-S1 — narration
**Picture:** [RS] [VE] place stamp "Oklahoma City · May 31, 2013 · evening". A real clip of a neighbourhood street under a dark sky, sirens audible in the clip's own sound, low. Over it the assessment's sentence as attributed text, one line at a time: "...telling listeners they would be unable to survive if not underground · NWS Service Assessment". Then the words "sheltering in place" from the same page. The bed returns under the last sentence.
> On May thirty first, some of the people giving tornado warnings told listeners they could not survive unless they were underground. That is the weather service's own finding, from the team it sent to ask why so many people left. The standing advice in central Oklahoma is the opposite, to stay and shelter in place.

*([loop L3 open]: what made people leave solid houses. It opens on the warning that only underground would do, which the intro has not given. Closes in A1-S4.)*

### A1-S2 — narration
**Picture:** a plain cutaway drawing of a one-storey house on a slab, nothing below the floor line. One low hit when the floor line draws. Then the master map: popfig "6:03 PM", the g-clock starts, and a tornado mark lights west of Oklahoma City.
> Not every house had a cellar to go to. For a family with no cellar, that meant their own house would not save them. And by six oh three PM, a tornado was on the ground west of the city.

### A1-S3 — narration
**Picture:** the master map, Oklahoma City at centre, an arrow drawing south out of the city on "drive south". The word "atypical" lifts out of the assessment page and holds. No station logo, no face, no name on screen in this act.
> People were also told what to do instead. They followed advice from the media to drive south at once, as storms were bearing down on Oklahoma City. The assessment's word for that advice is atypical, meaning it was not what Oklahomans are normally told. It overrode the plans families already had.

### A1-S4 — narration
**Picture:** a real news aerial of stopped traffic on a city highway that evening, held with its own sound for two seconds before the voice. Then a split card: "Rita · 2005" beside "Oklahoma City · 2013", both over lines of tail lights.
> So at the hour when the highways were already full of people heading home, more cars pulled out to join them. That choice, driving away instead of sheltering, led to the traffic jams and accidents that evening, the assessment found. It compares the evening to Hurricane Rita in two thousand five, when people who had just watched Katrina took to the roads.

*([loop L3 closes]: the underground warning and the advice to drive, which the assessment ties to the traffic. The next segment opens the act's second question, who the tornado's eight were; it pays in A1-S7.)*

### A1-S5 — narration
**Picture:** [HUMAN] the map slides west to El Reno. Text-only name card "Richard Henderson". A public domain or licensed shot of the tornado over fields; his own photograph is not used without a licence. His pin lights on the map on US Highway 81 (News 9, 4 Jun 2013, fact_check.md).
> But half of the people that tornado took were not running from it. West of the city, near El Reno, one man was driving toward the storm. Richard Henderson drove a truck for a living and chased storms as a hobby. He was thirty five, and he had left his home nearby to see this one.

### A1-S6 — narration
**Picture:** [RS] popfig "6:05 PM" on the g-clock, two minutes past the touchdown mark. The clock runs ten minutes forward and stops. The bed cuts to silence on "cut out" and stays out for one second. Then two small text cards, "Robbie" and "Wyatt". No assessment card here: its sentence on him carries a hard flag word, so it is paraphrased in the voice only.
> At six oh five PM, two minutes after the tornado touched down, he sent a friend a photograph of it. About ten minutes later, Henderson said he could hear debris hitting his pickup. Then his phone cut out. He left two sons, Robbie and Wyatt. The weather service's assessment gives him one sentence, as an amateur storm chaser who left his nearby home.

### A1-S7 — narration
**Picture:** the map holds on the El Reno track. Pins light as they are spoken: three together for the Cobalt, then a counter "4 of 8 · storm chasing · NWS Service Assessment" beside Henderson's pin and those three. Then one pin on a line drawn from El Reno toward Chickasha, labelled "67".
> Seven more people were lost in that tornado, and the weather service's table says what each was doing. Three were the crew of the white Cobalt. That makes four of the eight chasing the storm. One was a man of sixty seven, driving from El Reno to Chickasha.

### A1-S8 — narration
**Picture:** [RS] [HUMAN] one pin, label "32". Then Interstate 40 draws across the map and two pins land side by side on its shoulder, labels "26" and "17 days". Hold three seconds on those two with the bed low.
> One was a man of thirty two, and the table says only vehicle. Two were parked along Interstate forty, a woman of twenty six and a boy seventeen days old.

### A1-S9 — narration
**Picture:** the track over a land-use map near El Reno: the damaged homes and businesses as lit dots, no pin on any of them. Then the full sixteen miles, farmland pale, and three rural roads lighting as they are named. No city traffic aerial here.
> The tornado damaged homes and a few businesses near El Reno, and the table lists no one lost inside them. Most of its sixteen miles was open farmland. It did cross roads: Highway eighty one, Reuter Road and Interstate forty.

### A1-S10 — narration
**Picture:** the track animates: a speed readout climbs "35 mph" to "50+ mph · NWS Service Assessment" and the path bends left. A riser ends on "difficult".
> As the tornado strengthened, the assessment says, its forward speed rose from about thirty five miles an hour to more than fifty. It also made a sharp left turn, and driving away from it became difficult.

### A1-S11 — narration
**Picture:** a rain-streaked windshield view of a grey wall of rain (stock or public domain). On the second sentence a faint radar sweep crosses the frame and one small bright return shows inside the rain. The bed drops out on the question.
> But the drivers nearest El Reno had a second problem. The tornado was wrapped in rain, and radar recorded something moving inside it. What was turning inside that tornado?

*([loop L4 open]: what was inside the wide tornado. Closes in A2-S6.)*

### A1-S12 — Paul on camera, slot 1 (line picked by the owner, 9 Oct 26)
**Job:** the owner's hook callback at the act seam, the one affirming line after the exit question. It names the hook's claim (twenty-one lives, none inside a building) and points at what was inside the tornado.
**Budget:** 26 words at most, one clip of about 10 s, full frame. No new fact, no number that is not already spoken.
> Stick with me. What radar found inside that tornado is part of why twenty one lives were lost that night, and none inside a building.

*(blackout 0.7 s)*


## A2 · The tornado inside the tornado (starts about 5:24, runs to about 8:24, measured pace)

### A2-S1 — narration
**Picture:** time stamp "6:19 PM". The map at road level: the circulation as a wide ring reaching Highway 81. A bar "2.6 miles" spans it. Then two outlines side by side, "Hallam, Nebraska · 2004" and "El Reno · 2013", the second wider. A real clip of the tornado, wide shot, licensed or public domain.
> At six nineteen PM, sixteen minutes after it touched down, the El Reno tornado crossed Highway eighty one. Within minutes the whole turning mass of air, which scientists call the circulation, was two point six miles from edge to edge. The weather service said it believed this was the widest tornado ever recorded in the United States. The old mark was set at Hallam, Nebraska, in two thousand four.

### A2-S2 — narration
**Picture:** [VE] forty-five field outlines tile across the ring, end to end. An inner ring draws, "core · about 1.25 miles". Rain texture fills the ring until the edge cannot be seen. Two vehicle markers enter from the same side, marked "weak side · Wurman et al. 2014".
> Two point six miles is more than forty five football fields laid end to end. Its core, where the two chase crews drove in, was about a mile and a quarter across. And it was wrapped in rain. The radar team led by Joshua Wurman found that both crews drove in on its weaker side. The team wrote that they may not have known they were inside it.

### A2-S3 — narration
**Picture:** a third marker, "Dan Robinson", crosses the inner ring on Reuter Road with a "45 mph" readout and leaves the far side. Then a later time stamp, "6:27 PM": the whole ring drifts north of Interstate 40 and its readout falls to "under 10 mph · NWS Norman". The bed thins on the last sentence.
> But a car could drive through the wide circulation and come out. A chaser named Dan Robinson drove through its core on Reuter Road at about forty five miles an hour. He drove out the other side. Later, north of Interstate forty, the whole circulation slowed to less than ten miles an hour. The fast part was somewhere inside it.

### A2-S4 — narration
**Picture:** photographs of the two research radars on their trucks (licence check; government or university press images). Labels "University of Oklahoma" and "Doppler on Wheels · Joshua Wurman's team". A beam draws low across a field toward the ring.
> Two research radar teams had driven up to that tornado, and their beams measured the moving air near the ground.

### A2-S5 — Paul on camera, slot 2 (line picked by the owner, 9 Oct 26)
**Job:** the turn from how wide it was to what was inside it. He names "the tornado inside the tornado" and defines it in twelve words or fewer.
**Budget:** 26 words at most, one clip of about 10 s, full frame. The next segment opens on the scientists' word for it, so his line must not use "sub-vortex".
> Their radar showed two things turning. I call the second one the tornado inside the tornado: a much smaller one, spinning hard inside the wide one.

### A2-S6 — narration
**Picture:** [RS] [VE] the self-made radar replot: the wide ring, and one small bright circle turning inside it. Label "sub-vortex". A scale bar "300 to 750 feet" on the small circle, then one to two and a half field outlines laid on it, against the forty-five across the ring.
> Scientists call it a sub-vortex. The one Wurman's team tracked that evening was between about three hundred and seven hundred fifty feet across. That is one to two and a half football fields, inside a circulation more than forty five fields wide.

*([loop L4 closes]: a small, fast vortex inside the wide circulation.)*

### A2-S7 — narration
**Picture:** the small circle moves inside the ring, changing direction. A readout runs up to "about 175 mph · Wurman et al. 2014", with "about 260 feet every second" under it; a field outline sweeps past once a second to show the pace. Then a second readout, "about 295 mph · National Weather Service". One hit on each readout.
> A sub-vortex does not keep one speed or one direction. Wurman's team clocked sub-vortices in this tornado crossing the ground at up to about one hundred seventy five miles an hour. That is most of a football field every second. The air spinning inside them was faster still. The weather service puts it at about two hundred ninety five miles an hour.

### A2-S8 — narration
**Picture:** the replot widens. Faint circles appear and fade inside the ring. A small circle moves south into the ring's northwest side, "satellite tornado". Nearby a second circle turns the other way, an arrow showing clockwise, "Marshall et al., damage survey and radar analysis".
> Those sub-vortices were not alone. The damage survey's radar analysis shows other sub-vortices that came and went, and a second tornado nearby spinning clockwise, against the usual direction.

### A2-S9 — narration
**Picture:** [RS] the 21-pin map returns for four seconds, only the eight El Reno pins lit, each on a road line. No new text. The bed holds one note.
> So the widest tornado on record in the United States carried air moving at about two hundred ninety five miles an hour. And by the weather service's table, it took eight lives, every one of them in a vehicle.

### A2-S10 — narration
**Picture:** a real clip of the rain-wrapped tornado seen from road level (public domain or licensed news; no chaser footage without a licence), held two seconds before the voice. Then road level on the map: the wide ring passes over Robinson's marker and leaves it on the road, and the small circle crosses the same road in under a second. Popfig "about 30 seconds · Wurman et al. 2014".
> The wide circulation could surround a car, as it did Dan Robinson's, and leave it on the road. A sub-vortex a few hundred feet across could cross the same road faster than any car on it. Wurman's team put the possible warning for the Cobalt's crew at about thirty seconds.

### A2-S11 — narration
**Picture:** the replot, one small circle only. It sits on the S U V marker on "US-81" at "6:19 PM", then on the Cobalt marker on "Reuter Road" between four and five minutes on. The same circle, drawn at two positions, never two circles. Hold on both positions; the bed drops out on the question.
> As the tornado crossed Highway eighty one, by the radar team's account, one sub-vortex was turning inside it. It struck the Weather Channel S U V there. Between four and five minutes later it struck the white Cobalt on Reuter Road. It was one small vortex on two roads, and one crew survived. What happened at each road?

*([loop L2 stays open], sharpened: one sub-vortex, two roads, one crew survives. The question asks what happened at each road, not what the vortex did. Pays in A3.)*

*(blackout 0.7 s)*


## A3 · Two vehicles, minutes apart (starts about 8:24, runs to about 12:46, measured pace)

*(Clock note for the editor: every time in this act is the Wurman paper's radar timing, except 6:19 PM at the highway, which is the weather service's. Dan Robinson's own account puts his last sighting of the Cobalt about three minutes earlier; it is not spoken.)*

### A3-S1 — narration
**Picture:** time stamp "6:19 PM · National Weather Service". The road-level map: Highway 81 running north to south, the wide ring arriving from the west. One marker, "The Weather Channel", moving south. Name cards "Mike Bettes", "Austin Anderson · driver", "Brad Reynolds · camera". The crew's own footage is held for A3-S3.
> The weather service puts the tornado on Highway eighty one at six nineteen PM. A Weather Channel S U V was on that highway, heading south. Mike Bettes was aboard, with Austin Anderson driving and Brad Reynolds on the camera. The radar team's paper says they were trying to get through to the tornado's south side.

### A3-S2 — narration
**Picture:** the replot at road level: the one small circle crosses Highway 81 with the ring, readout "about 56 mph · Wurman et al. 2014", an arrow east-northeast. A side view lifts off the map: ground line, a mark at "about 400 feet", an arrow pointing east on the circle's south side.
> They met the sub-vortex as it crossed the road at about fifty six miles an hour. On its south side the air was blowing east.

### A3-S3 — narration
**Picture:** [RS] [VE] the TV crew's own footage, the one sequence in the film (owner's permission, 9 Oct 26), graded, running from here to the end of A3-S4. Readout "over 185 mph" on the first sentence, then the footage full frame. On "kept recording" the voice stops and the clip's own sound plays alone for about six seconds: the black picture, the crash, the camera settling on its side. A line "200 yards" over the settled frame.
> A few hundred feet up, the radar clocked that air at more than one hundred eighty five miles an hour. It carried the S U V off the east side of the highway, about two hundred yards. The crew's own camera kept recording.

### A3-S4 — narration
**Picture:** the same sequence continues under the voice. Two attributed text cards over it, one at a time, exact words: Bettes, "It was like we were floating. We were tumbling. We were airborne at least one point and we were floating." Then Anderson, "Next thing I know, we're flying into the tornado through the air. The glass in the truck blew out and we were upside down." Source line "weather.com" on both. Text only, never a voice.
> Bettes said afterward that it felt like floating, and that at one point they were in the air. Anderson remembered the glass blowing out and the truck upside down.

### A3-S5 — narration
**Picture:** a news still of the vehicle in the field after the storm (licence check). Three small markers beside it turn to "survived" one by one. The bed comes back in, lower than before.
> All three got out. They had been wearing seatbelts. Bettes and Reynolds came away with minor injuries. Anderson had a cracked breastbone, five broken ribs and a broken bone in his neck, and he needed surgery.

### A3-S6 — narration
**Picture:** place stamp "Reuter Road". The road-level map: two markers heading east inside the ring, "Dan Robinson" ahead, the white Cobalt behind. A "45 mph" readout on Robinson; the gap between the two opens. Two small headlight dots on the Cobalt marker fade at "6:22:15 PM · Wurman et al. 2014". Robinson's video is described, never shown: no licence on record.
> On Reuter Road, two more cars were heading east inside the wide circulation. The first was Dan Robinson's, and the white Cobalt was right behind him. Robinson was doing about forty five miles an hour, and the Cobalt fell behind. By the radar team's timing, its headlights were last seen behind him a little after six twenty two PM.

### A3-S7 — narration
**Picture:** the map pulls back: Reuter Road and Highway 81 empty except three markers, the two cars and one red pickup parked on the highway. Text line from the assessment, exact words: "there were no other vehicles in our immediate vicinity · Dan Robinson, quoted in the NWS Service Assessment".
> Robinson later wrote that the road around them was nearly empty. Apart from the Cobalt and one red pickup parked along Highway eighty one, he saw no other vehicle near them. The weather service's assessment took his account and found that traffic did not appear to be a factor for the research team.

### A3-S8 — narration
**Picture:** [RS] [VE] the replot: the same small circle leaves the highway, loops, brightens south of the Cobalt marker and comes north. Popfig "6:23:35 PM". It reaches Reuter Road and stops. A second counter starts at zero and runs to about twenty seconds while the circle does not move. Every other sound drops out under the counter.
> By then the sub-vortex had left the highway and looped back. By the radar team's account, it strengthened about five hundred and fifty yards south of the car, then moved north toward the road. Between four and five minutes after it crossed the highway, it reached Reuter Road and nearly stopped. It stayed over the road for about twenty seconds.

### A3-S9 — narration
**Picture:** the counter holds at its end. Readout "over 180 mph". A line draws from the Cobalt's starting mark, about 580 yards west of Radio Road, to a mark just north-east of the crossroads: "about 650 yards · about 20 seconds". No photograph of the car.
> The center of it sat just east of where the Cobalt is thought to have been. Air inside it was moving at more than one hundred eighty miles an hour. The Cobalt was not especially heavy, and it was not armored. In about twenty seconds it was carried about six hundred and fifty yards, past the crossroads at Radio Road.

### A3-S10 — narration
**Picture:** [RS] [HUMAN] black card, text only, one name at a time: "Tim Samaras · 55", "Paul Samaras · 24", "Carl Young · 45". No photographs. The names land on the last two sentences. One second of silence after the last sentence.
> The weather service's assessment calls these three some of the most experienced and safety minded chasers. The radar team wrote that Tim Samaras had long experience placing instruments in and near tornadoes. He was fifty five, and he was still belted into his seat. His son Paul was twenty four, and Carl Young was forty five.

### A3-S11 — narration
**Picture:** the paper's sentence as attributed text, exact words: "it is likely that no clear direction to safety was apparent · Wurman et al., Bulletin of the American Meteorological Society, 2014". Behind it the replot, the circle's looping track drawn as one line.
> The radar team gives them thirty seconds of possible warning, perhaps in poor visibility, from a vortex that kept changing direction. It concludes that they probably had no clear direction to safety.

### A3-S12 — Paul on camera, slot 3 (line picked by the owner, 9 Oct 26)
**Job:** pays L2. He sets the two strikes side by side in one breath: one vortex, crossing the highway at about fifty six miles an hour, nearly still over Reuter Road for about twenty seconds. Two facts, no cause, never "this is why".
**Budget:** 26 words at most, one clip of about 10 s, full frame. Only numbers already spoken in this act.
> One crew met it moving at about fifty six miles an hour. The other met the same vortex nearly still, for about twenty seconds.

### A3-S13 — narration
**Picture:** split frame, the same small circle on both sides. Left: Highway 81, "about 56 mph", a line "200 yards". Right: Reuter Road, "nearly still · about 20 seconds", a line "650 yards" drawn to the same scale. Under them two short lines of attributed text from the paper, one about speed and injuries, one about the car's build. No arrow or word joins the two sides.
> The S U V met that vortex crossing the highway, and was carried about two hundred yards. The Cobalt met it nearly still over Reuter Road, and was carried more than three times that far. The radar team wrote that the speed at the highway likely added to the injuries in the S U V. It wrote that the Cobalt's light build likely made it more vulnerable. It names no single cause.

*([loop L2 closes]: the two strikes as plain statements, the paper's two "likely" lines, and one line of limit. No cause stated.)*

### A3-S14 — narration
**Picture:** the 21-pin map returns. The eight El Reno pins are lit, each on a road. The view slides east to Oklahoma City, where twelve pins sit unlit at two points and one more stands apart. Hold on the twelve; the bed thins to rain.
> All eight people lost in the El Reno tornado were in vehicles, and both crews had gone out to find it. Twelve of the other thirteen had done the opposite. They had gone to hide from it.

### A3-S15 — Paul on camera, slot 4, the `cta-hinge` tease (line picked by the owner, 9 Oct 26)
**Job:** the line that home was the safe place, teasing the twelve who left theirs. It opens L5 and runs straight into the book ad. It gives no detail of the family: how far they went from their own door is A4-S1's first sentence.
**Budget:** 25 words at most (the hinge cap), one clip of about 10 s, full frame.
> That night, home was the safe place. Twelve people went to hide somewhere else. How far did they go?

*([loop L5 `cta-hinge` open]: who the twelve were. Book ad mounts here. Closes in A4-S1, first sentence.)*


## A4 · The twelve and the warning gap (starts about 12:46, runs to about 17:18, measured pace)

### A4-S1 — narration
**Picture:** straight out of the book ad, no black. A street map of Oklahoma City at "NW 26th St and Meridian": one house outline, one ditch line beside it, a short measure between them marked "a few feet · News 9, June 2013". Sirens in a real clip's own sound, low, under the second sentence. Text-only name card "Samuel Cifuentes".
> A few feet is how far one family of seven went from their own door, by the account their relatives gave News Nine. When the tornado sirens sounded in Oklahoma City that Friday, Samuel Cifuentes left his house near Northwest twenty sixth Street and Meridian.

*([loop L5 `cta-hinge` closes] in the first sentence: the family, and how far they went.)*

### A4-S2 — narration
**Picture:** [HUMAN] text-only name cards, one at a time, in two groups: "Samuel Cifuentes", "Florinda Santos", "Alex"; then "Yolanda Santos", "Cristofer", "Brandon", "Lesly". News 9's spellings. No photographs unless the family's are licensed. Seven pins light at one point on the 21-pin map.
> With him were his wife, Florinda Santos, and their son, Alex. With them were Florinda's cousin, Yolanda Santos, and Yolanda's three children, Cristofer, Brandon and Lesly.

### A4-S3 — narration
**Picture:** [RS] the house and ditch drawing again: a table outline moves from the house to the ditch. Then Enma Aguilar's sentence as attributed text, exact words, held four seconds: "They were in the ditch because they thought it was the safest spot because they just thought it was going to be a tornado, not a flooding. · Enma Aguilar, family member, to News 9". Text only, never a voice.
> They did not get in a car. They carried a table out of the house, went down into a drainage ditch a few feet away, and hid under the table. A relative, Enma Aguilar, told News Nine why. They thought the ditch was the safest spot, she said, because they thought a tornado was coming, not a flood.

### A4-S4 — narration
**Picture:** public domain footage of fast brown water in a concrete channel in the city that night or the next morning. The map draws a line from the ditch to "Deep Fork Creek · 4 miles". The bed thins to water sound. One second of silence after "survived".
> The tornado itself did not harm them, the first reports said. The water did. A surge of flood water came down the ditch and washed all seven away. None of the seven survived. Florinda Santos was found along Deep Fork Creek, four miles from where they had hidden.

### A4-S5 — narration
**Picture:** the map slides to "SW 15th St · near the Dell plant". A storm drain drawn in section under the street, eleven small markers inside. Source line "News 9, June 3, 2013".
> Elsewhere in the city, eleven more people had made the same choice. News Nine reported that most of them were young children. They were inside a storm drain under Southwest fifteenth Street, near the Dell plant, to get away from the tornadoes.

### A4-S6 — narration
**Picture:** [HUMAN] the section drawing: a water line rises to a mark "about 2 feet". A line draws from the drain to the "Oklahoma River · a quarter of a mile". One text-only card, "Corey Don Johnson · 3". No card and no name for either survivor: they are living people, one a child then.
> When the water in the drain reached about two feet, they tried to climb out and could not. It carried all eleven into the Oklahoma River, a quarter of a mile away. An aunt held her three year old nephew the whole way. His name was Corey Don Johnson, and he did not survive. An eight year old girl was pulled from the river near the dam.

### A4-S7 — narration
**Picture:** five of the eleven markers dim, six stay lit. Then the assessment's table, the twelve lines "Sheltering in drainage ditch, flash flood" highlighted, the name column absent. Counter "18 went in · 12 did not survive". Our pairing of press names with table lines is an inference and is never shown as the table's own.
> By the reports and the table, five of the eleven did not survive, and six did. So eighteen people went into two drains that evening, and twelve did not survive. The weather service's table has twelve lines that say, sheltering in drainage ditch, flash flood. It gives ages and no names. The names come from local reporters and from the families.

### A4-S8 — narration
**Picture:** one more pin, apart from the others, label "65". Then a plain timeline bar from "1934" to "2013" with nothing between them. Source line "NWS Service Assessment".
> The thirteenth life lost to the water that night was a man of sixty five, in a vehicle. The assessment calls it the worst flood Oklahoma City has ever had for lives lost. For the region the Norman office covers, it was the most lives lost to a flash flood since nineteen thirty four.

### A4-S9 — narration
**Picture:** [RS] [VE] the city map: several short tracks draw in, each stamped "EF0" or "EF1"; one carries the weather office's end point and time, "SW 15th / Meridian · 7:09 PM · EF1", on screen only. The drain markers are not drawn on this map: how far that end point was from either drain has not been measured. A small scale graphic, six steps, the bottom two lit. No pin sits on any track.
> The tornadoes they were hiding from were real. Several crossed into Oklahoma City that evening, and the weather office rated every one of them E F zero or E F one. Those are the two lowest ratings on the scale. None of them took a life.

### A4-S10 — narration
**Picture:** Enma Aguilar's line returns small in a corner, the words "a tornado, not a flooding" lit. Then the assessment page, Finding 6, as attributed text. Behind it, a real clip of that evening's television radar picture (licence check), silent.
> The assessment's team heard something like the family's reason from people across the city. They said broadcasters that evening kept their attention on the tornadoes and not on the flooding.

### A4-S11 — narration
**Picture:** the assessment's paragraph on screen, its two sentences lit one after the other: the Guatemalan family whose primary language was Spanish, then the warning resources. A thin rule between them, no arrow joining them. Source line "NWS Service Assessment".
> The assessment describes a Guatemalan family whose first language was Spanish, and in the same paragraph it raises one more thing. Emergency managers and broadcast meteorologists told its team there were not enough forecasts and warnings for people who do not speak English. Only a few radio and television stations broadcast in Spanish. It does not say the gap is why that family went to the ditch.

### A4-S12 — narration
**Picture:** the traffic aerial from A1 returns under a `data-callback`. Text-only name cards "Mike Morgan · KFOR" and "Gary England · KWTV, a competing station". No broadcast clip and no quoted line on screen until the recording is checked; the Gazette's words wait behind the tag. No card for Morgan's reply until its tag clears.
> The story usually told about the advice to drive south has one name in it. Mike Morgan was the chief meteorologist at K F O R. The Oklahoma Gazette reported that he told viewers to drive south. Gary England, a longtime meteorologist at the competing station K W T V, called that advice dangerous. By one local report, Morgan answered that week and wrote that he felt desperate to help.

*([loop L6 open]: who told the city to drive. Closes in A4-S15.)*

### A4-S13 — narration
**Picture:** [RS] [VE] a clock face runs back from "6:03 PM" to "1:00 PM", five hours. The weather office's message as attributed text, exact words: "TORNADO SAFETY: If you choose to flee in your car, plan for and anticipate traffic jams and blocked roads, hail, heavy rain and flooding. · NWS Norman, 1 PM, May 31, 2013, quoted in the NWS Service Assessment". One hit when the clock stops.
> The problem with the one name story is the clock. At one PM that day, five hours before the tornado, the weather office in Norman posted a safety message of its own. If you choose to flee in your car, it said, plan for traffic jams and blocked roads, hail, heavy rain and flooding.

### A4-S14 — narration
**Picture:** the message stays up. Two phrases lift out of it in turn, "traffic jams" over the highway aerial and "flooding" over the drain map.
> That message did not tell anyone to leave. But it treated a car as a choice a person might make, and it came from the office that issues the warnings. It also named the two things that went wrong that night, the traffic and the flood.

### A4-S15 — narration
**Picture:** the assessment's Recommendation 6 as attributed text. Then the two name cards and the weather office's message in one frame, kept visibly different in kind and size: an on-air instruction and a conditional safety note are not drawn as equals.
> The assessment's sixth recommendation is aimed at the weather service itself: give broadcasters better guidance when more than one danger is coming. So the idea that a car was an option did not start with one man on one channel.

*([loop L6 closes]: the broadcast advice and the weather office's own one PM message, side by side.)*

### A4-S16 — narration
**Picture:** [RS] the 21-pin map, full, every pin lit. Roads and drains carry pins; the building icons across the whole city stay unlit. On the second sentence a slow push in to the house outline at NW 26th and Meridian, unlit, with seven pins beside it. The bed drops out on the question. Pin places as in the I1-S4 tag: sixteen of the twenty-one are sourced so far.
> The map has twenty one pins, on roads and in two drains. The house near Northwest twenty sixth and Meridian is on it too, a few feet from seven of them. The same map is covered in houses, stores and schools, and not one of them has a pin. Why not?

*([loop L7 open]: what is missing from the 21-pin map. It is L1 asked aloud. Closes in A5.)*

*(blackout 0.7 s)*


## A5 · The map with 21 pins (starts about 17:18, runs to about 20:48, measured pace)

### A5-S1 — narration
**Picture:** date stamp "June 4, 2013". The weather office's public statement of that day on screen (public domain), the line about the upgrade lit. A stamp "EF5" lands on the El Reno track. Readout "about 295 mph".
> On June fourth, twenty thirteen, four days after the storm, the weather office in Norman raised the tornado to an E F five. It did that because of the radar. The research radars had measured air moving at about two hundred ninety five miles an hour.

### A5-S2 — narration
**Picture:** [RS] [VE] the "EF5" stamp lifts and "EF3" settles in its place, no date shown. Then the replot over a land-use map: the small circles' tracks cross fields and roads and touch no building dot. The weather office's sentence as attributed text: "none of these intense sub-vortices impacted any structures in rural Canadian County · NWS Norman".
> Later the office took the rating back down to E F three. The fastest air was inside the small sub-vortices, it wrote, and none of them crossed a single structure in rural Canadian County.

### A5-S3 — narration
**Picture:** public domain footage of a survey team at work. A short list graphic: house, barn, tree, power pole, each with a tick box and the label "marker". Over the sub-vortex tracks the structure boxes stay empty. The survey paper's sentence as attributed text, exact words: "Despite the intense wind velocities, surveyors could not find damage that would support a rating higher than EF3. · Marshall et al., damage survey".
> A tornado's rating comes from what it breaks. Surveyors walk the path and grade the damage to buildings, trees and other things on a set list. Call each one a marker. Where the sub-vortices went, the office found no structure for them to break. Despite those speeds, the survey team wrote, surveyors could not find damage that would support a rating higher than E F three.

*([loop L7 closes]: no pin on a building, because the strongest part of the storm crossed none.)*

### A5-S4 — narration
**Picture:** the sixteen mile track as a strip, the survey's markers as dots: thin away from one cluster, "average under 10 per square mile". A count "112 oil tank batteries" over a public domain photo of tank batteries in a field. Then two bars side by side, "damage" and "radar", the radar bar ten to thirty percent taller. Source line "Marshall et al., damage survey and radar analysis".
> The survey team counted what the tornado had to hit. Away from one cluster, the path averaged fewer than ten markers in a square mile. One hundred twelve of the ones they logged were oil tank batteries, the storage tanks that stand beside oil wells. And where radar and damage could be compared, the radar speeds ran ten to thirty percent higher.

### A5-S5 — narration
**Picture:** the track map near Interstate 40: a cluster of small squares just south of the road lights up, "manufactured homes · 69 markers per square mile". The eight El Reno pins stay on the roads; none sits in the cluster. On the last two sentences the weather service's guidance as attributed text, exact words: "Mobile homes and trailers are not safe. Evacuate immediately and seek shelter in a sturdy building. · National Weather Service". The safety text holds to the end of the segment and is never cut for time.
> The tornado did reach buildings. The survey found its densest cluster of damage in a group of manufactured homes, also called mobile homes, just south of Interstate forty. The weather service's table lists no one lost in them, and the survey does not say whether anyone was inside. That is not a reason to stay in one. The weather service's standing advice is that a mobile home is not safe in a tornado, and to get to a sturdy building.

### A5-S6 — narration
**Picture:** the map slides east to the city. The short "EF0" and "EF1" tracks from A4 return under a `data-callback`. Building icons everywhere, no pin on any.
> In Oklahoma City, where the buildings were, every tornado that entered that evening was an E F zero or an E F one. None took a life.

### A5-S7 — narration
**Picture:** date stamp "Moore · May 20, 2013 · EF5". Public domain aerials of Moore after the storm. The assessment's sentence as attributed text, exact words: "survived above ground in predetermined shelters. Shelters ranged from interior closets and bathrooms to safe rooms. · NWS Service Assessment". The word "predetermined" lifts out and holds.
> Eleven days earlier, the E F five in Moore had frightened people out of their houses. That tornado took twenty four lives, by the weather office's count. But the assessment found residents who came through it above ground in the shelters they had planned: closets, bathrooms and safe rooms. It calls those predetermined shelters, meaning places a family had picked before the storm came.

### A5-S8 — narration
**Picture:** text-only card "Harold Brooks · NOAA" with his words as attributed text: "irresponsible at best, and dangerous at worst". Behind it the cutaway house from A1-S2, an inner closet lit.
> Cellars, where people had them, worked too. Harold Brooks, a federal meteorologist, had words for the message that only underground would do. He called it irresponsible at best and dangerous at worst.

### A5-S9 — narration
**Picture:** the 21-pin map splits into two layers: roads lit near El Reno with the small circle crossing one; then the city's low ground shaded blue, water running into the two drains. Every pin falls inside one layer or the other.
> By the table, two things took lives that night. One was the tornado on the open roads near El Reno, where a sub-vortex could cross faster than any car. The other was the water, which ran to the lowest ground in the city. Every one of the twenty one was on a road or in the water.

### A5-S10 — narration
**Picture:** the map holds. A small line of text, "for the night of May 31", then one grey marker far to the east, "Okfuskee County · June 1", outside the frame of pins.
> None of this means a house is a match for a sub-vortex. No house was put to that test that night. And all of this is for that one night. The next morning the flooding took one more life, in Okfuskee County.

### A5-S11 — narration
**Picture:** [HUMAN] two short returns under `data-callback`, each two seconds: the house and ditch drawing with its "a few feet" measure; the traffic aerial with the assessment's words "unable to survive if not underground" over it. Then back to the full map.
> The family of seven were a few feet from their own door, hiding from tornadoes that were real. Many of the people in that traffic had left a house behind them because they were told it would not save them.

### A5-S12 — narration
**Picture:** [RS] [VE] the full 21-pin map, every pin lit, building icons unlit, the line "0 of 21 inside a building · NWS Service Assessment, Appendix C". The map keeps its tag [verify: a place for the 5 pins still unsourced; 16 of the 21 have one, see fact_check.md]. The bed rises under the last sentence and stops with it. The title's line is not spoken here; it is Paul's, next.
> The strongest part of the tornado crossed no building. The tornadoes that reached the city's buildings carried the two lowest ratings. And the water that took thirteen lives ran to the lowest ground, where twelve people were hiding.

*([loop L1 closes] across this segment and Paul's line: three sourced facts, then the title's line once. Stated as the film's reading of the table, inside what the sources say. No claim that a house would stand up to a sub-vortex.)*

### A5-S13 — Paul on camera, slot 5 (line picked by the owner, 9 Oct 26)
**Job:** the title's line, said once in the film's answer and only here: by that count, the safest place was home. He says it at the full 21-pin map, in his own voice, as the film's reading of the table. "Home" means a sturdy house; his wording must not read as covering a mobile home, and a lower third carries "sturdy building, not a mobile home · National Weather Service" under him. No new fact and no cause the sources do not give.
**Budget:** 26 words at most, one clip of about 10 s, full frame.
> That is my reading of the table. No one on it was inside a sturdy building. By that count, the safest place was home.

*(blackout 0.7 s)*


## Z1 · Close (starts about 20:48, runtime about 21:28, measured pace)

### Z1-S1 — narration
**Picture:** the assessment's table one last time, twenty-one lines, the name column absent. Then text-only names over the dimmed map, each landing on the voice, News 9's spellings: "Richard Henderson", "Tim Samaras", "Paul Samaras", "Carl Young", "Samuel Cifuentes", "Florinda Santos", "Alex", "Yolanda Santos", "Cristofer", "Brandon", "Lesly". g-outro begins.
> The weather service's table for the night of May thirty first, twenty thirteen, has twenty one lines, with ages and no names. Among them were Richard Henderson, Tim Samaras, Paul Samaras and Carl Young. Among them were Samuel, Florinda and Alex, and Yolanda with Cristofer, Brandon and Lesly. Among them was Corey Don Johnson, who was three.

### Z1-S2 — narration
**Picture:** the map fades to the outline of the state. Date card "May 31, 2027".
> On May thirty first, twenty twenty seven, it will be fourteen years.

### Z1-S3 — narration
**Picture:** the channel title card (DESIGN.md "Signature closing footnote": it IS the outro).
> Tornadoes don't ask permission. But they do send warnings. Learn what yours sounds like, and where in your own home you would go. Then when it comes, you already know what to do. This was The Warning Hour.

*(outro tail 4 s, g-outro, bed out)*

*(Full draft after the whole-script re-grade, 9 Oct 26. Narration 3,551 words, counted by script with tags stripped. Times are from the voice probe at this episode's tempo: predicted runtime 21:28.)*
