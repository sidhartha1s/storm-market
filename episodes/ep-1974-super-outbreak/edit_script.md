# ep-1974-super-outbreak · "The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak"

Lane: documentary (`/storm-episode`). Target 22:00 ± 1:00. Title locked by the owner 20 Sep 26. Script v8
(v1 graded 7/10 hook, 6/10 overall in `research/script_review_v1.md`; v2 applied the fixes; v3 added the
researched beats; v4 applied the second grade; v5 is the spoken-sentence pass on the palette in
`references/humanise-rules.md`; v6 applies the v5 grade, `research/script_review_v5.md`, 7/10: six fact
errors, opener cap, comma splices; v7 applies the v6 grade, `research/script_review_v6.md`, 7/10, hook 8: Tanner
timeline, rhetorical questions, anaphora, balanced-contrast reflex; v8 applies the v7 grade, `research/script_review_v7.md`, 7/10, hook 8: lead-time
line inverted, Tanner duration left to fact-QC, misattributed quotes, act seam chronology, opener cap; owner
length decision: natural 19 to 20 min).
Doctrine: `references/script-os.md`, `references/script-scaling.md`, DESIGN.md (hook contract, CTA contract,
on-screen text rules). Facts: `research/fact_sheet.md` + `fact_sheet_addendum.md`; every number is `[verify]`
until the fact-QC pass clears it; zero open markers before TTS. Delivery: pocket-TTS then atempo 1.10.

## Engine settings
- **Dominant question:** the viewer keeps watching to find out *how one day made seven F5 tornadoes, and why the man
  who saw it coming a day early still lost three hundred and thirty people.*
