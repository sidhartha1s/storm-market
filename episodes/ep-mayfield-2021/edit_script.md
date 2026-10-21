# ep-mayfield-2021 · edit_script.md (TTS segment format)

Lane: documentary (`/storm-episode`).
Status: DRAFT hook+intro for owner gate; acts are cards only. H1, T1 and I1 carry full prose; A1 to A5 and Z1 are
chapter cards, no narration yet. Nothing here goes to TTS until its section locks (markers resolved, owner approval,
hook passes the grader).

Proposed runtime: **21 to 24 min** (owner confirms). Reason: an open of about two and a half minutes, five acts of
three to four minutes and a three minute close. The material carries that much: two workplace arcs, a seven-day
forecast countdown, an explainer, the inspections and the Service Assessment close. It does not carry more, because
the picture is thin where it matters (no public-domain picture of the Amazon building, nothing from inside the factory,
no 911 or weather-radio audio found). Past 24 min the extra minutes would be stretched beats, not new acts.

Script concept (the angle's Claim, copied): The forecast was right days ahead, and nobody had told big workplaces
what to do.

Dominant question: the viewer keeps watching to find out how a forecast that was right four days out still ended with
people losing their lives at work, and why nobody had told those buildings where to send their people.

Architecture: **Countdown / Detective hybrid.** The countdown is the forecast clock (Day 8 on 3 Dec, Memphis on 6 Dec,
Slight, Enhanced, Moderate, the watches, the warnings) running toward each building. The detective layer is the
Weather Service's own review working out what was missing, paid in the close (Finding 6).

Hook sound: the civil-defence siren (`soundreality-civil-defense-siren-128262.mp3`), low under Paul's line from 0:00,
swelling into H1-S2. Reason: this story IS a warning, and the hook's question is literally what you do when a tornado
warning goes off at work. The siren puts the viewer in that moment before a word is explained. No broadcast, radio or
archive audio in the hook. A low drone bed takes over at T1.

## CTA hinge
Planned inside **A3** (the night the track ran), at about 11:30 of a 23 min cut (about 50 %, inside the 40 to 60 %
band; the editor checks it against `config.yaml channel.cta.window` once timed).
- Segment before: **A3-S9** (planned id), ends on the tease, at most 25 words. Draft tease (also Paul on camera, line P3):
  "Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own."
  [verify: tornado reached Mayfield around 9:25 to 9:30 PM CST]
- CTA file mounts here (`config.yaml channel.cta`, own VO).
- Segment after: **A3-S10** (planned id), payoff in its first sentence: "The power went out." Then: the Paducah office lost
  commercial power about nine twenty-five, its backup generator failed, and the Tornado Emergency for Mayfield still went
  out at nine twenty-six (SA p29, p30, p47).

## Paul on camera
| Mark | Where | Line (at most about 26 words) |
|---|---|---|
| HOOK | H1-S1, frame one | "A tornado warning goes off while you're at work. What do you do? You go where they tell you. Somebody planned for this." (22 words) |
| P1 | A1 exit, the turn from building to forecast | "Edwardsville met the minimum the federal rules asked for. What I couldn't find was anyone who'd told a building that big what the minimum should be." |
| P2 | A2 exit, the forecast was never the weak link | "That week, the forecast got louder every single day, and it was right. The trouble was waiting further down the line." |
| P3 · cta-hinge tease | A3-S9, right before the CTA | "Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own." (18 words) |
| P4 | A4, the strongest warning there is | "At nine twenty-six, Paducah used the strongest words a warning can carry. A Tornado Emergency, for Mayfield, by name." |
| P5 | Z1, the answer to the dominant question | "The forecast was right days ahead. What was missing was one page telling a building that big where its people should go." |

## Loop table
| Loop | Question the viewer holds | Planted | Paid |
|---|---|---|---|
| E1 (episode) | Who was supposed to tell big buildings where to shelter, and did anyone ever do it? | H1-S4 `[loop E1 open]` | Z1: Finding 6, Recommendation 6, the Illinois 2025 law `[loop E1 closes]` |
| L1 (A1) | What happened inside the Edwardsville building in those twenty-five minutes? | T1-S1, carried by I1-S7 (the megaphone) | A1 `[loop L1 closes]` |
| L2 (A2) | If the forecast was on the map for a week, how much did each office say, and when? | A1 exit (P1) | A2: the countdown and Finding 3a, "established playbooks" `[loop L2 closes]` |
| L3 (A3) | How does December, at night, make a tornado that stays down for a hundred sixty-five miles? | A2 exit: Memphis wrote "well into the 70s" for a December Friday | A3 explainer `[loop L3 closes]` |
| cta-hinge | What went wrong at the weather office as the storm reached Mayfield? | A3-S9 tease (P3) | A3-S10, first sentence: "The power went out." |
| L4 (A4) | The factory had a warning at nine-oh-five. What reached the people inside? | A3 exit: the track crosses into Graves County | A4 `[loop L4 closes]` |
| L5 (A5) | When the inspectors came, what rule could they measure a shelter plan against? | A4 exit | A5: "OSHA does not have a standard that requires severe weather emergency plans" `[loop L5 closes]` |

Intro micro-loops (each paid inside 45 s, L1 carried into Act 1): Q1 "why December" (I1-S1 to I1-S2), Q2 "what did the
forecasters see, and when" (I1-S2 to I1-S3), Q3 "what didn't the word come with" (I1-S4 to I1-S5), Q4 "what did the
office that saw it first-hand say" (I1-S5 to I1-S6).

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** Paul on camera, full frame, frame one (HOOK line). Popfig inside the first second: "December 10, 2021 · Edwardsville, Ill. · Mayfield, Ky." Siren low under him from 0:00.
> A tornado warning goes off while you're at work. What do you do? You go where they tell you. Somebody planned for this.

### H1-S2 — narration
**Picture:** hard cut on the siren swell to our own NEXRAD Level II replot of the Mayfield supercell at night (mid-action, never black). Chip "14 lives · at work". Map pins drop on Edwardsville, Illinois and Mayfield, Kentucky.
> On a Friday night in December, twenty twenty one, fourteen people lost their lives at work, in Illinois and in Kentucky. [verify: 14 = 6 Edwardsville + 8 candle factory; factory count is AP's 8, with 9 and 6 also published; official count unread]

### H1-S3 — narration
**Picture:** the NWS Memphis Area Forecast Discussion, IEM archive page, issuance "336 PM CST Mon Dec 6 2021", the line "could be another severe weather threat" highlighting word by word. Chip "4 days out". Stamp "RIGHT" lands on the last sentence.
> Four days earlier, a forecaster in Memphis had written that Friday could be another severe weather threat. The forecast was right.

### H1-S4 — narration
**Picture:** DVIDS/FEMA still of the candle factory site (dvidshub.net/image/7018049), slow push. Attributed text chip: "no official guidance on sheltering in the workplace · NWS St. Louis, quoted in the Service Assessment".
> And no official guidance existed for where to shelter in a building that big.

*[loop E1 open]*


## T1 · Hook tail (0:28)

### T1-S1 — narration
**Picture:** our own map of Madison County, Illinois: the EF3 track, 3.65 miles, draws toward a building outline in Edwardsville (no PD picture of the Amazon building exists; the outline is ours). Clock chip "about 25 min" (SA p29). Drone bed takes over from the siren.
> That night the warnings went out, too. The Amazon building in Edwardsville, Illinois got about twenty-five minutes, and it had no storm shelter. Where people went in those minutes is the first thing I looked up.

*[loop L1 open]* *(no void: straight into the intro, the line stays in the hook's scene)*


## I1 · Intro: the whole picture (0:42)

### I1-S1 — narration
**Picture:** NASA MODIS image of the long track, then our own eight-state map as seventy-one tracks draw in. Chips "71 tornadoes", "8 states", "89 lives". Source line on screen: "NWS Service Assessment, p4".
> That Friday, seventy-one tornadoes came down across eight states, and eighty-nine people lost their lives. It was the deadliest December tornado event on record since nineteen fifty. Six were people working at the building in Edwardsville. Eight were at a candle factory in Mayfield, Kentucky. And it happened in December. [verify: candle factory count 8 (AP, 14 Dec 2021); 9 and 6 also published]

*[Q1 open: why December]*

### I1-S2 — narration
**Picture:** NASA VIIRS night-lights over western Kentucky, before and after. Chip "after sunset · a Friday" (SA p6).
> The weather service's own report says the timing made it harder. People don't connect December with tornadoes, and these came after sunset on a Friday. If you've lived in western Kentucky, December is coat weather. The forecasters had been watching that Friday for a week, though.

*[Q1 closes]* *[Q2 open: what did they see, and when]*

### I1-S3 — narration
**Picture:** SPC Day 4-8 outlook archive text, 3:20 AM CST Fri 3 Dec, the Day 8 line lit; an empty map beside it with chip "no risk area yet". Then back to the Memphis discussion page, Monday 3:36 PM.
> On December third, the Storm Prediction Center first mentioned severe storms for the tenth. That was eight days out, and it didn't draw a risk area yet. On Monday afternoon, the Memphis office wrote that Friday could be another severe weather threat.

*[Q2 closes]*

### I1-S4 — narration
**Picture:** SPC archive outlook maps in sequence: Day 3 Slight (Wed 8 Dec, 2:15 AM), Day 2 Enhanced (Thu 9 Dec), Day 1 Moderate (Fri 10 Dec, 10:18 AM). Chip "sent 12 min early" on the Moderate map.
> By Wednesday there was a Slight Risk on the map, from northern Louisiana up into western Kentucky and southern Indiana. By Friday morning it was a Moderate Risk, sent out twelve minutes early to get the word out. What the word didn't come with was instructions for a building like these two.

*[Q3 open: what was missing]*

### I1-S5 — narration
**Picture:** Service Assessment cover, then p33 and p34; Finding 6 as attributed on-screen text, "a gap in NWS safety outreach and resources related to buildings with large footprints, such as warehouses".
> I read the whole review the weather service wrote afterward. It found a gap in its own safety outreach for buildings with large footprints, like warehouses. Its office in St. Louis, the one that covers Edwardsville, put it more plainly.

*[Q3 closes]* *[Q4 open: what St. Louis wrote]* [verify: WFO St. Louis's area includes Edwardsville, Madison County, Illinois]

### I1-S6 — narration
**Picture:** the WFO St. Louis after-action words as attributed text, quoted in the SA p33-34, three lines building one at a time. Then the claim on a clean card.
> That office wrote that there were no official recommendations for sheltering at work. There was no guidance on which warnings to shelter for, and nothing different for a big warehouse. The forecast was right days ahead, and nobody had told big workplaces what to do.

*[Q4 closes]*

### I1-S7 — narration
**Picture:** back to our Edwardsville map; the EF3 track meets the building outline. Clock chip "8:27 PM" (SA p29). Hold on the outline, then chapter blackout into A1.
> Edwardsville came first. At about eight twenty-seven that night, the tornado hit the Amazon delivery station, and the warning had been out about twenty-five minutes. Inside, the story of those minutes starts with a megaphone.

*[loop L1 carried into A1]* *(chapter blackout, hand-placed)*

---

## Chapter cards (cards only this round: no narration until the hook and intro lock)

Stakes order, not chronology. Each act changes what the viewer understood. Every act serves the Claim.

## A1 · Edwardsville: twenty-five minutes (about 2:30 to 6:00)
- **Purpose:** the first workplace. Show what a correct, on-time warning met inside a building with no shelter and no rule telling it where to put people.
- **Question:** what happened inside the building in those twenty-five minutes? (L1, carried from T1 and I1-S7)
- **Reveal:** the building was 1.1 million square feet with tilt-up walls and no storm shelter; city code asked for 90 mph wind resistance, and this was a 150 mph EF3 (SA p59; St. Louis Public Radio). OSHA sent a Hazard Alert Letter with no citation and no penalty, and said the procedures "met minimal federal safety guidelines for storm sheltering". Reported details (AP via Claims Journal): the written plan did not name a shelter location, the megaphone meant to start shelter-in-place was locked in a cage, some workers could not recall drills. The six were contractors working at the building (five delivery drivers, one building-services worker). WFO St. Louis staff had sheltered themselves at 7:45 to 7:53 PM. One named person, age, job, sourced quote [verify: none in the fact sheet]. Escalation: interesting, then surprising.
- **Visual event:** [RS] the building outline scaled against football fields as the 90 mph and 150 mph bars fill side by side [verify: 1.1 million sq ft in football fields]; the 25-minute clock running out over the outline.
- **Exit hook:** P1 on camera, then: the forecast for this night had been on the map for a week. `[loop L2 open]`
- Legal care: no blame; say "met minimal federal guidelines" and "no guidance existed". "Did not find any violations" is Amazon's spokesperson, never OSHA.

## A2 · The week the forecast held (about 6:00 to 9:30)
- **Purpose:** prove the first half of the Claim on the record. The forecast was right days ahead.
- **Question:** if it was on the map for a week, how much did each office say, and when? (L2)
- **Reveal:** the full countdown: SPC Day 8 on 3 Dec (no risk area, Finding 1); ECMWF Extreme Forecast Index flagged it at Day 7 (SA p45); Memphis on Mon 6 Dec 3:36 PM, repeated in three later issuances; WFO Paducah's first partner call that Monday (SA p14); Slight Wed 2:15 AM, about 60 hours before the first reports; Enhanced Thu with a 10 % tornado and a hatched area; Moderate Fri 10:18 AM, 15 % hatched, sent 12 minutes early "to get the word out"; Tornado Watch 552 at 3:00 PM (first of eleven), 6 h 25 min before Mayfield; Watch 553 at 5:20 PM, about 3 hours before Edwardsville. The twist: Finding 3a, some offices waited until Day 1 or 2 "in part due to established playbooks"; Recommendation 3, say what you know when you know it (SA p15). One named forecaster, sourced [verify: named forecaster and quote].
- **Visual event:** [RS] the countdown clock with each product stamping onto a growing risk map; [RS] Finding 3a as attributed text.
- **Exit hook:** P2 on camera. Then the Memphis line "Friday we should be well into the 70s" back on screen: seventy degrees, in December. `[loop L3 open]`

## A3 · Why December, why so long (about 9:30 to 13:30) · meteorology explainer · CTA hinge inside
- **Purpose:** the explainer layer: why a December night could make violent, long-track tornadoes, and how the long-track storm set out for Mayfield.
- **Question:** how does December, at night, make a tornado that stays down for a hundred sixty-five miles? (L3)
- **Reveal:** warm air advection and the 70s in Memphis ahead of a front (Memphis AFD); a pair of long-track, violent EF4s (SA p12): Bay, Arkansas to Samburg, Tennessee, 80.3 miles at 170 mph, and the Mayfield storm, near Woodland Mills, Tennessee at 8:49 PM to Falls of Rough, Kentucky at 11:47 PM, 165.6 miles, 190 mph, up to 1.13 miles wide, the longest tracked December tornado on record. SPC issued a record 28 mesoscale discussions that evening (SA p12). The mechanism lines are not in the fact sheet: [verify: Gulf moisture plus a strong jet stream in December; why the supercell stayed isolated and kept one tornado down so long; named researcher and institution for the mechanism]. The ruled-out lead stays a fact here, never the headline.
- **Visual event:** [RS] our own NEXRAD Level II replot loop, the hook echo crossing the Tennessee line; NASA MODIS track drawn end to end against a US landmark distance [verify: comparator, e.g. a drive the viewer knows].
- **CTA hinge:** A3-S9 tease (P3), CTA, A3-S10 payoff "The power went out." (see CTA hinge above).
- **Exit hook:** the track crosses into Graves County, and the county's warning goes out at 9:05 PM. `[loop L4 open]`

## A4 · The candle factory (about 13:45 to 17:45)
- **Purpose:** Arc 2, the bigger loss: the same correct forecast, the strongest warning there is, and still no guidance for a building that big.
- **Question:** the factory had a warning at nine-oh-five; what reached the people inside? (L4)
- **Reveal:** Graves County tornado warning 9:05 PM; Tornado Emergency for Mayfield 9:26 PM with the county emergency manager called directly (SA p29, p47), lead about 20 minutes (derived, not an SA figure: say "about twenty minutes" with the derivation on the source line); about 110 people inside (Spectrum News); eight lost their lives [verify: official count, Graves County coroner or Kentucky state; 9 and 6 also published]; the Graves County toll of 24 and 57 on the whole track (NWS Paducah event page). Night shift for seasonal orders [verify: unverified in the fact sheet]. One named person, age, job, sourced quote [verify: none in the fact sheet]. Never the Facebook Live from under the rubble, never chaser or drone aerials. Firing-threat claims only as allegations, attributed: at least five workers told NBC News supervisors warned they would be fired for leaving; the company spokesman called the claims "absolutely untrue". Both sentences together, or neither. Escalation: disturbing, then personal.
- **Visual event:** [RS] P4 on camera; DVIDS/FEMA candle-factory gallery stills; Kentucky Guard and Army Corps Mayfield photos; NWS Paducah survey photos.
- **Exit hook:** then the inspectors came, and they needed a rule to measure a shelter plan against. `[loop L5 open]`

## A5 · What the inspectors could check (about 17:45 to 20:30) · the debunk block
- **Purpose:** the sourced debunk at 60 to 75 %: the belief "there's a federal rule that says a workplace needs a tornado plan". The record says otherwise.
- **Question:** what rule could the inspectors measure a shelter plan against? (L5)
- **Reveal:** "OSHA does not have a standard that requires severe weather emergency plans but recommends them" (OSHA release, 26 Apr 2022). Amazon: Hazard Alert Letter, no citation, no penalty. The candle plant: Kentucky's state OSHA program cited 7 serious violations, $40,000 proposed (exit routes 1, emergency action plans 2, four under the pathogens standard); the company contested all seven; no outcome found through 2026; none of the seven is about a shelter. Say "cited" and "contested", never "fined". The 2019 $9,810 settlement is a separate matter and stays separate, or out. Lawsuits so far: procedural rulings only (Mar 2023; Kentucky Court of Appeals remand, 18 Jun 2026).
- **Visual event:** [RS] the citation list as an on-screen ledger with "contested" stamped on each line; the OSHA sentence as attributed text.
- **Exit hook:** so the only people writing down what was missing were the forecasters themselves. `[loop E1 still open, paid in Z1]`
- Legal care: no company blamed; the gap is the guidance.

## Z1 · Finding 6 (about 20:30 to 23:30) · close
- **Purpose:** answer the dominant question and pay E1: the gap was written down by the Weather Service itself, and one state has acted on it since.
- **Question:** who was supposed to tell big buildings where to shelter, and has anyone done it? (E1)
- **Reveal:** SA p33, the common theme "of a gap in NWS safety outreach materials or resources for buildings with large footprints", found as a result of the damage and the lives lost at large warehouse buildings (paraphrased: the SA's own word is on the flag-words list). Finding 6 (p34): "a gap". Recommendation 6: develop "materials with basic tornado safety guidelines for large facilities". WFO St. Louis's own words for "no guidance", attributed to it. What changed: Illinois Warehouse Tornado Preparedness Act (HB 2987, signed Aug 2025): every warehouse needs a tornado plan, new warehouses a designated refuge area. Kentucky: no law or OSHA rule found [verify: absence]. Whether NWS has published the Recommendation 6 materials [verify: unverified]. Fact plus a dated forward window [verify: an effective date or deadline for the Illinois act].
- **Visual event:** [RS] P5 on camera; Finding 6 and Recommendation 6 as attributed text; a map with Illinois lit and Kentucky not.
- **Exit:** the answer in the last 30 to 60 s, then the CTA spine once, then the signature line.
- **Signature line slot:** [signature closing footnote per DESIGN.md, written at the act round]

---

## Calls made (writer)
- Runtime band 21 to 24 min proposed (reason in the header); acts sized to it.
- Hook rewritten true: "four days" from Memphis's Monday discussion, and the hedged "could be another severe weather threat" quoted near-verbatim instead of "warned of exactly this". The card's draft hook was not used.
- Hook says "fourteen" and the intro splits it six and eight; both carry the factory-count `[verify]`.
- The "no guidance" words are said as WFO St. Louis's (I1-S5, I1-S6); Finding 6 is said as "a gap". The hook's flat line "no official guidance existed" follows the legal-care wording and is attributed on screen.
- Firing-threat allegations kept out of H1, T1 and I1; they sit in A4 only, attributed, with the denial.
- Edwardsville has no PD picture of the building: our own map and outline carry T1 and I1-S7.
- Siren under the hook only; drone bed from T1.
- CTA hinge placed inside A3 (both sides of it in one act), around 50 %.
- Years spoken as words ("twenty twenty one"), matching ep-enderlin-2025.
- Loop and question tags sit on their own lines after each quote so TTS never voices them; `[verify]` markers sit inline in the narration as the gate asks.
- Rationed devices used: "though" aside (I1-S2), first-person "I read the whole review" (I1-S5), "the first thing I looked up" (T1). Three in the open; the acts must ration from zero for their own.

## Self-scores ("a person talking to you", 1 to 10)
- H1: 8. The question and answer read like a friend; H1-S4 is a little flat.
- T1: 9. First person and plain.
- I1: 8. S3 and S4 carry a countdown of product names, which slides toward report register; the "coat weather" line and the first-person lines pull it back.
