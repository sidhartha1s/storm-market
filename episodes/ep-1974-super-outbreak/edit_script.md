# ep-1974-super-outbreak · "The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak"

Lane: documentary (`/storm-episode`). Target 22:00 ± 1:00. Title locked by the owner 20 Sep 26. Script v2 (after
the independent grade in `research/script_review_v1.md`: hook 7/10, overall 6/10, FIX THEN RE-GRADE).
Doctrine: `references/script-os.md`, `references/script-scaling.md`, DESIGN.md (hook contract, CTA contract,
on-screen text rules). Facts: `research/fact_sheet.md`; every number is `[verify]` until the fact-QC pass clears
it; zero open markers before TTS. Delivery: pocket-TTS then atempo 1.10 (probe the hook first).

## Engine settings
- **Dominant question:** the viewer keeps watching to find out *how one day made seven F5 tornadoes, and why the man
  who saw it coming a day early still lost three hundred and thirty people.*
- **Architecture:** Countdown 60 % (the phone call on 2 April → 2:16 PM → 10:57 PM, state by state) + Detective
  40 % (Fujita's ten months in the air, the F6 he wrote and crossed out, the straight-line damage nobody could
  explain).
- **Escalation:** one F5 over empty ground → a college on a hill → a town of 1,700 loses 31 → a city loses 34 in
  four minutes → five hooks on one radar → a city of 300,000 with a tornado the radar cannot see → the same
  town hit twice in an hour → two hours in the dark → the scale's inventor doubts his scale → a wind nobody
  could explain → the corridor is now a city of 433,000.
- **Carried question per act (v2 fix):** every act plants a question in its first 30 s that it pays in its last
  30 s, on top of the act bridges. Listed in the loop table.
- **Retention spikes (each with a `[VE]`):** 148 tornadoes · a bus on the stage the students just left · a 15 year
  old carries 169 people · five hooks on one scope · "It went through the rescuers" · "I have the thing on tape"
  · two hours, one hundred miles · Fujita writes F6 and crosses it out · trees down like combed hair ·
  433,000 people across the Tanner path.
- **Named person per act:** Pearson (I) · Tim Haley, Gus Allen (A1) · David Heath (A2) · Dick Gilbert (A3) ·
  Allen Lindley, Becky Todd (A4) · Fujita (A5) · Gus Allen returns (A6).
- **Register:** plain American, a third grader follows it aloud. Clock times are digits with AM/PM on screen and
  spoken as digits ("four forty five PM"); the first time each state appears the voice says its local time
  ("Central time") once. No cross-zone interval arithmetic. F5 is correct for 1974 (Fujita scale; EF from 2007).

## Packaging
- **Title (locked):** The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak
- **Thumb brief:** colour plate of the Xenia funnel (NOAA Photo Library via Commons, PD-US-no-notice, confirm per
  file) or a graded Wright-Patterson aerial of the Windsor Park path; two lines of type, top of frame: "1974"
  (Abril, red) over "SUPER OUTBREAK" (white). Nothing else. Same grammar as the 2011 Super Outbreak thumb (6.5 %).
- Alternate for Studio Test and Compare: same plate, "7 F5s" replacing "1974".

## Runtime and word budget
22:00 target. Narration budget ≈ 22 × 0.9 × 152 ≈ 3,010 words at the old pace; at atempo 1.10 the same words
run ≈ 9 % shorter, so the v2 script (measured by `research/wordcount` below, tag-stripped) is sized to land at
20:30 to 21:30 total with hook inserts, CTA, void and blackouts. Probe-TTS H and A4-S2 at 1.10, recompute.
CTA (15.139 s, v5) at the A2 → A3 seam ≈ 7:20 ≈ 35 %.