- **Architecture:** Countdown 60 % (2 April phone call → 2:16 PM → 10:57 PM, state by state) + Detective 40 %
  (Fujita's ten months in the air, the F6 he wrote and crossed out, the straight-line damage nobody could explain).
- **Escalation:** one F5 over empty ground → a college of 1,000 with zero dead → a town of 1,700 loses 31 → a city
  loses 34 in four minutes → five hooks on one radar and the office goes dark → a city of 360,000 with a tornado
  the radar cannot see → a courthouse safe falls three floors → the same town hit twice in an hour → two hours in
  the dark → the scale's inventor doubts his scale → a wind nobody could explain → the same corridor, 2011, an
  EF5 on the rebuilt houses → 433,000 people live there now.
- **Carried question per act:** every act plants a question in its first 30 s and pays it in its last 30 s, on
  top of the act bridges (loop table).
- **Retention spikes (each with a `[VE]`):** 148 tornadoes · a bus on the stage the students just left · a 15 year
  old carries 169 people · five hooks on one scope · the weather office loses power mid-outbreak · a safe falls
  three floors · "It went through the rescuers" · "I have the thing on tape" · two hours, one hundred miles ·
  Fujita writes F6 and crosses it out · trees down like combed hair · 2011, the same path, the rebuilt church ·
  433,000 across the Tanner path.
- **Named person per act:** Pearson (I) · Tim Haley, Gus Allen (A1) · David Heath (A2) · Dick Gilbert, Rod Poole
  (A3) · Allen Lindley, Becky Todd, Mildred McGuire (A4) · Fujita (A5) · Gus Allen returns (A6).
- **Register:** plain American, a third grader follows it aloud. Clock times as digits with AM/PM on screen and
  spoken as digits ("four forty five PM"); each region's local time is named once ("Central time"); no cross-zone
  interval arithmetic. F5 is correct for 1974 (Fujita scale; EF only from 2007).

## Packaging
- **Title (locked):** The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak
- **Thumb brief:** colour plate of the Xenia funnel (NOAA Photo Library via Commons, PD-US-no-notice, confirm per
  file) or a graded Wright-Patterson aerial of the Windsor Park path; two lines of type, top of frame: "1974"
  (Abril, red) over "SUPER OUTBREAK" (white). Nothing else. Same grammar as the 2011 Super Outbreak thumb (6.5 %).
- Alternate for Studio Test and Compare: same plate, "7 F5s" replacing "1974".

## Runtime and word budget
22:00 target at atempo 1.10 (≈ 167 wpm delivered): narration ≈ 22 × 0.9 × 167 ≈ 3,300 words. v3 measures with
`research/wordcount.py`; see the number printed there. Probe-TTS H and A4-S2 at 1.10 and recompute before
trimming or adding. CTA (15.139 s, v5) at the A2 → A3 seam ≈ 7:40 ≈ 35 %.

## Chapter cards (five fields)
| # | Chapter · words | Purpose | Question | Reveal | Visual event | Exit hook |
|---|---|---|---|---|---|---|
| H | Hook · 55 | Payoff first, then the contradiction | If he knew, why did so many die? | Seven F5s, 330 dead, a day's warning, five on one screen | g-scale slam, g-radar five hooks, popfig "4:45 PM" | question |
| I | The call · 200 | The man who saw it; why knowing was not enough; the US promise | What did he do with a day's warning, and why was it not enough? | Every office phoned; a warning in 1974 is a radio that has to be on | g-master-map offices lighting; popfigs | contradiction: "nobody to warn, and that was the last time that would be true" |
| A1 | First blood · 420 | The clock starts; who is in the way | Q-A1: why does a warned town still lose 31? | DePauw over empty ground; Hanover, 1,000 students, zero dead; Brandenburg, 15 minutes, 31 dead | map tracks 1–3, g-clock, g-person | location shift: "a drama teacher and a stage" |
| A2 | Xenia · 460 | The deadliest single tornado; the aftermath | Q-A2: thirty minutes, and still the worst; why? | The hallway and the bus; 34 dead; five schools by name; 1,445 Guardsmen; Nixon in a helicopter | g-clock, bus photo hold, aerial scar, g-scale bar 3, citation card | reveal tease → CTA |
| CTA | 15.139 s | must-keep | | | 1.0 s dips | |
| A3 | Five on one screen · 560 | Payoff (F6); the peak; the office that went dark; a city; a courthouse | Q-A3: the radar sees rain, not wind; how do you warn a city of 360,000? | The verbatim warning; power out 5:40 to 8:53 PM; Gilbert; Monticello's safe | g-radar, citation card, map surge, g-person ×2 | escalation: "the sun was still up" |
| A4 | Alabama after dark · 440 | Night; the same town twice; the tape | Q-A4: two F5s hit one town an hour apart; which one killed whom? | Rescuers under the second; Guin for two hours; the tape; Becky Todd's sons | g-clock, map southern arm, waveform, g-scale complete | consequence: "count everything else" |
| A5 | Ten months in the air · 470 | Detective act; the one machine | Q-A5: what did the map show that nobody expected? | 148 tracks by hand; the F-scale ladder; one air mass; F6 taken back; combed trees = microburst | g-survey, g-mechanism ×2, g-scale | present-day return: "not farmland any more" |
| A6 | The same corridor · 520 | 2011 on the same ground; answer the dominant question in the last 45 s | Q-A6: would the warning reach you? | 2011 EF5 on the rebuilt church; 16 dead then, 4 now, with 2.5× the people; the warning travels; the houses moved | g-master-map 1974 + 2011 + today, g-then-now, Gus Allen returns | thesis in the final 45 s |
| Z | Close · 50 | END CTA spine | | | g-outro | |

## Loop table (plant → pay)
| Loop | Planted | Paid |
|---|---|---|
| EPISODE: if he knew, why did so many die | H | A6-S3 (final 45 s) |
| L4: the corridor is the fastest growing city in the state today | I | A6-S1 |
| Q-A1: why does a warned town still lose 31 | A1-S1 | A1-S2 |
| L2: a drama teacher and a stage | A1-S3 | A2-S2 |
| Q-A2: thirty minutes, and still the worst; why | A2-S1 | A2-S3 |
| cta-hinge: "his own scale was too small" | A2-S5 | A3-S1 |
| Q-A3: the radar cannot see wind; how do you warn a city | A3-S2 | A3-S3 |
| Q-A3b: what happens when the office itself goes dark | A3-S2 | A3-S2b |
| L3: the sun was still up | A3-S5 | A4-S1 |
| Q-A4: which tornado killed whom | A4-S1 | A4-S1 (unanswerable, said so) |
| Q-A4b: the tape | A4-S2 | A4-S2 |
| L5: count everything else | A4-S3 | A5-S1 |
| Q-A5: damage no tornado could have made | A5-S1 | A5-S4 |
| L6: not farmland any more | A5-S4 | A6-S1 |
| Q-A6: the same path, 37 years later; what happened the second time | A6-S1 | A6-S1b |
| Q-A6b: would the warning reach you | A6-S1b | A6-S2 |

## Motion graphics (hand-authored comps, library first; each ≥3 type tiers, continuous motion)
g-master-map (one comp, seven fill states: outline · tracks 1–3 · surge · southern arm · Fujita's hand map ·
the 2011 path over the 1974 tracks · today's footprints; ep3 map-route-fit pattern; distances measured on the
plate) · g-clock (the #4 clock anatomy) · g-radar (WSR-57 scope, label "CINCINNATI WSR-57 · APRIL 3, 1974") ·
g-scale (seven F5 bars) · g-person · g-survey (tracks drawn by hand, date ticker) · g-mechanism (three cards:
the one-air-mass engine; how a rating is read from a house, F2 to F5 in the SPC wording; combed trees vs
rotated trees) · g-then-now (1974 vs 2011 vs today) · citation cards (the verbatim CVG warning, the CVG report's
closing line, the Athens newspaper line) · g-outro. **Red popfigs** (Abril, ≤3 words, mid-screen) for every
date, time and count while the voice says the human version. Footage: NOAA Photo Library and Wright-Patterson
aerials (PD), Commons Xenia set (licence per file), NWS Wilmington and Louisville galleries (licence per set),
WHAS archive (licence), NWS 50th-anniversary video (PD), Nixon Library 9 April 1974 material (PD, confirm),
FEMA (PD), our own 2011 episode's PD pool for A6, stock as fill only.

## Inserts (audio-carrying; owner YES before any render)
1. `ins-hook-whas` (hook, ~4 s): Dick Gilbert's live WHAS-AM report. LPM/WHAS archive [licence]. Transcribe first.
2. `ins-guin-tape` (A4, ~6 s): Allen Lindley's Guin recording. Tornado Talk hosts it [rights]. If rights fail, a
   waveform card over narration; no fabricated audio.
3. `ins-nws-50th` (A5 or A6, ~5 s): an NWS 50th-anniversary interview line [PD if NWS-produced, confirm].
All other broadcast pulls muted, narrated over, ≤ 8 s, `.bc` grade class, never the same cut twice.

---
## SCRIPT (readable form; TTS pass spells numbers, respells homographs, splits sentences over 24 words;
`[VE]` visual event · `[RS]` spike · `[HUMAN]` named person · `[Q]` open question · `[PAY]` payoff)

### H · hook (0:00–0:25, 55 w) · frame one mid-action: the scope, hooks blooming; popfig "APRIL 3, 1974 · CINCINNATI" inside the first second
*(ins-hook-whas under the first two seconds, ducked as the narrator enters)*
Seven F5 tornadoes in one day, and it has never happened again. [verify] [VE g-scale seven bars slam in]
Three hundred and thirty people dead. [RS] [VE g-radar: five hooks on one scope, popfig "5 HOOKS · ONE SCREEN"] Five
tornado hooks on one radar screen at once, and the worst of the night hadn't even formed yet. And the man who ran the
national forecast office knew it was coming a full day early. He knew, and three hundred and thirty people died anyway. [Q]
*(probes: `audio/probe/hook_plain_110.wav`, `demo_mixed_110.wav`; the shipped hook uses no device beyond the
contraction, per the palette)* *(1.5 s void)*

### I · the call (0:25–1:55, 200 w) · g-master-map v1, thirteen states outlined and empty; popfig "APRIL 2, 1974 · KANSAS CITY"
The day before, a man named Allen Pearson picked up a telephone. [HUMAN g-person Pearson] He ran the Severe
Storms Forecast Center, and the charts for the third of April scared him. He called every weather office in the
eastern half of the country and told them to fix their radar that night and bring in extra people the
next day. [VE map: the offices light up one by one] He was right about the day and he was right
about the place. The watches went out, the warnings went out, and people still died, because in 1974 a
warning was a voice on the radio, and a radio has to be switched on. [RS] After it was over, the Weather Bureau found that most people didn't know
it could forecast a tornado at all, or what a tornado watch was. [verify wording]

A hundred and forty eight tornadoes in less than a day, [VE popfig "148"] across thirteen states and a piece
of Canada, and two thousand six hundred miles of ground ripped up end to end. [VE popfig "2,600 MILES"] Seven
of those tornadoes sat at the top of a scale that was only three years old. And the man who invented that
scale was about to fly over every one of those miles and doubt his own numbers. And the corridor that took the
worst of it, in north Alabama, is the fastest growing city in the state today. [Q L4] The first F5 touched
down at 2:16 PM over farm country, and for the next eight hours most of the ones that followed found a town. [Q] *(blackout 0.7 s)*

### A1 · first blood (1:55–4:50, 400 w)
**A1-S1 (100 w) · g-clock "2:16 PM CDT" · g-master-map track 1.** The first F5 of the day came down south of
Huffman, Indiana, at 2:16 PM, Central time, [VE track drawn] and for sixty two miles it stayed over farmland,
through six counties and never a town. Six people died, in farmhouses that happened to be in the way. An hour and
a quarter later a town with a warning, with fifteen minutes to get ready, would lose twenty eight people, and thirty one along the whole path. [Q Q-A1]
The warning reached that town in time, and it still lost twenty eight people, and the reason is what was under
the houses.

**A1-S1b (110 w) · g-clock "3:51 PM EDT" · Hanover College stills, Ken Burns · track 2a.** At 3:51 PM, Eastern
time, a tornado hit Hanover College near Madison, Indiana, with nearly a thousand students on campus and some
of them still in class. [VE track] More than thirty of its thirty three buildings were damaged and two were destroyed,
[RS] [VE campus plan, buildings going dark one by one] and on that campus nobody died. The college still calls
it a miracle. Down the hill in the town of Madison seven people died from the same line of storms, in the
same minutes.

**A1-S2 (130 w) · g-clock "3:30 PM CDT" · track 2 · g-person Tim Haley.** The tornado that hit Brandenburg,
Kentucky, formed at 3:30 PM, Central time, and the town had fifteen minutes of warning. [VE clock] The tornado came up
the Ohio River toward the town so low and so wide that people said it looked like a wall, [VE bc pull, muted]
and it was half a mile across. A hundred and twenty eight homes and thirty businesses were gone from a town
of seventeen hundred, [verify population] and thirty one people were dead along its path. [RS] [PAY Q-A1] Fifteen minutes is
enough to get below ground, but few homes in Brandenburg had a below ground to get to. [verify] [HUMAN] A boy
named Tim Haley, he was fifteen. He spent that night carrying people out of the wreckage, a hundred and sixty
nine of them by his own count. [RS] [VE popfig counter ticking to 169 over a Brandenburg still] One of them
was a baby he had to take from a mother's arms so he could get her to safety. He became a soldier later, and fifty years
on he called that night pretty, pretty traumatic.

**A1-S3 (80 w) · g-person Gus Allen · g-scale bar 2 lit.** [HUMAN] Gus Allen lost his sister, his brother and a
two year old cousin in the same minutes, and his mother was carried about a mile by the wind and lived. Fifty
years later he described that day in one sentence. It was just a bad day. *(hold 3.0 s: Brandenburg memorial,
slow push, wind bed only, no voice)* [VE g-scale two bars lit, five dark] While that tornado was still on the ground,
about a hundred and seventy miles to the northeast, in Xenia, Ohio, a drama teacher was walking his students onto
a stage. [Q L2] *(blackout 0.8 s)*

### A2 · Xenia, 4:40 PM (4:50–7:40, 450 w)
**A2-S1 (100 w) · g-clock "4:10 PM EDT" → "4:33" → "4:40" · track 3.** Dayton's weather office put a tornado
warning on Xenia at 4:10 PM, Eastern time, [VE clock] which gave the town thirty minutes, and in 1974 thirty
minutes was a gift. Xenia still became the worst-hit town of the whole day. [Q Q-A2] At
4:33 a funnel came down near Lower Bellbrook Road, [VE track] and at 4:40 it was in the middle of the city,
half a mile to a mile wide. It went through Windsor Park and Arrowhead, streets full of the houses people
had bought after the war.

**A2-S2 (90 w) · g-person David Heath · Xenia High School footage, muted.** [HUMAN] At Xenia High School a
teacher named David Heath was rehearsing a musical with his students, and they were up on the stage when
something made them move. They went out into the main hallway, and seconds later the wind picked up a school
bus and dropped it on the stage, [RS] [VE popfig "A SCHOOL BUS"] right where they had been standing. *(hold
4.0 s: the bus-on-stage photo, slow push, rain bed only, no voice)* Not one of them was hurt, and everywhere
else in Xenia it went the other way.

**A2-S3 (170 w) · g-scale bar 3 lit · Wright-Patterson aerials, Ken Burns · popfig "5 SCHOOLS".** Thirty four
people died along that path, thirty two of them inside the city, and about twelve hundred were
hurt. Fourteen hundred buildings were damaged or gone, and five schools were destroyed: Xenia
High, Central Junior High, McKinley, Simon Kenton and Arrowood. [VE the names, one by one, over the aerial
scar] [PAY Q-A2] Xenia got its thirty minutes, and the tornado still took five schools, fourteen hundred buildings
and thirty four people, because thirty minutes moves you across a room, not out of a city. [HUMAN g-person Gilligan] That same evening Governor John Gilligan sent two hundred
and fifty National Guardsmen into Xenia, and by midnight fourteen hundred and forty five were on duty across
Ohio, more than half of them in this one town. [RS] [VE popfig "1,445 GUARDSMEN"] They spent the night
pulling people out of the houses on Windsor Park and Arrowhead, street by street, with the power out and the
rain still coming down. [verify rescue detail]

**A2-S4 (45 w) · Nixon Library material, muted, 6 s · popfig "APRIL 9, 1974".** Six days later President Nixon
walked the streets of Xenia, [HUMAN] [VE Nixon footage] and those pictures are the reason most people who
remember 1974 remember one word, and that word is Xenia. But Xenia was one tornado out of a hundred and forty
eight, and fifty miles away in Cincinnati the afternoon was about to get worse.

**A2-S5 (25 w) · cta-hinge tease.** Weeks later the man who invented the tornado scale flew over these streets,
and wrote down a number his own scale did not have. [Q cta-hinge] *(1.0 s dip)*

### CTA (≈7:40, 15.139 s, v5) *(1.0 s dip)*

### A3 · five on one screen (8:00–11:30, 560 w)
**A3-S1 (60 w) · [PAY] · g-survey close-up: a hand-written "F6", struck through.** He wrote down a six. [PAY] Ted
Fujita's scale ran from zero to five, and in his first notes on Xenia he wrote F6, [RS] [VE the F6 written,
then crossed out] then decided a six was a rating nobody could believe and took it back. Xenia stayed an F5.

