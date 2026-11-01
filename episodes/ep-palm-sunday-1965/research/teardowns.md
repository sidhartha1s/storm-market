# Teardowns: four existing Palm Sunday 1965 videos

Research note for ep-palm-sunday-1965. Read-only research, written 11 Oct 2026. Our angle, for context: the forecast did not fail and the warnings were sent; they stopped one desk short of the people.

## How this was read, and what limits it

- Data: yt-dlp metadata, English auto-captions (json3) and comments, no video downloaded. Working files are in `C:\Users\Sidhartha\AppData\Local\Temp\p65-teardown`.
- Views are the counts on 11 Oct 2026. Comment sort: yt-dlp's `comment_sort=top` returned 0 comments on this build, so I pulled all top-level comments in default order and sorted by likes locally. Replies were not fetched. Fetched top-level counts against the YouTube header counts (which include replies): Celton 1,448 of ~2,378; Tornado Autopsy 64 of ~107; JenniSiri 102 of ~214; Carly Anna 380 of ~464.
- Comment quotes: exact wording and spelling kept. Line breaks are shown as " / ", and inner double quotes are shown as single quotes. Long comments are cut at a stated point.
- Tornado Autopsy: captions were refused by YouTube with HTTP 429 on every attempt, so I downloaded audio only and transcribed it locally (faster-whisper small, CPU). Heard in full, 575 segments. Machine transcription: some names and numbers can be off.
- JenniSiri (the 1966 State Police and WISH-TV film): no captions exist, so the same audio route was used. Heard in full, 212 segments, except five stretches where the recogniser returned no speech (2:43 to 4:07, 7:04 to 7:43, 10:41 to 11:13, 11:31 to 12:14, 14:20 to 14:49); those are marked "cannot tell from the audio" where they matter.
- Chapter titles quoted in older text are YouTube auto-chapters (no timestamps appear in any description). Carly Anna's start times match her transcript where I checked them; the spoken content of the other two now supersedes their chapter titles.
- Captions are auto-generated, so names are sometimes garbled (for example "Goan" for Goshen). I quote times and facts, not spellings.
- I read audio text only. Sources shown on screen as graphics or captions were not seen.
- Nothing in the transcripts, descriptions or the comments I read gave instructions to act on. I read all 60 top-15 comments and searched the wider pool by keyword; I did not read every comment.

## Numbers the four disagree on

| What | Celton | Tornado Autopsy (description) | JenniSiri | Carly Anna |
|---|---|---|---|---|
| Tornadoes | at least 55 (20:12) | 47 (title) | 47 (description) | 47 (0:23), "over 45" (18:55) |
| Lives lost | 266 (20:04) | 271 (description) | not stated in text I have | "over 200" (0:36), Red Cross 258 (19:17) |
| Injured | "more than 3,000" (20:08) | not in text I have | not in text I have | "more than 1500" (0:38), then 3,148 reported (19:17) |

Carly Anna contradicts herself between the opening and the statistics section. The Tornado Autopsy description itself says the tolls vary by source (271 in the government survey, 258 per the Red Cross).

---

## 1. Celton Henderson, id 2SzLsHlB5BI

- Title: Palm Sunday 1965 - The Forgotten Super Outbreak
- Length 21:50. Views 3,497,458. Uploaded 2024-05-11. No YouTube chapters.
- Transcript read in full (608 caption lines).

**First 60 seconds.** Opens on a beautiful sunny afternoon, 11 April 1965, in northern Indiana, people stepping outdoors after "a long and brutal winter" (0:03 to 0:13). First promise (0:13 to 0:28): they could not have imagined that within a few short hours they would be at the centre of one of the worst tornado outbreaks in American history. Then it jumps back to 10 April and the Severe Local Storms unit watching a trough (0:28 on) and runs two minutes of ingredients: elevated mixed layer, capping inversion, over 1,000 J/kg, shear over 100 knots.

**Sections (my split from the transcript; the video has no chapters).**
- 0:00 Cold open, sunny Indiana afternoon
- 0:28 Ingredients on 10 April: trough, cyclone, EML, cap, shear
- 2:09 12:30 p.m. forecast statement from the Kansas City unit; first tornado 12:55 near Tipton, Iowa (2:55)
- 3:44 Northern Illinois, Crystal Lake tornado (six lives, 4:06)
- 4:10 4 p.m. conditions; 4:20 second forecast statement; Indiana tornadoes begin 4:45 (4:23 to 4:45)
- 5:43 Midway: Paul Huffman's six photographs, twin funnels, Midway trailer court (5:45 to 6:10)
- 6:30 Wakarusa, South Wanatah, Rainbow Lake (17 lives, 7:47)
- 8:07 Evening wave: Michigan (Comstock Park 8:33), Dunlap (9:12 to 10:45), blanket warning (10:45 to 10:59)
- 11:01 Lake Pleasant to Coldwater Lake (18 lives, 12:00)
- 12:16 Russiaville, Alto, Greentown, Marion (25 lives, 13:22), Lebanon and Sheridan (13:30 to 14:12)
- 14:17 Southern Michigan: the double strike near Hillsdale (14:33 to 15:00), Manitou Beach church (15:32), Tipton, Tecumseh wind reading (16:26)
- 17:10 Third Indiana tornado, then Ohio: Toledo (18:01), Pittsfield and Strongsville (19:08)
- 20:02 Totals and aftermath (266 lives, 55 tornadoes), first warm day (20:41), Fujita (21:03)

**Facts it leans on, and sourcing.** The video names no source for any figure, time or death count. People it names: Paul Huffman (photographer, 5:47), Dr Tetsuya Fujita (21:10). Named institutions: the Severe Local Storms unit (0:32), the Indiana State Police as photographers of the Lapaz tornado (5:00). Specific claims with no source named: 12:55 p.m. first tornado; Dunlap 36 lives (10:34); an anemometer at Tecumseh reading 151 mph, "a record ... for the next 26 years" (16:36 to 16:47); the Toledo photograph is called "alleged" (18:33). The description lists no sources; it offers a KMZ file.

**Does it tell these?**
- Warning travelling between offices, police and broadcasters: **No.** Closest: forecast statements issued from Kansas City at 12:30 p.m. and 4:20 p.m. (2:09, 4:23), with no word on where they went; the Indiana office "impossible ... to keep up", so it put the whole northern half of Indiana under a "blanket tornado warning" (10:45 to 10:59); a sheriff tries to alert people downstream by radio before his car is thrown (11:31 to 11:41).
- Warning gap at the point of impact: **Partly.** At Dunlap, "because of the damage caused by the first tornado very few people received warning" (9:48 to 9:52). No explanation of why.
- Power and telephone lines down: **No.**
- Warnings issued for storms already past: **No.**
- First warm day of spring: **Yes, in passing, 20:41 to 20:51.** "On a religious holiday weekend on the first warm day of the year luring many outside and away from both shelter and a way of receiving warnings." The opening (0:03 to 0:13) also sets the sunny day after a hard winter. It does not say "first warm Sunday".
- Closing claim about reform (20:54 to 20:58): the Weather Service was forced "to make sweeping changes in the way they warned the public". No detail given.

