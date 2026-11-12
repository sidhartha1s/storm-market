# Reels study, second pass (12 Nov 26)

Why this exists: the owner rejected the first pass (117 reels found by hashtag) on 12 Nov 26: "these are not
personalised videos u pulled. just faceless pages. we have paul, we are some what branded". He named ten accounts,
most of them animated end to end with Claude, plus Kallaway for script and frame one. Nothing here is built or
rendered. The reel format is open: "We are still experimenting phase ... nothing is finalized".

## What is in this folder
| File | What |
|---|---|
| `accounts.md` | The eleven accounts by median views per reel, last 45 days |
| `study.html` | The page the owner read: five directions, account cards, two Kallaway scripts taken apart sentence by sentence, his skeleton, frame-one notes. Its thumbnails are not tracked |
| `transcripts/<handle>.md` | Spoken words of the 65 reels that were transcribed (small.en, unchecked) |
| `data/` | Per account: every reel listed in the 45 days (`ig_<handle>.json`) and the ones pulled (`<handle>.picks.json`) |
| `pilot/timeline.html` | Pilot reel 1, "Stay or Go": the spoken lines with their sources. Its layout and its one drawn frame were rejected by the owner (12 Nov 26); the concept stands |
| `pilot/plot.html` | The plot six reels ahead: each reel's decision, what either choice costs, the real outcome with its script line, what happens when viewers take it elsewhere, the storms after |
| `tools/` | The one-off scripts that made the above. Not pipeline code, not gated |

## Method
- A reel's score is its views divided by its own account's median over the last 45 days. Reels under 3 days old are
  left out of "weakest" picks.
- Listing: the account's Reels tab read from a logged-in browser (`tools/ig_list.py`, needs `opencli` and the
  owner's Instagram login in Chrome; read and download only). The post date is decoded from the shortcode.
- Download: `yt-dlp` per reel, browser download as the fallback (`tools/pull.py`).

## What the accounts do
- Viewer-played serials (`oddhourtales`, `dontopenit.stories`) hold the two highest medians (887,500 and 944,000).
  Frame one: a clock, "Night 1/7", a rule sheet, an alert. Every reel ends on a choice, the comments vote, the next
  reel opens "You chose to…".
- One object followed end to end with a counter in the corner (`charles.zhengg`): two reels at 119x and 157x his
  median. The title names something of the viewer's.
- One question about your own body or house (`zhscience`): 3.0M on 2,607 followers.
- Kallaway: line 1 is the topic plus the outcome with a superlative, line 2 names the method, line 3 says what you
  get; each step is signpost, why most fail, the rule, an example, a one-line recap; each step change carries a
  fresh and stronger reason to stay; the end is a new gap, proof for the offer, one word to comment. His first-line
  template is the same at 17.11x and at 0.41x of his median: the subject and the frame-one picture separate the two.

## Owner's read of it (12 Nov 26)
- Direction 1 (the viewer-played serial on a real storm) is the one to scope.
- "the above reels claude automated mostly, have very generic opusslop ... animations - whcih are good. But generic
  among the 1000s." The pilot must not look like them.
- Paul's face in the circle is the branding that later sends people to the long form or the landing page, at least
  where he is the one talking; he stays the main narrator. The Instagram handle may change if needed.

## How a reel is shown to the owner (12 Nov 26, after he rejected the text timeline)
- As a storyboard: one real 9:16 frame per scene, read left to right, in several candidate looks. "I want different
  frames of different scenes basically"; "show me the candidates". Never tracks of words.
- One piece of text per frame at most. No date, clock or place caption: "Where should I look?"
- Graphics lead, the words are Paul's voice. "It is graphics less. I think you are trying to lead it with a lot of text."
- The brand is the long form's: its map, drawings, photos, palette and fonts (`library/inhouse/snippets/tokens.md`),
  and Paul's red-ringed circle on every frame. "my videos which you put on long form is much better than this."
