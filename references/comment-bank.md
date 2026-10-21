# Comment bank: what viewers say under reference videos

**Rule (owner, 6 Oct 26).** From 6 Oct 26 on, every reference video gets its comments analysed, whoever picked it
(the owner or the agent) and whatever it is a reference for (script, topic, thumbnail, edit). The findings are added
to this file, so the bank grows with every video. The episode research quotes the entries that apply, which is how
they reach the script writer. A new reference video with no entry here is unfinished research. Videos used as
references before 6 Oct 26 are not backfilled unless the owner asks.

## How to pull and read
1. Pull twice, into a scratch folder (never the repo): YouTube's "Top comments" order, then newest.
   ```
   yt-dlp --skip-download --write-comments --write-info-json --extractor-args "youtube:comment_sort=top;max_comments=300,300,0,0" -o "<dir>/top/%(id)s" <url>
   yt-dlp --skip-download --write-comments --write-info-json --extractor-args "youtube:comment_sort=new;max_comments=150,150,0,0" -o "<dir>/new/%(id)s" <url>
   ```
   The comments land in `<id>.info.json` under `comments` (`text`, `like_count`, `_time_text`, `is_pinned`,
   `author_is_uploader`). Replies are not pulled.
2. "Top comments" is YouTube's own order, not a likes sort: sort the top pull by `like_count` yourself (in the
   Titanic pull, 123 of the 300 had 0 likes). A sort is fine, and so is a word match to size a theme you have
   already read. Neither replaces reading, because what a comment means is a judgment.
3. Dates: use `_time_text` ("5 months ago") with the pull date. The `timestamp` field is only the pull date minus
   that age, so it is the latest possible date, not the real one.
4. Read both lists yourself: the most liked first, then the newest.
5. Write the entry below. Quote the comment as written, typos included, and give its likes. A finding with no quoted
   comment does not go in.

## What to look for
- **Did the video land, and why.** What viewers praise or attack: the art, the voice, the ending, the title.
- **What they wanted to see.** Requests, follow-up angles, "you missed X".
- **Suggestions and corrections.** A correction with hundreds of likes is a fact our script must get right.
- **High-like comments that are off the video's topic.** A viewer asking for x, y, z with 200 likes under an El Reno
  video is a topic lead for us even though it says nothing about El Reno. Keep it.
- **Dates.** Old top comments show the launch audience; the newest show who still arrives and what they say now.

## Earlier comment findings (before this file, not moved here)
`references/ep6-katrina/comment-insights-darkhorizon.md`, the "Top comments" blocks in
`references/mini-storms/teardowns/README.md`, and the per-video cards under `references/teardowns/`.

## Entries, newest first

_Camille 1969 episode research, 21 Oct 26: six reference videos on the subject (the Virginia mountain flood inside a famous coast hurricane), plus one extra general video. Pull: Top order (up to 300) and 150 newest, 21 Oct 26. Teardown: `episodes/ep-camille-1969/research/teardowns.md`._

### "Hurricane Camille (1969) - The Original Monster Storm | Documentary" (Rex Jones)
https://www.youtube.com/watch?v=mOLSKRBhcGM, uploaded 28 Aug 19 (a University of Mississippi film, 55:59, channel 2,020 subscribers).
Pulled 21 Oct 26: 300 from the Top order and the 150 newest (66 of the newest also in the Top 300, so 384 different comments); 750,323 views and 8,496 likes that day. In the Top 300, 47 have 0 likes.

**Why it landed**
- The most liked comment is a Seabee child's memory, not a comment on the film: "I was almost 5, the son of a Navy Hospital Corpsman assigned to the base dispensary at the SeaBee base in Gulfport." (411, 11 months ago). Next, the humanity: "I watched a video about the beauty of humanity. People lost everything in their lives but were full of love and smiles because they knew they still had their lives." (286, 1 year ago); "Tragedy doesn't build character…it reveals it." (200, 1 year ago).
- Katrina is the yardstick viewers use: "This is a good doc. Camille was the benchmark until the occurrence of Katrina." (164, 1 year ago); "Born 1980 and raised in Gulfport, all I ever heard growing up were horror stories of Camille." (130, 11 months ago).
- Calm after: "The big difference between Camille and Katrina is with Camille you don’t see all looting and violence" (67, 1 year ago).

**Corrections and pushback**
- The title is attacked from Texas: "The original monster storm was the 1900 Galveston Hurricane. But agree, Camille was awful." (168, 1 year ago, edited); "it is NOT the original monster. That honor goes to Galveston Texas." (63, 1 year ago).
- Betsy's year: "20:58 I’m confused, he says Betsy was in 47, but I thought Betsy was in 65." (0, 2 days ago).
- Two Virginia counts in one video's comments, both unsourced: "killed approximately 153 people, with many bodies never found" (127, 5 months ago) and "After leaving the coast the storm moved north and stalled over the Blue Ridge. 39 people died in Nelson County" (4, 1 year ago). Another says "Many hundreds perished in the flooding." (3, 1 year ago).

**The newest 150** (7 hours to 1 year old; the top one is the pinned question at 64 likes, a viewer asking why people stay in hurricane country, 5 months ago)
- A teacher's class: "My teacher is making me watch this i am in the middle of class" (1, 1 month ago).
- Who was left out: "Was there any black people affected by this hurricane" (0, 1 month ago).
- Still found as a lesson: "People need to pay attention to this and not ignore warnings." (0, 2 weeks ago).

**What they add or ask for**
- The Virginia gap, said in so many words: "I wish this doc had gone further and spoken of the devastating second strike that Camille made - in Nelson County, VA." (127, 5 months ago). The same viewer: "This portion of the tragedy is always given short shrift, but with a relatively small population in the foothills of the Blue Ridge Mountains, the loss of life was catastrophic."
- A second: "This video only shows the effects of the storm along the gulf coast and does not mention the effects of Camille on Nelson County, Virginia." (4, 1 year ago).
- A book lead with likes: "Read the book Torn Land. It tells of the storm coming through Nelson county Virginia." (20, 1 year ago).
- Viewers who were in Virginia: "Was a young kid when Camille came through our town outside of Richmond Virginia." (24, 1 year ago).
- Another comment says the video did not name the Tye River: "No mention of the Tye River in VA 31 inches of rain in 3 hrs mtns" (0, 1 month ago).

**For our scripts**
- The 127-like missed-Virginia comment under the most-watched Camille video is the audience for this angle. It also carries a count (153) and a claim (bodies "buried under the heavy Va clay turned slurry") with no source: the script gets its own count from the primary check.
- Do not let the opening claim "original monster" or "strongest": a Galveston reply has 168 likes.

### "HURRICANE CAMILLE 1969: The Category 5 Storm Too Strong to Measure" (FAULT LINES)
https://www.youtube.com/watch?v=nKvUuTK2piQ, uploaded 8 Aug 26 (29:54, channel 13,300 subscribers).
Pulled 21 Oct 26: 185 from the Top order (every comment on the video) and the 150 newest (146 also in the Top pull, 189 different comments); 251,635 views and 2,273 likes that day. 69 of the 185 have 0 likes.

**Why it landed**
- It is a Gulf Coast memory page. The most liked comments are first-person: "This film is so well done. Legendary storm." (74, 2 months ago); "I was 6. We lived in Louisiana and fled to my grandparents house near Hattiesburg MS because she was projected to hit Louisiana. That turned out to be a bad move." (61, 1 month ago); "I was 10 years old when she came through here. I still remember it like it was yesterday. Then we had Katrina." (58, 2 months ago).
- A coast family: "My dad had told my sister and I that he was camping with his family when he was five years old when Hurricane Camille hit." (32, 2 months ago).
- The barometric-pressure explanation is credited: "Very good explanation of "barometric pressure", the key to a hurricanes ultimate strength." (7, 1 month ago).

**Corrections and pushback**
- Pronunciation: "It's pronounced Pass Christi-anne not Christian just a FYI" (12, 2 months ago); said again "Its pronounced Pass Christi-ann bud not Christian" (0, 3 weeks ago).
- Ship Island: "The gap in Ship Island is NOT THERE. The island has recently been returned to its original state after all these years." (8, 2 months ago). The video says "The gap is still there."
- Galveston: "Do not ignore the Galveston Hurricane of 1900, 8,000 (maybe 12,000) killed" (8, 1 month ago).
- Venice, Louisiana left out: "No talk of the devastation in Venice, LA. It was as bad as anywhere." (0, 1 month ago).
- The voice: "Downvote for the AI voice." (0, 1 month ago); "The whistling sound of the voice narrating is almost unbearable to listen to this documentary!" (0, 1 month ago); "AI SLOP. I'M OUT." (0, 2 months ago).

**The hurricane party belief** (the video calls it a legend; viewers split)
- Believers: "I’m glad I watched this. I grew up in southeast Virginia and I do remember it being reported that those people did have a hurricane party." (2, 2 months ago); "I remember the gang of people in Biloxi that was having a “hurricane party “and I remember that after it was over, they were nowhere to be found ; they were told to leave and they didn’t want to and they all died." (2, 1 month ago, edited).
- Defenders of the practice: "Hurricane parties down here are a norm" (10, 2 months ago); "'Hurricane Parties' are not drunken debaucheries." (2, 1 month ago).

**Virginia mentioned by viewers** (4 of 189 by reading, 3 by word match)
- A driver on Route 29: "I lost my car driving through southwest Virginia when my brother and two friends as well as myself got stuck in the flood waters at a small intersection on route 29 Virginia in nelson County called davis creek...so many people lost their lives and I still don't know how we were spared" (7, 1 month ago).
- Northern Virginia: "I lived in Northern Virginia away from the worst by far, but the rainfall filled our basement and most the first floor." (5, 2 months ago).

**The newest 150** (6 days to 2 months old)
- Two near-identical comments quote the video's closing line back: "Five is not the top of what nature can do." (1, 6 days ago); "Five is not the top of what nature can do. It is only the top of what we had seen when we drew the chart." (1, 7 days ago). Both end in a question and look prompted.
- A Virginia camper: "We were camping with two neighbor families at Shenandoah Acres in Stuart’s Draft VA. I was 8 - my memory is of rain - hard and fast - and water inches deep running across the ground." (1, 1 month ago).
- A missing person's family: "My mom’s older sister died in Camille. Her name was Vera Pearl Holifield. She was found 3 weeks after the storm and was identified by her jewelry." (0, 1 month ago).

**What they add or ask for**
- No one asks for more on Virginia. The viewer base is the Gulf Coast, and the 4.5 minutes on Nelson County drew 3 or 4 comments in 189.

**For our scripts**
- The audience for a Camille video is largely coast people with first-hand memories. A Virginia-led video reaches a different set: the Virginians in the other entries.
- "Hurricane party" is believed by some viewers even after a video says it is a legend. If we touch it, say what the sources show and where the story started.
- A synthetic-sounding voice is attacked in three comments here. Our own voice is a clone of Paul's; keep it from sounding processed.

### "The Storm That Cut an Island in Half - Camille 1969" (Dark Horizon)
https://www.youtube.com/watch?v=QNkW1ndzsag, uploaded 4 Sep 26 (17:04, channel 49,100 subscribers).
Pulled 21 Oct 26: 42 from the Top order (every comment) and the 45 newest (45 different comments together, the whole set); 157,181 views and 1,060 likes that day. 18 of the 42 have 0 likes.

**Why it landed**
- A Mississippi widow corrects and compares: "Katrina hit the MS coast not NOLA and it did just as much damage due to it being very large but very slow." (35, 1 month ago). Next, locals: "My high school got absolutely destroyed from Camille and they had to rebuild it" (8, 1 month ago); "My Aunt and the elderly lady she took care of were both killed in Camille. She was my mom’s older sister. Her name was Vera Pearl Holifield." (8, 1 month ago).
- Real footage is praised: "Both storms found me - thanks for this using real memorable footage -- A plus documentary" (4, 1 month ago).
- A local who vouches: "You did an EXCELLENT job with this documentary. I was 7 and living in N. Biloxi on the bayou when Camille hit." (0, 1 month ago).

**Corrections and pushback**
- The hurricane party: "When can the hurricane party myth be put to bed?" (0, 1 month ago). The same viewer-voice: "I grew up hearing that legend about the “partiers” at the Richelieu, and to this day, I don’t know" (0, 1 month ago).
- The Camille Cut is closed: "AKA, the Camille cut. After Katrina widened it even more a restoration project was launched. As of 2019 it finally became a whole island again" (0, 1 month ago). (A similar correction is under FAULT LINES.)
- The voice: "the AI slop narration sucks" (0, 1 month ago); ""The goafuhmexico" I am out." (0, 1 month ago).
- Fringe: "HURRICANE CAMILLE WAS A MAN-MADE STORM" (0, 1 month ago).

**The newest 150** (here 45, 1 day to 1 month old)
- A same-week sixth category: "Now, here we are in 2026 and officials are talking about adding a 6th category to the scale." (0, 1 month ago).
- Practical: "Listen to the professionals. When they tell you to go, go. Find a way, and go." (0, 1 day ago).