**A3-S2 (130 w) · g-radar Cincinnati WSR-57 · citation card: the 4:05 PM warning, verbatim.** The radar at the
Cincinnati weather office was built in 1960, and it could see rain but it couldn't see wind.
[VE the scope, one sweep at a time] A tornado showed up only as a hook on the edge of a storm, if it showed up
at all, so the office was warning a city off a shape. [Q Q-A3] At 4:05 PM
the office put out a tornado warning for Hamilton County, and the reason it gave was hook echoes on the radar. [VE citation
card: the 4:05 PM warning, full clause] [RS] Twenty seven minutes later the hook it was looking at
came through Sayler Park on the west side of Cincinnati, and four people died in that county. [verify] By then
the office was looking at five hooks at once, [RS] [VE five bloom] [Q Q-A3b] and then, at 5:40 PM, his
office went dark.

**A3-S2b (90 w) · citation card: the CVG report · popfig "5:40 PM · POWER OUT".** [PAY Q-A3b] The Cincinnati
weather office lost power at 5:40 PM, in the middle of the outbreak, [VE the scope goes black] and with it the
radar, the teletype and the incoming phone lines. For three hours the office that had been warning half of
Ohio had to call Cleveland on whatever phone still worked and ask Cleveland to send its warnings out. [RS]
[VE map: the Cincinnati office goes dark, Cleveland lights up] Its own report six days later said the warnings
had saved many lives, and it also recorded seven dead in its area. Somewhere in that evening, fifteen
tornadoes were on the ground at the same time. [verify: Wikipedia only, no clock time in any source] [VE map surge: tracks 4 to 40]