- The concept is not what failed: "your conceptwise direction was good. failed on how to effectivate it/ visualise
  it designwise or branding wise to the viewers."

## The plot is planned ahead (12 Nov 26, after the owner asked where the stakes are)
Owner on the first storyboard: "Right now it's just a question ... where is the risk factor"; "You should be raising
the stakes somewhere"; "a really solid plot on either way whether they are choosing stay or go in nth episode"; "at
least see it two or three steps ahead of the people"; "people can take it anyway, they will give some suggestions,
and we might have to pivot midway"; "one bad episode can just shut the entire thing down".
- Every choice costs something on both sides, and both outcomes are shown. A choice with one plainly right answer
  is not a plot.
- The stakes rise reel to reel: less time, worse shelter, more people the viewer decides for.
- The reel's promise is what happened to "you", never "what the report says". The report is the receipt on screen.
- A plot goes to him with at least the next three reels worked out, a view to the end of the storm and the storm
  after, and what the next reel does for each way the comments can go. `pilot/plot.html` is that page.
- Each reel stands alone (it opens by replaying the last choice in picture), so one weak reel costs one reel.
- Nothing in it is invented except "you": every outcome is a line of the parent film's script.

## The pilot: "Stay or Go" (Moore, 3 May 1999, reel 1 of 6)
Look: the owner picked "Map room" from three storyboard looks ("A is good mate", 12 Nov 26): the film's county map
and line drawings turned upright, all vector, Paul's circle with the countdown ring. The storyboard page sits in a
scratch folder outside the repo until this merges.
`pilot/timeline.html` holds reel 1's lines; `pilot/plot.html` holds reels 1 to 6. Every fact is the parent film's
(`episodes/ep-moore-1999/edit_script.md`, lines named per beat; `fact_check.md`).
What separates it from the animated accounts: the choices are ones real people faced and the answer is read from
the weather service's report on screen; real NOAA and weather service photos and the real path map; everything on
screen is from 1999 (tube TV, weather radio, wall clock); Paul's circle and voice in every reel.

## Comment-to-DM (checked on vendor and Meta pages, 12 Nov 26)
- SuperProfile's free plan does keyword-comment to DM on a chosen reel: "Unlimited AutoDMs on Reels & Posts", one
  keyword per automation, one Instagram account. Free DMs end with a "Sent via" line naming SuperProfile
  (superprofile.bio/pricing, superprofile.bio/auto-dm).
- Ask-to-follow before sending: SuperProfile's pages disagree. The pricing card lists it under the free plan; the
  AutoDM page and guide say it needs a paid plan (Creator, $4.99 the first month, then $29 a month). Settled only by
  looking at the toggle inside the owner's account.
- CreatorFlow free: 500 DMs a month; its follow gate is on the $15 a month plan (creatorflow.so/pricing). ManyChat's
  pricing pages could not be opened.
- Instagram must be a Professional account; no Facebook Page is needed with Instagram Login; no follower minimum
  found (developers.facebook.com/docs/instagram-platform/overview).
- Meta: one private reply to a commenter, within 7 days of the comment; 750 private replies an hour per account.
- A vote and a giveaway can share a reel: the DM triggers on its keyword only, as long as "any comment" stays off.
  Read from the product page, not tested.

## Not done, not known
- Only the top reel's frame sheet per account was opened, plus a few more; 2 of Kallaway's 18 scripts are annotated.
- The 45-day lists for `charles.zhengg` and `factloree` may be incomplete (read by scrolling).
- Several accounts are weeks old (8 to 14 posts).
- The sound effects cut from `subhangfx82`'s demo reels are rips and stay out of the repo and out of every video
  (CLAUDE.md "Sound": never ripped or unlicensed audio).
- The 79 downloaded reels sit in a scratch folder outside the repo until this merges; `.gitignore` now covers
  `references/shorts/research-*/media/` so they can move into the main checkout.
