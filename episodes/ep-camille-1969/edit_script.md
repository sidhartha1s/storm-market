# ep-camille-1969 · edit_script.md (draft 1, 21 Oct 26: H1, T1 and I1 in full prose; acts as briefs only)

Lane: documentary (`/storm-episode`). Built on candidate 1 in `angle.md`, which waits for the owner's lock: the ticked line's
"deadliest part" broke on the sources and its twist is spent by two 2026 videos (`angle.md` "What the fact pass did"). If he
picks another candidate, H1, T1 and I1 are thrown away, not adapted. Facts: `research/facts-national.md` (N rows),
`research/facts-virginia-flood.md` (V rows), `research/facts-toll-people.md` (P rows); viewer comments:
`research/comment-bank-entries.md`. Status: DRAFT, phases 0 to 3 only (no TTS, no sourcing, no render).

## A. Header
- **Title:** none yet. Packaging follows the angle lock (`references/angle.md` order of work).
- **Target runtime:** not set. Proposed about 20 min (4 acts of 3 to 6 min plus hook, intro, CTA and close); the owner confirms it.
  `word_budget.py` has not run: it needs two probe wavs at the shipping tempo, and this round has no TTS. Planning pace: Joplin's
  measured 182.8 wpm on the Paul clone, so about 3,300 narration words for 20 min.
- **Claim (pending lock, copied from `angle.md`):** Camille's Virginia flood still is not closed: fifty-seven years later the state is asking for help to name eight people recovered from the Rockfish River, and about thirty-two more from Nelson County were never found at all.
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
  - About 32: never found, Nelson County (WHSV 2019; 33 in C-VILLE and the News & Advance). No primary. `[verify]` stays until one is found.
  - Eight: remains recovered around the Rockfish River and never identified (VDH via 29News/WVIR and WJLA, 31 Aug 2026).
  - Rain: 27 to 28 inches in central Nelson County in about 8 hours from about 7 p.m. on the 19th (N9). 31 inches near the Tye is
    "widely publicised" and unverified: never said.
  - "Probable maximum": the 1956 Weather Bureau study for the Corps of Engineers, 28 in in 6 h and 31 in in 12 h (N10). Never
    "the most rain physically possible".
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
  Writer's self-score for this draft: H1 9, T1 8, I1 8 of 10 on "a person talking to you".
- Numbers spoken the way a person says them, spelled out for the voice; years stay digits. One count per sentence.
- Flag words: no "killed" anywhere; "died" once, inside the count line I1-S10; "drowned" once, as the source's own contrast (I1-S7).
- The eight: the news copies describe seven people by age (two adults 30 to 50, one older woman 50 to 70, two teens 15 to 19,
  two children about 8 to 12) against a headline of eight. No age goes on screen until the VDH text is read.

## Loop table
| Loop | Plant | Pay |
|---|---|---|
| L1 episode: will the eight get their names, and why do they still not have them? | H1-S1 | A4 (the appeal, what is known, what is still open) and Z1 |
| Q1: how does one night of rain take people so completely? | T1-S3 | I1-S3 to I1-S7 in part (rain, slopes, injuries); in full across A1 and A2 |
| Q2: why there, two nights after landfall? | I1-S2 | I1-S3 |
| Q3: what does rain near that limit do to a mountain? | I1-S5 | I1-S6 |
| Q4: how many is "some"? | I1-S8 | I1-S9 and I1-S10 |
| Q5: where does the answer start? | I1-S11 | A1 (carried into Act 1) |
| A1 loop: what happened to the Wood children? | A1 | A3 (never recovered) |
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
chips (2 to 4 words, one at a time): "NAMED BY NOW?" on "has a name by now"; "8 STILL UNNAMED" on "eight of them", source line below
it: "Virginia Department of Health · August 2026". Cut out on his last word.
> A flood in 1969. You'd figure everyone it took has a name by now, right? This summer, Virginia asked for help naming eight of them.

