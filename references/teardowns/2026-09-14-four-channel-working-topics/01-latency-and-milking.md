# Task B — How GWN Finds and Milks a Story

## 1. Publish latency (event date in description vs. upload timestamp, UTC)
| Video | Event date (from desc) | Uploaded | Latency |
|---|---|---|---|
| ITm1adnq0H8 (682 dead) | Wed 26 Aug | 29 Aug 23:32 | ~91.5h |
| vKVM-E6C7rU (cause explainer) | Wed 26 Aug | 30 Aug 05:09 | ~97h |
| yOlIzAY294w (3,000+ dead) | Wed 26 Aug (same root event) | 1 Sep 19:04 | ~159h |
| 0Quh4cBdbco (Toronto storm) | 2 Sep | 3 Sep 02:26 | ~26.4h |
| lCOyJXyrEWE (Sakurajima) | Tue 8 Sep | 11 Sep 18:30 | ~90.5h |
Pattern: the FIRST video on a story ships in ~1-1.5 days of the triggering event; every later "new number" video in the same serial re-dates itself off the same root event, so latency keeps climbing (a 6.5-day-old event still gets published as "Latest Updates"). Most other hits (UBCcWOLALF8, WcZ4cQAHlPE, avZRDJLBJ_Q, I_ueiyLhVsg, etc.) give NO fresh calendar date at all — only "authorities say" — because they're serial continuations, not first reports; the date only appears in the story's origin video.

## 2. Nepal death-toll serial (chronological)
| Upload (UTC) | Title number | Views |
|---|---|---|
| 29 Aug 23:32 | 682 dead / 3,000 missing | 740,097 |
| 30 Aug 05:09 | (no number — "cause" explainer) | 99,420 |
| 31 Aug 03:17 | 1,700+ deaths estimated | 1,770,977 |
| 31 Aug 06:34 | 920+ dead / 2,000+ estimated | 633,955 |
| 31 Aug 15:21 | 1,000 deaths & 4,700 missing | 1,779,321 |
| 1 Sep 12:10 | 2,400+ deaths estimated | 561,950 |
| 1 Sep 19:04 | 3,000+ dead | 122,929 |
| 1 Sep 19:36 | 1,200+ dead confirmed | 815,518 |
| 5 Sep 14:39 | 1,400+ dead confirmed | 104,843 |
| 6 Sep 00:11 | 5,500+ missing | 215,879 |
| 6 Sep 20:59 | 1,400+ dead & 5,500 missing | 312,080 |
Numbers do NOT rise monotonically — "estimated" vs "confirmed" are different tallies from different agencies, and GWN titles whichever figure just landed, even if lower than yesterday's. Views peak on days 2-3 (Aug 31, ~1.7-1.8M each) when the story is new and the toll numbers are shocking, then decay hard by day 6-11 (100k-310k) as the news cycle moves on. The one non-numbered "cause/footage" angle (vKVM-E6C7rU) underperforms every numbered-toll video except the latest, tail-end ones — a bare number in the title outperforms an explainer framing.

## 3. Upload-hour histogram (UTC → US time, n=20)
- 00:00-06:00 UTC: 10 videos → 8pm-2am ET / 5pm-11pm PT (heaviest block, half of all hits)
- 12:00-15:00 UTC: 3 videos → 8-11am ET / 5-8am PT
- 18:00-23:00 UTC: 7 videos → 2-7pm ET / 11am-4pm PT
GWN publishes into US evening/prime-time (8pm-2am ET) most often, with a secondary afternoon push (2-7pm ET) — timed to the US audience's viewing hours, not to when the disaster physically happened.

## 4. Sourcing signals (from description SOURCES blocks)
- Every hit description ends in a `SOURCES` list of named outlets: wire/major (Reuters, AP, AFP-style — actually named "Associated Press", Reuters, CNN, BBC, Al Jazeera), local/regional (Kathmandu Post, Fox 5 Atlanta, CBC/CTV/CP24, Folha de S.Paulo, Xinhua/CGTN/China Daily), and agencies (Japan Meteorological Agency, VAAC Tokyo, Hawaii EMA, Environment Canada, INMET, SIMEPAR).
- Two hits cite a live-blog URL directly as the source (UBCcWOLALF8 → BBC live page; x7FNXluokNg → CNN live-news page) — GWN's own "Latest Updates" format is a direct copy of these outlets' live-blog format.
- Hashtags always end `#NaturalDisaster #ExtremeWeather #GlobalWeather` plus 8-25 story-specific tags (place + event + year, e.g. `#NepalFlood2026`).
- No "footage courtesy" lines found in any of the 20; footage is narrated over, not credited per-clip.

## 5. Caption check (3 hits, .en.srt)
- 0Quh4cBdbco (Toronto): opens with a raw news-clip quote (">> HAIL THE SIZE OF GOLF balls...") then switches to narrator VO; ~10 of ~200 unique caption lines are quoted clip/anchor audio (~5%).
- I_ueiyLhVsg (Nepal): same pattern, ~12 of 213 lines are quoted clip audio (~6%).
- 9DQrpDVNZQ8 (Sakurajima): almost entirely narrator VO, 1 of 52 lines is a quote.
- No spoken attribution anywhere in any transcript ("according to Reuters," etc.) — sourcing lives only in the written description/hashtags, never in the narration itself. Narration is a paraphrase of wire copy; raw clip audio is a hook/texture device, used most on the higher-drama storm-footage hits.

## RECIPE
- **Trigger source**: wire/agency reporting (Reuters, AP, AFP-adjacent), national met/volcano agencies (JMA, VAAC, Environment Canada, INMET), and outlet live-blogs (BBC/CNN "Latest Updates" pages) — GWN mirrors whichever outlet already has a live-blog running.
- **Trigger→publish clock**: first video on a new disaster ships ~26-100h after the event; once the story is running, each follow-up ships same-day to next-day off whatever new number/agency statement just posted, regardless of the original event's age.
- **Milking rule**: new number = new video. A changed death/missing/evacuee count, even a lower or re-labeled ("estimated"→"confirmed") one, from any named source is enough to justify another upload; non-numeric angle videos (cause/explainer/leaked-footage) are published between number-updates but earn fewer views than a bare-number title.
- **Title formula**: `[NUMBER/STAT] + [DEAD/MISSING/AFFECTED/WITHOUT POWER] – [PLACE] HIT BY [HAZARD] (Latest Updates)`
  1. "1700+ DEATHS Estimated! Nepal Flash Flood (Latest Updates)"
  2. "65,000 WITHOUT POWER – Toronto HIT by Destructive Storm (Latest Updates)"
  3. "83,000+ EVACUATED – China HIT by Massive Floods (Latest Updates)"
  4. "35,000+ WITHOUT POWER – Hurricane Lowell HITS Hawaii (Latest Updates)"
  5. "6 VOLCANOES ERUPT - 150,000 AFFECTED Across Indonesia (Latest Updates)"

**Source data**: `gwn-hits/*.info.json` (20 files, descriptions/tags/timestamps), `gwn-hits/*.en.srt` (3 sampled), `gwn-full-flat.json`. All numbers above came from the python extractions run in this session, not memory.