**What they add or ask for**
- Next-topic requests, by reading, 6 of 45: "Can you do. The storm that nearly erased Tampa Bay, Hurricane milton 2024" (8, 1 month ago); "Might be obligated to do the Labor Day hurricane next eh?" (3, 1 month ago); "Can you do Hurricane: 1970 Bhola Cyclone" (3, 1 month ago); "Can you do about the 1997 Jarrell Texas tornado" (2, 1 month ago).
- A comparison: "So Helene did almost exactly what Camille did" (6, 1 month ago).
- Virginia is not mentioned by any viewer in 45 comments, though the video spends 4.5 minutes on Nelson County and puts "124 people" in its description. The facts there (124, 33 never found, one phone call) drew no correction and no question.

**For our scripts**
- The closest rival video states our angle in its description and gets zero reaction to the Virginia half. Viewers react to the coast and to Katrina. A Virginia-first video has to give them a reason beyond the fact that there was also a flood.
- "Hurricane party myth" is a live annoyance. Settle it from the sources in one beat or leave it out.

### "Storm Stories: Hurricane Camille Part I" (The Weather Channel)
https://www.youtube.com/watch?v=okXBaOIvkQ4, uploaded 5 Aug 19 (22:03, channel 1,390,000 subscribers).
Pulled 21 Oct 26: 97 from the Top order (every comment) and the 102 newest (102 different comments together, the whole set); 151,218 views and 1,530 likes that day. 36 of the 97 have 0 likes.

**Why it landed**
- The top comment is about the husband in the bathtub, not the storm: "I had to watch that one scene again where the lady with her two babies ... told them her husband won't let them leave." (102, 7 years ago). Two more: "How stupid was that dad to put his entire family in danger" (25, 6 years ago); "When the dad's that delusional its time to kidnap the rational humans in the building" (12, 5 years ago).
- Fans of the series: "I've missed Storm Stories. One of my favorite shows." (52, 7 years ago); "I love these weather stories thank you for keeping these up" (34, 7 years ago).
- The reporter: "RIP Bert Case" (12, 7 years ago).
- Michael as the comparison: "We just went through Hurricane Michael.. a cat 5 and I will never stay for one again" (34, 7 years ago).

**Corrections and pushback**
- Rating: "Hurricane Camille was a 6 not a 5 and I will never forget Camille." (20, 7 years ago, edited). Another wants the wind revisited: "they downgraded the sustained winds from 185mph to 175mph on reanalysis of historic hurricanes several years back ... perhaps, they need to be reev" (3, 6 years ago).
- A "what if" about a big city: "Camille is the ultimate what if it hit somewhere populated storm" (13, 6 years ago).
- The hurricane party is unverified for one viewer: "I wonder if that story about the hurricane party at the Richelieu Apartments has ever been verified." (1, 5 years ago).

**The newest 150** (here 102, 2 months to 1 year old; nothing newer than 2 months)
- Anger at the coast: "and then most of the idiots rebuild in the same damn place" (0, 2 months ago), posted three times in one form or another.
- A rebuild point: "it’s 2026, move the hell on" (0, 2 months ago).

**What they add or ask for**
- Virginia is not mentioned. Three comments (of 102) say "hold my beer" about Katrina or Camille: "Camille the mother of all Hurricanes Katrina, hold my beer" (8, 7 years ago).
- Storm-survival folklore with likes: "Camille was no lady" (4, 5 years ago).

**For our scripts**
- The most-liked reaction is to a decision (the husband refusing to leave), not to the storm. That is a pattern for us: viewers answer a choice a person made. The Nelson County equivalent is a family's choice on the night (stay on the second floor, or get in the car).
- This episode has no Virginia segment and Part II (111,472 views) was not pulled. It does not tell us anything about Virginia viewers.

### "Living in Virginia: Remembering Hurricane Camille" (VPM)
https://www.youtube.com/watch?v=dT_UVZDOhWw, uploaded 11 Nov 14 (a 1999 public-TV episode, 26:46, channel 45,700 subscribers).
Pulled 21 Oct 26: 57 from the Top order (every comment) and the 60 newest (60 different comments together, the whole set); 75,971 views and 900 likes that day. 13 of the 57 have 0 likes.

**Why it landed**
- Most comments are by Virginians with a family link. "My great grandmother died during this flood when the mountains fell down on top of her home" (17, 5 years ago). "Jeffrey Wayne Oliver (3 years) Regina Rena (5 months). My cousins." (12, 4 years ago). "The Perry family were our cousins…😞" (3, 1 year ago).
- The Raines brothers are admired: "Carl Raines is and was a very very brave man......." (15, 7 years ago).
- The Mennonite disaster service is the best-liked thing in the film: "What the Mennonites did is above and beyond gracious!! Stuck it out for a year! That's pretty great!" (17, 4 years ago).
- For people outside Virginia it is news: "I only just came across this today and it was an incredible thing to learn about. We always here about Camille down in the gulf and the damage there. I had no idea that Virginia faced such a disaster as this" (4, 1 year ago); "I'm from Mississippi I never knew Camille was still so destructive when it passed over Virginia." (0, 5 months ago); "Thanks for sharing this. I know our Gulf hurricanes cause terrible damage north of us, but didn’t know about this aspect of Camille." (7, 3 years ago).

**Corrections and pushback**
- Tone: "I refuse to downvote this vid, but I don't feel like the narrator treats this with the respect it deserves. Seems to me like he is making light of this tragedy in the way he speaks and presents it." (8, 6 years ago).
- The rain figure moves by comment. "The 27 inches of rain was a world record in two hours or so." (10, 5 years ago); "In one area, 27 inches of rain fell in 8 hours!" (5, 1 year ago); "In Nelson county, over 35 inches of rain fell in 24 hours." (3, 1 year ago); a viewer's barrel: "it measured 31 inches of rain. Some estimates say that more than 40 inches of rain fell in Davis Creek." (11, 2 years ago, edited); "We had 30” of rain in 8 hours" (6, 1 year ago, edited, from Rockbridge County). None has a source.
- A copied encyclopedia paragraph (32, 4 years ago) says "Within a 3-hour period, it dumped a record quantity of 27 inches (690 mm) of rain." The video says six hours.
- Missing in another county: "Rockbridge County still has 9 people missing from Camille. Rockbridge County is on the other side of the Blue Ridge west of Nelson County." (6, 1 year ago, edited). Unsourced; it is a different county from the one the video covers.
- The trucker: "5 tractor trailers had stopped near the Rockfish River.. It said they only recovered 2 tractors. He was in one of them." (16, 1 year ago, edited).

**The newest 150** (here 60, 2 weeks to 1 year old)
- Local memory continues: "I lived through that night at my grandparents house in Piney River. ... We came around a curve only to find that the Tye river had turned into the Mississippi River!!!" (3, 1 year ago). A rescue-squad member: "My rescue squad was assigned the James River between Wingina and Hattens Ferry." (0, 5 months ago).
- Helene links it to now: "I lived through Camille on the Gulf Coast ... But also remembered the damage it did to Virginia as well. How quickly people forget and no one remembered this after Helene hit thinking nothing like this has ever happened." (1, 1 year ago). The Top-order version: "What is happening with Helene in September 2024 is sadly reminiscent of Camille." (37, 2 years ago). "The mountains aren’t ready for hurricanes the way the coast is" (0, 5 months ago).
- Sound: "Sound ?" (0, 1 month ago).

**What they add or ask for**
- A historical marker: "There is a historical marker on Route 29 in Nelson County in remembrance of the small town of Tyro, which almost literally wiped from the face of the earth. Many of the dead were never recovered." (8, 1 year ago).
- Names of those who found: "Ty to those good people who found his body and helped recover all the other ones." (16, 1 year ago).
- Nobody asks for a death count or disputes the film's "about 130".

**For our scripts**
- Virginians arrive with family names. Names on screen must match the record: Oliver, Huffman, Raines, Wood, Perry all appear in these comments.
- Rain numbers differ across viewers (27 in 2 hours, 3 hours, 8 hours, 31 in a barrel, 35 in 24 hours). Use the one primary-source figure and say where it was measured.
- "Helene" ties 1969 to the viewers' present: "What is happening with Helene in September 2024 is sadly reminiscent of Camille." (37, 2 years ago).

### "Hurricane Camille Remnants **GRAPHIC** - Flooding in Nelson County, Virginia" (Jamey Singleton)
https://www.youtube.com/watch?v=wBTuFYwjlLw, uploaded 19 Aug 19 (46:57, channel 689 subscribers; film plus a state trooper's recorded diary).
Pulled 21 Oct 26: 43 from the Top order (every comment) and the 43 newest (43 different comments together, the whole set); 26,394 views and 393 likes that day. 3 of the 43 have 0 likes.

**Why it landed**
- First-hand weather: "My father ... lived at the foot of Shoe Creek which bellows straight into the (Big Piney) on the Amherst/Nelson line. My father was 11 years old at the time and said it was raining so hard that birds were drowning in the air, you couldn’t breathe unless you put your hand over your mouth." (27, 4 years ago). The same image, twice more: "Birds drowned in the trees and cows drowned out in the fields due to the air being replaced with water!" (7, 4 years ago).
- Gratitude to the trooper: "Thank you for your selfless service to your fellow humans. You are a gentleman and, I think, a poet at heart." (12, 5 years ago).
- Realness: "This film is as real as it gets. My older brother and his best friend volunteered on the body search parties" (10, 3 years ago, edited).
- Names: "Lost 2 cousins during this hurricane. (Jeffrey Wayne Oliver age 3, Regina Rena Oliver age 5 months)" (10, 4 years ago, edited); "My dad loat his first wife and child in the flood in Nelson. My sister was only 13 months old." (8, 5 years ago).

**Corrections and pushback**
- Coverage: "It's a shame National Geographic or Readers Digest didn't cover this in detail at the time; they sure blew that opportunity to cover a "once in a 1,000 year" flash flood event. You never hear about Hurricane Camille's visit to VA on the Weather Channel either." (9, 5 years ago).
- Missing credit: "It needs to be mentioned that in addition to Trooper Tinsley and Inspector Jones, Dr Criswell, the local dentist deserves a nod for his service in identifying many of the dead" (3, 5 months ago).
- Title: "Why the click bait title?" (0, 5 months ago).
- Unbelief: "I Really don’t believe This After 50 years I still don’t believe it" (7, 6 years ago).

**The newest 150** (here 43, 2 weeks to 7 years old)
- Still posted: "Living in Amherst County my entire life. The story of this is still talked about from generation to generation." (2, 2 months ago); "I was 3 yrs old" (0, 2 weeks ago).
- A trucker's son: "My daddy was a truck driver he was swept off a bridge and they found him 20 miles down river of the rockfish river.." (0, 2 months ago). The same bridge-and-trucks story appears under VPM.

**What they add or ask for**
- More than the aftermath: "This is great, but only shows the aftermath. There are some excellent books that make you feel like you're literally there" (8, 6 years ago).
- The people on duty: "The Circuit Court ordered a temporary morgue established in Lovingston, and since our rescue boat was out of action. we were asked to help in the refrigerator vans at the funeral home." (2, 5 months ago).
- Neighbours in other places: "Hurricane Camille was one of the strongest hurricanes to make landfall on the US mainland in history and ended with a historic flood in VA." (4, 5 years ago); "Wow. This was about as bad as the actual Hurricane that destroyed the Mississippi Coast." (4, 5 years ago).
- A viewer offers a place name: "I still live in roseland and would never leave. My grandfather was in Vietnam at the time Camille hit and lost most of his family in the tyro area." (5, 5 years ago, edited).

**For our scripts**
- The diary makes the video: viewers react to a named man doing a job (the trooper) and to bodies and families they know. Our script should carry named people on the record, not only numbers.
- Birds drowning in the rain is told by three families as a family story; check it before quoting anywhere (no source in these comments).

### "HURRICANE CAMILLE - 'A Lady Called Camille' | FULL Documentary" (Bright Enlightenment, extra general video)
https://www.youtube.com/watch?v=J49V7gQyaxU, uploaded 28 Mar 13 (27:01, channel 47,200 subscribers; appears to be the 1969 civil-defense film).
Pulled 21 Oct 26: 158 from the Top order (every comment) and the 150 newest (142 also in the Top pull, 166 different comments); 119,157 views and 929 likes that day. 50 of the 158 have 0 likes.

**Why it landed**
- The film itself is the story: "I was six years old when this storm happened. They sent a copy of this movie to grade schools for viewing and made every schoolkid in the country watch this movie over the next two years. It gave me nightmares for weeks. Thanks, Office of Civil Defense!" (49, 12 years ago).
- Its first-person Gulf Coast comments rank: "I, Mom, Dad and Sister lived thru hurricane Camille..." (51, 7 years ago); a family loss: "R.I.P. to my grandmother Margaret Hollins!!! She passed away in this hurricane in Pass Christian Mississippi!!!" (56, 4 years ago).
- The wording: ""But like any lady, perfectly capable to changing her mind" Well damn" (81, 9 years ago). Another: "She was no “Lady.”" (27, 8 years ago).