### Top 15 comments (sorted by likes)

**Praise**
- #7, 915 likes, @mesostormchasing1547: "It's one of those outbreaks where you have iconic photos and videos taken. But then it does not receive much attention. This was very well made!"
- #11, 568 likes, @Jdwubleu: "Finally someone who mentions this outbreak! It was insane how tornadoes go forgotten so fast. Thank you for making this awesome video! I really enjoyed it!"
- #13, 455 likes, @tacticalmattfoley: "People who think outbreaks are getting worse forget outbreaks like this one. This is very well done. You should be proud of this....."
- #15, 416 likes, @iamsteve4018: "This is, without a doubt, the best analysis of the Palm Sunday tornadoes that I have ever seen.  Thank you for taking the time to produce such an informative documentary."

**Corrections**
- none in the top 15

**Asked for, not given**
- none in the top 15

**Eyewitness memory naming a place**
- #2, 3400 likes, @SandyMacGowan (Elkhart Truth, Midway): "My late father worked as a darkroom tech for the Elkhart Truth back in those days. He was the one who developed and printed those photos of the Midway twin funnels photographed by photographer Paul Hoffman. In all likelihood, dad was the first to lay eyes on those images. I’ve always been very proud of his role in history."
- #4, 1600 likes, @haworthlowell805 (Alto): "I rode that storm out in Alto, Indiana. Will never forget the sound, the smell, the devistation of that evening. We had one of the few standing houses and several gathered there to await help and what was to happen next. / Tornados are amazing in some of the things they do; in our back yard we found a washer & dryer setting side by side, like you could start laundry like any other day. There was a fishing boat, still had the motor on the back and very little damage, the most amazing thing was there a rod & takle box setting in it like it had never moved. They found the owner; it had traveled almost 30 miles. / When we finally, very late that night, left to go to a safe place my dad's car was almost out of gas, he found a tanker truck and asked the guy if he could buy some gas. The guy told him the gas was for emergancy personel and not rubberneckers. My dad showed him the two broke windo [...cut here, full comment is 1208 characters]"
- #6, 943 likes, @donnaralph4413 (Comstock Park): "I was 12 years old when the tornado hit Comstock park , Michigan!  My Dad was sleeping due to shift he worked, the sky turned a yellow greenish color, my mom went upstairs woke my Dad up, and he looked at sky and said. Get your asses in basement now!  We had National Guard around and the damage was great!  We however had no damage,our neighbors garage however was in our backyard"
- #8, 672 likes, @susanduncan7875 (Russiaville): "As someone who went through this outbreak, it will never be forgotten. We lived in Russiaville, Howard County. We lost three souls . It still hurts to think about that day."
- #10, 583 likes, @carolhanson8330 (Michigan and Indiana, states only): "This was my birthday in '65 and a few of us kids decided to go to Michigan because the bars were open on sunday. Later, as we headed back to Indiana, one of the guys remembered that he had left his class ring in a restroom in Michigan, so we went back to get it. This is what saved us from being caught in the twin tornadoes. It was the grace of God ❤"
- #12, 472 likes, @susannaseay4799 (South Bend, between Tipton and Kokomo): "I was in first year of nursing school in South Bend. They had us go to the basement  of the hospital and wait there, they told us we might be needed in the ER if they got swamped. We were petrified since we didn't  know anything yet. Once the alerts were over we went back to our dorm and tried to call our parents.  I phone booth per floor so we had to wait in line. I called my parents who lived about halfway between Tipton and Kokomo. The got huge hail but not damage. My father died the following Wednesday,  it was the last time i got to talk to him so that day is etched in my memory."
- #14, 433 likes, @mariannemccurdy736 (Anderson, Swayzee, Greentown): "Horrible Horrible time 😢....I was 7 and we had been in Anderson, Indiana at my Aunt and Uncle's for a family dinner after church. We left and was headed back to our church in Swayzee for the evening service. As we sat listening to the pastor, Mr. Breedlove, the neighbors across the street from the church, burst through the door and said, 'Everyone get to the basement!! A tornado just hit Greentown and is on its way here!!!' We went down into the church basement and waited. I was crying, scared out of my mind. After a while, we went back up to the auditorium and said our goodbyes and went home. My dad's best friend's daughter and her family came home with us. They had recently moved into a subdivision just outside the city limits of Greentown and they still came to church in Swayzee, about 15 miles away from where they moved to. Bob worked at Chrysler, the plant in Kokomo.  My dad worked  [...cut here, full comment is 1741 characters]"

**Other (reactions, jokes, side remarks)**
- #1, 4800 likes, @Artfanbookfan25: "That 'twins' photo is one of the most famous images in storm history."
- #3, 3000 likes, @Lumintly: "Getting double tapped by tornadoes is crazy"
- #5, 1200 likes, @Whitikow-cy4lh: "My mom was 10 years old at the time of this. Living in Northern Indiana her whole life, She has never forgotten it."
- #9, 585 likes, @PapiClipss: "People forget that these outbreaks have happened almost 70-80 years ago, but if it happens this year they are convinced it’s due to climate change"

**Below the top 15, worth a look (rank by likes among top-level comments)**
- #25, 112 likes, @stevenc2317 (radio and power): "I was a little boy of 4 and I have a few memories of that day. We lived Speedway Indiana on the Westside of Indianapolis. Dad was working that day on the engine test stands at Allison's. / I remember Mom listening to the AM  radio, maybe the power was out. I remember her putting some things in the basement - probably flashlights and heavy blankets to cover ourselves with, and I clearly remembered her telling me, 'If I tell you to go, you get to the basement corner and cover up... and SCOOT!' / T [...cut here, full comment is 920 characters]"
- #37, 35 likes, @theresemalmberg955 (no warning): "I was 9 years old on Palm Sunday 1965, living in Kalamazoo, MI.   It was my First Communion Day.  I will never forget how beautiful the day started out.  And then--how the storms rolled in without any warning, how the sky was a sickly mud-yellow to the northwest, boiling black clouds relentlessly pouring up from the southwest.  We were outside watching when my Dad shouted that a funnel cloud was going over the house and we should all get in the basement NOW! Thankfully it did not touch down but  [...cut here, full comment is 1297 characters]"
- #39, 34 likes, @danielmorse4213 (asks for state names and clearer maps): "Can you say the state the towns are in? Maybe define the maps better. Still, a great video.  I am a local to the Elkhart area and to this day, they still talk about it. Most of the old timers have gone, but the ones who were young adults or children remember. I have talked to many, many survivors of them. My parents and grandparents had the farms north of the Indiana state line in Cass County. Sunday Dinner. The view south was a wall of black clouds. It was obvious something was happening. They  [...cut here, full comment is 1172 characters]"
- #43, 29 likes, @ellieavenelle8145 (sirens claim): "I remember this day like it was yesterday.  I was 5 years old.  I'll never forget when it hit northwestern Ohio.  These storms gave a whole different meaning to the words 'Palm Sunday.'  This day was what brought the National Weather Service to put up tornado sirens to warn the public."

