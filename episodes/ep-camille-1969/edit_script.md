# ep-camille-1969 · edit_script.md (draft 5, 22 Oct 26: H1, T1 and I1 in full prose; grader PASS 8 of 10 on draft 4, its fixes taken; acts as briefs only)

Lane: documentary (`/storm-episode`). Built on candidate 1 in `angle.md`, locked by the owner on 22 Oct 26 with arcs 2 and 3.
**Owner sign-off (22 Oct 26):** `camille_hook` = "yes" and `camille_len` = "20" in
C:\Users\Sidhartha\.claude\scratch\devq-retention\answers-eps-gates.json (saved_at "22 Oct 26 02:01:13"), on eps-gates.html #camille.
That page showed H1 and T1 in full, and I1 abridged with "...". **LOCKED:** H1-S1, T1-S1, T1-S2, and the I1 lines the page showed
word for word: I1-S6, I1-S8, I1-S9. **Not yet locked** (not shown in full, waiting on his yes): I1-S1, I1-S2, I1-S3, I1-S4 (partly
shown), I1-S5, I1-S7, I1-S10 (not shown). Facts: `research/facts-national.md` (N rows),
`research/facts-virginia-flood.md` (V rows), `research/facts-toll-people.md` (P rows); viewer comments:
`references/comment-bank.md` (the seven Camille entries, 21 Oct 26). Status: DRAFT, phases 0 to 3 only (no TTS, no sourcing, no render).

## A. Header
- **Title:** none yet. Packaging follows the angle lock (`references/angle.md` order of work).
- **Target runtime:** about 20 min (owner, `camille_len` = "20", 22 Oct 26). 4 acts of 3 to 6 min plus hook, intro, CTA and close.
  `word_budget.py` has not run: it needs two probe wavs at the shipping tempo, and this round has no TTS. Planning pace: Joplin's
  measured 182.8 wpm on the Paul clone, so about 3,300 narration words for 20 min.
- **Claim (locked, copied from `angle.md`):** Camille's Virginia flood still is not closed: fifty-seven years later the state is asking for help to name eight people recovered from the Rockfish River, and about thirty-two more from Nelson County were never found at all.
- **Dominant question:** the viewer keeps watching to find out how one night of rain took people so completely that Virginia is
  still trying to put names to them fifty-seven years later.
- **Architecture:** detective. The 1969 count is the case file: it starts with 101 missing and works down to the people nobody
  found; the 2026 appeal is the case still open. The science acts (the rain, the slides) answer "how".
- **Scope held in every act (which count means what):**
  - 256 and 143: NWS Jackson, all of Camille and the Gulf Coast (N14). "Nearly half" = 113 of 256, said only with "the Weather
    Service's count" on screen.
  - 113 dead and 39 missing: Virginia, as of 13 Nov 1969, USGS OFR 70-51 and WSP 2030 (N11, P1). The only dated official pair.
  - "More than a hundred twenty": Nelson County. Sources give 114 (+37 missing, state marker), 123 and 126 (NWS), 124 (local), 125
    (News & Advance list). Never "124 in Virginia". The on-screen line names the source it shows.
  - 150 to 153: Virginia, later federal counts (USGS 1973, 1999; NWS). Said only as "later counts".
  - 33: never found, Nelson County (News & Advance 2019 list from the Oakland Museum: 84 + 33 missing + 8 unidentified = 125; C-VILLE 33). No 1969 primary; WHSV's 32 is the outlier.
  - Eight: found but never identified, Nelson County (VDH media update 28 Aug 2026); WHRO: seven in Nelson, one over the Albemarle line. Never "along one river". No ages on screen.
  - Rain: 27 to 28 inches in central Nelson County in about 8 hours from about 7 p.m. on the 19th (N9). 31 inches near the Tye is
    "widely publicised" and unverified: never said.
  - "Probable maximum": the 1956 Weather Bureau study for the Corps of Engineers, 28 in in 6 h and 31 in in 12 h (N10); Schwarz 1970
    (via PP 804): the night reached about 80 to 85 percent of the estimated maximum possible. Never "the most rain physically possible".
  - Warnings: no Virginia warning time is sourced yet. The script says nothing about warnings until the fact lane finds the record (angle candidate 5).

## Section ID map
`tts_episode.parse_segments` IDs must match `[A-Z]\d+-S\d+`.
| Section | ID prefix |
|---|---|
| Hook (Paul on camera) | H1 |
| Hook tail | T1 |
| Intro: the storm, the rain, the count | I1 |
| Act 1, the night: Massies Mill and the Tye | A1 |
| Act 2, the mountainsides came down: Davis Creek | A2 |
| Act 3, the count that would not close (book ad inside) | A3 |
| Act 4, the eight | A4 |
| Book ad | (none: `config.yaml channel.cta` carries its own voice) |
| Close | Z1 |

## Writer notes
- The blockquote is the spoken line and nothing else. Row tags sit on the `Rows:` line.
- **The hook's sound (reasoned, DESIGN.md "Cold-open hook contract"):** heavy rain on a tin roof under Paul from 0:00, cut dead on
  his last word. Not a siren: this story is a night with no siren and no sourced warning. The rain is the one sound that belongs
  to that night. No archive or broadcast audio in the hook.