**A3-S3 (140 w) · g-person Dick Gilbert · ins-hook-whas full line (owner YES) · Louisville track · popfig "361,000".**
In Louisville, Kentucky, an F4 touched down inside a city of three hundred and sixty thousand people at
5:37 PM, Eastern time, [verify: fact_sheet table converts 21:37 UTC to 4:37, the addendum says 5:37; 21:37 UTC is 5:37 PM EDT] and the radar couldn't see it. [VE track] [HUMAN] What could see it was a
helicopter. Dick Gilbert reported traffic for WHAS radio, he grew up on Pennsylvania Avenue in Crescent Hill,
and the tornado was on his street. He stayed. He stayed in the air, followed it, and told the whole city block
by block where it was and where it was going. [VE the track advancing with his words; insert audio] It tore the
roof off Freedom Hall at the fairgrounds and wrecked the Crescent Hill water station while he talked. [PAY Q-A3] Two people died in Louisville, and the
President sent him a special commendation for it. [RS] [VE g-person Gilbert card, "COMMENDED BY THE PRESIDENT"]

**A3-S4 (140 w) · g-clock "5:17 PM" · Monticello, Indiana · g-person Rod Poole · track: the 121-mile line.**
That same evening, up north, one tornado came down near Otterbein, Indiana, and didn't lift for a hundred and
twenty one miles. [VE map] [RS] At 5:17 PM, local time, [verify: Indiana on EST in 1974] it went through the middle of Monticello, where the county
courthouse came apart and a safe on the third floor fell straight through to the first. [VE popfig "121
MILES"] A railroad bridge over the Tippecanoe River was lifted off its footings and twisted. [HUMAN] Rod
Poole, who later ran the town's water department, said the sky was a greenish brown, and that everybody says a
tornado sounds like a train, and they're right. Eighteen people died along those hundred and twenty one miles.

**A3-S5 (40 w) · g-master-map: Georgia.** And more than four hundred miles south, in Georgia, an F4 went through Sugar
Valley and Resaca, with ten dead and two hundred hurt. [VE Georgia lights up] Four states inside two hours, all off one
storm system, and the sun was still up. [Q L3] *(blackout 0.8 s)*

### A4 · Alabama after dark (11:30–15:00, 440 w)
**A4-S1 (150 w) · g-clock "6:20 PM CDT" → "7:30" · southern arm · track 5, then 6.** At 6:20 PM, Central time,
a tornado formed near Moulton, Alabama, and stayed on the ground for fifty two miles. [verify duration: table 6:20 to 7:21 PM, prose about
90 min] [VE track] Twenty eight people died along those miles, from Lawrence County through Limestone, and the
neighbors were out in the wreckage behind it pulling people out when the second one came.
[RS] [VE second track, one mile west, drawn over the first] It formed about an hour after the first, ran a
mile to the west of it for ninety eight miles, and honestly it went straight through the people doing the
rescuing. [RS] *(hold 3.5 s: the second track pulsing over the first on the map, wind bed, no voice; no
blackout after a hold)* [Q Q-A4] So two F5 tornadoes hit one small town an hour apart. To this day nobody can
say for certain which one killed whom, because the people who could have told you were the ones under the
second one. Sixteen people died in Limestone County that night, [verify] and about fifty in that one stretch
of north Alabama. [verify]

**A4-S2 (170 w) · g-clock "8:25 PM" → "10:57 PM" · track 7 Guin · g-person Lindley · ins-guin-tape (owner YES).**
At 8:25 PM a tornado touched down in Mississippi and didn't lift for over two hours, [VE clock ticking through
the segment] a hundred and one miles, one of the longest-lived violent tornadoes ever recorded. It was heading
for Guin, Alabama, a town of about two thousand five hundred people, [verify population] and it got there in full dark,
about two hours after sunset. [verify strike time] [HUMAN] A
young man named Allen Lindley put a tape recorder in an open window, [Q Q-A4b] and he got a minute of it
coming and eighteen seconds of it going over the house. [VE waveform card; insert audio if cleared] I have the
thing on tape, he said, and it's a rare recording of an F5 passing directly over a house. [RS] [PAY Q-A4b]
[HUMAN] Becky Todd was in the car with her family when it rolled, and she said George told them to grab the seats
and hold on. Her
sons Mark and Paul didn't survive. [RS] [VE g-person card: two names] Seven hundred and thirty seven houses
were destroyed in Guin that night, and twenty eight people died. [verify: 28 official / 32 revised]