**Corrections and pushback**
- The hurricane party, both ways: "24 people went to party. only one made it out. That must of been one hell of a party." (5, 7 years ago) against "the truth about the hurricane party is that it never happened. ... Ben Duckworth one of the "party people" said the real story. they gathered there because it was a safe place, strong building." (3, 5 years ago).
- The count: "Those 23 people at that hurricane party found this out the hard way" (12, 7 years ago). The video says 24 in the building, 23 died.

**Virginia mentioned by viewers**
- "This storm is still talked about here in the Blue Ridge Mountains of Virginia, we lost many people in the floods and mudslides, a lot of which were never found." (37, 8 years ago).
- "My family drove to Rockbridge Co. in Virginia ... In Nelson Co. the whole side of a mountain washed down killing over a hundred people if memory serves." (16, 10 years ago).
- On warning: "The terrible truth is in Virginia, there was no warning. Without meaning to downplay the tragedy that hit Mississippi, people along the Gulf knew Camille was headed their way and had the authorities helping them to evacuate. Nelson County, Virginia had no warning." (4, 4 years ago, edited).
- Birds: "the super intense rains from Camille,drowned thousands of birds,where the perched in the trees." (29, 10 years ago).
- Arlington: "I remember when this storm hit Arlington Virginia near Washington, DC ... sweep away whole parking lots full of cars in a creek that was usually ankl" (0, 2 years ago).

**The newest 150** (here 150, 1 month to 7 years old)
- Present-day echoes: "This almost same exact scenario just happened with hurricane Helene." (0, 2 years ago); "Glad to hear that our hurricane paties are a long held tradition." (0, 2 years ago).

**What they add or ask for**
- "The amount of times New Orleans was shown they needed to reinforce the levees and yet Katrina still played out the way it did." (23, 5 years ago, edited).
- Wry notes: "More like just get the hell out as quickly as possible" (21, 7 years ago); "I feel so bad for the cow at 3:13." (21, 6 years ago).

**For our scripts**
- The 1969 film is where the 23-of-24 "party" number started, and viewers repeat it as fact. Our script does not take it from here.
- "The terrible truth is in Virginia, there was no warning." (4, 4 years ago, edited): a viewer already tells the contrast the angle wants (coast was warned, the mountains were not). Whether it holds is for the primary-source check; do not repeat it before then.

_Joplin 2011 episode research, 15 Oct 26: four more reference videos for the locked angle (sirens: belief vs record; 135 indoors, 0 below ground), plus our own old upload. Beat list per comment: the episode's devq page._

### "Joplin: The Worst-Case Tornado Scenario" (June First)
https://www.youtube.com/watch?v=syfeDcNgmL0, uploaded 22 May 26.
Pulled 15 Oct 26: 300 from the Top order and the 150 newest; 1,212,861 views and 16,388 likes that day.

**Why it landed**
- The top comment is a search-and-rescue account: "Im from Joplin. I was 19 when it hit, and worked search and rescue."
  (3,100, 4 months ago). No beat: no data point answers it.
- Viewers put themselves inside: "As soon as we closed the bathroom door, The Tornado was actively hitting our house."
  (907, 4 months ago).
- The fungus point is second-most liked: "So many healthcare providers are completely unaware of this risk." (1,500, 4
  months ago).
- Sirens as background noise: "I never once heard tornado sirens" (391, 4 months ago).
  "Tornado siren fatigue was wide spread in 2011." (79, 4 months ago).

**Corrections and pushback**
- Hospital foundation, two comments disagree: "the hospital was not shifted off it's foundation" (4, 4 months ago),
  against "the tornado rotated a part of the hospital 4 inches on its foundation." (2, 4 months ago). Verify before
  scripting.
- Death count: "I can’t believe the Joplin tornado, just one tornado, killed 161 people." (57, 4 months ago). Viewers
  say 161; our impact-death figure is lower.
- Store refuge: "every single person who chose to leave the stores instead of taking shelter died." (1,100, 4 months
  ago). Unchecked; it cuts against the refuge-area point.
- Street name: "that's Rangeline Road, one of the main streets in Joplin." (2, 4 months ago). Viewer says Rangeline
  Road, not "20th street".
- Butterfly people: "it was not butterflies, it was much worse." (3, 4 months ago).

**The newest 150**
- Still arriving with the toddler question: "DID THE TODDLER SURVIVE!?" (0, 2 weeks ago).
- Weekly tests: "not testing your sirens weekly is a huge takeaway here" (0, 2 months ago).
  "Testing an alarm once a week seems crazy to me." (0, 3 months ago).
- Codes: "Hospitals and shops without reinforced rooms." (0, 2 weeks ago).
- Basements: "wouldn't have BASEMENTS in tornado ally!" (0, 2 months ago).

**What they add or ask for**
- Shelters: "don't have mandatory shelters" (28, 4 months ago).
- Sound: "can we as a group decide of no siren ambience" (0, 3 months ago).
- Next topic: "Please do a video on the May 20th 2013 Moore OK EF5." (3, 4 months ago).

**For our scripts**
- Name one death count and say what it counts. "just one tornado, killed 161 people." (57, 4 months ago) will be quoted
  back.
- The hospital claims conflict. Check the source before the script takes a side:
  "the hospital was not shifted off it's foundation" (4, 4 months ago).
- The toddler and butterfly claims have no source in our list. They need one or they cut:
  "A toddler had his skin peeled away from around his neck" (1,200, 4 months ago).
- Keep the siren bed low under narration: "can we as a group decide of no siren ambience" (0, 3 months ago).

### "The 2011 Joplin EF5 Tornado - The Deadliest American Tornado In Over 50 Years" (Alferia)
https://www.youtube.com/watch?v=zMQd2F-GYiM, uploaded 14 Feb 24.
Pulled 15 Oct 26: 300 from the Top order and the 150 newest; 297,953 views and 6,934 likes that day.

**Why it landed**
- Survivor at the store: "I was in the 15th st Walmart. I remember it so well and I have PTSD severe anxiety ..."
  (415, 2 years ago).
- The chaser: "This was the first time I saw a storm chaser cry when he realised how many people had been killed in this storm"
  (1,000, 2 years ago).

**Corrections and pushback**
- Bettes: "is that he saw a dead body that was completely mangled" (18, 2 years ago).
- Deadliest: "Well Joplin is not the US most deadly tornado as the most deadly tornado is the tri-state tornado in 1925 ..."
  (2, 1 year ago).
- Count: "Were the fatalities 158 or 161? You can find both data and it's confusing" (1, 2 years ago).

**Sirens, warnings, basements (the most valuable)**
- "There had been so many warnings in the years past, many people just no longer thought anything would happen."
  (94, 2 years ago).
- "We didnt think anything of the sirens because of how many we had that month." (0, 2 years ago).
- "By the time the sirens went off it was already too late." (1, 2 years ago).
- "If it's a false alarm? Great, that's a blessing!" (0, 2 years ago).
- "Even you know it's real. If you can't get underground your in trouble." (1, 2 years ago).
- "My mom ushered my older brother and I into our basement. My dad ran to our neighbors’ houses who we knew didn’t have basements"
  (1, 2 years ago).
- "we used to normally go to st. john’s since we didn’t have any shelter to go to" (3, 2 years ago).
- "Nowadays, we have storm shelters that are designed to withstand a strong tornado such as Joplin."
  (0, 2 years ago).
- "It’s crazy to me how many people died despite taking the warning seriously and finding shelter."
  (0, 2 years ago).

**The newest 150** (149 viewer comments, 87 with 0 likes; 12 are months old, the rest a year or more)
- "Why do you have the tornado graphic and the name of the tornado blurred out?" (1, 6 months ago).
- "We have had 12 years of no EF5 which while good, disregards our ability to accurately determine windspeed."
  (1, 1 year ago).

**What they add or ask for**
- "I think it would be a good idea to give a brief description of the stuff like cape and sheer" (15, 2 years ago).
- "No mentions of the Butterfly People?" (6, 2 years ago).

**For our scripts** (mine)
- The siren belief is settled for viewers: "It was called the cry wolf factor." (94, 2 years ago). Answer it with the NIST figures.
- The blur is a live question: "It doesn't protect the victims" (1, 6 months ago). Decide it on purpose.

### "2011 Joplin EF5 Tornado: Unedited broadcast beginning 9 minutes before historic disaster" (Brad B)
https://www.youtube.com/watch?v=FagzNHuI5JI, uploaded 22 May 23. Pulled 15 Oct 26: 300 from the Top order and
the 150 newest; 1,636,849 views that day (likes hidden).

**Why it landed**
- Realisation on air: "You can hear the exact moment they realized how bad this actually was." (5,500, 3 years ago).
- Sirens under the cutoff: "...while sirens blare makes it even more so." (3,800, 3 years ago).
- The family in the house: "When the tornado hit we hid in our closet..." (267, 3 years ago).

**Corrections and pushback**
- Blame goes to the forecast:
  "All the Joplin-area stations were relying on the National Weather Service..." (2,000, 3 years ago).
- The warning belief: "Residents of Joplin had plenty of warning time." (1,800, 3 years ago). Answer it with the
  siren times.
- The lightning call:
  "...said the 1st power flash could've been from a lightning strike. It was not." (888, 3 years ago).
- Hospital time: "...struck St. John's Regional Medical Center at 5:41 PM." (26, 3 years ago). The poster adds
  "I can't be sure of this". Check it against our touchdown time.
- Speed disagrees: "...to monster tornado in about 2.2 secs." (23, 3 years ago), against
  "Literally 34 seconds from funnel to over a mile wide" (8, 2 years ago). Settle it from tower-cam frames.
- Death count disagrees: "It's terrible to think that 161 people are about to die." (14, 3 years ago), against
  "...the loss of 158 (maybe 161) souls." (8, 2 years ago). The script must say which count it means.

**The newest 150** (43 of the 150 have 0 likes; 47 also sit in the Top 300. The top one is pinned at 2,500 likes.)
- Pinned belief: "even the best of technology wouldnt have helped alert the people on time" (2,500, 2 years ago).
- Blame for the short notice: "Many blame local media (Weather) for the last minute notice." (423, 1 year ago).
- Sirens, first-hand: "i was 9 and had sirens going off, pitch black at around four pm." (0, 2 years ago).
- Basements: "If you're not underground." (0, 2 years ago).
- Silent broadcast: "...the radar and EAS alert on the bottom without any kind of voice..." (0, 2 years ago).

**What they add or ask for**
- Timestamps: "I really wish there were timestamps on this video." (3, 3 years ago).
- Other stations: "I wish somebody would upload KOAM's coverage of the tornado." (3, 2 years ago).
- Questions: "Was a tornado Emergency issued?" (19, 1 year ago), and
  "Not sure why they didn't look at the tower cam for their own visual confirmation sooner" (36, 3 years ago).

**For our scripts**
- Sirens and the broadcast carry it: "...while sirens blare makes it even more so." (3,800, 3 years ago). Give the
  sirens their own beat.
- The basement belief to answer: "her home didn’t really have a basement and she would have died..." (37, 3 years ago).

### "Joplin 15 Years Later", Parts 1 and 2 (The Weather Channel)
https://www.youtube.com/watch?v=4iGlOS8A0T4, uploaded 25 May 26 (Part 1)
https://www.youtube.com/watch?v=Leg98FOyIN0, uploaded 26 May 26 (Part 2)
Pulled 15 Oct 26: 90 comments in the Top order and 96 newest; 160,234 views that day (likes hidden), Part 1.
Pulled 15 Oct 26: 36 comments in the Top order and 36 newest; 59,483 views that day (likes hidden), Part 2.

**Why it landed**
- The rebuild account is the most-liked Part 2 comment: "I was directly hit by this tornado, Living just across
  from JHS. Catholic Charities helped us rebuild so we're still living here safe and sound." (59, 4 months ago).
- Viewers credit the presenter: "I really appreciate that they actually had Mike Bettes on this versus just some
  random narrator talking about it." (50, 4 months ago).
- Part 1's most-liked comment is about the subject itself: "Joplin documentaries are like 9/11 documentaries. No matter
  how many are made, you have to watch." (278, 4 months ago). Third is a chaser's account: "It was the first time I saw
  a professional storm chaser break down sobbing after finding bodies and realizing how serious this was" (116, 4
  months ago).

**Corrections and pushback**
- The hospital twist is the myth viewers call out: "It didn't rotate the hospital off it's foundation ..." (9, 4
  months ago), and "the false myth about the hospital moving and twisting off its foundation? False." (0, 4 months ago).
- The storm rating: "I say this absolute monster should have been categorized as an EF6." (10, 4 months ago).
- The track start: "Sorry but, he's wrong about ground 0." (3, 4 months ago).
- The timing: "It was 32 minutes not 38 minutes." (0, 3 months ago).

