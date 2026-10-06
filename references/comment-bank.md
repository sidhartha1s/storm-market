# Comment bank: what viewers say under reference videos

**Rule (owner, 6 Oct 26).** Every reference video gets its comments analysed, whoever picked it (the owner or the
agent) and whatever it is a reference for (script, topic, thumbnail, edit). The findings are added to this file, so
the bank grows and the writer reads it before every script. A reference video with no entry here is unfinished research.

## How to pull and read
1. Pull twice, into a scratch folder (never the repo): most liked, then newest.
   ```
   yt-dlp --skip-download --write-comments --write-info-json --extractor-args "youtube:comment_sort=top;max_comments=300,300,0,0" -o "<dir>/top/%(id)s" <url>
   yt-dlp --skip-download --write-comments --write-info-json --extractor-args "youtube:comment_sort=new;max_comments=150,150,0,0" -o "<dir>/new/%(id)s" <url>
   ```
   The comments land in `<id>.info.json` under `comments` (`text`, `like_count`, `timestamp`, `parent`). yt-dlp
   reads YouTube's "5 months ago", so a date is good to the month, not the day.
2. Read both lists yourself: the most liked first, then the newest with their dates. No keyword script: what a
   comment means is a judgment.
3. Write the entry below. Quote the comment and give its likes; a finding with no quoted comment does not go in.

## What to look for
- **Did the video land, and why.** What viewers praise or attack: the art, the voice, the ending, the title.
- **What they wanted to see.** Requests, follow-up angles, "you missed X".
- **Suggestions and corrections.** A correction with hundreds of likes is a fact our script must get right.
- **High-like comments that are off the video's topic.** A viewer asking for x, y, z with 200 likes under an El Reno
  video is a topic lead for us even though it says nothing about El Reno. Keep it.
- **Dates.** Old top comments show the launch audience; the newest show who still arrives and what they say now.

## Entries, newest first

### "Everything We Thought About Titanic Was Wrong" (Today I Learned Science)
https://www.youtube.com/watch?v=s4ewZK0uIIA. Pulled 7 Oct 26: the 300 most liked and the 150 newest; 2,325,424 views
and 46,773 likes that day. Teardown: `references/teardowns/2026-10-03-titanic-mirage.md`.

**Why it landed**
- Hand-made art is the top comment, above anything about the Titanic: "thank you for the amazing illustrations! It is
  a beautiful sight to see this effort amongst all the AI slop" (4,300 likes, May 26). Also "the art made by artists
  to elevate it" (216) and "the same vibe as watching the history channel when i was a kid" (280). A newest comment
  is just "Ai crap" (0 likes, Sep 26): viewers check for the AI look either way.
- The concept came back in the viewers' own words: "everything just all fall into place, human error, technical
  error, environment condition and even bad luck... intersected perfectly" (2,800); "every little thing that could've
  gone wrong... ended up happening" (246, Aug 26).
- The ending is carried by named small human moments: the man and his valet "really did go down as gentlemen"
  (2,100); "I literally got chills at the end. So many unnamed heroes" (1,700); the engineers keeping the light on
  (186, 142); the Lebanese family dancing dabke (120).
- Busting one common belief gets a "finally": "Finally... A video that acknowledges it wasn't the number of
  lifeboats, it was the time they had to launch them" (1,100).

**Corrections and pushback**
- Every factual slip became a liked thread: no double hull, only a double bottom (633 and 315); six compartments
  breached, not five (215); the lifeboat drill was not in dry dock (175); the ship broke between funnels 2 and 3
  (81); what CQD stands for (52); Captain Smith's record was not "without incident" (49).
- The title was called out: "good video but i must have missed the part where everything we know is wrong" (159);
  "For a seasoned Titanic Enthusiast, nothing new here. The Mirage is not new information" (66); a 676-like comment
  credits a documentary from a decade ago.
- Newest, Oct 26: "The host repeatedly said the tragedy started months before Titanic sets sail. That is wrong and
  is plain sensationalisation" (0 likes).

**What they add or ask for**
- Viewers reward a fact they can add: stars vanishing on the horizon is how the lookout saw the iceberg (3,000);
  lifeboats were meant to ferry people to a nearby ship, not hold everyone (1,300 and 47).
- Follow-up angles they raise themselves: the sister ship Olympic's long career (143, Jun 26); the Mackay-Bennett
  recovering the bodies (150); Carpathia's captain posting a lookout on the bow, below the haze (95).
- Off topic but liked: a navy veteran on fearing the sea at night (794); "today i learned i am more scared of the
  ocean now" (106). Personal fear of the hazard is what viewers want to talk about.
- Funnel: "Your shorts on Titanic hooked me" (382). The pinned creator comment asks a question and names next week's
  video (653). Releasing on the anniversary was noticed (216).
- The newest 150 (Sep and Oct 26) are mostly conspiracy claims (JP Morgan, the Olympic switch) and the binoculars-key
  myth, each at 0 or 1 like.

**For our scripts**
- The visible craft is the first thing praised, and the AI look is the first thing attacked.
- A concept title needs one fact the enthusiast has not heard, or the comments say so.
- One wrong technical detail becomes the top thread under the video. The storm audience watched these events live.
