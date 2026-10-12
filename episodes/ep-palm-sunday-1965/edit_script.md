# ep-palm-sunday-1965 · edit_script.md (v4: fix pass 1 applied 12 Oct 26 to acts A1 to A6 and the close Z1, after three fact checks and grade 1; acts not locked; nothing locked beyond H1, T1, I1)

Lane: documentary (`/storm-episode`). Built on the angle the owner locked on 11 Oct 26 (`angle.md`) and the structure he signed off (`structure.md`). The hook's idea is Rebuild 2 of `hook-critique.md`, the owner's pick: the telephone list, the blank row, the family at the end. Facts from `research/facts.md` and the fact check of 12 Oct 26 (page images read); pictures from `research/picture-inventory.md`. Status: DRAFT; one check round, then the voice.

## A. Header
- **Title (owner, verbatim):** Who Stopped the Palm Sunday 1965 Tornado Warning?
- **Target runtime:** 20 to 25 min; planned at 22:00 (`structure.md`) until `word_budget.py` sizes it from a probe at the shipping tempo.
- **Claim (locked, copied):** On Palm Sunday 1965 the forecast did not fail and the warnings were sent. They stopped one desk short of the people.
- **Dominant question:** the viewer keeps watching to find out why police who heard of a tornado told nobody, and whose job it was to tell the family at the end of the list.
- **Architecture:** a detective story on a clock. One message is followed from office to office; each act moves the clock on.
- **Scope held in every act:** the 1966 study covers Indiana only and hides its counties ("County A", "County B"). No county, town or department is named on air as the one. County A (rows C1, C2) and County B (rows A13, C5, C6, C7) are never joined in one sentence. What County A's police heard was a State Police report of a tornado at 5:50 PM, not a Weather Bureau warning. In County B the narration says "where the tornado was", never "tornado warning".

## Section ID map
`tts_episode.parse_segments` IDs must match `[A-Z]\d+-S\d+`.
| Section | ID prefix |
|---|---|
| Hook (Paul on camera) | H1 |
| Hook tail | T1 |
| Intro, the living room and the list | I1 |
| Acts one to six | A1..A6 |
| Book ad | (none: the `config.yaml channel.cta` file carries its own VO) |
| Close | Z1 |

## Writer notes
- The blockquote is the spoken line and nothing else: `parse_segments` voices every character in it. Row tags sit on the `Rows:` line under each segment, in sentence order, never inside the blockquote.
- Hook lines against Rebuild 2: H1-S1 is rewritten to the study's sentence (fact check, 12 Oct 26). The toll now comes straight after Paul (T1-S1). The 5:43 line says "issued a tornado warning"; the telephone is a general statement about South Bend's warnings. The list line, the announcer line and the question are word for word.
- H1-S1 alternative, not used: fails the check ("until it hit"). It read: "Police in one Indiana county heard a tornado reported and told nobody until it hit. South Bend's warning went to offices and stations, not homes."
- Narration numbers follow the El Reno copy: spelled out, no hyphen ("five forty three", "nineteen sixty five"). The claim in I1-S9 is the locked wording with its year spelled for the voice.
- The claim carries "desk", a word the critique lists as unshowable. It is the locked wording, so it stays; a drawn desk appears on that word.
- T1-S3 is four name-only sentences, the telephone list read aloud. The quickref bans trailer fragments; this is the owner's picked line and stays as picked (orchestrator ruling, 12 Oct 26).
- Study pages shown on screen are the scan of the 1966 working paper. That scan is not a row of the picture inventory; its rights line has not been read.
- Drawings are used only where the inventory has nothing real: the house, the living room and its television set, the announcer's microphone, the desk.
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- Start times wait on the voice probe; none is estimated here.
- Fix pass 1, 12 Oct 26 (acts and close; the three fact checks and grade 1 applied):
  - Page numbers in the acts are the fact checkers' readings of the page images, not the numbers in `facts.md`.
  - Every Picture note in the acts opens with a kind tag (`[page]`, `[photo]`, `[film]`, `[graphic]`, `[map]`, `[drawing]`, `[Paul]`) so page-crop runs are counted by script. 8 of 118 segments are page crops; each changes inside its own segment.
  - Film: inventory A14 only, logged shots only, each used once (14-01, 03, 04, 06, 07, 08, 09, 10, 11, 12, 13), muted, framed 4:3, labelled "Civil defense training film, 1967". It stands for a kind of room.
  - Spoken handles for the study's two counties: "the first county" (A2-S9) and "a second county" (Paul, A4-S7). Chips on screen: "the first county" and "a different county".
  - Cut by ruling: row C4. Cut on the grade: the 4:40 and 5:05 entries, the 8:30 all clear, Indianapolis at 8:33, the wire speed, the weather radio counts, the three restatements at the end of Act 4, the exit questions of Acts 2 and 4, the spoken source caveat.
  - Kept against the grade's cut list so the script stays above 20:00, each reworded and given its own picture: the 2:00 forecast (A1-S9), the 7:00 and 7:45 station (A3-S12), the two police departments (A3-S15), the 7:33 partial all clear, now the hand east (A3-S16), "about a third" (A6-S9).
  - Added from `facts.md` and the fact-check files, none read on a page image for this pass: the IWX table tolls 10, 14 and 25 (A2-S8, A2-S17, A5-S9); "the poor observer" (A3-S8); the newspaper quote (A4-S19, OCR); "a few sirens, and the loudspeakers on police cars" (A4-S15); "several doors away" and the warning light (A6-S2, A6-S4); Curran asleep until about 10:30 (A5-S18). The photographs C6 and C5 sit in Act 5 only if the builder confirms the tornado's path.
  - Act 4 has no photograph: every free damage picture carries a place name that would point at a county the study hides.
  - The close: Z1-S4 has no date, so there is no dated forward window. Z1-S3's picture is our own drawing; no present-day photograph is sourced. The spoken book line is a note, not copy.
  - "The information died with the police" is voiced once (A4-S6); `flag_words.py` warns on it as a soft word.
  - Length: 20:06 predicted at `--target 21`, at the floor of the band. Nothing was added to fill; a further cut needs new sourced material to stay above 20:00.
---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one: the white shirt desk frame used in El Reno, not a thumbnail image. He speaks these two sentences in one clip and nothing else. Label "April 11, 1965 · one Indiana county" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> City police in one county heard troopers report a tornado and told nobody until one hit. Weather Bureau warnings went to offices and stations, not homes.

**Rows:** [C2, A7; study printed pp. 19 to 20, page image read: city police monitored the 5:50 PM State Police message; headquarters notified no one "until after the first tornado hit the county"] · [A6; study printed p. 14: the list holds offices and stations, no households]


## T1 · Hook tail (start time waits on the voice probe)

### T1-S1 · narration
**Picture:** hard cut on the first word to real photographs, never black: the damage pictures marked Free in the inventory, each with its place label: Sunnyside in Dunlap, Indiana (C2) and Alto, Indiana, from the air (C5). C7 stays out until its town is confirmed. The number "271" lands on "two hundred seventy one" and holds, with the label "lives lost across six states" so the count is not read as Indiana's. Source line under it, small: "National Weather Service · other counts run from 260 to 266". One bed swell, no siren.
> Two hundred seventy one people lost their lives that day.

**Rows:** [F] (said once; the attribution sits on screen, after the number)

### T1-S2 · narration
**Picture:** a Weather Bureau teletype room photograph (inventory A3, teletype operators at the Weather Bureau Communications Center, about 1955). A clock "5:43 PM" lands on "five forty three". The warning itself comes in as the survey report's own page, first line underlined: "Severe thunderstorm and tornado warning." (inventory B1, file `media/docs/survey-pdf-67-orig.png`). Place label "South Bend, Indiana". On the second sentence a telephone ring, made in house, and the clock label fades so the telephone is not pinned to 5:43.
> At five forty three, the Weather Bureau in South Bend issued a tornado warning. It also telephoned its warnings down a list.

**Rows:** [A6; survey printed p. 39] · [A6; study printed p. 14: South Bend "also telephoned several organizations", said of its warnings in general]

### T1-S3 · narration
**Picture:** the whole telephone list typed over the teletype room photograph, eight rows in the study's order: State Police, Sheriffs' Departments, City Police Departments, Indiana and Michigan Electric Company, Red Cross, Specified radio and TV stations, Flying services, Airlines. The four spoken rows tick as they are said. The other four stay grey and readable, so four never reads as the whole list. One soft key strike per tick.
> State Police. Sheriffs. City police. Named radio and television stations.

**Rows:** [A6; study printed p. 14] (four of the eight entries)

### T1-S4 · narration
**Picture:** the list scrolls past its eighth row to a ninth, which is blank, cursor blinking, no tick. Below the list, apart from it, a drawn announcer's microphone and then a drawn house, both dark. The microphone stands for any station; no named or quoted station is drawn as part of the South Bend list. Drawn because the inventory has no 1965 studio or home.
> A family got it from an announcer, if the announcer had it.

**Rows:** [C12] [C8] (the C8 station has no name and no county in the study)

### T1-S5 · narration (tempo 0.85)
**Picture:** one frame holding everything so far: the eight rows, the blank ninth row, the dark microphone, the dark house. Push in slowly on the blank row and hold it through the question.
> Whose job was it to tell the family at the end of the list?

**Rows:** (the question; no row)

*([loop L1 open]: whose job it was to tell the family. The closing act is set when the acts are written.)*

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The living room and the list (start time waits on the voice probe)

### I1-S1 · narration
**Picture:** the drawn house from T1-S4, now in afternoon sun, seen from the street. Date label "Palm Sunday · April 11, 1965". Move through the front window into the living room: a television set and a table radio, both idle, with no one at them. A drawing, because the inventory holds no picture of a home or a street that day.
> April eleventh, nineteen sixty five, was the first nice spring day of the year. Many people were not listening to the radio or watching television.

**Rows:** [C21; study printed p. 25] · [C21; study printed p. 25]