**The newest**
- "I can't fathom losing a quarter of my city." (1, 1 month ago).

**What they add or ask for**
- Series follow-up: "when is part 3?" (6, 4 months ago) under Part 2, and "Where is the rest of the show part 2, 3,4
  etc?" (4, 4 months ago) under Part 1.
- "Why didn't they issue a tornado emergency before the Joplin tornado hit the city?" (0, 4 months ago).
- "With Joplin being situated in the old lead belt, was the soil turned up by the tornado have high levels of lead."
  (1, 3 months ago).
- "and see people building houses with wood, why , if your gona build, build something thing to withstand a tornado"
  (0, 4 months ago).

**For our scripts** (mine)
- The hospital myth returns under Part 2, and under the June First and Domin Ator videos above. The hospital beat must say what twisted and what did not move, in one
  plain line, before the St. John's section.

### "The Deadliest U.S. Tornado Since 1950 — Joplin, 2011" (Paul Raymond, our own old upload)
https://www.youtube.com/watch?v=s--FjTUXU-w, uploaded 23 Aug 26. Pulled 15 Oct 26: 565 views and 11 likes that day.

**What viewers said**
- Nothing. The only 2 comments are ours (the pinned book link and "Do you know anyone who had experienced Joplin
  tornado? Please comment the experience.", both 0 likes, 1 month ago). Zero viewer comments on 565 views.

**For our scripts** (mine)
- The new Joplin video gives viewers something to answer back to: it quotes their own comments from the videos above.

_Next-topic review, 15 Oct 26 (Joplin, Missouri, 22 May 2011): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "The Worst Tornado Disaster in 70 years - The Joplin EF5" (Swegle Studios)
https://www.youtube.com/watch?v=bDrvj83MNJY, uploaded 17 Feb 25. Pulled 15 Oct 26: 300 from the Top order and the 150 newest; 3,534,264 views and 62,507 likes that day.

**Why it landed**
- The top comment is a personal link to the victim the video spotlights: "I was in Joplin the day of the F5. My friend Will Norton was killed that day. He was the one they were looking for who they eventually recovered in a body of water." (10,000 likes, 1 year ago). Next: "It really breaks my heart that that poor boy just graduated and had a future ahead of him, and passed away so tragically. Thanks for spotlighting the victims." (3,800, 1 year ago). Will Norton is named in 8 of the 300 top comments by word match.
- The live audio of people realizing: "Jesus, the realization of those newscasters when they finally see the tornado. Chills." (5,300, 1 year ago). "Hearing the Storm Chasers freak out has got to be the scariest thing ever." (3,600, 8 months ago). "Mike Bettes was emotional because he saw deceased victims. It shocked him and he still becomes emotional discussing that moment." (4,100, 1 year ago).
- Residents wrote testimonies: "My uncle survived Joplin... He couldn't even take deliveries into or near Joplin." (2,700, 1 year ago). "I survived at the IHOP." (845, 1 year ago). "A friend of mine was in the Pizza Hut cooler. His body was recovered in the middle of Range Line Road." (826, 1 year ago).
- Appetite for the subject: "Joplin documentaries are like 9/11 documentaries. No matter how many are made, you have to watch." (3,100, 1 year ago). "How many Joplin Tornado youtube documentaries have i watched? I've lost count. Will I watch another one? Yeah." (1,000, 1 year ago).
- The fungus detail hit: "The fungus is a such a sinister byproduct." (2,400, 1 year ago).

**Corrections and pushback**
- "Correction regarding St Johns... it didn't twist the foundation, it twisted the building itself as you went up." (169, 1 year ago).
- Overpass footage drew a safety correction: "In case you don't know: one of the worst spots to be during a tornado is under an overpass/bridge." (862, 1 year ago).
- A resident on sirens: "...people just didn't think there would be an actual tornado because we get sirens and alerts every spring and it only ever amounted to wind and hail." (202, 1 year ago).
- The script's own numbers were challenged: "At 20:34 you say the tornado was over a mile and a half wide, but then say it reached a peak width of one and a quarter mile at 23:40. Which is it?" (0, 3 months ago). "70 years was 1956 2011 was 15 years ago Check Google If You Want To" (0, 3 months ago).
- The Bible belt line drew pushback: "I definitely enjoy your content, but attributing the heroic actions of people to be in the Bible belt is just ridiculous." (2, 3 months ago).

**The newest 150 (3 days to 4 months old; the first entry is the creator's pinned sponsor comment at 639 likes, so 149 viewer comments)**
- 119 of the 150 have 0 likes. The highest viewer comment has 5.
- Presenter complaints, all 0 likes: "Man you gotta work on your face expressions, your videos are awesome but it looks like you're mocking the deceased every time you appear on screen" (9 days ago). "It's weird how happy you look discussing this" (3 months ago). On the voice: "Your voice audio sounds like ADR or has a weird tone like lacking room tone or has post effects added to it. It gives an uncanny valley feel." (3 weeks ago).
- Praise from late arrivals: "This is probably one of the best documentaries I’ve seen on YouTube." (1, 1 month ago). "Amazing video. One of my favorites for not trying to sensationalize things..." (0, 2 months ago).
- The butterfly-people story is mentioned in 8 of the 150 by word match, mostly as theories about skin.
- A viewer reads the story as a warning failure: "It's really hard not to sound blamey here and I absolutely don't want to blame the news reporters, but wow. I could not show you a more obvious violent wedge tornado." (0, 2 weeks ago).

**What they add or ask for**
- Topic lead: "Please do a video on the infamous Tri-State tornado! If so, please release it on March 18th, which is not only going to be the 100th year since its occurrence..." (238, 1 year ago).
- Plain asks: "Shouldn’t there be warnings way before it happens" (0, 3 months ago). "Why didn’t they have storm shelters in tornado alley? Makes no sense" (0, 2 months ago). "...for the meteorologists and storm chasers who end up finding victims like that on live TV, is there usually any kind of support afterward" (0, 13 days ago).

**For our scripts** (mine)
- Named victims and live audio carry this video. A presenter who looks or sounds wrong for the subject is attacked even
  under a 3.5 million view hit: our Paul shots need a grave face, and the voice must not sound processed.

### "Tornado Alley - Real Time Tornado: Joplin, Missouri" (Domin Ator)
https://www.youtube.com/watch?v=6nX7J8_mZpE, uploaded 1 Jan 18 (a TV documentary re-upload, 42.4 min). Pulled 15 Oct 26:
300 from the Top order and the 150 newest; 3,249,766 views and 26,724 likes that day.

**Why it landed**
- Strangers in the gas station: "Hearing complete strangers telling each other I love you and comforting each other was
  heartbreaking." (2,700 likes, 7 years ago); "the lady yelling "JESUS" at gas station literally sent chills through my
  body." (552, 8 years ago).
- The driver inside it: ""I'm in the tornado." "I'm in the tornado!" how the hell does someone drive right through an EF5
  and survive!?" (2,700, 7 years ago).
- The mother and baby: "The woman who had her baby ripped from her arms by the tornado has every drop of sympathy I
  have." (520, 7 years ago).
- The town afterwards: "By the way, Joplin is thriving as of now. They’re rebuilding prettier buildings, preparing more
  public tornado shelters" (3,600, 8 years ago).
- Survivors and helpers: "Survived this F5 with wood impaled in my leg" (1,600, 6 years ago); "I remember taking a bus
  from my High School from Chicago down to Joplin the next day to help out." (890, 6 years ago).

**Corrections and pushback**
- None liked. A building fact offered: "The hospital was moved something like 4-6 inches off its foundation by the tornado,
  if I recall correctly." (472, 4 years ago).

**The newest 150**
- Still found and rewatched: "been watching this same video since i was 9 years old" (0, 4 weeks ago); "I put "really
  really good Joplin tornado documentary under 1 hour" and yt didn't dissapoint" (0, 3 months ago).
- A warning question: "I don't know why they didn't issue a tornado emergency instead." (0, 3 months ago).

**What they add or ask for**
- "I cant help but to wonder why d  homeless or lower income people dont  get interviewed. I want to know there
  experience.  Did anyone give them shelter ?" (316, 7 years ago); "just Imagine the homeless people..." (308, 8 years
  ago).
- Off topic but liked: "Am I the only one who are scared of storms but always watch tornado videos???" (2,400, 7
  years ago).

**For our scripts**
- Who was left out of the story is asked for with 316 likes; nobody answers it here.

### "JOPLIN, MO, Tornado, 22 May 2011" (RODALCO2007)
https://www.youtube.com/watch?v=CburjPYmSdo, uploaded 17 Jun 11 (chase footage, 8.9 min). Pulled 15 Oct 26: 300 from the
Top order and the 150 newest; 1,811,899 views and 16,461 likes that day.

**Why it landed**
- The Home Depot line: "Talking about taking cover at 2:00 and said, "what about that Home Depot? Think that'd be a
  bad spot?" Yes. It was completely crushed." (1,500, 10 years ago); "Home Depot would NOT have been a good spot to take
  shelter. That place was flattened that day, and eight people died there." (1,100, 11 years ago). At least 5 of the
  top 15 are about the Home Depot.
- The last look at the old town: "this is the last you see of the old Joplin 10/15 minutes before it was all destroyed."
  (1,000, 5 years ago).

**Corrections and pushback**
- The audience's own explanation is that people ignored the sirens: "no one is paying any attention to the sirens going
  off. I can't believe how many people are..." (3,000, 12 years ago).
- A defence of the people on screen: "Saying "Its like no one cares!" Wasn't meant how some of you are taking it."
  (944, 12 years ago).

**The newest 150**
- A Portuguese viewer after the Netflix documentary: "com tantos alertas, pq a maioria dos habitantes não procurou um
  abrigo?" ("with so many alerts, why did most residents not look for shelter?") (0, 1 month ago).
- "I would say this is one of the most important videos ever uploaded to youtube" (0, 2 weeks ago).

**What they add or ask for**
- Survivors: "Survivor here, and honestly, the hardest part of that video for me is the beginning" (1,300, 14 years ago);
  a rescued dog: "I have a wonderful dog rescued from that tornado. It killed her family." (1,600, 2 years ago).

**For our scripts**
- Viewers believe the sirens were ignored and that the big stores were deathtraps; both beliefs sit on our candidates.

### "Devastating Joplin, Missouri EF-5 Tornado - May 22, 2011" (Reed Timmer)
https://www.youtube.com/watch?v=XT7CtF5ljxY, uploaded 23 May 11 (chase footage, 3.4 min). Pulled 15 Oct 26: 300 from the
Top order and the 150 newest; 4,279,142 views and 14,298 likes that day.

**Why it landed**
- How fast it grew: "It's freakish how it goes from a thin rope like tornado to very large wedge tornado in a matter of
  30 seconds." (2,600, 11 years ago); "What shocked me about the Joplin tornado is how FAST this thing formed." (1,600,
  12 years ago).
- Locals: "I graduated from joplin high that day and lost a few of my close friends to the tornado" (1,000, 15 years ago).

**Corrections and pushback**
- The audience is sure of the rating: "It literately took just under a single MINUTE for the tornado to go from EF-1 to
  EF-5." (832, 10 years ago).

**The newest 150**
- Small and fond: "There’s something particularly ominous about this tornado and the bluish hue to it" (0, 2 weeks ago).

**What they add or ask for**
- "Wow I always wondered why there wasn't really any video of the Joplin tornado "as it formed and strengthened into the
  monster it became"" (148, 4 years ago).

**For our scripts**
- The birth-of-the-tornado footage is famous and not ours to use; the story that it grew in under a minute is known.

### "Joplin Tornado: East Middle School Surveillance Footage" (JoplinGlobeVideo)
https://www.youtube.com/watch?v=64covicCcIY, uploaded 1 Jul 11 (5.4 min). Pulled 15 Oct 26: 300 from the Top order and
the 150 newest; 3,598,430 views and 14,895 likes that day.

**Why it landed**
- Mostly jokes, the top four all over 4,000 likes: "They got to make the school out of whatever the camera is made out
  of..." (5,700, 12 years ago).
- The hallway: "Into the halls they said its the safest place they said." (2,400, 10 years ago).
- Near miss: "Keep in mind the tornado didn’t even hit the school. All of that damage was caused by a simple near miss."
  (1,000, 8 years ago).

**Corrections and pushback**
- None liked.

**The newest 150**
- "This is exactly why you don’t go into the hallway during a tornado" (0, 4 months ago); a 2011 graduate: "That day we
  were graduating when we heard the tornado sirens blare" (1, 4 months ago).

**What they add or ask for**
- "Why don't schools in tornado alley have storm shelters? I'm sure $$$ has something to do with it, but they are our
  children!" (367, 6 years ago); "I wouldn't even want to know how many kids would have been killed had this happened
  during school season." (572, 11 years ago).

**For our scripts**
- Where people sheltered, and whether it held, is what viewers argue about under the most-watched Joplin footage.

