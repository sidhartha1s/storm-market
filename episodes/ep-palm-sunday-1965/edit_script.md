# ep-palm-sunday-1965 · edit_script.md (v2: hook, hook tail and intro only; fix pass 1 applied 12 Oct 26, hook lines corrected to the page images; nothing locked)

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
- H1-S1 alternative, 26 words, with Indiana spoken and the Weather Bureau unnamed: "Police in one Indiana county heard a tornado reported and told nobody until it hit. South Bend's warning went to offices and stations, not homes."
- Narration numbers follow the El Reno copy: spelled out, no hyphen ("five forty three", "nineteen sixty five"). The claim in I1-S9 is the locked wording with its year spelled for the voice.
- The claim carries "desk", a word the critique lists as unshowable. It is the locked wording, so it stays; a drawn desk appears on that word.
- T1-S3 is four name-only sentences, the telephone list read aloud. The quickref bans trailer fragments; this is the owner's picked line and stays as picked (orchestrator ruling, 12 Oct 26).
- Study pages shown on screen are the scan of the 1966 working paper. That scan is not a row of the picture inventory; its rights line has not been read.
- Drawings are used only where the inventory has nothing real: the house, the living room and its television set, the announcer's microphone, the desk.
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- Start times wait on the voice probe; none is estimated here.

---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one: the white shirt desk frame used in El Reno, not a thumbnail image. He speaks these two sentences in one clip and nothing else. Label "April 11, 1965 · one Indiana county" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> Police in one county heard troopers report a tornado and told nobody until it hit. The Weather Bureau's warning went to offices and stations, not homes.

**Rows:** [C2, A7; study printed pp. 19 to 20, page image read: city police monitored the 5:50 PM State Police message; headquarters notified no one "until after the first tornado hit the county"] · [A6; study printed p. 14: the list holds offices and stations, no households]


## T1 · Hook tail (start time waits on the voice probe)

### T1-S1 · narration
**Picture:** hard cut on the first word to real photographs, never black: the damage pictures marked Free in the inventory, each with its place label: Sunnyside in Dunlap, Indiana (C2), Alto, Indiana, from the air (C5), Pittsfield, Ohio (C7). The number "271" lands on "two hundred seventy one" and holds. Source line under it, small: "four National Weather Service offices · other counts run from 260 to 266". One bed swell, no siren.
> Two hundred seventy one people lost their lives that day.

**Rows:** [F] (said once; the attribution sits on screen, after the number)

### T1-S2 · narration
**Picture:** a Weather Bureau teletype room photograph (inventory A3, teletype operators at the Weather Bureau Communications Center, about 1955). A clock "5:43 PM" lands on "five forty three". The warning itself comes in as the survey report's own page, first line underlined: "Severe thunderstorm and tornado warning." (inventory B1). Place label "South Bend, Indiana". On the second sentence a telephone ring, made in house, and the clock label fades so the telephone is not pinned to 5:43.
> At five forty three, the Weather Bureau in South Bend issued a tornado warning. It telephoned its warnings down a list.

**Rows:** [A6; survey printed p. 39] · [A6; study printed p. 14: South Bend "also telephoned several organizations", said of its warnings in general]

### T1-S3 · narration
**Picture:** the whole telephone list typed over the teletype room photograph, eight rows in the study's order: State Police, Sheriffs' Departments, City Police Departments, Indiana and Michigan Electric Company, Red Cross, Specified radio and TV stations, Flying services, Airlines. The four spoken rows tick as they are said. The other four stay grey and readable, so four never reads as the whole list. One soft key strike per tick.
> State Police. Sheriffs. City police. Named radio and television stations.

**Rows:** [A6; study printed p. 14] (four of the eight entries)

### T1-S4 · narration
**Picture:** the list scrolls past its eighth row to a ninth, which is blank, cursor blinking, no tick. Below the list, apart from it, a drawn announcer's microphone and then a drawn house, both dark. The microphone stands for any station; no named or quoted station is drawn as part of the South Bend list. Drawn because the inventory has no 1965 studio or home.
> A family got it from an announcer, if the announcer had it.