## Chapter cards (five fields)
| # | Chapter · words | Purpose | Question | Reveal | Visual event | Exit hook |
|---|---|---|---|---|---|---|
| H | Hook · 55 | Payoff first, then the contradiction | If he knew, why did so many die? | Seven F5s, 330 dead, a day's warning, five on one screen | g-scale slam, g-radar five hooks, popfig "4:45 PM" | question |
| I | The call · 190 | The man who saw it; why knowing was not enough; the US promise | What did he do with a day's warning, and why was it not enough? | Every office phoned; a warning in 1974 is a radio that has to be on | g-master-map offices lighting; popfigs "148", "2,600 MILES" | contradiction: "the first one hit where there was nobody to warn, and that was the last time that would be true" |
| A1 | First blood · 380 | The clock starts; who is in the way | Q-A1: why did a warned town still lose 31? | DePauw over empty ground; Hanover College's basements; Brandenburg with 15 minutes and no basements | map tracks 1–3, g-clock, g-person Haley, Allen | location shift: "a drama teacher was walking his students onto a stage" |
| A2 | Xenia · 330 | The deadliest single tornado | Q-A2: thirty minutes should have been enough; why was Xenia the worst? | Warning at 4:10 PM, school out, roads full; the hallway and the bus; 34 dead | g-clock, bus photo hold, aerial scar, g-scale bar 3 | reveal tease → CTA |
| CTA | 15.139 s | must-keep | | | 1.0 s dips | |
| A3 | Five on one screen · 380 | Payoff (F6); the peak of the afternoon; the radar that could not see wind | Q-A3: the radar sees rain, not wind; how do you warn a city of 300,000? | Five hooks at once; a helicopter and one radio voice; 15 on the ground | g-radar, map surge, g-person Gilbert, WHAS insert | escalation: "the sun was still up" |
| A4 | Alabama after dark · 440 | Night; the same town twice; the tape | Q-A4: two F5s hit one town an hour apart; which one killed whom? | Rescuers under the second; Guin for two hours; Lindley's tape; Becky Todd's sons | g-clock, map southern arm, waveform card, g-scale complete | consequence: "one man was already planning to count everything else" |
| A5 | Ten months in the air · 360 | Detective act | Q-A5: how do you grade a tornado when the wind is gone, and what did the map show that nobody expected? | 148 tracks by hand; F6 for Xenia, taken back; combed-hair damage = the microburst | g-survey, g-mechanism, g-scale seven bars | present-day return: "that corridor is not farmland any more" |
| A6 | The same corridor today · 400 | Answer the dominant question in the last 45 s | Could it happen again, and would the warning reach you? | 433,000 across the Tanner path; the warning travels now; the houses moved | g-master-map today, g-then-now, Gus Allen returns | thesis in the final 45 s |
| Z | Close · 50 | END CTA spine | | | g-outro | |

## Loop table (plant → pay, with times)
| Loop | Planted | Paid |
|---|---|---|
| EPISODE: if he knew, why did so many die | H 0:20 | A6-S3 ≈ 20:10 |
| L4: the corridor is the fastest growing city in the state today | I 1:50 | A6-S1 17:30 |
| Q-A1: why did a warned town still lose 31 | A1-S1 2:15 | A1-S2 4:00 |
| L2: a drama teacher and a stage | A1-S3 4:40 | A2-S2 5:35 |
| Q-A2: thirty minutes, and still the worst; why | A2-S1 4:50 | A2-S3 6:40 |
| cta-hinge: "he decided his own scale was too small" | A2-S4 7:05 | A3-S1 7:40 |
| Q-A3: the radar cannot see wind; how do you warn a city | A3-S2 8:00 | A3-S3 9:40 |
| L3: the sun was still up | A3-S4 10:20 | A4-S1 10:25 |
| Q-A4: which tornado killed whom | A4-S1 10:40 | A4-S1 close 12:00 (unanswerable, said so) |
| Q-A4b: the tape | A4-S2 12:10 | A4-S2 13:20 |
| L5: count everything else | A4-S3 14:00 | A5-S1 14:05 |
| Q-A5: what did the map show that nobody expected | A5-S1 14:20 | A5-S3 17:00 |
| L6: not farmland any more | A5-S3 17:20 | A6-S1 17:25 |
| Q-A6: would the warning reach you | A6-S1 17:40 | A6-S2 19:10 |

