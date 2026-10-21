# ep-mayfield-2021 · edit_script.md (TTS segment format)

Lane: documentary (`/storm-episode`).
Status: **H1, T1, I1 LOCKED 22 Oct 26.** Evidence: the owner's devq save `~/.claude/scratch/devq-retention/answers-eps-gates.json` (saved_at "22 Oct 26 02:01:13"): `mayfield_hook` = yes ("Good: lock the hook + intro" on `eps-gates.html#mayfield`), `mayfield_len` = 21-24. The page showed H1 and T1 in full and I1 as an excerpt; every shown line matches this file word for word. Markers resolved by `research/fc-slice-a/b/c.tsv`; grader 8/10 PASS (`research/grade-hook-intro-v3.tsv`). A1 to A5 and Z1: cards, prose in progress. A section goes to TTS only once it locks.

Runtime: **21 to 24 min** (owner, same devq save, `mayfield_len` = 21-24). Reason: an open of about two minutes, five acts of three to four
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
| P2 | A2 exit | "From Wednesday on, the forecast kept getting stronger, and it was right." |
| P3 · cta-hinge tease | A3-S9, right before the CTA | "Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own." (18 words) |
| P4 | A4, the strongest warning there is | "At nine twenty-six, Paducah issued a Tornado Emergency, the Weather Service's highest alert, for Mayfield by name." |
| P5 | Z1, the answer to the dominant question | "Almost five years on, one of the two states makes warehouses plan for tornadoes. From the Weather Service, the advice is still the general kind." |

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
> One of those workplaces was an Amazon delivery station in Edwardsville, Illinois. The other was a candle factory in Mayfield, Kentucky. Both got a tornado warning before the tornado arrived. What happened inside in those minutes is the first thing I looked up.

