# ep4-el-reno · edit_script.md (v4b: act outline, hook and intro; acts not written yet)

Lane: documentary (`/storm-episode`). Built on the angle the owner locked on 9 Oct 26 (`angle.md`). Facts from
`research/angle-facts-2026-10-09.md` (wins where it disagrees) and `research/facts.md`. Status: DRAFT, nothing locked;
hook and intro wait on the fact-check fan-out, the grader and the owner.

## A. Header
- **Title (owner, verbatim):** El Reno 2013: The Safest Place Was Home
- **Target runtime:** 20 to 25 min; planned at 23:00 until `word_budget.py` sizes it from a probe at the shipping tempo.
- **Claim (locked, copied):** On the night of May 31, 2013, 21 people lost their lives around Oklahoma City, and not one of them was inside a building.
- **Dominant question:** the viewer keeps watching to find out why, on a night of nineteen tornadoes around Oklahoma City, every one of the twenty-one lives was lost outside a building and none inside one.
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
| A3 · Two vehicles, minutes apart | 9:00 to 13:10 | 18.1 % | Two crews inside the same tornado on two roads, US-81 and Reuter Road. The SUV met a small vortex crossing fast; the car met one that sat nearly still for about twenty seconds. The two facts sit side by side and the script never says "this is why". The TV crew's own footage runs here as one sequence under narration. | Pays L2 (open question one). Last segment opens L5, the `cta-hinge`. | Mike Bettes and driver Austin Anderson; Tim Samaras, Paul Samaras and Carl Young; Dan Robinson as the last man to see the Cobalt. |
| Book ad | 13:10 | starts at 57.2 % | Sits between the tease and its payoff. | Inside L5. | none |
| A4 · The twelve and the warning gap | 13:30 to 18:30 | 21.7 % | Twelve people, eight of them aged eight or under, went into two storm drains to hide from tornadoes that were E F zero and E F one in the city, and water took them. The assessment names the lack of Spanish-language warnings beside the family of seven; the script says it sits beside them, never that it caused their choice. Then the fairness block at about 15:45 to 17:10 (68 to 75 %): "the problem with that story is" the weather office's own 1 PM tweet about fleeing by car, set next to the broadcast advice. | Pays L5 in its first sentence (open question two). Opens and pays L6 (who told the city to drive). Ends by opening L7 (all 21 pins on one map, and what is missing from it). | Yolanda Santos Solís and her children Brandon, Leslie and Christopher; Deputy Fire Chief Marc Woodard; Mike Morgan and Gary England in the fairness block. |
| A5 · The map with 21 pins | 18:30 to 22:20 | 16.7 % | The answer. The strongest winds sat in small vortices that crossed no structure, which is also why the rating stayed E F three; every tornado that entered the city was E F zero or E F one; the water went to the lowest ground. The pins sit on roads and in drains, and no pin sits on a building. | Pays L7, then L1 (open question three) in the last 30 to 60 s. | The weather office surveyors in Norman; Harold Brooks of NOAA on "get underground or you will not survive" messaging. |
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
- **Segment after:** A4-S1. Its first sentence is the payoff, first three words if possible: the family of seven.

### Paul on camera (besides the hook), position and job only
1. About 5:25, last line of A1: the owner's hook callback at the act seam; names the hook's claim and points at what was inside the tornado.
2. About 7:10, middle of A2: the turn from how wide it was to what was inside it; names "the tornado inside the tornado" and defines it in twelve words or fewer.
3. About 11:40, A3, after both vehicles have been struck: sets the two vortices side by side in one breath, two facts and no cause.
4. About 13:00, last segment of A3: the `cta-hinge` tease, 25 words at most.
5. About 21:30, A5, at the full 21-pin map: the answer line that returns to the hook's claim, before the close.

### Open items the later acts must tag (from angle-facts "Still open")
Richard Henderson's age; the two rating statements and their dates; the News 9 pages on the family of seven and the pairing of the press names with the table rows; the exact broadcast words; Joshua Wurman's institution; the June 1 flood loss. Each gets a verify tag where it is written, or stays out.

## Writer notes
- Narration numbers follow the shipped Enderlin copy: spelled out, no hyphen ("twenty one"). H1-S1 is the owner's line verbatim, hyphen included.
- "wind" does not occur in the hook, tail or intro. No homograph is respelled here; respelling waits for a TTS probe (`references/homographs.md`).
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- The estimated times on the section headings come from the word counts at the Enderlin intro's shipped pace. They are estimates until a probe at this episode's tempo.

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** Paul on camera, full frame, frame one, speaking this line and nothing else. Popfig "May 31, 2013 · Oklahoma City" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> Twenty-one people lost their lives that night, and not one of them was inside a building.

*([loop L1 open]: why nobody lost their life indoors. Closes in A5.)*


## T1 · Hook tail (0:05)

