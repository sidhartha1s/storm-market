# ep-1974-super-outbreak · "The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak"

Lane: documentary (`/storm-episode`). Target 22:00 ± 1:00. Title locked by the owner 20 Sep 26.
Doctrine: `references/script-os.md` (engine + architectures), `references/script-scaling.md` (lattice, fact-QC),
DESIGN.md (hook contract, CTA contract, on-screen text rules). Facts: `research/fact_sheet.md` (every number
below is `[verify]` until the fact-QC pass clears it; zero open markers before TTS).

## Engine settings
- **Dominant question:** the viewer keeps watching to find out *how one afternoon produced seven F5 tornadoes,
  and why the man who saw it coming a day early still lost three hundred and thirty people.*
- **Architecture:** Countdown 60 % (2 April phone call → 2:16 pm → 10:57 pm, state by state, the clock never
  stops) + Detective 40 % (Ted Fujita's ten months in the air, the F6 he nearly gave Xenia, what the survey
  found that nobody expected).
- **Escalation:** one F5 in empty woods → a town of 1,700 loses 31 → a city loses 34 in four minutes → five
  hook echoes on one radar scope, fifteen tornadoes on the ground at once → the same town hit twice in an
  hour → a tornado that lives for two hours in the dark → the scale itself nearly breaks → the corridor is
  now suburban Huntsville and the physics has not changed.
- **Retention spikes (each gets a `[VE]`):** 148 tornadoes · 15 on the ground at once · a bus on the stage the
  students had just left · a 15 year old carries 169 people · five hooks on one scope · Tanner hit twice ·
  "I have the thing on tape" · two hours, one hundred miles · Fujita writes F6 then crosses it out ·
  10,000 miles of survey by hand · 433,000 people now live across the Tanner path.
- **US stake by minute two:** "the corridor that took the worst of it is now the fastest growing city in
  Alabama" promised in the intro, paid in act 6.
- **Named person per act:** Pearson (intro) · Tim Haley and Gus Allen (A1) · David Heath (A2) · Dick Gilbert
  (A3) · Allen Lindley, Woodrow Haney, Becky Todd, Robert Pennington (A4) · Fujita (A5) · Gus Allen returns (A6).

## Packaging
- **Title (locked):** The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak
- **Thumb brief:** colour plate of the Xenia funnel (NOAA Photo Library, PD-US-no-notice on Commons, confirm
  per file) or a graded aerial of the Windsor Park path; two lines of type, top of frame: "1974" (Abril, red)
  over "SUPER OUTBREAK" (white). Nothing else. Same grammar as the 2011 Super Outbreak thumb that got 6.5 %.
- Alternate thumb for Studio Test and Compare: the same plate with "7 F5s" replacing "1974".

## Runtime and word budget
22:00 target. Narration ≈ 22 × 0.9 × 152 wpm ≈ 3,010 words. The script below counts about 2,950 narration words
(tag-stripped) ≈ 19:25 of voice ≈ 21:40 with the hook inserts, CTA, void and blackouts. Probe-TTS the hook and
A4-S2 before locking; recompute at the measured pace. CTA (15.139 s, v5) at the A2 → A3 seam ≈ 7:40 ≈ 35 %.
Blackouts 0.6 to 0.9 s at act seams; 1.5 s void after the hook.