### I1-S2 · narration
**Picture:** our own map of Indiana, a soft ring around the South Bend area. Name card "Ron Przybylinski · age 11 · South Bend area · recalled in 2014". Then the drawn television set, switched on, showing a plain programme frame. On the second sentence a station card comes up on its screen, the local station passing on the Weather Bureau's word: "so many tornado reports that it was hard to keep track of them", small line "as recalled in 2014". Not a "WEATHER BUREAU" bulletin card. No frame of the real show; nothing real exists that we may use.
> In the South Bend area, an eleven year old was watching Lassie on the local station. The station carried word from the Weather Bureau that there were too many tornado reports to keep track of.

**Rows:** [E] · [E] (a 2014 recollection: the "South Bend Indiana area", "the local CBS station"; an age and no gender, so "an eleven year old")

### I1-S3 · narration
**Picture:** the drawn television screen flips from the station card back to the plain programme frame on "went back". Then a clear sky, no time of day shown. Over it the study's own page (printed p. 36, file `media/docs/study-pdf-38-orig.png`), one sentence underlined as it is spoken: "There was not a cloud in the sky." It is the study's own sentence, not a person's words. Source line "Disaster Research Center, 1966, p. 36".
> TV stations cut in with a warning, then went back to their shows. Some people looked outside, and there was not a cloud in the sky.

**Rows:** [C22; study printed p. 36] · [C22; study printed p. 36]

### I1-S4 · narration
**Picture:** the tornado track map of the day (inventory B7, courtesy Dr. Russell Schneider, SPC). Six state names light one by one: Iowa, Illinois, Wisconsin, Indiana, Michigan, Ohio. Then a clock "11:45 AM" over a teletype machine photograph (inventory A4), with the label "Forecasters · Kansas City". No free picture of the Kansas City forecast room exists (A7 is Ask). No document card here: whether the 11:45 AM forecast is among the four scans of inventory A9 was not checked, so the clock over the photograph carries it.
> Tornadoes crossed six states that day. By eleven forty five that morning, forecasters in Kansas City had a tornado forecast out on the teletype.

**Rows:** [IWX page, six states confirmed by the checker 11 Oct 26] · [A1]

### I1-S5 · narration
**Picture:** the eight-row telephone list from T1-S3 returns over the teletype room photograph (inventory A3). The "Specified radio and TV stations" row lights and a small red "ON AIR" lamp comes on beside it. No tick boxes; nothing else on the list moves.
> The stations on that list were the ones expected to pass the warning to the public.

**Rows:** [A6; study printed p. 9: interviewees "said it was the responsibility of radio and TV stations to pass on such information"]

### I1-S6 · narration
**Picture:** the study's own page (printed pp. 19-20, files `media/docs/study-pdf-21-orig.png` and `media/docs/study-pdf-22-orig.png`), one sentence underlined as it is spoken: "Police headquarters did not notify other members of their own organization nor any other organization until after the first tornado hit the county." Label "one Indiana county", the county of Paul's line.
> In one county, police headquarters did not tell their own officers until the first tornado hit.

**Rows:** [C2] (County A)

### I1-S7 · narration
**Picture:** the study's own page (printed p. 22, file `media/docs/study-pdf-24-orig.png`), label "a different county". The sheriff's sentence is underlined as the narrator speaks it: "We didn't have any warning at all". Source line "a county sheriff · Disaster Research Center, 1966". The narrator reads the words; no actor's voice.
> A sheriff in another county found out when the tornado was going over, and said, "We didn't have any warning at all."

**Rows:** [C6] (County B)

### I1-S8 · narration
**Picture:** the same page holds (printed p. 22, file `media/docs/study-pdf-24-orig.png`); the underline moves on to the sheriff's next sentence, "the television didn't even list here". Then cut to the drawn television set from I1-S2, its screen on the plain programme frame.
> The television, the sheriff said, did not even list that county in the danger area.

