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
   Titanic pull, 123 of the 300 had 0 likes). A sort is fine; a keyword filter is not, because what a comment means
   is a judgment.
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
`references/ep6-katrina/comment-insights-darkhorizon.md`, and the "Top comments" blocks in
`references/mini-storms/teardowns/README.md`.

## Entries, newest first

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

**The newest 150 (2 days to about 1 month old, none above 21 likes)**
- The title complaint has not stopped: at least 7 of the 150. "What a weird clickbait title... 99% of what we know
  about Titanic is the same" (0 likes, 4 weeks ago); "Rename your bloody video. Click bait doesn't suit the
  excellent video this is" (0, 3 weeks ago); "What a bs title" (0, 3 weeks ago).
- Late arrivals accuse the script and the voice of being AI, although the art was praised as hand-made: "ChatGPT
  generated script combined with the influencer accent is a recipe for my ears to bleed" (0, 1 month ago); "Your
  script reeks of AI" (0, 1 month ago); "Why do you mispronounce words the way AI voiceovers do?" (0, 3 weeks ago).
- About 1 in 8 is a conspiracy claim (16 of 150 by a word match), none above 2 likes: "We all know JP Morgan
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
- The visible craft is the first thing praised, and an AI-sounding script or voice is attacked months later.
- A concept title needs one fact the enthusiast has not heard, or the comments keep saying so for months.
- A wrong technical detail draws a liked correction (633 here). The storm audience watched these events live.