## Chapter cards (five fields)
| # | Chapter · time · words | Purpose | Question | Reveal | Visual event | Exit hook |
|---|---|---|---|---|---|---|
| H | Hook 0:00–0:32 · 80 | Confirm the click with something more specific than the title | What is on that radar scope? | Five hook echoes at once; seven F5s before midnight; the forecaster knew a day early | g-radar: the Cincinnati scope, five hooks blooming | question |
| I | The call 0:32–2:05 · 230 | Consequence before mechanism; the man who saw it; the US promise | If he knew, why did 330 die? | Pearson phoned every office the day before; the warnings would exist and still not arrive | g-master-map v1 (13 states outlined, empty) + "APRIL 2, 1974 · KANSAS CITY" popfig | contradiction: "the first one hit where there was nobody to warn" |
| A1 | First blood 2:05–4:50 · 410 | The clock starts; the first town | Where does it start and who is in the way? | DePauw in the woods; Brandenburg with 15 minutes' warning and 31 dead; a boy carrying 169 people | g-master-map: tracks 1 to 3 drawn; g-clock 2:16 → 3:30 → 3:45 | location shift: "four hundred miles north-east, a drama teacher was starting rehearsal" |
| A2 | Xenia, 4:40 pm 4:50–7:40 · 410 | The deadliest single tornado; one named human moment | What happens to a city with 30 minutes' warning? | The hallway, the bus on the stage, 34 dead in four minutes; Fujita would look at this street and doubt his own scale | g-clock 4:10 warning → 4:33 → 4:40; g-scale first F5 bar lit; the bus-on-stage stays footage, never a graphic | reveal tease → CTA: "the scale's inventor would decide his scale was too small" |
| CTA | ≈7:40 · v5 15.139 s | must-keep | | | 1.0 s dip in, 1.0 s dip out, real footage payoff after | |
| A3 | Five hooks on one scope 7:57–10:35 · 390 | Payoff (F6) then the peak of the day, the science of the moment | How many can be on the ground at once? | Fifteen; Cincinnati's scope shows five hooks; a helicopter traffic reporter talks a city through it live | g-radar (five hooks), g-master-map surge (tracks 4 to 40), g-person Gilbert + WHAS audio insert | escalation: "the sun was still up, and the worst of the night had not started" |
| A4 | Alabama after dark 10:35–14:10 · 510 | The night; the same town twice; the tape | What does an F5 do at night to people who cannot see it? | Tanner hit twice in an hour, rescuers under the second; Guin lives two hours and one hundred miles; a man tapes it through the window | g-clock 6:20 → 7:30 → 8:25 → 10:57; g-master-map southern arm; g-person cards; the Lindley tape as an audio insert with a waveform card | consequence: "by midnight there was nothing left to count but the dead, and one man was already planning to count everything else" |
| A5 | Ten months in the air 14:10–17:40 · 480 | The detective act; what the survey found | What did 148 tracks on one map prove? | The F scale's first mass test; Fujita writes F6 for Xenia and retreats; 30 violent tornadoes; a straight-line damage pattern that became the microburst | g-survey: the 148 tracks drawn onto the master map as Fujita's hand map; g-scale all seven bars; g-then-now v1 | present-day return: "that corridor is not farmland any more" |
| A6 | The same corridor today 17:40–20:50 · 450 | Answer the dominant question; the US stake paid | Could it happen again, and would the warning reach you? | Yes; 433,000 people live across the Tanner path now; lead time went from minutes to a quarter hour; the forecast was right and 330 died because the warning could not travel; today it travels and the houses moved into the path | g-then-now v2 (1974 vs today: lead time, radar, population), g-master-map with today's city footprints, Gus Allen returns | thesis + close |
| Z | Close 20:50–21:35 · 70 | END CTA spine | | | g-outro | |

## Loop table
| Loop | Planted | Paid |
|---|---|---|
| EPISODE: how did one day make seven F5s, and why did knowing not save them | H | A6 |
| L1: the first one hit where there was nobody to warn | I close | A1 |
| L2: a drama teacher starting rehearsal | A1 close | A2 |
| cta-hinge: "the scale's inventor would decide his scale was too small" (A2-S4) → CTA → "He wrote a six." (A3-S1) | A2 | A3 |
| L3: the worst of the night had not started | A3 close | A4 |
| L4: the corridor is now the fastest growing city in Alabama | I | A6 |
| L5: one man was already planning to count everything else | A4 close | A5 |
| L6: that corridor is not farmland any more | A5 close | A6 |

## Motion graphics (hand-authored comps, library first; each ≥3 type tiers, continuous motion)
g-master-map (one comp, five states of fill: outline · tracks 1 to 3 · surge · southern arm · Fujita's hand
map · today's footprints; the ep3 map-route-fit pattern on a 13-state plate) · g-clock (the #4 clock anatomy;
reads 2:16 PM CDT etc., the voice says the human version) · g-radar (WSR-57 scope look, hooks drawn as sweep
returns; labelled "CINCINNATI WSR-57 · 4:45 PM") · g-scale (seven F5 bars: path length and dead, lit one by
one across the episode) · g-person (name, place, one line; glasscard) · g-survey (Fujita's tracks drawn by
hand over the map, ten months as a date ticker) · g-then-now (two-column scorecard: 1974 vs today) · g-outro.
Citation cards (source · date · one line) replace screenshots. Footage: NOAA Photo Library aerials (PD),
Wright-Patterson set (PD via NOAA), Commons Xenia funnel (PD-US-no-notice, confirm), NWS Wilmington and
Louisville anniversary galleries (licence per set; Kilinc set is permission-only), WHAS / WHAS11 archive
(licence), NWS 50th-anniversary videos (PD), FEMA library (PD), Pexels stock only as fill.