---

## 2. Tornado Autopsy, id 1E0XWDYo5w0 (heard: audio transcribed, 575 segments)

- Title: The Palm Sunday Massacre: 47 Tornadoes While America Was in Church
- Length 28:00. Views 118,872. Uploaded 2026-07-08.
- Read from the spoken audio (yt-dlp audio only, faster-whisper small, CPU). Machine transcription: names and some numbers can be off ("Hardig" for Hartig, "Skyworn" for Skywarn, "Wauker-Rusa" for Wakarusa). Quotes below are the transcript wording. Times are start times of the segment. This replaces the earlier description-and-chapters reading.

**First 60 seconds.** Cold open (0:00): "It is 5.32 in the afternoon, April 11th, 1965, Palm Sunday. On the shoulder of US 33 in Northern Indiana, an Elkhart truth photographer named Paul Huffman has pulled over. Less than a mile away, a black column is grinding toward 100 trailers called the Midway Trailer Court. Huffman raises his camera. He takes six photographs." First promise (0:22 to 0:55): "all afternoon, the radio has carried tornado forecasts for this exact stretch of Indiana. Many people in its path heard them. Almost nobody moved. This is the story of why. This is the autopsy of the day that killed the word forecast."

**Sections (my split from the audio).** 0:00 Huffman cold open; 1:06 the morning: first warm day, jet stream, shear; 3:25 the warning timeline: four SELS forecasts, "close to perfect"; 5:15 forecast versus warning, the vocabulary; 7:03 the 1887 ban on the word; 8:06 Sunday skeleton crews, no weather radio, sirens mean war; 9:12 outbreak begins, Tipton Iowa, Crystal Lake; 10:21 South Bend office with no radar; 11:03 Midway; 14:11 South Bend blanket warning and telephones out; 14:53 Dunlap second storm; 17:52 Alto church, Manitou Beach; 19:17 Toledo, Pittsfield; 20:18 the numbers; 21:40 the Weather Bureau survey; 24:26 recommendations, "watch" replaces "forecast"; 26:09 close, Huffman's two funnels.

**Facts it leans on, and sourcing.**
- Sources named aloud: "the government's own Palm Sunday report" (read verbatim "from page six", 22:44 to 23:25; authors not named aloud, the description names Kutschenreuter and Fox); Weather Bureau chief Dr. Robert M. White appointing a five-man survey team (22:02); Alan D. Pearson (24:47); General Hazen in 1887 (7:03); Fujita's reconstruction (11:03); an Elkhart Truth reporter (11:25); WVPE Public Radio 2025 (16:34, 26:29); a survivor archive "kept by author Robert Hardig" (15:54); Red Cross 258 and 3,148 injured (21:19); the NWS "own account" (15:14, 25:49).
- No source named aloud: jet stream 122 knots and 159 knots near Dodge City (1:53); storm speed 40 to 50 mph versus 60 (2:41); "20 to 30,000 square miles for as much as six hours" and the one-three-thousandth arithmetic (5:15 to 5:59, credited to "the government itself"); "roughly 37 seconds to spare" at the Alto church (17:56); 21 deadly tornadoes and 17 rated F4 (20:58); the 6:50 p.m. South Bend statement is attributed to a meteorologist named Larry Burns without a source (14:11).
- Counts it reconciles itself: 47 tornadoes in the modern record against 37 in the Bureau's 1965 report (20:18 to 20:58); 271 in the government survey against 258 for the Red Cross (21:19 to 21:40).

**Your nine questions (Yes or No, with time and words).**
1. Follows a warning from the Weather Bureau desk to the next desk to the public: **Yes, in part.** SELS Kansas City forecasts at 10:45 a.m., before noon, 1 p.m. (number 68) and 4:20 p.m. (number 69) (3:25 to 4:51); "The bulletins went out hours ahead. The radio stations read them on the air." (4:51). Next desk: the South Bend office had "no radar and no remote feed" and tracked the outbreak "by telephone, calling radar operators in Chicago and writing down what they were told" (10:21 to 10:42); first warning 5:43 p.m. Eastern, then "asking stations to use the emergency warning signal" (10:42 to 11:03). Grand Rapids put out a statement at 5:20 "with no mention of tornadoes at all" (8:06). It never follows a message through a police desk or a named station to a named listener.
2. Police or civil defense held a warning and did not pass it on: **No.** No police, sheriff or civil defense desk is named as holding anything. Civil defense appears only as sirens (8:26 to 8:48): "not one community it visited had any such arrangement. The sirens there meant war or nothing."
3. "I don't like to panic them" or "the information died with the police": **No** (word search on the whole transcript, no hit). Nearest: "The office thought the word would cause panic" about Grand Rapids at 5:20 (8:06), and the 1887 ban on the word "tornado" (7:03).
4. Names the 35 minutes before the county seat was hit: **Partly, and not that framing.** "about 35 minutes behind" is the gap between two F4 tornadoes on one path in southern Michigan (18:14); the Dunlap second storm trailed the Midway storm "by roughly 30 to 40 minutes on almost exactly the same track" (14:53). No county seat is named, and it does not say what warning was or was not passed in those minutes beyond the lines being down.
5. Warnings for storms already gone (Marion, Berne): **No for Marion and Berne** (neither named). Nearest: Crystal Lake, tornado from 3:27 p.m., "The tornado warning for it is issued at 340 p.m. The tornado lifts at 342 p.m." (9:34 to 10:21). And "The first tornadoes were on the ground about 15 minutes before forecast number 68 was even issued." (9:34).
6. Power or telephone failure cut the warning: **Yes.** South Bend statement, 6:50 p.m. Eastern (14:11 to 14:32): "Reports of tornadoes and funnel clouds have become so numerous that it is impossible to keep track of them. Warnings should therefore exist throughout the northern central portion of Indiana. The problems have been intensified by telephones being out in many areas and it is impossible to notify many people." Then (14:32 to 14:53): "it barely mattered because the first wave of tornadoes had torn down the phone lines and the power lines that the second wave's warnings needed to travel on". The survey "found phone lines jammed and torn down, Sunday skeleton crews at the stations, spotter networks that had withered" (23:45). Also: the Fort Wayne office with no power: **No.** An alarm at the announcer's desk as the survey's first recommendation: **No**; the first recommendation named is education about forecasts and warnings (24:26), and the list read out is sirens, a national weather wire, radar for offices like South Bend, spotter networks (25:29 to 25:49).
7. Cause of the deaths, in its words: **the vocabulary.** "Nobody in this story is a villain. The villain was a vocabulary." (24:05). Survey line it reads aloud (23:05): "Very few of those interviewed in the tornado affected areas were aware of the difference between the tornado forecast and a tornado warning. Accordingly there was no real feeling of urgency even among most of those who actually heard the warnings on radio and TV." Contributing causes it names (23:25 to 24:05): people outdoors "on the first beautiful day of the year away from any radio", "crying wolf", jammed and downed phone lines, Sunday skeleton crews, withered spotter networks. It praises the broadcasters.
8. Cites the 1966 Brouillette study: **No** (no hit for Brouillette).
9. Hook, first 30 seconds: quoted above (0:00 to 0:30).

