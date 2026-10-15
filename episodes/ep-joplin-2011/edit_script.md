# ep-joplin-2011 · edit_script.md (draft 1, 15 Oct 26: H1, T1 and I1 in full prose; acts A1 to A6 and the close Z1 as chapter cards with planned segments, no prose yet)

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
- Numbers are spoken the way an American says them at a kitchen table, spelled out for the voice: "a hundred thirty-five", "a hundred sixty-one", "twenty-five", never "one hundred thirty five of the one hundred fifty five". One count per sentence; where a ratio is needed, the plain share ("eighty-seven percent") or the screen carries the second number. Never "one thirty-five" (reads as a clock time). Years stay digits. (Owner, 15 Oct 26.)
- Source qualifiers stay off the spoken line and go on the on-screen source line with the exact base and finding: "in the investigators' count", "who lost their lives to its impact", "not one person the investigators could place", "NIST found". The spoken line stays plain and never claims more than the source: "none below ground" means those the tornado took. The locked claim lives in the header and on screen; spoken, it is said plainly. (Owner, 15 Oct 26.)
- No start times beyond `structure.md`'s plan; real times wait on the voice probe.

---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one, said like a man who is tired of the myth. Popfig inside the first second, top left: "Joplin, Missouri · May 22, 2011". No comment card, no other video, no like count. On "dark clouds" a small chip: "many residents to the NWS · Finding 2b". On "once a year" a second chip under Paul: "outside the weekly test · at most · since 2007 · NIST Finding 31". Sound: the civil-defense siren, low and distant, cut on his last word. Cut out on that word.
> Joplin residents said the sirens went off all the time, even for dark clouds, but outside a weekly test, those sirens sounded about once a year.

**Rows:** [S17: "Many noted ... hear sirens all the time and [sirens] go off for dark clouds", NWS Finding 2b] · [S5: weekly test] · [S2, S4: "once per year (at most)" since 2007, not including the weekly test]

