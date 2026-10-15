# ep-joplin-2011 · edit_script.md (draft 1, 15 Oct 26: H1, T1 and I1 in full prose; acts A1 to A6 and the close Z1 in full prose from draft 8)

Lane: documentary (`/storm-episode`). Built on the angle the owner locked on 15 Oct 26 (`angle.md`) and on `structure.md`. Facts from `research/facts.md` (row ids on every `Rows:` line); viewer comments from `research/comments-for-writer.md`. Status: DRAFT. The owner reads H1, T1 and I1 on the review page while the fact-checkers resolve the `[verify]` tags.

## A. Header
- **Title (owner, verbatim):** Joplin 2011: The Sirens Did Not Lie
- **Target runtime:** planned at 22:00 (`structure.md`; the owner has not set it) until `word_budget.py` sizes it from a probe at the shipping tempo.
- **Claim (locked, copied):** In Joplin the tornado found people indoors, in buildings with nothing below them: 135 of the 155 who lost their lives to its impact were inside a structure, and not one person the investigators could place was below ground. The town believed its sirens went off all the time; the records say about once a year.
- **Dominant question:** the viewer keeps watching to find out why the people of Joplin, most of them indoors and many doing what they were told, had nothing below them, and how a town whose sirens sounded about once a year came to hear them as noise.
- **Architecture:** detective, with a countdown inside it. NIST's investigators are the detectives; one master map of Joplin is the case board, walked location by location. Act 2 runs as a countdown from five oh nine to five thirty eight.
- **Scope held in every act (which count means what):**
  - 161: all deaths, NIST's total from the Missouri State Police list (T1). Said as "a hundred sixty-one lives"; the base goes on the source line.
  - 155: impact-related deaths, NIST Finding 29 (T2). The only base of the 135 and of "87 percent".
  - 154: NIST Table 4-3, every impact-related death placed by location except the one tied to the Golden Corral (T9, T12). The counter card is summed from this table; its inside count is 135, the same as Finding 40's.
  - 158: the Weather Service's headline count of direct deaths (T26). Said only with "the Weather Service".
  - 83.8 percent goes only with "of all 161" (on screen).
  - "Once a year": siren soundings outside the weekly one-minute Monday test, since 2007 (S2, S5). "Fourteen of eighteen": tornado warnings, 2005 to 2011 (S10). Two different sets, never merged into one figure.
  - Below ground: "not one person the investigators could place" or "no evidence", never "nobody". Twelve people in the Macadoodles wine cellar were below ground and all survived (B33 to B35, B49), so the zero is about those the tornado took.
  - Sirens: twenty five, NIST's count (S2). "The sirens did not lie" is the record's side, never a verdict that the sirens were not the problem: the Weather Service found the first siren had lost credibility (S19).

## Section ID map
`tts_episode.parse_segments` IDs must match `[A-Z]\d+-S\d+`.
| Section | ID prefix |
|---|---|
| Hook (Paul on camera) | H1 |
| Hook tail | T1 |
| Intro: the day, the place, the two numbers | I1 |
| Act 1, sirens: belief against record | A1 |
| Act 2, the evening, five oh nine to five thirty eight | A2 |
| Act 3, homes with nothing underneath (book ad inside) | A3 |
| Act 4, stores, churches, restaurants | A4 |
| Act 5, St. John's, Greenbriar and the age gap | A5 |
| Act 6, what changed and what did not | A6 |
| Book ad | (none: the `config.yaml channel.cta` file carries its own voice) |
| Close | Z1 |

## Writer notes
- The blockquote is the spoken line and nothing else. Row tags sit on the `Rows:` line under each segment.
- **The hook's sound:** the channel's civil-defense siren (`soundreality-civil-defense-siren-128262.mp3`), low and distant under Paul from 0:00 and cut dead on his last word, because the film is about whether that one sound was believed; it is the only sound that belongs in frame one, and no archive or broadcast audio plays in the hook.
- Pictures: NIST's own ground photographs (never the GeoEye or Pictometry aerials marked "Used with permission"), the NOAA radar image, our own maps, timelines and counters, public domain FEMA and NOAA material. News pulls only as inserts inside acts, never in the hook. Storm-chaser footage never: the opening comment sits under a chase video, so the comment appears as a card only, never with a frame of that video.
- A comment appears as an on-screen card with its likes and the video it sits under, verbatim, inside the acts only: never in the hook, never with a like count spoken. Narration answers it with a record; no segment reacts to it. The RODALCO2007 comment first appears in A1 (A1-S3).
- Register (owner, 15 Oct 26; `references/script-quickref.md` "Voice" on the docs-voice-hook-grain branch): Paul is an old friend you haven't seen in years, telling you what happened. First person where true of a presenter reading the sources ("I went through the whole NIST report"), "you", contractions, storm terms as fans say them (EF5, NWS, hook echo), never explained down. Writer's score for T1 and I1 in this draft: see the hand-back.
- Numbers are spoken the way an American says them at a kitchen table, spelled out for the voice: "a hundred thirty-five", "a hundred sixty-one", "twenty-five", never "one hundred thirty five of the one hundred fifty five". One count per sentence; where a ratio is needed, the plain share ("eighty-seven percent") or the screen carries the second number. Never "one thirty-five" (reads as a clock time). Years stay digits. (Owner, 15 Oct 26.)
- Source qualifiers stay off the spoken line and go on the on-screen source line with the exact base and finding: "in the investigators' count", "who lost their lives to its impact", "not one person the investigators could place", "NIST found". The spoken line stays plain and never claims more than the source: "none below ground" means those the tornado took. The locked claim lives in the header and on screen; spoken, it is said plainly. (Owner, 15 Oct 26.)
- No start times beyond `structure.md`'s plan; real times wait on the voice probe.

---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one, an old friend across the table, not a presenter. Popfig inside the first second, top left: "Joplin, Missouri · May 22, 2011". The civil-defense siren SFX starts on "A tornado siren goes off" and drops under him at "What do you do?", cut dead on his last word. A beat after "right?" so the viewer answers in their head. On "a hundred thirty-five" a chip: "135 of 155 impact-related · inside a structure · NIST Finding 40". On "below ground" a second chip: "NIST found no evidence any were underground · Finding 46". No comment card, no other video, no like count. Cut out on his last word. Glance chips (2 to 4 words, big, centre-left, one at a time, each gone before the next): "TORNADO SIREN" on "A tornado siren goes off"; "135 INDOORS" on "a hundred thirty-five" (the source chip stays below it); "0 BELOW GROUND" on "below ground".
> Okay. A tornado siren goes off. What do you do? You get inside, right? In 2011, a hundred thirty-five of the people the Joplin tornado took were inside a building when it hit. And as far as the investigators could tell, not one of them was in a basement or anywhere below ground.