**Rows:** (the viewer's belief, no row) · [VDH appeal, 29News/WVIR 31 Aug 2026; WJLA]

*(25 words. First break on the viewer's own answer. [L1 open]: who are they, and why no names?)*

## H1 alternatives (the owner picks one)
- Alternative 1 (24 words): "A hurricane in 1969. By now every person it took is counted and named, right? Virginia's still looking for eight names this year." Rows: VDH.
- Alternative 2 (26 words): "Camille, 1969. You know it as the Mississippi storm, right? Fifty-seven years later, Virginia is asking the public to help name eight people it took." Rows: VDH, N14. (Leads on the coast belief, which FAULT LINES and Dark Horizon already break: weaker.)
- Why the pick: the viewer's answer ("yes, of course they're named") is broken by a fact from this year, inside 10 s, and the second break follows at once in T1-S1.

---

## T1 · Hook tail (about 0:09 planned)

### T1-S1 · narration
**Picture:** hard cut on the first word, never black: LVA aerial of the Tye River valley at Massies Mill after the flood, slow push.
On "thirty-two" the number lands: "about 32 never found". Source line: "Nelson County · WHSV, 2019" (to be replaced by the primary once found).
> And about thirty-two more people from that same night were never found at all. [verify: never-found count for Nelson County, 32 (WHSV 2019) vs 33 (C-VILLE, News & Advance) vs 37 (state marker 2008); primary needed]

**Rows:** [P18, P17, P16, P19]

*(Second break, the double contradiction.)*

### T1-S2 · narration
**Picture:** our own map, first appearance: the Gulf Coast lit, Camille's track drawn north and east to Virginia, then a push in to
Nelson County and a thin blue line for the Rockfish River. Label "Rockfish River · Nelson County". Glance chip "NOT THE COAST" on "Virginia mountains".
> That was Hurricane Camille. You probably know it from the Mississippi coast, but those eight were recovered along the Rockfish River, up in the Virginia mountains.

**Rows:** [VDH appeal: "recovered around the Rockfish River in Nelson County", 29News] · [N7: track]

### T1-S3 · narration
**Picture:** the map holds on Nelson County; the rain gauge counter appears at 0.0 inches, not running yet.
> So how does one night of rain take people so completely that a state is still looking for their names fifty-seven years later?

**Rows:** (the question; no row)

*([Q1 open]. No void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*

## I1 · Intro: the storm, the rain, the count (about 0:24 planned)

### I1-S1 · narration
**Picture:** ATS-III satellite still of Camille in the Gulf, 17 Aug 1969 (UW-Madison SSEC, "No copyright (U.S.)", footage row S04).
Popfig "Aug 17, 1969 · 11 PM". Our map marks Waveland, Mississippi. Label "175 mph · reanalysis 2014". Then "143 · Gulf Coast · NWS".
> Camille came ashore in Mississippi just before midnight on August seventeenth, with winds of about a hundred seventy-five miles an hour, and a hundred forty-three people on the Gulf Coast lost their lives.

**Rows:** [N1: Waveland, 11 PM CDT] · [N4: 175 mph] · [N14: 143 on the Gulf Coast]

### I1-S2 · narration
**Picture:** the track crawls inland across Mississippi, Tennessee, Kentucky, West Virginia; the storm symbol shrinks and loses its
eye. A two-bar chart builds: "Gulf Coast 143 · Virginia 113 · NWS, of 256". Glance chip "NEARLY HALF" on the line.
> Two nights later, what was left of it was crossing Virginia, and the Weather Bureau wasn't even calling it a hurricane anymore. Yet nearly half of everyone Camille took lost their lives right there, in the Virginia mountains. [verify: Camille's official status over Virginia on the evening of 19 Aug 1969, depression or remnant low, from an ESSA/NHC text]

**Rows:** [N7, N8: track and the Virginia night] · [N14: 113 of 256 = 44 %, "nearly half"]

*([Q2 open]: why there? Paid in I1-S3.)*

### I1-S3 · narration
**Picture:** the rain gauge counter starts: popfig "7 PM · Aug 19". It climbs to "27 in" while a clock runs "about 8 hours". Source
line "ESSA-Weather Bureau survey · USGS Open-File Report 70-51".
> Rain. Starting about seven that evening, in roughly eight hours, around twenty-seven inches fell on the middle of Nelson County.

**Rows:** [N9, V1: 27 to 28 in, central Nelson County, 8 hours from about 7 p.m.]

*([Q2 paid].)*

### I1-S4 · narration
**Picture:** the gauge counter freezes at 27; the survey table's own row slides in as a beige cite card: "Nelson County · 27" ·
Trash barrel · accuracy: Good · emptied afternoon before rain began". Glance chip "A TRASH BARREL".
> One of the best measurements came from a trash barrel somebody had emptied that afternoon.

**Rows:** [V5: OFR 70-51 Table 1 row: "Trash barrel", "Good", "Barrel had been emptied afternoon before rain began"]

### I1-S5 · narration
**Picture:** a second bar beside the counter, labelled "the most it figured could fall · 28 in in 6 hours · Weather Bureau study for the
Corps of Engineers, 1956". The 27 bar rises to sit just under it.
> Thirteen years earlier, the Weather Bureau had already worked out, for the Army Corps of Engineers, the most rain it figured could ever fall on that area. Twenty-eight inches in six hours.

**Rows:** [N10, V2: "the probable maximum rainfall possible in this area was 28 inches in 6 hours and 31 inches in 12 hours"]

*([Q3 open]: what does rain that close to the limit do to a mountain? Paid in I1-S6.)*

### I1-S6 · narration
**Picture:** our cross-section of a steep wooded slope above a creek and a house; the soil darkens with water, then a long tongue of
it lets go and runs down into the hollow. Label "debris avalanche · USGS Professional Paper 804". Then a USGS photograph of a scar.
> On the steep slopes above the creeks, the soaked ground let go in the dark, and whole hillsides came down into the hollows where people were asleep.

**Rows:** [V29 to V33: debris avalanches, where and how] · [P9: NWS Sterling, "Most residents were asleep during the storm"]

*([Q3 paid].)*

### I1-S7 · narration
**Picture:** the cross-section holds; a beige cite card: "died from broken bones and other blunt-force injuries, rather than by
drowning · USGS Professional Paper 804, 1973". Glance chip "NOT THE WATER".
> When the geologists studied it afterward, they found most of the people the flood took there hadn't drowned. They had broken bones and blunt-force injuries.

**Rows:** [V34, P7: PP 804 abstract] [verify: V34 and P7 are FETCH status; re-read the abstract sentence raw]

*([Q1 partly paid]: the water was only half of it.)*

### I1-S8 · narration
**Picture:** the map, Nelson County outlined; a grid of a hundred small figures, one turns amber. Label "about 1 in 100 · Nelson County,
1970 census 11,702". Source line for the count: "Nelson County · NWS: 123 and 126 · state marker: 114 and 37 missing".
> In Nelson County, more than a hundred twenty people lost their lives. That's about one in every hundred people who lived there. [verify: "more than a hundred twenty" against the Nelson counts 114 + 37 missing, 123, 124, 125, 126; and "about 1 percent" against USGS OFR 99-518 raw text and the 1970 census primary]

**Rows:** [P9, P10, P15, P16, P19] · [P5: USGS 1999 "about 1 percent"] · [P24: 11,702]

*([Q4 open]: and how many of them are among "some"? Paid in I1-S9 and I1-S10.)*

### I1-S9 · narration
**Picture:** LVA aerial of the Davis Creek hollow (or the closest LVA frame captioned for Davis Creek); twenty-five small house
outlines along the creek, twenty-three fade. Label "2 of 25 houses left · USGS OFR 70-51".
> In one hollow along Davis Creek, two of twenty-five houses were left, and by that fall the count there was twenty-seven known dead and twenty-two still missing.

**Rows:** [N12: OFR 70-51 p. 22, "only two of 25 houses remained. Twenty-seven persons were known dead and 22 were missing from this one hollow."]

### I1-S10 · narration
**Picture:** our counter card, two rows: "113 died" and "39 missing", dated "Nov 13, 1969 · Virginia · USGS". Hold on the 39.
> By the middle of November, Virginia's count stood at a hundred thirteen people who had died and thirty-nine still missing.

**Rows:** [N11, P1: "As of Nov. 13, 1969, the State had counted 113 dead and 102 injured with 39 persons still missing."]

*([Q4 paid]: the missing are a third of the count. [L1] stays open.)*

### I1-S11 · narration
**Picture:** the map pushes into Davis Creek; popfig "Aug 19, 1969 · night". The USGS report cover and the 29News appeal headline
side by side for a beat, then away.
> I went through the federal flood reports and the state's new appeal, and the answer starts on a mountainside above Davis Creek, on the night of August nineteenth.

**Rows:** [OFR 70-51, PP 804, WSP 2030; VDH appeal] ("I went through the federal flood reports" is the presenter's own claim of work; keep it true)

*([Q5 open], carried into Act 1. First chapter blackout after this segment.)*