## Inserts (audio-carrying; owner YES before any render)
1. `ins-hook-whas` (hook, ~4 s): Dick Gilbert's live WHAS-AM helicopter report over Louisville, the line
   where he places the tornado on a street the audience can hear. Source: LPM/WHAS 1974 archive [licence].
   Transcribe in full first; cut at the sentence end.
2. `ins-guin-tape` (A4, ~6 s): Allen Lindley's Guin recording, the vortex passing overhead. Source: Tornado
   Talk hosts it [rights to clear]. If rights fail, the beat becomes a waveform card over the narration, no
   fabricated audio.
3. `ins-nws-50th` (A5 or A6, ~5 s): an NWS Wilmington or Louisville 50th-anniversary interview line from a
   survivor or forecaster [PD if NWS-produced, confirm].
All other broadcast pulls muted, narrated over, ≤ 8 s, `.bc` grade class, never the same cut twice.

---
## SCRIPT (readable form; TTS pass spells numbers and splits sentences over 24 words; `[VE]` visual event ·
`[RS]` spike · `[HUMAN]` named person · `[Q]` open question · `[PAY]` payoff)

### H · hook (0:00–0:32, 80 w) · frame one mid-action: the scope, hooks already blooming; popfig "APRIL 3, 1974 · CINCINNATI · 4:45 PM" inside the first second
*(ins-hook-whas under the first two seconds, ducked as the narrator enters)*
Seven F5 tornadoes in one afternoon. [VE g-scale seven bars slam in] Three hundred and thirty dead. [RS] And the
man in charge of the forecast knew a full day early. [VE g-radar: five hooks on one Cincinnati scope] This is the
radar at a quarter to five, five tornadoes on one screen, and the day is only half over. So why did knowing not
save them? [Q] *(1.5 s void)*

*(Hook rule, owner 20 Sep 26: the first sentence is the payoff the title promised, numbers first, no scene-setting
before it. 60 words, about 24 s with the insert.)*

### I · the call (0:32–2:05, 230 w) · g-master-map v1, thirteen states outlined and empty; popfig "APRIL 2, 1974 · KANSAS CITY"
The day before, a man named Allen Pearson picked up a telephone. [HUMAN g-person Pearson] He ran the Severe
Storms Forecast Center, and what he saw on the charts for the third of April made him do something no
director had done. He called every weather office in the eastern half of the country. Service your radar
tonight. Bring in extra staff tomorrow. Put the satellite on severe mode. [VE map: the offices light up one by
one as he calls] He was right about the day. He was right about the region. The watches went out, the
warnings went out, and it was not enough, because in 1974 a warning was a voice on a radio, and a radio has to
be switched on. [RS]

A hundred and forty eight tornadoes in sixteen hours. [VE map counter] Thirteen states and a piece of Canada.
Two thousand six hundred miles of ground torn open, and seven tornadoes at the top of a scale that had existed
for three years, whose inventor was about to fly over every mile of it and doubt his own numbers. The corridor
that took the worst of it, in north Alabama, is the fastest growing city in the state today, under the same
sky. [Q L4] The clock started at sixteen minutes past two, in a forest, where there was nobody to warn. [Q L1]
*(blackout 0.7 s)*

### A1 · first blood (2:05–4:50, 410 w)
**A1-S1 (110 w) · g-clock 2:16 PM CDT · g-master-map track 1.** The first F5 of the day touched down south of a
place called Huffman, Indiana, and for sixty two miles it did something almost merciful. [VE track drawn] It
missed. Perry County, Crawford, Harrison, Washington, Clark, Scott. Six counties, and never a town. Six people
died, most of them in farmhouses that happened to be in the way. The weather office had a warning out. There
was simply nobody underneath it to hear it. That would not be true again for the rest of the day.