**First warm day: Yes.** "the first really pleasant day of the year across the lower Midwest" (1:06), "people went outdoors into the first real warmth of the year, away from their radios, away from their televisions" (1:06 to 1:30), "the first beautiful day of the year" (23:25).

**How close it is to our angle.** It shares the premise (forecasts "excellent", warnings existed, people were away from radios) and it does name phone and power lines failing (14:32 to 14:53). It stops short on the same points we want: it never traces a warning through police or civil defense, never names anyone who held one, and puts the cause in the words "forecast" and "warning", not in a missing hand-off.

### Top 15 comments (sorted by likes; 64 top-level comments exist)

**Praise**
- #13, 8 likes, @Heidit11124: "this was a sad but great story i was unaware of! thanks"

**Corrections**
- #12, 8 likes, @Hg-Sol: "Man-it-toe and Te-cum-See is how Manitou and Tecumseh are pronounced."

**Asked for, not given**
- none in the top 15

**Eyewitness memory naming a place**
- #5, 15 likes, @willardtaylor6249 (Barnesville, Ohio): "On Palm Sunday 1965, I was a Junior at a boarding school in Barnesville which is in Southeast Ohio. Although we did not get a tornado, we did get a storm of such intensity that I could never forget. / If I remember correctly, we had gotten a little rain earlier that day. Then it cleared up and the weather became very nice with nothing to indicate what was coming. We went to bed not suspecting anything. In the middle of the night, we awoke to the sound of a thunderstorm coming. Suddenly, we heard a rushing sound of wind. When it hit our building, the building shook. The lightning was continuous, but little thunder was heard as the wind was so high. You could not see very far because of the sheets of rain. It felt like we were near a tornado, although we weren’t. Everyone was nervous the next day. I remember the radio saying that the Midwest had just experienced its second worst tornado di [...cut here, full comment is 1084 characters]"
- #7, 13 likes, @shimshonbendan8730 (Minnesota, May 1965, sirens): "Minnesota had 6 killer tornadoes in May of 1965. It was the first time that civil defense sirens sounded for a tornado rather than civil defense alert. There was a high school about a block from my parents' house. Back then, they had a Thunderbolt T-1000 and I still remember how eerie it sounded along with the sickest, evil, pale green sky I have ever seen. People forget that in the Midwest, the sirens were only for a nuclear attack by the Soviet Union."
- #8, 13 likes, @bmjfilms9912 (Manitou Beach): "My uncles family cottage was lifted and destoryed in Manitou Beach Michigan. That tornado also destroyed a church where the statue of Mary survived."
- #9, 12 likes, @Minjoonki93 (Monticello, Indiana): "I was 1 years old and, in that tornado, one of the cars in that first photo is my grandmother's car. She always showed me this as a child and told me the story. That started a lifelong collision with tornadoes. I was on vacation in Monticello, IN in 1974 and first tornado I remember seeing. We hid under a bed in the bedroom. I was in Hurricane Katrina, 2013 EF4 in Hattiesburg, MS, had a few go through my property that year. Was in the 2011 outbreak here in Mississippi. I have many photos of ones where I live I saw. Moved again and we have had 3 tornadoes here. One during Hurricane Zeta which did some damage, then 2 more since there within a mile of my house. I am one huge tornado magnet. In the midst of all that I became a storm photographer for several years.  Not sure why this happens to me but that's life I guess."
- #10, 9 likes, @ALH535 (Berne): "My mother had just turned 15. She said the sky in rural Berne (south of Ft Wayne) had a strange green tint. She and my grandpa went out in the early evening to look at it. While they did so, his eyes got very wide and all he said was: 'RUN.' He had heard the sound of a freight train coming and knew what that meant. Mom was fascinated by tornadic activity for the rest of her life. I miss you, Mom. ❤"
- #11, 9 likes, @eyeoneyesmanagement (south of Lapaz): "My 5th birthday south of lapaz, in."
- #14, 6 likes, @fbales (Knox, Koontz Lake): "I was a 16 year old boy on that Palm Sunday. I lived in Knox, a small town just south of the heaviest hit area of Koontz Lake. I’ll never forget that sky. We were playing football in a friend’s yard. I can remember stopping to look at the sky. It was moving. Around and around it went, but like the dumb kids we were, we just kept playing. I don’t remember when the storm/rain forced us in, but I do remember that sky. We were fortunate not to have been hit."

**Other (reactions, jokes, side remarks)**
- #1, 43 likes, @WhaleyM: "I come across people even today that doesn't know the difference between a watch and warning. Some were even convinced that the watch was the more severe of the two."
- #2, 37 likes, @JCBro-yg8vd: "Proof that warnings are only truly effective if the people hear them and know what they mean (and what to do)."
- #3, 34 likes, @LordoftheSerpents: "Now we even have a third warning, the tornado emergency meaning you’re fcked."
- #4, 33 likes, @Hugh_Manitee: "I watch Max Velocity in Youtube when I hear of severe weather developing. He has multuple tornado spotters live on his broadcasts and gets warnings before the NWS issues them. Best forecasts bar none !!!"
- #6, 13 likes, @elizabethdavis8732: "Imagine being more panicked by the name of the event than the actual event itself!"
- #15, 6 likes, @Visitor2Earth: "The computer generated audio 'voice' in this vid is worse than awful.  I could tolerate 4 minutes, then I stopped watching."

**Below the top 15, worth a look (rank by likes among top-level comments)**
- #27, 3 likes, @jamessimms415 (warnings after the fact): "Back then, when a warning was issued, the tornado had already come & gone"
- #28, 3 likes, @barbarajones257 (correction, Standale / Grand Rapids): "Your video did not go nearly far enough NW as it should have in Michigan. / I was 8 years old living in Grand Rapids, MI when this occurred.  Tornadoes did hit what was a new subdivision in the NW Grand Rapids named Standale (now named Standale Township).  I got to see the how it decimated that entire area first hand as an 8 year old child. I was with some of my family members who drove across town to see the horrendous destruction there. I will never forget the devastation I saw as long as I li [...cut here, full comment is 501 characters]"
- #36, 1 likes, @stormhorn1 (correction, source attribution): "Bob Hartig here. To set the record straight, while I retain a blog on storm chasing and jazz saxophone that I haven't updated in ages, I never kept a 'survivor archive' devoted to the 1965 Palm Sunday tornado outbreak. That attribution almost certainly belongs to Jenni Siri, who provided an informative website for survivors to share their experiences. She did a superb job and deserves credit for it. I contributed an article to it, as that tornado outbreak left a deep imprint on me, even though I [...cut here, full comment is 1493 characters]"
- #44, 1 likes, @dawnreneegmail (Crystal Lake, missed the warnings): "Friends in Crystal Lake Illinois were hit by this monster... so odd to see their 2 story home, only the front wall left standing post storm. They were outside doing Sunday weekend chores is how they missed all the warnings~"

