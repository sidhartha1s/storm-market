# Other platforms: where the same videos can earn, and one place to post from

Owner, 10 Oct 26: "check up other platforms where we can post such videos, long form and short, to multiply the revenue
generation, like let's say Facebook ... Maybe Spotify is a good choice because people like to listen as music. And maybe
at some point we will have one single dashboard where we will be able to quickly post to all these platforms in a
single go. Like I will be giving you all the API keys and stuff, you will automate all those things."

**State: a first check, not a plan.** Read by web search on 10 Oct 26. Most entry bars, API limits and prices below come from
third-party guides that disagree with each other; the platform's own page or the account's own monetization tab is the only
authority, and each one is re-read before any build. Which platforms a short goes to, and in what order, is set out
in `references/shorts/PLAN.md` ("Platform facts" and section 4; its pilot go and its TikTok route are still open there).
This file adds long form and the payout programs, and what the posting tools cost today. The reminder is `ops/tasks.md` task 26.

## What each platform pays for

| Platform | Takes | Pays through | Entry bar, as found | Posting by API |
|---|---|---|---|---|
| Facebook Page | long videos and Reels | Content Monetization, one program for Reels, long videos, photos and text | Guides say invite-only with no published bar (Meta's own page was not read). Guides cite 10,000 Page followers and 600,000 minutes viewed in 60 days. Originality and rights are reviewed | Yes. Reels by the Reels Publishing API (3 to 90 s, 9:16, 30 posts per 24 h per Page); long videos by the Video API. An app used only by people with a role on it needs no App Review |
| Spotify | long form, as video podcast episodes | Partner Program: 50 % of the ad revenue in the episodes, plus a share of Premium video revenue | 3 episodes, 2,000 hours consumed in 30 days, 1,000 unique streamers (lowered Jan 2026). A stream counts at 60 s | No creator API: video goes up on the Spotify for Creators web page. An API exists only through partner hosts (Libsyn, Podigee, Audioboom, Audiomeans, Podspace, live 14 May 26) |
| X | shorts and long form (in-app up to 6 hours for subscribers) | Original Content Rewards; the old ad revenue sharing was retired 7 Sep 26 | Premium subscription, 500 verified followers, 500,000 home-timeline impressions from verified users in 90 days (third-party summaries) | Yes, pay per use: $0.015 a post, $0.20 when the post carries a link. One source gives 140 s and 512 MB as the API video limit, so long form by API is unclear |
| TikTok | videos over 1 minute | Creator Rewards | 10,000 followers, 100,000 views in 30 days, original videos | Content Posting API, free; public posting needs an app audit. Blocked in India: see `references/shorts/PLAN.md` |
| Snapchat | Spotlight videos over 1 minute | Unified Monetization Program | Invite-only; 50,000 followers. One guide says fully AI-generated videos left the payout pool in May 2026 (one source) | not checked |
| Rumble | long form | ads and licensing | Low, per guides: an account in good standing and original videos | No upload API found |
| Dailymotion | long form | Partner Program | No 2026 bar found | Yes, a documented upload API |

## What decides it for this channel

- **The owner's country.** Most programs pay by where the creator lives. Spotify's own page lists 19 countries (Europe,
  the US, Canada, Australia, New Zealand) and announced more than 35 new markets for autumn 2026; India was not in the
  part of the list this check could read. One guide names India for Facebook's program; Meta's page was not read.
  Each is a short look at the account's own monetization tab, and it comes before any other work.
- **Originality rules.** The programs with an entry bar review originality. Our videos are scripted narration with analysis, which is
  the safe side; the AI presenter and the short broadcast excerpts are the two things to read each platform's rule on.
- **The book can sell everywhere.** A post can sell the book where the platform pays nothing, and that has no entry
  bar. Where the link goes on each platform is `references/shorts/PLAN.md` section 4. Not measured on any platform yet.
- **Audio.** The owner's Spotify point fits: the documentaries are narration-led, so they hold as audio. The maps and
  diagrams do not travel, so the script would need its on-screen-only facts spoken.

## My reading (not decided)

1. **Facebook first.** The second-largest reach among US 65+ (`references/shorts/PLAN.md` "Platform facts"), one
   program for both lengths, and an API for both. The Page does not exist yet.
2. **Spotify second**, once the country question is answered. Upload is by hand unless a partner host is used.
3. **X and Instagram for reach and the book.** X's payout bar is in the table; Instagram's payout programs were not checked.
4. **Not now:** TikTok (India), Snapchat (50,000 followers, the AI rule), Rumble and Dailymotion (small; revisit).

## One place to post from

When a posting tool is chosen is already ruled in `references/shorts/PLAN.md` section 4: the first week of uploads is by
hand, and "No scheduler until the hand-upload week gives per-platform numbers". This section does not change that; it
only records what the ways cost today. Each episode already has `metadata.md` (title, description, chapters, tags) and
its master file, so a tool can read those; captions stay different per platform, as that section says.

| Way | What it is | Cost found (US$ a month) | Catch |
|---|---|---|---|
| Our own script in `scripts/` | Calls each platform's API with the owner's keys from the repo `.env` | 0, plus API fees (X charges per post) | We maintain it. The code sits in this folder; the new accounts it needs (Facebook Page, Meta developer app, paid X API, Spotify for Creators or a partner host) are exceptions to declare in `CLAUDE.md` in the build PR |
| Postiz | Open source, self-hosted or cloud, 30+ platforms | Self-hosted 0; cloud from 29 for 5 channels | A new outside tool: an exception to declare in `CLAUDE.md` first |
| A paid posting API | Upload-Post or Ayrshare | Upload-Post from 24 for 5 profiles; Ayrshare from 149 for 1 profile | Same exception; none of them gets around TikTok's audit or Spotify's missing upload API |

My reading for when that gate is passed: our own script, YouTube and Facebook first (two APIs), and a look at Postiz only if the
list grows past four platforms.

## Needed from the owner before any build

- The hand-upload week from the shorts plan comes first; no posting tool is built before its numbers exist.
- The Facebook Page and the Instagram account (`references/shorts/PLAN.md` open item 2), and a Meta developer app.
- A look at the monetization tab on Facebook and on Spotify for Creators from his own account: is his country in.
- The keys, into the repo `.env`. They are never printed or committed.

## Not checked

Instagram's payout programs, YouTube's podcast feature, audio-only feeds (Apple, Amazon), pay rates per 1,000 views on
any platform, how broadcast excerpts are claimed outside YouTube, and tax and payout setup from India.

## Sources (read 10 Oct 26)

- Facebook: https://www.buffer.com/resources/how-to-make-money-on-facebook/ · https://creatorsagency.co/blog/facebook-content-monetization-requirements-2026 · https://www.shortsync.app/resources/facebook-content-monetization-program-2026 · https://www.socialcal.app/blog/how-much-does-facebook-pay-for-views · https://developers.facebook.com/docs/video-api/guides/reels-publishing
- Spotify: https://support.spotify.com/us/creators/article/spotify-partner-program/ · https://newsroom.spotify.com/2026-01-07/spotify-partner-program-updates/ · https://newsroom.spotify.com/2026-09-17/partner-program-expansion-global/ · https://techcrunch.com/2026/09/17/spotify-expands-its-partner-program-for-podcasts-to-35-new-countries/ · https://creators.spotify.com/resources/news/expanding-video-partners-and-platforms
- X: https://help.x.com/en/using-x/creator-revenue-sharing · https://opentweet.io/tools/original-content-rewards-checker · https://postproxy.dev/blog/x-api-pricing-2026
- TikTok: https://www.toptal.com/creator/post/how-to-join-the-tiktok-creator-rewards-program · https://www.blotato.com/blog/tiktok-api-pricing
- Snapchat: https://www.netinfluencer.com/snapchat-announced-unified-monetization-program/ · https://www.shortsync.app/resources/snapchat-spotlight-monetization-2026
- Rumble and Dailymotion: https://rumble.support/help/rumble-creator-program · https://developers.dailymotion.com/guides/upload/
- Posting tools: https://docs.upload-post.com/resources/pricing-and-limits · https://www.blotato.com/blog/postiz-vs-ayrshare · https://opentweet.io/alternatives/ayrshare · https://buffer.com/resources/social-media-api-multi-platform-posting/
