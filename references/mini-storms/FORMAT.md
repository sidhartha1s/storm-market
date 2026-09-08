# Breaking-lane FORMAT — measured rules for The Warning Hour fast videos

Source: `teardowns/README.md` (10 videos, contact sheets + scene-cut detection + comments,
2026-09-08). Numbers below are measured, not guessed; re-measure before changing them.
Owner brief (2026-09-08): 8–12 min, stitched clips + stills with motion, narration, red emphasis
text, BREAKING-style packaging, ≤3 h to ship, one owner gate, clip pool reused across angles.

## The two formats that win (pick per topic)

| | A. Fast-cut compilation | B. Live-data explainer |
|---|---|---|
| Models | Disaster Pulse 28UP8fh-sCU (386k/day), The Field Report iexrMZYDTNw, The Space Desk z_vo0DCEKAE | Stefan Burns (798k subs, 9ws0qN4hFtY / hf7xCeEWeOE / YHjdguvoksw) |
| Median shot | 3.5–4.5 s (hook 3.5–4.2 s), 230–280 cuts / 19 min | 7–33 cuts total; 0 cuts in the first 60 s; one real data feed held 20–60 s |
| Footage | ~70 % real broadcaster / CCTV / social, ~30 % stock or AI stills | Only live public-agency feeds + archival; zero AI |
| Narration | 160–200 wpm | 160–180 wpm |
| Cadence | daily while the event is hot | every ~1.6 days, whatever hazard is live |

Default for us: **A**, with B's data-feed holds (USGS / NOAA / NASA loops, labelled) dropped in
every 2–3 min as credibility anchors. Never AI-only: the AI-stills-only video (n_41Jzj3KPU) is the
weakest of the set and audiences call out AI inserts by timestamp even at 1k subs.

## Structure (owner rule 2026-09-08)
HOOK **3–10 s** (one present-tense sentence paying off the title, spoken + red popfig) → INTRO to
~1:10 (stakes numbers, open loops, promise) → CHAPTERS → PAYOFF → WARM CLOSE → subscribe.
Size every section in words before TTS at the delivered pace (~148 wpm ≈ 2.47 words/s with
atempo 1.15): 8:30 ≈ 1,260 words, 9:30 ≈ 1,410, 12:00 ≈ 1,780. Table goes in packaging.md.

## Hook + intro (0–1:10)
1. The hook sentence says the title's headline number or claim (3–10 s), spoken and popped.
2. Intro withholds the real angle one beat: surface story → "but that's not the real threat" → thesis + open loop.
3. Best carry-over pattern (3r5HgsfWtRQ, 129× subs): the title's odd claim IS the hook's literal
   thesis, resolved with a real precedent (date + death toll) inside the intro.
4. Weakest: a title that names no subject (YHjdguvoksw). Always name the hazard.
5. Thumbnail phrase (≤4 words, TOP of frame) is spoken aloud inside the intro.