_Next-topic review, 15 Oct 26 (Fargo, 20 June 1957): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "Fargo F5 - The Tornado That Changed Meteorology Forever" (CFproductions)
https://www.youtube.com/watch?v=LQXxbSiNqe4, uploaded 26 Sep 24. Pulled 15 Oct 26: 300 from the Top order and the 150
newest; 770,709 views and 14,481 likes that day.

**Why it landed**
- The two most liked comments are not about Fargo: "everybody gangster till the corn starts sweating" (1,800 likes,
  2 years ago) and "I experienced El Reno and that tornado completely showed us just how little we actually knew about
  tornadoes even today it's still being studied" (1,000, 2 years ago).
- Fujita is the hero: "The number of lives that Dr. Fujita has saved with his research is nothing short of
  incredible." (826, 1 year ago); "1 Japanese man saved so many American lives, I will forever be grateful for his work"
  (285, 1 year ago); "He should have gotten a nobel prize for that." (150, 1 year ago).
- Local witnesses: "I'm from the Golden Ridge. On the other side of the block from where I grew up there was a tree
  that had a horseshoe that was stuck in it from the tornado." (335, 1 year ago).

**Corrections and pushback**
- Corn sweat is the claim viewers fight, each pushback at 0 to 3 likes: "There was no corn in ND in 1957 fyi." (2,
  1 year ago); "I have a hard time believing the corn sweat theory. In those days they didn't grow near the corn they
  do today" (3, 1 year ago). The joke version is the most liked comment (1,800).
- Neighbours left out: "I feel a little disappointed that nobody ever mentions Moorhead, even though it is literally
  right next to Fargo." (0, 3 months ago).
- Style: "You talk to much, how about some action. Like Reed Timmer and Pecos Hank." (1, 3 months ago).

**The newest 150**
- Enderlin keeps coming up: "There was another one that hit enderlin last year June 20th 2025 68 years later on the
  exact same day that's pretty creepy" (0, 3 months ago).
- A photographer's grandson: "My grandfather Cal Olson took photos from that day when he worked from the Fargo Forum.
  I saw many many unseen photos of that day." (0, 3 months ago).

**What they add or ask for**
- "fun fact, this is the tornado featured on the cover art for Stevie Ray Vaughan's, "Couldn't Stand The Weather"
  album!" (0, 3 months ago).

**For our scripts**
- Fujita as a person carries this subject. Corn sweat is a claim to avoid or source tightly.

### "The Fargo F5 Tornado of 1957 - The Science Behind the Slow-Moving Monster" (weatherbox studios)
https://www.youtube.com/watch?v=w7o7xfEApWw, uploaded 21 Apr 23. Pulled 15 Oct 26: 300 from the Top order and the 150
newest; 601,330 views and 13,007 likes that day.

**Why it landed**
- Fujita again: "Never ceases to amaze me how ahead of his time Dr. Ted Fujita was, just incredible." (1,600, 3 years
  ago); "that Fujita report is insane and shows how one man's obsession can lead to great discovery" (778, 3 years ago).
- The photo triangulation as a way of telling it: "I love this way of telling the story, triangulating the photos with
  the locations as the storm tracked." (80, 3 years ago); "Those animations were incredible." (214, 3 years ago).
- Survivors and family links: "My uncle was a Fargo Tornado survivor." (492, 3 years ago); "My best friend's dad was
  Richard Shaw, the man carrying out one of the children who passed away." (75, 2 years ago).
- The human cost: "That picture was heartbreaking but I'm so glad you put it in. It's easy to get fascinated by these
  storms and forget the human cost." (24, 3 years ago).

**Corrections and pushback**
- The creator pinned his own corrections: "It's inevitable that after I put out a video, I find out I've gotten a few
  things wrong." (513, 3 years ago).

**The newest 150**
- Mostly thanks and memories: "I was 6 when this tornado passed 1 block south of my house on 10th street north."
  (0, 4 months ago); a repeat request: "Could you do the jackson Mississippi candle stick park tornado of 1966" (0,
  4 months ago).

**What they add or ask for**
- Topic leads, off Fargo: "I wonder if a video about days that are forcast to be big but bust would be interesting"
  (61, 3 years ago); "I would love to see your video analysis on the Jacks[on Candlestick Park tornado]" (53, 3 years
  ago); "I would love to see your analysis of the Jarrell TX Tornado" (43, 3 years ago); "1956 Comstock Park F5 and more
  importantly, the 1953 Flint-Beecher F5" (33, 3 years ago).
- The early warning, admired: "one hour early lead time...unheard of!" (53, 3 years ago).

**For our scripts**
- The hour of warning is already noticed as remarkable by viewers. What it was based on is not discussed.

### "Fargo: The F5 Tornado that Changed Everything" (June First)
https://www.youtube.com/watch?v=UzJ1ZXfYgjs, uploaded 22 Sep 24. Pulled 15 Oct 26: 300 from the Top order and the 150
newest; 183,079 views and 5,152 likes that day.

**Why it landed**
- "This Ted Fujita guy sounds pretty smart" (738, 2 years ago); the near-miss of the Nagasaki bomb is retold: "He was
  in Kokura, which was the city meant to take the second bomb" (202, 1 year ago).
- The Munson family: "That poor damned family. And what a way for the father to discover that nearly all his children
  died in the tornado." (284, 2 years ago); "Mercedes hearing her eldest's voice right before the tornado took six of
  her seven children away." (97, 2 years ago).
- The amount of film: "its honestly crazy that there is videos and this tornado happened 67 years ago." (317, 2 years
  ago).
- The photographer: "Cal Olson, took that photograph of Richard Shaw, 21, carrying the body of Jeanette Munson, 5"
  (54, 2 years ago).

**Corrections and pushback**
- Editing: "5:36 This transition is so abrupt and jarring. There's not even a real space for breath" (6, 11 months ago).

**The newest 150**
- Enderlin on the same date: "The fact that the Enderlin EF5 happened on the same day is nuts" (20, 1 year ago).

**What they add or ask for**
- "I'm gonna visit every place that was hit by F5/EF5 including Fargo" (25, 2 years ago).

**For our scripts**
- Leave room after a big reveal; viewers notice cuts that jump on.

_Next-topic review, 15 Oct 26 (Palm Sunday outbreak, 27 March 1994): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "Piedmont - The Most Evil Tornado in History" (weatherbox studios)
https://www.youtube.com/watch?v=1ol-0AI3DC4, uploaded 31 Oct 25, 14.1 min, channel 142,000 subs.
Pulled 15 Oct 26: 300 from the Top order and the 150 newest; 415,762 views and 10,122 likes that day. 129 of the newest 150 are also in the Top 300, so the pull holds 321 different comments. In the Top 300, 139 have 0 likes and only 34 have 10 or more.

**Why it landed**
- The most liked comment is a joke about the churches: "If you've ever been to Alabama, you know that it's a miracle this tornado only struck 5 churches" (1,600 likes, 11 months ago). Next: "Nobody steps on a church in my town! -Bill Murray" (262, 11 months ago). The church frame is what viewers carry away.
- Local TV memory: "It's crazy to think of the monsters that James Spann has been on air for. Saved many lives in his time. Absolute legend for sure" (734, 11 months ago); "I had to do a double take after seeing younger James Spann." (10).
- Archive material is praised: "I don't know where you dig up all the archival material you use, but it sure makes for compelling well-documented videos. Thank you. No IA crap on this channel." (17, 11 months ago).
- Three of the top six are about upload day, not the subject: "This week really is stacked with banger YouTuber weather documentaries." (468); "First Celton Henderson, then TornadoTRX, now WeatherBox!..." (258); "TRX and weatherbox on the same day, what a blessed day" (237).
- The room itself: "Those situations where a large gathering of people are in a single structure with only one wall separating them from the outside are a worst case scenario for tornadoes. Great video." (386, 11 months ago). The memorial lands: "That memorial is harrowing" (13); "13:49 Man, the sight of that memorial is just haunting." (5).
- A clergy member: "The story about Goshen UMC is one of my worst nightmares as clergy." (45, 11 months ago).
- The thumbnail photo: "The thumbnail (if genuine/not AI) is one of the most terrifying tornado photos I've ever seen" (11).
- The narrative style split the channel's own fans. Defence: "Being able to change up your style and knowing when to choose the appropriate style is a sign of an excellent creator." (78, 11 months ago). Attack: "I really think tornoda rtx style has overtaken this style. I much more prefer the more conversation style of older content." (13); "Is the darker atmosphere here to stay? I liked the energetic, passionate-sounding videos you uploaded before." (13); "you sound so dead inside, and where are the physical demonstrations?" (3).

**Corrections and pushback**
- The title. At least 15 comments object to "evil", counted by reading (a word match gives 32 of 321). "Tornadoes are not evil . They are weather. Stupid title" (2, 11 months ago); "An evil tornado? I have never heard of weather possessing intent" (1); "Nature is not evil nor is it good; those are human characteristics only." (3); "To call mother nature evil is wild work. We not gods here." (4). Even the jokes agree: "Me: "oh we really shouldn't moralize natural disasters by calling them evil..." Tornado: *utterly plows through 5 churches I stand corrected lol" (4).
- The "targeted churches" frame: "It's a bit misleading to present this as a tornado that somehow targeted churches. As it passed through each town, it destroyed everything, indiscriminately." (1, 11 months ago). The plain reason: "It was the timing that was the issue. Lots of churches get hit during the week, but nobody's there except maybe the pastor, janitor or secretary." (1); "A tornado only has to stay on the ground for 5 blocks, to hit 5 churches" (2).
- Lake City, which the video rated EF4 (10 comments name it): "Little Freudian slip on calling Lake City an EF4. It was an EF3 because it did not "sweep clean" the foundation of a well-built anchor bolted home." (32, 11 months ago); "I though lake city was an ef3 not ef4" (8); "Lake city was an EF3. Other than that great vid" (2). One goes the other way: "idk if you called Lake City an EF4 on purpose, but thanks for doing that because one of those homes could have easily been rated 170 and just wasnt" (1).
- Piedmont's own rating: "When did this get downgraded? It's was always an F5. I remember them saying it had 210mph winds if not mistaken." (0, 7 months ago). Against it: "Winds between 166MPH and 200MPH" (1).

- Protestants do not say Mass. 6 comments: "Just a note: Protestant congregations, including United Methodists, don't celebrate Mass." (1, 11 months ago); "Minor detail, but protestant church services are not called "mass"" (1, 7 months ago); "Mass isn't Baptist. Mass is Catholic." (1, 3 months ago).
- Holy Week wording: "7:24 this is incorrect and highly offensive to Christian." (1, 8 months ago).
- Naming: "You might consider adding AL to the title to make it clear this video is about the tornado that hit a specific town named Piedmont, rather than the tornadoes that hit the Piedmont region of the Carolinas" (2). Six say they took it for El Reno-Piedmont 2011: "When I hear piedmont I think 2011, didn't know they were that unlucky" (42); "I thought this was the 2011 El-Reno Piedmont tornado from the thumbnail" (6); "NOT ME THINKING THIS WAS EL RENO PIEDMONT 2011 EF5 UNTIL I SAW THE YEAR" (0, 3 months ago).
- "It's pronounced Gill-ee-ad" (0, 3 months ago). No comment disputes the Goshen facts (time, deaths, building).

**The newest 150 (1 day to 11 months old; apart from the 93-like pinned sponsor read, the top viewer comment is 48 likes)**
- The video is quiet now: 28 of the 150 are 11 months old, 1 is a day old.
- The title complaint continues: "Tornados are not evil. They are weather. Otherwise, great video!" (0, 2 months ago); "How can a tornado be "evil?"" (0, 6 months ago).
- Religion is the loudest theme, 39 of 321 by a word match, none above 20 likes. Both camps: "Ngl if you're at church during a tornado you kinda deserve to die for being a stupid brainwashed cultist" (0, 6 months ago); "As a follower of Christ I really think this tornado is prob a demonic attack" (0, 7 months ago). The most liked is an atheist veteran (20, 11 months ago).

- Ad anger, 13 by a word match: "Way too many ads to perceive as enjoyable!" (0, 5 months ago); "These paid ads are out of control, dude. It just screams 'greed'" (0, 6 months ago); "4:55 skips ad" (14, 11 months ago).
- Style: "Man, I miss the old '80s style of editing so much more unique." (0, 1 day ago); "i miss your synth in the opening" (0, 10 months ago).
- Late local memories: "I remember when this happened I was only 4 but I lived in Piedmont at the time. It destroyed my grandmothers home and 2 of our churches." (0, 3 months ago).