**A1-S1b (120 w) · g-clock 3:19 PM EST · Hanover College footage or stills, Ken Burns · g-master-map track 2a.**
An hour later, near Madison, Indiana, an F4 found something to hit. [VE track] Hanover College, on a bluff
above the Ohio River, had thirty three buildings. When the tornado had passed, thirty two of them were damaged
or gone. [RS] [VE the campus plan, buildings going dark one by one] Nobody on the campus died; the students
had been sent to the basements. Seven people died in the town of Madison below it, eleven along the track.
That is the shape of the whole day in one hill. The same wind, the same minutes, and the difference between
a basement and a living room is the difference between a story and a name on a wall.

**A1-S2 (170 w) · g-clock 3:30 · track 2 · g-person Tim Haley.** An hour and fourteen minutes later, in
Brandenburg, Kentucky, they had fifteen minutes. [VE clock] Fifteen minutes was good for 1974. The tornado
that came up the Ohio River toward the town was described afterward as a wall, a cloud base so low it looked
solid. [VE bc pull, muted] It was half a mile wide. It took a hundred and twenty eight homes and thirty
businesses out of a town of seventeen hundred people, and thirty one of them died. [RS] [HUMAN] A boy named
Tim Haley was fifteen. He spent the evening carrying people out of what was left, a hundred and sixty nine of
them by his own count, dead and living, [RS] including a baby he had to take out of a mother's arms so that he
could get her to safety. He was a soldier later. He said that one was the hardest thing he ever did.

**A1-S3 (130 w) · g-person Gus Allen · g-scale bar 2 lit.** [HUMAN] Gus Allen lost his sister, a two year old
cousin, and his brother in the same minutes. His mother was carried about a mile by the wind and lived. Fifty
years later, asked to describe the third of April, he said seven words. It was just a bad day. Hold that,
because Brandenburg was the second of seven, and it was not yet four o'clock. [VE g-scale two bars lit, five
dark] Four hundred miles to the north-east, in a town called Xenia, a drama teacher was walking his students
onto a stage to rehearse a musical. [Q L2] *(blackout 0.8 s)*

### A2 · Xenia, 4:40 pm (4:50–7:40, 410 w)
**A2-S1 (110 w) · g-clock 4:10 PM EDT warning → 4:33 touchdown → 4:40 · g-master-map track 3.** Dayton's
weather office put a tornado warning on Greene County at ten past four. [VE clock] Xenia had thirty minutes,
which in 1974 was a gift. The problem with thirty minutes is what a town does with them. School had let out.
People were driving home. At four thirty three a funnel came down near Lower Bellbrook Road, [VE track] and
seven minutes later it was in the middle of the city, half a mile to a mile wide, moving through Windsor Park
and Arrowhead, subdivisions full of the houses people had bought after the war.

**A2-S2 (130 w) · g-person David Heath · footage of Xenia High School, muted.** [HUMAN] At Xenia High School, a
teacher named David Heath was running an after-school rehearsal of a musical called The Boy Friend. The
students were on the stage. Something made them move. They went out to the main hallway, and seconds later
the wind picked up a school bus and put it on the stage, [RS] on the boards where they had been standing.
Not one of them was hurt. [VE hold on the bus photo, slow push, 5 s] Everywhere else in Xenia the story went
the other way.

**A2-S3 (100 w) · g-scale bar 3 lit · aerial PD set (Wright-Patterson), Ken Burns.** Thirty four people died along
that path, thirty two of them inside the city, in about four minutes. Eleven hundred were hurt. Fourteen
hundred buildings, seven of them schools, damaged or gone. [VE the aerial track, the scar across the grid] A
quarter of a billion dollars of damage from one tornado, in 1974 money. It is still the deadliest single
tornado of the day, and the reason the day has a name.

**A2-S4 (25 w) · cta-hinge tease.** Weeks later the man who invented the tornado scale flew over these streets,
and decided his own scale was too small. [Q cta-hinge] *(1.0 s dip)*

### CTA (≈7:40, 15.139 s, v5) *(1.0 s dip)*

### A3 · five hooks on one scope (7:57–10:35, 390 w)
**A3-S1 (90 w) · [PAY] · g-survey close-up: a hand-drawn "F6" struck through.** He wrote a six. [PAY] Ted Fujita's
scale ran from zero to five, and in his early notes on Xenia he rated it F6, wind he called inconceivable.
[RS] [VE the F6 written, then crossed out] He took it back. The scale stayed at five, Xenia stayed the worst of
the worst, and he went on flying. But while he was still in the air, the third of April was only half over.

