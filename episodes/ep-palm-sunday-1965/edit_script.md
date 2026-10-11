# ep-palm-sunday-1965 · edit_script.md (v1: hook, hook tail and intro only; nothing locked, nothing fact-checked)

Lane: documentary (`/storm-episode`). Built on the angle the owner locked on 11 Oct 26 (`angle.md`) and the structure he signed off (`structure.md`). Hook and tail are Rebuild 2 of `hook-critique.md`, the owner's pick. Facts from `research/facts.md`; pictures from `research/picture-inventory.md`. Status: DRAFT; hook and intro wait on the fact-check fan-out, the grader and the owner.

## A. Header
- **Title (owner, verbatim):** Who Stopped the Palm Sunday 1965 Tornado Warning?
- **Target runtime:** 20 to 25 min; planned at 22:00 (`structure.md`) until `word_budget.py` sizes it from a probe at the shipping tempo.
- **Claim (locked, copied):** On Palm Sunday 1965 the forecast did not fail and the warnings were sent. They stopped one desk short of the people.
- **Dominant question:** the viewer keeps watching to find out where exactly the warning stopped, and who was holding it.
- **Architecture:** a detective story on a clock. One message is followed from office to office; each act moves the clock on.
- **Scope held in every act:** the 1966 study covers Indiana only and hides its counties ("County A", "County B"). No county, town or department is named on air as the one. County A (rows C1, C2) and County B (rows A13, C5, C6, C7) are never joined in one sentence. In County B the narration says "where the tornado was", never "tornado warning".

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
- H1-S1 and T1-S1 to T1-S5 are Rebuild 2 word for word. No word was changed.
- Narration numbers follow the El Reno copy: spelled out, no hyphen ("five forty three", "nineteen sixty five"). The claim in I1-S8 is the locked wording with its year spelled for the voice.
- The claim carries "desk", a word the critique lists as unshowable. It is the locked wording, so it stays; its picture is the chain graphic stopping one link short of the house.
- T1-S2 is four name-only sentences, the telephone list read aloud as it writes itself. The quickref bans trailer fragments; this is the owner's picked line, kept as picked and flagged for the grader.
- Loop tags and timing notes sit between segments as plain notes, never inside a blockquote.
- Start times wait on the voice probe; none is estimated here.
- Every line from the 1966 study (C rows) was read from scan text and needs the page image read before it is voiced.

---

## H1 · Hook (0:00)

### H1-S1 · Paul on camera, one clip
**Picture:** Paul on camera, full frame, frame one: the white shirt desk frame used in El Reno, not a thumbnail image. He speaks these three sentences in one clip and nothing else. Label "April 11, 1965 · Indiana" inside the first second. Low drone bed from 0:00; no broadcast, radio or archive audio. Cut out on his last word.
> Police headquarters heard the tornado warning and did nothing until it hit. That warning never went to homes. It was telephoned down a list of offices.

**Rows:** [C2] · (no row; follows from A6) · [A6] [verify: C2 says police "had heard the State Police message" (A7); read the page image before "heard the tornado warning" is voiced. The telephone list in A6 is the South Bend warning of 5:43 PM; confirm "That warning" may stand for both messages]


## T1 · Hook tail (start time waits on the voice probe)

### T1-S1 · narration
**Picture:** hard cut on the first word, never black: a Weather Bureau teletype room photograph (inventory A3, teletype operators at the Weather Bureau Communications Center, about 1955; or A4). A clock "5:43 PM" lands on "five forty three". The warning itself slides in as a teletype card, first line readable: "Severe thunderstorm and tornado warning." (Weather Bureau survey report, inventory B1). Place label "South Bend, Indiana". A telephone ring is the only sound effect, made in house.
> At five forty three, the Weather Bureau in South Bend picked up the telephone.

**Rows:** [A6]

### T1-S2 · narration
**Picture:** the telephone list writes itself, one typed row per name, each row landing on its word and getting a tick: "State Police", "Sheriffs", "City police", "Named radio and TV stations". The clock from T1-S1 keeps running in the corner. One soft key strike per row.
> State Police. Sheriffs. City police. Named radio and television stations.

**Rows:** [A6]

### T1-S3 · narration
**Picture:** the list scrolls to its last row, which is blank, cursor blinking, no tick. The chain graphic draws out from the "stations" row to a drawn radio announcer's microphone, then to a drawn house at the end of the chain. The house is dark.
> A family got it from an announcer, if the announcer had it.

**Rows:** [C12] [C8]

### T1-S4 · narration
**Picture:** photographs of the damage, the rows marked Free in the inventory: Sunnyside in Dunlap (C2), Alto from the air (C5), Pittsfield (C7). The number "271" lands on "two hundred seventy one" and holds. Small source line "National Weather Service". One bed swell, no siren.
> Two hundred seventy one people lost their lives that day.

**Rows:** [F] (four Weather Service pages give 271; the count is disputed, 258 to 271, and is said once)