## Motion graphics (hand-authored comps, library first; each ≥3 type tiers, continuous motion)
g-master-map (one comp, six fill states: outline · tracks 1–3 · surge · southern arm · Fujita's hand map ·
today's footprints; ep3 map-route-fit pattern on a 13-state plate; distances on the map are measured, the voice
says "about a hundred and seventy miles", "about four hundred miles") · g-clock (the #4 clock anatomy, reads
"2:16 PM CDT") · g-radar (WSR-57 scope, hooks as sweep returns, label "CINCINNATI WSR-57 · APRIL 3, 1974";
no clock on the label until the fact pass gives a timestamp) · g-scale (seven F5 bars) · g-person (name, place,
one line) · g-survey (tracks drawn by hand, date ticker April 1974 → February 1975) · g-mechanism (two cards: the
one-air-mass engine; how a rating is read from a house) · g-then-now (1974 vs today) · g-outro. **Red popfigs**
(Abril, ≤3 words, mid-screen) for every date, time and count while the voice says the human version.
Citation cards replace screenshots. Footage: NOAA Photo Library and Wright-Patterson aerials (PD), Commons
Xenia set (licence per file), NWS Wilmington and Louisville galleries (licence per set), WHAS archive (licence),
NWS 50th-anniversary video (PD), FEMA (PD), stock as fill only.

## Inserts (audio-carrying; owner YES before any render)
1. `ins-hook-whas` (hook, ~4 s): Dick Gilbert's live WHAS-AM helicopter report, the line where he puts the
   tornado on a street. LPM/WHAS 1974 archive [licence]. Transcribe first; cut at the sentence end.
2. `ins-guin-tape` (A4, ~6 s): Allen Lindley's Guin recording. Tornado Talk hosts it [rights to clear]. If rights
   fail, a waveform card over the narration; no fabricated audio.
3. `ins-nws-50th` (A5 or A6, ~5 s): an NWS 50th-anniversary interview line [PD if NWS-produced, confirm].
All other broadcast pulls muted, narrated over, ≤ 8 s, `.bc` grade class, never the same cut twice.

---
## SCRIPT (readable form; TTS pass spells numbers, respells homographs, splits sentences over 24 words;
`[VE]` visual event · `[RS]` spike · `[HUMAN]` named person · `[Q]` open question · `[PAY]` payoff)

### H · hook (0:00–0:25, 55 w) · frame one mid-action: the scope, hooks blooming; popfig "APRIL 3, 1974 · CINCINNATI" inside the first second
*(ins-hook-whas under the first two seconds, ducked as the narrator enters)*
Seven F5 tornadoes in one day. [VE g-scale seven bars slam in] Three hundred and thirty people dead. [RS] And
the man in charge of the forecast knew it was coming a full day early. [VE g-radar: five hooks on one scope,
popfig "4:45 PM"] Five tornadoes on one radar screen at the same time, and the worst ones had not even formed
yet. So if he knew, why did so many people die? [Q] *(1.5 s void)*

### I · the call (0:25–1:55, 190 w) · g-master-map v1, thirteen states outlined and empty; popfig "APRIL 2, 1974 · KANSAS CITY"
The day before, a man named Allen Pearson picked up a telephone. [HUMAN g-person Pearson] He ran the Severe
Storms Forecast Center, and the charts for the third of April scared him. So he called every weather office in
the eastern half of the country. Fix your radar tonight. Bring in extra people tomorrow. [VE map: the offices
light up one by one] He was right about the day. He was right about the place. The watches went out. The
warnings went out. And people still died, because in 1974 a warning was a voice on the radio, and a radio has
to be switched on. [RS]

A hundred and forty eight tornadoes in sixteen hours. [VE popfig "148"] Thirteen states and a piece of
Canada. Two thousand six hundred miles of ground ripped up, [VE popfig "2,600 MILES"] and seven tornadoes at
the top of a scale that was only three years old. The man who invented that scale was about to fly over every
one of those miles and doubt his own numbers. And the corridor that took the worst of it, in north Alabama, is
the fastest growing city in the state today. [Q L4] The first tornado touched down at 2:16 PM, over empty
ground, where there was nobody to warn. That was the last time that would be true all day. [Q] *(blackout 0.7 s)*

