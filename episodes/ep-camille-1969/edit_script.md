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