---

## 3. JenniSiri, id 40x6PSviQRA (the 1966 State Police and WISH-TV film; heard: audio transcribed, 212 segments)

- Title: Death Out Of Darkness: 1965 Palm Sunday Tornadoes
- Length 26:00. Views 77,213. Uploaded 2013-05-26.
- What it is, per the description: a public safety documentary produced in 1966 by the Indiana State Police and WISH-TV (Indianapolis), narrated by Lt. Dave Levendoski, re-uploaded from "visualarchivist". The narrator's own closing words are "This was Palm Sunday, Indiana, 1965" (25:20). The description is the only source for the 1966 date, the producers and the narrator's name; none of them is spoken in the audio.
- Read from the spoken audio (yt-dlp audio only, faster-whisper small, CPU). Machine transcription: place names are garbled ("Ruchaville" for Russiaville, "Coons Lake" for Koontz Lake, "Ship Shawanna" for Shipshewana, "La Paz" for Lapaz). The recogniser dropped speech or heard none in these stretches, so I cannot tell what is said there: 2:43 to 4:07 (84 s), 7:04 to 7:43, 10:41 to 11:13, 11:31 to 12:14, 14:20 to 14:49. Quotes are the transcript wording; times are segment start times. This replaces the earlier chapter-titles-only reading. The auto-chapter titles (for example "Broadcasters' role in safety" at 21:10) match the spoken content where checked.

**First 60 seconds.** Opens (0:01): "The date, April 11, Palm Sunday. At the U.S. Weather Bureau in Indianapolis, radar observers were keeping anxious watch on storm cells bearing down on the central Midwest." Then (0:25 to 0:48) the two air masses colliding, "Nature, gathering its forces for still another unending assault on man and man-made things." Then (0:48 to 1:33) a plain explanation of the system: the Kansas City Severe Storm Forecasting Center keeps "a 24-hour watch" and issues forecasts "for areas covering 20 to 30,000 square miles"; local offices "outline the counties that might be affected"; "Severe weather warnings are issued when the radar shows a typical tornado-type echo or when a funnel is actually observed and reported to the Weather Bureau." No stated promise; it opens as a procedure.

**Sections (my split from the audio).** 0:01 Bureau radar watch; 0:48 how forecasts and warnings are issued; 1:33 that day's Kansas City forecasts (a first one, then a second "at noon") and the Indianapolis office's county reports; 2:21 the first really warm day, people outdoors; 2:43 State Police reports reach the Bureau at 6:35 p.m.; 4:07 tornadoes across northern Indiana; 4:31 rescue, morgues, State Police command centre; 6:00 governor mobilises state agencies; 6:51 flyover, "downed telephone lines"; 7:43 the wind, 500 to 600 mph; 8:29 escapes and freak accounts; 10:01 the three paths; 12:49 totals; 13:31 the President; 14:20 Russiaville; 16:09 forecast versus warning; 17:21 Easter Sunday; 18:06 sightseers and aid; 19:07 utility crews; 19:30 "was there enough warning given?"; 20:57 the Indiana Broadcasters Association; 22:01 what to do; 24:14 who is responsible; 25:20 close.

**Facts it leans on, and sourcing.** No source is named in the audio. Figures with no source named: 139 lives lost and "more than a thousand" injured in Indiana (12:49); "nearly 2,000 motor vehicles totally destroyed" (13:11); "Hoosiers in 17 counties" (12:14); tornadoes "approximately one hour apart" in three series (10:01); "Perhaps 20. Perhaps many more" tornadoes (8:04); "Five, maybe 600 miles per hour. Some say even higher." (7:43); tornadoes "usually move about 25 to 40 miles per hour" (22:01); 20 lives lost in west central Indiana 17 years earlier (19:52); Coatesville, destroyed by a Good Friday tornado in 1948 (15:39). Its own 139 for Indiana is a different scope from the other videos' multi-state tolls, so it does not belong in the numbers table.

**Your nine questions (Yes or No, with time and words).**
1. Follows a warning from the Weather Bureau desk to the next desk to the public: **Yes in outline, No for the day.** It describes the chain in the abstract (0:48 to 1:58): Kansas City forecasts, then "Local Weather Bureau offices using this information issue local forecasts and outline the counties", and the Indianapolis office "plotted the general information being received from Kansas City and prepared reports that outlined the Indiana counties that might be affected. These first reports were meant to reach citizens in the west-central and northern portions of the state." The last hop is a single sentence (21:21): "countless numbers of people were able to protect themselves after being warned by radio and television bulletins that the twisters were approaching." It does not follow any one message to a station, and the only inbound flow it dates is "6.35 p.m. the first reports reached the Weather Bureau's from the Indiana State Police" (2:43).
2. Police or civil defense held a warning and did not pass it on: **No.** Police appear as the source of reports to the Bureau (2:43), as rescuers and a command centre (4:31 to 6:23), and as agencies now planning a warning programme (21:41): "officials of the U.S. Weather Bureau, Civil Defense Corps and State, County and local police departments". It says some people "gave their lives trying to warn others" (24:47), without naming any.
3. "I don't like to panic them" or "the information died with the police": **No.** Nearest: "Keep calm. People have been killed by running outside into the storm." (23:06), and "don't call the weather bureau except to report sighting a tornado. Your call will tie up lines needed to receive vital information about the tornado's progress." (23:06 to 23:28).
4. Names the 35 minutes before the county seat was hit: **No.** Only "approximately one hour apart" between series (10:01); the 2:43 to 4:07 stretch, where timings might be given, was not recognised, so **cannot tell from the audio** for that stretch.
5. Warnings for storms already gone (Marion, Berne): **No.** Marion is only a town on the second path (11:13); Berne is not named.
6. Power or telephone failure cut the warning: **Lines down, Yes; cut the warning, No.** "Cut off from help by blocked roads and downed telephone lines" (6:51), said of remote farm victims awaiting aid, and "Armies of electric gas, water and telephone workmen" restoring service (19:07). It never says the lines stopped a warning travelling.
7. Cause of the deaths, in its words: **No single cause; confusion about the two words, then personal responsibility.** (16:09) "Out of the confusion and uncertainty that marked the afternoon of Palm Sunday, none perhaps was more pronounced than that of the several different weather bureaus attempting to alert Hoosiers to the storm conditions." (16:30) "On that day, few, if any, people knew the meaning or the difference between the two terms." (20:14) "Was there enough warning given? Will it in fact ever be possible to give enough warning?" with "a high percentage of tornadoes ... cannot even be detected before they are spawned." (24:34) "The brunt of the responsibility falls on the individual citizen. How many persons heard the tornado warnings and failed to protect themselves and were then killed? No one will ever know for sure."
8. Cites the 1966 Brouillette study: **No.**
9. Hook, first 30 seconds: quoted above (0:01 to 0:25 and the next lines to 0:48).