### A1 · first blood (1:55–4:40, 380 w)
**A1-S1 (100 w) · g-clock "2:16 PM CDT" · g-master-map track 1.** The first F5 of the day came down south of
Huffman, Indiana, at 2:16 PM, Central time. [VE track drawn] For sixty two miles it stayed over farmland. Six
counties, and never a town. Six people died, in farmhouses that happened to be in the way. Ninety minutes later
a town with a warning, with fifteen minutes to get ready, would lose thirty one people. [Q Q-A1] Why does a
warned town still lose thirty one? The answer is on a hill above the Ohio River.

**A1-S1b (90 w) · g-clock "3:19 PM EST" · Hanover College stills, Ken Burns · track 2a.** At 3:19 PM an F4 hit
Hanover College, near Madison, Indiana. [VE track] Thirty three buildings on the campus. Thirty two of them
damaged or destroyed. [RS] [VE campus plan, buildings going dark one by one] Not one student died. [verify:
where the students sheltered] Eleven people died along that track, seven of them down in the town of Madison.
Same wind. Same minutes. The college had somewhere to go. The town did not.

**A1-S2 (120 w) · g-clock "3:30 PM CDT" · track 2 · g-person Tim Haley.** At 3:30 PM, in Brandenburg, Kentucky,
they had fifteen minutes. [VE clock] That was good for 1974. The tornado came up the Ohio River toward the town
so low and so wide that people said it looked like a wall. [VE bc pull, muted] Half a mile across. A hundred
and twenty eight homes and thirty businesses gone, in a town of seventeen hundred, and thirty one people dead
along its path. [RS] [PAY Q-A1] Fifteen minutes is enough to get below ground. Most of Brandenburg had no
below ground to get to. [HUMAN] A boy named Tim Haley was fifteen. He spent that night carrying people out of
the wreckage, a hundred and sixty nine of them by his own count, [RS] including a baby he had to take out of a
mother's arms so he could get her to safety. He became a soldier. He said that was the hardest thing he ever
did.

**A1-S3 (70 w) · g-person Gus Allen · g-scale bar 2 lit.** [HUMAN] Gus Allen lost his sister, his brother and a
two year old cousin in the same minutes. His mother was carried about a mile by the wind, and lived. Fifty years
later he described that day in one sentence. It was just a bad day. [VE g-scale two bars lit, five dark] It was
not yet four o'clock. And about a hundred and seventy miles to the north-east, in Xenia, Ohio, a drama teacher
was walking his students onto a stage. [Q L2] *(blackout 0.8 s)*

### A2 · Xenia, 4:40 PM (4:40–7:20, 330 w)
**A2-S1 (100 w) · g-clock "4:10 PM EDT" → "4:33" → "4:40" · track 3.** Dayton's weather office put a tornado
warning on Xenia at 4:10 PM, Eastern time. [VE clock] Thirty minutes. In 1974 that was a gift. And Xenia still
became the worst-hit town of the whole day. [Q Q-A2] Why? Because school had just let out. Because the roads
were full of people driving home. At 4:33 a funnel came down near Lower Bellbrook Road, [VE track] and at 4:40
it was in the middle of the city, half a mile to a mile wide, going through Windsor Park and Arrowhead, streets
full of the houses people had bought after the war.

**A2-S2 (90 w) · g-person David Heath · Xenia High School footage, muted.** [HUMAN] At Xenia High School a
teacher named David Heath was rehearsing a musical with his students. They were on the stage. Something made
them move. They went out into the main hallway, and seconds later the wind picked up a school bus and dropped
it on the stage, [RS] right where they had been standing. [VE hold on the bus photo, slow push, 5 s] Not one of
them was hurt. Everywhere else in Xenia, it went the other way.