## H1 alternatives (the owner picks one; the pick above is H1-S1, 26 words; all comment-free; any pick keeps the H1-S1 chips so "at most", "since 2007" and "Finding 31" are on screen)
- Alternative 1 (26 words): "Plenty of Joplin residents told the Weather Service the sirens went off all the time, but outside a weekly test, they sounded about once a year." Rows: S17, S5, S2. ("Plenty" matches the NWS "a large number of participants".)
- Alternative 2 (24 words, the twist first): "More than eight in ten of the people the Joplin tornado took were already indoors, and investigators found no sign any were below ground." Rows: T3, T7, H5. Screen: "135 of 155 impact-related · Finding 40" and "no evidence any were underground · Finding 46". (Off the title, and the tail would need rewriting.)
- Alternative 3 (25 words): "People in Joplin said they heard the sirens so often they quit listening, but outside a weekly test, those sirens sounded about once a year." Rows: S17 ("bombarded with [sirens] so often that we don't pay attention"), S16, S5, S2.
- Why the pick (the grader's ship line, made true): the belief is in the residents' own words to the Weather Service, "all the time" sets up the direct contrast with "about once a year", "a weekly test" needs no explaining to a cold viewer, and "those sirens" keeps the pronoun off "dark clouds". "Joplin residents said" names who said it (many residents, NWS Finding 2b) instead of "Joplin swore" or an unnamed crowd. The hook never says the sirens were not the problem.

---

## T1 · Hook tail (0:08 planned)

### T1-S1 · narration
**Picture:** hard cut on the first word, never black: a NIST ground photograph of a flattened residential street (NIST NCSTAR 3, figure to pick at sourcing; its caption must place it in Joplin's damage path; never an aerial marked "Used with permission"). On "a hundred sixty-one" the number lands: "161 lives lost". Source line: "NIST count, Missouri State Police list · Finding 28". One bed swell, no siren.
> The tornado took a hundred sixty-one lives.

**Rows:** [T1: 161, base Missouri State Police list, NIST Finding 28]

### T1-S2 · narration
**Picture:** our own master map of Joplin, first appearance: the six-mile damage path in grey. Dots light inside building outlines on the first sentence; a thin line under the map, labelled "below ground", stays empty on the second. Source lines: "135 of 155 impact-related · inside a structure · NIST Finding 40" and "NIST found no evidence any were underground · Finding 46".
> Most of them were indoors when it hit, and the investigators found no sign any of them was below ground.

**Rows:** [T3, T7: 135 of 155 and 135 of 161, so "most" holds on both bases] · [H5: Finding 46, "no evidence ... underground"]

### T1-S3 · narration
**Picture:** push in on the empty "below ground" line, then cut to our own cross-section of a one-story house on a slab or crawl space (never drawn as a solid block), label "no basement · 82% of Joplin homes · NIST Finding 20". On "having one" a second, smaller cross-section with a basement slides in beside it, its stairs lit and empty. Bed drops to near silence on the last word.
> Most homes in Joplin had no basement, and having one didn't always mean you were down in it.

**Rows:** [H1: 82 percent lacked basements] · [H22, H8: 3 of 71 had basement access, at least 2 not in it; B31, B33: the theater basement, the Macadoodles cellar] (no causal claim; plants the A3 hinge without spending the three-of-seventy-one count; basements that were used held, per Finding 46)

*([loop L8 open]: what happened where there was a basement. Closes in A3 (the three with basement access) and A4 (the theater stairs, the Macadoodles cellar).)*

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · Intro: the day, the place, the two numbers (0:20 planned)

### I1-S1 · narration
**Picture:** our own map of the United States, pushing in to the four-state corner where Missouri, Kansas, Oklahoma and Arkansas touch, then to Joplin, label "Joplin, Missouri · population 50,150 · 2010 Census (via NIST)". A touchdown dot lands just southwest of the city limits with a clock "about 5:34 PM" and the source line "NWS timeline: approximate touchdown". The path draws west to east across the city on the second sentence, width shown as a band "up to 1 mile". Labels "6 miles in Joplin" on the path and "about 15 minutes in the city", source line "NIST Sec. 1.3" under both (the spoken line carries only the minutes; Act 2 never labels 5:38 to 5:50 as 15 minutes).
> On Sunday evening, May twenty-second, 2011, a tornado touched down just outside Joplin, Missouri, a town of about fifty thousand. It cut across the city in about fifteen minutes.

**Rows:** [NIST Sec. 1.2: "On Sunday, May 22, 2011"; E13: approximate touchdown, southwest of the city limits] · [X21: 50,150, so "fifty thousand" said round; NIST Sec. 1.1: southwest Missouri] · [W3, W8: six miles, about fifteen minutes] · [W3, W6: "as much as a mile wide", "up to a mile wide in some places"]

### I1-S2 · narration
**Picture:** the master map holds. Twenty five siren icons appear at once, placed from NIST Fig. 4-2: twenty three inside the city outline, one at Duenweg and one at the Village of Airport Drive, just outside it. Source line: "25 sirens in Joplin's outdoor system · 23 in the city · NIST Sec. 4.3.1". A calendar strip slides in under the map: a grey tick on Mondays, labelled "test · 10 AM · 1 minute · weather permitting".
> Joplin's warning system ran twenty-five outdoor sirens, and the city tested them most Monday mornings.

**Rows:** [S2: 25-siren system; NIST Sec. 4.3.1: 23 in the city, 1 in Duenweg, 1 in Airport Drive] · [S5: Mondays, 10 a.m., 1 minute]

### I1-S3 · narration
**Picture:** the calendar strip stretches to 2007 to 2011; the grey Monday ticks fill it. Three red marks stand out, one a year: January 18, 2007; May 10, 2008; May 8, 2009. Then a gap to May 22, 2011. Source line: "once a year at most since 2007 · NIST Finding 31 and Sec. 4.3.4, from the county emergency manager". No label calls them wind events.
> Outside that test, they went off about once a year, if that.

**Rows:** [S2: Finding 31] · [S4, S6, S7: the rate and the dates, according to the Joplin-Jasper County emergency manager] (per the S9 CONFLICT: not called wind events)

### I1-S4 · narration
**Picture:** the Weather Service assessment's own page, the residents' words underlined as the narrator speaks: "hear sirens all the time and [sirens] go off for dark clouds". Source line "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b". The narrator speaks the line; no actor's voice.
> But plenty of people told the Weather Service the sirens went off all the time, even for dark clouds.

**Rows:** [S17: "Many noted..."]

### I1-S5 · narration
**Picture:** the NIST report's cover (NIST NCSTAR 3, public domain), then a name card "NIST · National Institute of Standards and Technology · federal investigators". The master map returns and dots begin to land, one location type at a time, each with a small on-screen label (not spoken): houses, apartments, two big box stores, a phone store, a pizza restaurant, a lodge, a theater, two churches, a hospital, two nursing homes, and outside. Source line: "154 of 155 impact-related deaths placed · NIST Table 4-3".
> Afterward, federal investigators found out where almost everyone the tornado took was when it hit.

**Rows:** [T9, T12: Table 4-3 places 154 of the 155, so "almost every"] (labels: H26, B45, C6, C23, C25, T17; B2 "big-box stores")

### I1-S6 · narration
**Picture:** [RS] [VE] the whole map lit: 135 dots inside building outlines and 19 outside, 12 of them marked as in vehicles, with a small label "154 placed · 1 not placed · location unknown"; the empty "below ground" line under the map. On "a hundred thirty-five" the figure lands large: "135 of 155 impact-related · inside a structure · 87% · NIST Finding 40". On "below ground" the figure "0" lands on the empty line: "NIST found no evidence any were underground · Finding 46". Hold. The locked claim sits in the header; this line speaks it plainly, as the owner ordered on 15 Oct 26.
> A hundred thirty-five of them were inside a building, and the investigators found no sign that any of them was in a basement, or anywhere below ground.

**Rows:** [claim, angle.md, spoken plain] · [T3: 135 of 155, Finding 40] · [T17: outside 19, 12 in vehicles; T12: one death with no known location] · [H5, H6: Finding 46 and Sec. 4.6.2.2]

### I1-S7 · narration
**Picture:** the calendar strip from I1-S3 returns under the map, the grey Monday ticks dimmed and the red marks lit, small label "outside the weekly test". Then the Weather Service assessment's page, unmarked, a slow push in on the word "sirens". Source line: "NWS assessment team · interviewed over 60 survivors". The bed drops out on the last word.
> So if the sirens hardly ever went off for real, why did so many people think they never stopped? After the storm, the Weather Service interviewed more than sixty survivors.

**Rows:** [S3: residents believed in many false alarms] · [X26: "interviewed over 60 survivors"; S16] (the exit question plus one affirming line)

*([loop L2 open]: why people thought the sirens went off all the time. Closes in A1.)*

*(blackout 0.7 s)*

---

## A1 · Sirens: belief against record (1:45 to 4:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** prove the belief and the record side by side, and keep the two false-alarm numbers apart.
- **Question:** where did "all the time" come from, if the record says about once a year?
- **Reveal:** the weekly one-minute Monday test (about fifty two a year) plus about one real sounding a year since 2007, three of them dated. The false alarms were real, in a different set: 14 of 18 tornado warnings from 2005 to 2011 had no verified tornado, in line with the national 74.7 percent, and 11 of 12 in the last five years. People heard warnings and tests and filed them all under "sirens". Plus the belief in a "protective bubble".
- **Visual event:** [RS] a two-row calendar 2007 to 2011: fifty two grey test ticks a year against single red marks; a second, separate strip for the 18 warnings, 4 verified.
- **Exit hook:** "On May twenty-second, the sirens went off twice, and people couldn't agree on what the second one meant."
- **Comments answered:** RODALCO2007 ("no one is paying any attention to the sirens going off", 3,000 likes; its first and only card, at A1-S3); "The sad part is nobody knew what really was coming that day." (824 likes).

**Planned segments:**
- A1-S1 · narration · opens straight on what people told the Weather Service, no Paul line at the seam: sirens for thunderstorms, sirens that only meant "a little more water in the gutter", people "bombarded" by them · S17, S18 · NWS assessment page, lines underlined, then a NIST ground photograph of a Joplin street.
- A1-S2 · narration · stakes first: one man told NIST that nine times out of ten you hear the sirens and nothing happens; he was an actor at the Stained Glass Theater, and that evening three people in that building did not make it (his words as attributed text) · S24, B25 · quote card (NIST Interview 120) over a NIST ground photograph of the theater · plants A4-S9.
- A1-S3 · narration · the RODALCO2007 card appears here, its first time on screen ("no one is paying any attention to the sirens going off", 3,000 likes, under "JOPLIN, MO, Tornado, 22 May 2011"; likes on the card, never spoken), and the record answers it: the Weather Service found most of the people it surveyed had gone numb to the sirens, and the first siren had lost some of its pull · S16, S19 · the card beside the assessment page.
- A1-S4 · graphic · the count, said once and fast (the weekly test was already spoken in I1): fifty-two tests a year against three real soundings, January 2007, May 2008, May 2009, then May twenty-second, 2011 · S4, S6, S7 · calendar red marks.
- A1-S5 · narration · plain: the investigators found no sign the sirens had a false-alarm problem, whatever people believed; "NIST Finding 31" on screen · S1, S15 · NIST page.
- A1-S6 · Paul · HC1, moved off the 1:45 seam (about 3:15): "Stick with me, because what I'm about to explain is exactly why Joplin heard rare sirens as noise." · no row · Paul full frame.
- A1-S7 · narration · the other set, a different count: of eighteen tornado warnings for Joplin from 2005 to 2011, fourteen never came with a tornado, about the national average; in the last five years, eleven out of twelve. One count per sentence; the national seventy-four point seven percent sits on screen with NIST as its source · S10 to S14 (per the S10 CONFLICT) · a second strip, separate from the siren strip.
- A1-S8 · narration · stakes: the sirens didn't sound for every warning, so the two were different counts, but people lumped them together; NIST says that distrust and confusion is one of two reasons people were slow to move that evening · S8, S28, S39, S40 · two strips side by side, never merged.
- A1-S9 · graphic · no news pull (UNVERIFIED in factcheck-acts: no source names a clip or its rights holder): a NIST Interview 58 quote card, "the announcer and the weatherman ... seemed to say the track was ... mainly north of town" (NIST Ch. 4), with the comment card "The sad part is nobody knew what really was coming that day." (824 likes) beside it · E11, E12, NIST Interview 58 · quote card over the calendar strip.
- A1-S10 · narration · the protective bubble: people said storms always split and missed Joplin; since 1950 the city itself had one EF-2 or stronger, while a hundred eighty-two hit within eighty miles (two sentences, one count each) · S23, S36, S37, S38 · our map, eighty-mile ring, a NIST ground photograph of the 2011 path over it.
- A1-S11 · narration · exit hook: "On May twenty-second, the sirens went off twice, and people couldn't agree on what the second one meant." · S27 · map with two siren rings · [loop L2 closes] [loop L3 open].

*(blackout 0.7 s)*

---

## A2 · The evening, five oh nine to five thirty eight (4:45 to 7:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** a countdown that shows the first siren sounded for a storm that never made a tornado, and the second came as the tornado entered the city.
- **Question:** what did the second siren mean to the people who heard it?
- **Reveal:** 5:09 warning for a different storm; 5:11 first siren, mainly for funnel reports in Kansas, heard as meant for the north; 5:17 the city-wide warning, no new siren; media still saying the storms were passing north; rotation from 5:29 to touchdown at 5:34; 5:38 second siren, four minutes after touchdown. Lead time: seventeen minutes to touchdown from the 5:17 warning, twenty three from the first siren. People read the second siren as worse, or as an all clear; the city had no all-clear signal. For most it was the non-routine signal that sent them to shelter.
- **Visual event:** [RS] a clock running down the master map: polygon 30 in the north, polygon 31 over the city, siren rings at 5:11 and 5:38, the touchdown dot at 5:34. Radar: NWS Assessment Appendix A, Figure 4 panel (G): KSGF 0.5 degree base reflectivity, valid 22 May 2011 22:34Z (5:34 pm CDT), credited "NOAA/NWS", no NWS logo and no third-party basemap; panel (H) storm-relative velocity at the same time if wanted; never NIST Fig. 2-7 as "NOAA" (factcheck-acts, A2 radar CONFIRMED).
- **Exit hook:** "At five thirty-eight, most people went for the best spot they had. The investigators went back later and looked at what was underneath it."
- **Comments answered:** "Residents of Joplin had plenty of warning time." (1,800 likes); "even the best of technology wouldnt have helped alert the people on time" (2,500 likes); "Joplin didn't receive a tornado emergency because of how fast it developed." (1,500 likes).

**Planned segments:**
- A2-S1 · narration · one-thirty, the tornado watch; four thirty-three, the Weather Service calls the county emergency manager about storms to the west · E1 (NWS time, per the E1/E2 CONFLICT), E3 · clock graphic.
- A2-S2 · narration · five-oh-nine, a tornado warning for the northeast corner of town, for a storm that never made a tornado ("polygon 30" on screen only) · E4, E5 · polygon on the map.
- A2-S3 · narration · five-eleven, the first siren, three minutes, set off mostly by funnel reports over in Kansas; people figured it was for the storm up north · E6, E8, E8b · siren ring, Kansas arrow.
- A2-S4 · narration · few signs outside; the NIST interviewee who looked out, saw nothing, and went back to finish eating (attributed text) · E7, E34 · quote card, NIST Interview 108.
- A2-S5 · narration · five-seventeen, a warning over the whole city, and no second siren, probably because the first had gone off six minutes earlier ("polygon 31" on screen only) · E9, E10 · polygon on the map.
- A2-S6 · graphic · no TV pull (UNVERIFIED in factcheck-acts): the NIST sentence as on-screen text, "the media continued to report on storms said to be passing to the north and missing Joplin, or moving away from the City", then the NIST Interview 58 quote card · E11, E12, NIST Interview 58 · NIST page. The "National Weather Service computer projections" comment card is cut: no source supports it.
- A2-S7 · graphic · lead time, one number per sentence: seventeen minutes from the five-seventeen warning to touchdown; twenty-three from the first siren; the screen adds nineteen to the city line and NIST's "close to 20 min" · E21, E22, E23 · comment card "Residents of Joplin had plenty of warning time." (1,800 likes).
- A2-S8 · narration · rotation from five twenty nine to touchdown at five thirty four, rain-wrapped, hard to see until close; then the safe line: "The Weather Service issued no Tornado Emergency headline for Joplin proper; the tornado formed fast on the city's edge and its size was not clear until it was well into the city." Never "no emergency was declared by anyone" · E25, E13, E32, NWS Assessment paragraph before Finding #8 and footnote 10 · NWS Assessment Appendix A, Figure 4 panel (G): KSGF 0.5 degree base reflectivity, valid 22 May 2011 22:34Z (5:34 pm CDT), credited "NOAA/NWS", no NWS logo and no third-party basemap; panel (H) storm-relative velocity at the same time if wanted; never NIST Fig. 2-7 as "NOAA" (factcheck-acts, A2 radar CONFIRMED) · comment card "Joplin didn't receive a tornado emergency because of how fast it developed." (1,500 likes), answered: the NWS gives the same reason.
- A2-S9 · Paul · turning point: "Five thirty-eight. The tornado was already inside the city when the sirens went off a second time." (19 words; "4 minutes after touchdown · NIST Finding 35" on screen) · E14, E15 · Paul full frame.
- A2-S10 · narration · the rule was one siren per alert, so the second one was out of the ordinary, and for most people that's what finally got them moving · E20, E19, E37 · assessment page.
- A2-S11 · narration · what the second siren meant: some heard it as worse, some as the all clear, and the city had no all-clear signal at all · S25, S26, S33 · two labels on the siren ring · [loop L3 closes].
- A2-S12 · narration · exit hook: "At five thirty-eight, most people went for the best spot they had. The investigators went back later and looked at what was underneath it." · H23 · map, the residential area lit · [loop L4 open].

*(blackout 0.7 s)*

---

## A3 · Homes with nothing underneath (7:45 to 11:15 planned; book ad inside)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the first and largest group on the map: 71 in houses and apartments, in a city where 82 percent of homes had no basement and no public shelter existed.
- **Question:** what was under the best place they had?
- **Reveal:** 82 percent of homes had no basement; no community shelter or safe room in city or county. 59 in single-family homes, 54 of them in homes rated demolished, 50 in one-story homes; 12 in apartments, all above ground. After the ad: only 3 of the 71 had a basement they could reach, and at least two of the three were not in it when the storm hit. Survivors in the EF-4 zone: 11 of 27 in basements, 15 in interior rooms. A neighborhood of early-1980s ranch homes with basements: heavy damage, nobody lost.
- **Visual event:** [RS] the 71 dots light on the map in house outlines; a cross-section of a one-story house with an empty space where a basement would be. Counter visit 1: "INSIDE A BUILDING 71 of 135" over "BELOW GROUND 0", about 5 s.
- **Exit hook:** "The big stores had something the homes didn't: a safe spot, and staff who knew where it was."
- **Comments answered:** "most people that took shelter in their homes" (1,100 likes); "my step dad went to the center most closet in the house, threw everything out into the hallway" (1,600 likes); "How does anyone survive this?" (431 likes).

**Planned segments:**
- A3-S1 · narration · eight in ten Joplin homes had no basement ("82% · Finding 20" on screen) · H1 · cross-section graphic · [loop L4 closes] [loop L8 closes].
- A3-S2 · narration · and there was nowhere public to run: no community shelter or safe room in the city or the county · H3, H4 · map, no shelter icons anywhere.
- A3-S3 · narration · fifty-nine people lost in single-family homes, almost all in houses the storm flattened, most of them one-story ("51 homes · 54 demolished · 50 one-story" on screen, not spoken) · H9, H10, H11 (Table 4-3 base, per the H25/H26 CONFLICT) · dots in house outlines · ends on the plant: "Some homes in the path did have a basement, and the investigators checked whether anyone the storm took had made it down." · H7, H22 · [loop cta-hinge planted early].
- A3-S4 · narration · twelve more in three apartment complexes, all above ground, wood frame, nowhere protected; a woman at the Somerset who ran out and rode it out under the staircase with her neighbors · H19, H20 · NIST ground photograph.
- A3-S5 · narration · the survivors NIST talked to in the worst zone: twenty-seven people; eleven were in basements, the rest in closets, hallways and bathrooms (the split of fifteen on screen) · H13, H14 · comment card "my step dad went to the center most closet in the house..." (1,600 likes).
- A3-S6 · graphic · why the houses came apart: the joints between roof, walls and floor gave way, not the boards themselves · H30 · exploded house diagram, our own.
- A3-S7 · narration · the few people with a shelter built into the house came through, and very few had one · H16, H18 · NIST ground photograph.
- A3-S8 · Paul · cta-hinge tease, the paradox spoken (22 words): "Three of the seventy-one people lost at home had a basement they could get to, and they still did not make it." · H22 · Paul full frame · [loop cta-hinge open].
- (book ad, 24.4 s, its own voice; planned 10:30 to 10:54.4)
- A3-S9 · narration · payoff in the first words: "At least two of them never got down there before it hit." Nobody could say where the third one was ("NIST · circumstances unknown" on screen) · H8, H22 · basement stairs drawn, empty · [loop cta-hinge closes].
- A3-S10 · narration · and a neighborhood of early-eighties ranch houses with basements got hit hard, and nobody there was lost · H15 · map, a pocket with no dots.
- A3-S11 · graphic · counter visit 1: INSIDE A BUILDING 71 of 135 · BELOW GROUND 0 · H26, H19 (Table 4-3 rows) · glass card top right, about 5 s.
- A3-S12 · narration · exit hook: "The big stores had something the homes didn't: a safe spot, and staff who knew where it was." · B2 · map, commercial strip lit · [loop L5 open].

*(blackout 0.7 s)*

---

## A4 · Stores, churches, restaurants (11:15 to 14:45 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the refuge areas that existed, and why they did not hold; plus the one cellar that did.
- **Question:** did the refuge areas protect the people inside them?
- **Reveal:** NIST found no evidence the designated refuge areas helped. Walmart: fifty to sixty in the refuge area, the wall came in onto it, a D-shaped pocket, three lost, location uncertain. Home Depot: thirty five in the training room survived as the panels fell outward; eight lost walking along the front wall. Pizza Hut cooler, five lost; they argued whether the second siren was an all clear. Dillon's cooler: thirty five, all survived. Stained Glass Theater: the only basement among the eight buildings, one person wide at the stairs. Two churches, seven lost. Then Macadoodles: twelve people twenty feet down in a concrete wine cellar, all walked out.
- **Visual event:** [RS] NIST ground photographs of the Walmart and Home Depot; the D-shaped pocket drawn over the Walmart floor plan; the Macadoodles cellar as a cross-section, twelve figures below the line. Counter visit 2: "INSIDE A BUILDING 102 of 135" over "BELOW GROUND 0", about 5 s.
- **Exit hook:** "One building in the path was full of people who couldn't move themselves, and its plan waited on a siren."
- **Comments answered:** "what about that Home Depot? Think that'd be a bad spot?" (1,500 likes) with "Home Depot would NOT have been a good spot ... eight people died there." (1,100 likes); "At the Walmart and home depot it wasn't mentioned that every single person who chose to leave the stores instead of taking shelter died." (1,100 likes).

**Planned segments:**
- A4-S1 · narration · HC2: "Stick with me, because what I'm about to explain is exactly why the safe spots in Joplin's biggest stores didn't hold." · no row · map, commercial strip.
- A4-S2 · narration · few businesses had a basement, none had a storm shelter above ground, but most big stores and the hospital had a spot picked out · B1, B2 · map.
- A4-S3 · narration · Walmart: about two hundred people inside; staff sent folks to the layaway area at the back, fifty or sixty of them, and the outside wall came in on top of it · B5, B6, B8, B9 · NIST ground photograph.
- A4-S4 · graphic · the wall came to rest on a row of cabinets and left a D-shaped pocket; three people were lost, and nobody can say where in the store they were · B10, B7 · our floor plan · comment card "At the Walmart and home depot ... every single person who chose to leave..." (1,100 likes), answered: the record does not place the three.
- A4-S5 · narration · Home Depot: thirty-five people in the training room at the back, and the walls there fell outward, away from them; eight were lost along the front wall, just in from the lumber entrance; sixty-three of seventy-three wall panels came down (on screen) · B11, B12, B13, B14 (8 with its base, per CONFLICT) · NIST ground photograph · comment cards (1,500 and 1,100 likes).
- A4-S6 · narration · Pizza Hut: staff and customers got into the walk-in cooler, the building was flattened, and five were lost; at five thirty-eight they were arguing over whether the second siren meant all clear · B18, B19 · callback to L3.
- A4-S7 · narration · over at Dillon's grocery, thirty-five people in the produce cooler, the store flattened, and every one walked out · B20 · NIST ground photograph.
- A4-S8 · narration · the AT&T store: eleven people in the men's room, one lost; the Elks Lodge: five ran for the cooler, nobody reached it, four lost · B21, B22, B23 · map dots.
- A4-S9 · narration · the Stained Glass Theater: fifty-six people, a director who told them they could go down to the basement, stairs one person wide, about fifteen got down, three lost above ground · B24 to B31 · quote cards (NIST Interviews 121, 115).
- A4-S10 · narration · two churches, Harmony Heights and Full Gospel, seven lost between them; at Harmony Heights it was the second siren and the off-duty firefighters' radios that got people moving · B36 to B39 (7, per the B39/B50 CONFLICT) · NIST ground photograph.
- A4-S11 · narration · in every building the storm flattened, the people lost or badly hurt were above ground ("NIST Sec. 4.6.2.1" on screen) · B32, B4 · NIST page.
- A4-S12 · narration · [RS] Macadoodles: twelve people went down into a concrete wine cellar twenty feet under the floor, the building came down on top of them, and nobody got hurt · B33, B34, B35, B49 · cross-section, twelve figures below the line.
- A4-S13 · graphic · counter visit 2: INSIDE A BUILDING 102 of 135 · BELOW GROUND 0 · B45 (Table 4-3 rows) · glass card top right, about 5 s.
- A4-S14 · narration · exit hook: "One building in the path was full of people who couldn't move themselves, and its plan waited on a siren." · C10 · map, St. John's outline lit · [loop L5 closes] [loop L6 open].

*(blackout 0.7 s)*

---

## A5 · St. John's, Greenbriar and the age gap (14:45 to 18:15 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** the buildings full of people who needed help to move, and the finding no competitor tells: older people lost their lives at four times the rate.
- **Question:** why did buildings that stood, or had a plan, still lose people, and who were they?
- **Reveal:** St. John's towers stood but did not protect everyone: 12 impact-related, 4 in intensive care, with 14 as the all-causes count, each with its base. Condition Gray started when the head nurse verified sirens; she likely heard only the second round. Greenbriar: the center of the tornado passed over it, 19 of 95, plan to move residents to inner hallways, people in the hallway buried. Meadows: two, in an EF-1 wind zone. Then Finding 47: about 8 per thousand aged 60 and over against 2 per thousand under 60, and it holds after removing every hospital and nursing home death.
- **Visual event:** [RS] the age-gap bar pair, 8 against 2 per thousand, then the hospital and nursing-home dots removed and the gap staying. Counter visit 3: "INSIDE A BUILDING 135 of 135" over "BELOW GROUND 0", about 5 s.
- **Exit hook:** "NIST wrote sixteen recommendations. Some made it into the codes. Some didn't."
- **Comments answered:** "the only tangible building standing was the hospital." (58 likes); "Being in the upper floors, if you couldn't get downstairs fast enough, your best course of action was to go to the midmost location..." (671 likes); "I was in the greenbrier nursing home when it happened." (193 likes).

**Planned segments:**
- A5-S1 · narration · St. John's: a hundred eighty-three patients and staff inside, a hospital a hundred forty thousand people relied on (two sentences, one count each) · C8, C9 · NIST ground photograph · ends on the plant (pays at A5-S9, about two minutes later): "And one group in Joplin was lost at four times the rate of everybody else." · C29 · [loop L9 open].
- A5-S2 · narration · the hospital's plan, Condition Gray, moved patients into the hallways once the head nurse confirmed the sirens; she remembered hearing them once, most likely the second time, at five thirty-eight · C10, C11 · callback to L3 · [loop L6 closes].
- A5-S3 · narration · doors blew open down the hallways, winds around a hundred seventy miles an hour, and the building with the backup generators was flattened · C12, C13, C14 · NIST ground photograph · comment card "Being in the upper floors..." (671 likes).
- A5-S4 · narration · the towers stayed up and still didn't protect everyone: twelve lost to the storm itself, four of them in intensive care (fourteen counting every cause, on screen with its base) · C1, C2, C6, C7 (per the hospital CONFLICT) · comment card "the only tangible building standing was the hospital." (58 likes).
- A5-S5 · narration · on the fifth floor, the impact-resistant windows mostly held while the ordinary ones broke · C15 · NIST photograph.
- A5-S6 · narration · Greenbriar: the center of the tornado went right over it; nineteen of the ninety-five people inside were lost; the plan sent residents to the inner hallway, and the people there were buried ("one-story building", per the Greenbriar CONFLICT) · C17, C19, C20, C21 · comment card "I was in the greenbrier nursing home when it happened." (193 likes).
- A5-S7 · narration · Meadows, a second nursing home, in winds of only EF-1 strength; two people lost after the storm; NIST's reading: people already frail may not get through even a weaker hit · C25, C26, C27 (timing not given, per the Meadows CONFLICT) · map.
- A5-S8 · graphic · counter visit 3: INSIDE A BUILDING 135 of 135 · BELOW GROUND 0 · C6, C23, T11 (Table 4-3 rows) · glass card top right, about 5 s.
- A5-S9 · Paul · turning point, the age gap: "Past sixty, about eight in every thousand people in Joplin were lost. Under sixty, about two." (16 words) · C29 · Paul full frame · [loop L9 closes].
- A5-S10 · graphic · [RS] the bars; the hospital and nursing-home share removed; the gap stays · C30 · our chart, source line "NIST Finding 47".
- A5-S11 · narration · NIST's possible reasons: word didn't reach them as well, fewer people around to help, a body less able to recover; the Weather Service adds that they need more time or a hand to reach shelter · C31, C37, C38 · NIST page.
- A5-S12 · narration · exit hook: "NIST wrote sixteen recommendations. Some made it into the codes. Some didn't." · R1 · recommendation board · [loop L7 open].

*(blackout 0.7 s)*

---

## A6 · What changed and what did not (18:15 to 21:00 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** what NIST asked for, what the national code bodies adopted, and what the supplied records do not show.
- **Question:** would a store, an apartment block or a nursing home in the path today have something below or around its people?
- **Reveal:** NIST's sixteen recommendations; Recommendation 7, shelters in multi-family, mercantile, school and assembly buildings. Adopted: tornado loads in ASCE 7-22; under the model building code (Section 423, since the 2015 IBC) ICC 500 shelters are required for new schools and emergency response buildings in the highest tornado zone, with the 2018 editions adding the school-campus change; FEMA and NIST list nothing for new stores or apartments. Joplin's school district has built 14 FEMA-backed safe rooms since 2011. Mercy says its new hospital has a window system designed to withstand 250 mph winds. As of NIST's 2018 review and the Weather Service's siren FAQ, there is still no national standard for sounding sirens; in 2011 there was none, and no national all-clear protocol. The NWS asked for a non-routine warning and fewer perceived false alarms.
- **Visual event:** a recommendation board: Recommendations 7, 8 and 13 ticked where adopted, left open where the sources say nothing.
- **Exit hook:** "The rule that took hold covers new schools. On May twenty-second, 2011, Joplin High and East Middle School were empty. The people Joplin lost were at home, at the store, in church, in the hospital and in nursing homes." (A6-S7; R13, B40, B42; no mirrored callback)
- **Comments answered:** "By the way, Joplin is thriving as of now. They're rebuilding prettier buildings, preparing more public tornado shelters..." (3,600 likes); "I wonder why commercial buildings and residential homes like at 15:15 don't have mandatory shelters" (28 likes); "Asked a nurse why the windows looked a little weird and she told me they were rated for 250mph winds" (482 likes).

**Planned segments:**
- A6-S1 · narration · Recommendation 7: shelters in new and existing apartment buildings, stores, schools and places of assembly; the reason, refuge areas in big stores performed badly. Ends on the open question: "NIST asked for shelters in new stores and apartment buildings. Whether any code asks for them now is a harder question." · R3, R4 · NIST page over the NIST ground photograph of the Walmart refuge area from A4 · [loop L7 closes] [loop L10 open].
- A6-S2 · narration · stakes, one person: the 3,600-like comment says Joplin is "preparing more public tornado shelters"; partly right on the shelters, wrong on who builds them: "Since 2011, Joplin's school district has built fourteen safe rooms, made to take winds up to two hundred fifty miles an hour, and neighbors with nowhere else to go can use them." ("FEMA case study" on screen) No "more are coming" (no source) · FEMA case study "Schools in Joplin, Missouri stand up to tornadoes by building safe rooms" (updated 30 Jul 2024); FEMA release 20 Feb 2020 · comment card (3,600 likes) · visual change: a NIST 2011 ground photograph of the school site, then a FEMA photograph of a Joplin school safe room [verify: the FEMA case-study photograph is public domain, not credited to a third party].
- A6-S3 · narration · payoff: what was adopted, said as what a building in the path would have today: tornado loads in ASCE 7-22; ICC 500 shelters required in new schools and emergency response buildings across parts of twenty-two states, in the 2018 codes, with a set capacity and travel distance · R12 to R16 · our map of the twenty two states filling in, then a FEMA P-361 safe-room diagram (public domain).
- A6-S4 · narration · what the sources show, narrowly: "Today's model code wants a shelter in new schools and emergency buildings in the worst tornado zone. For new stores and apartments, FEMA and NIST list nothing." Never "no code requires it" (local amendments exist); never imply 2018 was the first shelter rule (Section 423 dates from the 2015 IBC) · FEMA Recovery Advisory 1 (Feb 2023); NIST news (Jul 2024); ICC 2024 IBC Significant Changes, 423.4; R13, R15 · comment card "I wonder why commercial buildings and residential homes ... don't have mandatory shelters" (28 likes) · [loop L10 closes].
- A6-S5 · narration · the windows: in 2011 the impact-resistant fifth-floor windows mostly held while ordinary ones broke; then "Mercy says the hospital it opened in 2015 has a window system designed for two hundred fifty mile-an-hour winds." A design claim attributed to Mercy; never "rated for", never "all windows" · C15; mercy.net Joplin tornado history page · NIST photograph of the West Tower, then the comment card (482 likes), a nurse's account the company line only partly supports.
- A6-S6 · narration · sirens: no national standard for sounding them in 2011 and no national all-clear protocol; then "As of 2018, there was still no national standard for how a town sounds its sirens." Date on screen ("as of 2018 · NIST TN 2008; NWS siren FAQ"); never "today". The Weather Service asked for a simple, tiered warning, a non-routine warning for violent tornadoes, and less perception of false alarms · S34, R24, NIST TN 2008 (Aug 2018), weather.gov/dvn/sirenFAQ, R21, R22, R23 · NOAA public domain siren or warning graphic, not a report page.
- A6-S7 · narration · exit hook, no mirrored callback: "The rule that took hold covers new schools. On May twenty-second, 2011, Joplin High and East Middle School were empty. The people Joplin lost were at home, at the store, in church, in the hospital and in nursing homes." · R13, B40, B42 · NIST ground photograph of Joplin High School, then the master map with the 135 dots.

*(blackout 0.7 s)*

---

## Z1 · Close (21:00 to 22:00 planned)

**Chapter card (copied from `structure.md`):**
- **Purpose:** answer the dominant question in the last 30 to 60 s, a fact with a dated forward window, then the signature line.
- **Question:** (answered) the siren record matched what NIST found, not what the town believed, and the buildings people went to had nothing below them.
- **Reveal:** the record against the belief, one last time, then the forward window.
- **Visual event:** the master map, all 135 dots, the empty below-ground row.
- **Exit hook:** none (end card).
- **Comments answered:** none (no mirrored callback).

**Planned segments:**
- Z1-S1 · narration · the belief against the record one last time, no comment card (no mirrored callback): the sirens went off about once a year outside the Monday test; the warnings were a separate count · S2, S5, S10 · calendar strip · [loop L1 closes].
- Z1-S2 · narration · the answer to the dominant question, plain and with no "because": "A hundred thirty-five people were inside a building. None of them was below ground. And most homes in Joplin had no basement to go to." (bases on screen: "135 of 155 · Finding 40", "no evidence any were below grade · Finding 46", "82% · Finding 20") · T3, H5, H1 · master map, all dots.
- Z1-S3 · narration · dated forward window, safe line: "The 2027 edition of the building code is coming out now, and whether it widens the shelter rule is the next thing to check." No claim that it widens the rule [verify: re-check 2027 IBC shelter rules (Section 423, Group M and R) the week of render] · ICC store page for the 2027 IBC (stamp 7 Oct 2026); R13, R15 as the 2018 baseline · recommendation board.
- Z1-S4 · Paul · the signature line per DESIGN.md "Signature closing footnote" (not written here) · Paul full frame.