- Pictures: Library of Virginia aerials (Massies Mill, Tyro, the Tye at Norwood, Lovingston; rights "No known copyright
  restrictions", LVA asks permission and a fee: settle before use), USGS PP 804 and OFR 70-51 figures, VCU reels of the James at
  Richmond (PD stated), our own maps, rain gauges and counters. No PD moving picture of Nelson County found yet
  (`research/footage-inventory.tsv`). News pulls only as inserts inside acts.
- Register: Paul is an old friend you haven't seen in years telling you what happened (`references/script-quickref.md` "Voice").
  Grader on draft 1: hook 7 of 10, register 6 of 10 (FAIL). Draft 2 takes its five fixes: the hook opens on the belief, the tail
  runs under 15 s, one count per sentence, the 1969 count (113 and 39) and Davis Creek move to acts 3 and 2, "you" through the intro.
  Grader on draft 3: hook 7 of 10, register 7 (FAIL); draft 4 takes its five fixes plus the reveal-flip in I1-S7 and the
  Virginia-against-Nelson count clash in I1-S2 and I1-S8.
  Grader on draft 4: hook 8 of 10 (65 %), register 8, PASS. Draft 5 takes its fixes 1 and 2 (injuries before the slope; the probable
  maximum in one sentence, the 1956 study and the Corps on the card) and a fact-safe form of 3 (C-VILLE: "Two of the Wood children").
- Numbers spoken the way a person says them, spelled out for the voice; years stay digits. One count per sentence.
- Flag words: no "killed" anywhere; "drowned" only on the I1-S7 cite card, as the source's own words.
- The eight: the news copies describe seven people by age (two adults 30 to 50, one older woman 50 to 70, two teens 15 to 19,
  two children about 8 to 12) against a headline of eight. No age goes on screen until the VDH text is read.

## Loop table
| Loop | Plant | Pay |
|---|---|---|
| L1 episode: will the eight get their names, and why do they still not have them? | H1-S1 | A4 (the appeal, what is known, what is still open) and Z1; re-shown at I1-S9 |
| Q1: how does one night of rain take people that completely? | T1-S2 | I1-S3 to I1-S7 in part (rain, slopes, injuries); in full across A1 and A2 |
| Q2: why there, two nights after landfall? | I1-S2 | I1-S3 |
| Q3: what does rain that close to the limit do to a mountain? | I1-S5 | I1-S7 |
| Q4: how does rain break bones? | I1-S6 | I1-S7 |
| Q5: how many people is that? | I1-S7 | I1-S8 |
| A1 loop: what happened to the Wood children? | I1-S10 | A3 (never recovered) |
| cta-hinge: the missing list starts at a hundred and one; where did it go? | last line of A3 before the ad | first line of A3 after the ad |

## Act briefs (structure only; prose waits for the lock)
> **ACT 1 — the night: Massies Mill and the Tye · about 4.5 min**
> **Job:** put the viewer in Nelson County from about 7 p.m. on the 19th to daybreak: the rain, the river, one family.
> **In / out:** a weather report for "showers, clearing in the morning" (P27, `[verify]`) → Warren Raines in a tree at daybreak (P31).
> **Loops:** plants "the Wood children" · pays Q5.
> **Rehooks:** LVA aerial of Massies Mill; our rain-gauge counter climbing hour by hour; Warren Raines's own words on a card (WTKR 2019).
> **Tempo + emotion:** slow build, one human story, banks the first emotion.

> **ACT 2 — the mountainsides came down: Davis Creek · about 4.5 min**
> **Job:** the mechanism: debris avalanches (PP 804: where they started, how fast, what they sounded like), why the injuries were
> blunt force, why people were carried miles.
> **In / out:** a Woods Mill survivor's description of the ground moving (V31) → Davis Creek, 2 of 25 houses left (N12).
> **Loops:** plants "the count" · pays Q1 in full.
> **Rehooks:** USGS scar photographs; our cross-section of a slope letting go; the sound quote on a beige cite card (V32).
> **Tempo + emotion:** fast science, then a hold on Davis Creek.

> **ACT 3 — the count that would not close · about 5 min (book ad inside, about the halfway mark)**
> **Job:** the search and the count: the working numbers moving through August (trooper tape: 101 missing on the 24th, 88 on the
> 26th, about 32 "probably never be found" by 1 Sep, all `[verify]` against a 1969 paper), the 13 Nov 1969 count (113 and 39), every
> later source a different number, and why.
> **CTA hinge:** tease = last line before the ad (the list starts at a hundred and one) → CTA → payoff = first line after (where it went).
> **Rehooks:** our counter; LVA recovery photographs; Ginger Raines found two weeks later, twenty miles away (WTKR, `[verify]`).
> **Tempo + emotion:** detective pace, the Wood children paid here.

> **ACT 4 — the eight · about 4 min**
> **Job:** the 2026 appeal: who is looking (Lara Newell, VDH), what is known (recovered around the Rockfish River, cremated,
> autopsy and dental records), what anyone can do.
> **In / out:** the 29News headline → the open question, with a dated window.
> **Loops:** pays L1 (partly: the names are still open, and the script says so).
> **Tempo + emotion:** the strongest emotion of the film sits here, in the last third.

---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one. Popfig inside the first second, top left: "Nelson County, Virginia · August 1969".
Rain on a tin roof under him from 0:00, cut dead on his last word. A beat after "right?" so the viewer answers in their head. Glance
chips (2 to 4 words, one at a time): "IDENTIFIED BY NOW?" on "identified by now"; "8 STILL UNNAMED" on "eight of them", source line below
it: "Virginia Department of Health · August 2026". Cut out on his last word.
> You'd think every person a 1969 hurricane took has been identified by now, right? Virginia's still asking for help putting names to eight of them.

**Rows:** (the viewer's belief, no row) · [VDH media update, 28 Aug 2026: eight unidentified, Nelson County (factcheck-A item 3)]

*(26 words. Sentence one is the viewer's belief, not a date. First break inside 10 s. [L1 open]: who are they, and why no names?)*

## H1 alternatives (the owner picks one)
- Alternative 1 (24 words): "A hurricane in 1969. By now every person it took is counted and named, right? Virginia's still looking for eight names this year." Rows: VDH. (Opens on a fragment and a date: weaker.)
- Alternative 2 (26 words): "Camille, 1969. You know it as the Mississippi storm, right? Fifty-seven years later, Virginia is asking the public to help name eight people it took." Rows: VDH, N14. (Leads on the coast belief, which FAULT LINES and Dark Horizon already break: weaker.)
- Why the pick: the viewer's answer ("of course they're named") is broken by a fact from this year inside 10 s, and the second break follows at once in T1-S1. Grader on draft 1: 7 of 10; this line is the grader's fix 1, trimmed; "found along one river" was cut by fact-check A (the eight were found in Nelson County, one over the Albemarle line, six on the Rockfish and two on the James in the 1969 list).

---

## T1 · Hook tail (about 0:08 planned, about 14 s)

### T1-S1 · narration
**Picture:** hard cut on the first word, never black: LVA aerial of the Tye River valley at Massies Mill after the flood, slow push.
On "thirty-three" the number lands: "33 never found". Source line: "Nelson County · News & Advance, 2019 (Oakland Museum list)".
> And thirty-three more people from that same night were never found at all.

**Rows:** [factcheck-A item 1: News & Advance 2019 list, "Eight never were identified; 33 were never found", 84 + 33 + 8 = 125; C-VILLE 33] (no 1969 primary; WHSV's 32 is the outlier)

*(Second break, the double contradiction.)*

### T1-S2 · narration
**Picture:** our own map, first appearance: Camille's track drawn up from the Gulf to Virginia, then a push in to Nelson County and a
its rivers drawn in thin blue, labelled "Nelson County, Virginia". On "how" the rain gauge counter appears at 0.0 inches, not running yet.
> The storm was Hurricane Camille, and the place was Nelson County, up in the Virginia mountains. So how does one night take people that completely?

**Rows:** [VDH media update 28 Aug 2026: Nelson County] · [N7: track]

*([Q1 open]. No void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*

## I1 · Intro: the storm, the rain, the people (about 0:22 planned)

### I1-S1 · narration
**Picture:** ATS-III satellite still of Camille in the Gulf, 17 Aug 1969 (UW-Madison SSEC, "No copyright (U.S.)", footage row S04).
Our map marks Waveland, Mississippi; popfig "Aug 17, 1969 · 11 PM". On the second sentence a bar builds: "Gulf Coast · 143 · NWS".
> You probably know Camille from the Mississippi coast, where it came ashore late on the night of August seventeenth, 1969. A hundred forty-three people lost their lives on the Gulf Coast.

**Rows:** [N1: Waveland, 11 PM CDT] · [N14: 143 on the Gulf Coast]

### I1-S2 · narration
**Picture:** the track crawls inland across Mississippi, Tennessee, Kentucky, West Virginia; the storm symbol shrinks and loses its eye.
No second bar (a Virginia number here would clash with the Nelson share in I1-S8). Glance chip "TWO NIGHTS LATER".
> Two nights later, what was left of it crossed into Virginia, and the Weather Bureau wasn't even calling it a hurricane anymore. Up in those mountains, it took well over a hundred lives.

**Rows:** [N7, N8: track and the Virginia night] · [N14: 113 in the Virginia floods] · [factcheck-B I1-S2: HURDAT2 tropical depression from 19 Aug 0600 UTC; OFR 70-51 p. 1 "became a tropical depression"; Corps of Engineers Mobile District 1970 advisory table, warnings discontinued 18 Aug]

*([Q2 open]: why there? Paid in I1-S3.)*

### I1-S3 · narration
**Picture:** the rain gauge counter starts: popfig "7 PM · Aug 19". It climbs to "27 in" while a clock runs "about 8 hours". Source
line "ESSA-Weather Bureau survey · USGS Open-File Report 70-51".
> What made the difference was rain. From about seven that evening, around twenty-seven inches fell on the middle of Nelson County in roughly eight hours.

**Rows:** [N9, V1: 27 to 28 in, central Nelson County, 8 hours from about 7 p.m.]

*([Q2 paid].)*

### I1-S4 · narration
**Picture:** the counter freezes at 27; the survey table's own row slides in as a beige cite card: "Nelson County · 27 · Trash barrel ·
accuracy: Good · emptied afternoon before rain began". Glance chip "A TRASH BARREL".
> I read the Weather Bureau's survey, and one of the biggest readings came from a trash barrel somebody had emptied that afternoon.

**Rows:** [V5, factcheck-B: OFR 70-51 p. 11, Table 1 row: "Trash barrel", "Good", "Barrel had been emptied afternoon before rain began"]

### I1-S5 · narration
**Picture:** a beige cite card: "probable maximum rainfall · Weather Bureau study for the Corps of Engineers, 1956 · USGS OFR 70-51 p. 7".
Then a single gauge filled to about four-fifths, label "about 80 to 85 % of the maximum possible · Schwarz 1970, via USGS PP 804".
Never 27 in 8 h drawn against 28 in 6 h as if they shared a duration.
> Weather experts had already worked out the most rain those mountains could ever get, and that night reached about four-fifths of it.

**Rows:** [N10, V2: the 1956 study, OFR 70-51 p. 7, CONFIRMED raw] · [V3: PP 804 p. 5, "Schwarz (1970, p. 853) states that Camille's rainfall in Virginia was within about 80-85 percent of the estimated maximum possible rainfall, for areas up to 1,000 sq mi over a 12-hour period", read raw by the orchestrator]

*([Q3 open]: what does rain that close to the limit do to a mountain? Paid in I1-S7.)*

### I1-S6 · narration
**Picture:** LVA aerial of a scarred hollow; a beige cite card: "died from broken bones and other blunt-force injuries, rather than by
drowning · USGS Professional Paper 804, 1973". Glance chip "BLUNT-FORCE INJURIES".
> Most of the people the flood took there had broken bones and other blunt-force injuries.

**Rows:** [V34, P7: PP 804 abstract, CONFIRMED raw by factcheck-B; the finding rests on Dr. J. H. Gamble's examinations]

*([Q4 open]: how does rain break bones? Paid in I1-S7.)*

### I1-S7 · narration
**Picture:** our cross-section of a steep wooded slope above a creek and a house; the soil darkens with water, then a long tongue of it
lets go and runs down into the hollow. Label "debris avalanche · USGS Professional Paper 804". Then a USGS photograph of a scar.
> If you lived up one of those hollows, the soaked slope above you could let go in the dark and come straight down the creek.

**Rows:** [V29 to V33: debris avalanches, where and how; PP 804 pp. 15 to 17: scars 25 to 75 ft wide, surges down the channels] (factcheck-B: "whole hillsides" and "asleep" cut, the second rests only on an uncited NWS Sterling line)

*([Q3 paid] and [Q4 paid]: the slopes came down. [Q5 open]: how many people is that? Paid in I1-S8.)*

### I1-S8 · narration
**Picture:** the map, Nelson County outlined; a grid of a hundred small figures, one turns amber. Label "about 1 in 100 · Nelson County,
1970 census 11,702". Source line for the count: "Nelson County · NWS: 123 and 126 · 125 on the 2019 list".
> In Nelson County alone, the flood took about one in every hundred people who lived there.

**Rows:** [P9, P10, P15, P16, P19] · [P5: USGS OFR 99-518 "about 1 percent of the citizens of Nelson County", raw] · [1970 census PC(1)-A48 Table 9: 11,702] (factcheck-A item 2, CONFIRMED)

*([Q5 paid].)*

### I1-S9 · narration
**Picture:** back to the Nelson County map; eight small markers, unlabelled, no ages. Source line "Virginia Department of
Health · August 2026".
> And eight of the people the water gave back there still don't have a name.

**Rows:** [VDH media update 28 Aug 2026; WHRO 13 Oct 2026: seven found in Nelson, one over the Albemarle line] (no ages on screen)

*([L1] back in front of the viewer at about 1:25.)*

### I1-S10 · narration
**Picture:** the map pushes west to the Tye River at Massies Mill; popfig "Aug 19, 1969 · night". LVA aerial of Massies Mill.
> The first family I want you to meet lived on the Tye River at Massies Mill. With them that night were two of the Wood children, eighteen-year-old Donna Fay and four-year-old Gary.

**Rows:** [News & Advance 2019 list, read raw by the orchestrator: "The missing ... Wood, Donna Fay, 18, Massies Mill; Wood, Gary, 4, Massies Mill"; five Raines of Massies Mill among the dead] · [C-VILLE 14 Aug 2019, raw: "Two of the Wood children—Donna Fay and Gary—were among the 33 people whose bodies were never recovered."]

*([A1 loop open]: what happened to Donna Fay and Gary? Carried into Act 1, paid in A3 (both on the 2019 list of the never found). First chapter blackout after this segment.)*

<!-- ACTS SPLICED FROM drafts/ BELOW; edit the drafts, not this block -->

# A1 · Act 1, the night: Massies Mill and the Tye (draft 2, 22 Oct 26: factcheck-A1 and grader fixes applied)

Writer: Act 1 lane. Target about 760 spoken words, about 4.5 min. Seam in: I1-S10, then the chapter blackout.
Footage note: no moving picture of Nelson County exists in `research/footage-inventory.tsv`, so the real-thing beats here are LVA stills
(V01 Massies Mill aerial, V02 the church left standing, V03 Tyro, V04 the Tye at Norwood), the OFR 70-51 table rows and the survivor words
as beige cards. The rain-gauge counter never shows hourly values: no hourly record exists (A1-S6 is the reason).
Draft 2 sources added beyond facts-*.md: factcheck-A1 (RAW reads of C-VILLE, Radio IQ 19 and 23 Aug 2019, WDBJ7 12 Aug 2019, WTKR 2 Sep 2019,
News & Advance list, OFR 70-51, PP 804). Radio IQ survivor quotes are 2009 interviews published 2019: their cards say so.

### A1-S1 · narration
**Picture:** out of the blackout on rain sound, never black on the first word. Our own map: the Tye River drawn in thin blue through
Massies Mill, Route 56 beside it. Popfig top left: "Tuesday · Aug 19, 1969 · 7 PM · Massies Mill". Rain texture over the map.
> Tuesday, August nineteenth, 1969, around seven in the evening, and it's starting to rain on Massies Mill. It's a small place on the Tye River, along Route fifty-six.

**Rows:** [V9: OFR 70-51 p. 7, "the 8-hour period beginning about 7 p.m. on the 19th"] · [factcheck-B 1: Corps report "Late Tuesday evening, 19 August"] · [factcheck-A1 S1: WTKR "the small village sits nestled in the valley"; OFR gauge on State Highway 56] · [N1, factcheck-B 4: landfall 11 PM CDT 17 Aug]

### A1-S2 · narration
**Picture:** the map pushes in; a small square beside the Tye marked "the Raines house". Name chips one at a time: "Warren Raines, 14",
"Carl Raines, 16". A second square next door: "the Wood family".
> Warren Raines lived there, close to the river, with his parents and his four brothers and sisters. Warren was fourteen. His brother Carl was sixteen. Next door lived the Wood family. Before that night was over, four of the Wood children would be riding with the Raines family in one station wagon.

**Rows:** [factcheck-A1 marker 4: C-VILLE RAW, siblings Johanna, Carl, Sandy, Ginger; Warren 14 and Carl 16 (Radio IQ, C-VILLE); C-VILLE RAW "Their neighbors, the Woods, sent their four children"; WTKR RAW "The seven Raines and the neighbor's four children escaped in the family station wagon"]
*(Family inside minute one. [A1 loop] carried from I1-S10: Donna Fay and Gary are two of those four.)*

### A1-S3 · narration
**Picture:** beige cite card 1: "The weather bureau at the time simply stated there will be showers tonight, clearing in the morning." ·
Jeff Halverson, meteorology professor, UMBC · Radio IQ (WVTF), 23 Aug 2019. Then beige cite card 2: "11 o'clock news that night, weather
report said rainy and cloudy. Just go to bed, yeah." · Bernard McGinnis, recalled · interviewed 2009 · Radio IQ (WVTF), published 2019.
> A meteorologist who has studied that night says the forecast was showers, clearing in the morning. Bernard McGinnis, from Nelson County, remembered the eleven o'clock news. Rainy and cloudy, it said, so you went to bed.

**Rows:** [factcheck-A1 marker 1: Halverson, Radio IQ 23 Aug 2019, RAW] · [P26, factcheck-A1 marker 2: McGinnis, Radio IQ 19 Aug 2019, RAW]
*(No narrator claim about warnings. The card is a recollection, said as one.)*

### A1-S4 · narration [RS]
**Picture:** [VE] the screen goes white for a frame on a lightning flash, then back to the map, now dark and wet. The rain-gauge counter
appears bottom right and starts climbing slowly, no numbers between start and finish. Table 1 remark slides in as a chip: "Hard rain
from 8 p.m. to 4 a.m.". Then beige cite card: "if you were out in it it was almost like you couldn't breathe" · Audrey Diane Evans ·
interviewed 2009 · Radio IQ (WVTF), published 2019.
> By eight, the rain was coming down hard, and one gauge note from that night says it didn't ease until four in the morning. Federal scientists who studied the storm wrote that the thunder and lightning were intense all night, except for one brief lull around midnight. One woman who was out in it told Radio IQ it was almost like you couldn't breathe. What I wanted to know was why it rained like that there, hours before the storm's center even reached Virginia.

**Rows:** [V10: OFR 70-51 Table 1 remark "Hard rain from 8 p.m. to 4 a.m."; PP 804 pp. 4 to 5, "Except for a brief lull at about 2330 or 2400 hours, the rainfall, thunder, and lightning were intense during the entire storm"] · [factcheck-A1 marker 3: Evans, RAW] · [factcheck-B 1: HURDAT2, center over Kentucky at 8 PM EDT; OFR 70-51 p. 5, center moved into Virginia "Near midnight"]
*(Open question for the science: why there? Paid in A1-S5.)*

### A1-S5 · narration
**Picture:** our own map, wide. A popfig "8 PM" over Kentucky marks Camille's remnant swirl. An amber band of storms is already over
Virginia, drawn in from the north and northwest. Popfig "near midnight": the swirl crosses into Virginia south of Roanoke and Lynchburg and
tightens. Soft blue shading southeast of Nelson County is drawn in under it; label "moist air · about 3,000 ft deep". Source line "USGS
Open-File Report 70-51 · USGS Professional Paper 804, after Schwarz 1970".
> At eight that evening, what was left of Camille was still over Kentucky. The rain over Nelson County was already falling from a band of heavy storms that had pushed in from the north earlier that day. Near midnight, the storm's center crossed into Virginia and began to strengthen. Its winds pulled in air from the southeast that had been filling with moisture for days, and the rain along the Blue Ridge picked up fast. And the Tye ran right past the Raines house. How much fell in each of those hours, I still can't tell you, and the reason is a rain gauge.

**Rows:** [factcheck-B 1: HURDAT2 20 Aug 0000 UTC, 84.0W, Kentucky] · [V14: OFR 70-51 p. 5, "merging with a band of heavy showers and thunderstorms that had moved into Virginia from the north and northwest earlier in the afternoon and evening"; "Near midnight, the low pressure center began to intensify as it moved eastward into Virginia along a track south of Roanoke and Lynchburg. Rainfall ... increased very rapidly along the western slopes of the Blue Ridge Mountains"] · [V15: PP 804 p. 4, moist air "accumulating for several days", "These winds drew moist air from the southeast"]
*(Pays "why there". Opens the gauge question, paid in A1-S6. No "the Blue Ridge caused it" (V16).)*

### A1-S6 · narration [RS]
**Picture:** [VE] the counter climbs, then jams at "11+" and blinks. Beige cite card, the survey row's own words: "Nelson County · WB
Recorder · 11+ · Gage overflowed" · USGS Open-File Report 70-51, Table 1. A second row: "11+ · 11" bucket · Bucket overflowed before 2 a.m.".
Then three quick rows from the same table: "Barrel", "Street trash container", "Plastic garbage container". On the last three sentences,
two dots on the map less than 5 miles apart, one labelled "20+ in", the other "under 6 in"; chip "4 TIMES"; source line "Weather Bureau
survey team, reported in USGS Professional Paper 804".
> A Weather Bureau recording gauge in Nelson County, the kind that logs rain as it falls, stopped at eleven inches, because it overflowed. Another bucket in the county overflowed before two in the morning. So most of what we know about that night came from whatever happened to be sitting outside and catching rain. And they didn't agree. The survey team found more than twenty inches in some spots. A few miles away, the same team found less than six. That happened four separate times, which means one family's night could look nothing like the next hollow's.

**Rows:** [V5, factcheck-A1 S6: OFR 70-51 Table 1, "WB Recorder", "11+", "Gage overflowed" (37 52' / 79 08'); "11" bucket", "Bucket overflowed before 2 a.m." (37 49' / 78 52'); barrel, street trash container, plastic garbage container] · [V13, factcheck-A1 S6: PP 804 reporting Schwarz 1970, "for each of four observations of over 20 inches total rainfall, less than 6 inches was measured at a location less than 5 miles away"]
*(Ends on the disagreement between nearby gauges. The probable-maximum segment is cut: I1-S5 holds it, and it is ruled-out lead 6.)*

### A1-S7 · narration
**Picture:** back to the Raines square; a phone icon rings once. Popfig "2 AM · Aug 20". Chip "PHONES STILL WORKING".
> Around two in the morning, the phone rang at the Raines house. Warren remembered the family running to see who was calling at that hour. A neighbor was on the line, saying the water was coming up fast. The phones still worked then, but not for much longer.

**Rows:** [factcheck-A1 marker 4: Radio IQ RAW "The phones were still working, and at 2 a.m. the family ... got a call, warning them that the nearby Thye River was coming up fast"; WDBJ7 RAW, Warren "We run to the bedroom to see who's calling at two in the morning", "A neighbor was alerting the Raines' to the fact that their small community was filling up with water"] · [V10: cloudburst about 0250 cut telephones]
*(A neighbor's call, CONFIRMED. Nothing here says any agency warned anyone.)*

### A1-S8 · narration
**Picture:** the Wood square next door lights; a line of small figures crosses from it to the Raines square. Chip "11 IN ONE STATION WAGON".
Beige cite card: "Next door neighbor asked if four of their kids could come with us." · Warren Raines · interviewed 2009 · Radio IQ (WVTF),
published 2019.
> Next door, Mrs. Wood used a wheelchair, and the Woods figured they'd take a chance on riding it out. But Mr. Wood would feel better if his kids went with the Raines family. So eleven people piled into the family station wagon, a 1968 Ford, and tried to get out.

**Rows:** [factcheck-A1 marker 4: Radio IQ RAW, Warren "Next door neighbor asked if four of their kids could come with us. His wife was wheelchair-bound, and they figured they'd take a chance at riding it out, but he'd feel better if his kids came with us, so eleven of us got in the family station wagon"] · [factcheck-A1 S9: WDBJ7 "1968 Ford Ranch station wagon"]

### A1-S9 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. Rain bed ducks under him, no narration under the clip.
> I keep coming back to that choice. Stay in a house beside a rising river, or get everybody in the car and go. They went.

**Rows:** (presenter line, no new fact) · [factcheck-A1 S10: CONFIRMED]
*(25 words. The act's turning point: the family leaves the house. Flag from factcheck-A1: the Raines house stood, upstairs untouched. The
line does not say staying was safe; Act 3 may pay the irony, never by saying they would have lived.)*

### A1-S10 · narration [RS]
**Picture:** [VE] the car icon barely leaves the square and stops dead as the blue line floods over the road. Then LVA aerial V03 (Tyro,
Route 56 along the Tye) with lightning flicker, slow push, and a beige cite card: "There was cattle floating by, logs, automobiles. Even had
an entire house float by." · Warren Raines · WDBJ7, 12 Aug 2019.
> Carl said they backed out of the driveway and had just passed the house when the engine flooded. So they got out and went on foot, into the dark. The lightning hardly stopped, so they could see what the river was carrying past them.

**Rows:** [factcheck-A1 marker 5: WDBJ7 RAW, Carl "We backed out of the driveway and just passed the house when the motor flooded out"; WTKR RAW "the group had to flee on foot"; Radio IQ RAW "Lightning was constant - allowing them to watch the destruction"; WDBJ7 RAW Warren quote for the card] · [V03]

### A1-S11 · narration
**Picture:** popfig "2:50 AM", glance chip "POWER AND PHONES OUT". The map pulls out from the Tye to the whole county; the Rockfish River
draws in to the north and one narrow hollow on Davis Creek glows amber, labelled "Davis Creek". Davis Creek is drawn on the Rockfish
side, never as a Tye tributary.
> At about ten to three, a cloudburst cut the power and the phones for many people. And the single worst-hit place in the county that night was one narrow hollow along Davis Creek, over on the Rockfish side, away from any big river.

**Rows:** [V10, factcheck-A1 S12: PP 804 p. 5, "A particularly strong cloudburst struck about 0250, cutting off electricity and telephones for many of the inhabitants"] · [P13: most deaths along Davis Creek and Huffman's Hollow] · [factcheck-A1 S12: OFR p. 22 Davis Creek; OFR 99-518 "the 50 fatalities in that one area"; OFR Fig. 4 "Davis Creek, 5 miles north of Lovingston"]
*([A2 loop open]: why was a hollow with no big river the worst-hit place? Paid in Act 2. The count stays for Act 2.)*

### A1-S12 · narration [RS]
**Picture:** [VE] hard cut to the Tye River hydrograph as a single line that shoots up off the top of the frame; beige cite card:
"gage destroyed by flood" · Tye River near Lovingston · USGS OFR 70-51. Chip "8× THE 31-YEAR RECORD". Popfig "4 AM".
> Downstream near Lovingston, the water tore the river gauge right out. High-water marks showed the Tye peaked around four that morning. That was about eight times its old record.

**Rows:** [V18, factcheck-A1 S13: station 02-0270.00, 80,000 cfs at 0400 Aug 20, gage destroyed, floodmarks; abstract "eight times the previous high during the 31 years of record"]

### A1-S13 · narration
**Picture:** the county map, the Rockfish and the James drawn in; eight small unlabelled markers fade in and hold. Source line "Virginia
Department of Health · August 2026". No ages, no names.
> Somewhere in this same night are the eight people Virginia is still trying to name.

**Rows:** [VDH media update 28 Aug 2026 (factcheck-A 3)]
*([L1] kept alive, one line, no new fact.)*

### A1-S14 · narration [RS]
**Picture:** [VE] the map dissolves into the LVA aerial of Massies Mill after the flood (V01), slow push; then the church left standing on
Route 56 (V02). Popfig "Aug 20, 1969 · daybreak". Cite line "USGS Open-File Report 70-51".
> Around four, the rain finally thinned to a mist. When it got light, you could see what was left of Massies Mill. Every building but two houses and a church was ruined, and much of the town had been swept away.

**Rows:** [V31: PP 804 p. 16, "after the rain had abated to a sprinkle or mist, at about 0400 hours on August 20"] · [V24, factcheck-A1 S15: OFR 70-51 p. 22] · [V01, V02]

### A1-S15 · narration
**Picture:** LVA still of the Tye in flood near Massies Mill (pick from V13 at sourcing; V04, the Tye at Norwood, as the fallback). Name
chips: "Warren Raines, 14" then "Carl Raines, 16". No tree assigned to either brother.
> Warren and Carl had spent the night in trees, cold and soaked through. At first light, rescuers came by boat and found them still there.

**Rows:** [factcheck-A1 S16: WTKR RAW "At daybreak, rescuers in boats pluck the brothers from two trees"; WDBJ7 RAW "Warren and Carl stayed in their trees, cold and drenched with rain, until daybreak"]

### A1-S16 · narration
**Picture:** the same still darkens; beige cite card, held about 5 s after the line, no music swell: "My mother said, 'Let go. We'll catch
you.' I let go of it. And I got there, and they were gone." · Warren Raines · WTKR News 3, 2019. Rain bed out on the last word of the
card's read time. Chapter blackout follows.
> Fifty years later, Warren told a Norfolk TV station what happened in that water.

**Rows:** [P31, factcheck-A1 marker 6: WTKR 2 Sep 2019, RAW]
*([A1 loop] stays open: the card does not say who was lost, and nothing here says Donna Fay and Gary were never found. Paid in Act 3.)*

---

## Writer's check
- Spoken words: 735 (counted by script). Target about 760.
- Register self-score: 9 of 10 (first person at "What I wanted to know", "I still can't tell you", "I keep coming
  back"; the family in minute one; contractions). A point off for A1-S12, which still reads closer to a report.
- Flag words: none of the hard list; no died, dead, death, drowned, bodies in the spoken lines or cards.
- Open question through the science: why there (S4, paid S5) → why no hourly record (S5, paid S6) → one family's night vs the next
  hollow (S6, carried into S11's Davis Creek plant).
- Loops: A1 loop (Donna Fay and Gary) kept open; L1 one line (A1-S13); A2 plant (A1-S11). Pays nothing.
- No line repeats H1, T1 or I1: the trash barrel, the four-fifths, the probable maximum, the 27 inches and the blunt-force line are not restated.
- Verify markers: 0. Every new fact comes from factcheck-A1 or factcheck-B, both read raw.

## A2 · Act 2, the mountainsides came down: Davis Creek (about 4.5 min planned; fix pass 1, 22 Oct 26, factcheck-A2 and grader applied)

*(Chapter blackout before this segment, hand-placed. Act 1 ends at daybreak on the 20th with Warren Raines in a tree by the Tye.)*

### A2-S1 · narration
**Picture:** up from black on the first word: our own map, Nelson County, pushes east from the Tye to Davis Creek and Woods Mill; the creek drawn in thin blue with small hollows branching off it. Place stamp popfig: "Davis Creek · Woods Mill · night of Aug 19, 1969". Then LVA aerial of mudslide homes along Rt. 29 (footage V06), slow push, label "Nelson County, 1969".
> If you lived up Davis Creek near Woods Mill, there's a good chance your house stood in one of the small hollows that fold back off the creek into the mountain. That night, the ground above those hollows started to move.

**Rows:** [factcheck-A2 S1: PP 804 p. 16, "A number of missing houses, particularly in the Davis Creek basin, originally stood in small hollows which were scoured by avalanches"; OFR 70-51 fig. 4 "Landslide at Davis Creek, 5 miles north of Lovingston"; Woods Mill and Davis Creek same spot]
*([Q1] still open from T1-S2; this act pays it. Open: what does moving ground look like? Paid in S2.)*

### A2-S2 · narration
**Picture:** beige cite card: "the ground started oozing slowly downhill for a fraction of a second, and then the entire section of the hillside suddenly slid quickly down the slope · S. O. Mawyer, Woods Mill, as reported by USGS Professional Paper 804 (1973)". Behind it, our cross-section of a wooded slope: the soil creeps a hair, holds, then a strip lets go. **[RS] [VE]** the strip breaks loose on "fast".
> S. O. Mawyer of Woods Mill was nearly swept away by a small slide near his home. He saved himself by grabbing a bush just past its edge. He said the ground started oozing downhill, slowly, for a fraction of a second. Then that whole section of hillside slid down the slope, fast, with a loud noise.

**Rows:** [V31; factcheck-A2 S2: PP 804 p. 15, "almost swept away in a small avalanche near his home and only saved himself by grabbing a bush that was growing just beyond the slide border"] (the paper's report of what he said, not his recorded words)

### A2-S3 · Paul on camera, one clip
**Picture:** Paul full frame, no narration under it. Cut out on his last word.
> I'd always pictured a flood as water rising. On Davis Creek, the hillside above the houses came down, and it brought the creek with it.

**Rows:** [V33: avalanches made surges in the creeks] · [factcheck-A2 S3: CONFIRMED]
*(25 words, unchanged. The turning point: the flood story becomes a ground story.)*

### A2-S4 · narration
**Picture:** black frame with a low rumble bed rising under it, then the beige cite card: "like a squadron of airplanes warming up for takeoff · residents, as reported in USGS Professional Paper 804". **[RS] [VE]** our map of the hollows trembles on a ring that spreads out several miles, label "ground shook for several miles".
> People who lived near those mountains all talked about the roar, from the slides and from the creeks. One description stays with me: a squadron of airplanes warming up for takeoff. The bigger slides shook the ground for several miles around, so you could feel one you never saw.

**Rows:** [V32; factcheck-A2 S4: PP 804 p. 16, "unanimous in emphasizing the awful roar they heard associated with both the debris avalanches and the swollen streamflow"; quivering "for a radius of several miles"] (the dynamite and cannonball wordings are left off: flag words)
*(Open: how long did a slide last, and when did they stop? Paid in S5.)*

### A2-S5 · narration
**Picture:** a slim timeline under our map, small marks dropping on it as slides go, closer together toward the end, then two more after a popfig "about 4 AM · rain down to a mist". Glance chip "ABOUT 3 MINUTES" on Floyd.
> B. R. Floyd of Lovingston figured the slide near his home went on for about three minutes. People said the slides came more often toward the end of the storm. And some were still coming at about four in the morning, after the rain had eased to a mist.

**Rows:** [V31; factcheck-A2 S5: PP 804 pp. 15 to 16, Floyd; "the avalanching was more frequent toward the end of the storm"; slides at about 0400 on Aug 20]
*(Open: why one slope and not the next? Paid in S6.)*

### A2-S6 · narration
**Picture:** title card of USGS Professional Paper 804, "Garnett P. Williams and Harold P. Guy · U.S. Geological Survey · 1973". Then our cross-section again, now labelled: a slope steeper than 35 percent drawn as "1 ft up for every 3 ft across"; a dip in the slope glows; the top of the strip sits at the steepest point; a compass rose lights N, NE and E. **[VE]** each label lands on its word.
> Two USGS scientists, Garnett Williams and Harold Guy, went back afterward to find out why one slope let go and the next one held. I read their paper. The slides usually came off slopes steeper than thirty-five percent, about a foot up for every three feet across. Most followed dips already in the hillside, and the top of each scar tended to sit at the steepest part of the slope. Hillsides facing north, northeast and east gave way several times as often as most others.

**Rows:** [V29; factcheck-A2 S6: PP 804 abstract p. 1 and title page "By GARNETT P. WILLIAMS and HAROLD P. GUY"; "pre-existing depressions"; "slopes facing north, northeast, and east experienced several times as many avalanches as slopes facing most other directions"] (first names checked in the raw text the fact-check cites)
*(Open: how big was one of these slides? Paid in S7.)*

### A2-S7 · narration
**Picture:** a USGS photograph of an avalanche scar from PP 804 (figure number to be pulled; PD-federal, footage V23). Our overlay draws its outline and three measure lines: "25 to 75 ft wide", "300 to 600 ft long · USGS OFR 70-51", "1 to 3 ft deep". A football field slides in beside the length line for scale. **[RS] [VE]** a ten-foot boulder silhouette next to a pickup truck for scale. Then our map: a shaded patch "about 40 sq mi" just south of Horseshoe Mountain.
> Each scar is a long strip down the slope. A typical one is twenty-five to seventy-five feet wide. It runs three to six hundred feet long, one or two football fields. And it's only one to three feet deep. That thin layer of soil came down full of trees, water and rock, with boulders up to ten feet across. Those scars are mostly confined to about forty square miles in the middle of Nelson County, just south of Horseshoe Mountain.

**Rows:** [V30; factcheck-A2 S7: OFR 70-51 p. 41, "A typical scar is about 1 to 3 feet deep, 25-75 feet wide ... and 300-600 feet long"; "generally restricted to a 40-squaremile area in the middle of Nelson County, just south of Horseshoe Mountain"] · [V28: PP 804 p. 14, boulders "up to 10 feet in intermediate diameter"] (PP 804's 200 to 800 ft not used; strips, never "whole hillsides")
*(Open: what happened when one reached the creek? Paid in S8.)*

### A2-S8 · narration
**Picture:** our cross-section pulls back to the hollow floor: the strip hits the creek and a wall of brown water and timber runs down the channel. Then a back-yard water gauge graphic climbs: "about 5 ft in 20 min · Woods Mill". Source line "USGS Professional Paper 804".
> When a slide reached the creek at the bottom, it sent a surge of water, mud and rock racing down the channel, and sometimes it blocked the creek for a while upstream. In one back yard at Woods Mill, the water rose about five feet in twenty minutes.

**Rows:** [V33; factcheck-A2 S8: PP 804 abstract p. 1 surges, p. 5 "rose about 5 feet in 20 minutes"] · [factcheck-A2 S1: PP 804 p. 16, houses in small hollows "scoured by avalanches"]
*(Open: what did that do to the people in its path? Paid in S9.)*

### A2-S9 · narration
**Picture:** beige cite card: "almost none of the dead showed evidence of drowning · USGS Professional Paper 804 (1973), on the findings of Dr. J. H. Gamble of Lovingston". Glance chip "MULTIPLE FRACTURES". Then LVA aerial of the Lovingston access road with debris and wrecked vehicles (footage V05), slow push.
> Dr. J. H. Gamble of Lovingston was in charge of identifying and examining the people who died. What he found, again and again, was multiple fractures, from the rock and timber the creek was carrying.

**Rows:** [V34; factcheck-A2 S9: PP 804 p. 16, Gamble "found that almost none of the dead showed evidence of drowning"; "multiple fractures ... from rocks and trees and so forth" (Simpson and Simpson 1970 via PP 804, paraphrased, not quoted aloud)]
*([Q1 paid] in full: the slopes let go, the creeks surged with rock and timber, and the people caught in them were struck by it. Open: who were they? Paid in S12 to S15, the Huffmans, Harvey and Sissy.)*

### A2-S10 · narration
**Picture:** our map returns to Davis Creek; one hollow outlined. A row of twenty-five small house icons; twenty-three fade out one by one, two remain. **[RS] [VE]** the last fade lands on "two". Glance chip "2 OF 25".
> Up Davis Creek, in one of those hollows, twenty-five houses had stood. Only two were left.

**Rows:** [V24, N12; factcheck-A2 S11: OFR 70-51 p. 22, CONFIRMED raw]

### A2-S11 · narration
**Picture:** beside the houses, a counter: "27" lands with the source line "Davis Creek community · USGS Open-File Report 70-51". Then a second counter "22 missing".
> The federal flood report counted twenty-seven people confirmed lost from that one hollow. Twenty-two more were still missing.

**Rows:** [V24, N12; factcheck-A2 S12: OFR 70-51 p. 22, "Twenty-seven persons were known dead and 22 were missing from this one hollow"] (undated sentence)

### A2-S12 · narration
**Picture:** the counters clear; our Davis Creek map, a single line along the creek. On-screen count, the only place 52 appears: "Davis Creek · 52 · News & Advance list, 2019 (Oakland Museum), counted; WDBJ and C-VILLE 2019". Then a family-name card, "Huffman · 18", no first names, no faces.
> Later counts put the toll along Davis Creek at about fifty lives. Eighteen of them were Huffmans.

**Rows:** [factcheck-A2 S13: N&A list counted, 33 dead + 19 missing = 52 Davis Creek rows, 18 Huffman rows; C-VILLE and WDBJ 2019 RAW, 52 and 18] · [P6: OFR 99-518 "the 50 fatalities in that one area"] (WSET's 23 is a household count: not used)

### A2-S13 · narration, then a real clip
**Picture:** lower third "Deborah Harvey · 8 years old in 1969". Real clip: WDBJ, "Hurricane Camille: Davis Creek", 19 Aug 2019 (Anvato 554865782), Harvey's sound bite at about 103 to 109 s, cut on her last word; her words play in her own voice, burned-in caption of the clip's wording, card "WDBJ, Aug 19, 2019". Open the frames before wiring to confirm she is on camera there; Content ID claim expected (CLAUDE.md "News footage"). Fallback if the clip is not used: a beige quote card with the article text, "You started realizing that all of these people who rode the school bus with you, went to church with you, were gone. · Deborah Harvey, WDBJ, Aug 19, 2019". **[HUMAN] [RS] [VE]** the clip.
> Deborah Harvey was eight, and her home sat safely on higher ground. Fifty years later, she told WDBJ what came after.

### Harvey clip · real clip (WDBJ, Aug 19, 2019), no narration under it
**Picture:** the WDBJ clip as set up in A2-S13, cut on her last word.

### A2-S14 · narration
**Picture:** back to the WDBJ b-roll of the Davis Creek road (same clip, outside the bite), or our map with the road drawn up the hollow.
> It took her father a week to build a road her family could get through in a jeep.

**Rows:** [factcheck-A2 S14: WDBJ, Tim Saunders, 19 Aug 2019, RAW: "eight years old", "Her home rested safely on higher ground", "it took a week for her father to build a road that her family could travel in a jeep"; clip exists and carries the bite; the father line is the reporter's voice-over, so we narrate it]

### A2-S15 · narration
**Picture:** a single row from the list on a beige card, set like the page: "Martin, Mary Ann "Sissy," 10, Davis Creek" under the heading "The missing", source line "News & Advance, 2019 · names from the Oakland-Nelson County Museum of History". No photo. Then the chip "Davis Creek · 19 never found".
> On that list of Davis Creek's missing is Mary Ann Martin. She was ten, and the list calls her Sissy. Nineteen of the people lost along Davis Creek were never found at all, and she's one of them.

**Rows:** [N&A list, Wayback 7 Aug 2021, section "The missing": "Martin, Mary Ann "Sissy," 10, Davis Creek"] · [factcheck-A2 S15: 19 never found, N&A list counted (C-VILLE says 20, not used)]

### A2-S16 · narration
**Picture:** the hold begins. LVA aerial of a scarred Nelson County hollow (footage V03, Tyro, "fatal mudslides in Nelson"), very slow push, the rain bed gone, only a low creek ambience. Beige cite card: "If both evacuation plans and a warning system had been in place ... the citizens along Davis Creek would have been advised just before midnight of August 19 to seek refuge at a nearby structure not in the path of streams draining steep slopes, such as the Oak Hill Church. · USGS Open-File Report 99-518, 1999". No church marker on the map (the report gives no location).
> Thirty years later, a US Geological Survey study went back over the storm's damage in Nelson County. With a warning system and an evacuation plan, the report says, people along Davis Creek would have been told, just before midnight, to get to a building out of the creek's path, like the Oak Hill Church.

**Rows:** [factcheck-Z1 Z1-S4: OFR 99-518, Mitigation section, RAW; the report's own hypothetical, conditional kept, not what happened that night]

### A2-S17 · narration
**Picture:** the hold continues on the hollow. Chip "IF ALL HAD HEARD AND GONE: MOST OR ALL OF 50 COULD HAVE BEEN AVOIDED · USGS OFR 99-518". It fades.
> If everyone there had heard a warning like that and gone, the report says, most or all of the fifty people lost in that one place could have lived.

**Rows:** [factcheck-Z1 Z1-S5: OFR 99-518, "Had all the citizens heard and heeded this warning, most or all of the 50 fatalities in that one area could have been avoided"] (the report's 50 is its own count; 52 stays on screen in S12 only)

### A2-S18 · narration
**Picture:** the hold continues; a slow fade toward the chapter blackout. No text.
> Williams and Guy wrote that there's no way to tell how many of Nelson County's lost were taken by the slides themselves. So when the slides carry people off in the dark, and some are never found, how do you count who's missing?

**Rows:** [V26; factcheck-A2 S15: PP 804 p. 16, "There is no way to determine how many of the 125 people who lost their lives in Nelson County were killed by debris avalanches"] (exit question, no row)
*([A2 loop open] / count loop planted for A3: how many were missing, and how do you count who is missing? Chapter blackout after this segment.)*

## A3 · Act 3, the count that would not close (book ad inside)

*(Fix pass 1, 22 Oct 26: rebuilt on research/factcheck-A3.md. Seam in: chapter blackout after Act 2's hold on Davis Creek, hand-placed. Chapter card: "The count". Act 2 planted "how do you count people a mountain buried?"; this act answers it.)*

### A3-S1 · narration
**Picture:** hard in from the blackout on LVA V05, the Lovingston access road to Route 29, debris and wrecked cars, slow push. Popfig "Aug 20, 1969 · Nelson County". Then our own map: Nelson County outlined, its roads greying out one by one until the county sits alone; the Blue Ridge drawn on its northwest edge; a thin radio arc runs from Massies Mill and Tyro over the ridge to Augusta County, then a line on to Richmond. Glance chip "CUT OFF".
> By morning, Nelson County was cut off from the rest of Virginia. The phone lines were down, and the roads and bridges were gone. Sheriff Bill Whitehead was trapped out in the west of the county, but he got a distress call out by radio. The sheriff's department in Augusta County, over the Blue Ridge, heard it and passed it on to civil defense in Richmond. And nobody outside the county knew yet how many people were missing.
**Rows:** [factcheck-A3 S1: C-VILLE 14 Aug 2019 raw, "he was able to make a radio distress call that was heard by the sheriff's department in Augusta County, which alerted the civil defense office in Richmond"] · [WHSV Part 2 raw: "all telephone and radio communication was lost"] · [factcheck-A3 S1: Augusta across the Blue Ridge, northwest] · [V05]
*(Answers Act 2's "how do you count people": first, nobody could get in. Micro-loop: how many were missing?)*

### A3-S2 · narration
**Picture:** LVA V10, the briefing before a rescue mission on the Route 29 bypass outside Lovingston. Then a beige cite card: "It took me about 8 hours to do that and there were no main, secondary roads in to Nelson County." · Ed Tinsley, State Police, Amherst County · WHSV, 2019. The card lands on the second sentence, after "check which roads were open", so it never reads as eight hours to reach Nelson.
> Ed Tinsley was a state trooper next door in Amherst County. That morning he was sent out to check which roads were open, and it took him about eight hours. There was no main road or secondary road into Nelson County. He said the lack of communication was the biggest thing.
**Rows:** [factcheck-A3 S2: C-VILLE raw "preparing for a nuclear disaster"; WHSV Part 2 raw, Tinsley quotes] · [V10]
*([VE] the Tinsley card. Nuclear-disaster line cut: no source says the civil defense team couldn't find a road in. The "133 BRIDGES OUT" chip is dropped: unchecked against the LVA caption.)*

### A3-S3 · narration
**Picture:** LVA V13, an Army or rescue still from the Commons set, slow push in on the men. Beige cite card: "By the first night, it was obvious it was not a rescue." · Dick Whitehead, the sheriff's son · C-VILLE, 2019.
> Dick Whitehead was the sheriff's son, almost eighteen. By that first night, he told C-VILLE, everybody could see it wasn't a rescue anymore. Thirty people from the county's school system lost their lives, he said. Three of them were in his own class, and one was Warren Raines's sister, Johanna.
**Rows:** [factcheck-A3 S3: C-VILLE raw, "almost 18"; "By the first night, it was obvious it was not a rescue."; "Thirty in the Nelson County school system died, he says ... Three were in his class, including Warren Raines' sister, Johanna."]
*([RS] [VE] the quote card lands on "not a rescue". [HUMAN]. Ties back to the Raines family from Act 1.)*

### A3-S4 · narration
**Picture:** LVA V01, aerial of Massies Mill, slow push. Then our own map: the Tye River drawn from Massies Mill down toward the James, a small unlabelled marker at Massies Mill, waiting.
> You met the rest of the Raines family back at Massies Mill. About a week after the flood, the family's funeral was held, and Warren says his little sister Ginger still hadn't been found.
**Rows:** [factcheck-A3 S4: C-VILLE raw, Warren Raines, the funeral about a week after the storm, "My little sister hadn't been found then"] · [V01]
*([HUMAN]. Micro-loop across the ad: where was Ginger? Paid in A3-S8.)*

### A3-S5 · narration
**Picture:** a two-column counter of our own builds on screen, "KNOWN LOST" and "MISSING". Popfig "Aug 22, 1969". MISSING fills to "100+" on the second sentence; KNOWN LOST stays blank (no dead count spoken). Source line: "Associated Press, Aug 22, 1969 (The Pontiac Press, p. 1)".
> So the count changed every day, and the papers printed each new number. On Friday the twenty-second, the Associated Press said at least a hundred people were missing.
**Rows:** [factcheck-A3 A1: AP, Pontiac Press 22 Aug 1969 p. 1, "State police said at least 100 persons were missing", image-checked]
*(Sets the object the hinge pays: the missing count, still climbing.)*

### A3-S6 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, no narration under it. One glance chip on "a hundred and ten": "110+ MISSING · AUG 23 · AP". Source line: "Associated Press, Aug 23, 1969 (The Pontiac Press, p. 1)". Cut out on his last word, straight into the ad.
> By Saturday, August twenty-third, more than a hundred and ten people were listed as missing in Virginia. Watch what that number does next.
**Rows:** [factcheck-A3 A2: AP, Pontiac Press 23 Aug 1969 p. 1, "More than 110 persons were listed as missing", image-checked]
*(23 words. [cta-hinge open]: the missing at its peak; what happens to it?)*

### CTA · book ad (config.yaml channel.cta, 24 s, 1.0 s dips)

### A3-S7 · narration
**Picture:** back on the counter, MISSING at "110+" from before the ad. It ticks down to "109" (popfig "Aug 24 · AP"), then to "89" (popfig "Aug 25 · UPI"). Source lines change with each step: "Associated Press, via The Pontiac Press, Aug 25, 1969, p. 7" then "United Press International, via The Pontiac Press, Aug 25, 1969, p. 62 · AP and UPI counts differ". KNOWN LOST climbs on the last sentence with no number shown, only an arrow.
> The missing fell. On Sunday the twenty-fourth, the Associated Press had it at a hundred and nine. By Monday, United Press was reporting eighty-nine. Searchers were still out in the mountains, looking. And all that week, the number of people known to have lost their lives kept climbing.
**Rows:** [factcheck-A3 A3: AP, "the toll rose Sunday to at least 74 dead, 109 missing"] · [factcheck-A3 A4: UPI, "At least 75 were known dead and 89 missing"] · [factcheck-A3 A: known dead 46, 60, 74, 75 across 22 to 25 Aug]
*([cta-hinge paid] in the first three words, with its referent named. [RS] [VE] the counter running down. Dead counts kept off screen so no three numbers clash. Micro-loop: how low does it go?)*

### A3-S8 · narration
**Picture:** our own map again: the marker at Massies Mill slides down the Tye toward the James, label "20 miles". Then VCU reel V16, the James in flood after Camille, real moving water, about 4 s.
> The search went on for weeks. Ed Tinsley worked twenty-seven straight days in the county. Ginger Raines was found two weeks after the flood, twenty miles away. She'd turned seven just before it.
**Rows:** [factcheck-A3 S2: WTKR raw, Tinsley "labored 27 straight days helping the county recover"] · [factcheck-A3 S4: WTKR 2 Sep 2019 raw, "The remains of their baby sister Ginger were discovered two weeks later. 20 miles away. 'The flood happened after her 7th birthday,' says Warren."] · [V16]
*([HUMAN] [RS] [VE] the marker running twenty miles. Pays the S4 micro-loop. Real clip beat: V16.)*

### A3-S9 · narration
**Picture:** a clean card, Virginia outline, popfig "Nov 13, 1969". Two bars build one at a time, "113" then "39 still missing". Source line: "USGS Open-File Report 70-51, p. 1". On the last sentence a beige cite card: "thirty-nine missing and presumed dead" · Encyclopedia Virginia, timeline (the source's own words; soft flag word on screen, quoted).
> By November thirteenth, 1969, the state had counted a hundred thirteen people who'd lost their lives. Thirty-nine were still missing across Virginia. That's almost three months after the flood. Encyclopedia Virginia still lists those thirty-nine as missing.
**Rows:** [N11: OFR 70-51 p. 1, CONFIRMED raw] · [P1: WSP 2030 p. 147, RAW] · [factcheck-B: CONFIRMED] · [factcheck-A3 S9: Encyclopedia Virginia raw, "thirty-nine missing and presumed dead"]
*(The only dated official pair. Micro-loop: so why does every source since give a different number?)*

### A3-S10 · narration
**Picture:** our own graphic: four number cards in a row, each with its source line and a one-word tag of what it counts: "113 · Virginia, found, Nov 1969 · USGS" · "124 · Nelson County · Virginia Dept. of Health" · "150 · Virginia, later count · USGS 1973, 1999" · "153 · Virginia, later count · National Weather Service". On "a hundred fifty" a small inset under the 150 card: "125 in Nelson · USGS PP 804" (screen only). On "Nelson County alone" a ghost tag "124 · Virginia? · Encyclopedia Virginia" flickers under the 124 card. No arithmetic drawn between them.
> I lined up every count I could find since then, and they don't agree. The hundred thirteen counts only the people who'd been found. One Geological Survey report from 1973 puts Virginia at about a hundred fifty. The Weather Service goes as high as a hundred fifty-three. And the hundred twenty-four you'll see in a lot of places is Nelson County alone. They're measuring different things: the whole state or one county, the found or the missing, 1969 or years later. And not one source I read shows how those later totals were built.
**Rows:** [N11, P1: 113 and 39] · [P4, P7, N13, factcheck-A3 S10: 150] · [P8, P9, P10: 153] · [factcheck-A item 3: VDH "In total, 124 people died in Nelson County"] · [factcheck-A3 S10: PP 804 raw "About 150 people, 125 of them in Nelson County, died"; no source says how 150 or 153 was built] · [P11: Encyclopedia Virginia raw "Virginia counted 124 deaths"]
*([RS] [VE] the four cards. Scope held: 150 to 153 only as later counts, 124 only as Nelson.)*

### A3-S11 · narration
**Picture:** the 2019 list fills the frame, a slow scroll of names under the heading "The dead". Source line: "Nelson County · News & Advance, 2019 (Oakland Museum list)". A counter in the corner reaches 125.
> The closest thing to a final answer for Nelson County is a list of names. The Oakland Museum put it together, and the Lynchburg paper printed it in 2019. It has a hundred twenty-five people on it. Eighty-four of them were found and named. Every line gives a name, an age and the place that person lived.
**Rows:** [factcheck-A3 S11: News & Advance 2019, Wayback raw, recounted; 84 under "The dead"]
*(Micro-loop: and the other forty-one?)*

### A3-S12 · narration
**Picture:** the scroll stops on the heading "The missing". Two rows highlight in amber: "Wood, Donna Fay, 18, Massies Mill" and "Wood, Gary, 4, Massies Mill". Then a beige cite card: "Two of the Wood children—Donna Fay and Gary—were among the 33 people whose bodies were never recovered." · C-VILLE Weekly, 2019. On the last sentence, nineteen rows ending "Davis Creek" light up together. Source line: "19 never found + 33 named under The dead = 52 · News & Advance 2019 list; C-VILLE, WHSV 2019".
> The next heading is the missing, and thirty-three people from Nelson County are on it. There you'll find Donna Fay Wood of Massies Mill. Her little brother Gary is there too. Neither of them was ever found. Nineteen of them came from one place, Davis Creek. Folks at Davis Creek still say the creek took fifty-two people.
**Rows:** [factcheck-A3 S12: list raw, Wood rows under "The missing"; 19 of 33 rows Davis Creek (18) or Davis Creek area (1); 33 Davis Creek rows under "The dead"; 33 + 19 = 52 = C-VILLE and WHSV "52 people died at Davis Creek"] · [C-VILLE 14 Aug 2019, raw]
*([A1 loop paid]: what happened to Donna Fay and Gary. [HUMAN] [RS] [VE] the two rows turning amber, then the Davis Creek rows. Ages on screen only; I1-S10 said them.)*

### A3-S13 · narration
**Picture:** the scroll moves on to the last heading, "The unidentified". Eight rows, the text softened so no age or place reads; one small amber marker per row. Source line: "News & Advance, 2019 (Oakland Museum list)". Hold, then cut to the chapter blackout.
> The list has one more heading, and it's the shortest. Eight people were found, and nobody could say who they were. Each one is written down the only way anyone could, as a guess at the age and the place they were found. Fifty-seven years on, can anyone still give them back their names?
**Rows:** [factcheck-A3 S13: 8 under "The unidentified", counted] · [factcheck-A item 3: 1969 list entries by approximate age and place found] · [VDH media update 28 Aug 2026]
*(Out: hands to Act 4, the 2026 appeal. [L1] in front of the viewer again; the one chapter-exit question. No ages, no river on screen. Chapter blackout after this segment.)*

# A4 · Act 4, the eight (draft 3, 22 Oct 26, act writer: factcheck-A4 corrections and two grader passes applied)

Seam in: chapter blackout after A3 ("will they ever get names?"). Out: Z1 (what is still open; no source gives a dated window).
No age on screen. Ages in narration come only from the 2019 News & Advance list (factcheck-A4 "The 2019 News & Advance list"), always with "the list describes". Order: adults first, children last, one person per sentence.

### A4-S1 · narration
**Picture:** out of the blackout, popfig "Late August 2026". The VDH media-update page as a beige cite card, item heading "OCME Missing Persons Program", source line "Virginia Department of Health · media update, August 28, 2026". [VE] the card slams in on "eight people"; the line "working to raise awareness and generate new leads" highlights as it is said. Glance chip "NO AGES · NO NAMES". [RS]
> In late August 2026, fifty-seven years after that night, the Virginia Department of Health posted a few short lines on its website. The state medical examiner's office wanted help naming eight people from the flood in Nelson County. I read the notice. The office is working, in its words, to raise awareness and generate new leads. Beyond that there's no age in it, no river, and no name.
**Rows:** [factcheck-A4 S1 and S3: VDH RAW, "working to raise awareness and generate new leads"; archive heading "August 28, 2026"; WSET and CBS19 public 27 Aug 2026, so "late August"]
*([L1] back in front. Open: where does anything about the eight come from? Paid in A4-S3.)*

### A4-S2 · narration
**Picture:** our own card, two stacks side by side, never merged: left "33 never found", right "8 found, never named". Source line "Nelson County list · News & Advance, 2019". Then a date strip: "found Aug 24 to Sept 6, 1969", source line "NamUs, via CBS19, August 2026".
> Searchers did find these eight, between five and eighteen days after the flood. The water gave them back, and nobody could say who they were.
**Rows:** [factcheck-A4 S4: N&A RAW "Eight never were identified; 33 were never found"; CBS19 RAW "some were found that have never been identified"] · [factcheck-A4 list section: CBS19 (NamUs) found dates Aug 24 to Sept 6, 1969] (five and eighteen days: 19 Aug to 24 Aug, 19 Aug to 6 Sept)

### A4-S3 · narration
**Picture:** the list as a beige cite card, heading "The unidentified", source line "News & Advance, August 10, 2019 · information from the Oakland-Nelson County Museum of History". Our Nelson County map behind it; the eight unlabelled markers from I1-S9 return.
> For the rest, you go to the list of everyone the flood took in Nelson County, which the News and Advance published in 2019 with information from the county's history museum. It describes each of the eight by where they were found. It also says where they might have been going, and that may be why nobody here knew them.
**Rows:** [factcheck-A4 S5: N&A RAW, "Information courtesy of Oakland-Nelson County Museum of History"]
*(Open question paid. New open: where were they going, and why did nobody know them? Paid in A4-S8 and A4-S9.)*

### A4-S4 · narration
**Picture:** LVA aerial of the flooded Rockfish lowlands west of Rockfish (footage V08), slow push. On the map two markers slide onto the Rockfish River with place chips "Woods Mill" and "1 mile below". Place chips only.
> The list describes a woman of thirty-five to forty with well-groomed brown hair, found at Woods Mill on the Rockfish River. The list describes another woman in her late forties or early fifties, with wavy brown hair, found a mile below Woods Mill.
**Rows:** [factcheck-A4 S6: N&A RAW, "Female, 35 to 40 years old, well-groomed brown hair, found at Woods Mill"; "Female, late 40s to early 50s, moderate-length brown, wavy hair, found one mile below Woods Mill"]

### A4-S5 · narration
**Picture:** LVA photograph of the Route 602 bridge washed out near Howardsville (V09). A marker lands across the county line, chip "Howardsville · Albemarle shore". Then the map widens up the James: a marker at "Buford Island", the white of the river under it.
> Then the list describes a man in his late fifties, found on the Albemarle shore at Howardsville. He's the one public radio reported just over the line in Albemarle County. Last of the adults, the list describes a woman of about seventy with long white hair, found on Buford Island in the James. The other four are the hard part.
**Rows:** [factcheck-A4 S7: N&A RAW "Male, late 50s, ... found on Albemarle shore at Howardsville"; WHRO RAW, Newell: "another was found nearby, over the Albemarle County line"; CBS19 male "in Albemarle County, not far from Howardsville"] · [factcheck-A4 S8: N&A RAW "Female, about 70 years old, long, white hair, found at Buford Island between Howardsville and Wingina"]
*(Open, said aloud: the other four are the hard part. Paid in A4-S6 and A4-S7.)*

### A4-S6 · narration
**Picture:** LVA photograph of the Schuyler dam and the bridge over the Rockfish (V07). Three markers land one by one on the Rockfish: chips "below Schuyler", "below the railroad bridge", "2 miles above Howardsville". Smaller markers than the adults'.
> They were young. Below Schuyler, the list describes a boy of about seventeen. The list describes a boy of twelve to fourteen, found half a mile below the Southern Railroad bridge. And the list describes a girl of about ten, found two miles above Howardsville.
**Rows:** [factcheck-A4 S7: N&A RAW "Male, about 17, found below Schuyler"; "Male, about 12 to 14 years old, found one-half mile below Southern Railroad bridge"; "Female, about 10 years old, ... found about two miles above Howardsville"]

### A4-S7 · narration
**Picture:** the map keeps widening down the James, past the Nelson County line, into Fluvanna County. One last small marker, chip "above Bremo · Fluvanna County". [VE] four of the eight markers turn amber one by one; glance chip "4 OF THE 8: CHILDREN OR TEENS", source line "WHRO, October 13, 2026". Score drops out under the last sentence. [RS]
> The list describes the youngest as a girl of six to eight, found in the James above the Bremo power plant, down in Fluvanna County. Four of the eight were children or teenagers. Four kids, and nobody has named them.
**Rows:** [factcheck-A4 S8: N&A RAW "Female, about 6 to 8 years old, found above the Bremo Power Plant"; Bremo Bluff is in Fluvanna County (Wiki-Bremo RAW); CBS19 "about seven or eight miles upriver from the Bremo Bluff Plant"] · [factcheck-A4 S9: WHRO RAW "four children possibly between 6 and 19"]

### A4-S8 · narration
**Picture:** the list card returns; its closing lines highlight as they are said: "believed to be traveling on U.S. 29" and "believed to have been traveling together". Our map draws U.S. 29 through Nelson County as one thin line. [VE] [RS]
> The adults, the list says, were believed to be traveling on U.S. Twenty-Nine when the floodwaters swept them away. The children, it says, were believed to be traveling together, because they had all eaten red beans shortly before the flood took them.
**Rows:** [factcheck-A4 list section: N&A RAW "the adults were believed to be traveling on U.S. 29 when they were swept away in the floodwaters. The children all were believed to have been traveling together since they had all eaten red beans shortly before they died."]
*(Open from A4-S3 paid. [L1 paid, part 1]: who the eight were, as far as the record goes.)*

### A4-S9 · narration
**Picture:** cite card: "potentially a family or families on vacation ... traveling through Virginia" · Lara Newell, WHRO, October 13, 2026. Then the map: U.S. 29 running north and south out of the frame.
> Lara Newell, the state's long-term unidentified coordinator, told public radio they may have been a family, or families, on vacation, traveling through Virginia. If they were passing through, nobody in Nelson County would have known their faces.
**Rows:** [factcheck-A4 S13 and finding 6: WHRO RAW, "potentially a family or families on vacation, Newell said, traveling through Virginia"; Newell's title, VDH RAW and 29N RAW] (second sentence is the narrator's reasoning from the first, stated as an "if")
*(A4-S3 open paid: the travelers on U.S. Twenty-Nine. [L1 paid, part 2]: why no names, as far as the record goes: they may not have been from there. The names themselves stay open.)*

### A4-S10 · narration
**Picture:** no card. Our Nelson County map, the eight markers lit; small chips pop beside them one at a time as each is said: "cremated", "autopsy", "dental records", "no DNA test". Source line under the map: "WSET, August 27, 2026 · WHRO, October 13, 2026". [VE] the markers dim on the question.
> The eight were cremated, which leaves investigators with paper: the autopsy results and the dental records made after the flood. Public radio reported that because of the cremation, DNA testing isn't possible. So if the remains can't say who they were, who can?
**Rows:** [factcheck-A4 S12: 29N RAW, WSET RAW "working with autopsy results and postmortem dental records"; WHRO RAW "making DNA testing impossible — until technological advances potentially make the process available on cremains"]
*(Spoken open question. Paid in A4-S11 and A4-S12.)*

### A4-S11 · narration
**Picture:** cite card, verbatim: "We just want to make sure that some of these older cases are highlighted, especially as time goes on, we start losing the people who had historical knowledge of events." Lara Newell, long-term unidentified coordinator, Office of the Chief Medical Examiner · 29News/WVIR, August 31, 2026.
> Newell is the one handling it, and she told 29News why a case this old matters now. Quote, "We just want to make sure that some of these older cases are highlighted, especially as time goes on, we start losing the people who had historical knowledge of events."
**Rows:** [factcheck-A4 S13: 29N RAW quote, character for character]

### A4-S12 · narration
**Picture:** LVA ground photograph from the V13 set, U.S. 29 or a Nelson County road after the flood [verify: pick the frame from V13], slow push. Glance chip "62 TO 74 TODAY".
> Medical records from a missing person could be checked against what the investigators have. That needs someone who knows which person to look for, and somebody who was a kid in 1969 is in their sixties or seventies now.
**Rows:** [factcheck-A4 S14: WSET RAW "medical records from a missing person could be compared with the information investigators have"] (arithmetic: ages 5 to 17 in 1969 are 62 to 74 in 2026)

### A4-S13 · Paul on camera, one clip
**Picture:** Paul on camera, full frame. No narration under it, no music swell; room tone only.
> Every one of those eight had a name in August 1969. Somebody, somewhere, may still remember it, and the state is asking them to say it.
**Rows:** (turning point; facts from the rows above)
*(26 words. The peak of the act, placed last before the contact card.)*

### A4-S14 · narration
**Picture:** a clean contact card, centred: "Office of the Chief Medical Examiner, Central District · OCME_CENT@vdh.virginia.gov". Held for at least four seconds. [VE] the card lifts in over the map's eight markers. [RS]
> If you remember a family member, a friend or a neighbor who went missing in August 1969, the medical examiner's office wants to hear from you.
**Rows:** [factcheck-A4 S15: VDH-MP RAW, OCME_CENT@vdh.virginia.gov, Central District; WSET RAW "someone who remembers a missing family member, friend or neighbor can help give a name"; 29N RAW same address]

### A4-S15 · narration
**Picture:** back to the map; the eight markers stay unlabelled. Popfig "October 2026". Slow fade of the score toward the close.
> As of October, all eight are still unnamed, and the state hasn't said when it expects to know more.
**Rows:** [factcheck-A4 S16: WHRO RAW 13 Oct 2026 "attempting to identify the remains of eight people"; no identification found to 22 Oct 2026; neither VDH nor WHRO gives a date]
*([L1 stays open]: the names themselves are not known, said plainly. Hand to Z1: what is still open; no source gives a dated window.)*

## Z1 · Close (about 50 s, seam in: Act 4 ends on the open appeal for the eight)

### Z1-S1 · narration
**Picture:** our own map of Nelson County at night, the rain gauge counter near its top; a clock popfig "about 2:50 AM · Aug 20". On "lights" the few house dots on the map go dark one by one. Then [RS] [VE] our cross-section from I1-S7 comes back, now dark: a tongue of soil lets go above a house in the hollow, then a second, then a third, while the clock popfig runs on to "about 4 AM". Label "debris avalanches · USGS Professional Paper 804". Source line "USGS Professional Paper 804, pp. 4 to 5, 15 to 16".
> Back on the night of the flood, at about ten to three in the morning, a strong cloudburst hit, and for a lot of people in Nelson County it cut the lights and the phones. So by then, a lot of families were sitting in the dark with no way to call anybody, and the slopes above them were still letting go. The slides went on until about four.

**Rows:** [V10, factcheck-Z1 S1: PP 804 p. 5, "A particularly strong cloudburst struck about 0250, cutting off electricity and telephones for many of the inhabitants."] · [factcheck-Z1 S2: PP 804 p. 15 "obscured because of the darkness"; p. 16 "avalanching was more frequent toward the end of the storm", "at about 0400 hours on August 20"]

### Z1-S2 · narration
**Picture:** LVA aerial of the Rockfish River lowlands (footage V08), slow push; our map draws the Rockfish running down into the James. Eight small unlabelled markers, six along the Rockfish and two on the James (one of them above the Rockfish mouth), no ages. Chip "8 STILL UNNAMED". Source line "Virginia Department of Health · August 2026 · WHRO, 13 Oct 2026".
> The water carried people down into the Rockfish and the James, some of them miles from where they went in. Eight of them are still waiting for a name.

**Rows:** [factcheck-A3.md S4, CONFIRMED: Ginger Raines found about two weeks later, 20 miles away] · [factcheck-A item 3: the 1969 list's find places, six unidentified from the Rockfish, two from the James] · [factcheck-A item 3, factcheck-Z1 S3: VDH media update 28 Aug 2026, eight still unidentified, CONFIRMED as of 22 Oct 2026; WHRO 13 Oct 2026] · [verify: re-read VDH page on publish day]

*([L1 closes] honestly: the names are still open, and the line says so.)*

### END-ASK · config.yaml channel.end_ask (two clips, back to back)

### Z1-S3 · narration
**Picture:** the close card, The Warning Hour title, close bed under it. Narration only (no Paul on camera).
> Disasters don't ask permission. But they do send warnings. Learn what yours sounds like, so when it comes, you already know what to do. This was The Warning Hour.

**Rows:** (signature line, DESIGN.md "Signature closing footnote", canonical wording; no row)