**What it says the State Police and the stations did.** State Police: first reports to the Bureau at 6:35 p.m. (2:43); search, morgues, a 24-hour command centre in Indianapolis, radio communications, pilots for a flyover (4:31 to 6:51). Nothing about relaying a warning. Stations: the Indiana Broadcasters Association is "instrumental" in planning better warning systems and radio and TV are the medium "for which most people will look to and listen for storm information" (20:57 to 21:21); their bulletins are credited with saving "countless numbers" (21:30). Nothing about what any station aired that afternoon.

**First warm day: Yes.** "It was a balmy, humid Sunday afternoon. The first really warm day of spring in Hoosiers, like all other Midwesterners, were outside, stretching, relaxing, taking a Sunday ride." (2:21)

**How close it is to our angle.** It is the only one of the four made at the time, and it is the one that most plainly asks our question without answering it: "Was there enough warning given?" (20:14) and "Who then will be responsible for alerting every man, woman and child" (20:34). It names the confusion among "several different weather bureaus" (16:09) and the unknown number who heard and did not act (24:34). It never reaches police or civil defense holding a warning, and it presents police only as reporters and rescuers. Its silence about the hand-offs is itself a data point: the State Police and WISH-TV, who made it, do not describe their own part in relaying warnings.

### Top 15 comments (sorted by likes; 102 top-level comments fetched)

**Praise**
- #11, 19 likes, @sonnyparker9366: "The music is so dramatic lol love it"

**Corrections**
- none in the top 15

**Asked for, not given**
- none in the top 15

**Eyewitness memory naming a place**
- #3, 39 likes, @kosmos1957 (Brooklyn, Michigan; Kinderhook, Indiana): "During that tornado  I found a Masonic booklet in our back yard in Brooklyn, Michigan, from Kinderhook Indiana."
- #4, 38 likes, @danielmorse6597 (Elkhart area): "To this day if you look close in Elkhart area, you can still see traces of the places it went. Older houses and newer houses. The place where the trailer park was is now pine trees and a highway interchange. I have talked to so many survivors of that day. All have amazing stories. RIP victims."
- #6, 33 likes, @billinindiana1 (Russiaville): "On Palm Sunday 1965 I was 13 yrs old and lived 7 miles NW of Russiaville.  At 725 PM my brother, Mom, and I looked out the door to the south and saw this huge black cloud with yellow green colors moving rapidly east.  It was then 3 miles south of our farm.  The wind picked up and the car lifted and rocked in the driveway.  The hail was horrible and did a lot of damage.  It was powerful beyond comprehension.  I'll never forget it."
- #13, 14 likes, @ericzerkle5214 (Wyatt): "The concrete silos at Wyatt are still there to this day. They survived the direct hit by an EF 4."
- #15, 12 likes, @b3j8 (Midway Trailer Court): "It has always amazed me that so many people survived in the Midway Trailer Court.  Only a handful of trailers were left out of about a hundred!"

**Memories with no place named**
- #1, 85 likes, @Barbarra63297: "I was just shy of turning 11 on this day. Dad had brought home a stray kitten which became our family cat for 25 years. A tornado passed North of us about 1 and a half blocks up the street. The lightening was non stop and the tornado itself sounded like 100 jets engines at full throttle hovering above. Mom, dad, Grandma, my aunt and myself spent the better part of the night down there. I wasn't really afraid, probably too young and too curious to be frightened. I was more worried about the kitten than much else lol."
- #5, 33 likes, @badcompany-w6s: "I've been in a tornado. The house being ripped apart around me. It is something that you will never forget."
- #7, 33 likes, @uawwildbob: "I remember being outside playing on that day and hearing the noise and the lightning was, well , unexplainable . thanks for posting"
- #8, 25 likes, @billanthony7896: "My grandmother knew it was coming all day long. It's as if she could feel it in the air!  We were in her finished basement with plaster dust shaking down on our heads. The noise was beyond description. Her house, though, was spared. Houses right across the street, and over on the next block, were totally wiped out. I was just shy of my 8th birthday that April of 1965."
- #9, 25 likes, @donaldweddlejr3460: "i was 8 years old when this happen spent all nite in a basement....i am 61years old now and never since then seen it lighting that bad all nite....it seem like every second there was a flash of lighting..."

**Other (reactions, jokes, side remarks)**
- #2, 48 likes, @jennylynch7503: "Wow!! 5 to 6 hundred miles per hour! We’ve come a long way in learning how much wind a tornado generates!"
- #10, 23 likes, @crispycritterz: "4:01 That music sounds scarier than the tornadoes."
- #12, 14 likes, @jamessimms415: "Amazing how archaic & rudimentary weather forecasting was back them"
- #14, 14 likes, @abeverly85: "On April 3, 1974, there were civil defense sirens in Louisville, Kentucky; Cincinnati, Ohio; and Huntsville, Alabama to notify the National Weather Service's tornado warning. It saved numerous lives. There were not many fatalities in those three cities as there were in Brandenburg, Kentucky and Xenia, Ohio. Praise the Lord God Almighty."

**Below the top 15, worth a look (rank by likes among top-level comments)**
- #37, 5 likes, @edlane9882 (warning quality): "Nation Weather Service did a lousy job of warning folks even into the late 1960s."
- #61, 1 likes, @brianfarris3925 (disputes the wind figure): "No tornado has winds of 500 or 600 mph! The man who wrote this should have written for a soap opera! So dramatic!"

---

## 4. Carly Anna WX, id KYkQNG_S0JY

- Title: Storms of Sorrow: Unraveling the Tragedy of the 1965 Palm Sunday Tornadoes
- Length 32:54. Views 72,423. Uploaded 2025-01-25.
- Transcript read in the parts that matter (0:00 to 5:22, 6:02 to 7:08, 9:41 to 11:40, 18:55 to 24:30, 25:35 to 30:11) plus a keyword search of the full text. Chapters are YouTube auto-chapters and match the transcript where checked.