**A3-S2 (130 w) · g-radar Cincinnati WSR-57, five hooks · g-clock 4:45 · track 4 Sayler Park.** At the Cincinnati
weather office the radar was a 1960 machine that saw rain and nothing else, no wind, no rotation, just the
shape of the echo. [VE the scope, one sweep at a time] A hook on the edge of a storm meant a tornado. The
forecaster on duty at a quarter to five was looking at five hooks. [RS] [VE five bloom] One of them was
coming for Sayler Park, on the west side of the city, and he warned it with minutes to spare. Three people
died there instead of thirty. Across the map, at that same moment, fifteen tornadoes were on the ground at
once. [RS] [VE g-master-map surge: tracks 4 to 40 drawn in ten seconds]

**A3-S3 (170 w) · g-person Dick Gilbert · ins-hook-whas full line (owner YES) · Louisville track.** In Louisville,
Kentucky, the warning did not come from a radar. [HUMAN] It came from a helicopter. Dick Gilbert reported
traffic for WHAS radio, and when the F4 came across the river at twenty to five he stayed in the air, followed
it, and told the city street by street where it was and which way it was going. [VE the track advancing with
his words; insert audio] Two people died in Louisville. A tornado that size through a city of that size and
two people died, and the President wrote to him afterward to say why. [RS] That was the best a warning could
do in 1974, one man, one helicopter, one radio station.

**A3-S4 (150 w) · g-master-map: the 121-mile Indiana track and the Georgia arm · g-clock 4:47 → 6:47.** The
same hour, the map grew in two directions at once. [VE] Across northern Indiana a single tornado stayed on
the ground for a hundred and twenty one miles, [RS] from Otterbein to Wolcottville, two hours of it, eighteen
dead, a track so long the survey crews later had trouble believing it was one storm. And six hundred miles
south, in Georgia, an F4 came through Sugar Valley and Resaca, ten dead, two hundred hurt, in a state that
does not think of itself as tornado country. [VE Georgia lights up on the map] Indiana, Kentucky, Ohio,
Tennessee, Georgia, all inside one hour, all from the same engine. And the sun was still up. The worst of the
night had not started. [Q L3] *(blackout 0.8 s)*

### A4 · Alabama after dark (10:35–14:10, 510 w)
**A4-S1 (150 w) · g-clock 6:20 PM CDT → 7:30 · g-master-map southern arm · track 5, then 6 one mile west.** The
first Tanner tornado formed near Moulton, Alabama, at about twenty past six, and stayed on the ground for
ninety minutes. [VE track] Fifty two miles. Twenty eight dead. The town of Tanner, in Limestone County, took
it directly, and by half past seven neighbours were in the wreckage with flashlights, pulling people out.
Then the second one came. [RS] [VE second track, one mile west, drawn over the first] Same corridor, one mile
to the west, one hour later, ninety eight miles long. It went through the rescuers. The exact split of the
dead between the two is still argued fifty years on, because nobody on the ground that night could tell which
tornado had done what. Together they killed about fifty people in one stretch of north Alabama. [RS]

**A4-S2 (200 w) · g-clock 8:25 → 10:57 · track 7 Guin · g-person Lindley · ins-guin-tape (owner YES).** At twenty
five past eight a tornado touched down in Mississippi, near Caledonia, and did not lift for over two hours.
[VE clock ticking through the whole segment] A hundred and one miles. Nobody in America had seen a violent
tornado live that long. Its target, if a thing like that has a target, was Guin, Alabama, a town of about two
thousand five hundred, at about nine o'clock at night, in the dark. [HUMAN] A young man named Allen Lindley
put a tape recorder in an open window and recorded a minute of it coming and eighteen seconds of it going
over the house. [VE waveform card; insert audio if cleared] He said afterward, I have the thing on tape.
[HUMAN] Woodrow Haney was in a storm cellar and said it sounded like two or three freight trains plus maybe a
jet bomber. [HUMAN] Becky Todd's family car was rolled with the family inside. She told them to hold on to the
seats. Her sons Mark and Paul did not survive it. [HUMAN] Robert Pennington worked for the electric
department. He came back to find no house, no foundation, no framing, nothing, and his wife Juanita, who was
sixty four, dead. [RS]