**What they add or ask for**
- First-hand accounts, the strongest material. A Piedmont native: "...my uncle Scott ran out to Goshen to help them uncover the rubble... it turns out she was the little girl my uncle pulled out." (48, 6 months ago). A rescuer: "I was on top of adderholt mountain on this day. I witnessed this tornado as it crossed highway 9 in Goshen, and I helped rescue the people that were in Goshen United Methodist Church." (0, 11 months ago). A neighbour: "My wife... and her 4 kids were in the church. They were all slightly injured but her youngest daughter was seated between two people who were killed." (2, 11 months ago).
- The warning gap: "1994 seems like just yesterday, but it might as well be ancient history. Today, everybody's cell phone would get an alert, and everyone would have gone to whatever safe space." (22, 11 months ago). Pushback: "I worry how accurate smart phone tornado alerts are at actually warning people when they need to be warned" (3); "with the recent defunding of the NWS, those phone alerts you mentioned might be less prominent" (1). Claims to check: "This tornado was the entire reason the small town of Piedmont installed tornado sirens." (1, 6 months ago); "The tragedy @ Goshen Methodist Church spurred the expansion of Weather Radio transmitters." (0, 11 months ago).

- Topic requests, 13 by my reading, none above 5 likes: "Can you do a video on Tanner Alabama and all the tornadoes that have ravaged it" (5); Havana 2019 EF4 (1); Raleigh 1988 F4 (1); Woodstock Ontario 1979 (1); Tri-State 1925 (1); Kalamazoo 1980 (0); Fritch TX 1992 (0); Lancaster TX 1995 (0); Rolling Fork 2023 (0).
- The 1965 link: "1965 and 1994 had Palm Sunday Tornado Outbreaks. This one you barely hear about. Great video on bringing it to light" (8, 11 months ago); "I can't believe there were two Palm Sunday tornado events, both involving places named Goshen." (3).
- Off topic but liked: "Seeing these chasers go into the trees with some of these storms always gets me a bit worried." (202, from a Skywarn spotter, 11 months ago); the Centralia mine fire from the sponsor read (25); "Where is the intro again... We need them!" (20).

**For our scripts**
- The audience arrives with the church frame. The honest correction (it did not target churches; people were there because it was Sunday morning) is already said by two viewers, with 1 and 2 likes.
- Local witnesses still read and write here. Facts must be right, and a rescue or survivor account is what viewers react to most.
- Do not write "mass". Do not rate comparison tornadoes without checking the survey. Do not give weather a will in the title.
- Pre-empt "which Piedmont": say Alabama in the title or thumbnail line.

---

### "1994 Alabama Palm Sunday Tornado - Part One" (ABC 33/40 Weather)
https://www.youtube.com/watch?v=JJID5zcr6MU, uploaded 27 Mar 09, 9.9 min, channel 40,000 subs.
Pulled 15 Oct 26: 15 from the Top order and the 16 newest (16 different comments together, the whole set); 24,387 views and 151 likes that day.

**Why it landed**
- Almost every comment is someone who was there. "Terrible day. I worked for an EMS service that day and we responded to Goshen. I will NEVER,NEVER NEVER forget what I saw and had to do that day." (17, 10 years ago); "I have an actual photo of this tornado as it hit." (7, 8 years ago).
- "This happened about two miles from where I grew up in Piedmont, Alabama. Love how the community came together when tragedy struck." (4, 6 years ago); "My great grandmother died from injuries she sustained in this tornado. My family lived in Dahlonega, GA at the time." (4, 2 years ago).
- The survivor on camera: "so strong kelly brave mom" (1) and "5:00 Irish Appalachian redhead survivor very courageous" (1), both 6 years ago.

**Corrections and pushback**
- No fact is disputed. The pushback is about the woman pastor: "God DID NOT ordain women to lead, pastor or guide a church body. It is not Biblical at all!!" (1, 3 years ago). The same point under weatherbox: "Really? Female Pastor" (1, 11 months ago).

**The newest 150 (here 16, aged 2 to 10 years)**
- Dormant: the newest comment is 2 years old. "25 years later they were to have a remembrance of this, but it was canceled due to the palm Sunday 2019 tornado storms." (1, 3 years ago).

**What they add or ask for**
- The viewer's own cause: "It's a tragedy that could have been prevented. If they had a NOAA Weather Radio." (6, 7 years ago).
- Era: "NO Social Media, NO Smartphones, but Windows 95, and Internet were a Year away." (1, 3 years ago).
- Faith: "It's stuff like this that makes me wonder why God didn't warn or protect His people." (0, 2 years ago).

**For our scripts**
- Rescuers, responders and the survivor on camera are what viewers answer. The weather radio gap is a cause they name unprompted.

---

### "WHNT Coverage of Palm Sunday Tornadoes - 3/27/94" (Bamawxcom)
https://www.youtube.com/watch?v=SYWgc0ItA6w, uploaded 27 Mar 14, 68.2 min, channel 8,290 subs.
Pulled 15 Oct 26: 18 from the Top order and the 19 newest (19 different comments together, the whole set); 18,452 views and 123 likes that day.

**Why it landed**
- Viewers love the sound and look of live 1994 TV: "RIP Myke Motley :( I watched this coverage live while dispatching rescue in Fyffe, Alabama. So long ago." (19, 8 years ago); "02:47 WHOA! That's a sound that I haven't heard in decades!" (12, 6 years ago); "Especially when you hear the printer going off, you know that's the NWS office giving out more watches and warnings." (11, 10 years ago); "LOVED the GTE/Weather Wire set-up on these days!" (5, 8 years ago).

**Corrections and pushback**
- No factual dispute. A figure: "The tornado on this day that destroyed the church in Piedmont, AL, killing 20 people, was the one that convinced me to reject christianity." (2, 5 years ago). A slip: "...was an Easter Sunday 1994" (2, 5 years ago); it was Palm Sunday.

**The newest 150 (here 19, aged 9 months to 12 years)**
- Dormant. Newest: "I don't see how they can tell a tornado by radar . Looks like rain in today's radar imagery." (0, 9 months ago); "What the hell is wrong with the sound cutting out so bad??" (0, 1 year ago).

**What they add or ask for**
- The outbreak was long: "Lived through these storms in Coosa Ga. Came in three waves. Around noon, late afternoon, then the final round at night. To this day the most frightening day of my life weather wise." (2, 2 years ago).
- 1965 comparison: "This didn't seem as bad as the one in 1965 that one was devastating, but still, any tornado can be destructive and deadly" (1, 1 year ago).
- Off topic: a political rant about the 90s (4, 6 years ago).

**For our scripts**
- Period sounds (the wire printer, the alert tone) are what viewers remember. Rights to this broadcast were not checked.
- "How can radar see a tornado" is a one-line explainer a 1994 story can answer.

---

_Next-topic review, 15 Oct 26 (Lubbock, Texas, 11 May 1970): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "Winds of Change | The Catastrophic 1970 Lubbock Texas F5 Tornado" (Carly Anna WX)
https://www.youtube.com/watch?v=8VPDTiE7uj8, uploaded 01 Dec 23. Pulled 15 Oct 26: 300 from the Top order and the 150 newest; 151,727 views and 4,575 likes that day. 29.4 min, 72,100 subscribers.

**Why it landed**
- The viewers are mostly Lubbock people and their families, and they say it got their story right. 86 of the 300 are first-person or family accounts (word match, after reading). "Everything you spoke on was 100% accurate!" (2 likes, 2 years ago). "This is the best description, from start to finish, of this tornado." (3 likes, 1 year ago).
- Restraint is praised: "I thoroughly appreciate the documentary style of approach to these videos. No extra drama or hyperbole, just facts with sources cited in easily processable segments." (4 likes, 2 years ago).
- The top comment is not about Lubbock: "These videos are immensely therapeutic in the healing of PTSD and survivors guilt that I battle." (387 likes, 2 years ago). The channel's loyal audience drives the likes, so they are a weak measure of Lubbock demand. Many comments are about the presenter's hair.
- Lubbock is a story its own people say is rarely told: "I rarely ever see it discussed so thank you for discussing this piece of history from my hometown." (13 likes, 2 years ago). "The Lubbock tornado seems to be the forgotten tornado. I figure because it happened at night & there is no video of it." (1 like, 2 years ago). Outsiders: "I travel from Amarillo to Lubbock every few months and did not know about this event." (4 likes, 2 years ago).