**A2-S3 (90 w) · g-scale bar 3 lit · Wright-Patterson aerials, Ken Burns.** Thirty four people died along that
path, thirty two of them inside the city, in about four minutes. About twelve hundred were hurt. Fourteen
hundred buildings damaged or gone, seven of them schools. [VE the aerial scar across the street grid] [PAY
Q-A2] Thirty minutes was enough time. It was not enough shelter. Xenia is still the tornado people mean when
they talk about that day.

**A2-S4 (25 w) · cta-hinge tease.** Weeks later the man who invented the tornado scale flew over these streets,
and decided his own scale was too small. [Q cta-hinge] *(1.0 s dip)*

### CTA (≈7:20, 15.139 s, v5) *(1.0 s dip)*

### A3 · five on one screen (7:40–10:20, 380 w)
**A3-S1 (60 w) · [PAY] · g-survey close-up: a hand-written "F6", struck through.** He wrote a six. [PAY] Ted
Fujita's scale ran from zero to five. In his first notes on Xenia he wrote F6, [RS] [VE the F6 written, then
crossed out] then decided a six was a rating nobody could believe, and took it back. Xenia stayed an F5. And
the afternoon was not over.

**A3-S2 (120 w) · g-radar Cincinnati WSR-57 · track 4 Sayler Park.** The radar at the Cincinnati weather office
was built in 1960. It could see rain. It could not see wind. [VE the scope, one sweep at a time] So a tornado
showed up only as a hook on the edge of a storm, if it showed up at all. [Q Q-A3] How do you warn a city when
your radar cannot see the thing you are warning about? On the afternoon of April third the man on duty was
looking at five hooks at once. [RS] [VE five bloom] One of them was headed for Sayler Park, on the west side of
Cincinnati. He warned it. Three people died there. Across the map, [VE map surge: tracks 4 to 40] fifteen
tornadoes were on the ground at the same time. [RS]

**A3-S3 (120 w) · g-person Dick Gilbert · ins-hook-whas full line (owner YES) · Louisville track.** In
Louisville, Kentucky, an F4 crossed the river into a city of three hundred thousand people at 4:40 PM, and the
radar could not see it. [VE track] [HUMAN] What could see it was a helicopter. Dick Gilbert reported traffic for
WHAS radio. He stayed in the air, followed the tornado, and told the whole city, street by street, where it was
and where it was going. [VE the track advancing with his words; insert audio] One man, one helicopter, one
radio station. [PAY Q-A3] That was the warning. Two people died in Louisville. President Nixon wrote to him
afterward. [RS]

**A3-S4 (80 w) · g-master-map: the 121-mile Indiana track and Georgia · g-clock "4:47 PM" → "6:47".** In that same
hour the map grew in two directions. [VE] Across northern Indiana one tornado stayed on the ground for a hundred
and twenty one miles, [RS] two hours, eighteen dead. And about four hundred miles south, in Georgia, an F4 went
through Sugar Valley and Resaca, ten dead, two hundred hurt. [VE Georgia lights up] Five states in one hour,
all from the same storm system. And the sun was still up. [Q L3] *(blackout 0.8 s)*

### A4 · Alabama after dark (10:20–14:00, 440 w)
**A4-S1 (150 w) · g-clock "6:20 PM CDT" → "7:30" · southern arm · track 5, then 6.** At 6:20 PM, Central time,
a tornado formed near Moulton, Alabama, and stayed on the ground for ninety minutes. [VE track] Fifty two miles.
Twenty eight dead. The town of Tanner took it head on, and by 7:30 PM neighbours were in the wreckage with
flashlights, pulling people out. Then the second one came. [RS] [VE second track, one mile west, drawn over
the first] Same town. One mile to the west. One hour later. Ninety eight miles long. It went through the
rescuers. [RS] [Q Q-A4] Two F5 tornadoes hit one small town an hour apart, in the dark, and nobody has ever
been able to say for certain which one killed whom. Fifty years later the count is still argued. About fifty
people died in that one stretch of north Alabama. [verify combined toll]