### T1-S1 — narration
**Picture:** hard cut on the word "night" to mid-action footage, never black: a real clip of the evening sky and loaded highways around Oklahoma City on May 31 (news or public domain; no chaser footage without a licence). A counter "19 tornadoes · NWS Norman" lands on "nineteen". On "Twelve of the twenty one": twenty-one small markers appear in a row and twelve of them light. One bed swell under the last clause, no siren.
> That night was May thirty first, twenty thirteen, around Oklahoma City. The weather service counted nineteen tornadoes in the area that day. Twelve of the twenty one had taken shelter from those tornadoes, and the tornadoes are not what took them.

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The night and the count (0:20)

### I1-S1 — narration
**Picture:** the master map opens: central Oklahoma, Oklahoma City labelled, El Reno marked to its west. Popfig "6:03 PM" and the g-clock starts. A real clip of the tornado over open fields (public domain or licensed news). A bar marked "2.6 miles" draws across the section roads on the last sentence.
> It was a Friday. The storms arrived around rush hour, when many people were already in their cars. At three minutes past six, a tornado touched down in open farmland near El Reno, a town west of Oklahoma City [verify: El Reno lies west of Oklahoma City]. It stayed on the ground for about forty minutes and grew to two point six miles wide.

### I1-S2 — narration
**Picture:** the weather service's assessment on screen, Appendix C, cropped to the table rows. The "Circumstance" column is read down: eight rows highlight and the word "Vehicle" underlines in each. On the map eight pins drop along the El Reno track. Eighteen other small tracks draw in grey, each with a "0". A soft hit on each group, not on each pin.
> The National Weather Service later published a table of every life lost that night, with each person's age and where they were. Eight were in the path of the El Reno tornado, and all eight were in vehicles. Eighteen other tornadoes touched down that day. None took a life.

### I1-S3 — narration
**Picture:** the map slides east to Oklahoma City. Public domain footage of flooded city streets that night. Back to the table: one row "Vehicle, flash flood", then twelve rows "Sheltering in drainage ditch, flash flood" highlight together. The age column ticks eight of the twelve. Text card "5 months". Twelve pins land at two points in the city, one more for the vehicle. The bed thins to rain.
> The other thirteen were lost to flood water, as the same storms poured rain over the Oklahoma City area. One of them was in a vehicle. Twelve were sheltering in drainage ditches and storm drains, and eight of those twelve were children aged eight or under. The youngest of the twelve was five months old.

### I1-S4 — narration
**Picture:** [RS] [VE] the full map, all twenty-one pins lit for the first time. Every pin sits on a road or a drain; the building icons on the map stay unlit. Text line "0 of 21 inside a building · NWS Service Assessment, Appendix C". Hold the map through the second sentence. Pin positions wait on sourcing [verify: a location for each of the 21 Appendix C rows, needed to place the pins; the table gives a circumstance, not a place].
> Nowhere on that table is a house, a store, a school or a storm shelter. That night, the safest place around Oklahoma City was home, and many people had just driven away from theirs.

### I1-S5 — narration
**Picture:** a real news aerial of a jammed highway that evening. Popfig "Moore · May 20, 2013 · EF5", then "11 days earlier". Study card "6 metro areas, 2011 to 2018 · Weather, Climate, and Society, 2022" over the traffic.
> Eleven days earlier, an E F five tornado had gone through Moore, Oklahoma. People later told the weather service that fear from that day led them to do things they normally would not. A twenty twenty two study compared tornado evacuations in six American metro areas, and none came near the size of this one.

### I1-S6 — narration
**Picture:** the map pushes in on the track. Two vehicle markers on two labelled roads, "US-81" and "Reuter Road", so the two roads read at a glance. A news still of the Weather Channel vehicle after the storm (licence check; the crew's own footage is held for A3). Name card "Mike Bettes · The Weather Channel". A "200 yards" line draws from the road into the field.
> Two of the vehicles inside the El Reno tornado carried storm chasing crews, with three people in each. One was a Weather Channel S U V carrying the meteorologist Mike Bettes. The tornado threw it about two hundred yards.

### I1-S7 — narration
**Picture:** the second marker lights on Reuter Road. Name cards "Tim Samaras · 55", "Paul Samaras · 24", "Carl Young · 45", text only. Two marks on the g-clock, minutes apart.
> The other was a white Chevrolet Cobalt carrying the researcher Tim Samaras, his son Paul [verify: Paul Samaras was Tim Samaras's son] and Carl Young. It was struck minutes later, on a different road.

### I1-S8 — narration
**Picture:** split frame: left "3 of 3 survived" over the S U V marker, right "0 of 3" over the Cobalt marker. Then a self-made radar replot of the wide circulation with two small circles inside it, unlabelled. Hold on the two circles through the last sentence; the bed drops out on the last word.
> Everyone in the S U V survived. No one in the Cobalt did. Scientists later rebuilt both moments from radar, and what struck the S U V is not what struck the car.

*([loop L2 open]: why one crew survived. Closes in A3 with the two vortices side by side, no cause stated.)*

*(blackout 0.7 s)*


*(A1 onward: not written. Outline in section B.)*