### T1-S5 · narration
**Picture:** back to the whole chain graphic in one frame: Kansas City, South Bend, the four ticked rows, the blank row, the dark house. Push in slowly on the blank row and hold it through the question.
> Whose job was it to tell the family at the end of the list?

**Rows:** (the question; no row)

*([loop L1 open]: whose job it was to tell the family. The closing act is set when the acts are written.)*

*(no void: cut straight into the intro. No black hold, title card or disclaimer before 1:00.)*


## I1 · The living room and the list (start time waits on the voice probe)

### I1-S1 · narration
**Picture:** the drawn house from T1-S3, now in afternoon sun, seen from the street. Date label "Palm Sunday · April 11, 1965". Move through the front window into the living room: a television set and a table radio, both switched off. Not in the inventory: this room is our own drawing.
> April eleventh, nineteen sixty five, was the first nice spring day of the year. Many people had no radio or television on.

**Rows:** [C21] · [C21]

### I1-S2 · narration
**Picture:** our own map of Indiana, one pin on South Bend. Name card "Ron Przybylinski · age 11 · South Bend · recalled in 2014". Then the drawn television set, switched on: its screen changes from a plain programme frame to a card reading "WEATHER BUREAU". No frame of the real show.
> In South Bend, Indiana, an eleven year old was watching Lassie when the Weather Bureau came on the station.

**Rows:** [E]

### I1-S3 · narration
**Picture:** the drawn television screen flips from the "WEATHER BUREAU" card back to the plain programme frame on "went back". Then the living room window: a clear evening sky, nothing in it. Quote card "There was not a cloud in the sky." with source line "Disaster Research Center, 1966".
> Stations cut in with a warning, then went back to their shows. People looked outside, and there was not a cloud in the sky.

**Rows:** [C22] · [C22]

### I1-S4 · narration
**Picture:** the tornado track map of the day (inventory B7, courtesy Dr. Russell Schneider, SPC). Six state names light one by one: Iowa, Illinois, Wisconsin, Indiana, Michigan, Ohio. Then a clock "11:45 AM" over a teletype machine photograph (inventory A4), and the first link of the chain graphic lights: "Forecasters · Kansas City". Not in the inventory: a free picture of the Kansas City forecast room (A7 is Ask). [verify: whether the 11:45 AM forecast is one of the four forecast scans in inventory A9, to show it as a document card]
> Tornadoes crossed six states that day. Forecasters in Kansas City had a forecast on the Weather Bureau teletype by eleven forty five that morning.

**Rows:** [IWX page, six states confirmed by the checker 11 Oct 26] · [A1]

### I1-S5 · narration
**Picture:** the telephone list from T1-S2 returns. The "Named radio and TV stations" row lights and a small red "ON AIR" lamp comes on beside it. Then each other row (State Police, Sheriffs, City police) gets an empty tick box labelled "back up radio and TV" and every box stays empty. Source line "Disaster Research Center, 1966".
> The stations on that list were to put the warning on the air. Asked later, no one in any organization saw backing up radio and television as their job.

**Rows:** [A6] [verify: the A6 warning asks stations "to use emergency frequencies"; confirm that this means broadcast it] · [C9]

### I1-S6 · narration
**Picture:** a drawn telephone on a police switchboard, receiver back on its hook. Chain graphic label "one Indiana county". The study's sentence as a document card, one phrase underlined: "did not notify other members of their own organization". Not in the inventory: any picture of a 1965 police radio room.
> In one county, police headquarters did not tell their own officers until the tornado had hit.

**Rows:** [C2] (County A)

### I1-S7 · narration
**Picture:** chain graphic label changes to "a different county". Role card "SHERIFF" with a drawn sheriff's star. Quote card, his words only: "We didn't have any warning at all." Source line "a county sheriff · Disaster Research Center, 1966". Text only, never a voice.
> A sheriff in another county found out when the tornado was going over, and said, "We didn't have any warning at all."

**Rows:** [C6] (County B)

### I1-S8 · narration
**Picture:** [RS] [VE] the whole chain graphic, drawn end to end for the first time: Kansas City, South Bend, the telephone list, the announcer's microphone, the house. Every link lights in order and the light stops one link short of the house. The house stays dark. Hold through the second sentence.
> On Palm Sunday nineteen sixty five the forecast did not fail and the warnings were sent. They stopped one desk short of the people.

**Rows:** [claim, angle.md]

### I1-S9 · narration
**Picture:** the telephone list one more time. The "City police" row is already marked. The other rows pulse one at a time: "State Police", "Sheriffs", "Named radio and TV stations". Hold on the list; the bed drops out on the last word.
> Were police the only ones who told nobody?

**Rows:** (the question, from "Questions worth keeping" in `hook-critique.md`; no row)

*([loop L2 open]: whether police were the only ones. First paid in Act 1 with the stations that never passed on the forecast, row C13.)*

*(blackout 0.7 s)*