**A4-S3 (120 w) · g-scale all seven bars lit · aerial of Guin · g-person Mildred McGuire.** [HUMAN] Mildred
McGuire, who ran McGuire Drugs, survived with a broken pelvis and later wrote a poem about what Guin did next,
which was rebuild on the same ground. That was the seventh F5, [VE bar 7 lit, the set complete] seven between two in
the afternoon and eleven at night, from Indiana to Alabama. Three hundred and thirty people were dead by NOAA's count, and five thousand four
hundred and eighty four were hurt. [RS] [VE
popfigs "330 DEAD" then "5,484 HURT"] And one man in Chicago was already planning to count everything else.
[Q L5] *(blackout 0.9 s)*

### A5 · ten months in the air (15:00–18:30, 470 w)
**A5-S1 (110 w) · g-survey: a small plane over the map, tracks appearing, date ticker April 1974 → February 1975.**
Ted Fujita had invented his scale in 1971, [HUMAN] and it graded a tornado from zero to five by the damage it
left, because nobody could measure the wind inside one. He had a hundred and forty eight tornadoes to
grade at once, so he flew. Ten months, more than ten thousand miles, low and slow, with every track drawn
by hand onto one map. [VE plane, tracks] [RS] [Q Q-A5] And somewhere in those ten thousand miles he
found a kind of damage that no tornado could have made.

