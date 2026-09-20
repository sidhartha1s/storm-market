"""One-shot: replace the SCRIPT section of edit_script.md with the v5 spoken-sentence pass."""
import re, sys, pathlib

p = pathlib.Path(__file__).resolve().parent.parent / "edit_script.md"
t = p.read_text(encoding="utf8")
head, rest = t.split("### H · hook", 1)
tail = "## Fact register" + rest.split("## Fact register", 1)[1]

script = r'''### H · hook (0:00–0:25, 55 w) · frame one mid-action: the scope, hooks blooming; popfig "APRIL 3, 1974 · CINCINNATI" inside the first second
*(ins-hook-whas under the first two seconds, ducked as the narrator enters)*
Seven F5 tornadoes in one day, and it has never happened again. [verify] [VE g-scale seven bars slam in]
Three hundred and thirty people dead. [RS] [VE g-radar: five hooks on one scope, popfig "4:45 PM"] Five
tornadoes on one radar screen at once, and the worst ones hadn't even formed yet. And the man who ran the
national forecast office knew it was coming a full day early. So if he knew, why did so many people die? [Q]
*(probes: `audio/probe/hook_plain_110.wav`, `demo_mixed_110.wav`; the shipped hook uses no device beyond the
contraction, per the palette)* *(1.5 s void)*

### I · the call (0:25–1:55, 200 w) · g-master-map v1, thirteen states outlined and empty; popfig "APRIL 2, 1974 · KANSAS CITY"
The day before, a man named Allen Pearson picked up a telephone. [HUMAN g-person Pearson] He ran the Severe
Storms Forecast Center, and the charts for the third of April scared him enough that he called every weather
office in the eastern half of the country and told them to fix their radar that night and bring in extra
people the next day. [VE map: the offices light up one by one] He was right about the day and he was right
about the place, the watches went out, the warnings went out, and people still died, because in 1974 a
warning was a voice on the radio and a radio has to be switched on. [RS] Here's the thing. Many people that
year didn't even know what a tornado watch was. [verify]

A hundred and forty eight tornadoes in less than a day, [VE popfig "148"] across thirteen states and a piece
of Canada, and two thousand six hundred miles of ground ripped up end to end. [VE popfig "2,600 MILES"] Seven
of those tornadoes sat at the top of a scale that was only three years old, and the man who invented that
scale was about to fly over every one of those miles and doubt his own numbers. And the corridor that took the
worst of it, in north Alabama, is the fastest growing city in the state today. [Q L4] The first tornado
touched down at 2:16 PM over empty ground, where there was nobody to warn, and that was the last time that
would be true all day. [Q] *(blackout 0.7 s)*

### A1 · first blood (1:55–4:50, 400 w)
**A1-S1 (100 w) · g-clock "2:16 PM CDT" · g-master-map track 1.** The first F5 of the day came down south of
Huffman, Indiana, at 2:16 PM, Central time, [VE track drawn] and for sixty two miles it stayed over farmland,
through six counties and never a town. Six people died, in farmhouses that happened to be in the way. Ninety
minutes later a town with a warning, with fifteen minutes to get ready, would lose thirty one people. [Q Q-A1]
The warning worked there, but the warning wasn't the thing that saved anybody, and the reason why starts on a
hill above the Ohio River.

**A1-S1b (110 w) · g-clock "3:51 PM EDT" · Hanover College stills, Ken Burns · track 2a.** At 3:51 PM, Eastern
time, a tornado hit Hanover College near Madison, Indiana, with nearly a thousand students on campus and some
of them still in class. [VE track] Thirty of the thirty three buildings were damaged and two were destroyed,
[RS] [VE campus plan, buildings going dark one by one] and on that campus nobody died, not one person. The
college still calls it a miracle, and nobody has ever fully explained it. Down the hill in the town of Madison
seven people died, eleven along that one track, and it was the same wind in the same minutes.

**A1-S2 (130 w) · g-clock "3:30 PM CDT" · track 2 · g-person Tim Haley.** At 3:30 PM, Central time, in
Brandenburg, Kentucky, they had fifteen minutes, [VE clock] and that was good for 1974. The tornado came up
the Ohio River toward the town so low and so wide that people said it looked like a wall, [VE bc pull, muted]
and it was half a mile across. A hundred and twenty eight homes and thirty businesses were gone from a town
of seventeen hundred, and thirty one people were dead along its path. [RS] [PAY Q-A1] Fifteen minutes is
enough to get below ground, but few homes in Brandenburg had a below ground to get to. [verify] [HUMAN] A boy
named Tim Haley, he was fifteen. He spent that night carrying people out of the wreckage, a hundred and sixty
nine of them by his own count, [RS] [VE popfig counter ticking to 169 over a Brandenburg still] including a
baby he had to take from a mother's arms so he could get her to safety. He became a soldier later, and he said
that was still the hardest thing he ever did.

**A1-S3 (80 w) · g-person Gus Allen · g-scale bar 2 lit.** [HUMAN] Gus Allen lost his sister, his brother and a
two year old cousin in the same minutes, and his mother was carried about a mile by the wind and lived. Fifty
years later he described that day in one sentence. It was just a bad day. *(hold 3.0 s: Brandenburg memorial,
slow push, wind bed only, no voice)* [VE g-scale two bars lit, five dark] It wasn't yet four o'clock, and about
a hundred and seventy miles to the north-east, in Xenia, Ohio, a drama teacher was walking his students onto
a stage. [Q L2] *(blackout 0.8 s)*

### A2 · Xenia, 4:40 PM (4:50–7:40, 450 w)
**A2-S1 (100 w) · g-clock "4:10 PM EDT" → "4:33" → "4:40" · track 3.** Dayton's weather office put a tornado
warning on Xenia at 4:10 PM, Eastern time, [VE clock] which gave the town thirty minutes, and in 1974 thirty
minutes was a gift. And Xenia still became the worst-hit town of the whole day, right? [Q Q-A2] So why? At
4:33 a funnel came down near Lower Bellbrook Road, [VE track] and at 4:40 it was in the middle of the city,
half a mile to a mile wide, going through Windsor Park and Arrowhead, streets full of the houses people had
bought after the war.

**A2-S2 (90 w) · g-person David Heath · Xenia High School footage, muted.** [HUMAN] At Xenia High School a
teacher named David Heath was rehearsing a musical with his students, and they were up on the stage when
something made them move. They went out into the main hallway, and seconds later the wind picked up a school
bus and dropped it on the stage, [RS] [VE popfig "A SCHOOL BUS"] right where they had been standing. *(hold
4.0 s: the bus-on-stage photo, slow push, rain bed only, no voice)* Not one of them was hurt, and everywhere
else in Xenia it went the other way.

**A2-S3 (100 w) · g-scale bar 3 lit · Wright-Patterson aerials, Ken Burns · popfig "5 SCHOOLS".** Thirty four
people died along that path, thirty two of them inside the city, in about four minutes, and about twelve
hundred were hurt. Fourteen hundred buildings were damaged or gone, and five schools were destroyed: Xenia
High, Central Junior High, McKinley, Simon Kenton and Arrowood. [VE the names, one by one, over the aerial
scar] [PAY Q-A2] Thirty minutes was enough time, but it wasn't enough shelter, and Xenia is still the tornado
people mean when they talk about that day.

**A2-S4 (45 w) · Nixon Library material, muted, 6 s · popfig "APRIL 9, 1974".** Six days later President Nixon
walked the streets of Xenia, [HUMAN] [VE Nixon footage] and those pictures are the reason most people who
remember 1974 remember one word, and that word is Xenia. But Xenia was one tornado out of a hundred and forty
eight, and forty miles away in Cincinnati the afternoon was about to get worse than any radar operator alive
had seen.

**A2-S5 (25 w) · cta-hinge tease.** Weeks later the man who invented the tornado scale flew over these streets,
and decided his own scale was too small. [Q cta-hinge] *(1.0 s dip)*

### CTA (≈7:40, 15.139 s, v5) *(1.0 s dip)*

### A3 · five on one screen (8:00–11:30, 560 w)
**A3-S1 (60 w) · [PAY] · g-survey close-up: a hand-written "F6", struck through.** He wrote down a six. [PAY] Ted
Fujita's scale ran from zero to five, and in his first notes on Xenia he wrote F6, [RS] [VE the F6 written,
then crossed out] then decided a six was a rating nobody could believe and took it back. Xenia stayed an F5,
and the afternoon wasn't over.

**A3-S2 (130 w) · g-radar Cincinnati WSR-57 · citation card: the 4:05 PM warning, verbatim.** Now look at the
radar at the Cincinnati weather office. It was built in 1960, and it could see rain but it couldn't see wind,
[VE the scope, one sweep at a time] so a tornado showed up only as a hook on the edge of a storm, if it showed
up at all. [Q Q-A3] How do you warn a city when your radar can't see the thing you're warning about? At 4:05 PM
the office put out a tornado warning for Hamilton County, and the reason it gave was one line: [VE citation
card, verbatim] based on hook echoes on the radar. [RS] Twenty seven minutes later the hook it was looking at
came through Sayler Park on the west side of Cincinnati, and four people died in that county. [verify] By then
the man on duty was looking at five hooks at once, [RS] [VE five bloom] [Q Q-A3b] and then, at 5:40 PM, his
office went dark.

**A3-S2b (90 w) · citation card: the CVG report · popfig "5:40 PM · POWER OUT".** [PAY Q-A3b] The Cincinnati
weather office lost power at 5:40 PM, in the middle of the outbreak, [VE the scope goes black] and with it the
radar, the teletype and the incoming phone lines. For three hours the office that had been warning half of
Ohio had to call Cleveland on whatever phone still worked and ask Cleveland to send its warnings out. [RS]
[VE map: the Cincinnati office goes dark, Cleveland lights up] Its own report six days later said the warnings
had saved many lives, and it also recorded seven dead in its area, and both of those were true. Across the
map at that hour, fifteen tornadoes were on the ground at the same time. [verify] [VE map surge: tracks 4 to 40]

**A3-S3 (140 w) · g-person Dick Gilbert · ins-hook-whas full line (owner YES) · Louisville track · popfig "361,000".**
In Louisville, Kentucky, an F4 came across the river into a city of three hundred and sixty thousand people at
5:37 PM, Eastern time, [verify] and the radar couldn't see it. [VE track] [HUMAN] What could see it was a
helicopter. Dick Gilbert reported traffic for WHAS radio, he grew up on Pennsylvania Avenue in Crescent Hill,
and the tornado was on his street. He stayed. He stayed in the air, followed it, and told the whole city block
by block where it was and where it was going, [VE the track advancing with his words; insert audio] while it
tore the roof off Freedom Hall at the fairgrounds and wrecked the Crescent Hill water station. One man, one
helicopter and one radio station, and that was the warning. [PAY Q-A3] Two people died in Louisville, and the
President sent him a special commendation for it. [RS] [VE g-person Gilbert card, "COMMENDED BY THE PRESIDENT"]

**A3-S4 (140 w) · g-clock "5:17 PM EDT" · Monticello, Indiana · g-person Rod Poole · track: the 121-mile line.**
In that same hour, up north, one tornado came down near Otterbein, Indiana, and didn't lift for a hundred and
twenty one miles. [VE map] [RS] At 5:17 PM it went through the middle of Monticello, where the county
courthouse came apart and a safe on the third floor fell straight through to the first, [VE popfig "121
MILES"] and a railroad bridge over the Tippecanoe River was lifted off its footings and twisted. [HUMAN] Rod
Poole, who later ran the town's water department, said the sky was a greenish brown, and that everybody says a
tornado sounds like a train, and they're right. Eighteen people died along those hundred and twenty one miles.

**A3-S5 (40 w) · g-master-map: Georgia.** And about four hundred miles south, in Georgia, an F4 went through Sugar
Valley and Resaca, with ten dead and two hundred hurt. [VE Georgia lights up] That was five states in one
hour, from one storm system, and the sun was still up. [Q L3] *(blackout 0.8 s)*

### A4 · Alabama after dark (11:30–15:00, 440 w)
**A4-S1 (150 w) · g-clock "6:20 PM CDT" → "7:30" · southern arm · track 5, then 6.** At 6:20 PM, Central time,
a tornado formed near Moulton, Alabama, and stayed on the ground for ninety minutes and fifty two miles.
[VE track] Twenty eight people died, most of them in and around the town of Tanner, and by 7:30 PM the
neighbours were out in the wreckage with flashlights pulling people out. That's when the second one came.
[RS] [VE second track, one mile west, drawn over the first] It formed about an hour after the first, ran a
mile to the west of it for ninety eight miles, and honestly it went straight through the people doing the
rescuing. [RS] *(hold 3.5 s: the second track pulsing over the first on the map, wind bed, no voice; no
blackout after a hold)* [Q Q-A4] So two F5 tornadoes hit one small town an hour apart, and to this day nobody
can say for certain which one killed whom, because the people who could have told you were the ones under the
second one. Sixteen people died in Limestone County that night, [verify] and about fifty in that one stretch
of north Alabama. [verify]

**A4-S2 (170 w) · g-clock "8:25 PM" → "10:57 PM" · track 7 Guin · g-person Lindley · ins-guin-tape (owner YES).**
At 8:25 PM a tornado touched down in Mississippi and didn't lift for over two hours, [VE clock ticking through
the segment] a hundred and one miles, one of the longest-lived violent tornadoes ever recorded. It was heading
for Guin, Alabama, a town of about two thousand five hundred people, and it got there at about 9 PM. [HUMAN] A
young man named Allen Lindley put a tape recorder in an open window, [Q Q-A4b] and he got a minute of it
coming and eighteen seconds of it going over the house. [VE waveform card; insert audio if cleared] I have the
thing on tape, he said, and it's a rare recording of an F5 passing directly over a house. [RS] [PAY Q-A4b]
[HUMAN] Becky Todd's family were in their car when it rolled, and she told them to hold on to the seats. Her
sons Mark and Paul didn't survive. [RS] [VE g-person card: two names] Seven hundred and thirty seven houses
were destroyed in Guin that night, and twenty eight people died. [verify: 28 official / 32 revised]

**A4-S3 (120 w) · g-scale all seven bars lit · aerial of Guin · g-person Mildred McGuire.** [HUMAN] The town's
pharmacist, Mildred McGuire, survived with a broken pelvis and later wrote a poem about what Guin did next,
which was rebuild on the same ground. That was the seventh F5, [VE bar 7 lit, the set complete] seven in nine
hours from Indiana to Alabama, and by midnight there was nothing left to count but the dead, three hundred and
thirty of them by the government's number, and five thousand four hundred and eighty four hurt. [RS] [VE
popfigs "330 DEAD" then "5,484 HURT"] And one man in Chicago was already planning to count everything else.
[Q L5] *(blackout 0.9 s)*

### A5 · ten months in the air (15:00–18:30, 470 w)
**A5-S1 (110 w) · g-survey: a small plane over the map, tracks appearing, date ticker April 1974 → February 1975.**
Ted Fujita had invented his scale in 1971, [HUMAN] and it graded a tornado from zero to five by the damage it
left, because nobody could measure the wind inside one. Now he had a hundred and forty eight tornadoes to
grade at once, so he flew, for ten months and more than ten thousand miles, low and slow, with every track
drawn by hand onto one map. [VE plane, tracks] [RS] [Q Q-A5] And somewhere in those ten thousand miles he
found a kind of damage that no tornado could have made.

**A5-S2 (120 w) · g-mechanism: two frames, F4 and F5, in the scale's own words · g-person Robert Pennington.**
Here is what he was reading. [VE card: a house in two states] A well-built house with its walls gone is an F4,
and the same house swept clean off its foundation, with the cars a hundred yards away and the trees stripped
of their bark, is an F5. [RS] [VE the second frame: the slab, the bark] [HUMAN] In Guin, a man named Robert
Pennington came home from his shift at the electric company to that. He said there was no sign of the house,
the foundation, the framing, or anything, and his wife Juanita, who was sixty four, was found dead. [RS] [VE
g-person card] That is what an F5 looks like from the ground, and Fujita read ten thousand miles of it from the
air, and seven times he wrote the top of his scale. [verify against the DePauw damage]

**A5-S3 (120 w) · g-mechanism: the one-air-mass engine, one diagram.** And the map answered the first question,
which is how one day makes seven of them. [VE the card: warm wet air below, dry air above, the jet stream on
top, a cold front as the trigger] You take warm, wet air off the Gulf of Mexico, put a layer of dry air over
the top of it, run a jet stream above that to turn the whole column, and send a cold front through to set it
off, from Illinois to Alabama, all afternoon and all night. [verify synoptic summary] Every storm that formed
in that column had the same engine, and that's what an outbreak is, I mean, not a lot of tornadoes but one
machine making them for the better part of a day. [RS] [VE the engine card cycles once, one storm after
another off the same column] But the map's biggest finding wasn't the engine.

**A5-S4 (130 w) · g-mechanism: combed trees vs rotated trees · g-then-now v1.** [PAY Q-A5] In the survey photos
Fujita kept finding trees knocked down in straight lines, all in the same direction, like hair that had been
combed, [RS] [VE the card: rotation pattern vs straight-line pattern] and a tornado can't do that, because a
tornado turns things. Nothing in the science of 1974 explained it, so a few years later he gave it a name, the
microburst, and it went on to explain why airliners were falling out of the sky near thunderstorms. [verify]
The country used the rest of his map too, and weather offices got backup power, [VE row lights] and the case
for a radar that could see wind finally had its evidence, and the Doppler network that watches the same sky
today grew out of days like this one. [VE "contributed"] And the corridor the map drew across north Alabama is
not farmland any more. [Q L6] *(blackout 0.8 s)*

### A6 · the same corridor (18:30–22:00, 520 w)
**A6-S1 (150 w) · g-master-map: the 2011 path drawn over the 1974 Tanner tracks · popfig "APRIL 27, 2011".** Put
another map on top of the 1974 tracks. [VE] On April 27th, 2011, an EF5 tornado came out of Mississippi,
crossed Alabama for a hundred and thirty two miles and killed seventy two people, the deadliest single tornado
in the state's history, [RS] [VE popfig "132 MILES · 72 DEAD"] and in Limestone County it ran straight down the
1974 Tanner corridor. [Q Q-A6] It destroyed homes, a mobile home park and a church that the first two Tanner
tornadoes had destroyed thirty seven years earlier, and that people had rebuilt on the same ground. [VE the two
paths lining up] A weather service meteorologist and a geography professor had been comparing the tracks for
three years before it happened, and afterward they said the paths matched almost exactly. [HUMAN citation
card] So what happened the second time?

**A6-S1b (110 w) · g-then-now: 1974 vs 2011, two rows · popfig "16 → 4".** [PAY Q-A6] In 1974 the two Tanner
tornadoes killed sixteen people in Limestone County, [verify] and in 2011, with two and a half times as many
people living there, the EF5 killed four. [RS] [VE the two numbers] More houses in the path and fewer dead,
and the researchers, they said why in two words: better warnings. That's the whole story of this channel in
one county, and it's why the 1974 map still matters. [PAY L4] Madison County next door, where the second Tanner
tornado ended, has four hundred and thirty three thousand people today, and Huntsville is the biggest city in
Alabama. [Q Q-A6b] So the real question isn't whether it happens again, it's whether the warning reaches you.

**A6-S2 (130 w) · g-then-now v2: 1974 vs today, radar, warning, phone.** Could April third happen again? Yes, it
could, because the ingredients were ordinary spring weather for that part of the country arriving on the same
day, and every few decades they do. [verify] What changed is the warning. [VE two columns] In 1974 the radar
saw rain, and today it sees the wind turning inside the storm before the funnel exists. In 1974 the warning was
a radio you had to have switched on, and today it's the phone in your pocket, and it will wake you up. [verify
WEA] In 1974 a good warning was fifteen minutes and most places got less, and today fifteen minutes is about
the average. [verify] [PAY Q-A6b] [RS] [VE the two columns fill, 1974 left, today right] Allen Pearson's
forecast was right a day early, and three hundred and thirty people died because a correct warning couldn't
travel. Today the warning travels, and the houses moved into the path instead.

**A6-S3 (130 w) · g-person Gus Allen returns · Brandenburg today, muted · g-then-now v3: the fifteen minute card.**
[HUMAN] Gus Allen still lives near Brandenburg, and his sister, his brother and his small cousin are on the
memorial there. It was just a bad day, he said, and that's the part that should worry you, because the day
wasn't rare. [PAY EPISODE] So if he knew, why did so many people die? Because in 1974 knowing a day early
bought you nothing without a radio and a basement, and today the warning buys you fifteen minutes. [VE card,
three rows] A storm shelter is thirty seconds away, an inside room on the lowest floor is a minute, and a car
trying to outrun a mile-wide tornado is the one thing every survivor on this map would tell you not to do.
[RS] [VE third row: the car, struck through] Fifteen minutes is enough to get below ground and not enough to
get out of town, so know which one your house is before the day comes.

### Z · close (22:00–22:30, 50 w) · g-outro
Where are you watching this from, and do you have a place below ground? Tell me in the comments, I read all of
them. The 2011 Super Outbreak, the tornado that ran the same corridor, is linked below, and the Storm-Ready
Home is the first link in the description. See you in the next one.

---
'''