**Corrections and pushback**
- Fujita's term: `*"suction spots" If you're going to try and understand the work of a genius like Dr Fujita, please at least do him the courtesy of quoting him correctly.` (1 like, 2 years ago). Our c2 quotes NWS as "path of suction spots".
- A structural claim drew a rebuke: "You young lady, are NOT a Structural Engineer...STOP with ridiculous opinions, which is how all theses conspiracy theories get started." (2 likes, 2 years ago). It does not say which line. My reading: the Great Plains Life Building segment (the transcript has "concerned about that structurally" near 24:55). Another viewer: "I’ll give you an Oklahoma guarantee that if that building didn’t fall Monday night it never will." (1 like, 1 year ago).
- Sirens, two versions. "Little did I know that during the 1970 tornado Lubbock had sirens which failed due to the power actually being knocked out by the tornado." (3 likes, 2 years ago). Another local: "As a kid I observed tornado sirens at all the fire stations; however, none were operational." (92 likes, 2 years ago).
- Hostile or minor: "Are you always so dramatic?" (0 likes, 2 years ago); "The commercials are really excessive." (0, 2 years ago); "its not Lubbic its Lubbock, I'm from there and I can't stand to hear you people say it wrong, can't watch this" (0, 3 months ago). One conspiracy line: "I wonder if it was an experiment with “ new” technology. ???" (1 like, 1 year ago).

**The newest 150 (12 days to 2 years old; 144 of 150 also in the Top pull)**
- Little is new: Lubbock family memories ("I was working at Oakwood Lanes (about 30th st &Slide Rd.) that night." 3 likes, 4 months ago) and F6 drift ("bro was so surreal fujita himself rated bro an f6", 0 likes, 12 days ago).
- Lubbock people compare any big storm to this one: "A few days ago, June 5th 2025, we had a massive wedge tornado, probably the same size as this one." (1 like, 1 year ago).

**What they add or ask for**
- Family stories with names are the most liked Lubbock material. A student carried "the body of a woman who had been crushed by a pickup dropped on her by the storm" (182 likes, 2 years ago). A grandfather caught north of town, and a family looking for his body at the Winchester Theater (268 likes, 2 years ago). "I was 3 years old… I remember the man yelling on the radio…" (44 likes, 2 years ago).
- A named person who lost their life: "@16:02 Youll see “Woman crushed to death under pickup truck by storm while attempt - to reach storm shelter. That was was Estefana Guajardo Paez. She is my dads grandma." (9 likes, 9 months ago). "I had 5 cousins killed in this one." (8 likes, 2 years ago).
- The barrio: "it hit downtown, the campus area, the barrio, the country club area, and industrial areas" (17 likes, 2 years ago).
- Unanswered questions:
  - "The lack of a severe thunderstorm or tornado watch puzzles me as well." (13 likes, 2 years ago).
  - "Always wondered why officials waited so long to activate the sirens. They should've done that when the first tornado warning went out." (1 like, 2 years ago).
  - "what was the cape for this storm?" (0, 2 years ago).
  - "Are there any existing TV or radio broadcasts from this event?" (0, 2 years ago).
  - "I wonder if the policemen who drove in front of the tornado to warn the people made it out ok?" (0, 2 years ago).
- A chaser's lead: "To this day there's some debate on what the final ingredient was that triggered a couple of extremely intense thunderstorms on what looked like a quiet weather day" (4 likes, 2 years ago).
- Other-storm requests, all small: Antlers 1945 (17 likes), Waco 1953 (17 likes, the same comment as the barrio line), Panhandle 8 June 1995 (2), Red River Valley 1979 (1), Saragosa 1987 (0).
- "14:45 "no looting was reported." snert" (14 likes, 2 years ago).

**For our scripts**
- The viewers know the streets, the barrio and the buildings, and a wrong detail will draw a local correction.
- Two questions are asked by name and answered in no video here: why no watch (13 likes), and why the sirens waited (1 like). Both sit inside c3 and c6.
- Locals tell the siren story two different ways, so our script must state which, with the survey report rule.
- A named person who lost their life is already in the comments, and the family is watching.

---

### "The Lubbock 1970 F5 Tornado Documentary" (NWSLubbock)
https://www.youtube.com/watch?v=CDVtXl5eN1k, uploaded 05 Sep 13. Pulled 15 Oct 26: 123 from the Top order and the 130 newest; 142,902 views and 1,177 likes that day. 12.8 min, 1,240 subscribers. The Top pull has 123 because that is all the video has.

**Why it landed**
- It landed with people who lived it. The top comment is the best single source in the subject: "I'm a local amateur historian and survivor of the storm. I was RIGHT IN THE MIDDLE of that tornado running for cover." (102 likes, 9 years ago). It gives:
  - the street (Ave. M between 7th and 8th);
  - the boarding-house cellar;
  - "At the time, we didn't know ANYWONE had died";
  - "I remember the smell of burnt fireworks everywhere";
  - "There was a helicopter upside down in the middle of the street";
  - troops by nightfall;
  - the aftermath: "the city used the Imminent Domain law to secure our home, tear down the entire neighborhood and build the Civic Center."
- The archive material carries it: "the photos and data are priceless" (0 likes, 12 years ago). 35 of 123 are first-person memories (word match, after reading).

**Corrections and pushback**
- The death count, same top comment: "26 people were killed, not the 28 reported in the video." (102 likes, 9 years ago). It adds "The storm was classified as an F5 tornado after the fact and an EF5 in 2007."
- Voice is the dominant complaint, about 32 of 123 (word match, after reading), for 12 years. "did Hank Hill narrate this?" (96 likes, 9 years ago). "I didn't know Hank Hill was a weather fanatic." (45, 8 years ago). "A computer voice with a Southern accent?" (23, 8 years ago). "How about using a "real" person and not a computer!" (13, 10 years ago). This year: "Robby the robot, can't watch this ai robot production, I'm blocking this channel" (0, 3 months ago) and "The narration of this video is a bit monotoned. Basically terrible." (0, 5 days ago). The voice was a real person ("I know the guy who narrates this", 8 likes, 11 years ago), and it is still read as a machine.
- Anachronism: "Is anyone going to point out that the kids are playing soccer on the fields north of the loop that were built on the rubble from the tornado? Or the wind generatoor that hadn't been invented yet?" (0 likes, 1 month ago).
- "Chart of the so-called "Tornado Alley" @1:50 must be a joke... That's not even half of tornado alley!" (0, 5 years ago). "lol... was not an F5." (0, 7 years ago).
- Looting, the opposite of the other video: "I remember lots of stereo equipment being sold out of the back of vans in Amarillo, after this tornado.  I assume from people who looted damaged stores.  I hate looters." (4 likes, 9 years ago).
- "Lol “exceptional air quality”? Lived there for 5 years the air is at least 25 percent dirt." (26 likes, 7 years ago).

**The newest 150 (here 130, 5 days to 12 years old; 123 of 130 also in the Top pull)**
- New ones are more voice complaints ("omg the narrator makes this video un-watchable.", 1 like, 8 years ago), one ad, the Tornado Alley chart point, and family memories ("A couch went flying by in the street, then a car rolled by, then uprooted trees.", 0 likes, 2 months ago).

**What they add or ask for**
- Local follow-ups:
  - Civic Center, Buddy Holly Hall, Mahon Library, the new airport, and the old terminal that became the Silent Wings Museum (all from the 102-like comment).
  - "The hills that make up the Windmill museum use a lot of debris from this tornado as the base to build them up" (0, 2 years ago).
- "Wait, they said back in 1970 that it was three tornado's that formed into the F5 that hit Lubbock." (4 likes, 8 years ago).
- Warning words: "I have to explain the difference between a watch and warning, all the time! Some people think a watch means they are watching a tornado...lol" (10 likes, 11 years ago). This touches c6.
- People who left by car: "He drove around trying to avoid the path of the tornado. I know this is not a safe thing to do, however, we didn't have a storm shelter, so he did what he thought best." (52 likes, 7 years ago).
- "Anyone know the background music used in the beginning? It's beautiful." (0, 8 years ago).
- Off topic but liked: "my mom had a 5 dollar bill on her night stand...untouched.....creepy" (3 likes, 5 years ago).

**For our scripts**
- The 26 versus 28 dispute sits on the first comment anyone reads (102 likes). We must pick a number and name its source.
- Do not say it was "rated F5 at the time".
- A flat or synthetic-sounding voice is attacked here for 12 years, and ours would be exposed to the same complaint.
- No modern B-roll in a 1970 scene.

---

### "Only Two Tornadoes That Fujita Himself Gave a Preliminary F6 Rating - Lubbock, Texas and Xenia, Ohio" (Deadliest Disasters)
https://www.youtube.com/watch?v=xsKfpUwSuy4, uploaded 16 Apr 25. Pulled 15 Oct 26: 111 from the Top order and the 112 newest; 80,589 views and 1,686 likes that day. 14.1 min, 5,210 subscribers.

**Why it landed**
- It landed as a debate. 36 of the 111 mention F6 or EF6 (word match, after reading), and viewers add their own candidates.
- The Fujita biography surprised people: "WOAH!!!  The man who invented the tornado scale first studied Hiroshima and Nagasaki?!?!?" (37 likes, 6 months ago). "I would have loved to have met and had a chance to chat with Dr. Fujita- I think he would have been fascinating to talk with." (36, 4 months ago).

**Corrections and pushback**
- "Only two" is contradicted by the next two most-liked comments: "Dr. Fujita also considered the April 1977 Smithfield (Birmingham), AL F5 as an F6." (65 likes, 5 months ago) and "He also said it about 1974 Guin. My aunt lost her house in that one" (61, 5 months ago).
- The opposite camp, all 0 likes: "There is no F6." (3 months ago); "CLICK BAIT GARBAGE..... THERE IS NO EF6" (3 months ago); "This is fake news" (4 months ago). A better-argued one: "He never added a 6 to the Fujita scale and abandoned the idea anyway." (1 like, 4 months ago).
- A local corrects Lubbock: "I have lived in Lubbock since 74. What most people don't know is that night  Lubbock was hit by a F4 tornado shortly before the F5 ripped through the north part of town. There is a monument in town that shows the path of each one of these." (28 likes, 4 months ago).
- "The photo in that newspaper clipping is not the Lubbock tornado." (4 likes, 6 months ago).
- "lubbock tornado was only 1.5 miles wide but had winds of 318 mph and possibly little higher in it" (38 likes, 4 months ago).
- Pushback on Lubbock's importance: "I gotta be honest... i never really got why storms like Xenia, Lubbock, Pampa, Piedmont/El Reno, and Jordan get all this notoriety." (3 likes, 4 months ago).
- Voice, small: "I loved the video and it had great fascinating information but the monotone voice killed me." (4 likes, 4 months ago); "Snored to death." (4, 4 months ago).

**The newest 150 (here 112, 8 days to 1 year old; 111 of 112 also in the Top pull)**
- The new ones keep adding to the F6 list: "So, reading all of these comments, it appears that as many as 6 tornadoes were either rated or seriously considered for an F6 rating!" (2 likes, 8 days ago).

**What they add or ask for**
- F6 candidates: "The Jarrel F5 in 1997 would be another contender." (178 likes, 6 months ago), Bridge Creek-Moore 1999 (24), Smithville 2011 (7), Tri-State 1925 (9), El Reno 2013 (12 and 9).
- "I wonder how Dr Fujita would rank some of the biggest tornadoes we've had since his passing?" (48 likes, 5 months ago).
- A Lubbock detail: "Looking at the Lubbock storm's abrupt left turn, then a full swing around to again move in the original general direction, some people were lucky, some thought they were, but then..." (15 likes, 5 months ago). "these abrupt changes in direction and intensity may be explained as the paths of the suction vortices" (2, 4 months ago). Source question: "Where do you get that paper that has the cyclone forming image?" (1, 2 months ago).
- Off topic but liked: Jarrell (178), the Guin aunt (61), Hiroshima (37).

**For our scripts**
- "Only two" is not safe: it was corrected within the two most-liked replies (65 and 61 likes). Say "two of the best known" or leave the count out.
- The F6 argument is the biggest pull in the subject and also the oldest story for these viewers. The ruled-out list already says we do not lead with it.
- A viewer ties the left turn to the vortices, which supports showing what happened inside the tornado.

---

_Next-topic review, 15 Oct 26 (Woodward, Oklahoma, 9 April 1947): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "It Came Without Warning | The Deadliest Tornado Oklahoma Ever Saw" (Carly Anna WX)
https://www.youtube.com/watch?v=OE_7raGTzhE, uploaded 11 Jan 26 (24.6 min). Pulled 15 Oct 26: 222 from the Top order and the 150 newest; 28,848 views and 2,491 likes that day. Of the 222 Top comments, 138 have 0 likes.

**Why it landed**
- It landed as a return of the channel more than as a story. The most liked comment: "I'm glad you are continuing to produce these videos. I really like the way you cover these events. You have a unique style that is refreshing." (171 likes, 9 months ago). Next: "we are so back" (132). By a word match after reading, 95 of the 222 Top and 56 of the 150 newest are welcome-back, voice, hair or cat comments.
- The human angle is the most liked comment about the content: "I love the human element you highlight in these videos. Gives me hope that someday we can and will return to this level of empathy we had long ago." (81, 9 months ago). Echoed by "I love how you include the positive showing how people pull together and rebuild." (0, 9 months).
- The topic is under-covered, and viewers say so: "Glad to see you uploading again, this one is a bit overlooked in the history of violent tornadoes." (73, 9 months ago); "I live in Woodward, thanks for covering this because there really isnt as much content about this as you would think there should be" (40, 9 months ago); "The Woodward tornado never really gets any attention" (7, 9 months). Also "I was born and raised in Oklahoma City and this is the first time I've ever heard anything about this tornado" (0, 9 months).
- The survivor recording is noticed: "Thank you for including the survivor recording." (4, 9 months).
- No viewer attacks the title.

**Corrections and pushback**
- No liked factual correction. Small unliked ones: "you have 'Agnes tried to call her husband who usually visited the diner she wored at.' I think you mean 'Worked'" (0, 8 months); "IT might be the deadliest but it's not the most destructive 1999 more OKC holds that record" (0, 9 months); "I'm a little confused. I thought Glazier TX was wiped out and the only thing left now is a concrete jail." (0, 9 months).
- A doubter of "no warning": "No warning huh? So the skies where clear and the tornado appeared out of nothing? I don't think so...." (0, 8 months).
- Against the padding: "How to turn a 5 minute video in to 25....just tell and show the story of the tornado. No need for town and peoples background story." (0, 4 months). It is outweighed by the 81-like praise for the human element.
- On delivery: "Its extremely difficult to listen to your narration because how you read ....but you are extremely smart" (0, 9 months).

**The newest 150 (1 to 9 months old, nothing above 20 likes)**
- The video is only 9 months old, so the newest list is mostly the same launch crowd. Late arrivals still post cat and welcome-back comments: "I watch for the subject of the videos, but I love seeing the kitties." (0, 1 month).
- Late discoveries: "Great upload. I have never heard of this awful storm." (0, 9 months).
- Family stories keep arriving: "My cousin died in this tornado... in 47, I was born in 73. The Grayson boy, was my great uncles son..." (0, 4 months); "Ambulance's couldn't get into town so a Dr and local pilots flew in and out taking people to the hospitals." (0, 3 months).

**What they add or ask for**
- Local knowledge: "K-101 did a great service to the community back in the late '80's documenting that story by interviewing the people that lived it. Almost all of those voices have since passed on" (12, 9 months). The same viewer says the theatres were playing "'Rage in Heaven' and 'Devils on Wheels'".
- Family accounts: "My grandpa was involved in the cleanup and recovery efforts for Woodward. He was only 17, but in the aftermath he saw a baby wrapped up in the spring of a car seat" (7, 9 months); "My grandpa lost 2 of sisters, Darla and Arleta, and his mom Goldie due to this tornado." (1, 8 months). One viewer's father flew doctors in from Oklahoma City and "was involved with the man that flew to Washington DC and I believe it was the first time a city had petitioned Congress for emergency disaster aid." (0, 8 months).
- Agnes: "Agnes Giddens had a backbone of steel. After losing her home, husband, and son in Woodward, she rebuilt her life ... Unfortunately, that new home was in Udall, Kansas." (1, 9 months).
- Relief and neighbours: "man, 1947 had really good emergency response. tornado town is so much better than a coupon for a marriot" (21, 9 months); "being 'neighborly' was literally a survival strategy." (2, 9 months).

- Meteorology progress: "It is the stories of these older events that make you appreciate how far meteorology has come along." (10, 9 months); "the first (tornadic) hook echo was not identified on radar until 1953" (0, 8 months).
- Follow-ups asked for: "You should do the Great Plains Outbreak in May of 1955. One supercell spawned two nocturnal F5 tornadoes." (4, 9 months). Also the 1993 Colonial Heights Virginia tornado (0), the Belmond Iowa F5 (0, 3 months), Guin and McDonald Chapel Alabama (0), and Henryville Indiana (0).
- Off topic but liked: voice care, "honey, lemon juice and ginger ... Andy Serkis" (10, 9 months); "I want to do a video on storm anxiety, would love your help." (6, 9 months); tornado days versus snow days near Atlanta (7, 9 months).

**For our scripts**
- Under-coverage is a selling point with proof (73 and 40 likes).
- Viewers engage with named people and their afterlife (Agnes, the families, the pilots).
- The local and family details in comments are leads to check, not facts to use.

### "Tornado Town. 1947" (OHS Film and Video Archives)
https://www.youtube.com/watch?v=1S-dQ7s9ZnY, uploaded 13 Jun 12. Pulled 15 Oct 26: 20 from the Top order and the 22 newest (about 22 comments exist, so the lists are the same); 16,102 views and 149 likes that day. This is a 1947 film. Commenters are survivors and their families.

**Why it landed**
- Viewers come to say where they or their family were: "My mother was 10 years old when this happened. She and her friends were at the theater right before it hit." (8, 6 years ago); "That's my parents Chet & Lillie Tripp (Stricker) at tape position 5:40 or so." (4, 4 years ago).

**Corrections and pushback**
- The film's toll is disputed. "If you watched the whole of this film the film was wrong on number of deaths. A hundred twenty or more people in Woodward died, and altogether 220 people died in that tornado from Texas northeast." (7, 7 years ago, from someone who was nine that night). Another: "this tornado killed 181 (101 in Woodward) ... traversed 125 miles (they thought it was 220, but they found breaks in the path between Woodward and St. Leo, Kansas)" (8, 5 years ago).
- Film quality jokes: "Sounds like this film went thru a tornado!" (15, 9 years ago); "most horrible music I ever heard." (4, 11 years ago).

**The newest 150**
- There is no real newest list. The newest comment is "My grandpa was 17 at the time. He lost his mom and his 16 and 9yo sisters." (0, 1 year ago). Carly Anna's "Darla and Arleta, and his mom Goldie" (1, 8 months) may be the same family (my guess).

**What they add or ask for**
- A child's view: "we passed by Adams Brothers' Grocery which was being looted ... injured and dead laid out on the front lawn, there being no more room in the small hospital. Schools were damaged so bad the school term was cancelled" (11, 9 years ago); "the 28-bed hospital where bodies of dead, dying, and injured lay on the front yard." (7, 7 years ago).

- The Higgins cafe: "a woman lying in a ditch and she asked someone to give her daughter. She said, I know she's dead but would you still give her to me?" (7, 3 years ago).
- The Joan Croft case comes up unprompted: "this disaster is attached to one of the most creepy US mysteries of all time was the kidnaping of the little baby girl that was found after the tornado. The family never found that girl." (11, 6 years ago). The wording contradicts itself.
- Relief compared with today: "Today the Red Cross charges for services and you're lucky to get a blanket and coffee from them." (3, 3 years ago); "These days they would just give everybody obama care and a free phone." (5, 7 years ago). It matches the 21-like relief comment on Carly Anna's video.

**For our scripts**
- The scenes locals care about are the hospital lawn, the looting, and school in church basements. These comments are unsourced, so they are leads, not quotes.
- Handle the toll with care: the film and viewers disagree.

### "Lost in the Confusion: The Haunting Disappearance of Joan Croft | SERIOUSLY STRANGE #136" (Rob Gavagan)
https://www.youtube.com/watch?v=wYfR9D4ophI, uploaded 15 Jun 23 (10.3 min). Pulled 15 Oct 26: 139 from the Top order and the 150 newest; 96,931 views and 5,605 likes that day. A true-crime channel with 2.99M subscribers. It is the most watched video found on this subject. Read it as a reference only.

**Why it landed**
- The hook is the mystery, and viewers do the work. Top comment: "How is a child being taken from the hospital by two strangers not enough indication of a kidnapping to the FBI?" (460, 3 years ago). Next: "The two men walking in to ask for her by name makes me wonder if they were watching the family with the intent of kidnapping Joan before the tornado hit" (243); "I can't imagine what her sister went through. A 7 year old who is with her baby sister." (123).
- It reaches into present-day Woodward: "Joan Croft reports still come through till this day. Its just interesting how many old lady's believe it could be them. A friend of mine who works as a police officer where the Croft family lived has a photo of her hanging in the chief's office." (109); "I was born and raised in Woodward. When I was in the 7th grade, Unsolved Mysteries came to town and did a segment about her." (54).
- The tornado is the setting: "1.8.miles wide is an unfathomable monster of a tornado" (16); "Imagine surviving a tornado just to get kidnapped. Smh." (58). Viewers posted from live storms that day: "Well we are going to have severe storms tonight here in Oklahoma, so hopefully this video isn't some bad foreshadowing." (20).

**Corrections and pushback**
- "It's 'AMARILLO'. Not Armarillo." (0, 2 years ago).
- "It's weird they would go all the way from Woodward to Washington, OK. Woodward is way over in Northwest and Washington South of OKC. That's a nearly 3 hour drive." (2, 3 years ago).
- The accounts of the men differ: "In another video it was 3 men in military uniforms taking her to Oklahoma City." (0, 2 months).
- Channel complaints: "Remember when Seriously Strange was three bizarre little stories ... Now it's always murders and disappearances." (0, 3 years); "Hate the outro" (0, 3 years).

**The newest 150 (2 months to 3 years old, nothing new above 3 likes)**
- This is the same launch crowd. The channel's drop-off shows: "Where have you gone Rob Gavagan??" (2, 10 months); "I miss this channel so bad !!" (3, 11 months); "80k views in 1 year ? Fell off" (1, 2 years).
- By a word match after reading, about 19 of the 139 Top and 26 of the 150 newest mention kidnap, trafficking, the father, genealogy, the FBI or Unsolved Mysteries.

**What they add or ask for**
- Open questions: "I've got to wonder why they did not also take the older sister, Geraldine, especially when Joan was insisting that she wanted to stay with her sister. They specifically wanted THIS girl, for some reason." (64); "Why were they after the girl!? How did they know the girl!?" (9).
- Theories: "What if Joan's father wasn't her real father?" (37); the men "obviously went into the hospital with the intent to kidnap the child" (39). DNA: "I imagine with DNA testing and Ancestry, it would be possible nowadays to solve this mystery." (2); "Genealogy might be an option" (4).

**For our scripts**
- This is the strongest hook on the whole subject (460 likes, the highest in all three videos), and Woodward locals still know it.
- The facts differ by teller (two men or three, Washington or Oklahoma City). The case is unsolved, so there is no ending. This audience is true-crime, not weather.

_Next-topic review, 15 Oct 26 (Palm Sunday outbreak, 28 March 1920): reference videos for a candidate subject. The page summary per subject is in the research folder, not here._

### "A Terrible Tornado Outbreak In 1920" (The1920sChannel)
https://www.youtube.com/watch?v=FHRAAN5fixw, uploaded 20 Aug 26. Pulled 15 Oct 26: 10 from the Top order and the 10
newest (the video has 10 comments in all); 1,553 views and 144 likes that day.

**Why it landed (or did not)**
- Too few comments to say. The most liked is about the channel's music, not the storm: "What is your theme music
  called? I have always loved it" (5 likes, 1 month ago).
- The human details are what one viewer retold: "especially the man who had not just one but two stoves land right
  next to him. And how funny that one of the bodies was actually a mannequin!" (0 likes, 1 month ago).

**Corrections and pushback**
- None.

**The newest 150**
- The same 10 comments; the newest is 3 weeks old: "Bless Mr. Askew❤" (0 likes, 3 weeks ago).

**What they add or ask for**
- A social angle, unprompted: "even in disaster, segregation was enforced." (1 like, 1 month ago).
- A link to a later storm: "Palm Sunday indiana 1968 hit again ..." (1 like, 1 month ago). (My note: the second Palm
  Sunday outbreak was 1965, not 1968; the comment is the viewer's own.)
- No forecasting then: "They didn't have radar or satellite in those days, so they were at the mercy of the clouds"
  (1 like, 1 month ago).

**For our scripts**
- Named people and odd objects (the stoves, the mannequin, Mr. Askew) are what viewers repeat back.

### "Weather History: 1920 Palm Sunday Tornado Outbreak" (Pandavision Productions)
https://www.youtube.com/watch?v=oj9jfW97DBE, uploaded 14 Mar 14. Pulled 15 Oct 26: 3 comments in all; 3,204 views and
26 likes that day.

**Why it landed (or did not)**
- The one liked comment says the outbreak is forgotten next to 1925: "This is an often forgotten tornado outbreak. When
  people think of a tornado from the 1920's they think of the tri state tornado of 1925. They dont often think of the
  1920/03/28 tornado outbreak." (3 likes, 2 years ago).

**Corrections and pushback**
- A long objection to the video's Wizard of Oz line: "So, how can the grandiose final statement even be considered as
  factu[al]" (0 likes, 11 years ago).

**The newest 150**
- The same 3 comments.

**What they add or ask for**
- A local tie: "An F2 from this storm started just miles from the house I was born in." (0 likes, 1 year ago).

**For our scripts**
- Avoid pop-culture claims we cannot source (the Wizard of Oz line drew the only pushback).

### "Palm Sunday Tornado, Elgin Il.1920.f4v" (Phil Grindstone)
https://www.youtube.com/watch?v=e7YwJuik_m0, uploaded 3 Jun 11. Pulled 15 Oct 26: 3 comments in all; 2,475 views and 32
likes that day.

**Why it landed (or did not)**
- A survivor telling her own story is what the three comments thank: "i love this woman and her story." (1 like, 13
  years ago); "Love hearing her tell her story of that day and the photoes" (0 likes, 14 years ago).

**Corrections and pushback**
- None.

**The newest 150**
- The same 3 comments.

**What they add or ask for**
- Nothing beyond thanks.

**For our scripts**
- First-person survivor voice and old photographs carry this subject.

### "Everything We Thought About Titanic Was Wrong" (Today I Learned Science)
https://www.youtube.com/watch?v=s4ewZK0uIIA, uploaded 14 Apr 26. Pulled 7 Oct 26: 300 from the Top order and the
150 newest; 2,325,424 views and 46,773 likes that day. Ages below are as YouTube showed them on the pull date.
Teardown: `references/teardowns/2026-10-03-titanic-mirage.md`.

**Why it landed**
- Hand-made art is the most liked comment, above anything about the Titanic: "thank you for the amazing
  illustrations! It is a beautiful sight to see this effort amongst all the AI slop" (4,300 likes, 5 months ago).
  Also "the art made by artists to elevate it" (216) and "the same vibe as watching the history channel when i was
  a kid" (280).
- The concept came back in the viewers' own words: "everything just all fall into place, human error, technical
  error, environment condiiton and even bad luck... intersected perfectly" (2,800); "every little thing that
  could've gone wrong... ended up happening" (246, 2 months ago).
- The ending is carried by named small human moments: the man and his valet "really did go down as gentlemen"
  (2,100); "I literally got chills at the end. So many unnamed heroes" (1,700); the engineers keeping the light on
  (186, 142); the Lebanese family dancing dabke (120).
- Busting one common belief gets a "finally": "Finally... A video that acknowledges it wasn't the number of
  lifeboats, it was the time they had to launch them" (1,100).

**Corrections and pushback**
- Factual slips drew liked corrections: no double hull, only a double bottom (633, the 12th most liked comment of the
  pull, and 315); six compartments breached, not five (215); the lifeboat drill was not in dry dock (175); the ship
  broke between funnels 2 and 3 (81); what CQD stands for (52); Captain Smith's record was not "without incident" (49).
- The title was called out at launch: "good video but i must have missed the part where everything we know is
  wrong" (159); "For a seasoned Titanic Enthusiast, nothing new here. The Mirage is not new information" (66); a
  676-like comment credits a documentary from a decade ago.

**The newest 150 (1 day to about 1 month old, no viewer comment above 2 likes)**
- The title complaint has not stopped: at least 7 of the 150. "What a weird clickbait title... 99% of what we know
  about Titanic is the same" (0 likes, 4 weeks ago); "Rename your bloody video. Click bait doesn't suit the
  excellent video this is" (0, 3 weeks ago); "What a bs title" (0, 3 weeks ago).
- Late arrivals accuse the script and the voice of being AI, although the art was praised as hand-made: "ChatGPT
  generated script combined with the influencer accent is a recipe for my ears to bleed" (0, 1 month ago); "Your
  script reeks of AI" (0, 1 month ago); "Why do you mispronounce words the way AI voiceovers do?" (0, 3 weeks ago).
- About 1 in 9 is a conspiracy claim (16 of 150 by a word match, after reading), none above 2 likes: "We all know JP Morgan
  intentionally put that iceberg there to collect the insurance" (0, 2 weeks ago).
- "The host repeatedly said the tragedy started months before Titanic sets sail. That is wrong and is plain
  sensationaliation" (0, 3 days ago).

**What they add or ask for**
- Viewers reward a fact they can add: stars vanishing on the horizon is how the lookout saw the iceberg (3,000);
  lifeboats were meant to ferry people to a nearby ship, not hold everyone (1,300 and 47).
- Follow-up angles they raise themselves: the sister ship Olympic's long career (143, 4 months ago); the
  Mackay-Bennett recovering the bodies (150); Carpathia's captain posting a lookout on the bow, below the haze (95).
- Off topic but liked: a navy veteran on fearing the sea at night (794); "today i learned i am more scared of the
  ocean now" (106). Personal fear of the hazard is what viewers want to talk about.
- Funnel: "Your shorts on Titanic hooked me" (382). The creator's own comment asks a question and names next week's
  video (653); the pinned comment is a partner promo (21). Releasing on the anniversary was noticed (216).

**For our scripts**
- The visible craft is the first thing praised. An AI-sounding script or voice still gets attacked months later
  (here in a few 0-like comments).
- A concept title needs one fact the enthusiast has not heard, or the comments keep saying so for months.
- A wrong technical detail draws a liked correction (633 here). The storm audience watched these events live.