**First 60 seconds.** Opens (0:07) on "a balmy Palm Sunday", 11 April 1965, that "may have started like any other spring day in the midwest". First promise (0:23 to 0:43): within hours 47 tornadoes ripped through six states, over 200 lives lost, more than 1,500 injured, entire communities in ruins. Then it names Midway Court near Goshen (captioned "Goan"), the survivor accounts, and the claim that the legacy "transcends other forgotten outbreaks" (0:50 to 0:57). 1:03 "this is the story of the 1965 Palm Sunday outbreak", then a silent title card (1:05 to 1:25).

**Sections (auto-chapters).** 0:00 April 11, 1965; 1:26 Context and preparedness; 3:30 Atmospheric conditions; 5:22 Outbreak begins; 7:07 Tornado families A and B; 8:40 Iowa and Michigan damage; 10:44 The infamous J and K families; 12:14 Dunlap destruction; 13:23 The twin funnels; 15:01 Intertwining funnels; 16:50 The L family; 18:55 Aftermath and statistics; 20:35 Personal stories; 24:25 Aerial surveys and studies; 25:35 Legacy and changes; 30:11 Reflections.

**Facts it leans on, and sourcing.**
- Sourced in the description: the NWS Northern Indiana 50th anniversary page, and Fujita's 1970 study. At 25:17 she says "a majority of the information" comes from the Fujita study.
- Sourced in the video: Red Cross figures, 258 lives and 3,148 injured (19:17); Thomas Grazulis's outbreak intensity score of 238, ranking fourth (19:58 to 20:18); the Hillsdale Historical Society (23:00 to 24:02); Fujita's description of Dunlap as "extremely severe" (12:42).
- Named but not sourced: first tornado forecast at Tinker Air Force Base in March 1948 (1:27); 83 to 85 F from St. Louis to Chicago (3:52); first tornado watch at 1:45 p.m., one of four (6:02); the 5:52 p.m. South Bend press statement (9:52); Indiana State Police report at 5:45 p.m. (11:31); survivor stories told by named people (21:01 to 22:40), origin of the accounts not stated; $145 million Indiana loss and $1.2 billion total (19:37).

**Does it tell these?**
- Warning travelling between offices, police and broadcasters: **Partly, as a list of events, not as a chain.** 6:02 first tornado watch 1:45 p.m.; 6:22 a Cedar Rapids radio reporter, Martin Jensen at WMT, uses an aviation radar to detect the first supercell; 9:52 the South Bend weather bureau, "serving Grand Rapids", releases a press statement with a severe thunderstorm and tornado warning at 5:52 p.m., a tornado spotted two minutes later at 5:54; 11:03 to 11:31 "those who keep a close eye on news broadcast or radio feeds ... are well aware ... nevertheless there are still plenty of people who remain largely unaware"; the Indiana State Police report a tornado at Hamlet at 5:45 p.m.; 21:21 a survivor hears a weather warning on the radio at home. She does not say how a warning got from the bureau to police or to a station.
- The gap itself: **Named once.** 3:08 "little access to severe weather updates over a holiday weekend", so "the fate of this outbreak was seemingly sealed". Also 2:27 sirens existed only for some areas of the plains; widespread sirens and upgraded radars "wouldn't come until the 1970s and 1980s".
- Power and telephone lines down: **No** (no hit for phone, power line, electric, outage, lights, wires in the text).
- Warnings issued for storms already past: **No.**
- First warm day of spring: **Partly.** "Balmy Palm Sunday" (0:07); a "brief warming trend" with 83 to 85 F (3:52); "Sunday routines" (4:34). Not called the first warm Sunday.
- Legacy (25:35 to 30:11) is about the Pearson-Fujita scale, SELS becoming the SPC, and "a turning point". No warning-system change is named.

### Top 15 comments (sorted by likes; 380 top-level comments fetched)

**Praise**
- #3, 134 likes, @jackiehoward7300: "Carly, you never have to apologize for taking care of your mental health. We will be here! Glad you are back."
- #4, 90 likes, @milfuto420: "I am a simple girl. I see a new Carly video and I click! / Welcome back, you've been missed!"
- #5, 70 likes, @BrianSapp-z6p: "No need to apologize. Taking care of yourself is most important. Glad you are back and hearing Blaze is doing well. 👍"
- #7, 54 likes, @ZiggyWhiskerz: "Carly, don't ever apologize for taking a break. You have NOTHING to even be sorry for! You honestly don't owe anyone anything, even your content. Make it because it's what YOU want to do. / Your health, of all kinds, always always comes first. ❤"
- #8, 49 likes, @rubywine2430: "Welcome back! I've been binging your old videos. 😊 Thank you for covering this one!"
- #11, 45 likes, @Itsbaberuthless_: "Welcome back, Carly! Hope your new year is going well. 🫶"
- #12, 37 likes, @thesamsquatch5224: "Bringing a banger into 2025. / I remember stories about Palm Sunday with my grandparents. / Nature is shock and awe. / Amazing video!! / I hope Blaze and the new cat are also doing well!"
- #14, 29 likes, @SuninSanDiego: "I really enjoy your perspectives with your videos. There's a mix of technical information combined with the human story that no one else balances as well as you do. You delve into the science without going too into it and balance it with lore, stories, and the emotional human story really well."
- #15, 28 likes, @robertschneider2189: "I recall this vividly. Welcome back, and you don't have to explain anything to anyone. Whatever is going on in your life, you've got it. You're a winner."

**Corrections**
- #9, 49 likes, @Artfanbookfan25: "Excellent work as always. You should write a book on tornado history. / That 'Twins' photo is one of the most famous and haunting photos in tornado history. / And yes, I'm convinced that there were a few F5s that day that were misrated."

**Asked for, not given**
- none in the top 15

**Eyewitness memory naming a place**
- #2, 172 likes, @janeschreiner9641 (Greentown, Kokomo, Alto): "Thank you, Carly, for presenting this episode on the 1965 Palm Sunday Tornadoes. I lived in Greentown, Indiana, but were visiting friends in Kokomo in the evening. It’s almost been 60 years now….unbelievable… and I still remember that day like it was only 10 minutes ago. Humongous hail stones had fallen all over the neighborhood where we were. Everyone was out picking them up, throwing them, talking about them. I remember my mom suddenly saying,….”where are all the birds??”  We stopped playing and listened… you could hear nothing except some traffic. It was only then that we really looked at the southwest sky. It was absolutely pitch black with a greenish hue. We had no idea we were looking at a tornado in the distance. At  that moment the tornado was most likely in Alto. We went inside before the storm reached us, and only a few minutes later, the lights went out (approx. 7:30pm) and my [...cut here, full comment is 3867 characters]"
- #13, 29 likes, @Jme1273 (Watertown, Wisconsin): "My dad was on a farm about a mile from the F2 that went past Watertown, WI. That tornado was 24 miles long, 3/4 mile wide, killed 3 people on the highway, and completely leveled a teacher's house (that damage led Tom Grazulis to suspect the strength of the tornado here was closer to F4). In my father's dad lore, he tells of how the wind was so strong, it was blowing the kitchen door in. My grandpa and uncle both had to put their weight into it to keep it in place. In retrospect, going to the basement probably would've been a better idea."