## Body
- 8–12 idea blocks of 45–75 s; each ends on a connective (but / and / however) into the next.
- Section break = 1–2 s glitch or hard cut to a bold white-caps card on black ("WHAT HAPPENS
  NEXT" is a genre convention; use our own wording).
- Every spatial / mechanism claim gets a purpose-built diagram or labelled agency graphic, not
  b-roll with text over it.
- Real-clip rehook every 45–60 s (channel rule); stock / stills only fill between real clips.
- Content-gap layer from comments: the whole niche's top comments ask "is this exaggerated?" and
  nobody answers on-screen. One explicit "what is NOT happening" beat per video.
- Word budget at ~148 delivered wpm (2.47 w/s): 8:30 → 1,260 words; 9:30 → 1,410; 12:00 → 1,780.

## On-screen text layer
- Numbers: red popfig (Abril, text-shadow, ≤3 words) synced to the spoken word, PLUS a bottom-left
  data chip for the running stat ("50,000 feet", "6 airports"). Never a colour-block card.
- Burned-in word-highlight captions are near-universal (9/10 videos): white caps, bottom third,
  key word highlighted. Ours: yellow highlight on the same words that get a popfig.
- BREAKING kicker: lower-third bug with the channel name + rotating headline every 10–15 s.
  Never invent a network name (qLun3DQLu5s's fake "GNN" is a trust risk we do not take).
- Labelled agency graphics ("SOURCE: USGS", "© CSU/CIRA · JMA/JAXA") kept, as credibility.

## Clips
- 9:16 sources: pillarboxed centre on a blurred, darkened copy of themselves; never cropped to fill.
- Credit `@handle · platform` lower-left for the clip's whole duration. The 386k/day video lifted
  Stefan Burns' TikTok uncredited; we credit every small creator, always (owner rule: credit ≠
  licence, so still no chaser / independent videographer footage without a licence).
- Broadcaster logos stay burned in; pulls 3–5 s each, never the same cut twice.
- Stills: 3–6 % pan / push over the hold, ≤4 s static ever.
- Pool: `library/mini-storms/<event>/` + provenance.csv; second and later angles reorder and retrim
  the same pool, never the same sequence.

## CTAs and interaction beats (owner ledger 2026-09-09; placed by judgment while scripting, never by code)
- **Paul's ebook CTA** — every video, from `config.yaml channel.cta`, at the story break (~40 %), 1 s dips, film layer off.
  Description line 1 = paulraymond.online. No "book mentioned at mm:ss" line.
- **Hard cap: 3 CTA beats per mini-storm, including the END CTA, excluding Paul's.** Breadcrumbs do not count.
- **B · Where are you watching from** — once per video, near the one-minute mark, worded fresh every episode; also the
  owner's pinned comment on upload.
- **C · One mid-video question** — a concept, not a line: something the viewer answers in a few words about their own
  situation, OR a "think about it yourself" beat that asks for no comment. Invented from that episode's material;
  never reuse a previous video's question or wording.
- **D · Name-drop** — one line that references a real-sounding place from the thread (first: Lancaster County, an
  actual comment). While threads are thin it may be invented, phrased as a place people ask about — never a quoted
  commenter. Counts as a beat only if it asks for a comment.
- **END CTA (fixed spine, owner's words):** "If you enjoyed this video, like and subscribe for more! I truly appreciate
  it. Comment [ONE item: favourite moment / custom / next video idea] or any suggestions for improvements. I love reading
  all your comments. Make sure to check out the ebook in the description, and stay tuned for the next video. Good day."
  The bracket is chosen per video; never a favourite-moment ask on a tragedy-spined video.
- **No separate mid-video "comments line"** — it duplicated the end CTA; too many asks and the viewer leaves.
- **Breadcrumbs inside hard chapters** (≤2 per chapter, 5–10 words): signpost, technical-then-plain,
  guess-before-reveal, one-number rule, callback.
- **Spacing and tone:** never in the first 60 s, never inside a number run, never back to back, nothing near Paul's CTA;
  the writer places them where the narration already breathes. Narrator voice for narration; the beats are the chill
  uncle — one breath, no lecture, no repeated words.
- **Upload routine (owner):** pin the where-are-you-watching comment, post the next-topic vote five minutes later,
  answer the first ten comments within the hour, open the next video by naming the winner.

## Audio
- Narration 150–160 wpm delivered. Pocket-TTS Pharaoh lands ~129 natively; use `atempo 1.15–1.2`
  in the breaking lane only (documentary lane stays native). Verify by ear on segment 1.
- One tense music bed at −24 LUFS under narration, ducked 6 dB under popfigs; master −14 LUFS.

## Topic selection (Stefan Burns / Hidden Constructions lesson)
- Be first with credentialed coverage of whatever hazard is live this week; speed is the moat.
- Uncontested angle beats channel size: unrest-mystery framing ("doing something it shouldn't")
  took a 1,150-sub channel to 148k views.
- Search sweep recipe (no NexLev needed): `yt-dlp "https://www.youtube.com/results?search_query=<q>&sp=CAISBAgCEAE%253D" --flat-playlist --playlist-end 20 --print ...`
  (this-week filter), rank ≥5-min uploads by views; see `ytsearch-outliers-2026-09-08.tsv`.