*[loop L1 open]* *(no void: straight into the intro, the line stays in the hook's scene)*


## I1 · Intro: the whole picture (0:35)

### I1-S1 — narration
**Picture:** NASA MODIS image of the long track, then our own map drawn from SA Appendix C as seventy-one tracks draw in (no state count on screen). Chips "71 tornadoes", "89 lives", then "1953 · 38" beside "2021 · 89". Source line: "NWS Service Assessment, p4: deadliest December tornado event on record since 1950".
> From Friday evening into Saturday, the Weather Service confirmed seventy-one tornadoes, and eighty-nine people lost their lives. Since nineteen fifty, no December tornado outbreak has taken more lives. The old record was thirty-eight lives, in Vicksburg, Mississippi, in nineteen fifty-three. And the people whose job is to see that coming had seen it.

*[Q1 open: what had they seen]*

### I1-S2 — narration
**Picture:** the SPC Day 4-8 outlook archive text, 3:20 AM CST Fri 3 Dec, the Day 8 line lit (one beat only; the countdown is A2's). Then Army Corps or Kentucky Guard photo of the factory site; chip "about 110 inside" (Gov. Beshear and company spokesman, via AP and KSL, Dec 2021).
> A week ahead, the Storm Prediction Center had already named that Friday for severe storms. That night, about a hundred ten people were at work inside the candle factory in Mayfield. The review says a forecast like this one was harder to get across, and it says why.

*[Q1 closes]* *[Q2 open: why it was harder]*

### I1-S3 — narration
**Picture:** NASA VIIRS night-lights over western Kentucky, before and after. Chip "after sunset" (SA p6). Then our own Edwardsville building outline (labelled illustrative) growing to its full size.
> The storms were forecast for after sunset, in December. If you've lived in western Kentucky, you know December is coat weather, not tornado weather. And the building in Edwardsville covered more than a million square feet.

*[Q2 closes]* *[Q3 open: what a building that size is like inside]*

### I1-S4 — narration
**Picture:** the outline fills with football fields laid end to end; chip "6 lives". Then a Mayfield survey photo (NWS Paducah); chip "8 lives" with source line "Mayfield Consumer Products and AP, 14 Dec 2021".
> That's about nineteen football fields under one roof. Six people working there lost their lives. At the candle factory, eight did. Afterward, the weather office in Saint Louis, the one covering Edwardsville, wrote down what had been missing.

*[Q3 closes]* *[Q4 open: what St. Louis wrote]*

### I1-S5 — narration
**Picture:** the WFO St. Louis after-action words as on-screen text, verbatim with the ellipsis marked, attributed "WFO St. Louis after-action review, quoted in the Service Assessment, p33-34". Paul's voice says it plainly; the card carries the exact words.
> That office wrote that there was no advice, from the weather service or from OSHA, on where to shelter people at work. There was nothing on which warnings to shelter for, or on what a big warehouse needs.

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

<!-- draft:A1 start (spliced from drafts/A1.md) -->
## A1 · Edwardsville: more than twenty minutes (about 2:00)

### A1-S1 — narration
**Picture:** out of the blackout, the drawn megaphone from I1-S7 alone, then a drawn cage door swings shut over it with a click [VE]. Cut to the OSHA Hazard Alert Letter to Amazon (dol.gov PDF, US gov work), item 1 lit. Chip "locked in a cage". Source line: "OSHA Hazard Alert Letter, 26 Apr 2022; AP via Claims Journal, 28 Apr 2022".
> It was the device meant to start the shelter plan. OSHA's letter puts it first on the list: locked in a cage and not accessible. I had to read that line twice.

*[L1 payoff begins: the megaphone tease from I1-S7 closes here]* *[RS] cage shuts* *[rationed device: the one aside in this act, "I had to read that line twice"]*

### A1-S2 — narration
**Picture:** NWS St. Louis event page track map (weather.gov/lsx/12_10_2021, E01, SAFE-PD), then our own map: the 8:06 PM warning polygon draws over Madison County, a pin on Edwardsville. Clock chips "5:20 PM watch" (SA p9) and "8:06 PM warning" (SA p28).
> A tornado watch had been up since five twenty PM, about three hours ahead. At eight oh six PM, the weather office in Saint Louis put out a tornado warning that covered part of Madison County, Illinois. Edwardsville sits in Madison County.

*[micro-loop: how long did they have]*

### A1-S3 — narration
**Picture:** [RS] the clock chip runs from 8:06 to 8:27 over our building outline (labelled illustrative) [VE]; chip "more than 20 min" (SA p28, p29).
> The tornado reached the delivery station at about eight twenty-seven, more than twenty minutes later.

*[micro-loop pays: more than twenty minutes; new gap: so where did people go]*

### A1-S4 — narration
**Picture:** a plain card, the WFO St. Louis timeline from SA p26 as attributed text: "staff sheltered 7:45 to 7:53 PM CST". Then our building outline beside a small drawn safe room. Source line "NWS Service Assessment, p26; St. Louis Public Radio, 17 Apr 2022".
> Earlier that evening, at seven forty-five, the staff at that same weather office had gone into their own safe room. They came out at seven fifty-three. The people writing the warning had a safe room. The building in their warning had no storm shelter built to withstand a tornado.

*[connect two points: the office's safe room beside the building; never merged into blame]*

### A1-S5 — narration
**Picture:** [RS] the building outline fills with football fields laid end to end (1.1 million sq ft, about 19 fields of 360 by 160 ft), then a simple drawn panel lies flat and tilts up on a crane. Source line: "St. Louis Public Radio, 26 Aug 2022; Tilt-Up Concrete Association".
> The delivery station covered one point one million square feet. I looked up how a building like that goes up. Its walls were tilt-up concrete: big panels cast flat on the ground, then lifted upright by a crane.

### A1-S6 — narration
**Picture:** two bars fill side by side: "90 mph · city code" (St. Louis Public Radio, 17 Apr 2022) and "150 mph · EF3, estimated" (NWS SA p4, p59) [VE]; then the EF3 track draws across our Edwardsville map and crosses the outline (chip "3.65 mi", SA p59).
> The city's code asked it to stand up to ninety mile an hour winds. This tornado was an EF3, with estimated peak winds of a hundred fifty miles an hour. Ninety against a hundred fifty is the gap those walls faced.

### A1-S7 — narration
**Picture:** our own KLSX Level II replot over Edwardsville, the debris signature blooming at 8:29 PM (SA p28) [VE]. Attributed text chip "WGN Radio / FOX 2 report". The station's audio clip is a licence item and is not mounted; only the reported claim is used.
> At about eight twenty-nine, the Saint Louis weather office saw signs of debris on radar over Edwardsville. WGN Radio and FOX 2 reported that an emergency responder called in a mass casualty incident.

*[micro-loop: who was inside]*

### A1-S8 — narration
**Picture:** dark card, six small marks appear one by one; chips "5 delivery contractors", "1 in-house contractor", "contractors · 4 companies". Source line: "OSHA Chicago release, 26 Apr 2022; House Oversight, 1 Apr 2022". No faces, no names, no company names on screen.
> Six people working at the building lost their lives. Five were delivery contractors, people who deliver packages to doors, maybe to yours. The sixth was an in-house contractor assigned to the building.

*[HUMAN] slot open: the research has no named person with age, job and a sourced quote. Orchestrator call: source one or leave the act without a named person.*

### A1-S9 — narration
**Picture:** our building outline again, a bathroom on the south side, near the loading docks, lit; a second restroom on the north side marked "designated shelter" (OSHA Hazard Alert Letter, items 1 and 2). Source line "OSHA Chicago release and Hazard Alert Letter, 26 Apr 2022".
> Managers had been telling people to get to a restroom. Five of the six who lost their lives were in one, on the south side of the building. OSHA's letter says the designated tornado shelter was the restroom on the north side.

*[loop L1 closes: what happened between the warning and the hit]* *[RS] north and south rooms lit together*

### A1-S10 — narration
**Picture:** a short narrated pull of the damaged building from GMA / ABC News (E12, NEWS-CLAIM-LIKELY, a few seconds, narrated over; never the FOX 2 aerial). Then the OSHA Chicago release (osha.gov) as attributed text; chips "Hazard Alert Letter", "no citation", "no penalty".
> The next April, OSHA sent Amazon what it calls a Hazard Alert Letter. It's a letter asking Amazon to make voluntary changes. No citation, no penalty.

*[real clip moment: the building after the tornado, news pull]*

### A1-S11 — narration
**Picture:** the AP lines as attributed text, "AP, 28 Apr 2022"; OSHA's letter item 3 lit (evacuation maps). Then OSHA's recommendation shown whole: "All audible warning devices, as well as the location of the device(s), should be clearly identified within the severe weather emergency plan and readily accessible." · OSHA hazard alert letter to Amazon, Apr 2022 (candidates/a1 a1-s11_c1). The drawn megaphone returns behind its cage.
> The AP reported the written plan did not specifically identify where the shelter was. OSHA's letter adds that evacuation maps posted at the site showed it. The AP also reported that some workers couldn't remember ever doing a severe weather drill.

### A1-S12 — narration
**Picture:** OSHA's recommendations as attributed text, one line at a time over the drawn megaphone; the cage door swings open on the last line [VE].
> OSHA asked for this. Say where the shelter is, in writing, for this building. Name every warning device in the plan, say where it is, and keep it where people can reach it.

### A1-S13 — narration
**Picture:** (Paul on camera, P1) full frame. Source line under him: "OSHA Chicago release, 26 Apr 2022".
> OSHA said the procedures met minimal federal safety guidelines for storm sheltering.

*[turn: from the building to the forecast]*

### A1-S14 — narration
**Picture:** hard cut from Paul to the SPC Day 4-8 outlook archive text, 3:20 AM CST Fri 3 Dec (spc.noaa.gov archive, SAFE-PD), held one beat; then Finding 3a's page (NWS SA p15) slides in, the words blurred until A2. Then chapter blackout into A2, hand-placed.
> The forecast for that night started long before the warning. The Weather Service's own review looked at offices across the outbreak. Some waited until the last day or two to say how bad it could be. It gives a reason, and I didn't expect it.

*[loop L2 open: how much did each office say, and when; A2 pays with Finding 3a, "established playbooks"]* *(chapter blackout, hand-placed)*
<!-- draft:A1 end -->

<!-- draft:A2 start (spliced from drafts/A2.md) -->
## A2 · The week the forecast held (5:30)

*[loop L2 closes across S1 to S9: how much each office said, and when]* *(one clock for the whole act: a countdown chip, top right, "7 days out", "4 days out", "about 60 hours"... to "Friday night", restamped at every step; product names, percents and issue times stay on screen, never read as a ladder)*

### A2-S1 — narration
**Picture:** from the A1 blackout, the SPC Day 4-8 outlook archive page for Fri 3 Dec, 3:20 AM CST (spc.noaa.gov archive, SAFE-PD), two sentences lit, verbatim: "This moisture return may be accompanied by some potential for severe convection. Regardless, predictability remains very low owing to the uncertainty in the large-scale pattern at this extended time frame." Chip "7 days out". Then the ECMWF Extreme Forecast Index chart as printed in the Service Assessment (Figure 22, p45), one beat, its caption's valid time on screen (00Z Sat Dec 11 to 00Z Sun Dec 12). Source line: "NWS Service Assessment, p7, p45".
> On Friday the third, the Storm Prediction Center's long-range outlook first mentions the chance of severe storms for Friday the tenth. It warns that predictability remains very low. No risk area is drawn, just words. The next day, the European weather model's Day Seven forecast flagged Friday night as far outside normal. It showed very unusual storm fuel and very unusually warm air.

*[Q open: who else saw it]*

### A2-S2 — narration
**Picture:** the IEM archive text of the NWS Memphis Area Forecast Discussion, "336 PM CST Mon Dec 6 2021" (mesonet.agron.iastate.edu, SAFE-PD), scrolling to the paragraph; the severe-weather sentence highlights as it is said, verbatim on screen. Chip "Mon 3:36 PM · 4 days out". A small locator map of the Memphis office's area (55 counties: west TN, northeast AR, north MS, Missouri Bootheel; NWS API offices/MEG).
> By Monday afternoon, the Weather Service office in Memphis has it in writing. That office covers west Tennessee, northeast Arkansas, north Mississippi and the Missouri Bootheel. I read it in the archive. A front would come through Friday or Saturday, and the forecaster wrote, "This looks like it could be another severe weather threat."

### A2-S3 — narration
**Picture:** the same line stamping down the page at each issuance with its time on screen (3:36, 5:46, 9:24, 11:35 PM CST, IEM archive); the last two marked "carried forward". Then the Paducah office pin on the map, Mayfield inside its area (Graves County, NWS API offices/PAH); chip "first conference call · Mon 6 Dec" (SA p14).
> It's a careful sentence, and Memphis kept it on the page. The same words were still there in three later issuances that night. That same Monday, Paducah held its first conference call about the chance of strong to severe storms hitting the same areas again. That's the office that covers Mayfield.

*[Q closes]*

### A2-S4 — narration
**Picture:** [VE] our own countdown map: the first risk area paints in, northern Louisiana up through western Kentucky into southern Indiana, from the SPC Day 3 archive graphic, Wed 8 Dec 2:15 AM CST (spc.noaa.gov, SAFE-PD). Chip "about 60 hours". Pins on Mayfield and Edwardsville stay lit.
> Early Wednesday, the map gets its first color. A risk area runs from northern Louisiana up through western Kentucky and into southern Indiana, about sixty hours before the first storm reports. If you lived in western Kentucky, you were inside the line now, and you stayed inside it through Friday.

*[RS] the map takes its first color* *[micro-loop: how high does it go]*

### A2-S5 — narration
**Picture:** the risk area deepens a shade on the same map (SPC Day 2, Thu 9 Dec 12:58 AM CST); hatching draws in. Chip "10 % tornado · hatched". Then the Paducah Hazardous Weather Outlook phrase verbatim on a clean card, "a couple of long-track supercell tornadoes are also possible", attributed "NWS Paducah Hazardous Weather Outlook, 9 Dec 2021, 2:42 PM CST".
> A day later, they raise it a level. It's a ten percent chance of a tornado within twenty-five miles of any given spot, and a hatched area for strong ones. That afternoon, Paducah's outlook put it this way: a couple of long-track supercell tornadoes are also possible.

*[A3 calls back to the Paducah long-track line]*

### A2-S6 — narration
**Picture:** the SPC Day 1 Moderate Risk graphic from the NWS Paducah event page ("Day 1 Late Morning Outlook.gif", SAFE-PD); chips "Moderate · 4 of 5", "15 % tornado · hatched", "10:18 AM · 12 min early". Then [VE] the NWS Paducah post of 10:19 AM as attributed text, verbatim, full screen ("quoted in the Service Assessment, p20"). Real clip: a Friday-morning local TV weather segment from the Paducah or Nashville market, a short narrated pull [footage gap: not in footage-inventory.tsv, to source; news pull, Content ID expected].
> Then on Friday morning, the Storm Prediction Center goes to a Moderate Risk, level four of five. The forecaster sent it twelve minutes ahead of schedule, in the review's words, "to get the word out." A minute later, Paducah posted, "Think about what you would do now. Better to err on the safe side."

*[RS] the Paducah post, full screen*

### A2-S7 — narration
**Picture:** the Tornado Watch 552 graphic from the NWS Paducah event page ("Tor Watch #1.jpg", SAFE-PD), the box drawing over central Arkansas to southwest Indiana; chip "Watch 552 · 3:00 PM · 1 of 11". Clock runs "about 6 h 25 min" to a Mayfield pin. Then the Watch 553 box from the SPC archive page (spc.noaa.gov/products/watch/2021/ww0553.html) over central Missouri and west-central Illinois; chip "Watch 553 · 5:20 PM", clock "about 3 h" to the Edwardsville pin. Under it, our own NEXRAD Level II replot of the first cells going up (NCEI archive).
> At three that afternoon, the first tornado watch went up, from Arkansas to southwest Indiana. Its text warned of intense tornadoes, and it was the first of eleven. It went out about six hours and twenty-five minutes before the tornado reached Mayfield. At five twenty that evening, a second watch took in Missouri and Illinois, about three hours before Edwardsville was hit.

### A2-S8 — narration
**Picture:** [VE] the countdown map holds, every stamp from the week still on it; then Finding 3a as attributed text, verbatim: "While some offices took a more proactive approach, others waited until Day 1 or 2 to ramp up services in part due to established playbooks." · Service Assessment, Finding 3a, p15. No office named or highlighted on the map.
> But the offices didn't all move at once. The Weather Service's own review found some moved early. Others waited until a day or two out, in part because of what it calls established playbooks. The review doesn't name which offices waited.

*[RS] Finding 3a on screen* *[loop L2 closes]*

### A2-S9 — narration
**Picture:** Recommendation 3 as attributed text: "say what you know when you know it" · Service Assessment, Recommendation 3, p15. Then back to the Memphis and Paducah stamps on the countdown map, Monday highlighted.
> The review asked for one thing: say what you know when you know it. Memphis said what it knew on Monday, and Paducah held its first conference call that same day.

### A2-S10 — narration
**Picture:** (Paul on camera, P2) full frame, about 4 s. Bed drops under him.
> From Wednesday on, the forecast kept getting stronger, and it was right.

### A2-S11 — narration
**Picture:** the Memphis discussion back on screen, the Friday sentence lit, verbatim: "Friday we should be well into the 70s" · NWS Memphis, 6 Dec 2021, 3:36 PM CST. Chip "70s °F · forecast for Fri 10 Dec". Then a slow push on a NASA MODIS still of the region; chapter blackout into A3 (hand-placed).
> Go back to that Monday discussion from Memphis. Before the front and before any storm, it said Friday should be "well into the seventies." How does seventy-degree air, on a December night, turn into a tornado that stays down for more than a hundred sixty-five miles? The answer starts with that warm air.

*[loop L3 open]* *(chapter-exit question plus its one affirming line; chapter blackout, hand-placed)*
<!-- draft:A2 end -->

<!-- draft:A3 start (spliced from drafts/A3.md) -->
## A3 · Why December, why so long (about 9:00)

### A3-S1 — narration
**Picture:** straight from the A2 exit into a two-part explainer card (our own MG): "fuel" (warm, wet air low) and "twist" (wind turning with height). Source line: "NOAA Storm Prediction Center, Tornado FAQ; NWS".
> A tornado like this one needs several things to line up, and two of them matter most here. One is warm, wet air near the ground to feed it. The other is wind that changes speed and direction as you go up, to spin it.

*[loop L3 carried from the A2 exit]* *[Q open: why December had both]*

### A3-S2 — narration
**Picture:** the explainer card: "twist" fills first (a winter jet stream band across the map, source line "NOAA JetStream"), "fuel" stays empty. Lower third: "Victor Gensini · Northern Illinois University". Optional on-screen quote, verbatim with the source's doubled word kept or marked: "It was really a late spring type of setup in in the middle of December." · Victor Gensini to the Associated Press, 12 Dec 2021.
> In December, the twist is usually there. Winter has the biggest temperature contrast, and the jet stream runs strongest then. Victor Gensini, a meteorologist at Northern Illinois University, told the Associated Press the same thing: winter usually brings plenty of twist, but little of the fuel.

*[Q stays open: so where did the fuel come from]*

### A3-S3 — narration
**Picture:** the "fuel" half of the card fills, warm colour flooding north across the South. Chip "after sunset" (SA p6, no clock time). Then the Louisville words as attributed on-screen text, verbatim: "SIGNIFICANT NIGHTTIME SEVERE WEATHER EVENT EXPECTED LATE FRIDAY NIGHT INTO THE EARLY MORNING HOURS OF SATURDAY" · NWS Louisville Area Forecast Discussion, 3:30 AM EST Thu 9 Dec 2021 (IEM archive). Chip "Thursday · early morning".
> That Friday, the fuel showed up too. Gensini told NBC News the heat and humidity across the South was pretty uncharacteristic for this time of year. And much of the severe weather was forecast for after sunset, on some of the shortest days of the year. By Thursday morning, the Louisville office was already calling it a significant nighttime severe weather event.

*[Q closes: fuel and twist together, after dark]* *[Q open: who would be out in it]*

### A3-S4 — narration
**Picture:** NASA VIIRS night-lights over western Kentucky (the I1 asset, the "before" frame only); SA p6 as attributed on-screen text, verbatim: "a time of year when many in the public, and even our partners, do not normally associate with a threat for tornadic activity" · NWS Service Assessment, p6. Then two pins light on the dark map, Edwardsville and Mayfield.
> That's the part that matters for this story. The review says many people, and even the Weather Service's own partners, don't connect December with tornadoes. A December storm after dark finds people who aren't watching for one. And that Friday night, people were still at work, in Edwardsville and in Mayfield.

*[HUMAN: the stake, the two workplaces on the map]* *[Q open: did anyone say how bad]*

### A3-S5 — narration
**Picture:** the Paducah outlook as attributed on-screen text, verbatim: "but a couple of long-track supercell tornadoes are also possible." · NWS Paducah Hazardous Weather Outlook, 2:42 PM CST Thu 9 Dec 2021. Chip "Thursday · 2:42 PM". Short hold (A2 already showed this product: callback only).
> Remember Paducah's outlook from Thursday afternoon. Its main worry was damaging winds and isolated tornadoes, possibly a couple of strong ones. It also said a couple of long-track supercell tornadoes were possible. That was more than a day before the first one touched down.

*[callback to A2's Paducah line, not a repeat of its reveal]* *[Q closes]*

### A3-S6 — narration
**Picture:** [VE] our own NEXRAD Level II replot (KNQA, footage F11), the hook echo moving from northeast Arkansas through the Missouri Bootheel into Tennessee; the Bay to Samburg track draws in red. Chip "EF4" only. At "eight forty-nine" a second pin drops near Woodland Mills, Tennessee. Do not draw the 13 minutes between the tracks as empty: three brief, weak tornadoes sit in it (NWS Memphis survey). Source line: "NWS Memphis and Paducah damage surveys; SA p3, p12, p59".
> That's what came. The review calls it a pair of long-track, violent EF4 tornadoes, from the same storm. The first ran from Bay, Arkansas, to Samburg, Tennessee. At eight forty-nine, the second one touched down near Woodland Mills, Tennessee.

*[RS] the second pin drops on the replot* *[Q open: where the second one went]*
*Note: "from the same storm" rests on NWS Memphis ("the long-track supercell storm that moved from western Poinsett County AR, to Obion County TN, and into Kentucky") and SA p30 ("the main supercell storm"), per fc-A3. No NWS sentence says both EF4s in one line; the fact-checker CONFIRMED it with that caveat.*

### A3-S7 — narration
**Picture:** [VE] our own line traces the track end to end, Woodland Mills 8:49 PM to Falls of Rough 11:47 PM; NASA MODIS Aqua natural-colour image, 12 Dec (footage T04, credit NASA Earth Observatory) for the western Kentucky stretch only, as NASA's caption says. Chip "165.6 mi" only. Then a pin on the candle factory in Mayfield, on the line. Source line: "NWS Service Assessment, p3, p4, p59; NWS Paducah event page (width)".
> It stayed down for a hundred sixty-five point six miles, the longest tracked December tornado on record. That's a little shorter than the drive from Nashville to Louisville. And Mayfield sat right on that line. That Friday night, the candle factory there had people working inside.

*[RS] the factory pin lands on the track* *[loop L3 closes: December fuel plus twist, after dark, and the one long track]*

### A3-S8 — narration
**Picture:** the SPC mesoscale discussion archive page for 10 Dec 2021 (SPC/IEM archive, SAFE-PD), evening-shift entries only; a counter ticks to 28 beside a ghost bar at 20. Source line: "NWS Service Assessment, p12". Optional chip "about one every 17 minutes" (derived: 480 minutes over 28).
> While it ran, the Storm Prediction Center never went quiet. Its forecasters put out twenty-eight mesoscale discussions in one eight-hour evening shift. The old record was twenty. Each one is a short note on what the storms are doing now and what to expect over the next few hours.

*[RS] the counter passes the old record*

### A3-S9 — narration
**Picture:** (Paul on camera, P3) full frame, the cta-hinge tease. Nothing added to fill his clip.
> Right as the storm reached Mayfield, the weather office watching it ran into a problem of its own.

*[loop cta-hinge open]* *(18 words, at most 25. The CTA mounts after this segment: `config.yaml channel.cta`, own VO.)*

### A3-S10 — narration
**Picture:** hard cut from the CTA to black, then SA p30 as attributed on-screen text, verbatim: "At approximately 9:25 P.M. CST, commercial power was lost at WFO Paducah and the backup generator failed." Then the NWS Paducah KPAH radar still as the tornado crossed Mayfield (footage F10, about 9:27 PM, SAFE-PD). Clock chips "about 9:25 PM · power out", "9:52 PM · Springfield, Mo.".
> The power went out. At about nine twenty-five, the Paducah office lost commercial power, and its backup generator failed. Its warnings still went out. Louisville was asked to take over first, but it couldn't get extra staff in quickly enough. At nine fifty-two, the office in Springfield, Missouri, took over Paducah's work.

*[loop cta-hinge closes: first sentence]* *(the 9:26 Tornado Emergency is left to A4 and P4)*

### A3-S11 — narration
**Picture:** rewind effect on our own track map back to 9:05 PM; the Graves County tornado warning polygon (SA p29) lights, the tornado marker in Fulton and Hickman counties, never drawn at the Graves County line and never captioned "entering Graves County" (fc-A3: Cayce 9:01 PM, Hickman County 9:06 PM, Mayfield 9:26 PM). Pin on the candle factory; chip "about 110 inside" (Gov. Beshear and company spokesman, via AP and KSL, Dec 2021). Chapter blackout into A4, hand-placed.
> Nine oh five, twenty-one minutes earlier. Paducah had warned Graves County about a tornado already on the ground. At that minute, the tornado was still crossing Fulton and Hickman counties, to the southwest. The company says about a hundred ten people were inside the candle factory that night. What reached them?

*[loop L4 open]* *(chapter-exit question; no affirming line)* *(chapter blackout, hand-placed)*
<!-- draft:A3 end -->

<!-- draft:A4 start (spliced from drafts/A4.md) -->
## A4 · The candle factory (about 13:15)

### A4-S1 — narration
**Picture:** NWS Paducah "Tornado Warning Dec 10 Timeline" graphic (footage-inventory F09, SAFE-PD), the Graves County polygon lit; clock chip "9:05 PM". Source line: "NWS Service Assessment, p29 and p47".
> That nine oh five warning wasn't the first word Mayfield got that day.

*[loop L4 carried in from A3-S11, which already gives the 9:05 warning and "near Mayfield around nine thirty"]*

### A4-S2 — narration
**Picture:** the SPC Tornado Watch 552 graphic from the NWS Paducah event page (F08, SAFE-PD), Mayfield pinned inside it; chip "Watch since 3:00 PM". Source line: "Service Assessment, p9; p14 (first Paducah conference call, Mon 6 Dec)".
> By then, Mayfield had been inside a tornado watch since three that afternoon. By the review's count, that was six hours and twenty-five minutes ahead of the tornado. That watch talked about intense tornadoes. The Paducah office had held its first conference call about this storm back on Monday. Now the warning put a clock on it.

### A4-S3 — narration
**Picture:** USACE Louisville District video of the factory site by day (T10, DVIDS public domain), slow. Name chip "Mark Saxton · 37 · forklift operator", source line "NBC News, 12 Dec 2021". His words as on-screen text, verbatim: "I can't believe I'm even here." · Mark Saxton, NBC News. Never on the same card or cut as A4-S10.
> One of the people on that Friday night shift was thirty-seven-year-old Mark Saxton, a forklift operator at the candle factory. He'd come in thirty minutes early, the way he always did. He survived. Afterward, he told NBC News, "I can't believe I'm even here."

*[HUMAN] (Saxton's own published words only; never tied to the A4-S10 allegation)*

### A4-S4 — narration
**Picture:** the Service Assessment pages (A01, SAFE-PD), never its cover image, which carries a FOX 2 aerial; our own MG: a search of the review's text types "candle" and returns "0 results". Chips "75 pages", "Mayfield: 17 mentions" (fc-A4 text search).
> I wanted to know what reached the people on that floor in those minutes. So I searched the Weather Service's own review of that night. It runs seventy-five pages. It never mentions the candle factory. Not once. The word Mayfield shows up seventeen times.

*[RS] [VE] the search returning zero (if challenged: the text of the review, all 75 pages)*

### A4-S5 — narration
**Picture:** our own clock MG over a Graves County map: a bar fills from "9:05 PM warning" to "9:26 PM"; chip "21 minutes". On-screen quote, verbatim: "In the twenty-one minutes between these tornado warnings" · Service Assessment, p47. Then chips "outbreak average lead: 19 min" and "Paducah: 25 warnings, 20 min average" (SA p32).
> The review does keep the clock. The warning had said nine thirty, and the tornado came at about nine twenty-six. That's about twenty-one minutes from the warning to the tornado in town. Across the outbreak, the average lead time on a tornado warning was about nineteen minutes. Paducah's twenty-five warnings averaged about twenty. Mayfield's twenty-one minutes ran close to both.

### A4-S6 — narration
**Picture:** (Paul on camera, P4), full frame. Chip "TORNADO EMERGENCY · 9:26 PM" lands on "Tornado Emergency".
> At nine twenty-six, Paducah issued a Tornado Emergency, the Weather Service's highest alert, for Mayfield by name.

*[RS] [VE] P4 on camera*

### A4-S7 — narration
**Picture:** NWS Paducah radar still "927pm_Mayfield_KPAH.png" (F10, SAFE-PD), the storm over town; chip "8 Tornado Emergencies that night" (SA p46). Then the review's line as attributed text: "The outlooks, forecasts and warnings issued for this historic event ... were excellent." · Service Assessment, p4.
> Paducah contacted the Graves County emergency manager directly. That night, offices issued eight Tornado Emergencies in all. Later, the Weather Service's own review called the outlooks, forecasts and warnings for this outbreak excellent.

### A4-S8 — narration
**Picture:** real clip: CBS News "rescue efforts continue at Kentucky candle factory" (M06), a short pull narrated over, never its own audio bed (Content ID likely; if claimed, a FEMA / DVIDS factory gallery still, M02, image only, carries the line). Chip "8 lives", source line "Mayfield Consumer Products (KSL) and AP, 14 Dec 2021".
> Through that weekend, rescue crews worked through the wreckage of the factory, looking for anyone still alive. Eight of the people inside did not survive. The company's spokesman said the count would stand at eight.

### A4-S9 — narration
**Picture:** NWS Paducah Graves County survey photos (T01) and a FEMA Mayfield still; never the Guard video DVIDS 825642 here, which was filmed in Dawson Springs and would sit under Graves County chips. Chips "24 · Graves County", "57 · one tornado", "500+ hurt" (NWS Paducah event page); "most in the Paducah office's history" (Service Assessment, p30).
> Across Graves County, twenty-four people lost their lives. Along the whole track of that one tornado, the toll reached fifty-seven, and more than five hundred were hurt. The Weather Service's review says it was the most lives lost in the Paducah office's history.

### A4-S10 — narration
**Picture:** two attributed text cards, same size, one cut, no worker names or faces (Saxton never here). Card one, verbatim: "at least five workers said supervisors warned employees that they would be fired if they left their shifts early" · NBC News, 13 Dec 2021. Card two, verbatim: "It's absolutely untrue." and "Employees can leave any time they want to leave and they can come back the next day." · Bob Ferguson, company spokesman, NBC News, 13 Dec 2021.
> At least five workers told NBC News that supervisors had warned employees they would be fired if they left their shifts early. The company's spokesman, Bob Ferguson, told NBC, "It's absolutely untrue." He said employees can leave any time they want and come back the next day.

*(legal: allegation and denial in the same segment and the same cut; never split them)*

### A4-S11 — narration
**Picture:** FEMA / DVIDS candle-factory gallery still, image 10 of 25 (dvidshub.net/image/7018055, image only, never its caption), slow push. Chip "rulings so far: not on the facts".
> Those claims are now lawsuits. So far, the courts have ruled only on which claims can go forward, never on what happened that night. I'm not going to settle that for them. What I can show you is what one weather office wrote down afterward.

*(legal: never say which side a ruling favoured)*

### A4-S12 — narration
**Picture:** the WFO St. Louis after-action words as attributed text, verbatim with the ellipsis marked: "(no official NWS/Occupational Safety & Health Administration (OSHA) recommendations for severe weather sheltering guidelines in the workplace ..." and "The NWS has very little outreach material to aid private companies in developing their severe weather plans" · WFO St. Louis after-action review, quoted in the Service Assessment, p33-34 (callback to I1-S5, `data-callback` reason: the answer to L4), over an NWS Paducah Mayfield survey photo (T01).
> The Saint Louis office wrote that there were no official Weather Service or OSHA recommendations for sheltering at work. It added that the Weather Service had very little outreach material to help private companies make severe weather plans. That office covers Edwardsville, not Mayfield, and it was writing about big warehouses.

*(legal: the office's words, attributed in the sentence; never the narrator's fact, never Finding 6)*

### A4-S13 — narration
**Picture:** three stamps drop onto one Mayfield timeline, our own MG: "WATCH 3:00 PM", "WARNING 9:05 PM", "EMERGENCY 9:26 PM". Under them, verbatim: "no guidance on what types of warnings to shelter for" · WFO St. Louis after-action review, quoted in the Service Assessment, p34.
> And that office wrote that there was no guidance on what types of warnings to shelter for. That Friday, Mayfield got a watch at three, a warning at nine oh five and an Emergency at nine twenty-six.

*[loop L4 closes] (what reached the town: a watch, a warning about twenty-one minutes ahead, then the Emergency as it hit; what one office found missing: official workplace sheltering recommendations and guidance on which warnings to shelter for)*

### A4-S14 — narration
**Picture:** FEMA / DVIDS candle-factory still (M01, dvidshub.net/image/7018049, image only, never its caption), slow push; chip "Kentucky workplace safety agency", source line "AP, 14 Dec 2021". Chapter blackout, hand-placed.
> Four days after the storm, Kentucky's workplace safety agency, part of the state Labor Cabinet, said it would look into what happened at the factory. Then the inspectors came. What could they measure a shelter plan against?

*[loop L5 open]* *(chapter-exit question; no affirming line; does not say whether a rule existed, A5 answers)* *(chapter blackout into A5)*
<!-- draft:A4 end -->

<!-- draft:A5 start (spliced from drafts/A5.md) -->
## A5 · What the inspectors could check (17:15)

### A5-S1 — narration
**Picture:** opens on our own graphic, no DVIDS still (A4 ends on 7018049): a plain clipboard icon drawn over a blank federal rulebook page, chip "the inspectors". The page stays blank as the line runs.
> When the inspectors came, you'd figure they carried a rulebook. You'd figure there's a federal rule that says a workplace this big needs a tornado plan, and somebody checks it. I figured that too, until I read what OSHA put out in April twenty twenty two.

*[loop L5 carried from A4: what rule could they measure a plan against]*
*[device: none; first person is register]*

### A5-S2 — narration
**Picture:** the OSHA sentence as attributed on-screen text, verbatim: "OSHA does not have a standard that requires severe weather emergency plans but recommends them" · OSHA news release, Chicago region, 26 Apr 2022. The word "recommends" lifts and turns amber. Then, beside it and kept separate, the St. Louis words as their own card, verbatim: "The NWS has very little outreach material to aid private companies in developing their severe weather plans" · WFO St. Louis after-action review, quoted in the NWS Service Assessment, p33-34.
> In OSHA's own words, "OSHA does not have a standard that requires severe weather emergency plans but recommends them." Recommends, not requires. The weather office in Saint Louis wrote about a related gap afterward: it said the Weather Service has "very little outreach material to aid private companies in developing their severe weather plans."

*[RS] [VE] the OSHA sentence on screen, "recommends" lit; the St. Louis card sits beside it, never merged*
*[loop L5 closes]*

### A5-S3 — narration
**Picture:** the General Duty Clause words as attributed on-screen text, verbatim: "a place of employment free from known hazards" · OSHA news release, 26 Apr 2022. Behind it, our own blank page titled "Tornado plan standard", empty.
> What the release does cite is one broad rule, the General Duty Clause. The release describes it as requiring employers to provide "a place of employment free from known hazards." The law itself says "recognized hazards." Neither wording says anything about where to shelter a building full of people in a storm.

*[Q open: so what did each building get]*

### A5-S4 — narration
**Picture:** NOAA Damage Assessment Toolkit viewer, Edwardsville EF3 survey points (apps.dat.noaa.gov, screen-recorded, US gov; check the points carry no third-party photos), then our Edwardsville building outline. The quote as a chip: "met minimal federal safety guidelines for storm sheltering". Source line: "OSHA news release, Chicago region, 26 Apr 2022".
> At Edwardsville, the same release said Amazon's procedures "met minimal federal safety guidelines for storm sheltering." The minimum was a recommendation.

*[Q closes]* *[Q open: what Kentucky did at the candle plant]*
*[note: the Hazard Alert Letter, its terms and the site-specific advice live in A1; not restated here]*

### A5-S5 — narration
**Picture:** a USACE Louisville District video item from the Kentucky tornado response gallery (dvidshub.net/mediagallery/detail/id/262927), Mayfield debris work, narrated over, natural sound low. No credit, unit or date on screen until the item page is opened and its public-domain credit confirmed. Map chip: Kentucky outlined, "state-run OSHA program".
> The candle factory in Mayfield went a different way, because Kentucky runs its own OSHA program, through a state agency. In twenty twenty two, the state program cited the plant for seven violations, with forty thousand dollars in proposed penalties. The AP called all seven serious.

*[real clip moment: USACE video, Mayfield; footage credit to confirm per item before locking]*

### A5-S6 — narration
**Picture:** the citation list as an on-screen ledger, one line at a time: "Exit routes · 1", "Emergency action plans · 2", "Pathogens standard · 4". Source line: "OSHA citations, 2022, as reported by Hop Town Chronicle and AP". A blank fourth line reads "Storm shelter · 0".
> One of the seven was about exit routes. Two were about emergency action plans. Four came under the pathogens standard. Not one of the seven is about a storm shelter. So a plan could still be cited. No OSHA standard required a tornado shelter.

*[RS] [VE] the ledger builds; the "Storm shelter · 0" line lands on "Not one"*
*[note: the pathogens standard keeps its short name in voice and on screen; its full name carries a hard flag word]*

### A5-S7 — narration
**Picture:** "CONTESTED" stamps onto each of the seven ledger lines in turn. Then the FEMA Mayfield courthouse still (candidates/a5 S7_c3), wide; no second candle-factory frame exists and 7018049 stays A4's.
> The company contested all seven. A citation is the state's allegation, and a contested one isn't settled. At the time, the case was open, and the violations could still be changed, removed or added. I looked for how it ended, and in everything I read through twenty twenty six, I couldn't find a final outcome.

*[VE] "contested" stamped on each line*
*[Q open: did the courts decide anything]*

### A5-S8 — narration
**Picture:** a Kentucky National Guard video of debris clearing (DVIDS 825642, 36 to 58 s), narrated over. It was filmed in Dawson Springs, not Mayfield: no place name on screen. No unit, credit or date on screen until the page is read and its public-domain status confirmed. Date chips "Mar 2023 · federal court" and "Jun 18, 2026 · Ky. Court of Appeals"; the claims are not named on screen.
> Former workers have sued the company. So far, the rulings are about procedure. A federal judge sorted out which claims could go ahead in March twenty twenty three. Then in June twenty twenty six, Kentucky's Court of Appeals sent one case back for trial. For the workers who sued, there's still no ruling on the night itself.

*[Q closes]* *[real clip moment: Kentucky Guard video; footage status to confirm before locking]*
*[HUMAN: the workers who sued, unnamed by choice; no supervisor named, no allegation content]*

### A5-S9 — narration
**Picture:** the Service Assessment title as our own text card (title, office names, date from the cover); never the cover image, which carries a FOX 2 aerial. Slow push, then chapter blackout, hand-placed, into Z1.
> The weather service wrote that gap down itself, in its own review of that night. What I wanted to know next was whether anyone has filled it since.

*[loop E1 still open, paid in Z1]* *(chapter blackout, hand-placed)*
<!-- draft:A5 end -->

<!-- draft:Z1 start (spliced from drafts/Z1.md) -->
## Z1 · Has anyone written it since (20:15)

### Z1-S1 — narration
**Picture:** hard cut out of the A5 blackout to the Service Assessment PDF, page thirty-three, the first sentence of the "common theme" passage lit, attributed "NWS Service Assessment, p33" (the second sentence, which carries a flag word, stays off screen). Then NWS St. Louis survey stills from Edwardsville (weather.gov/lsx/12_10_2021, SAFE-PD E03; they show the town, never claimed as the building), slow push.
> When the Weather Service wrote up its review of that night, the same worry came up from more than one office. The review calls it a common theme.

*[loop E1 paying]* *(pays A5's exit: the people who wrote down what was missing were the forecasters themselves)*

### Z1-S2 — narration
**Picture:** Finding 6 as attributed text on a clean card, verbatim: "Multiple offices identified a gap in NWS safety outreach and resources related to buildings with large footprints, such as warehouses." · Service Assessment, Finding 6, p34. The words "a gap" stamp on as they are said.
> On page thirty-four it becomes Finding six, and I'll read it to you word for word. Multiple offices identified a gap in NWS safety outreach and resources related to buildings with large footprints, such as warehouses.

*[RS]* *[VE: "a gap" stamps onto the Finding 6 card, the same words the hook said, now with their page]*

### Z1-S3 — narration
**Picture:** Recommendation 6 slides in under Finding 6, the whole sentence verbatim, attributed "Service Assessment, Recommendation 6, p34". Then a real clip to break the run of cards: USACE Louisville District, "Louisville District continues Mayfield, Kentucky debris removal" (DVIDS 827619, gallery 262927, SAFE-PD T10; open the item page and read its date and credit before wiring), narrated over.
> Right under it sits Recommendation six. It asks the Weather Service to work with experts and develop materials with basic tornado safety guidelines for large facilities. That's the advice the Saint Louis office said was missing.

### Z1-S4 — narration
**Picture:** a US map, Illinois lighting up; chips "Warehouse Tornado Preparedness Act · HB 2987" and "Workplace tornado law" on Illinois. Source line: "Illinois Public Act 104-0262; St. Louis Public Radio, 22 Aug 2025".
> Then I checked what has changed since. In Illinois, the law changed. In August twenty twenty five, the governor signed the Warehouse Tornado Preparedness Act. Every warehouse operator in the state now has to write a tornado safety plan. And new warehouses have to be designed with tornadoes in mind. People inside must be as protected from a tornado as from the other extreme events the building code already covers.

*[RS]* *[VE: Illinois lights up on the map, labelled "Workplace tornado law"]* *[HUMAN: the bill followed Edwardsville, the six from A1]*

### Z1-S5 — narration
**Picture:** NWS St. Louis Edwardsville track map (weather.gov/lsx/12_10_2021, SAFE-PD E01), the EF3 line across Madison County; chip "in effect since Aug 15, 2025". Source line: "Illinois Public Act 104-0262; St. Louis Public Radio, 22 Aug 2025".
> That bill followed the Edwardsville tornado and the six people who lost their lives at the delivery station. The plan rule took effect the day it became law. Existing warehouses had one hundred twenty days to file theirs with the local fire department.

### Z1-S6 — narration
**Picture:** the map pans south; Kentucky stays unlit, Illinois keeps its "Workplace tornado law" label. Source line under the Kentucky beat: "8 at the factory: Mayfield Consumer Products and AP, 14 Dec 2021". Then the weather.gov tornado safety page (weather.gov/safety/tornado-during, Q2-02), the "large open rooms" line lit.
> In Kentucky, where eight people lost their lives at the factory, I couldn't find a new law on tornado plans at work. There's no new OSHA rule on it that I could see either. A national set of tornado safety guidelines for large facilities, the thing Recommendation six asked for, I couldn't find. The Weather Service's general safety page does say to stay out of large open rooms, like cafeterias and gyms.

*[RS]* *[VE: the map holds, Illinois lit with its workplace-law label and Kentucky dark]*

### Z1-S7 — narration
**Picture:** (Paul on camera, P5) full frame, the answer to the dominant question. P5 wording: "Almost five years on, one of the two states makes warehouses plan for tornadoes. From the Weather Service, the advice is still the general kind." (24 words). Lower chip under him: "Illinois: workplace tornado law · Recommendation 6 materials: not found".
> Almost five years on, one of the two states makes warehouses plan for tornadoes. From the Weather Service, the advice is still the general kind.

*[loop E1 closes]* *("Almost five years" holds until 10 Dec 2026; if the episode publishes after that, say "Five years on".)*

### Z1-S8 — picture only (narration cut, P5 carries the answer)
**Picture:** back to the Mayfield survey photo from I1-S6 (NWS Paducah, SAFE-PD T01), the same frame, now in daylight colour, about two seconds under the bed; chip "1 of 2 states: a workplace tornado law".

### Z1-S9 — narration
**Picture:** [source: shelter sign / floor map, stock]: a worker reading a posted floor map, then a hallway with a tornado shelter sign, warm and calm, daylight. Close bed rises gently.
> There's one thing you can do this week, wherever you work. Ask where your building's tornado shelter is. Ask who sounds the alarm, and how you'd hear it on the far side of the floor. Then walk there once, on a calm day, so your feet know the way.

### Z1-S10 — end ask (no narration)
**Picture:** the two `config.yaml channel.end_ask` clips, back to back, full frame, with their own voice (DESIGN.md "End ask"). Narration and the circle off; the close bed runs on under them. First clip starts inside the last thirty seconds.

### Z1-S11 — narration
**Picture:** the close card, channel logo; Paul's signature line over it (DESIGN.md "Signature closing footnote").
> Tornadoes don't ask permission. But they do send warnings. Learn where you'd go when yours sounds, at home and at work, so when it comes, you already know what to do. This was The Warning Hour.
<!-- draft:Z1 end -->

---

## Chapter cards (planning record; the narration above supersedes them)

Stakes order, not chronology. Each act changes what the viewer understood. Every act serves the Claim.

## A1 · Edwardsville: more than twenty minutes (about 2:00 to 5:30)
- **Purpose:** the first workplace. Show what a correct, on-time warning met inside a building with no reinforced storm shelter and no weather-service guidance for its size.
- **Question:** what happened between the 8:06 PM warning and the hit at about 8:27 PM? (L1, carried from T1 and I1-S7)
- **Reveal:** the building was 1.1 million square feet with tilt-up walls and no reinforced storm shelter; workers were sent to a designated interior area (a south-side bathroom, per OSHA); codes did not require a shelter; city code asked for 90 mph wind resistance, and this was a 150 mph EF3 (SA p59; St. Louis Public Radio). OSHA sent a Hazard Alert Letter with no citation and no penalty, and said the procedures "met minimal federal safety guidelines for storm sheltering". OSHA's letter lists the megaphone first (locked in a cage); reported details (AP via Claims Journal): the written plan did not name a shelter location, some workers could not recall drills. The six were contractors working at the building (five delivery drivers, one building-services worker). WFO St. Louis staff had sheltered themselves at 7:45 to 7:53 PM. One named person, age, job, sourced quote [verify: none in the fact sheet]. Escalation: interesting, then surprising.
- **Visual event:** [RS] the building outline scaled against football fields as the 90 mph and 150 mph bars fill side by side (1.1 million sq ft = about 19 fields of 360 by 160 ft, end zones included); the 8:06 to 8:27 clock running out over the outline.
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