**A4-S2 (170 w) · g-clock "8:25 PM" → "10:57 PM" · track 7 Guin · g-person Lindley · ins-guin-tape (owner YES).**
At 8:25 PM a tornado touched down in Mississippi and did not lift for over two hours. [VE clock ticking through
the segment] A hundred and one miles, one of the longest-lived violent tornadoes ever recorded. It was heading
for Guin, Alabama, a town of about two thousand five hundred, and it got there at about 9 PM, in the dark.
[HUMAN] A young man named Allen Lindley put a tape recorder in an open window. [Q Q-A4b] He got a minute of it
coming and eighteen seconds of it going over the house. [VE waveform card; insert audio if cleared] I have the
thing on tape, he said. It is one of the only recordings of an F5 passing directly over a house in 1974. [RS]
[PAY Q-A4b] [HUMAN] Becky Todd's family were in their car when it rolled. She told them to hold on to the
seats. Her sons Mark and Paul did not survive. [RS] Seven hundred and thirty seven houses were destroyed in
Guin that night, and twenty eight people died. [verify: 28 official / 32 revised]

**A4-S3 (120 w) · g-scale all seven bars lit · aerial of Guin · g-person Mildred McGuire.** [HUMAN] The town's
pharmacist, Mildred McGuire, survived with a broken pelvis and later wrote a poem about what Guin did next,
which was rebuild on the same ground. That was the seventh F5. [VE bar 7 lit, the set complete] Seven, in nine
hours, from Indiana to Alabama. By midnight there was nothing left to count but the dead. Three hundred and
thirty of them, by the government's number. Five thousand four hundred and eighty four hurt. [RS] And one man
in Chicago was already planning to count everything else. [Q L5] *(blackout 0.9 s)*

### A5 · ten months in the air (14:00–17:20, 360 w)
**A5-S1 (110 w) · g-survey: a small plane over the map, tracks appearing, date ticker April 1974 → February 1975.**
Ted Fujita had invented his scale in 1971. [HUMAN] It graded a tornado from zero to five by the damage it left,
because nobody could measure the wind inside one. Now he had a hundred and forty eight tornadoes to grade at
once. So he flew. [VE plane, tracks] Ten months. More than ten thousand miles, low and slow, every track drawn
by hand onto one map. [RS] [Q Q-A5] And somewhere in those ten thousand miles he found a kind of damage that
no tornado could have made.

**A5-S1b (100 w) · g-mechanism: how a rating is read from a house, four frames.** Here is how you grade a tornado
from the air after the wind is gone. [VE card: a house in four states] Roof gone, that is an F2. Walls down,
F3. The house swept clean off its slab, the slab still there, the house in the next field, that is F4 or F5,
depending on how well it was built and how far it went. [RS] Fujita read ten thousand miles of slabs that way.
Seven times he found whole neighbourhoods swept to the foundations, and seven times he wrote the top of his
scale. [verify: DePauw F5 damage indicators]

**A5-S2 (70 w) · g-then-now v1, two rows.** The country used his map. Weather offices got backup power. [VE row
lights] The case for a radar that could see wind, not just rain, finally had its evidence, and the Doppler
network that watches the same sky today grew out of days like this one. [VE row lights, labelled "contributed"]
But the map's biggest finding was not on any list of fixes.

**A5-S3 (80 w) · g-mechanism: combed trees vs rotated trees.** [PAY Q-A5] In the survey photos Fujita kept finding
trees knocked down in straight lines, all the same direction, like hair that had been combed. [RS] [VE the
card: rotation pattern vs straight-line pattern] A tornado cannot do that. A tornado turns things. Nothing in
the science of 1974 explained it. He gave it a name a few years later, the microburst, and it went on to
explain why airliners were falling out of the sky near thunderstorms. [verify] That discovery started on this
map. And the corridor it drew across north Alabama is not farmland any more. [Q L6] *(blackout 0.8 s)*