head = head.replace("Script v3\n(v1 graded", "Script v5\n(v1 graded")
head = head.replace(
    "v3 adds the\nresearched beats from `research/fact_sheet_addendum.md` to reach length without filler).",
    "v3 added the\nresearched beats; v4 applied the second grade; v5 is the spoken-sentence pass on the palette in\n"
    "`references/humanise-rules.md`; owner length decision: natural 19 to 20 min).")
p.write_text(head + script + tail, encoding="utf8")
print("v5 written", p)

# sentence census on narration only
body = script
body = re.sub(r"\*\*A\d-S\d[^*]*\*\*", "", body)
body = re.sub(r"\*\([^)]*\)\*", "", body)
body = re.sub(r"\[[^\]]*\]", "", body)
body = re.sub(r"###[^\n]*", "", body)
sents = [s.strip() for s in re.split(r"(?<=[.?!])\s+", body) if s.strip()]
lens = [len(s.split()) for s in sents]
print("sentences", len(sents), "avg", round(sum(lens) / len(lens), 1),
      "under6", sum(1 for l in lens if l < 6), "over28", sum(1 for l in lens if l > 28))
print("short:", [s for s in sents if len(s.split()) < 6])
print("long:", [s[:60] for s in sents if len(s.split()) > 28])
for w in (" uh", " um", "not before", "not since", "in the dark"):
    print(w, body.lower().count(w))