**A5-S2 (120 w) · g-mechanism: two frames, F4 and F5, in the scale's own words · g-person Robert Pennington.**
He was grading by what was left. [VE card: a house in two states] A well-built house with its walls gone is an F4.
The same house swept clean off its foundation, with the cars a hundred yards away and the trees stripped
of their bark, is an F5. [RS] [VE the second frame: the slab, the bark] [HUMAN] In Guin, a man named Robert
Pennington came home from his shift at the electric company to that. He said there was no sign of the house,
the foundation, the framing, or anything, and his wife Juanita, who was sixty four, was found dead. [RS] [VE
g-person card] Fujita read ten thousand miles of that from the air, and seven times he wrote the top of his
scale. [verify against the DePauw damage]

**A5-S3 (120 w) · g-mechanism: the one-air-mass engine, one diagram.** And the map answered the first question,
which is how one day makes seven of them. [VE the card: warm wet air below, dry air above, the jet stream on
top, a cold front as the trigger] You take warm, wet air off the Gulf of Mexico, put a layer of dry air over
the top of it, run a jet stream above that to turn the whole column, and send a cold front through to set it
off. That ran from Indiana to Alabama, all afternoon and all night. [verify synoptic summary] Every storm that formed
in that column had the same engine. One machine made all of them, and it ran for the better part of a day. [RS] [VE the engine card cycles once, one storm after
another off the same column]

**A5-S4 (130 w) · g-mechanism: combed trees vs rotated trees · g-then-now v1.** [PAY Q-A5] In the survey photos
Fujita kept finding trees knocked down in straight lines, all in the same direction, like hair that had been
combed. [RS] [VE the card: rotation pattern vs straight-line pattern] A tornado can't do that, because a
tornado turns things. Nothing in the science of 1974 explained it, so a few years later he gave it a name, the
microburst. It went on to explain why airliners were falling out of the sky near thunderstorms. [verify]
The country used the rest of his map too, and weather offices got backup power. [VE row lights] The case
for a radar that could see wind finally had its evidence, and the Doppler network that watches the same sky
today grew out of days like this one. [VE "contributed"] And the corridor the map drew across north Alabama is
not farmland any more. [Q L6] *(blackout 0.8 s)*

### A6 · the same corridor (18:30–22:00, 520 w)
**A6-S1 (150 w) · g-master-map: the 2011 path drawn over the 1974 Tanner tracks · popfig "APRIL 27, 2011".** Put
another map on top of the 1974 tracks. [VE] On April 27th, 2011, an EF5 tornado came down at Hackleburg,
Alabama, and ran a hundred and thirty two miles across five counties, and it killed seventy two people, the
deadliest single tornado in the state's history. [RS] [VE popfig "132 MILES · 72 DEAD"] In Limestone County it ran straight down the
1974 Tanner corridor. [Q Q-A6] It destroyed homes, a mobile home park and a church that the first two Tanner
tornadoes had destroyed thirty seven years earlier, and that people had rebuilt on the same ground. [VE the two
paths lining up] A weather service meteorologist and a geography professor had been comparing the tracks for
three years before it happened, and afterward the local paper quoted them saying the paths matched almost exactly. [HUMAN citation
card] The second time, the numbers went the other way.