### A6 · the same corridor today (17:20–20:40, 400 w)
**A6-S1 (120 w) · g-master-map: today's city footprints over the 1974 tracks · popfig "MADISON COUNTY · 433,000".**
Put today's map under the 1974 tracks. [VE] The two Tanner tornadoes ran across what is now Madison County,
Alabama. Four hundred and thirty three thousand people live there. [PAY L4] Huntsville, at the end of that
corridor, is the biggest city in the state and the fastest growing, about a quarter of a million people where
the 1974 map shows fields. [RS] North of Louisville and south of Lexington, suburbs sit on the Kentucky tracks,
and the same ground was hit again in March 2012. [Q Q-A6] So the real question is not whether. It is whether the
warning would reach you this time.

**A6-S2 (150 w) · g-then-now v2: 1974 vs today, radar, warning, phone.** Could April third happen again? Yes. The
ingredients were ordinary spring weather for that part of the country, arriving on the same day, and every few
decades they do. [verify] What changed is the warning. [VE two columns] In 1974 the radar saw rain. Today it
sees the wind turning inside the storm before the funnel exists. In 1974 the warning was a radio you had to
have switched on. Today it is the phone in your pocket, and it will wake you up. [verify WEA] In 1974 fifteen
minutes was the best any town got. Today it is about the average. [verify lead time] [PAY Q-A6] [RS] Allen
Pearson's forecast was right a day early, and three hundred and thirty people died because a correct warning
could not travel. Today the warning travels. The houses moved into the path instead.

**A6-S3 (130 w) · g-person Gus Allen returns · Brandenburg today, muted · g-then-now v3: the fifteen minute card.**
[HUMAN] Gus Allen still lives near Brandenburg. His sister, his brother and his small cousin are on the memorial
there. It was just a bad day, he said, and that is the part that should worry you, because the day was not
rare. [PAY EPISODE] So if he knew, why did so many people die? Because in 1974 knowing a day early bought you
nothing without a radio and a basement. Today the warning buys you fifteen minutes. [VE card, three rows] A
storm shelter is thirty seconds away. An inside room on the lowest floor is a minute. A car trying to outrun a
mile-wide tornado is the one thing every survivor on this map would tell you not to do. [RS] Fifteen minutes
is enough to get below ground and not enough to get out of town. Know which one your house is before the day
comes.

### Z · close (20:40–21:10, 50 w) · g-outro
Where are you watching this from, and do you have a place below ground? Tell me in the comments, I read all of
them. The 2011 Super Outbreak and Joplin are linked below, and the Storm-Ready Home is the first link in the
description. See you in the next one.

---
## Fact register (every number above; `[verify]` = confirm from a primary source before TTS, unverified = cut)
- 148 tornadoes, 13 states + Ontario, 2,598 combined miles, 30 F4/F5, 5,484 injured: NCEI. Dead: NCEI 335 /
  NOAA 330; the script says "three hundred and thirty, by the government's number" `[verify which figure the
  NCEI page carries today; use it everywhere]`.
- 15 on the ground at once `[Wikipedia only; verify or cut]`. Five simultaneous hooks at Cincinnati: NWS
  Wilmington `[no timestamp; the hook popfig "4:45 PM" is the Sayler Park warning time, verify or drop the time]`.
- Pearson's 2 April calls `[Wikipedia; verify NWS/NOAA history]`; "charts scared him" is editorial, keep plain.
- DePauw: 2:16 PM CDT, 62 mi, 6 dead, six counties `[NWS Indianapolis 404; verify]`.
- Hanover College 3:19 PM EST, 32 of 33 buildings, 11 dead, 7 in Madison: NWS Louisville. "Not one student died"
  and where they sheltered `[verify]`.
- Brandenburg 3:30 PM CDT, ~½ mi wide, 128 homes + 30 businesses, 31 dead on the path (28 in the area), 15 min
  warning: NWS Louisville. Town ~1,700 `[verify 1970 census]`. "Most had no below ground" `[verify or soften to
  "few had a basement"]`. Tim Haley 15, 169 `[army.mil, secondary]`. Gus Allen `[WAVE3, secondary]`.
- Brandenburg → Xenia ≈ 168 mi (grader measured); script says "about a hundred and seventy". Otterbein →
  Sugar Valley ≈ 424 mi; script says "about four hundred".