**A4-S3 (160 w) · g-scale all seven bars lit · aerial of Guin · g-person Mildred McGuire.** Seven hundred and
thirty seven houses were destroyed in Guin, a hundred and ninety one of them mobile homes. Twenty eight dead by
the official count, thirty two by the town's own. [VE bar 7 lit, the set complete] The pharmacist, Mildred
McGuire, survived with a broken pelvis and later wrote a poem about what the town did next, which was rebuild
on the same ground. [HUMAN] That was the seventh F5. Seven, in nine hours, from Indiana to Alabama. By
midnight there was nothing left to count but the dead, three hundred and thirty of them by the government's
number, five thousand four hundred and eighty four hurt. [RS] And one man in Chicago was already planning
to count everything else. [Q L5] *(blackout 0.9 s)*

### A5 · ten months in the air (14:10–17:40, 480 w)
**A5-S1 (150 w) · g-survey: a small plane over the map, the tracks appearing under it, a date ticker April 1974 → February 1975.** Ted Fujita had published his scale in 1971. [HUMAN] It graded a tornado from zero to five by the
damage it left, because nobody could measure the wind inside one. Three years later the third of April gave
him a hundred and forty eight tornadoes to grade at once, and he did it the only way he trusted. He flew.
[VE plane, tracks] Ten months. More than ten thousand miles of low aerial survey. Every track hand drawn onto
one map, [RS] with its rating, its width, its length, in his own pen. When he was finished, the map showed
thirty tornadoes rated F4 or F5, more violent tornadoes in one day than any outbreak before or since. [VE
g-master-map becomes Fujita's hand map]

**A5-S1b (130 w) · g-mechanism: how a rating is read from a house, one card, four frames.** Here is how you grade
a tornado from the air when the wind is long gone. [VE card: a house in four states] A house with its roof off
is an F2. A house with its walls down is an F3. A house swept clean off its slab, the slab still there, the
house somewhere in the next county, is an F4 or F5, and the difference between the two is how well the house
was built and how far it went. [RS] Fujita flew low over ten thousand miles of slabs and read them like a
doctor reading x-rays. Seven times he found whole streets swept to the foundations, and seven times he wrote
the top of his scale. That is where the number in the title comes from. It was counted from the air, house by
house.

**A5-S2 (170 w) · g-mechanism: one card, the ingredients; g-scale.** Here is what the map proved. Seven F5s did
not come from seven freak storms. They came from one air mass. [VE the card: warm Gulf air below, dry air
above, a jet stream on top, a cold front as the trigger, one diagram, labelled in plain words] Warm wet air
off the Gulf, dry air riding over it, a jet stream at the top turning the whole column, and a cold front to
set it off, from Illinois to Alabama, all afternoon. Every storm that formed in that column had the same
engine. That is what an outbreak is. It is not a lot of tornadoes. It is one machine making them for sixteen
hours. [RS] And inside the survey Fujita found something else, a pattern of damage laid out in straight lines,
trees down like combed hair, that no rotating wind could make. He had no name for it in 1974. He would call it
a microburst, and it would go on to explain airliner crashes. [RS]

**A5-S3 (160 w) · g-then-now v1: FIXED / STILL MISSING scorecard.** What the country did with the map. Weather
offices got backup power, because some had gone dark that afternoon. [VE scorecard row lights] Offices,
police and radio stations got a system for talking to each other during a warning instead of after it. The
argument for a radar that could see wind, not just rain, got the evidence it had needed, and it took another
generation, but the Doppler network that watches the same sky today grew out of days like this one. [VE row
lights, labelled "contributed", never "caused"] And the scale, Fujita's scale, became the one every warning
still uses, updated in 2007, top mark still five. The one thing the map could not fix was geography. The
corridor it drew across north Alabama is not farmland any more. [Q L6] *(blackout 0.8 s)*

### A6 · the same corridor today (17:40–20:50, 450 w)
**A6-S1 (150 w) · g-master-map: today's city footprints laid over the 1974 tracks · popfig "MADISON COUNTY · 433,000".** Put today's map under the 1974 tracks. [VE] The two Tanner tornadoes ran across what is now
Madison County, Alabama. Four hundred and thirty three thousand people live there. Huntsville, at the end of
that corridor, is the largest city in the state and its fastest growing, about a quarter of a million people
where the 1974 map shows fields. [RS] North of Louisville and south of Lexington, suburbs sit across the
Kentucky tracks, and the same ground was hit again in the outbreak of March 2012. Nothing about the sky
changed. What changed is how many roofs are under it.

**A6-S2 (160 w) · g-then-now v2: 1974 vs today, lead time, radar, sirens, phones.** So take the dominant
question straight. Could the third of April happen again? Yes. The ingredients are ordinary spring weather in
that corridor, arriving together, and they arrive together about once a generation. Would the warning reach
you? That is the part that changed. [VE two columns] In 1974 the average lead time was measured in seconds
for many towns, and fifteen minutes at Brandenburg was called good. Today it averages a quarter of an hour,
and a long-track storm can give half an hour. [RS] In 1974 the radar saw rain. Today it sees the wind turning
inside the storm before the funnel exists. In 1974 the warning was a radio you had to have switched on. Today
it is the phone in your pocket, and it will wake you up. Allen Pearson's forecast was right a day early, and
three hundred and thirty people died because a correct warning could not travel. Today the warning travels.
The houses moved into the path instead. [RS]

**A6-S3 (140 w) · g-person Gus Allen returns · Brandenburg today, muted footage · the thesis.** [HUMAN] Gus Allen
still lives near Brandenburg. His sister, his brother, his small cousin are on the memorial there with twenty
eight other names. It was just a bad day, he said, and he is right, and the point of this whole story is that
the day was not rare. The air mass was ordinary. The front was ordinary. Seven F5 tornadoes came out of one
afternoon because the ingredients lined up, and the ingredients still line up. What the country built after
1974 buys you fifteen minutes you did not have then. [PAY]

**A6-S4 (120 w) · g-then-now v3: the fifteen minute card, three rows.** So do the arithmetic on fifteen minutes.
[VE card] A basement or a storm shelter is thirty seconds away. An interior room on the lowest floor, no
windows, is a minute. A car on a highway trying to outrun a mile-wide tornado is the one thing every survivor
on this map would tell you not to do, and it takes longer than fifteen minutes to fail. [RS] Brandenburg had
fifteen minutes and lost thirty one people, because in 1974 most of them were still finding out. Today the
minutes are there. Fifteen minutes is enough to get below ground and not enough to get out of town. Know
which one your house is before the day comes. That is the whole answer.

### Z · close (20:50–21:35, 70 w) · g-outro
Where are you watching this from, and do you have a place below ground? Tell me in the comments, I read all
of them. The 2011 Super Outbreak and Joplin are linked below, and the Storm-Ready Home is the first link in
the description. Fifteen minutes is enough if you already know where you are going. See you in the next one.

---
## Fact register (every number above; `[verify]` = confirm from a primary source before TTS, unverified = cut)
- 148 tornadoes, 13 states + Ontario, 2,598 combined miles, 30 F4/F5, 5,484 injured, ~$5.3 B (2024 $): NCEI
  page. Dead: NCEI 335 / NOAA 330 — the script says "three hundred and thirty" and "by the government's number";
  `[verify]` which figure the NCEI page carries today and use that one everywhere.
- 15 tornadoes on the ground at once `[verify primary; Wikipedia only]`. Seven F5s `[NCEI/Fujita, confirm list]`.
- Pearson's 2 April calls (every office, radar service, staffing, satellite) `[verify beyond Wikipedia; NWS or
  NOAA history page]`. Commerce Gold Medal 1974.
- DePauw F5: 2:16–3:25 pm CDT, 62 mi, 6 dead, six counties named `[verify NWS Indianapolis page, 404 on fetch]`.
- Brandenburg: 3:30 pm CDT, ~2,400 ft wide, 128 homes + 30 businesses, 31 dead (28 in town), 15 min warning:
  NWS Louisville. Town population ~1,700 `[verify 1970 census]`. Tim Haley 15, "169" `[army.mil, secondary]`;
  Gus Allen quote `[WAVE3, secondary]`; memorial name count `[verify]`.
- Xenia: warning 4:10 pm EDT (Montgomery + Greene), touchdown ~4:33 near Lower Bellbrook Rd, city 4:40, ½–1 mi
  wide, 32 in city / 34 on path, 1,150–1,300 injured, ~1,400 buildings incl. 7 schools, ~$250 M 1974 $: NWS
  Wilmington. David Heath / "The Boy Friend" / bus on stage `[Cedarville retrospective, secondary; find a
  Xenia Gazette or WHIO primary]`. "Deadliest single tornado of the day" `[verify vs Brandenburg 31 + Guin 28–32]`.
- Fujita F6 for Xenia, "inconceivable" `[Chicago Magazine; find the Fujita/Abbey 1981 wording]`.
- Cincinnati WSR-57 installed 1960, five simultaneous hooks, Sayler Park warning 4:45, 3 dead: NWS Wilmington.
- Louisville F4 4:37–4:59, 2 dead; Dick Gilbert WHAS helicopter; Nixon commendation `[LPM + Wikipedia; verify
  the commendation document]`.
- Tanner 1: ~6:20 pm CDT near Moulton, ~90 min, 51–52 mi, 28 dead `[WAAY, secondary; NWS Huntsville 404]`.
  Tanner 2: ~7:30, 1 mi west, ~98 mi, deaths split `[unverified; say "about fifty together" only if a primary
  supports ~50 combined]`.
- Guin: 8:25 pm CDT Caledonia MS → 10:30–10:57 pm Morgan Co AL, 101–102 mi, 1,350 yd, 28 (NCDC) / 32 (Tornado
  Talk), 737 houses / 191 mobile homes, $45 M; Lindley, Haney, Todd, Pennington, McGuire quotes: Tornado Talk
  `[secondary; quotes verbatim from that page only, on-screen attribution "Tornado Talk oral history"]`.
  Guin population ~2,500 `[verify 1970 census]`. "Nobody had seen a violent tornado live that long" `[soften to
  "one of the longest-lived" unless a primary supports the superlative]`.
- Fujita: scale 1971, ten months, 10,000+ miles, 148 tracks hand-drawn, 30 F4/F5, microburst origin
  `[Chicago Mag + Climate Central; verify against Fujita 1981 and the NWS microburst history]`. "Airliner
  crashes" `[Eastern 66 1975 / Delta 191 1985; verify]`.
- Ingredients card (Gulf moisture, dry layer, jet, cold front) `[verify against the NWS Wilmington synoptic
  summary; keep the words plain]`.
- Post-1974 changes: backup power, inter-agency coordination, Doppler "contributed" `[NWS Wilmington; keep
  "contributed"]`. EF scale 2007: NCEI.
- Today: Huntsville 249,102 (2025), Madison County 433,516 (2025): huntsvilleal.gov. Louisville/Lexington
  suburbs + 2 March 2012 `[Yale Climate Connections, secondary]`. Lead time then vs now `[LiveScience,
  secondary; find NWS/NOAA lead-time statistic; if none, cut the numbers and keep "seconds then, a quarter of
  an hour now" only with a source]`. Phone alerts (WEA) since 2012 `[verify]`.
- Once-a-generation ingredients `[editorial; soften to "every few decades" unless sourced]`.

## Pre-TTS gates (script-os.md)
1. Retention scorecard per minute (6 axes, 1–5); no two consecutive low minutes.
2. Cut filter A/B/C/D per sentence; cut D.
3. Visual audit: every `[RS]` has a `[VE]` (checked: 14/14 above).
4. AVD pass at 0:30, 1:30 … 20:30.
5. Fact-QC: zero open `[verify]`; homograph scan (read → "reed", live, wind, record, lead, tear, close).
6. Probe-TTS H + A4-S2 → recompute words at measured wpm → trim to 22:00.

## Build plan (after owner approval of this script)
1. Fact-QC agent clears the register (primary sources only), edits numbers in place, lists what was cut.
2. TTS per segment → words.json.
3. Sourcing: NOAA Photo Library + Wright-Patterson aerials (PD), Commons Xenia set (licence per file), NWS
   Wilmington/Louisville galleries (licence per set), WHAS audio (licence request), Tornado Talk tape (rights
   request), FEMA/NWS 50th-anniversary video (PD), stock fill; provenance rows with `shot` per clip; one
   labelled grid read before wiring.
4. Compositions: 8 hand-authored comps above, library first (#4 clock, ep3 map-route-fit, ep2 stat panel).
5. Static suite → freeze scan → comp lint → frame read → ONE draft → owner preview → ONE full render.
6. master_deliverables → metadata (first URL = paulraymond.online, book line at the CTA time, links to the 2011
   Super Outbreak and Joplin) → PR.