**A6-S1b (110 w) · g-then-now: 1974 vs 2011, two rows · popfig "16 → 4".** [PAY Q-A6] In 1974 the two Tanner
tornadoes killed sixteen people in Limestone County, [verify] and in 2011, with two and a half times as many
people living there, the EF5 killed four. [RS] [VE the two numbers] More houses in the path and fewer dead,
and the researchers said the reason was most likely better warnings. [PAY L4] Madison County next door, where the first Tanner
tornado ended, has four hundred and thirty three thousand people today, and Huntsville is the biggest city in
Alabama. [Q Q-A6b] It will happen again, and what decides the count is whether the warning reaches you.

**A6-S2 (130 w) · g-then-now v2: 1974 vs today, radar, warning, phone.** April third can happen again, because
the ingredients were ordinary spring weather for that part of the country arriving on the same
day, and every few decades they do. [verify] What changed is the warning. [VE two columns] In 1974 the radar
saw rain, and today it sees the wind turning inside the storm before the funnel exists. Back then the warning was
a radio you had to have switched on, and today it's the phone in your pocket, and it will wake you up. [verify
WEA] Brandenburg got fifteen minutes that day and most towns got nothing at all, and today the average warning
runs eight to fifteen minutes everywhere. [verify: national average lead time] [PAY Q-A6b] [RS] [VE the two columns fill, 1974 left, today right] Allen Pearson's
forecast was right a day early, and three hundred and thirty people still died, because a warning is only as good as the
radio it plays on and the basement you can reach. Today the warning reaches you, and the houses moved into
the path instead.

**A6-S3 (130 w) · g-person Gus Allen returns · Brandenburg today, muted · g-then-now v3: the fifteen minute card.**
[HUMAN] Gus Allen still lives near Brandenburg, and his sister, his brother and his small cousin are on the
memorial there. It was just a bad day, he said, and days like it come back every few decades. [PAY EPISODE] Pearson knew a day early, and the warnings he set up saved the people who heard them, and
in 1974 hearing one meant a radio that happened to be switched on. Today the warning buys you minutes. [VE card,
three rows] A storm shelter or an inside room on the lowest floor you can reach in that time, and a car
trying to outrun a mile-wide tornado is the one thing you can't. [RS] [VE third row: the car, struck through]
Know before the day comes which room in your house is the one you run to.

### Z · close (22:00–22:30, 50 w) · g-outro
Where are you watching this from, and do you have a place below ground? Tell me in the comments, I read all of
them. The 2011 Super Outbreak, the tornado that ran the same corridor, is linked below, and the Storm-Ready
Home is the first link in the description. See you in the next one.

---
## Fact register (every number above; `[verify]` = confirm from a primary source before TTS, unverified = cut)
- 148 tornadoes, 13 states + Ontario, 2,598 combined miles, 30 F4/F5, 5,484 injured: NCEI. Dead: NCEI 335 /
  NOAA 330 `[verify which figure the NCEI page carries today; use it everywhere]`.
- 15 on the ground at once `[Wikipedia only; verify or cut]`. Five simultaneous hooks: NWS Wilmington `[no
  timestamp; the hook popfig "4:45 PM" is the CVG 4:45 warning time; verify or drop]`.
- Pearson's 2 April calls `[Wikipedia; verify NWS/NOAA history]`. "Most people did not know what a tornado watch
  was" `[Weather Bureau qualitative finding only; soften to "many people" or cut]`.
- DePauw: 2:16 PM CDT, 62 mi, 6 dead, six counties `[NWS Indianapolis 404; verify]`.
- Hanover College 3:51 PM EDT, ~1,000 on campus, 30 of 33 buildings damaged, 2 destroyed, zero campus deaths
  ("miraculous"): hanover.edu. 11 dead on the track, 7 in Madison: NWS Louisville. Shelter detail `[not found;
  the line "moved when they were told" must be cut unless sourced]`.
- Brandenburg 3:30 PM CDT, ~½ mi, 128 homes + 30 businesses, 31 dead on the path (28 in the area), 15 min warning:
  NWS Louisville. Town ~1,700 `[verify 1970 census]`. "Few homes had a basement" `[verify or cut]`. Tim Haley
  `[army.mil, secondary]`. Gus Allen `[WAVE3, secondary]`.
- Brandenburg → Xenia ≈ 168 mi; Otterbein → Sugar Valley ≈ 424 mi (grader measured); "about" in the voice.
- Xenia: warning 4:10 PM EDT, touchdown ~4:33, city 4:40, ½–1 mi, 32 city / 34 path, 1,150–1,300 hurt, ~1,400
  buildings: NWS Wilmington. Five schools destroyed by name `[secondary synthesis; verify each]`. "School was
  out, buildings not empty": drama rehearsal underway `[Cedarville, secondary]`. Guard 250 → 1,445 by midnight,
  more than half in Xenia: AP via Yahoo `[secondary; verify Ohio Adjutant General record]`. Nixon 9 April, Wright-
  Patterson, helicopter, walked the town: Nixon Library almanac. "Pictures went around the world" `[editorial]`.
  Cincinnati ~40 mi from Xenia `[measure on the plate]`.