- Xenia: warning 4:10 PM EDT, touchdown ~4:33, city 4:40, ½–1 mi, 32 city / 34 path, 1,150–1,300 hurt ("about
  twelve hundred"), ~1,400 buildings incl. 7 schools: NWS Wilmington. David Heath / bus on stage `[Cedarville,
  secondary; find a Xenia Gazette or WHIO primary]`. "Worst-hit town of the day" `[verify vs Brandenburg, Guin]`.
- Fujita F6 for Xenia, rating "inconceivable" `[Chicago Mag; find the 1981 Fujita/Abbey wording]`.
- Cincinnati WSR-57 installed 1960, Sayler Park warning 4:45 PM, 3 dead: NWS Wilmington.
- Louisville F4 4:37–4:59 PM, 2 dead; Gilbert; Nixon commendation `[LPM/Wikipedia; verify the document]`.
  Louisville population ~300,000 `[verify 1970 census, ~361,000]`.
- Otterbein–Wolcottville 121 mi, 18 dead, ~2 h; Sugar Valley–Resaca F4, 9–10 dead, 200+ hurt `[Wikipedia list]`.
- Tanner 1: ~6:20 PM CDT, ~90 min, 51–52 mi, 28 dead `[WAAY; NWS Huntsville 404]`. Tanner 2: ~7:30 PM, 1 mi west,
  ~98 mi. Combined ~50 `[secondary; verify or say "dozens"]`.
- Guin: 8:25 PM CDT → 10:30–10:57 PM, 101–102 mi, 28 (NCDC) / 32 (Tornado Talk revised); 737 houses; Lindley,
  Todd, McGuire quotes verbatim from Tornado Talk `[secondary; on-screen attribution "Tornado Talk oral
  history"]`. Town ~2,500 `[verify 1970 census]`. "One of the only recordings" `[verify or "a rare recording"]`.
- Fujita: scale 1971, ten months, 10,000+ mi, 148 tracks, 30 F4/F5; microburst origin and airliner link
  (Eastern 66 1975, Delta 191 1985) `[verify against NWS microburst history]`.
- Rating-from-a-house card `[verify the F2/F3/F4/F5 damage indicators against the original Fujita scale text]`.
- Post-1974: backup power, Doppler "contributed": NWS Wilmington `[verify the backup-power line]`.
- Today: Huntsville 249,102, Madison County 433,516 (2025): huntsvilleal.gov. March 2012 outbreak on the
  Kentucky tracks `[Yale Climate Connections, secondary]`. Lead time today "about fifteen minutes" `[find an
  NWS/NOAA lead-time statistic; cut the number if none]`. WEA phone alerts `[verify since 2012]`. "Every few
  decades" `[editorial; keep vague]`.
- TTS respellings: "read" in Z → "reed"; "wind" (noun) fine; "lead" not used as a verb; "live" not used.

## Pre-TTS gates (script-os.md)
1. Independent grade ≥ 8 on the hook, no chapter axis under 3 (`research/script_review_v2.md`).
2. Cut filter A/B/C/D per sentence; cut D.
3. Visual audit: every `[RS]` has a `[VE]`.
4. AVD pass at 0:30, 1:30 … 20:30.
5. Fact-QC: zero open `[verify]`; homograph scan.
6. Probe-TTS H + A4-S2 at atempo 1.10 → recompute words → trim to 22:00 ± 1.

## Build plan (after owner approval of this script)
1. Fact-QC agent clears the register from primary sources, edits numbers in place, lists cuts.
2. TTS per segment → atempo 1.10 → re-transcribe → words.json.
3. Sourcing (PD spine first), provenance rows with `shot`, one labelled grid read before wiring.
4. Compositions: the comps above, library first (#4 clock, ep3 map-route-fit, ep2 stat panel).
5. Static suite → freeze scan → comp lint → frame read → ONE draft → owner preview → ONE full render.
6. master_deliverables → metadata (first URL = paulraymond.online, book line at the CTA time, links to the 2011
   Super Outbreak and Joplin) → PR.