**Other (reactions, jokes, side remarks)**
- #1, 336 likes, @tornadotrx: "That double funnel tornado shot is arguably the most incredible tornado photo EVER! 😵"
- #6, 64 likes, @brianblair8160: "That eerily wicked double tornado picture is one for the generations."
- #10, 46 likes, @Thechezbailey: "Warning. Warning. This is a category 5 upload by Carly WX. The 'like' button was found a mile away, mangled beyond recognition in a tree. The 'subscribe' button was completely slabbed."

**Below the top 15, worth a look (rank by likes among top-level comments)**
- #39, 9 likes, @justjilly1966 (warm Palm Sunday memory): "Carly I grew up near Kokomo Indiana but wasn’t born until 1966.  My mother was on the north side and would always share her story through the years whenever it was too warm outside on Palm Sunday or Easter.  My uncle Richard Gore was a newlywed and lived in Russiaville. They were closing on the house in a week so were not moved in yet. Houses on both sides were gone and their home was heavily damaged.  Thank you for sharing this story. I sent it to my 83 year old mom today after watching and she [...cut here, full comment is 525 characters]"
- #40, 9 likes, @jeremysaysrawr119 (asks for 1994 Palm Sunday): "I’d love to see the 1994 Palm Sunday outbreak. The F2 that hit my neighborhood was during this outbreak and I feel like it’s forgotten."
- #58, 5 likes, @liamsmith728 (asks for 1984 Carolinas outbreak): "Can you do a vid on the 28 March 1984 Carolinas Outbreak?  Dr. Fujita studied it in great detail and likened the set up to 1925 I believe.  I lived through the F4 that hit.  Not a lot out there on that event that I can find. It was a rude welcome to the states for me a lad of 10 at the time."

---

## What all four already tell

All four were heard (Celton and Carly Anna from captions, Tornado Autopsy and the 1966 film from audio). Each line says which of the four.

- Palm Sunday, 11 April 1965 (all four: Celton 0:03 and 20:43, Carly Anna 3:08, Tornado Autopsy 0:00 and 1:06 "the start of Holy Week", film 0:01).
- The outbreak, with heavy loss of life and no agreed figure (Celton 266 at 20:04, Carly Anna "over 200" at 0:36 then Red Cross 258 at 19:17, Tornado Autopsy 271 or 258 at 21:19, film 139 in Indiana only at 12:49). The film covers Indiana only; the other three cover six states.
- A mild or warm Sunday that had people outdoors (all four: Celton 0:03 and 20:45, Carly Anna "balmy" 0:07 and 83 to 85 F at 3:52, Tornado Autopsy 1:06, film 2:21). Said as "first" warm day by three: Celton "the first warm day of the year" (20:45), Tornado Autopsy "the first really pleasant day of the year" (1:06), film "The first really warm day of spring" (2:21). Carly Anna does not say "first".
- Forecasts and warnings existed that day (all four: Celton 2:09 and 10:45, Carly Anna 6:02 and 9:52, Tornado Autopsy 3:25 to 4:51, film 1:33).
- The Dunlap area on the path (all four: Celton 9:12, Carly Anna 12:14, Tornado Autopsy 14:53, film 10:21). The Midway twin-funnel photograph in three (Celton 5:43, Carly Anna 13:23, Tornado Autopsy 0:00); the film does not mention it in the parts heard.
- Fujita's survey as the lasting result: three (Celton 21:10, Carly Anna 24:25, Tornado Autopsy 11:03); not the film.
- The difference between a forecast and a warning: two (Tornado Autopsy 5:15 to 5:59 and 22:44 to 23:25; film 16:30 "few, if any, people knew the meaning or the difference between the two terms"). Not Celton or Carly Anna.

## What none of them tells

Every line says which of the four was heard. All four were heard unless a gap is named.

- A warning followed hop by hop from the Bureau desk through police or civil defense to a station to a named listener: **none of the four.** The Bureau side is told by two (Tornado Autopsy 10:21 to 11:03, South Bend by telephone to Chicago radar operators and then asking stations to use the emergency signal; film 0:48 to 1:58, Kansas City to local offices to county outlines). No video follows a message past the Bureau.
- Police or civil defense holding a warning: **none of the four.** Tornado Autopsy has civil defense only as sirens that "meant war or nothing" (8:26 to 8:48). The film has police only as reporters to the Bureau (2:43), rescuers (4:31) and planners (21:41). Celton and Carly Anna have police only as photographer or reporter (Celton 5:00, Carly Anna 11:31).
- "I don't like to panic them" or "the information died with the police": **none of the four.** Nearest: Tornado Autopsy, Grand Rapids avoided the word at 5:20 because "The office thought the word would cause panic" (8:06); film, "Keep calm" (23:06).
- Warnings issued for storms already gone (Marion, Berne): **none of the four.** Nearest: Tornado Autopsy, Crystal Lake warning at 3:40 p.m., tornado lifts 3:42 p.m. (10:01), and the first tornadoes "about 15 minutes before forecast number 68 was even issued" (9:34).
- The 35 minutes before the county seat: **none of the four.** Gaps between paired storms are told by Tornado Autopsy ("about 35 minutes behind", 18:14; "30 to 40 minutes", 14:53) and by Celton ("30 minutes after the first", 15:42) without a county seat. The film's unrecognised stretch 2:43 to 4:07 could hold timings: cannot tell from the audio.
- Power and telephone lines failing as the reason a warning did not travel: **only Tornado Autopsy** (14:32 to 14:53 and 23:45). Film: lines down, but for rescue, not warnings (6:51). Celton: "because of the damage caused by the first tornado very few people received warning" (9:48), without naming lines. Carly Anna: not told.
- What a person at the last step received or did not: **none of the four.** The only on-the-ground versions are in the comments (church neighbour shouting "get to the basement", nursing students sent to a hospital basement, a mother in Greentown whose lights went out).
- An alarm at the announcer's desk, or any named recommendation about it: **none of the four.** Tornado Autopsy lists sirens, a national weather wire, radar and spotter networks (25:29 to 25:49).
- The 1966 Brouillette study: **none of the four.**
- A count of how many people a warning reached: **none of the four.** The film asks and gives up: "How many persons heard the tornado warnings and failed to protect themselves and were then killed? No one will ever know for sure." (24:34)

**Closest to our angle.** Tornado Autopsy for the premise and the downed lines (forecasts "excellent", warnings read on the air, "the first wave of tornadoes had torn down the phone lines and the power lines that the second wave's warnings needed to travel on"), though it blames the vocabulary. The 1966 film for the question itself ("Was there enough warning given?", 20:14) and for the confusion among "several different weather bureaus" (16:09). Neither says who held a warning.