**Rows:** [C6] (County B; the sheriff's words are "as being in the danger area")

### I1-S9 · narration
**Picture:** [RS] [VE] the whole chain in one frame: Kansas City, South Bend, the eight-row list, the microphone, the house. Light runs from Kansas City to South Bend and onto the list, and stops on the list. The microphone and the house stay dark. On "desk" a drawn desk with a telephone on its hook appears at the place the light stopped. Hold through the second sentence.
> On Palm Sunday nineteen sixty five the forecast did not fail and the warnings were sent. They stopped one desk short of the people.

**Rows:** [claim, angle.md]

### I1-S10 · narration
**Picture:** the eight-row list one more time, over the teletype room photograph. The "City Police Departments" row is already marked. The other rows pulse one at a time. Hold on the list; the bed drops out on the last word.
> Were police the only ones who told nobody?

**Rows:** (the question, from "Questions worth keeping" in `hook-critique.md`; no row)

*([loop L2 open]: whether police were the only ones. First paid in Act 1 with the stations that never passed on the forecast, row C13.)*

*(blackout 0.7 s)*


## A1 · They saw it coming (11:45 AM to 5:43 PM; start time waits on the voice)

### A1-S1 · narration
**Picture:** [photo] the teletype machines photograph (inventory A4, true caption in the credit corner). The clock stamp from the intro returns as a glass card, "FORECASTERS · 11:45 AM EST · Kansas City". The drawn teletype icon of the chain lights amber, alone.
> A forecast in nineteen sixty five was one message, so follow that one message from the start. It starts in Kansas City at eleven forty five that morning, Eastern time.

**Rows:** [A1; study printed p. 6: "At 11:45 a.m. (EST)"] (said in I1-S4; the hand-on)

### A1-S2 · narration
**Picture:** [map] our own map of the Midwest. A band is drawn from northeastern Missouri up to north central Indiana as the words are said. On the second sentence a small source card comes in: "did not indicate any immediate tornado threat to any portion of Indiana", source line "Disaster Research Center, 1966, p. 6".
> It covered a strip from northeastern Missouri up to north central Indiana. A later study calls it general, with no immediate tornado threat to Indiana.

**Rows:** [A1; study printed p. 6] · [A1; study printed p. 6]

### A1-S3 · narration
**Picture:** [map] our Indiana map. Clock stamp "WEATHER BUREAU · 12:20 PM · South Bend, Indiana". Starke, Porter and Laporte counties light amber with their names. A paper card holds the survey's 12:20 entry (inventory B1, printed p. 37), "several tornadoes are expected" underlined on the second sentence.
> South Bend's Weather Bureau office sent it on anyway. Its version named three Indiana counties, and said several tornadoes were expected between one that afternoon and seven that evening.

**Rows:** [A1; survey printed p. 37: "several tornadoes are expected ... 1 PM to 7 PM EST"; "Starke and southern Porter and Laporte Counties"]

### A1-S4 · narration
**Picture:** [photo] the Weather Bureau's own map of a teletype circuit (inventory A1, the Service A teletypewriter system map slide, file `media/stills/a1-service-a-teletype.jpg`; true caption "Service A teletypewriter system, about 1960 · NOAA"). Slow push toward the Midwest. One amber pulse is drawn along a line of the map from Kansas City to northern Indiana.
> It moved by teletype, which was a telephone line with a typewriter on each end. What Kansas City typed, a machine in South Bend typed out.

**Rows:** [NWS Heritage, https://vlab.noaa.gov/web/nws-heritage/-/stop-shouting-the-forecast : "Teletypes, basically telephone lines connected to typewriters"]

### A1-S5 · narration
**Picture:** [graphic] two clocks side by side. Left, the clock stamp "an office · 11:45 AM EST", lit amber. Right, beside the drawn house, a clock face with no hands. Small source line "Disaster Research Center, 1966, p. 6 (footnote)". The empty clock face pulses once on "family".
> Every forecast time in the study is the time a Weather Bureau office got it. It isn't the time a family heard it, and that's the clock to watch.

**Rows:** [study printed p. 6, footnote: the SELS forecast times "refer to the time the forecast first entered the system via local Weather Bureaus, and not the time that the general public became aware of the threat"]

*([loop L5 open]: when a family heard the forecast. Paid in A1-S16 and A1-S17.)*

### A1-S6 · narration
**Picture:** [map] our own map of the United States: a low is drawn over the northern plains, a large "L" with one warm front and one cold front, and wind arrows turning around it. In a card at its own size, the Weather Bureau's Daily Weather Map for Sunday, April 11, 1965 (inventory B5, file `media/stills/b5-surface-map-1965-04-11.png`). The later replots (B3, B4) are not shown.
> What the forecasters had on their morning map was one powerful storm system, a low, turning over the northern plains.

**Rows:** [H; IWX: "A powerful mid-latitude cyclone"; NWS Louisville, https://weather.gov/lmk/basic-fronts ; the fact check read the large "L" over the northern plains at 7 AM EST]

### A1-S7 · narration
**Picture:** [photo] the tornado track map (inventory B7, "Courtesy: Dr. Russell Schneider, SPC"). The tracks light from west to east. Label on glass: "supercell: a thunderstorm that rotates", then "single storms lasted up to 4.5 hours". No timer is tied to any one track. On the second sentence one arrow is drawn east northeast with the chip "about 45 mph".
> The storms it set off were supercells, thunderstorms that rotate, and single storms lasted up to four and a half hours. South Bend's own messages had them moving east northeast at about forty five miles an hour.

**Rows:** [H; IWX: "individual storms persisted for up to 4.5 hours"; NWS glossary, https://forecast.weather.gov/glossary.php?word=supercell] · [survey printed pp. 38 and 39: "moving east northeast about 45 mph"]

### A1-S8 · narration
**Picture:** [graphic] the same track map dims; county lines come up under one track and each county it crosses blinks in turn. Between each pair of counties a small hand-off mark is drawn, a dotted link like the chain's. On the second sentence the marks turn Label grey and three of them drop out.
> A storm that lasts that long crosses county after county, so its warning has to be handed on each time. That day, following a tornado from county to county was neither planned ahead nor systematic.

**Rows:** [H] (the writer's reading) · [study printed p. 21: "neither pre-planned nor systematic"]

### A1-S9 · narration
**Picture:** [graphic] clock stamp "FORECASTERS · 2:00 PM EST · Kansas City". The real forecast scan in a card at its own size (inventory A9, Forecast 68, file `media/stills/a9-sels-forecast-68.png`), with a large quote strip lifted beside it: "ONE OR TWO TORNADOES". On our map the three states fill in turn. Indiana stays unlit.
> At two that afternoon a second forecast went out, for parts of Wisconsin, Iowa and Illinois, with the words "one or two tornadoes."

**Rows:** [A2; study printed p. 6: Forecast 68, "ISSUED 1:00 P.M. CST (2:00 EST)"]

### A1-S10 · narration
**Picture:** [graphic] [RS] [VE] clock stamp "FORECASTERS · 5:20 PM EST · Kansas City". The forecast scan in a card at its own size (inventory A9, Forecast 69, file `media/stills/a9-sels-forecast-69.png`). Two quote strips lift out of it in turn: "PORTIONS OF NORTHERN INDIANA", then "A TORNADO OR TWO". On our Indiana map the northern half fills amber.
> Then at five twenty came Severe Weather Forecast Number Sixty Nine. It named parts of northern Indiana, and it used the words "a tornado or two."

**Rows:** [A5; study printed p. 7; the scan reads "ISSUED 4:20 P.M. CST (5:20 EST)"]

### A1-S11 · narration
**Picture:** [map] the same Indiana map. Clock stamp 5:30 PM, South Bend. Seven counties light one by one with their names: Porter, Laporte, St. Joseph, Elkhart, Starke, Marshall, Kosciusko. Small source line "Weather Bureau survey, 1965, p. 38".
> It covered most of the northern half of the state. South Bend passed it on ten minutes later and named seven counties.

**Rows:** [A5; study printed p. 7] · [A5; survey printed p. 38]

### A1-S12 · narration
**Picture:** [map] the same map. A dot for Fort Wayne comes up in the east with a drawn teletype icon beside it, lines at rest, unlit. A small paper card: "but not the one at 5:20 p.m.", source line "Disaster Research Center, 1966, p. 10". Push in on the unlit icon.
> The Weather Bureau office in Fort Wayne didn't pass this one on. Remember Fort Wayne.

**Rows:** [A5; study printed p. 10] (paid in A5-S1)

### A1-S13 · narration
**Picture:** [graphic] the chain from the intro: the Kansas City teletype and the South Bend telephone both lit, a small tick drawn over each. A paper card: "gave adequate forewarning", source line "Disaster Research Center, 1966, pp. 9-10". Everything after the list stays unlit.
> Those two afternoon forecasts, the study found, gave the local Weather Bureau offices adequate forewarning.

**Rows:** [study printed pp. 9-10: "at 2:00 and 5:20 p.m. SELS gave adequate forewarning to the local WS's"]

### A1-S14 · Paul on camera, one clip
**Picture:** [Paul] Paul on camera, full frame, the white shirt desk frame. One clip, these words and nothing else.
> At five twenty, no tornado had touched Indiana, and the forecast was already out. Getting it from an office into a house was somebody else's job.

**Rows:** [A5; study printed p. 7] · [IWX table: first Indiana tornado 5:45 PM EST; study printed p. 14: about 6:00 PM] · [A6; study printed p. 9: said of the forecast, "the responsibility of radio and TV stations"]

### A1-S15 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-03, 0:57.8 to 1:03.6: a room of men and women at a long table, a wall board), muted, in a framed 4:3 window with the label "Civil defense training film, 1967". It stands for a kind of room, not an Indiana office. On the second sentence the window dims and one word lifts onto a quote strip: "inaction", source line "Disaster Research Center, 1966, pp. 8-9".
> The Weather Bureau, the State Police and most sheriffs passed the forecast along as routine. Many of the other offices that heard it did nothing more, and the researchers' word for that is inaction.

**Rows:** [C20; study printed pp. 8-9: "rather routinely disseminated"; "it was that of inaction insofar as further dissemination and transmission of the tornado forecasts was concerned"]

### A1-S16 · narration
**Picture:** [film] the same film (shot 14-09, 6:23.9 to 6:49.6: a man in glasses reads from a sheet into a studio microphone), muted, framed, same label. It stands for an announcer, not a named station. On the last sentence the window empties to the drawn microphone alone, its ON AIR lamp off, and a paper card: "(A few stations never passed on the forecast)", source line "p. 10".
> That left the radio and TV stations, on Palm Sunday weekend. Most were short of staff, so the forecast often went out late. A few stations never passed it on at all.

**Rows:** [C13; study printed p. 10]

*([loop L2, first payment]: police were not the only ones; a few stations never passed on the forecast. Closes in A4-S16.)*

### A1-S17 · narration
**Picture:** [drawing] the drawn microphone, its ON AIR lamp red. A dotted link runs to the drawn house, and one window turns amber. On the second sentence two paper strips sit side by side: "A TORNADO OR TWO · half a state" and "should be on the alert · three counties".
> Many stations did get it on the air well ahead of the first tornado. But a forecast covered half a state for hours, and a warning named counties and told people to be on the alert.

**Rows:** [C13; study printed p. 10: "many stations broadcast the forecast sufficiently in advance of the first tornado"] · [A5; A6: the two texts, study printed p. 7 and survey printed p. 39]

*([loop L5 closes]: a family heard the forecast late, on time or never, depending on its station.)*

### A1-S18 · narration
**Picture:** [photo] the teletype room photograph (inventory A3, true caption). Clock stamp "WEATHER BUREAU · 5:43 PM · South Bend, Indiana", as in the hook tail. The eight-row list slides in beside it, all rows plain.
> At five forty three, South Bend issued a warning of its own. Now there was one message, with one telephone list to cross.

**Rows:** [A6; survey printed p. 39; study printed p. 13: "The first actual tornado warning for parts of northern Indiana was issued by the South Bend Weather Bureau at 5:43 p.m."]

### A1-S19 · narration
**Picture:** [graphic] hold on the list and the clock. The minute hand starts to move.
> How long does a warning take to cross that list?

**Rows:** (the act's exit question; no row)

*([loop L6 open]: how long a warning took to cross the list. Paid in A2-S5, closes in A2-S15.)*

*(blackout 0.7 s)*


## A2 · One message, one telephone list (5:43 to 6:46 PM)

### A2-S1 · narration
**Picture:** [map] our Indiana map. Drawn echo blobs come up near Michigan City and just west of Knox. LaPorte, Starke and Marshall counties light. The survey's 5:43 entry sits in a paper card (file `media/docs/survey-p39-warning-crop.png`, printed p. 39), "should be on the alert" underlined on the second sentence.
> The warning said radar showed strong storm echoes near Michigan City and just west of Knox. It told people in three counties to be on the alert.

**Rows:** [A6; survey printed p. 39]

### A2-S2 · narration
**Picture:** [map] the same map pulls back. Drawn radar rings sit at Chicago, Fort Wayne and Indianapolis. South Bend is a dot with no ring. A drawn telephone line runs from Chicago to South Bend. Small source line "Disaster Research Center, 1966, p. 13 · National Weather Service, Northern Indiana".
> But South Bend had no radar. Its radar news came over the telephone, from operators at other Weather Bureau offices.

**Rows:** [H; study printed p. 13] · [H; IWX: "relying on phone conversations with radar operators in Chicago"]

### A2-S3 · narration
**Picture:** [graphic] [VE] the chain graphic. A new station is drawn in front of South Bend: a drawn radar scope (a circle and one sweep line), joined to South Bend's telephone by a solid link. The chain is one link longer than it was in the intro.
> So the office that started the telephone list was already at the far end of somebody else's telephone line.

**Rows:** [H] (the writer's reading of the two rows above)

### A2-S4 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-13, 11:41.5 to 11:57.3: women in headsets on telephones), muted, in the framed 4:3 window with the label "Civil defense training film, 1967". It stands for telephone operators of the time, not a South Bend room. Then the eight-row list beside the window.
> From there its warnings went out twice, once by teletype and once by telephone, office after office.

**Rows:** [A6; study printed p. 14, said of the warnings in general]

### A2-S5 · narration
**Picture:** [graphic] [RS] [VE] the chain of desks with its running clock. An amber arc grows on the clock from the 5:43 mark, labelled "at least 10 minutes", while the light crawls from the list toward the microphone. Small source line "Disaster Research Center, 1966, p. 14".
> And between a warning being issued and radio or TV putting it on the air, the delay was generally at least ten minutes.

**Rows:** [A6; study printed p. 14]

*([loop L6, first payment]: at least ten minutes.)*

### A2-S6 · narration
**Picture:** [graphic] two glass cards, each with a clock face and its own source line. Left: "5:45 PM · Starke County", source "National Weather Service, Northern Indiana". Right: "about 6:00 PM · Marshall County", source "Disaster Research Center, 1966, p. 14". Each lands on its own sentence. They are not merged into one figure.
> The Weather Service has the first Indiana tornado on the ground at five forty five, in Starke County. The nineteen sixty six study has the first touchdown at about six o'clock, in Marshall County.

**Rows:** [B table; IWX: "two minutes before the Koontz Lake tornado touched down"; table 2245 UTC = 5:45 PM EST] · [study printed p. 14: "approximately seventeen minutes before the first tornado touched down at Lapaz"; 5:43 plus 17 by the checker's script]

### A2-S7 · narration
**Picture:** [graphic] under both cards the amber bar "at least 10 minutes" is laid against each: it covers all of the left card's two minutes and most of the right card's seventeen.
> A ten minute delay eats all of a two minute head start, and most of a seventeen minute one.

**Rows:** [A6, F] (ten against two and against seventeen; recomputed by the fact check)

### A2-S8 · narration
**Picture:** [photo] the tornado track map (inventory B7); the first Indiana track lights from Starke County to just south of South Bend. On the second sentence the toll on glass, "10 lives lost · this tornado", source line "National Weather Service".
> That first tornado ran from Starke County to just south of South Bend. Ten people did not survive it.

**Rows:** [B table; IWX tornado table: "NE of Knox (Koontz Lake) to S of South Bend", 5:45 PM, 10]

### A2-S9 · narration
**Picture:** [graphic] clock stamp 5:50 PM. Label chip "the first county · not named in the study". A drawn telephone, handset off the hook, joined to the drawn teletype icon; light runs from the telephone to the teletype, the reverse of the list. On the second sentence the page from the intro comes in as a small card (file `media/docs/study-p20-police-crop.png`, printed pp. 19-20).
> At five fifty, State Police in one county saw a tornado and phoned the Weather Bureau. It's the county whose city police were listening, and told nobody until the first tornado hit. Call it the first county.

**Rows:** [A7; study printed p. 19] · [C2; study printed pp. 19-20] (County A; said in H1-S1 and I1-S6)

### A2-S10 · narration
**Picture:** [drawing] the drawn microphone, lamp dark, beside a strip of blank ground. Drawn tornado marks land on the ground one, two, three; the lamp turns red only after the third. Label chip "the first county".
> By the time stations put that report on the air, tornadoes were already touching down there.

**Rows:** [A7; study printed p. 19] (County A)

### A2-S11 · narration
**Picture:** [drawing] the drawn house at dusk, dark. A drawn clock beside its door reads "20 minutes after". A paper quote strip: "until twenty minutes after it hit", source line "Disaster Research Center, 1966, p. 20". No person is drawn.
> The first county's civil defense director found out when a local police officer came to the director's home. That was twenty minutes after the tornado hit.

**Rows:** [C1; study printed p. 20] (County A)

### A2-S12 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-06, 1:46.0 to 1:57.4: men at a table with telephones under wall maps), muted, framed, same label. It stands for a civil defense office of the time, not this county's. On the second sentence two words lift onto a quote strip: "too late", source line "p. 20".
> Civil defense there saw part of its job as the back up for radio and TV. Its plan started after the first tornado had already passed through.

**Rows:** [C3; study printed p. 20] (County A)

*([loop L2, second payment]: civil defense, part of the back up, was itself told late.)*

### A2-S13 · narration
**Picture:** [drawing] the drawn living room: the television's screen goes from the plain programme frame to idle in one hard cut, then the window light goes. Label chip "the first county".
> And when the tornadoes knocked out the power there, anyone listening on a plug in set was cut off.

**Rows:** [D, County A row; study printed p. 19] (County A)

### A2-S14 · narration
**Picture:** [map] our Indiana map. Clock stamp 6:00 PM, South Bend. St. Joseph, Marshall, Elkhart and Kosciusko counties light. The survey's 6:00 entry in a paper card (printed p. 39), "during the next 30 to 60 minutes" underlined. On the second sentence drawn tornado marks land inside the lit counties.
> At six o'clock South Bend warned four counties to take emergency precautions for the next thirty to sixty minutes. That was just about when the tornadoes first started touching down.

**Rows:** [A8; survey printed p. 39] · [A8; study printed p. 14]

### A2-S15 · narration
**Picture:** [page] the study's page (printed p. 24) as a crop, "15-30 minutes" underlined on the first sentence. On the second the words lift onto a quote strip, "too old ... to be truly worthwhile as a warning", attribution "media personnel · Disaster Research Center, 1966", and the drawn microphone comes in beside it.
> A broadcaster told the researchers tornado warnings were generally fifteen to thirty minutes old. They were too old, that broadcaster said, to be truly worthwhile as a warning.

**Rows:** [C14; study printed p. 24: "Media personnel typically commented as follows"]

*([loop L6 closes]: at least ten minutes to cross, and generally fifteen to thirty minutes old.)*

### A2-S16 · narration
**Picture:** [map] our map of northern Indiana: a dot for Elkhart, name card "Paul Huffman · photographer, The Elkhart Truth", small line "as told by the National Weather Service". On the second sentence a dot for Nappanee, a drawn tornado mark northwest of it and an arrow pointing northeast.
> In Elkhart, a newspaper photographer named Paul Huffman was sifting through the warnings when his editor told him to grab his camera. Before he left, the South Bend weather office told him a tornado was reported northwest of Nappanee, moving northeast.

**Rows:** [E, Huffman; IWX narrative, confirmed word for word by the fact check]

### A2-S17 · narration
**Picture:** [photo] [RS] [VE] the real photograph, full frame, slow push: Paul Huffman's twin funnels (inventory C1, the owner's "use it."). Clock chip "6:32 PM". Credit "Paul Huffman, The Elkhart Truth · April 11, 1965". Place label "Midway Trailer Court". On the third sentence the toll on glass, "14 lives lost · this tornado", source line "National Weather Service".
> At six thirty two he took this picture, two funnels side by side. The Weather Service calls it one of the most celebrated tornado pictures of all time. Fourteen people lost their lives in the tornado he photographed.

**Rows:** [inventory C1: 11 Apr 1965, 6:32 pm] · [IWX: "one of the most celebrated tornado pictures of all-time"] · [B table; IWX tornado table: "the Dunlap twin funnel, first Dunlap tornado", 14]

### A2-S18 · narration
**Picture:** [photo] the damage photograph (inventory C2, file `media/stills/c2-dunlap-sunnyside-damage.jpg`; 800 px wide, so inside a framed card, not full frame). Place label "Sunnyside · Dunlap, Indiana". Slow push.
> And this is the Sunnyside subdivision in Dunlap, after a tornado crossed it that evening.

**Rows:** [inventory C2: "Sunnyside subdivision in Dunlap, Indiana, following the F4 tornado of April 11, 1965"]

### A2-S19 · narration
**Picture:** [map] our map again. Three paper log cards land one by one on their times, "6:23 PM", "6:24 PM", "6:35 PM" (survey printed pp. 39-40), and Plymouth, Bremen and Goshen light in turn.
> South Bend kept typing as the sightings came in. In twelve minutes it reported a tornado west of Plymouth, one moving toward Bremen, and one three miles west of Goshen.

**Rows:** [A9; survey printed pp. 39-40] (twelve minutes is 6:23 to 6:35, the writer's subtraction)

### A2-S20 · narration
**Picture:** [graphic] the chain's front end: a drawn house, a drawn telephone with the handset off the hook, a police desk, a link to South Bend. Light runs toward the Weather Bureau, the wrong way down the chain.
> A warning could start anywhere. A person sees a tornado and calls the police, and the police pass it to the Weather Bureau.

**Rows:** [study printed p. 12: a warning "can enter the system at any point"; "An individual may sight a tornado, call the police, who in turn will relay the message to the WB"]

### A2-S21 · narration
**Picture:** [photo] the teletype room photograph (inventory A3, true caption). Clock stamp 6:50 PM, South Bend. The eight-row list over it with the blank ninth row and its cursor, as in the hook tail. On the second sentence a blank sheet of paper slides in where the next page will come.
> Whose job it was to tell a family is still open. And at six fifty, the South Bend desk typed a message no warning office wants to send.

**Rows:** (the question of T1-S5, restated) · [A10; survey printed p. 40]

*([loop L1 restated]. [loop L7 open]: what the six fifty message said. Paid in A3-S1.)*

*(blackout 0.7 s)*


## A3 · The wires (6:50 to 7:45 PM)

### A3-S1 · narration
**Picture:** [page] [RS] the survey's page (inventory B1, printed p. 40), the 6:50 entry as a document crop, underlined as spoken: "telephones being out in many areas", then "it is impossible to notify many people". Clock stamp 6:50 PM. The words lift onto a quote strip, attribution "Weather Bureau, South Bend · 6:50 PM".
> The six fifty message said telephones were out in many areas, and that it was impossible to notify many people.

**Rows:** [A10; survey printed p. 40]

*([loop L7 closes].)*

### A3-S2 · narration
**Picture:** [drawing] the drawn television from the intro, its screen on the station card with the recalled words and the small line "as recalled in 2014" (callback). Beside it a paper strip with the message's own words, "so numerous that it is impossible to keep track of them".
> It opened with almost the words an eleven year old remembered on television, tornado reports so numerous it was impossible to keep track.

**Rows:** [E, Przybylinski, 2014: "hard to keep track"; A10: "impossible to keep track"]

### A3-S3 · narration
**Picture:** [map] our Indiana map: the whole north central part fills amber at once; no town is named. Small source line "Weather Bureau survey, 1965, p. 40".
> And it widened the warning to the whole north central part of Indiana.

**Rows:** [A10; survey printed p. 40: "Warnings should therefore exist throughout the northern central portion of Indiana"]

### A3-S4 · narration
**Picture:** [graphic] [VE] the chain graphic. The solid links between South Bend and the list flicker, turn dotted, then go dark one at a time. The list and everything after it lose their light.
> A telephone list runs on telephone lines and electric power. The first tornadoes of the evening were taking both down ahead of the later ones.

**Rows:** [D; study printed p. 16: "knocked out numerous electric power and telephone lines"; study printed p. 25]

### A3-S5 · narration
**Picture:** [map] our map. Clock stamp 7:10 PM. The Bremen dot takes a red ring; a drawn tornado mark sits just west of it; the telephone link into the town is dark. A paper card: "Bremen cannot be contacted by phone.", source line "Weather Bureau survey, 1965, p. 41".
> At seven ten a tornado was just west of Bremen, moving toward it, and Bremen couldn't be reached by phone. South Bend asked radio and TV stations to use their emergency warning devices.

**Rows:** [A11; survey printed p. 41; study printed p. 17]

### A3-S6 · narration
**Picture:** [map] the same map. One dotted arc, a broadcast, reaches from the drawn microphone toward the town. On the second sentence a small plug and cord are drawn under the microphone and under the house.
> That left a broadcast as South Bend's way into the town, for anyone there who was listening. And listening took electricity.

**Rows:** [A11] (the writer's reading of the 7:10 message)

*([loop L8 open]: who could still listen. Paid in A3-S11 to A3-S13.)*

### A3-S7 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-10, 7:48.0 to 8:04.3: a man at a desk with a black rotary telephone writes a note, a second man takes over the phone), muted, framed, label "Civil defense training film, 1967". It stands for a busy desk telephone, not South Bend's. Clock chip 7:13 PM. On the second sentence a quote strip: "numerous poor joke calls and they tie up the lines", attribution "Weather Bureau, South Bend · 7:13 PM".
> Three minutes later the office was asking for help with its own phones. People should stop calling the Weather Bureau unless they had weather to report, because joke calls were tying up the lines.

**Rows:** [A12; survey printed p. 41]

### A3-S8 · narration
**Picture:** [photo] the teletype room photograph (inventory A3: two operators seen from behind at their machines; true caption in the credit corner), slow push. On the second sentence a quote strip: "the poor observer", attribution "National Weather Service, Northern Indiana".
> The Weather Service's own history has a name for the man typing those messages. It calls him "the poor observer."

**Rows:** [E, the South Bend observer; IWX]

### A3-S9 · narration
**Picture:** [film] the same film (shot 14-04, 1:03.7 to 1:13.7: a woman on a black telephone at a desk), muted, framed, same label. On the second sentence the window gives way to two drawn telephones with a busy mark between them.
> People who lost their power tried to phone for more information. So many were calling that they couldn't get through, and offices trying to reach each other hit the same jam.

**Rows:** [D; study printed p. 25] · [D; study printed p. 17]

### A3-S10 · narration
**Picture:** [graphic] [RS] [VE] the eight-row list, close; one row lights with the amber band, "Indiana and Michigan Electric Company". Then our graphic: fifty four small drawn steel towers in rows, falling one after another while a count runs to "54"; above them "11 breaks in major lines". Label "Indiana · reported by the Indiana and Michigan Electric Company". No map. Nothing of the study's footnote for this line is shown.
> One name on South Bend's list was a power company, Indiana and Michigan Electric. It reported eleven breaks in its major lines in Indiana, and fifty four steel towers down.

**Rows:** [A6; study printed p. 14] · [D; study printed p. 16]

### A3-S11 · narration
**Picture:** [drawing] the drawn microphone; its ON AIR lamp goes from red to dark, then blinks on and off. Label "a station". A quote strip on the second sentence: "broadcasting was on an intermittent basis", attribution "media personnel · Disaster Research Center, 1966".
> With the power went radio and TV, in many areas. One station told the researchers all power to its studio and transmitter was out, and it broadcast on and off from emergency power.

**Rows:** [D; study printed p. 16] · [D; study printed p. 24] (no time, no name and no county in the study)

### A3-S12 · narration
**Picture:** [graphic] two clock faces, 7:00 and 7:45, with an amber arc between them. Label "a station". Quote strip: "our immediate vicinity was not included until 7:00 p.m. and our transmitters were hit at 7:45", attribution "media personnel · Disaster Research Center, 1966".
> A station said its area wasn't named in the warnings until seven o'clock. Its transmitters were hit at seven forty five.

**Rows:** [C8; study printed p. 25] (the study does not say whether this is the station of A3-S11; no county given)

### A3-S13 · narration
**Picture:** [drawing] the drawn living room, evening: the window dark, the television screen idle. On the side table the drawn table radio alone keeps a small amber dial. Small source line "Disaster Research Center, 1966, p. 25".
> In many houses the sets went dark with the lights. Unless a family owned a battery powered transistor radio, it couldn't get any later warning.

**Rows:** [D; study printed p. 25]

*([loop L8 closes]: whoever had a battery radio.)*

### A3-S14 · narration
**Picture:** [drawing] the drawn television: the plain programme frame cuts to idle, then the window light goes. Name card "Kathy Selzer Miller · Fort Wayne", small line "a recollection published by the National Weather Service". No frame, title or name of the real show on screen.
> In Fort Wayne, Kathy Selzer Miller remembers watching Ed Sullivan, with Herman's Hermits on, when the TV signal was lost. Then the power went out, she remembers, for three days.

**Rows:** [E, families; IWX, read by the fact check: "the Ed Sullivan Show with the Herman's Hermits performing and the tv signal was lost"; "then the power went out for 3 days"]

### A3-S15 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-11, 11:27.8 to 11:36.4: a desk with a typewriter and a lamp, a seated man), muted, framed, same label. It stands for an office of the time. Small source line "Disaster Research Center, 1966, p. 29".
> Two city police departments had no good back up power either, and lost full communication for a time.

**Rows:** [D; study printed p. 29]

### A3-S16 · narration
**Picture:** [map] our Indiana map. Clock stamp 7:33 PM, South Bend. A line is drawn through Mishawaka, Walkerton and Culver, the Indiana part of the line the page gives; the ground west of it dims. On the second sentence one arrow points east from the line toward Fort Wayne's dot.
> At seven thirty three South Bend called a partial all clear for everything west of a line. The storms were moving east, toward Fort Wayne's side of the state.

**Rows:** [A14; survey printed p. 41] · [survey printed pp. 38-39: "moving east northeast about 45 mph"]

### A3-S17 · narration
**Picture:** [graphic] a road drawn as one line; a drawn tornado mark moves along it toward a drawn desk. Three ticks light in turn as they are said: "30 minutes out", "10", "1". On the second sentence the tornado mark passes the desk and a paper message card lands behind it.
> Where an office in a tornado's path did get an alert, it came one, ten or thirty minutes ahead. Later that night, some came after.

**Rows:** [C15; study printed p. 21] · [A22, C16]

*([loop L3 opens]: warnings that arrived after the tornado.)*

### A3-S18 · narration
**Picture:** [graphic] the chain graphic with its dark links. One new thing: a dotted amber arc, a radio, between two drawn desks. It is the only light on the screen.
> A warning could still move over the radios that police and civil defense used.

**Rows:** [A13; study printed p. 21: the civil defense director "radioed" the city police]

### A3-S19 · Paul on camera, one clip
**Picture:** [Paul] Paul on camera, full frame, the white shirt desk frame. One clip, these words and nothing else. Cut to the book ad on his last word.
> One county still had working radios. At about seven fifteen, its civil defense director learned where a tornado was. What did he do?

**Rows:** [A13; study printed p. 21] (County B; "where a tornado was", never "tornado warning")

*([loop cta-hinge open]: what he did with it. Paid by the first sentence of A4-S1.)*

*(book ad here: after A3-S19, Paul's tease, and before A4-S1, which pays it in its first three words. The ad file carries its own voice; no ad copy is written here. Where the chapter blackout sits around the ad follows DESIGN.md "CTA contract".)*


## A4 · The desk where it stopped (7:15 to 8:07 PM)

### A4-S1 · narration
**Picture:** [page] the study's page (printed p. 21) as a crop, "with his own eyes" underlined. Label chip "a different county". Beside the crop the clock stamp "about 7:15 PM", its minute hand sweeping a quarter turn to "about 7:30 PM".
> He waited fifteen minutes, until he saw the tornado, in the study's words, "with his own eyes."

**Rows:** [A13; study printed p. 21] (County B)

*([loop cta-hinge closes].)*

### A4-S2 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-07, 1:57.5 to 2:12.5: a man on a telephone at a desk, a second man leans in with a paper), muted, framed, label "Civil defense training film, 1967". It stands for word arriving at a desk, not for either county's office. Label chip "a different county".
> He'd heard about it one county over, where he was helping the sheriff recover a person lost in the water. State Police had told that sheriff a tornado was coming in from the west.

**Rows:** [A13; study printed p. 21]

### A4-S3 · narration
**Picture:** [graphic] the chain for this county comes up desk by desk: a civil defense desk, lit amber; then the police desk with its telephone, the microphone, the house, all in Label grey, unlit.
> He told his own civil defense members, and no other office in his own county.

**Rows:** [A13; study printed p. 21] (County B)

### A4-S4 · narration
**Picture:** [graphic] [VE] the same chain. A dotted amber radio arc is drawn from the civil defense desk to the police desk and the light crosses it. Clock stamp "about 7:30 PM".
> At about seven thirty he saw the tornado himself. He radioed the city police with its location and direction, and asked them to tell the radio station.

**Rows:** [A13, C5; study printed p. 21] (County B)

### A4-S5 · narration
**Picture:** [graphic] the same chain. A faint grey ghost of the light runs on ahead of the real one: police desk, microphone, house. It is drawn in Label grey, never amber.
> That was the path he counted on. Civil defense tells the police, the police tell the station, and the station tells everyone.

**Rows:** [A13; study printed p. 21] (the director's own request; the fact check's wording)

### A4-S6 · narration (tempo 0.85)
**Picture:** [page] [RS] [VE] the study's page (printed p. 22) as a crop, one sentence underlined in red as it is spoken: "The information died with the police." Source line "Disaster Research Center, 1966, p. 22". Beside it the chain: the grey ghost fades, the light stays on the police desk and a red stop mark lands on it. Hold.
> It didn't happen. "The information died with the police."

**Rows:** [C5; study printed p. 22] (County B; the study's own sentence, voiced once)

*([loop L1, first answer]: where it stopped and who was holding it.)*

### A4-S7 · Paul on camera, one clip
**Picture:** [Paul] Paul on camera, full frame, the white shirt desk frame. One clip, these words and nothing else. On-screen label chip for the whole clip: "a different county".
> This is a second county and a second police desk. They had the tornado's location and a working radio, and apparently told no other office.

**Rows:** [C5; study printed p. 22: "the police apparently did not notify the local radio station nor any other organization within the county"] (County B)

### A4-S8 · narration
**Picture:** [page] the study's page (printed p. 22), the chief's words underlined: "I don't like to panic them." On the second sentence they lift onto a quote strip in Georgia, attribution "a city police chief · Disaster Research Center, 1966". On the third the underline moves to "might panic unnecessarily". Label chip "a different county". The narrator reads the words; no actor's voice.
> Their chief told the researchers why. He said, "I don't like to panic them." He was afraid people might panic for nothing if they heard it straight from the police.

**Rows:** [C5; study printed p. 22] · [I, item 4; study printed p. 22]

### A4-S9 · narration
**Picture:** [graphic] the eight-row list, close. Light sits on the "City Police Departments" row, then jumps to the "Specified radio and TV stations" row and stays there. Quote strip: "usually the radio has the information even before we get it", attribution "a police chief, asked about the forecast · Disaster Research Center, 1966, p. 9". No county label.
> About the forecast earlier that day, a police chief said it was never their primary duty to inform the public. The radio, that chief said, usually had the information before they did.

**Rows:** [C10; study printed p. 9: asked about "alerting the public to the fact that tornadoes could develop"; the study does not tie this chief to a county]

### A4-S10 · narration
**Picture:** [graphic] the list holds. Three rows pulse in turn, "Sheriffs' Departments", "City Police Departments", and a civil defense mark drawn beside the sheet, and each sends its light to the stations row.
> The researchers wrote that this chief summed up the feeling in sheriffs' offices, city police departments and civil defense units.

**Rows:** [C10; study printed p. 9: "summed up succinctly the feeling of other respondents in sheriffs' offices, city police departments and CD units"]

### A4-S11 · narration
**Picture:** [graphic] the list holds. Every row but "Specified radio and TV stations" fades to grey ink. Quote strip: "only an indirect role in alerting the public", source line "Disaster Research Center, 1966, p. 9".
> Asked what their part was in alerting the public, those offices typically said it was only an indirect one.

**Rows:** [study printed p. 9: "typically replied that they had only an indirect role in alerting the public"]

### A4-S12 · narration
**Picture:** [graphic] [RS] [VE] back to the second county's chain, held on the police desk with its red stop mark. Beside it the clock stamp runs from "about 7:30 PM" to "8:07 PM", an amber arc growing with the label "the study says: about 35 minutes". The microphone and the house stay dark. Label chip "a different county".
> So the call to the radio station apparently never came, and the clock ran. The tornado hit the county seat at eight oh seven, about thirty five minutes after he first radioed the police.

**Rows:** [C5] · [C7; study printed p. 22] (County B)

### A4-S13 · narration
**Picture:** [graphic] the same chain; every light on it goes out, the police desk last. On the first sentence the sheriff's words from the intro return as a small quote strip (file `media/docs/study-p22-sheriff-crop.png`, printed p. 22). Label chip "a different county".
> The county's sheriff learned of it when it was going over. "We didn't have any warning at all," the sheriff said. As it went through, power to the stations and the public was cut, and city police communication was out for about an hour.

**Rows:** [C6; study printed p. 22] · [D, County B row; study printed p. 22]

### A4-S14 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-12, 11:36.5 to 11:41.4: a man close at a studio microphone, reading a sheet), muted, framed, same label. Label chip "a station · county not given in the study". On the second sentence a quote strip: "were not notified by the local police so we couldn't prepare our listeners", attribution "media personnel · Disaster Research Center, 1966, p. 25".
> A station said later that local police had been told a tornado was headed its way. "We were not notified by the local police," it said, "so we couldn't prepare our listeners."

**Rows:** [C8; study printed p. 25] (not tied to County B: county-key.md)

### A4-S15 · narration
**Picture:** [graphic] the chain's far end: the microphone and the house, with one link between them. Two other ways to the house are drawn in dotted Label grey: a horn on a pole, a police car. On the second sentence each blinks amber once and goes back to grey.
> There was little or no attempt to warn people any other way than radio and TV. The exceptions were a few sirens, and the loudspeakers on police cars.

**Rows:** [study printed p. 35: "little or no attempt by the system ... to use mechanisms other than radio and TV warnings"] · [study printed p. 33, from the fact check's note "a few sirens, police car speakers"; the line is read on the page image before the voice]

### A4-S16 · narration
**Picture:** [graphic] the eight-row list, close. Quote strip over it: "No member of any organization interviewed saw it as their responsibility", attribution "said of the forecast · Disaster Research Center, 1966, p. 9". The stations row is lit; every other row is plain.
> Police weren't the only ones. Earlier, when the forecast went out, no member of any office interviewed saw it as their job to back up radio or TV.

**Rows:** [C9; study printed p. 9: "in response to a tornado forecast"]

*([loop L2 closes]: police were not the only ones.)*

### A4-S17 · narration
**Picture:** [graphic] [VE] eight plain squares in a row, no names. Seven fill amber on "seven"; the eighth takes a red outline on "one". Small source line "Disaster Research Center, 1966, p. 15". This frame never shares the screen with the sheriff's words.
> Seven of the eight counties in the study were in a Weather Bureau advisory before a tornado touched down there. Only one got no notice ahead of time.

**Rows:** [C19; study printed p. 15]

### A4-S18 · narration
**Picture:** [graphic] [RS] the whole chain in one frame, as in I1-S9: Kansas City, South Bend and the list lit; the desk with its red stop mark; the microphone and house dark. On the second sentence a quote strip: "the system tended to break down on the receiving end", source line "Disaster Research Center, 1966, p. 34".
> In most cases the Weather Bureau sent the warning, and it broke down on the receiving end. Key offices and the public often got it late, or not at all.

**Rows:** [C11; study printed p. 34: "Crucial organizations and the general public often did not receive the warnings in time or at all"]

### A4-S19 · narration
**Picture:** [graphic] the whole chain dims behind one large quote strip in Georgia, two lines landing one after the other: "In general, the alert seemed adequate." then "But specifically it appeared non-existent." Attribution "an Indiana newspaper, April 15, 1965 · quoted in Disaster Research Center, 1966". The paper's name stays off screen: it names a county.
> That week an Indiana newspaper wrote, "In general, the alert seemed adequate. But specifically it appeared non-existent."

**Rows:** [study footnote 16, printed p. 36 per county-key.md, read there as OCR; the quote is read on the page image before the voice]

### A4-S20 · narration
**Picture:** [map] our Indiana map. The South Bend dot dims; a dot for Fort Wayne lights to the east with the drawn teletype icon beside it, a paper strip coming out of it. Hold on the strip.
> And one office to the east, the Fort Wayne Weather Bureau was still typing warnings for storms that had already gone by.

**Rows:** [A20, A22, C16; survey printed pp. 43, 45]

*([loop L3 open]: why warnings kept going out for storms that had already passed. Closes in A5-S12.)*

*(blackout 0.7 s)*


## A5 · Warnings for storms already gone (7:40 to 10:30 PM)

### A5-S1 · narration
**Picture:** [map] our Indiana map: Fort Wayne's dot with the unlit teletype icon of A1-S12 beside it. On the second sentence a drawn radar ring comes up around Fort Wayne; South Bend's dot has none. Label chip "Weather Bureau · Fort Wayne".
> Fort Wayne is the office that didn't pass on the five twenty forecast. It had something South Bend didn't have, a radar of its own.

**Rows:** [A5; study printed p. 10] · [A20; survey printed p. 43: "The Weather Bureau radar at Baer Field"]

### A5-S2 · narration
**Picture:** [drawing] name card "John Curran · observer, Fort Wayne Weather Bureau, 1965", small line "his recollection, published by the National Weather Service". Then a drawn radar scope, large: a circle, one sweep line, a bright smear that fades behind the line. No map lines on it. Drawn because no 1965 radar scope picture exists (inventory D9).
> A man who worked there, John Curran, remembers it as a set built in World War Two to spot aircraft. Its small scope had no map on it, and the picture faded fast.

**Rows:** [H, Curran; IWX personal stories: "built in WWII for the purpose of detecting aircraft"; "a rapid decay rate with no map background"]

### A5-S3 · narration
**Picture:** [graphic] clock stamp "WEATHER BUREAU · 8:40 PM · Fort Wayne, Indiana". On the drawn scope a small hook shape appears west of a dot labelled Berne. On the second sentence the survey's 8:40 entry comes in as a paper card (inventory B1, printed p. 43), "for the next 30 to 60 minutes" underlined.
> At eight forty that scope showed a strong hook shape about five miles west of the town of Berne, moving east. Fort Wayne told Berne to take immediate precautions for the next thirty to sixty minutes.

**Rows:** [A20; survey printed p. 43: "a strong hook echo about 5 miles west of Berne Indiana and moving eastward"]

### A5-S4 · narration
**Picture:** [map] our map of the Indiana and Ohio line, drawn from true positions: Linn Grove, Berne, the state line. A drawn tornado mark sits at Linn Grove with the chip "8:40 PM" and moves to the state line, chip "near 8:52 PM". Label chip "John Curran's recollection" under the first sentence only. Source line "Weather Bureau survey, 1965, pp. 43 and 45".
> Curran recalls the man in charge, Clyde Downes, issuing it straight off the radar. The Bureau's own survey has that tornado over Linn Grove at eight forty, and across the Ohio line near eight fifty two.

**Rows:** [E, Downes; Curran in IWX; survey printed p. 45 for the name] · [A20; survey printed p. 45]

### A5-S5 · narration
**Picture:** [map] [RS] [VE] the same map. A long amber bar, "warning: the next 30 to 60 minutes", is laid over it and runs far past the state line; under it a short red bar, "12 minutes", stops at the line.
> A warning for the next hour was covering a tornado with about twelve minutes left in Indiana.

**Rows:** [A20] (8:40 to near 8:52, twelve minutes by the fact check's script)

### A5-S6 · narration
**Picture:** [photo] a Weather Bureau teletype room (inventory A5, file `media/stills/a5-teletype-room-1947.jpg`, true caption "Teletypes and operator, about 1947 · NOAA"). Clock stamp 9:00 PM, Fort Wayne. The line lifts onto a quote strip as it is said: "Hold the line a minute for a definite report on tornado at Berne.", attribution "Weather Bureau, Fort Wayne · 9:00 PM".
> At nine o'clock Fort Wayne typed, "Hold the line a minute for a definite report on tornado at Berne." It had hit, the office said, ten to fifteen minutes ago. Several houses were gone, it typed, and ambulances were rushing to the scene.

**Rows:** [A21; survey printed p. 43: "several houses destroyed and ambulances are rushing to scene"]

### A5-S7 · narration
**Picture:** [photo] [RS] the real photograph of a tornado that evening (inventory C6, true caption "Tornado near Alto, moving toward Kokomo · April 11, 1965 · Kokomo Morning Times"), full frame, slow push. The builder confirms on the IWX table row "Russiaville to SE of Marion and Greentown" that this is the tornado that went on to Marion before it sits under this line; if not, the aerial of Alto (C5) with its label. On the second sentence, clock chip 9:20 PM and a dot for Marion on a small inset of our map.
> That same storm had already been through Marion. At nine twenty Fort Wayne put it on the wire: three tornadoes had struck the city, with extensive damage.

**Rows:** [survey printed p. 45: one path, out of Howard County at 7:50, near Marion near 8, Linn Grove at 8:40] · [A22; survey printed p. 43]

### A5-S8 · narration
**Picture:** [graphic] [RS] [VE] two clocks side by side. Left, a drawn wall clock stopped at 8:10, label "a hospital clock, Marion · Weather Bureau survey, p. 45". Right, the clock stamp at 9:20 PM, Fort Wayne. On the second sentence a quote strip between them: "a full hour and twenty minutes earlier", attribution "National Weather Service, Northern Indiana".
> Marion was hit near eight o'clock. Fort Wayne's message went out a full hour and twenty minutes later. A clock in a Marion hospital had stopped at eight ten.

**Rows:** [A22; survey printed p. 45] · [C16; IWX, read by the fact check] · [survey printed p. 45: "The clock at the hospital stopped at 8:10 PM."]

*([loop L3, first payment]: how late.)*

### A5-S9 · narration
**Picture:** [photo] the damage photograph from the air (inventory C5, file `media/stills/c5-alto-aerial-damage.jpg`, place label "Alto, Indiana"), slow push; the builder confirms Alto is on this tornado's path (IWX table row below) before it sits here, else the track map with this track lit. Toll on glass: "25 lives lost along this tornado's path", source line "National Weather Service".
> The Weather Service counts twenty five lives lost along that tornado's path, from Russiaville to Marion.

**Rows:** [B table; IWX tornado table: "Russiaville to SE of Marion and Greentown", 25]

### A5-S10 · narration
**Picture:** [map] our map: Wells, Adams, Blackford and Jay counties light amber with their names and the chip "9:20 PM · on alert". On the second sentence the tornado's track is drawn across Blackford, Wells and Adams to the state line with the chip "8:52 PM · already in Ohio".
> With that message Fort Wayne put four counties on alert for a storm moving east. The tornado had already crossed three of them and left Indiana.

**Rows:** [A22; survey printed p. 43: "under alert for eastward movement"] · [survey printed p. 45: across Blackford, Wells and Adams, into Ohio near 8:52]

### A5-S11 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-08, 4:19.5 to 4:24.3: a man talking on a black telephone), muted, framed, label "Civil defense training film, 1967". It stands for a telephone call, not Fort Wayne's. Clock chip 9:07 PM on the second sentence.
> The reason was a phone call. Word from Marion reached Fort Wayne's signal department at nine oh seven, about an hour after the tornadoes hit.

**Rows:** [A22; survey printed p. 43: "reported through the Fort Wayne signal department at 9.07 PM EST"] · [C16, Curran: "a tornado that had passed through an hour earlier"]

### A5-S12 · narration
**Picture:** [graphic] the chain's front end, as in A2-S20: a town, a drawn telephone, a dotted link to the Weather Bureau, and nothing drawn between. Quote strip: "primitive, mostly nonexistent", attribution "John Curran, on the trained spotter network".
> There was almost no trained spotter network. For Marion, the warning office was waiting on a telephone call, like everyone else.

**Rows:** [E, Curran: "The trained spotter network was primitive, mostly nonexistent."] · [C16; the fact check's wording]

*([loop L3 closes]: for Marion, the warning was late because the report it was built on came late. The Berne warning came off radar.)*

### A5-S13 · Paul on camera, one clip
**Picture:** [Paul] Paul on camera, full frame, the white shirt desk frame. One clip, these words and nothing else.
> The office warning those towns then lost its own power. For one hour that night, the Fort Wayne Weather Bureau sent out nothing at all.

**Rows:** [A23; survey printed p. 44]

### A5-S14 · narration (tempo 0.85)
**Picture:** [page] [RS] [VE] the survey's page (printed p. 44) as a crop, one line underlined in red: "No issuances between 9:30 PM EST and 10:30 PM EST due to power failure." The frame around the page dims almost to black while the line stays lit. Clock stamp 9:30 PM.
> "No issuances between nine thirty and ten thirty, due to power failure."

**Rows:** [A23; survey printed p. 44]

### A5-S15 · narration
**Picture:** [drawing] a row of three drawn houses at night, every window dark; behind them one drawn steel tower, leaning. Small line "John Curran's recollection, not a log". Nothing ties the towers to the office's own power.
> Curran remembers that the power company's high voltage lines were down, and none of its Fort Wayne customers had power.

**Rows:** [D, Curran; IWX personal stories, a recollection] (no source says the office was one of those customers)

### A5-S16 · narration
**Picture:** [photo] the track map (inventory B7), the Toledo track lit. Clock stamp "9:30 PM · Toledo, Ohio". Label chip "Toledo had its own Weather Bureau office". On the second sentence the toll on glass, "18 lives lost · northern Toledo", source line "National Weather Service". No line or arrow joins Toledo to Fort Wayne.
> At nine thirty that night, a tornado started in northern Toledo, Ohio, a city with its own Weather Bureau office. The Weather Service says it was never warned for, and eighteen people there lost their lives.

**Rows:** [B table: 9:30 PM, 18; IWX] · [survey table of contents: a Toledo log] · [C18; IWX narrative] (Ohio: IWX is the source, not the study; no cause claimed)

### A5-S17 · narration
**Picture:** [map] our map of Ohio: Toledo in the north, Columbus in the middle, a dotted teletype line between them. Chip "Columbus weather office · ten minutes before".
> Its only mention came from the Weather Bureau in Columbus, ten minutes before it struck.

**Rows:** [C18; IWX narrative]

### A5-S18 · narration
**Picture:** [drawing] the name card for John Curran again. A drawn wall clock at 4:00 PM, then the drawn house with a dark window, then the clock at 10:30 PM and the window lit.
> Curran had finished his shift at four that afternoon, with no severe weather anywhere in Fort Wayne's area. He slept until a roommate woke him, around ten thirty.

**Rows:** [E, Curran: "At the end of my shift no severe weather was in the Ft. Wayne County warning Area"; IWX, read by the fact check: asleep until a roommate woke him around 10:30 PM]

### A5-S19 · narration
**Picture:** [drawing] [VE] a drawn scene, because no picture of the office exists: a dark room, two drawn teletype icons lit amber, and one line, the extension cord, running along the floor, out of the door and down a hall to a box labelled "FAA Flight Service Station". No person is drawn.
> He was back at midnight. The teletype machines were running on an extension cord from the aviation office down the hall, strung by a technician named Arnie Koch.

**Rows:** [E, Curran; IWX: "the electronics technician Arnie Koch had strung an extension cord down the hall from the FAA Flight Service Station"]

### A5-S20 · narration
**Picture:** [page] date label "April 12, 1965". The survey report's memo page (inventory B1, PDF page 3), underlined: "The tornado survey team which you established on April 12, 1965". On the second sentence a tighter crop of printed p. 1, one word underlined: "excellent".
> The next day the Chief of the Weather Bureau named a team of five. Its job was to find out why so many lives were lost after forecasts called excellent.

**Rows:** [E, Kutschenreuter memo; survey PDF p. 3] · [survey printed p. 1: "a survey team of five Weather Bureau officials"; "excellent" forecasts]

### A5-S21 · narration
**Picture:** [graphic] the end of the chain: the eight-row list, the drawn announcer's microphone, dark, and the house. Hold on the microphone, not on the police desk.
> Did anyone fix the end of the list?

**Rows:** (the act's exit question; no row)

*([loop L4 open]: whether anyone fixed the end of the list, the announcer's desk. Paid in A6-S2 to A6-S4 and in the close.)*

*(blackout 0.7 s)*


## A6 · What they fixed, and what they didn't (April 12 to May 2, 1965, and the three months after)

### A6-S1 · narration
**Picture:** [page] the survey's recommendations page (inventory B1, printed p. 2), whole for a moment with the date label "May 2, 1965" and the name card "P. H. Kutschenreuter · chairman, Weather Bureau survey team" (on screen only, not spoken). Then a tight crop on recommendation 1.
> On May second, three weeks after the storms, the team made ten recommendations, and the first one reaches the announcer.

**Rows:** [G; survey printed p. 2; survey PDF p. 3: memo dated May 2, 1965; 11 April to 2 May is 21 days by the fact check's script]

### A6-S2 · narration
**Picture:** [graphic] [RS] [VE] a floor plan we draw: a teletype in one room, three doors, the announcer's booth with the drawn microphone at the far end. On the second sentence a bell mark is drawn on the teletype and a line runs from it through the doors to a lamp beside the microphone; the lamp lights amber. Small paper card with the page's own words: "positive alerting devices (remoted to the announcer's position where necessary)".
> The report describes weather teletypes sitting several doors away from the announcer. So it asked stations to put an alarm on the machine, one that goes off where the announcer sits.

**Rows:** [survey printed p. 4: "located several doors away from the announcer's position"; "such as an alarm indicator lamp or warning bell"] · [G, Rec. 1; survey printed p. 2]

### A6-S3 · narration
**Picture:** [graphic] the hook tail's frame returns: the eight rows, the blank ninth row, the microphone, the house. This time the microphone is lit; the house is still dark.
> A family got it from an announcer, if the announcer had it. The team's first recommendation was to make sure the announcer had it.

**Rows:** [C12; G, Rec. 1] (the first sentence is T1-S4, word for word; a recommendation, not a thing done)

*([loop L4, first payment]: the first recommendation reaches the announcer's desk.)*

### A6-S4 · narration
**Picture:** [drawing] the drawn microphone with the lamp beside it; the lamp goes back to an empty outline. Chip "three months later". On the second sentence four marks from earlier come up in a row, each dark: the police desk with its stop mark, the dotted telephone link, the unlit Fort Wayne dot, the telephone at Marion.
> Three months later, one station's warning light still hadn't been installed. And that was one desk, on an evening that broke in four more places.

**Rows:** [study printed p. 31: a station's warning light "had not yet been installed at the time of the DRC study"; study printed p. 28: "In the three months after Palm Sunday"]

*([loop L9 open]: the other four places. Paid in A6-S5 to A6-S8.)*

### A6-S5 · narration
**Picture:** [graphic] the chain: a solid link is drawn from the teletype icon straight to a drawn desk, twice, and both desks light. Small source line "Disaster Research Center, 1966, p. 29". The page itself is not shown: it prints the study's county letters.
> The police desk got a wire of its own in two towns. One police department and one fire department were hooked directly to the Weather Bureau teletype.

**Rows:** [G; study printed p. 29]

### A6-S6 · narration
**Picture:** [graphic] the dark telephone links of A3-S4 return; over them an amber radio arc is drawn from office to office. A small paper card: "back up emergency radio communications", source line "Weather Bureau survey, 1965, p. 2, recommendation 7".
> For the telephones that failed, the team asked for back up radio between Weather Bureau offices, and out to civil defense and local offices.

**Rows:** [G, Rec. 7; survey printed p. 2]

### A6-S7 · narration
**Picture:** [drawing] the dark office of A5-S19: the extension cord fades and a drawn generator mark takes its place; the room lights. On the second sentence our map: a radar ring is drawn around South Bend's dot. Small paper cards for recommendations 8 and 5.
> Fort Wayne's dark hour brought a call for emergency power at every Weather Bureau office. And any office leaning on another city's radar, as South Bend was, was to get a scope of its own.

**Rows:** [G, Rec. 8; survey printed p. 2] · [G, Rec. 5; survey printed p. 2: "Provide remote narrow bandwidth radar repeater scope"] (asked for, not done)

### A6-S8 · narration
**Picture:** [graphic] the chain's front end of A5-S12: between the town and the Weather Bureau, small spotter marks are drawn one by one and each lights. A small paper card: "severe storm warning reporting networks", source line "Weather Bureau survey, 1965, p. 2, recommendation 3". On the second sentence the word "SKYWARN" on glass, source line "National Weather Service, Chicago".
> For Marion's late phone call, it asked for stronger storm reporting networks in local communities. The Weather Service says that push led, in time, to the spotter program called Skywarn.

**Rows:** [G, Rec. 3; survey printed p. 2] · [G; LOT: "eventually resulted in the formation of SKYWARN"]

*([loop L9 closes].)*

### A6-S9 · narration
**Picture:** [graphic] a circle drawn in three parts; one part fills amber on "a third". Then two small generator marks under two drawn desks. Small source line "Disaster Research Center, 1966, pp. 28 to 30".
> Within three months, about a third of the offices the researchers asked had made changes or planned to. Two city police departments ordered new generators.

**Rows:** [G; study printed pp. 28-29] · [G; study printed pp. 29-30]

### A6-S10 · narration
**Picture:** [drawing] the drawn microphone, its lamp lit. Two paper strips come in beside it, one under the other: "TORNADO FORECAST", "TORNADO WARNING". Small paper card: "Saturate the public", source line "Weather Bureau survey, 1965, p. 2, recommendation 2", then "Disaster Research Center, 1966, p. 30".
> The team asked the Bureau to flood the public with material on forecasts, warnings and what to do for each. Radio, TV and newspapers were already spending much more time explaining the difference.

**Rows:** [G, Rec. 2; survey printed p. 2] · [G; study printed p. 30]

### A6-S11 · narration
**Picture:** [graphic] two typed words on glass, our label and not paper: "TORNADO FORECAST" with a line through it, then "TORNADO WATCH". Source line "National Weather Service, Chicago".
> Many people, the Weather Service says, had taken a warning for a mere update to the forecast. So the tornado forecast was renamed the tornado watch.

**Rows:** [G; LOT, read by the fact check: "they simply thought a warning was an 'update'"; "the term 'tornado forecast' was changed to 'tornado watch'"] (a Weather Service statement; no year given, no 1965 document read)

### A6-S12 · narration
**Picture:** [graphic] our drawing of a horn on a pole; on the first sentence sound lines are drawn from it, then a second set shaped like speech. On the second sentence a paper card: "It is presently impossible to tell what effect these recommendations will eventually have", source line "Disaster Research Center, 1966, p. 31".
> Several communities were looking into a warning system that could carry a voice as well as a blast. The researchers wrote that it was impossible to tell yet what the recommendations would do.

**Rows:** [G; study printed p. 33] · [study printed p. 31]

### A6-S13 · narration
**Picture:** [film] the 1967 civil defense training film (inventory A14, shot 14-01, 0:33.3 to 0:45.6: a siren horn on a pole in tree branches), muted, in the framed 4:3 window with the label "Civil defense training film, 1967". It stands for a siren of the time, not an Indiana one. No siren is heard, here or anywhere. On the second sentence a quote strip: "have not gone to a siren system", source line "Disaster Research Center, 1966, p. 33".
> But that evening, in most communities, no siren sounded. And when the researchers asked, most communities in northern and central Indiana still had no siren system.

**Rows:** [F, sirens row; study printed p. 33]

*(blackout 0.7 s)*


## Z1 · Close

### Z1-S1 · Paul on camera, one clip
**Picture:** [Paul] Paul on camera, full frame, the white shirt desk frame. One clip, these words and nothing else.
> When the forecast went out, the offices typically said telling the public was the stations' job. Backing the stations up was nobody's job.

**Rows:** [A6; study printed p. 9: "typically replied"] · [C9; study printed p. 9: "in response to a tornado forecast"]

*([loop L1 closes]: whose job it was to tell the family.)*

### Z1-S2 · narration
**Picture:** [graphic] the hook tail's frame one last time: the eight rows and the blank ninth row with its cursor. Nothing is typed into it. On the second sentence the chain comes up under the list with the police desk and its red stop mark.
> The family was never a row on that list. Reaching them was mostly left to an announcer who might not have been told, and that evening it stopped on a police desk.

**Rows:** [A6; study printed p. 14] · [C12; study printed p. 35; C5; study printed p. 22]

### Z1-S3 · narration
**Picture:** [drawing] [RS] [VE] our own drawing in the same line: a cell phone beside the drawn house, a drawn cell tower behind them. Light runs from the Weather Bureau desk to the tower and to the phone, past the list. The house's window turns amber for the first time. Source line "National Weather Service".
> Today a tornado warning from the National Weather Service goes out through the phone carriers to the cell phones in the warned area. Nobody is on a list, and nobody has to sign up.

**Rows:** [NWS, https://www.weather.gov/riw/WEA_Info : "sent directly to your phone by authorized government alerting authorities through your mobile carrier"; NWS, https://www.weather.gov/news/062422-wea-10yr ; FEMA, https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system]

*([loop L4 closes]: the end of the list today.)*

### Z1-S4 · narration
**Picture:** [map] our Indiana map, every county lighting amber in one sweep from the Weather Bureau's dot. Label "statewide tornado drill · each spring". No date.
> And Indiana still runs a statewide tornado drill each spring, a test of the systems that carry a warning.

**Rows:** [NWS Indianapolis, https://www.weather.gov/ind/severewxweek : "statewide test of communication systems"; the 2026 drill was in March; no later date is published]

*(the book, once, here: per structure.md "then the book once". No copy is written here; the wording belongs to the CTA contract in DESIGN.md.)*

### Z1-S5 · narration
**Picture:** [graphic] the channel title card. The signature footnote plays over it; it is the outro.
> Disasters don't ask permission. But they do send warnings. Learn how yours will reach you, so when it comes, you already know what to do. This was The Warning Hour.

**Rows:** (the channel's signature closing footnote, DESIGN.md; "what yours sounds like" changed to "how yours will reach you" for this episode)


## Sound, hook and intro
Preview v1, 12 Oct 26. Files in `media/sfx/`, mounted in `index.html` "SOUND". No broadcast, radio or archive audio.
- **No siren.** The story is a warning that did not travel, so the sound a warning makes is never heard here.
- **One low bed from 0:00, mounted 0.13** (`bed-hook-intro.mp3`): the DeAPI track `assets/sfx/deapi/score-act1-darkambient.mp3`, a slow sub-bass drone with no pulse and no melody, so nothing in it sounds like an alarm. The track is a 60 s loop that falls about 20 dB in places; it is levelled so the bed never drops out by accident (mean -20.0 dB, the level of El Reno's bed). `ffmpeg -ss 18 -t 111.24 -i assets/sfx/deapi/score-act1-darkambient.mp3 -af "dynaudnorm=f=250:g=15:p=0.5:m=30,afade=t=in:d=0.4,afade=t=out:st=110.94:d=0.30" -ar 48000 -b:a 192k media/sfx/bed-hook-intro.mp3`
- **The bed leaves on the intro's last word.** It fades over 0.3 s from the start of "nobody?" (110.94), so the word ends in silence and the hold and the blackout after it are silent. The question is the first moment with nothing under it.
- **One swell, on the toll, mounted 0.4** (`swell-toll.wav`): it starts at 8.19 under Paul's last words ("stations, not homes"), carries the cut to the photographs and ends on the last sound of "that day" (13.19), as a riser ends where its line ends. It is the only swell in this cut. The source peaks at -20 dB, so it is raised first: `ffmpeg -i assets/sfx/sfx-swell.wav -af volume=14dB media/sfx/swell-toll.wav` (peak -6.0 dB).
- **A telephone ring, mounted 0.3** (`telephone-ring.wav`), on "It", the first word of T1-S2's second sentence (19.17): one ring of a bell telephone, 1.25 s and its ring-out, over by the word "list". It is the Weather Bureau calling out, heard before the telephone is drawn. Made in house, two bell tones struck in turn 20 times a second: `ffmpeg -f lavfi -i "aevalsrc='if(lt(t,1.25),(0.55*sin(2*PI*1020*t)+0.20*sin(2*PI*2815*t))*exp(-38*mod(t,0.05))+(0.45*sin(2*PI*1290*t)+0.16*sin(2*PI*3560*t))*exp(-38*mod(t+0.025,0.05)),((0.55*sin(2*PI*1020*t)+0.20*sin(2*PI*2815*t))+0.39*(0.45*sin(2*PI*1290*t)+0.16*sin(2*PI*3560*t)))*exp(-9*(t-1.25)))':s=48000:d=1.85" -af "highpass=f=500,lowpass=f=4500,aecho=0.8:0.5:35:0.25,afade=t=in:d=0.004,afade=t=out:st=1.70:d=0.15,volume=3.7dB" -ac 1 media/sfx/telephone-ring.wav` (peak -6.0 dB). It sits under speech for its whole length, so it is mounted under the 0.4 a short hit gets.
- **Four soft key strikes, mounted 0.35** (`key-strike.wav`), one on each row read aloud in T1-S3: "State" 22.66, "Sheriffs" 24.34, "City" 25.60, "Named" 26.96. The list is typed, so each name read off it gets one key. The four grey rows get none. Made in house, a short click over a low thud: `ffmpeg -f lavfi -i "aevalsrc='(random(0)*2-1)*exp(-120*t)*0.7+sin(2*PI*190*t)*exp(-38*t)*0.6+sin(2*PI*2400*t)*exp(-160*t)*0.25':s=48000:d=0.22" -af "highpass=f=100,lowpass=f=5500,afade=t=in:d=0.002,afade=t=out:st=0.17:d=0.05,volume=-4.4dB" -ac 1 media/sfx/key-strike.wav` (peak -6.0 dB).
- Nothing else. No hit on a page, a clock or the chain: from the list to the question the bed and the voice carry it.