- Fujita F6 for Xenia, rating "inconceivable" `[Chicago Mag; find the 1981 Fujita/Abbey wording]`.
- CVG: WSR-57 installed 1960; warnings 4:00 PM (Butler, Warren), 4:05 PM (Boone, Hamilton), 4:45 PM; wording
  "based on hook echoes on WSO CVG radar"; power out 5:40–8:53 PM EDT, relay via WSFO Cleveland; closing line
  "saved many lives"; area toll 7 dead, 331 hurt: CVG_Report.pdf (primary). Sayler Park ~4:32 PM, "four in the
  county" `[Hamilton County 4 per CVG report; Sayler Park proper 1; say "four people died in that county"]`.
- Louisville: 361,472 (1970 census); F4 5:37 PM EDT north of Standiford Field, Freedom Hall roof, horse barns,
  Crescent Hill pumping station, 2 dead; Gilbert "Skywatch 84", Pennsylvania Avenue, Crescent Hill: LPM +
  Wikipedia `[verify the 5:37 vs 4:37 CDT clock; Louisville is Eastern]`. Nixon commendation `[verify document]`.
- Monticello: Otterbein–Wolcottville ~121 mi, Monticello 5:17 PM local, courthouse destroyed, safe third to
  first floor, railroad bridge lifted, church van with six girls swept ~50 ft into the Tippecanoe `[WIBC; verify
  the girls' fate before any line implies it]`; Rod Poole quote (WIBC); 18 dead full track `[8/10/17 sub-counts
  conflict]`.
- Sugar Valley–Resaca F4, 9–10 dead, 200+ hurt `[Wikipedia list]`.
- Tanner 1: ~6:20 PM CDT, ~90 min, 51–52 mi, 28 dead `[WAAY; NWS Huntsville 404]`. Tanner 2: ~7:30 PM, 1 mi west,
  ~98 mi. Limestone County 16 dead from both `[Athens News Courier, secondary]`; combined ~50 `[secondary]`.
- Guin: 8:25 PM CDT → 10:30–10:57 PM, 101–102 mi, 28 (NCDC) / 32 (Tornado Talk); 737 houses; Lindley, Todd,
  McGuire verbatim from Tornado Talk `[secondary; on-screen attribution "Tornado Talk oral history"]`. Town
  ~2,500 `[verify 1970 census]`.
- Fujita: scale 1971, ten months, 10,000+ mi, 148 tracks, 30 F4/F5; F2–F5 wording: SPC legacy F-scale page
  (primary); microburst + airliners (Eastern 66 1975, Delta 191 1985) `[verify NWS microburst history]`.
- Synoptic engine (Gulf moisture, dry layer, jet, cold front) `[verify against the NWS Wilmington synoptic
  summary; keep the words plain]`. Post-1974 backup power, Doppler "contributed" `[NWS Wilmington]`.
- 2011: Hackleburg–Phil Campbell EF5, 132 mi, 72 dead statewide, deadliest single tornado in Alabama history,
  path over rebuilt 1974 Tanner homes, mobile home park and church: Wikipedia `[verify against NWS Huntsville
  2011 survey]`. Limestone 4 dead 2011 vs 16 in 1974; Troutman (NWS) + Gaston (UNA) "paths match almost
  exactly"; "better warnings": Athens News Courier `[secondary; quote the paper on the citation card]`.
  Limestone 41,699 (1970) → 103,570 (2020) = 2.5×; Madison 186,540 → 388,153: census via Wikipedia `[verify]`.
- Today: Huntsville 249,102, Madison County 433,516 (2025): huntsvilleal.gov. Lead time "about fifteen minutes
  today" `[find an NWS/NOAA statistic; cut the number if none]`. WEA phone alerts `[verify since 2012]`. "Every
  few decades" `[editorial; keep vague]`.
- TTS respellings: "read" in Z → "reed"; "wind" noun only; "lead", "live", "tear", "close" not used as verbs.

## Pre-TTS gates (script-os.md)
1. Independent grade ≥ 8 on the hook, no chapter axis under 3 (`research/script_review_v3.md`).
2. Cut filter A/B/C/D per sentence; cut D.
3. Visual audit: every `[RS]` has a `[VE]`.
4. AVD pass at 0:30, 1:30 … 21:30.
5. Fact-QC: zero open `[verify]`; homograph scan.
6. Probe-TTS H + A4-S2 at atempo 1.10 → recompute words → trim to 22:00 ± 1.

## Build plan (after owner approval of this script)
1. Fact-QC agent clears the register from primary sources, edits numbers in place, lists cuts.
2. TTS per segment → atempo 1.10 → re-transcribe → words.json.
3. Sourcing (PD spine first), provenance rows with `shot`, one labelled grid read before wiring.
4. Compositions: the comps above, library first (#4 clock, ep3 map-route-fit, ep2 stat panel).
5. Static suite → freeze scan → comp lint → frame read → ONE draft → owner preview → ONE full render.
6. master_deliverables → metadata (first URL = paulraymond.online, book line at the CTA time, link to the 2011
   Super Outbreak) → PR.