**Rows:** [C12] [C8] (the C8 station has no name and no county in the study)

### T1-S5 · narration
**Picture:** one frame holding everything so far: the eight rows, the blank ninth row, the dark microphone, the dark house. Push in slowly on the blank row and hold it through the question.
> Whose job was it to tell the family at the end of the list?

**Rows:** (the question; no row)

*([loop L1 open]: whose job it was to tell the family. The closing act is set when the acts are written.)*

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The living room and the list (start time waits on the voice probe)

### I1-S1 · narration
**Picture:** the drawn house from T1-S4, now in afternoon sun, seen from the street. Date label "Palm Sunday · April 11, 1965". Move through the front window into the living room: a television set and a table radio, both switched off. A drawing, because the inventory holds no picture of a home or a street that day.
> April eleventh, nineteen sixty five, was the first nice spring day of the year. Many people had no radio or television on.

**Rows:** [C21] · [C21]

### I1-S2 · narration
**Picture:** our own map of Indiana, one pin on South Bend. Name card "Ron Przybylinski · age 11 · South Bend · recalled in 2014". Then the drawn television set, switched on: its screen changes from a plain programme frame to a card reading "WEATHER BUREAU". No frame of the real show; nothing real exists that we may use.
> In South Bend, Indiana, an eleven year old was watching Lassie when the Weather Bureau broke into the show.

**Rows:** [E] (facts.md states an age and no gender, so "an eleven year old")

### I1-S3 · narration
**Picture:** the drawn television screen flips from the "WEATHER BUREAU" card back to the plain programme frame on "went back". Then the study's own page (printed p. 37) fills the frame, one sentence underlined as it is spoken: "There was not a cloud in the sky." Source line "Disaster Research Center, 1966".
> Stations cut in with a warning, then went back to their shows. People looked outside, and there was not a cloud in the sky.

**Rows:** [C22] · [C22]

### I1-S4 · narration
**Picture:** the tornado track map of the day (inventory B7, courtesy Dr. Russell Schneider, SPC). Six state names light one by one: Iowa, Illinois, Wisconsin, Indiana, Michigan, Ohio. Then a clock "11:45 AM" over a teletype machine photograph (inventory A4), with the label "Forecasters · Kansas City". No free picture of the Kansas City forecast room exists (A7 is Ask). [verify: whether the 11:45 AM forecast is one of the four forecast scans in inventory A9, to show it as a document card]
> Tornadoes crossed six states that day. By eleven forty five that morning, forecasters in Kansas City had a tornado forecast out on the teletype.

**Rows:** [IWX page, six states confirmed by the checker 11 Oct 26] · [A1]

### I1-S5 · narration
**Picture:** the eight-row telephone list from T1-S3 returns over the teletype room photograph (inventory A3). The "Specified radio and TV stations" row lights and a small red "ON AIR" lamp comes on beside it. Nothing else on the list moves.
> The stations on that list were supposed to put the warning on the air.

**Rows:** [A6] [verify: the A6 warning asks stations "to use emergency frequencies"; confirm that this means broadcast it]

### I1-S6 · narration
**Picture:** the study's own page (printed pp. 19 to 20), one sentence underlined as it is spoken: "Police headquarters did not notify other members of their own organization nor any other organization until after the first tornado hit the county." Label "one Indiana county", the county of Paul's line.
> In one county, police headquarters did not tell their own officers until the first tornado hit.

**Rows:** [C2] (County A)

### I1-S7 · narration
**Picture:** the study's own page (printed p. 23), label "a different county". The sheriff's sentence is underlined as the narrator speaks it: "We didn't have any warning at all". Source line "a county sheriff · Disaster Research Center, 1966". The narrator reads the words; no actor's voice.
> A sheriff in another county found out when the tornado was going over, and said, "We didn't have any warning at all."

**Rows:** [C6] (County B)

### I1-S8 · narration
**Picture:** the same page holds; the underline moves on to the sheriff's next sentence, "the television didn't even list here". Then cut to the drawn television set from I1-S2, its screen on the plain programme frame.
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