**Rows:** (the viewer's belief, no row) · [T3: 135 of 155, Finding 40] · [H5: Finding 46, "no evidence ... underground"]

*(Two breaks on the viewer's own answer: they were inside, and they still were not below ground. [Q0 open]: then what went wrong? Carried as the episode loop L1.)*

## H1 alternatives (the owner picks one; the pick above is H1-S1, 43 words, one Paul clip)
- Alternative 1 (38 words): "Tornado warning, sirens going. Where do you go? Inside, lowest floor, right? In Joplin, a hundred thirty-five of the people that tornado took were inside. And as far as the investigators could tell, not one was below ground." Rows: T3, H5. Same chips as H1-S1.
- Alternative 2 (37 words): "Okay. Siren goes off. What do you do? Head for the basement, right? In Joplin, most homes didn't have one. And of the hundred thirty-five the tornado took indoors, investigators couldn't place a single one below ground." Rows: H1, T3, H5. Chips: "82% of homes · no basement · Finding 20", then the two H1-S1 chips. (Spends the basement answer that T1-S3 and I1-S1 pay.)
- Why the pick: the owner's shape, kept. The viewer answers "go inside", hears they were right, and is broken twice inside 15 s. "Were indoors when it hit" replaces "did exactly that", because NIST places them inside a structure and does not say they went in because of the siren (many were already in church, in a store, at home).

---

## T1 · Hook tail (0:15 planned)

### T1-S1 · narration
**Picture:** hard cut on the first word, never black: a NIST ground photograph of a flattened residential street (NIST NCSTAR 3, figure to pick at sourcing; its caption must place it in Joplin's damage path; never an aerial marked "Used with permission"). On "a hundred sixty-one" the number lands: "161 lives lost". Source line: "NIST count, Missouri State Police list · Finding 28". One bed swell, no siren.
> It was a Sunday evening, May twenty-second, 2011, in Joplin, in southwest Missouri, and that tornado took a hundred sixty-one lives.

**Rows:** [NIST Sec. 1.2: "On Sunday, May 22, 2011"; NIST Sec. 1.1: southwest Missouri] · [T1: 161, Finding 28]

### T1-S2 · narration
**Picture:** our own master map of Joplin, first appearance. Two siren rings pulse over the city, stamped "5:11 PM" and "5:38 PM", source line "NWS timeline · 3 minutes each". On "twice" both rings flash. Glance chip "SOUNDED TWICE" on "They went off twice".
> You might think Joplin's tornado sirens failed that evening, but they didn't. They went off twice.

**Rows:** [E6: 5:11 first siren] · [E14: 5:38 second siren] · [S27: two activations the same evening] (A2 says the second came after touchdown)

*(Third break on the viewer's belief; holds L1 open.)*

### T1-S3 · narration
**Picture:** the master map, a thin line under it labelled "below ground", empty; push in on it until it fills the frame.
> Then if the sirens worked and people were inside, why wasn't anyone down in a basement?

**Rows:** (the question; no row)

*([Q1 open]: why wasn't anybody below ground? Paid in I1-S1.)*

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · Intro: the day, the place, the two numbers (0:24 planned)

### I1-S1 · narration
**Picture:** cut to our own cross-section of a one-story house on a slab or crawl space (never drawn as a solid block), label "no basement · 82% of Joplin homes · NIST Finding 20". Then the map with no shelter icons anywhere, label "no community shelters or safe rooms · city or county · Finding 20", city label "Joplin · population 50,150 · 2010 Census (via NIST)"; the path draws west to east with the labels "6 miles in Joplin" and "about 15 minutes in the city", source line "NIST Sec. 1.3" (on screen only). [CLIP 1, candidate, not sourced] under the first sentence: public domain FEMA or NWS video of a Joplin residential street in the path, muted, about 6 s; if none is found with a provenance row, NIST ground photographs instead. On "having a basement" a second, smaller cross-section with a basement slides in, its stairs lit and empty. Glance chip "8 IN 10: NO BASEMENT" on "About eight in ten had none".
> Because most homes in Joplin didn't have a basement. About eight in ten had none. And there wasn't a single public shelter in a town of about fifty thousand. Even people who had a basement weren't always down in it when the tornado hit.

**Rows:** [H1: 82 percent lacked basements] · [H3, H4: no community shelters or safe rooms; the city owned no public storm shelter] · [X21: 50,150] · [H22, H8: 3 of 71 had basement access, at least 2 not in it] (no causal claim; plants the A3 hinge without spending the three-of-seventy-one count)

*([Q1 paid]: most homes had none, and no public shelter. [Q2 open]: who had a basement and wasn't down in it? Carried to A3-S8/S9.)*

### I1-S2 · narration
**Picture:** twenty five siren icons appear at once, placed from NIST Fig. 4-2: twenty three inside the city outline, one at Duenweg and one at the Village of Airport Drive. Source line: "25 sirens in Joplin's outdoor system · 23 in the city · NIST Sec. 4.3.1". A calendar strip slides in under the map: a grey tick on Mondays, labelled "test · 10 AM · 1 minute · weather permitting".
> If you lived in Joplin, how often do you figure you heard those tornado sirens? You could hear them most Monday mornings, because the city tested all twenty-five of them. But how often did they go off for a real storm?

**Rows:** [S2: 25-siren system; NIST Sec. 4.3.1: 23 in the city, 1 in Duenweg, 1 in Airport Drive] · [S5: Mondays, 10 a.m., 1 minute, weather permitting; S30: generally heard indoors as well as outside]

*([Q2b open] and paid in this segment: most Mondays, the test. [Q3 open]: how often for real? Paid in I1-S3.)*

### I1-S3 · narration
**Picture:** the calendar strip stretches to 2007 to 2011; the grey Monday ticks fill it. Three red marks stand out, one a year: January 18, 2007; May 10, 2008; May 8, 2009. Then a gap to May 22, 2011. Source line: "once a year at most since 2007 · NIST Finding 31 and Sec. 4.3.4, from the county emergency manager". No label calls them wind events. Glance chip "ABOUT ONCE A YEAR" on the line, the source line stays below it.
> Outside that weekly test, about once a year, if that.

**Rows:** [S2: Finding 31] · [S4, S6, S7: the rate and the dates, according to the Joplin-Jasper County emergency manager] (per the S9 CONFLICT: not called wind events)

*([Q3 paid].)*

### I1-S4 · narration
**Picture:** the calendar strip holds; a name card slides in over it: "Joplin-Jasper County emergency manager". On "every tornado warning" a second, separate strip appears under the siren strip: the tornado warnings for 2007 to 2011 only (twelve marks, S13), not paired mark by mark with the sirens. Label "not every warning got a siren · NIST Sec. 4.3.4".
> Why'd they go off so rarely? For one, Joplin's emergency manager didn't sound them for every tornado warning.

**Rows:** [S4: the Joplin-Jasper County emergency manager] · [S8: "not sounding the sirens for every tornado warning ... based on other factors as well"] · [S13: 12 warnings in the five years before 22 May 2011, the strip only]

*([Q4 open] and [Q4 paid] in this segment. The warnings strip plants A1-S7.)*

### I1-S5 · narration
**Picture:** the NWS assessment's own page, the residents' words underlined as Paul speaks: "hear sirens all the time and [sirens] go off for dark clouds". Source line "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b". Paul speaks the line; no actor's voice.
> But plenty of people there told the NWS those sirens went off all the time, even for dark clouds.

**Rows:** [S17: "Many noted..."]

*(The belief is on the table; its question is held for I1-S9 so it carries into A1.)*

### I1-S6 · narration
**Picture:** [CLIP 2, candidate, not sourced] a news pull of the aftermath along 20th Street and Range Line Road, the heavily damaged big box stores and their collapsed walls, an insert inside the intro (never in the hook), transcribed in full before the cut is chosen, held under 12 s with Paul over it. Then the NIST report's cover (NIST NCSTAR 3, public domain) and a name card "NIST · National Institute of Standards and Technology · federal investigators". Source line: "154 of 155 impact-related deaths placed · NIST Table 4-3".
> And where was everybody when the tornado hit? I went through the whole NIST report, and the federal investigators found out where almost every person the tornado took had been.

**Rows:** [T9, T12: Table 4-3 places 154 of the 155, so "almost every one"] · [B6, B9, B13: Walmart partial collapse, Home Depot wall panels, for the picture wording] · (clip: insert gate, transcript first, provenance row read; Content ID claim expected, segment must survive a claim) ("I went through the whole NIST report" kept pending the owner's answer)

*([Q5 open]: where was everybody? Paid in I1-S7 and I1-S8.)*

### I1-S7 · narration
**Picture:** the master map returns and dots land one location type at a time, each with a small on-screen label as it is named: houses, apartments, two big box stores, a pizza restaurant, two churches, a hospital, two nursing homes; then the unspoken labels a phone store, a lodge, a theater, and outside.
> They were at home, in apartments, in big box stores, a pizza place, churches, a hospital, nursing homes, and a few other spots.

**Rows:** [H26: homes, apartments; B45: Walmart, Home Depot, Pizza Hut, Full Gospel, Harmony Heights; C6: St. John's; C23, C25: Greenbriar, Meadows; B2: "big-box stores"] (a partial list, hence "a few other spots"; the screen completes it from Table 4-3)

### I1-S8 · narration
**Picture:** [RS] [VE] the whole map lit: 135 dots inside building outlines and 19 outside, 12 of them marked as in vehicles, with a small label "154 placed · 1 not placed · location unknown"; the empty "below ground" line under the map. On "a hundred thirty-five" the figure lands large: "135 of 155 impact-related · inside a structure · 87% · NIST Finding 40". On "below ground" the figure "0" lands on the empty line: "NIST found no evidence any were underground · Finding 46". Hold. The locked claim sits in the header; this line speaks it plainly (owner, 15 Oct 26).
> A hundred thirty-five of them were inside a building, and the investigators couldn't find a single one who was below ground.

**Rows:** [claim, angle.md, spoken plain] · [T3: 135 of 155, Finding 40] · [T17: outside 19, 12 in vehicles; T12: one death with no known location] · [H5, H6: Finding 46 and Sec. 4.6.2.2]

*([Q5 paid]: inside a building, none below ground. The hook's claim holds past 60 s.)*

### I1-S9 · narration
**Picture:** [CLIP 3, candidate, not sourced] public domain NWS or FEMA footage of the survey team in Joplin, muted under the voice; if none is found with a provenance row, NWS assessment photographs or figures instead. Then the calendar strip from I1-S3 returns, the grey Monday ticks dimmed and the red marks lit, small label "outside the weekly test", and the NWS assessment's page, a slow push in on the word "sirens". Source line: "NWS assessment team · interviewed over 60 survivors". The bed drops out on the last word.
> So if those tornado sirens hardly ever sounded for a real storm, why did so many people think they went off all the time? After the storm, the NWS interviewed more than sixty survivors, and plenty of them talked about the sirens.

**Rows:** [S3: residents believed in many false alarms] · [X26: "interviewed over 60 survivors"; S16, S17: "a large number of participants", "Many noted"] (the exit question plus one affirming line)

*([Q6 open] = [loop L2 open]: why people thought the sirens went off all the time. Carried out of I1; paid in A1.)*

*(blackout 0.7 s)*

---

## A1 · Sirens: belief against record (1:45 to 4:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** prove the belief and the record side by side, and keep the two false-alarm numbers apart.
- **Question:** where did "all the time" come from, if the record says about once a year?
- **Reveal:** the weekly one-minute Monday test (about fifty two a year) plus about one real sounding a year since 2007, three of them dated. The false alarms were real, in a different set: 14 of 18 tornado warnings from 2005 to 2011 had no verified tornado, in line with the national 74.7 percent, and 11 of 12 in the last five years. People heard warnings and tests and filed them all under "sirens". Plus the belief in a "protective bubble".
- **Visual event:** [RS] a two-row calendar 2007 to 2011: fifty two grey test ticks a year against single red marks; a second, separate strip for the 18 warnings, 4 verified.
- **Exit hook:** "The second time Joplin's tornado sirens went off that evening, people couldn't agree on what it meant."
- **Comments answered:** RODALCO2007 ("no one is paying any attention to the sirens going off", 3,000 likes; its first and only card, at A1-S3); "The sad part is nobody knew what really was coming that day." (824 likes).

**Segments:**

### A1-S1 · narration
**Picture:** the NWS assessment's own page (Finding 2b), each line underlined as Paul speaks it: "sirens are sounded even for thunderstorms", "all sirens mean is there is a little more water in the gutter", "bombarded with [sirens] so often that we don't pay attention". Source line "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b". Then a NIST ground photograph of a Joplin street in the path (credit line checked). Low bed.
> I went through what people in Joplin told the NWS afterward. They said the tornado sirens went off even for thunderstorms. Some said all a siren meant was a little more water in the gutter. Others said they'd been bombarded so often, they'd stopped paying attention.

**Rows:** [S18] · [S18] · [S17]

### A1-S2 · narration
**Picture:** a quote card over a NIST ground photograph of the Stained Glass Theater (credit line checked): "I didn't put much stock in that siren, because I'd heard them before, and 9 times out of 10, you hear the sirens but nothing really happens" · "an actor in the play · NIST Interview 120". On "three people" three small markers light on the theater's outline on the master map. Chip "3 LOST HERE".
> One of the people NIST talked to was an actor at the Stained Glass Theater, and the actor said they didn't put much stock in that siren. Nine times out of ten, you hear the sirens and nothing really happens. Three people in that theater were lost. So were the sirens really crying wolf in Joplin?

**Rows:** [S24: NIST Interview 120, no gender given] · [B25: three lost at the theater]

*([A1-Q1 open]: did the sirens really cry wolf? Paid in A1-S5. Plants A4-S9.)*

### A1-S3 · narration
**Picture:** the RODALCO2007 card, its first and only appearance: "no one is paying any attention to the sirens going off" · RODALCO2007 · 3,000 likes · under "JOPLIN, MO, Tornado, 22 May 2011" (likes on the card, never spoken; no frame of that video). Beside it, the NWS assessment's page with "desensitized or complacent" underlined. Chip "NUMB TO SIRENS". Source line "NWS Assessment, Preface and Finding 2c".
> You've probably seen comments like this one under the old Joplin videos. The NWS found something close to it. Most of the people it surveyed had gone numb to the tornado sirens, and the first siren had lost some of its credibility.

**Rows:** [angle.md: the comment, verbatim] · [S16: "desensitized or complacent"] · [S19: "initial siren activation has lost a degree of credibility"]

### A1-S4 · narration
**Picture:** the channel's civil-defense siren SFX for one second, then the calendar strip 2007 to 2011: fifty two grey ticks a year, and the three red marks land together on "three times", each carrying its own label on screen, not spoken: "Jan 2007 · winds over 70 mph", "May 2008 · EF1 outside the city", "May 2009 · winds over 85 mph". Chips "52 TESTS A YEAR", then "3 REAL SOUNDINGS". Source line "dates per the county emergency manager · NIST Sec. 4.3.4".
> So how often did those sirens actually go off? If you lived in Joplin, you heard them every week, because the test ran about fifty-two times a year. Outside that test, they went off for real three times from 2007 on: twice for strong winds, and once for an EF1 outside town. Then nothing, until May twenty-second, 2011.

**Rows:** [S4: about 52 a year] · [S6: 18 Jan 2007, winds over 70 mph; 10 May 2008, EF-1 outside the city limits] · [S7: 8 May 2009, winds over 85 mph; next on 22 May 2011]

### A1-S5 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. No chip.
> Stick with me, because what I'm about to explain is a big part of why Joplin heard rare tornado sirens as noise.

**Rows:** (hook callback HC1, no row; "a big part of", per factcheck-A1-A3 row A1-S6. Moved ahead of the Finding 31 line per the acts grade, top 5 #1, so the question is answered straight after it is asked; the segment ids S5 and S6 swapped with it.)

### A1-S6 · narration
**Picture:** the NIST page, Finding 31, the sentence underlined: "Despite public perception, no evidence was found of high false-alarm rates for Joplin's outdoor siren system." Chip "NO FALSE-ALARM PROBLEM". Source line "NIST NCSTAR 3 · Finding 31".
> I checked that against the NIST report. Despite what people believed, it found no evidence that Joplin's tornado sirens had a false alarm problem. So if the sirens weren't crying wolf, what was?

**Rows:** [S1: Finding 31] · [S15: siren false alarm defined as a sounding with no severe weather in Joplin]

*([A1-Q1 paid]. [A1-Q2 open]: if not the sirens, what was crying wolf? Paid in A1-S7.)*

### A1-S7 · narration
**Picture:** [RS] a second strip slides in under the siren strip, separate from it and in a different color: eighteen warning marks from 2005 to 2011, four of them ticked "verified". Chip "14 OF 18 · NO TORNADO". Then the last five years zoom in: twelve marks, one ticked. Chip "11 OF 12". Source line "NIST Finding 30 · national 2007 to 2011 average 74.7% (NIST)". The two strips never merge.
> There's a second count, and it isn't the sirens. It's the tornado warnings from the NWS. From 2005 to 2011, Joplin got eighteen tornado warnings, and fourteen of them never came with a tornado. That's about the national average. In the last five years, it was eleven out of twelve.

**Rows:** [S10, S12: 14 of 18, 2005 to 2011; national 74.7% on screen with NIST as its source, per the S10 CONFLICT] · [S11, S13: 11 of 12, 2007 to 2011] · [S14: a warning false alarm is an unverified warning]

*([A1-Q2 paid]: the tornado warnings did have a false alarm problem.)*

### A1-S8 · narration
**Picture:** the two strips side by side; a name card "Joplin-Jasper County emergency manager" over the gap between them. Chip "TWO DIFFERENT COUNTS". Source lines "NIST Sec. 4.3.4" and "NIST Finding 44 · Sec. 4.7.3".
> So did people keep the two apart? Joplin's emergency manager didn't sound the sirens for every one of those warnings, so you can't add them together. But people thought both were crying wolf anyway, and that kind of distrust and confusion is one of the reasons people were slow to act that evening.

**Rows:** [S8] · [S28: citizens perceived high false-alarm rates for both] · [S39, S40: distrust of or confusion about the emergency communications system, in the second factor]

### A1-S9 · narration
**Picture:** a quote card: "the announcer and the weatherman that came on the TV seemed to say the track was, you know, mainly north of town" · "a Joplin native · NIST Interview 58". Beside it the comment card "The sad part is nobody knew what really was coming that day." (824 likes). Then the NIST sentence as on-screen text: "the media continued to report on storms said to be passing to the north and missing Joplin". Chip "TRACK: NORTH OF TOWN". Then the real clip, a friend saying "look at this": the live TV broadcast re-upload, YouTube FagzNHuI5JI (research/comment-beats.json; comments-for-writer.md "live TV broadcast re-upload"), a few seconds where the coverage talks about storms to the north, cut on an audio event. Transcribe first; station name, provenance row and Content ID risk checked at sourcing. If the transcript has no such moment: CLIP NEEDED: local TV coverage that afternoon saying the storms were north of Joplin.
> Then there's what people were seeing on TV. One Joplin native remembered the announcer and the weatherman seeming to say the storm was tracking north of town. So why were people in Joplin so ready to believe that?

**Rows:** [E12: media reported storms passing north] · [NIST Interview 58, factcheck-A1-A3 row A1-S9: TV only, "a Joplin native"]

*([A1-Q3 open]: why so ready to believe it? Paid in A1-S10.)*

### A1-S10 · narration
**Picture:** our own map, an eighty-mile ring around Joplin. On "a hundred eighty-two" the ring fills with small dots; inside the city outline one dot, "May 5, 1971". Chips "1 IN THE CITY", then "182 WITHIN 80 MILES". Source line "NIST Finding 33". The NWS page with "protective bubble" underlined.
> Because people there believed storms always blew over and missed Joplin, as if the town had a protective bubble around it. And you can see where that came from. Since 1950, the city itself had been hit by one tornado rated EF2 or stronger. Within eighty miles of Joplin, there'd been a hundred eighty-two.

**Rows:** [S23: "protective bubble"] · [S36: one EF-2 or greater in the city since 1950, 5 May 1971] · [S37: 182 within 80 miles] · [S38: NIST calls the immunity belief scientifically unfounded]

*([A1-Q3 paid]. [loop L2 closes], as our reading: the weekly tests and the warnings both sat under the word "sirens" for people; NIST's finding is only that citizens perceived high false-alarm rates for both.)*

### A1-S11 · narration
**Picture:** the master map, two siren rings, the second one pulsing. The bed drops out on the last word.
> The second time Joplin's tornado sirens went off that evening, people couldn't agree on what it meant.

**Rows:** [S26, S27]

*([loop L3 open]: what the second siren meant. Paid in A2-S11.)*

---

## A2 · The evening, five oh nine to five thirty eight (4:45 to 7:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** a countdown that shows the first siren sounded for a storm that never made a tornado, and the second came as the tornado entered the city.
- **Question:** what did the second siren mean to the people who heard it?
- **Reveal:** 5:09 warning for a different storm; 5:11 first siren, mainly for funnel reports in Kansas, heard as meant for the north; 5:17 the city-wide warning, no new siren; media still saying the storms were passing north; rotation from 5:29 to touchdown at 5:34; 5:38 second siren, four minutes after touchdown. Lead time: seventeen minutes to touchdown from the 5:17 warning, twenty three from the first siren. People read the second siren as worse, or as an all clear; the city had no all-clear signal. For most it was the non-routine signal that sent them to shelter.
- **Visual event:** [RS] a clock running down the master map: polygon 30 in the north, polygon 31 over the city, siren rings at 5:11 and 5:38, the touchdown dot at 5:34. Radar: NWS Assessment Appendix A, Figure 4 panel (G): KSGF 0.5 degree base reflectivity, valid 22 May 2011 22:34Z (5:34 pm CDT), credited "NOAA/NWS", no NWS logo and no third-party basemap; panel (H) storm-relative velocity at the same time if wanted; never NIST Fig. 2-7 as "NOAA" (factcheck-acts, A2 radar CONFIRMED).
- **Exit hook:** "At five thirty-eight, most people went for the best spot they had. The investigators went back later and looked at what was underneath that spot."
- **Comments answered:** "Residents of Joplin had plenty of warning time." (1,800 likes); "even the best of technology wouldnt have helped alert the people on time" (2,500 likes); "Joplin didn't receive a tornado emergency because of how fast it developed." (1,500 likes).

**Segments:**

### A2-S1 · narration
**Picture:** [RS] the countdown begins: a clock top left on the master map, "1:30 PM", then "4:33 PM". Chips "TORNADO WATCH", then "NWS BRIEFING". Source line "NWS Assessment, Table 1 · NIST E.3".
> Let's go back to that Sunday afternoon. By one-thirty, the SPC had a tornado watch out for southwest Missouri, and by four thirty-three, the Springfield NWS office had briefed Joplin's emergency manager about storms to the west. So if you lived in Joplin, when did the tornado sirens first go off?

**Rows:** [E1: 1:30 pm, NWS time, per the E1/E2 CONFLICT] · [E3: 4:33 pm briefing]

### A2-S2 · narration
**Picture:** clock "5:09 PM". Warning polygon 30 draws over western Jasper County, clipping the northeast corner of Joplin; "polygon 30" on screen only. Chip "WARNING · NE CORNER". Source line "NWS Table 1 · NIST Sec. 2.2.2".
> At five-oh-nine, a tornado warning went out, but it only clipped the northeast corner of Joplin, and the storm behind it never made a tornado.

**Rows:** [E4] · [E5: the storm did not produce a tornado; only a small part of the city]

### A2-S3 · narration
**Picture:** clock "5:11 PM". The siren ring pulses over the whole city; the civil-defense siren SFX, three seconds, under Paul. An arrow points west into Kansas: "funnel cloud reports · SE Kansas". Chip "FIRST SIREN · 3 MIN". Then the polygon in the north lights again. Source line "NWS Assessment, Sec. 3".
> At five-eleven, Joplin's tornado sirens went off for three minutes, mostly because of funnel cloud reports over in southeast Kansas. People heard the sirens, heard that the warning was for the north side, and figured the sirens were for the north side too. So what did they do next?

**Rows:** [E6: 3 minutes] · [E8: funnel reports in SE Kansas] · [E8b: assumed it was for the area to the north]

*([A2-Q1 open]: what did people do next? Paid in A2-S4.)*

### A2-S4 · narration
**Picture:** a quote card over a NIST ground photograph (credit line checked): "The tornado sirens went off once, we walked outside and you couldn't really, didn't really see nothing then, and we went back in and finished eating." · "a survivor · NIST Interview 108". Chip "NOTHING TO SEE". Source line "NIST E.3: few environmental clues".
> Some people looked outside, and there wasn't much to see. One survivor said they walked out after the sirens, didn't see anything, and went back in to finish eating.

**Rows:** [E7: few environmental clues] · [E34: NIST Interview 108]

*([A2-Q1 paid].)*

### A2-S5 · narration
**Picture:** clock "5:17 PM". Polygon 31 draws over the whole city; "polygon 31" on screen only. The siren ring stays dark. Chip "WHOLE CITY · NO SIREN". Source line "NIST Sec. 1.2".
> At five-seventeen, a new tornado warning covered the whole city. Did the sirens go off again? They didn't, most likely because they'd already gone off six minutes earlier.

**Rows:** [E9] · [E10: not activated again, probably because sounded 6 min earlier]

*([A2-Q2 open] and paid in this segment.)*

### A2-S6 · narration
**Picture:** the NIST sentence as on-screen text over the master map, an arrow running north toward "Webb City · Carl Junction": "the media continued to report on storms said to be passing to the north and missing Joplin, or moving away from the City". Source line "NIST Sec. 1.2". No TV pull (none sourced).
> And if you had the TV on, the news was still talking about storms passing to the north, up toward Webb City and Carl Junction.

**Rows:** [E11: warning information before 5:17 was about a storm to the north, toward Webb City or Carl Junction] · [E12]

### A2-S7 · narration
**Picture:** two comment cards side by side: "Residents of Joplin had plenty of warning time." (1,800 likes) and "even the best of technology wouldnt have helped alert the people on time" (2,500 likes). Between them a lead-time bar. Chips "17 MIN" on the first count, "23 MIN" on the second. Source lines "17 min · 5:17 warning to touchdown · NIST Sec. 2.2.2 · NWS Sec. 4", "23 min · first siren to touchdown" and "most did not act on a warning alone · NWS Assessment".
> So how much warning did people in Joplin actually get? From the citywide warning, people had seventeen minutes before touchdown, and from the first siren, they had twenty-three. On paper, that's real lead time. But most people didn't act on a warning alone. They waited for something out of the ordinary.

**Rows:** [E21, E22: 17 min from TO.31; 23 min from the first siren] · [E37: most did not act until a non-routine trigger]

*([A2-Q3 open] and paid: how much warning. [A2-Q4 open]: what was the out-of-the-ordinary thing? Paid in A2-S10.)*

### A2-S8 · narration
**Picture:** the radar: NWS Assessment Appendix A, Figure 4 panel (G), KSGF 0.5 degree base reflectivity, valid 22 May 2011 22:34Z (5:34 pm CDT), credited "NOAA/NWS", no NWS logo and no third-party basemap. Clock "5:29 PM" then "5:34 PM". Chips "RAIN-WRAPPED", then "NO TORNADO EMERGENCY". The comment card "Joplin didn't receive a tornado emergency because of how fast it developed." (1,500 likes) slides in at the end. Source line "NWS Assessment, Finding 10 and the paragraph before Finding 8".
> Could people at least see it coming? The storm wasn't giving them much to look at. The rotation tightened up from five twenty-nine, and by five thirty-four the tornado was on the ground, wrapped in rain. The NWS never put out a Tornado Emergency headline for Joplin itself. The tornado formed too fast, right at the edge of the city, and you couldn't tell how big it was until it was well into town.

**Rows:** [E25: 5:29 to touchdown 5:34] · [E13] · [E32: rain-wrapped] · [NWS Assessment, paragraph before Finding 8, factcheck-acts row A2-S8]

### A2-S9 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. Chip on "four minutes": "4 MIN AFTER TOUCHDOWN", source chip "NIST Finding 35". The cut lands on his last word, straight into the real clip that opens A2-S10.
> At five thirty-eight, the tornado's been on the ground for four minutes. It's just reaching the city, and that's when the tornado sirens go off again.

**Rows:** [E14] · [E15, E17: "almost exactly when the tornado entered the City", per factcheck-A1-A3 row A2-S9]

### A2-S10 · narration
**Picture:** first the real clip, before Paul's voice comes in: the live TV broadcast re-upload, YouTube FagzNHuI5JI (research/comment-beats.json), 4 to 6 s of the moment the studio takes shelter while the sirens blare (the 3,800-like comment in comments-for-writer.md describes it), its own audio up, cut on an audio event. Transcribe first; a different cut from A1-S9's; station name, provenance row and Content ID risk checked at sourcing. Then the NWS page, Finding 2d (c), "non-routine second siren alert" underlined. Chip "SECOND SIREN". Then the NIST page, Finding 45, "hearing or seeing the tornado approaching" underlined. Source lines "NWS Assessment, Finding 2d" and "NIST Finding 45".
> So what finally got people moving? Joplin's rule was one sounding per alert, and for a lot of people, that second siren was the out-of-the-ordinary thing that got them going. But the biggest push of all was seeing or hearing the tornado coming.

**Rows:** [E20: one sounding per alert] · [E19: the second siren raised awareness, prompted shelter] · [E37] · [E33: Finding 45, high-intensity cues]

*([A2-Q4 paid].)*

### A2-S11 · narration
**Picture:** the siren ring splits into two labels: "a worse warning" and "all clear". On "all-clear signal" a crossed-out icon, chip "NO ALL-CLEAR SIGNAL". Source line "NIST Sec. 4.7.1.2 · Sec. 4.3.1".
> So what did that second siren mean? It depended on who you asked. Some people took it as a worse warning. Others took it as the all clear. And Joplin's sirens didn't even have an all-clear signal.

**Rows:** [S25, S26] · [S33: no all-clear message by design]

*([loop L3 closes].)*

### A2-S12 · narration
**Picture:** the master map, the residential area lit; a thin "below ground" line under it. The bed drops out on the last word.
> At five thirty-eight, most people went for the best spot they had. The investigators went back later and looked at what was underneath that spot.

**Rows:** [H23: most took shelter in the most appropriate place available]

*([loop L4 open]: what was underneath. Paid in A3-S1.)*

---

## A3 · Homes with nothing underneath (7:45 to 11:15 planned; book ad inside)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the first and largest group on the map: 71 in houses and apartments, in a city where 82 percent of homes had no basement and no public shelter existed.
- **Question:** what was under the best place they had?
- **Reveal:** 82 percent of homes had no basement; no community shelter or safe room in city or county. 59 in single-family homes, 54 of them in homes rated demolished, 50 in one-story homes; 12 in apartments, all above ground. After the ad: only 3 of the 71 had a basement they could reach, and at least two of the three were not in it when the storm hit. Survivors in the EF-4 zone: 11 of 27 in basements, 15 in interior rooms. A neighborhood of early-1980s ranch homes with basements: heavy damage, nobody lost.
- **Visual event:** [RS] the 71 dots light on the map in house outlines; a cross-section of a one-story house with an empty space where a basement would be. Counter visit 1: "INSIDE A BUILDING 71 of 135" over "BELOW GROUND, NONE FOUND", about 5 s.
- **Exit hook:** "Most of the big stores had something the homes didn't: a spot set aside for cover, and staff who knew where it was."
- **Comments answered:** "most people that took shelter in their homes" (1,100 likes); "my step dad went to the center most closet in the house, threw everything out into the hallway" (1,600 likes); "How does anyone survive this?" (431 likes).

**Segments:**

### A3-S1 · narration
**Picture:** our own cross-section of a one-story house on a crawl space, a figure in an interior bathroom, label "no basement · 82% of Joplin homes · NIST Finding 20". Chip "8 IN 10: NO BASEMENT". Source line "NIST Sec. 1.2". Then the master map with no shelter icons anywhere, chip "NO PUBLIC SHELTER", source line "no community shelters or safe rooms · city or county · Finding 20" (the spoken A3-S2 line is cut per the acts grade: the viewer already heard it in I1-S1; the chip carries it).
> For most families in Joplin, the best spot was a closet, a hallway or a bathroom in the middle of the house. Eight of ten homes there didn't have a basement to go to.

**Rows:** [H2: interior bathrooms, closets, laundry rooms, hallways] · [H1: 82 percent lacked basements] · [H3, H4: on screen only]

*([loop L4 closes].)*

### A3-S3 · narration
**Picture:** [RS] dots light in house outlines across the residential area. Chip "59 LOST IN HOUSES". Running label (on screen, not spoken): "59 people · 51 homes · 54 lost in demolished homes · 50 in one-story homes". Source line "NIST Sec. 4.6.2.2 · Table 4-3".
> Fifty-nine people were lost in single-family houses, and nearly all of them were in a house the tornado flattened. Some homes in the path did have a basement, though. So did anyone the tornado took make it down there?

**Rows:** [H9, H10, H11: 59 people, 51 homes; 54 of the 59 in demolished homes; 50 of the 59 in one-story homes; Table 4-3 base per the H25/H26 CONFLICT] · [H7: 3 of 59 had access to an underground level]

*([cta-hinge planted early]: the question is answered after the ad.)*

### A3-S4 · narration
**Picture:** a NIST ground photograph of a demolished apartment complex (figure to pick at sourcing; credit line checked). Twelve dots in three apartment outlines. Chip "12 IN APARTMENTS". Then a drawn staircase, neighbors under it. Source line "NIST Sec. 4.6.2.2 · Sec. 1.2".
> Twelve more people were lost in three apartment complexes. The buildings were mostly wood frame, there wasn't any protected space, and every one of those twelve was above ground. At the Somerset complex, one woman got out of her apartment and rode out the tornado under the building's staircase with her neighbors.

**Rows:** [H19: 12 in three complexes, all above ground] · [H20: the Somerset survivor]

### A3-S5 · narration
**Picture:** the comment card "my step dad went to the center most closet in the house, threw everything out into the hallway" (1,600 likes). Then a tally: "27 survivors in the EF-4 zone · 11 basements · 1 crawl space · 15 closets, hallways, bathrooms". Chip "27 SURVIVORS". Source line "NIST Sec. 4.6.2.2". Then CLIP NEEDED: a Joplin survivor who rode it out in a closet, hallway or bathroom, telling it in their own voice (FEMA survivor interview first, public domain; research/ names no clip for this beat).
> So who came through? I looked at the people NIST talked to who'd survived in houses in the worst part of the path. Eleven of them had made it to a basement, and almost everyone else rode it out in a closet, a hallway or a bathroom.

**Rows:** [H13: 11 of 27 in basements] · [NIST Sec. 4.6.2.2, one in a crawl space, factcheck-A1-A3 row A3-S5] · [H14: 15 in internal first-floor spaces]

*([A3-Q1 open] and paid.)*

### A3-S6 · narration
**Picture:** a NIST ground photograph of a wood-frame house with its roof and walls separated (figure to pick at sourcing; credit line checked; no video sourced). Then our exploded house diagram: roof-to-wall and wall-to-floor joints highlighted. Chip "THE JOINTS GAVE". Source line "NIST Finding 14". CLIP NEEDED: moving footage of a wood-frame house in the path with its roof and walls pulled apart (public domain FEMA or NOAA first; research/ names no video for this beat).
> So why didn't more of these houses hold? Look at how they came apart, and you'll see it. Mostly, they gave at the joints, where the roof meets the walls and the walls meet the floor.

**Rows:** [H30: failures predominantly at the connections]

### A3-S7 · narration
**Picture:** a NIST ground photograph of an in-home shelter standing in a destroyed house (figure to pick at sourcing; credit line checked). Chip "IN-HOME SHELTERS HELD". Source line "NIST Finding 23 · Sec. 1.2".
> If you had a storm shelter built into your house, you came through. Hardly anybody had one.

**Rows:** [H16: in-home shelters performed well] · [H18: very few had one; those who did survived]

### A3-S8 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. Chip on "seventy-one": "71 LOST AT HOME", source chip "NIST Sec. 4.6.2.2". Hold on his face for a beat after the last word.
> Three of the seventy-one people lost at home had a basement they could get to, and they still didn't make it.

**Rows:** [H22: only three of the 71 had access to basements]

*([loop cta-hinge open]: how?)*

### Book ad (24.4 s, its own voice, mounted from `config.yaml channel.cta`; planned 10:30 to 10:54.4)

### A3-S9 · narration
**Picture:** a drawn basement stair, lit, empty. Chip "2 OF 3 NOT DOWN THERE". Source chip "at least 2 of 3 · the third: circumstances unknown · NIST Sec. 4.6.2.2".
> At least two of the three weren't in the basement when the tornado hit. Where the third person was, NIST couldn't say.

**Rows:** [H8] · [H22]

*([loop cta-hinge closes].)*

### A3-S10 · narration
**Picture:** the master map: a pocket of early-1980s ranch houses lit, no dots in it. Chip "BASEMENTS HELD". Source lines "NIST Finding 46" and "NIST Sec. 1.2".
> So what about the people who did get down there? Their basements held. In the flattened houses where people went down to the basement, nobody was lost. And there's a whole neighborhood of early-eighties ranch houses with basements that got hit hard, and nobody there was lost either.

**Rows:** [H5: no fatalities in demolished detached homes where people took refuge in basements] · [H15: the ranch-home neighborhood]

*([loop L8 closes] in part: having a basement and being down in it were two different things.)*

### A3-S11 · narration
**Picture:** counter visit 1: the glass card top right, "INSIDE A BUILDING 71 of 135" over "BELOW GROUND, NONE FOUND", about 5 s, source line "NIST Table 4-3 · impact-related · Finding 46". Then the commercial strip on 20th Street lights on the master map. The bed drops out on the last word.
> Most of the big stores had something the homes didn't: a spot set aside for cover, and staff who knew where it was.

**Rows:** [H26, H19: 59 + 12 = 71, Table 4-3] · [B2: designated refuge areas in most big-box stores] · [B5, B44: staff direction and business plans]

*([loop L5 open]: was that spot the protection people hoped for? Paid in A4.)*

---

## A4 · Stores, churches, restaurants (11:15 to 14:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the refuge areas that existed, and why they did not hold; plus the one cellar that did.
- **Question:** did the refuge areas protect the people inside them?
- **Reveal:** NIST found no evidence the designated refuge areas helped. Walmart: fifty to sixty in the refuge area, the wall came in onto it, a D-shaped pocket, three lost, location uncertain. Home Depot: thirty five in the training room survived as the panels fell outward; eight lost there, and survivors' accounts put seven of them inside, walking along the front wall. Pizza Hut cooler, five lost; some discussed whether the second siren meant all clear. Dillon's cooler: thirty five, all survived. Stained Glass Theater: the only basement among the eight buildings, one person wide at the stairs. Two churches, seven lost. Then Macadoodles: twelve people twenty feet down in a concrete wine cellar, all walked out.
- **Visual event:** [RS] NIST ground photographs of the Walmart and Home Depot; the D-shaped pocket drawn over the Walmart floor plan; the Macadoodles cellar as a cross-section, twelve figures below the line. Counter visit 2: "INSIDE A BUILDING 102 of 135" over "BELOW GROUND, NONE FOUND", about 5 s.
- **Exit hook:** "One building in the path was full of patients, some of whom needed help to move, and that evening its plan started when a nurse heard a tornado siren."
- **Comments answered:** "what about that Home Depot? Think that'd be a bad spot?" (1,500 likes) with "Home Depot would NOT have been a good spot ... eight people died there." (1,100 likes).

**Segments:**

### A4-S1 · narration
**Picture:** the master map, the commercial strip at 20th Street and Range Line Road, refuge-area markers in the big stores; Paul's voice over it. Then CLIP NEEDED: moving footage of the 20th Street and Range Line Road stores after the tornado (public domain FEMA video first; a news pull only as a short insert, transcribed first; research/ names no clip for this beat).
> Stick with me, because what I'm about to explain is a big part of why the safe spots in Joplin's biggest stores weren't the protection people hoped for.

**Rows:** (hook callback HC2; wording per factcheck-A4-Z1 row A4-S1; "exactly why" softened to "a big part of why" to match A1-S5, per factfix-verify residual flag) · [B1, B2, B3: few basements, refuge areas picked out, no evidence they changed outcomes]

### A4-S3 · narration
**Picture:** our floor plan of the Walmart on Range Line Road, the layaway area at the back lit, then a NIST ground photograph of the Walmart (credit line checked; never an aerial marked "Used with permission"; no news pull). Chips "200 INSIDE", then "50 TO 60 AT THE BACK". Source line "NIST Sec. 1.2 · Sec. 4.6.2.1".
> Take the Walmart on Range Line Road. There were about two hundred people inside, and staff sent fifty or sixty of them to the layaway area at the back. Then the tornado brought the outside wall down, inward, right onto that area. So how did anyone back there make it out?

**Rows:** [B9: about 200 inside] · [B5: Site-to-Store or layaway area] · [B6: 50 to 60 there; the wall collapsed inward onto the refuge area]

*([A4-Q1 open]. Paid in A4-S4.)*

### A4-S4 · narration
**Picture:** the floor plan: the fallen wall drawn resting on a row of cabinets, the D-shaped pocket lit. Chip "A D-SHAPED POCKET". Then three markers near the middle of the store, not in the refuge area, chip "3 LOST", source chip "location uncertain · likely near the center · NIST Sec. 1.2".
> The wall came to rest on a row of cabinets, and it left a pocket of space shaped like a D. Three people were lost in that Walmart. Exactly where they were isn't certain, but they were most likely near the middle of the store.

**Rows:** [B10: D-shaped pocket of safety] · [B7: three lost, location uncertain; NIST Sec. 1.2, likely near the center, factcheck-A4-Z1 row A4-S4] · [B6: some protection for the 50 to 60]

*([A4-Q1 paid].)*

### A4-S5 · narration
**Picture:** the comment card "what about that Home Depot? Think that'd be a bad spot?" (1,500 likes), then a NIST ground photograph of the Home Depot, panels down (credit line checked). Label "63 of 73 wall panels collapsed" (on screen, not spoken). Our floor plan: the training room at the back lit, the panels there falling outward; the front wall and the lumber entrance marked. Chips "35 IN THE TRAINING ROOM", then "8 LOST". Source line "8 per death certificates · 7 inside per survivors · lumber entrance and front wall per store management · NIST Sec. 4.6.2.1 · Sec. 1.2". CLIP NEEDED: moving footage of the Home Depot site with its wall panels down (public domain FEMA first; research/ names no clip for this beat).
> And what about the Home Depot? About thirty-five people sheltered in the training room at the back. If you were in there, the concrete walls fell outward, away from you. Eight people were lost at that Home Depot, and most of them had just come in through the lumber entrance. They were walking along the front wall when it came down.

**Rows:** [B11: approximately 35, panels collapsed outward] · [B14: 8 by death certificates, 7 inside by survivor interviews, per the CONFLICT] · [B12: store management's account] · [B13]

*([A4-Q2 open] and paid: the Home Depot.)*

### A4-S6 · narration
**Picture:** the master map: the tornado's center line drawn just north of 20th Street, between the two stores, passing near the Pizza Hut. Then a drawn cooler door. Chip "5 LOST". Source line "NIST Sec. 1.2 · Sec. 4.4.8".
> The center of the tornado passed between those two stores, right by the Pizza Hut. Staff and customers there got into the cooler. The building was demolished, and five people were lost. At five thirty-eight, some of them had been discussing whether that second siren meant all clear. So was getting into a cooler a mistake?

**Rows:** [B17] · [B18: five lost, two employees, three customers] · [B19: some discussed whether it meant all clear]

### A4-S7 · narration
**Picture:** the map moves to 20th Street and Connecticut; a NIST ground photograph of the Dillon's grocery (credit line checked). A drawn produce cooler, thirty five figures. Chip "35 IN THE COOLER · ALL SURVIVED". Source line "NIST Sec. 1.2".
> Not at the Dillon's grocery store. Thirty-five people there got into the produce cooler. The building was demolished, and all thirty-five of them survived, with at most minor cuts and bruises.

**Rows:** [B20]

### A4-S9 · narration
**Picture:** a NIST ground photograph of the Stained Glass Theater (credit line checked). The full quote card, no ellipsis: "We have a strong building here and anyone who wants to stay is welcome to do so. We can all go down in the basement." (NIST Interview 121), then "we want you to get to the basement right now". Chip "56 INSIDE". Source line "NIST Sec. 4.4.3".
> Remember the Stained Glass Theater, where that actor didn't put much stock in the siren? Fifty-six people were inside. Right around the first siren, the director told everyone it was a strong building. Anyone who wanted to stay could, and they could all go down to the basement. Twenty-five minutes later, the director told everyone still there to get to the basement right now. Did they make it?

**Rows:** [B24: 56 inside] · [B26: the first announcement, around the first siren, full quote] · [B27: about 25 minutes later]

*([A4-Q3 open]. Paid in A4-S10.)*

### A4-S10 · narration
**Picture:** a drawn stair, one person wide; figures on it, fifteen below the line. Three markers above it. Chips "STAIRS ONE PERSON WIDE", then "ABOUT 15 GOT DOWN". Source line "one interviewee · NIST footnote 153 · Sec. 4.6.2.1".
> The stairs down were only about one person wide. About fifteen people got down. There's no evidence any of the three people lost ever made it to the basement, and the director was still at the top of the stairs when the building was hit.

**Rows:** [B28] · [B29: about 15, one interviewee] · [B25, B31: no evidence any of those lost were in the basement] · [B30: the director at the top of the stairs]

*([A4-Q3 paid]. Pays A1-S2.)*

### A4-S11 · narration
**Picture:** a NIST ground photograph of Harmony Heights Baptist (credit line checked), then the Full Gospel Church site. Chips "3 LOST", then "4 LOST". Source line "NIST Sec. 4.4.5 · 7 in churches per Table 4-1".
> Two churches were in the path too. At Harmony Heights Baptist, the second siren came just as off-duty firefighters' radios were talking about tornadoes, and the pastor sent people to safe places. Three women were lost there. At the Full Gospel Church, four people were lost.

**Rows:** [B37: second siren coincided with the radios; the pastor sent people to safety] · [B36: three women] · [B38] · [B39, B45: 3 and 4; 7 on the source line, per the B39/B50 CONFLICT]

### A4-S12 · narration
**Picture:** our own text card, never the NIST page (its sentence carries a hard flag word): "In all of the demolished buildings, those lost or badly hurt were above ground · NIST Sec. 4.6.2.1". Chip "ALL ABOVE GROUND".
> In every demolished building the investigators looked at, the people who were lost or badly hurt were above ground. So did anybody in that part of town make it below ground?

**Rows:** [B32] · [B4: no building type provided life-safety protection]

*([A4-Q4 open]. Paid in A4-S13.)*

### A4-S13 · narration
**Picture:** [RS] [VE] a NIST ground photograph of the demolished Macadoodles (credit line checked), then our cross-section: the store above, a concrete cellar twenty feet below, twelve figures below the line. Chip "12 BELOW GROUND · ALL OK". Source line "NIST Sec. 4.4.3".
> One group did. At Macadoodles, the manager led six customers, one of them a baby, and six staff down into a concrete wine cellar about twenty feet deep. The building above them was demolished, and nobody down there got hurt.

**Rows:** [B34: six customers including a baby, six staff] · [B49: the manager led them down] · [B35: concrete, about 20 ft deep] · [B33: demolished, no injuries]

*([A4-Q4 paid]. The zero below ground is about the people the tornado took, never about everyone below ground.)*

### A4-S14 · narration
**Picture:** counter visit 2: the glass card top right, "INSIDE A BUILDING 102 of 135" over "BELOW GROUND, NONE FOUND", about 5 s, source line "NIST Table 4-3 · impact-related · Finding 46". Then St. John's outline lights on the master map. The bed drops out on the last word.
> One building in the path was full of patients, some of whom needed help to move, and that evening its plan started when a nurse heard a tornado siren.

**Rows:** [B45, H26, H19: 71 + 31 = 102, Table 4-3] · [C10: Condition Gray started when the head nurse verified the sirens] · [C8]

*([loop L5 closes] above; [loop L6 open]: what happened when the plan started on a siren. Paid in A5-S2.)*

---

## A5 · St. John's, Greenbriar and the age gap (14:45 to 18:15 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the buildings full of people who needed help to move, and the finding no competitor tells: older people lost their lives at four times the rate.
- **Question:** why did buildings that stood, or had a plan, still lose people, and who were they?
- **Reveal:** St. John's towers stood but did not protect everyone: 12 impact-related, 4 in intensive care, with 14 as the all-causes count, each with its base. Condition Gray started when the head nurse verified sirens; she likely heard only the second round. Greenbriar: the center of the tornado passed over it, 19 of 95, plan to move residents to inner hallways, people in the hallway buried. Meadows: two, in an EF-1 wind zone. Then Finding 47: about 8 per thousand aged 60 and over against 2 per thousand under 60, and it holds after removing every hospital and nursing home death.
- **Visual event:** [RS] the age-gap bar pair, 8 against 2 per thousand, then the hospital and nursing-home dots removed and the gap staying. Counter visit 3: "INSIDE A BUILDING 135 of 135" over "BELOW GROUND, NONE FOUND", about 5 s.
- **Exit hook:** "NIST wrote sixteen recommendations. Some made it into the codes. Some didn't."
- **Comments answered:** "the only tangible building standing was the hospital." (58 likes); "Being in the upper floors, if you couldn't get downstairs fast enough, your best course of action was to go to the midmost location..." (671 likes); "I was in the greenbrier nursing home when it happened." (193 likes).

**Segments:**

### A5-S1 · narration
**Picture:** the FEMA still "St. John's Regional Medical Center is a total loss", 24 May 2011, credit "Jace Anderson/FEMA" (FEMA use guidelines checked before use; no news pull), then a NIST ground photograph of the towers (credit line checked). Chips "183 INSIDE", then "HOSPITAL FOR 140,000", then "4 TIMES THE RATE". Source line "NIST Sec. 1.2".
> This is St. John's Regional Medical Center. A hundred eighty-three patients and staff were inside that evening. And one group of people in Joplin was lost at about four times the rate of people under sixty.

**Rows:** [C8: 183] · [C9: care for 140,000 area residents] · [C29: about 8 against 2 per thousand, so "about four times"; the comparison group is people under sixty]

*([loop L9 open]: which group? Paid in A5-S8.)*

### A5-S2 · narration
**Picture:** a drawn hallway, beds rolled in from the rooms; label "Condition Gray". Then a clock "5:38 PM", and a chip "5 TO 7 MINUTES", source chip "before the tornado hit the hospital · NIST Sec. 4.4.2". Source line "NIST Sec. 1.2 · Sec. 4.4.2".
> The hospital had a plan called Condition Gray. Once the head nurse confirmed the tornado sirens were sounding, staff moved patients into the hallways. The head nurse only remembered one siren, and it was most likely the second one, at five thirty-eight. So staff had five to seven minutes before the tornado hit the hospital. Was that enough?

**Rows:** [C10] · [C11]

*([loop L6 closes].)*

### A5-S3 · narration
**Picture:** the comment card "Being in the upper floors, if you couldn't get downstairs fast enough, your best course of action was to go to the midmost location..." (671 likes). Then a NIST ground photograph of the generator building (credit line checked). Chip "ABOUT 170 MPH", source chip "estimate · EF-4 range · NIST Sec. 4.6.2.1". Then the real clip: the Weather Channel show re-upload, YouTube 6nX7J8_mZpE (research/comment-beats.json; its viewers talk about St. John's), a few seconds of the hospital towers after the storm if the transcript and frames have them; provenance row, chaser-footage check and Content ID risk at sourcing. If it has no usable St. John's shot: CLIP NEEDED: moving footage of the St. John's towers after the storm (public domain FEMA first).
> Then the doors blew open down those hallways, and people there remembered everything flying from one end of the hall to the other. The wind on the hospital towers was around a hundred seventy miles an hour, and the building with the backup generators was demolished.

**Rows:** [C12] · [C13: 170 mph estimate] · [C14: the generator building]

### A5-S4 · narration
**Picture:** the comment card "the only tangible building standing was the hospital." (58 likes). Then the towers on the map, twelve dots, four marked "ICU". Chips "12 FROM THE STORM", then "7 LOST LATER, ELSEWHERE". Source line "12 impact-related · Finding 42 · Table 4-3 · 14 all causes · Table 4-1".
> One comment says the hospital was the only building left standing. The towers did stay up, but did they protect everyone inside? Twelve people at St. John's were lost to that storm, and four of them were in intensive care. Seven of the twelve were lost later, in other hospitals.

**Rows:** [C1: Finding 42] · [C6: seven injured at SJRMC, died later at another hospital] · [C2, C7: 14 all causes, on screen only, per the hospital CONFLICT]

*([A5-Q1 open]: did the windows matter? Paid in A5-S5.)*

### A5-S5 · narration
**Picture:** a NIST photograph of the West Tower (credit line checked), the fifth floor highlighted, its windows intact against broken ones below. Chip "IMPACT WINDOWS HELD". Source line "NIST Finding 18".
> And did the windows make a difference? Up on the fifth floor, the impact-resistant windows mostly held. Most of the regular windows broke.

**Rows:** [C15]

*([A5-Q1 paid]. Plants A6-S5.)*

### A5-S6 · narration
**Picture:** the comment card "I was in the greenbrier nursing home when it happened." (193 likes). A NIST ground photograph of the Greenbriar site (credit line checked). Our drawing of a one-story building, the inner hallway lit. Chip "19 OF 95 LOST". Source line "NIST Sec. 1.2 · Sec. 4.4.4 · Sec. 4.6.2.2". On "buried in rubble" a source chip "media reports · CDC interviews · where the 19 were: not known (NIST)".
> Then there's the Greenbriar nursing home. The center of the tornado went right over it. Ninety-five people were inside, and nineteen were lost. The plan was to move residents into the inner hallway and close their room doors against flying glass. Accounts afterward say people in that hallway were buried in rubble.

**Rows:** [C17: 19 of 95; "one-story building", walls not described, per the Greenbriar CONFLICT] · [C19] · [C20] · [C21]

### A5-S7 · narration
**Picture:** the map: a second nursing-home outline at the edge of the path, a pale wind-zone band labelled "EF-1". Chip "EF1 WINDS · 2 LOST". Then counter visit 3: the glass card top right, "INSIDE A BUILDING 135 of 135" over "BELOW GROUND, NONE FOUND", about 5 s, source line "NIST Table 4-3 · impact-related · Finding 46".
> There was a second nursing home, Meadows Healthcare, where the winds were only EF1 strength, and two people there were still lost after the storm. So how do you lose two people in winds that were only EF1? One possibility is that people who were already frail might not get through even a weaker hit.

**Rows:** [C25: two deaths after the storm, timing not given per the Meadows CONFLICT] · [C26: EF-1 zone] · [C27] · [C6, C23, T11: 102 + 12 + 19 + 2 = 135, Table 4-3]

### A5-S8 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. Chips "60 AND OVER: 8 IN 1,000", then "UNDER 60: 2 IN 1,000", source chip "NIST Finding 47".
> If you were sixty or older in Joplin, about eight in every thousand people your age were lost. If you were under sixty, it was about two.

**Rows:** [C29]

*([loop L9 closes].)*

### A5-S9 · narration
**Picture:** [RS] [VE] our bar pair, 8 against 2 per thousand; then the hospital and nursing-home share drains out of the taller bar and the gap stays. Chip "THE GAP STAYS". Source line "NIST Finding 47".
> You might think the hospital and the nursing homes are pulling that number up. They aren't. NIST took out every life lost in the hospital and the nursing homes, and the gap was still there. So why were older people lost at that rate?

**Rows:** [C30]

*([A5-Q2 open]: why? Paid in A5-S10.)*

### A5-S10 · narration
**Picture:** the NIST page, Finding 47, the three factors underlined one by one; then the NWS page, "elderly, infirm, or disabled". Chips "LESS WORD", "LESS HELP", "HARDER TO RECOVER". Source lines "NIST Finding 47" and "NWS Assessment, Finding 2d".
> NIST doesn't say for sure. The warning may not have reached older people as fast. They might have had fewer people around to help. Or their bodies couldn't take the hit, or recover from it. And older and disabled people need more time, or a hand, to get to shelter.

**Rows:** [C31] · [C37]

*([A5-Q2 paid].)*

### A5-S11 · narration
**Picture:** a recommendation board, sixteen tiles, all grey. Chip "16 RECOMMENDATIONS". The bed drops out on the last word.
> NIST wrote sixteen recommendations after the Joplin tornado. Some made it into the building codes. Some didn't.

**Rows:** [R1]

*([loop L7 open]. Paid in A6.)*

---

## A6 · What changed and what did not (18:15 to 21:00 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** what NIST asked for, what the national code bodies adopted, and what the supplied records do not show.
- **Question:** would a store, an apartment block or a nursing home in the path today have something below or around its people?
- **Reveal:** NIST's sixteen recommendations; Recommendation 7, shelters in multi-family, mercantile, school and assembly buildings. Adopted: tornado loads in ASCE 7-22; under the model building code (Section 423, since the 2015 IBC) ICC 500 shelters are required for new schools and emergency response buildings in the highest tornado zone, with the 2018 editions adding the school-campus change; FEMA and NIST list nothing for new stores or apartments. Joplin's school district has built 14 FEMA-backed safe rooms since 2011. Mercy says its new hospital has a window system designed to withstand 250 mph winds. As of NIST's 2018 review and the Weather Service's siren FAQ, there is still no national standard for sounding sirens; in 2011 there was none, and no national all-clear protocol. The NWS asked for a non-routine warning and fewer perceived false alarms.
- **Visual event:** a recommendation board: Recommendations 7, 8 and 13 ticked where adopted, left open where the sources say nothing.
- **Exit hook:** "The rule that took hold covers new schools and emergency buildings. On May twenty-second, 2011, Joplin High School and East Middle School were empty. Most of the people Joplin lost were indoors that evening: at home, at the store, in church, in the hospital and in nursing homes." (A6-S7; R13, B40, B42; no mirrored callback)
- **Comments answered:** "By the way, Joplin is thriving as of now. They're rebuilding prettier buildings, preparing more public tornado shelters..." (3,600 likes); "I wonder why commercial buildings and residential homes like at 15:15 don't have mandatory shelters" (28 likes); "Asked a nurse why the windows looked a little weird and she told me they were rated for 250mph winds" (482 likes).

**Segments:**

### A6-S1 · narration
**Picture:** the recommendation board; tile 7 lifts out. The NIST page, Recommendation 7, underlined, including "located in tornado hazard areas". Then the NIST ground photograph of the Walmart refuge area from A4. Chip "RECOMMENDATION 7". Source line "NIST Sec. 5.2.2, Recommendation 7".
> The one that matters most here is Recommendation seven. NIST asked for tornado shelters in apartment buildings, stores, schools and places where crowds gather, old and new, in tornado-prone areas. The safe spots in the big stores hadn't done the job they needed to. So does any building code ask for those shelters now?

**Rows:** [R3: Recommendation 7, in tornado hazard areas] · [R4: inadequate performance of the best available refuge areas]

*([loop L7 closes]; [loop L10 open]: does any code ask for them now? Paid in A6-S3 and A6-S4.)*

### A6-S2 · narration
**Picture:** the comment card "By the way, Joplin is thriving as of now. They're rebuilding prettier buildings, preparing more public tornado shelters..." (3,600 likes). Our own drawing of a school safe room, made from the FEMA case study's description (no FEMA photograph exists on that page). Chips "14 SAFE ROOMS", then "250 MPH". Source line "FEMA case study, updated Jul 30, 2024". CLIP NEEDED: moving footage inside a Joplin school safe room (public domain FEMA first; research/ names only the FEMA case study page, which has no video).
> One comment says Joplin is building more public tornado shelters, and it's partly right. Since 2011, the Joplin School District has built fourteen safe rooms, made to take winds up to two hundred fifty miles an hour. And if you live nearby with nowhere else to go, you can use them.

**Rows:** [FEMA case study "Schools in Joplin, Missouri stand up to tornadoes by building safe rooms" (updated 30 Jul 2024); FEMA release 20 Feb 2020; factcheck-acts row A6-S4 and factcheck-A4-Z1 row A6-S2]

### A6-S3 · narration
**Picture:** our map of the United States: the parts of twenty-two states that hold the highest tornado zone fill in. Our own redrawn safe-room diagram (no P-361 figure cleared). Chips "ASCE 7-22", then "22 STATES · NEW SCHOOLS", then "MINIMUM SIZE · MAX WALKING DISTANCE" (moved off the spoken line). Source lines "ASCE 7-22 · NIST Impacts page" and "IBC Section 423 · FEMA Recovery Advisory 1, Feb 2023".
> Some of it did change. Tornado loads made it into the engineering standard most building codes rely on. And the model building code now requires a storm shelter in new schools and emergency buildings in the worst tornado zone, which covers parts of twenty-two states.

**Rows:** [R12: ASCE 7-22] · [R13: parts of 22 states] · [R16: capacity and travel distance] · [FEMA Recovery Advisory 1, factcheck-acts row A6-S3]

### A6-S4 · narration
**Picture:** the comment card "I wonder why commercial buildings and residential homes like at 15:15 don't have mandatory shelters" (28 likes). The board: tile 7 half lit, "stores · apartments" left grey. Chip "STORES, APARTMENTS: NOTHING LISTED". Source line "FEMA Recovery Advisory 1 · NIST news, Jul 2024 · ICC 2024 IBC, 423.4".
> So what about a new store, or a new apartment building? There's still no shelter rule for those on the list. And stores and homes are where most of the people inside were lost.

**Rows:** [FEMA, NIST, ICC summaries, factcheck-acts row A6-S3] · [T22: 59 percent residential, 41 percent non-residential of the 135; Table 4-3 rows]

*([loop L10 closes].)*

### A6-S5 · narration
**Picture:** the comment card "Asked a nurse why the windows looked a little weird and she told me they were rated for 250mph winds" (482 likes). The NIST photograph of the old West Tower's fifth floor from A5, with a text card over it carrying Mercy's own words (no photograph of the new hospital): "a window system designed to withstand 250 mph winds · Mercy". Chip "DESIGNED FOR 250 MPH". Source line "mercy.net, Joplin tornado history".
> Remember those fifth-floor windows at St. John's? Mercy says the new hospital it opened in 2015 has a window system designed for two hundred fifty mile-an-hour winds.

**Rows:** [C15] · [mercy.net history page, factcheck-acts row A6-S5: a design claim, never "rated for", never "all windows"]

### A6-S6 · narration
**Picture:** our own drawn siren icon (no NOAA graphic cleared). Chips "NO NATIONAL STANDARD · 2011", then "STILL NONE AS OF 2018", source chip "NIST TN 2008"; the NWS siren FAQ on the source line with no date claim. Then the NWS page, Recommendation 2, underlined. Source line "NIST Finding 39 · NWS Assessment, Recommendation 2".
> And what about the tornado sirens? In 2011, there wasn't a national standard for how a town sounds them, and there wasn't a national all-clear signal either. As of 2018, there still wasn't a standard. The NWS asked for something simpler: warnings in tiers, based on impact, and an out-of-the-ordinary warning for the violent tornadoes.

**Rows:** [S34, R24: 2011] · [NIST TN 2008 (Aug 2018), factcheck-acts row A6-S6; NWS siren FAQ undated, per factcheck-A4-Z1 row A6-S6] · [R21, R22, R23]

### A6-S7 · narration
**Picture:** a NIST ground photograph of Joplin High School (credit line checked), chip "EMPTY THAT EVENING". Then the real clip: the school CCTV video re-upload, YouTube 64covicCcIY (research/comment-beats.json; comments-for-writer.md "school CCTV video"), a few seconds of empty school halls as the storm hits, its own sound, no narration over its peak. Confirm which school it shows before any caption names one (a viewer there says the tornado did not hit that school); provenance row and claim risk checked at sourcing. Then the master map with the 135 dots, chip "MOST WERE INDOORS" (the spoken list of places is cut per the acts grade; the map carries it). The bed drops out on the last word.
> The rule that took hold covers new schools and emergency buildings. But on May twenty-second, 2011, Joplin High School and East Middle School were empty.

**Rows:** [R13] · [B40: no one in Joplin High School] · [B42: East Middle School not occupied] · [T3: 135 of 155 inside structures]

---

## Z1 · Close (21:00 to 22:00 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** answer the dominant question in the last 30 to 60 s, a fact with a dated forward window, then the signature line.
- **Question:** (answered) the siren record matched what NIST found, not what the town believed, and the buildings people went to had nothing below them.
- **Reveal:** the record against the belief, one last time, then the forward window.
- **Visual event:** the master map, all 135 dots, the empty below-ground row.
- **Exit hook:** none (end card).
- **Comments answered:** none (no mirrored callback).

**Segments:**

### Z1-S1 · narration
**Picture:** the calendar strip one last time: grey Monday ticks, four red marks; the warnings strip below it, separate. Chips "ONCE A YEAR SINCE 2007", then "THE FALSE ALARMS: WARNINGS". No comment card.
> So did the tornado sirens lie? No. Outside that Monday test, Joplin's sirens went off about once a year since 2007, if that. The tornado warnings were a different count, and that's where the false alarms were.

**Rows:** [S2, S5] · [S10, S28]

*([loop L1 closes].)*

### Z1-S2 · narration
**Picture:** [RS] the master map, all 135 dots, the empty below-ground line. Chips "135 INDOORS", "NONE FOUND BELOW GROUND", "8 IN 10: NO BASEMENT". Source lines "135 of 155 impact-related · NIST Finding 40", "no evidence any were underground · Finding 46", "82% of homes · no basement · Finding 20".
> A hundred thirty-five of the people the Joplin tornado took were inside a building. NIST found no evidence that any of them were underground. And most homes in Joplin had no basement.

**Rows:** [T3] · [H5] · [H1]

### Z1-S3 · narration
**Picture:** the recommendation board, tile 7 half lit. Chip "2027 BUILDING CODE". Source line "ICC store page, Oct 2026".
> The 2027 edition of the International Building Code is coming out now, and whether it widens the shelter rule is the thing to watch.

**Rows:** [ICC store page for the 2027 IBC, factcheck-acts row Z1-S3; factcheck-A4-Z1 row Z1-S3] [verify: re-check 2027 IBC shelter rules (Section 423, Group M and R) the week of render]

### Z1 signature line (not written here: DESIGN.md "Signature closing footnote"; Paul on camera, full frame)
