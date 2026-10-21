# ep-mayfield-2021 · edit_script.md (TTS segment format)

Lane: documentary (`/storm-episode`).
Status: DRAFT hook+intro for owner gate; acts are cards only. Fix rounds 1 and 2 (21 to 22 Oct 26): H1, T1 and I1 rewritten from `research/grade-hook-intro-v2.tsv`,
`research/grade-hook-intro.tsv` and `research/fc-slice-a/b/c.tsv`. A1 to A5 and Z1 are chapter cards, no narration yet.
Nothing here goes to TTS until its section locks (markers resolved, owner approval, hook passes the grader).

Proposed runtime: **21 to 24 min** (owner confirms). Reason: an open of about two minutes, five acts of three to four
minutes and a three minute close. The material carries that much: two workplace arcs, a week-long forecast countdown,
an explainer, the inspections and the Service Assessment close. It does not carry more, because the picture is thin
where it matters (no public-domain picture of the Amazon building, nothing from inside the factory, no 911 or
weather-radio audio found). Past 24 min the extra minutes would be stretched beats, not new acts.

Script concept (the angle's Claim, copied): The forecast was right days ahead, and nobody had told big workplaces
what to do.

Dominant question: the viewer keeps watching to find out how a forecast that was right days ahead still ended with
people losing their lives at work, and whether anyone has written the advice those buildings never had.

Architecture: **Countdown / Detective hybrid.** The countdown is the forecast clock (Friday 3 Dec Day 8, Monday 6 Dec
Memphis, Slight, Enhanced, Moderate, the watches, the warnings) running toward each building. The detective layer is
the Weather Service's own review working out what was missing, and the close checks whether anyone fixed it.

Hook sound: the civil-defence siren (`soundreality-civil-defense-siren-128262.mp3`), low under Paul's line from 0:00,
swelling into H1-S2. Reason: this story IS a warning, and the hook's question is what you do when a tornado warning
goes off at work. The siren puts the viewer in that moment before a word is explained. No broadcast, radio or archive
audio in the hook. A low drone bed takes over at T1.

## CTA hinge
Planned inside **A3** (the night the track ran), at about 11:30 of a 23 min cut (about 50 %, inside the
`config.yaml channel.cta.window` of 0.40 to 0.60, per fc-slice-c).
- Segment before: **A3-S9** (planned id), ends on the tease, at most 25 words. Draft tease (also Paul on camera, line P3):
  "Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own." (18 words; the
  tornado reached Mayfield at 9:26 PM, NWS Paducah event page; Paducah lost power about 9:25 PM, SA p30)
- CTA file mounts here (`config.yaml channel.cta`, own VO).
- Segment after: **A3-S10** (planned id), payoff in its first sentence: "The power went out." Then: the Paducah office lost
  commercial power about nine twenty-five, its backup generator failed, and the Tornado Emergency for Mayfield still went
  out at nine twenty-six (SA p29, p30, p47).

## Paul on camera
| Mark | Where | Line (at most about 26 words) |
|---|---|---|
| HOOK | H1-S1, frame one | "A tornado warning goes off at work. What do you do? You go where they tell you. Somebody planned for it." (21 words) |
| P1 | A1 exit, the turn from building to forecast | "OSHA said the procedures met minimal federal safety guidelines for storm sheltering." |
| P2 | A2 exit | "That week, the forecast kept getting stronger, and it was right." |
| P3 · cta-hinge tease | A3-S9, right before the CTA | "Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own." (18 words) |
| P4 | A4, the strongest warning there is | "At nine twenty-six, Paducah issued a Tornado Emergency, the Weather Service's highest alert, for Mayfield by name." |
| P5 | Z1, the answer to the dominant question | "The forecast was right days ahead. The review asked for basic tornado safety guidelines for large facilities, and Illinois now makes warehouses write a tornado plan." |

## Loop table
Fix 4 choice: **E1 re-aimed.** The hook and intro now carry the gap itself (Finding 6 in the voice, the St. Louis
after-action words in I1-S5), because they are the WHAT. E1 becomes "has anyone written that advice since?", which only
Z1 can pay (Recommendation 6, the Illinois 2025 law, Kentucky, whether NWS published the materials).

| Loop | Question the viewer holds | Planted | Paid |
|---|---|---|---|
| E1 (episode) | Almost five years on, has anyone written the advice those buildings never had? | I1-S6 `[loop E1 open]` (set up by H1-S2) | Z1: Recommendation 6, the Illinois 2025 law, Kentucky, NWS materials `[loop E1 closes]` |
| L1 (A1) | Both buildings had a warning first. What happened between the warning and the hit? | T1-S1, asked aloud ("What happened inside in those minutes"), carried by I1-S7 (more than twenty minutes, the megaphone teased; the cage held for A1) | A1 `[loop L1 closes]` |
| L2 (A2) | If the forecast was on the map for a week, how much did each office say, and when? | A1 exit (P1) | A2: the countdown and Finding 3a, "established playbooks" `[loop L2 closes]` |
| L3 (A3) | How does December, at night, make a tornado that stays down for a hundred sixty-five miles? | A2 exit: Memphis wrote "well into the 70s" for a December Friday | A3 explainer `[loop L3 closes]` |
| cta-hinge | What went wrong at the weather office as the storm reached Mayfield? | A3-S9 tease (P3) | A3-S10, first sentence: "The power went out." |
| L4 (A4) | The factory had a warning at nine-oh-five. What reached the people inside? | A3 exit: the track crosses into Graves County | A4 `[loop L4 closes]` |
| L5 (A5) | When the inspectors came, what rule could they measure a shelter plan against? | A4 exit | A5: "OSHA does not have a standard that requires severe weather emergency plans" `[loop L5 closes]` |

Intro micro-loops (each paid inside 45 s, L1 carried into Act 1): Q1 "what had the forecasters seen" (I1-S1 to I1-S2),
Q2 "why was the forecast harder to get across" (I1-S2 to I1-S3), Q3 "what is a million square feet like" (I1-S3 to
I1-S4), Q4 "what did the St. Louis office write" (I1-S4 to I1-S5). L1 is asked aloud in T1. No "why December" loop in the intro: A3 owns it.

---

## H1 · Hook (0:00)

### H1-S1 — narration
**Picture:** Paul on camera, full frame, frame one (HOOK line). Popfig inside the first second: "December 10, 2021 · Edwardsville, Ill. · Mayfield, Ky." Siren low under him from 0:00.
> A tornado warning goes off at work. What do you do? You go where they tell you. Somebody planned for it.

### H1-S2 — narration
**Picture:** hard cut on the siren swell to the DVIDS/FEMA still of the candle factory site (dvidshub.net/image/7018049, image only, never its caption), slow push. Chip "14 lives · 2 workplaces". Source line: "6 at Edwardsville (House Oversight; OSHA) · 8 at the factory: Mayfield Consumer Products and AP, 14 Dec 2021".
> One Friday night in December, fourteen people lost their lives at two workplaces.

### H1-S3 — narration
**Picture:** our own NEXRAD Level II replot of the supercell at night (mid-action). On-screen quote over it, verbatim: "a gap in NWS safety outreach and resources related to buildings with large footprints, such as warehouses" · Service Assessment, Finding 6. Stamp "RIGHT" lands on "right".
> The Weather Service's own review found a gap in its safety advice for buildings as big as warehouses. And the forecast was right.


## T1 · Hook tail (0:20)

### T1-S1 — narration
**Picture:** no radar here: a plain map with the two tornado warning polygons alone, 8:06 PM over Madison County, Illinois (SA p28) and 9:05 PM over Graves County, Kentucky (SA p29), pins on Edwardsville and Mayfield; then a Kentucky Guard still of Mayfield. Drone bed takes over from the siren.
> One was an Amazon delivery station in Edwardsville, Illinois. The other was a candle factory in Mayfield, Kentucky. Both got a tornado warning before the tornado arrived. What happened inside in those minutes is the first thing I looked up.

*[loop L1 open]* *(no void: straight into the intro, the line stays in the hook's scene)*


## I1 · Intro: the whole picture (0:35)

### I1-S1 — narration
**Picture:** NASA MODIS image of the long track, then our own map drawn from SA Appendix C as seventy-one tracks draw in (no state count on screen). Chips "71 tornadoes", "89 lives", then "1953 · 38" beside "2021 · 89". Source line: "NWS Service Assessment, p4: deadliest December tornado event on record since 1950".
> From Friday evening into Saturday, the Weather Service confirmed seventy-one tornadoes, and eighty-nine people lost their lives. Since nineteen fifty, no December tornado outbreak has taken more lives. The old record was thirty-eight lives, in Vicksburg, Mississippi, in nineteen fifty-three. And the people whose job is to see that coming had seen it.

*[Q1 open: what had they seen]*

### I1-S2 — narration
**Picture:** the SPC Day 4-8 outlook archive text, 3:20 AM CST Fri 3 Dec, the Day 8 line lit (one beat only; the countdown is A2's). Then Army Corps or Kentucky Guard photo of the factory site; chip "about 110 inside" (Spectrum News).
> A week ahead, the Storm Prediction Center had already named that Friday for severe storms. That night, about a hundred ten people were at work inside the candle factory in Mayfield. The review says a forecast like this one was harder to get across, and it says why.

*[Q1 closes]* *[Q2 open: why it was harder]*

### I1-S3 — narration
**Picture:** NASA VIIRS night-lights over western Kentucky, before and after. Chip "after sunset" (SA p6). Then our own Edwardsville building outline (labelled illustrative) growing to its full size.
> The storms were forecast for after sunset, in December. If you've lived in western Kentucky, you know December is coat weather. And the building in Edwardsville covered more than a million square feet.

*[Q2 closes]* *[Q3 open: what a building that size is like inside]*

### I1-S4 — narration
**Picture:** the outline fills with football fields laid end to end; chip "6 lives". Then a Mayfield survey photo (NWS Paducah); chip "8 lives" with source line "Mayfield Consumer Products and AP, 14 Dec 2021".
> That's about nineteen football fields under one roof. [verify: 1.1 million sq ft as about nineteen football fields, end zones included] Six people working there lost their lives. At the candle factory, eight did. Afterward, the weather office in St. Louis, the one covering Edwardsville, wrote down what nobody had told buildings like that.

*[Q3 closes]* *[Q4 open: what St. Louis wrote]*

### I1-S5 — narration
**Picture:** the WFO St. Louis after-action words as on-screen text, verbatim with the ellipsis marked, attributed "WFO St. Louis after-action review, quoted in the Service Assessment, p33-34". Paul's voice says it plainly; the card carries the exact words.
> That office wrote that nobody, not the weather service and not OSHA, had told businesses where to shelter people at work. Nobody had said which warnings to shelter for, or what a big warehouse needs.

*[Q4 closes]*

### I1-S6 — narration
**Picture:** a real picture between the text screens: NWS Paducah survey photo of Mayfield, slow push; then the claim on a clean card.
> The forecast was right days ahead, and nobody had told big workplaces what to do. Almost five years on, I went to find out if anyone has written that advice since.

*[loop E1 open]*

### I1-S7 — narration
**Picture:** back to our Edwardsville map; the EF3 track meets the building outline. Clock chips "8:06 PM warning" and "8:27 PM" (SA p28, p29). A drawn megaphone, alone, then chapter blackout into A1 (the cage is A1's reveal).
> Edwardsville came first. At about eight twenty-seven, the tornado hit the delivery station, and the warning had been out for more than twenty minutes. The first thing OSHA's letter lists is a megaphone, and where it was that night.

*[loop L1 carried into A1]* *(chapter blackout, hand-placed)*

---

## Chapter cards (cards only this round: no narration until the hook and intro lock)

Stakes order, not chronology. Each act changes what the viewer understood. Every act serves the Claim.

## A1 · Edwardsville: more than twenty minutes (about 2:00 to 5:30)
- **Purpose:** the first workplace. Show what a correct, on-time warning met inside a building with no reinforced storm shelter and no weather-service guidance for its size.
- **Question:** what happened between the 8:06 PM warning and the hit at about 8:27 PM? (L1, carried from T1 and I1-S7)
- **Reveal:** the building was 1.1 million square feet with tilt-up walls and no reinforced storm shelter; workers were sent to a designated interior area (a south-side bathroom, per OSHA); codes did not require a shelter; city code asked for 90 mph wind resistance, and this was a 150 mph EF3 (SA p59; St. Louis Public Radio). OSHA sent a Hazard Alert Letter with no citation and no penalty, and said the procedures "met minimal federal safety guidelines for storm sheltering". OSHA's letter lists the megaphone first (locked in a cage); reported details (AP via Claims Journal): the written plan did not name a shelter location, some workers could not recall drills. The six were contractors working at the building (five delivery drivers, one building-services worker). WFO St. Louis staff had sheltered themselves at 7:45 to 7:53 PM. One named person, age, job, sourced quote [verify: none in the fact sheet]. Escalation: interesting, then surprising.
- **Visual event:** [RS] the building outline scaled against football fields as the 90 mph and 150 mph bars fill side by side [verify: 1.1 million sq ft in football fields]; the 8:06 to 8:27 clock running out over the outline.
- **Exit hook:** P1 on camera, then: the forecast for this night had been on the map for a week. `[loop L2 open]`
- Legal care: no blame; say "met minimal federal safety guidelines" and "no guidance existed". "Did not find any violations" is Amazon's spokesperson, never OSHA.

## A2 · The week the forecast held (about 5:30 to 9:00)
- **Purpose:** prove the first half of the Claim on the record. The forecast was right days ahead.
- **Question:** if it was on the map for a week, how much did each office say, and when? (L2)
- **Reveal:** the full countdown, on one weekday clock: SPC Day 8 text the Friday before (3 Dec, no risk area, Finding 1); ECMWF Extreme Forecast Index flagged it at Day 7 (SA p45); Memphis on Monday 3:36 PM, the front "Friday/Saturday" that "could be another severe weather threat", repeated in three later issuances (say where Memphis's area is); WFO Paducah's first partner call that Monday (SA p14); Slight on Wednesday 2:15 AM, about 60 hours before the first reports; Enhanced on Thursday with a 10 % tornado and a hatched area; Moderate on Friday 10:18 AM, 15 % hatched sent twelve minutes early "to get the word out" (SA p7; moved here from the intro in fix round 2, never confused with warning lead time on screen); Tornado Watch 552 at 3:00 PM (first of eleven), 6 h 25 min before Mayfield; Watch 553 at 5:20 PM, about 3 hours before Edwardsville. The twist: Finding 3a, some offices waited until Day 1 or 2 "in part due to established playbooks"; Recommendation 3, say what you know when you know it (SA p15). One named forecaster, sourced [verify: named forecaster and quote].
- **Visual event:** [RS] the countdown clock with each product stamping onto a growing risk map; [RS] Finding 3a as attributed text.
- **Exit hook:** P2 on camera. Then the Memphis line "Friday we should be well into the 70s" back on screen: seventy degrees, in December. `[loop L3 open]`

## A3 · Why December, why so long (about 9:00 to 13:00) · meteorology explainer · CTA hinge inside
- **Purpose:** the explainer layer: why a December night could make violent, long-track tornadoes, and how the long-track storm set out for Mayfield.
- **Question:** how does December, at night, make a tornado that stays down for a hundred sixty-five miles? (L3)
- **Reveal:** warm air advection and the 70s in Memphis ahead of a front (Memphis AFD); a pair of long-track, violent EF4s (SA p12): Bay, Arkansas to Samburg, Tennessee, 80.3 miles at 170 mph, and the Mayfield storm, near Woodland Mills, Tennessee at 8:49 PM to Falls of Rough, Kentucky at 11:47 PM, 165.6 miles, 190 mph, up to 1.13 miles wide, the longest tracked December tornado on record. SPC issued a record 28 mesoscale discussions that evening (SA p12). The mechanism lines are not in the fact sheet: [verify: Gulf moisture plus a strong jet stream in December; why the supercell stayed isolated and kept one tornado down so long; named researcher and institution for the mechanism]. The ruled-out lead stays a fact here, never the headline.
- **Visual event:** [RS] our own NEXRAD Level II replot loop, the hook echo crossing the Tennessee line; NASA MODIS track drawn end to end against a US landmark distance [verify: comparator, e.g. a drive the viewer knows].
- **CTA hinge:** A3-S9 tease (P3), CTA, A3-S10 payoff "The power went out." (see CTA hinge above).
- **Exit hook:** the track crosses into Graves County, and the county's warning goes out at 9:05 PM. `[loop L4 open]`

## A4 · The candle factory (about 13:15 to 17:15)
- **Purpose:** Arc 2, the bigger loss: the same correct forecast, the strongest warning there is, and still no weather-service guidance for a building that big.
- **Question:** the factory had a warning at nine-oh-five; what reached the people inside? (L4)
- **Reveal:** Graves County tornado warning 9:05 PM; the tornado reached Mayfield at about 9:26 PM (NWS Paducah event page), the same minute as the Tornado Emergency for Mayfield, with the county emergency manager called directly (SA p29, p47). The lead is the twenty-one minutes from the 9:05 warning (SA p47: "In the twenty-one minutes between these tornado warnings"), never a lead from the 9:26 Emergency. About 110 people inside (Spectrum News); eight lost their lives (CONFIRMED with attribution: Mayfield Consumer Products and AP, 14 Dec 2021, on a source line; never state 6 or 9, never show the DVIDS caption); the Graves County toll of 24 and 57 on the whole track (NWS Paducah event page). Night shift for seasonal orders [verify: unverified in the fact sheet]. One named person, age, job, sourced quote [verify: none in the fact sheet]. Never the Facebook Live from under the rubble, never chaser or drone aerials. Firing-threat claims only as allegations, attributed: at least five workers told NBC News supervisors warned they would be fired for leaving; the company spokesman called the claims "absolutely untrue". Both sentences together, or neither. Escalation: disturbing, then personal.
- **Visual event:** [RS] P4 on camera; DVIDS/FEMA candle-factory gallery stills (images only); Kentucky Guard and Army Corps Mayfield photos; NWS Paducah survey photos.
- **Exit hook:** then the inspectors came, and they needed a rule to measure a shelter plan against. `[loop L5 open]`

## A5 · What the inspectors could check (about 17:15 to 20:15) · the debunk block
- **Purpose:** the sourced debunk at 60 to 75 %: the belief "there's a federal rule that says a workplace needs a tornado plan". The record says otherwise.
- **Question:** what rule could the inspectors measure a shelter plan against? (L5)
- **Reveal:** "OSHA does not have a standard that requires severe weather emergency plans but recommends them" (OSHA release, 26 Apr 2022). Amazon: Hazard Alert Letter, no citation, no penalty. The candle plant: Kentucky's state OSHA program cited 7 serious violations, $40,000 proposed (exit routes 1, emergency action plans 2, four under the pathogens standard); the company contested all seven; no outcome found through 2026; none of the seven is about a shelter. Say "cited" and "contested", never "fined". The 2019 $9,810 settlement is a separate matter and stays separate, or out. Lawsuits so far: procedural rulings only (Mar 2023; Kentucky Court of Appeals remand, 18 Jun 2026).
- **Visual event:** [RS] the citation list as an on-screen ledger with "contested" stamped on each line; the OSHA sentence as attributed text.
- **Exit hook:** so the people who wrote down what was missing were the forecasters themselves. `[loop E1 still open, paid in Z1]`
- Legal care: no company blamed; the gap is the guidance.

## Z1 · Has anyone written it since (about 20:15 to 23:15) · close
- **Purpose:** answer the dominant question and pay E1 (re-aimed): the Weather Service named the gap and asked for the advice; one state has acted since.
- **Question:** almost five years on, has anyone written the advice those buildings never had? (E1)
- **Reveal:** Finding 6 (p34) in full as attributed text, "a gap" (already heard in H1-S2: here it gets its page and its "multiple offices"). Recommendation 6: develop "materials with basic tornado safety guidelines for large facilities". Never say the review "had no guidance": Finding 6 says "gap", and "no guidance" is the St. Louis office's after-action review. What changed: Illinois Warehouse Tornado Preparedness Act (HB 2987, signed Aug 2025): every warehouse needs a tornado plan, new warehouses a designated refuge area. Kentucky: no law or OSHA rule found [verify: absence]. Whether NWS has published the Recommendation 6 materials [verify: unverified]. Fact plus a dated forward window [verify: an effective date or deadline for the Illinois act].
- **Visual event:** [RS] P5 on camera; Recommendation 6 as attributed text; a map with Illinois lit and Kentucky not.
- **Exit:** the answer in the last 30 to 60 s, then the CTA spine once, then the signature line.
- **Signature line slot:** [signature closing footnote per DESIGN.md, written at the act round]

---

## Calls made (writer)
- Runtime band 21 to 24 min proposed (reason in the header); acts sized to it.
- Fix round 1: hook cut to three short segments; sentence two breaks "Somebody planned for it" with the review's gap, then "The forecast was right", anchored to the Storm Prediction Center (it covered both towns), not Memphis.
- Fix 4: E1 re-aimed to "has anyone written that advice since?"; Finding 6's gap is said in the hook, the St. Louis words in I1-S5, and Z1 pays with Recommendation 6 and the Illinois law.
- Fix round 2: the loss is H1-S2 ("fourteen people lost their lives at two workplaces"), then the gap and "the forecast was right" in H1-S3; the SPC week-ahead line moved to I1-S2 as Q1's payoff, said once. T1 names the two buildings and asks L1 aloud; no toll repeat.
- Factory count resolved as CONFIRMED with attribution (coordinator, fix round 2): 8 per Mayfield Consumer Products (KSL) and AP, 14 Dec 2021, on a source line wherever it is said. No inline marker on it.
- I1-S2 carries the human stake (about a hundred ten at work inside the factory) instead of the outlook timing; "twelve minutes early" moved to the A2 card; "kept getting stronger" left to P2.
- I1-S5 said plainly in the St. Louis office's mouth; the exact words are on the card only. "still" dropped from I1-S3; the cage held for A1.
- One new marker: the football-field comparator in I1-S4 (human scale the grader asked for).
- One clock: weekdays ("a week ahead", "that Friday", "that night"). Year left to the popfig in the hook.
- No state count anywhere; "more than twenty minutes" for Edwardsville everywhere; "no reinforced storm shelter".
- Firing-threat allegations kept out of H1, T1 and I1; they sit in A4 only, attributed, with the denial.
- Hook avoids both rival openings: no cold open on the candle factory as an event (the DVIDS still sits under the review's line), and no "warning is no longer the problem" framing; the gap is the guidance.
- Siren under the hook only; drone bed from T1. Years spoken as words.
- Loop and question tags sit on their own lines after each quote so TTS never voices them; `[verify]` markers sit inline.
- Rationed devices in the open: "If you've lived in western Kentucky, you know" (I1-S3), first person "I went to find out" (I1-S6), "the first thing I looked up" (T1). Three used, the cap for a 20 min script: the acts use none of these three again.

## Self-scores ("a person talking to you", 1 to 10)
- H1: 8. Question, answer, then the loss and the gap in plain words.
- T1: 8. Names the buildings and asks the question in first person.
- I1: 8. S5 now sounds like Paul telling you what the office wrote; S1 still carries a record line.
