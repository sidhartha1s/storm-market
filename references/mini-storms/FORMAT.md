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

## Format C · Rolling update — DEFAULT for the news lane from 2026-09-15 (owner 2026-09-14)
Measured from the four-channel teardown (`references/teardowns/2026-09-14-four-channel-working-topics/`): under a live-hazard
keyword the videos that surface are present-tense "Latest Updates" on the event, not retention-engineered mini-docs. Our two
Krakatau mini-docs got 55–60 impressions under the same keyword; the format mismatch was ranked the top controllable cause.
- **One live story, many videos, one clip pool.** Each new video carries a new official number, alert level or angle
  (what happened → who is at risk → what the agency said today → the mechanism → the US stake); clips re-ordered and
  re-trimmed, narration written fresh with analysis (reused-content safe). GWN's Nepal serial: 11 videos, 682 → 3,000 dead.
- **Order of information, every video:** what is happening right now → hard numbers with an as-of time → where and who →
  the named agency, quoted verbatim on screen with title → cause or escalation → what is being done → what is still
  unknown. Framing verbs: "here is where things stand", "as of Tuesday evening", "officials have not confirmed".
- **Sourcing convention:** "Indonesia's Center for Volcanology and Geological Hazard Mitigation" on first mention, PVMBG
  after; a named individual only when quoted, always with title. One spoken verbatim quote on screen per video, minimum.
- **Close:** the unresolved tracking line ("what it left behind has not been counted yet"), then ONE soft line: tell me
  in the comments where you are watching from, and subscribe for the next update. No resolved ending, no END CTA spine.
- **Pace:** Paul's TTS at the lane tempo (`config.yaml channel.tempo`, applied by `scripts/tts_episode.py`), timed after the speed-up. Measured fact to respect: GWN's
  hits run 66–78 wpm over the whole runtime because footage with natural sound breathes between narration blocks; the
  slowness comes from footage holds, not slow speech. A footage-only hold (natural sound, popfig place label) every
  60–90 s is allowed, not required: narrated clips as shipped so far are equally fine; the editor picks per cut (owner 2026-09-14).
- **Skeleton, 12:00 (the Words column is a planning shape; size the real script with `scripts/word_budget.py`, CLAUDE.md Voice; scale beats 3, 5, 7 for 10–14 min):**

| # | Beat | Time | Words |
|---|---|---|---|
| 1 | Cold open, what is happening right now (title number spoken + popped) | 0:00–0:45 | 124 |
| 2 | Numbers snapshot, as-of time | 0:45–2:00 | 206 |
| 3 | Where: ground-level scene, place names on a map | 2:00–4:00 | 330 |
| 4 | Named agency quote on screen, with title | 4:00–5:30 | 248 |
| 5 | Cause: how it happened or is escalating (the mechanism the news skipped) | 5:30–8:00 | 413 |
| 6 | What is being done: response, restrictions, the US stake | 8:00–9:30 | 248 |
| 7 | What is still unknown: the tracking line | 9:30–11:45 | 371 |
| 8 | Soft close: one comment + subscribe line | 11:45–12:00 | 41 |

  Paul's ebook CTA position and entry: `config.yaml channel.cta` (news lane `window_ms`) and the mini-storms skill's Dujuan rules. Humanise rules apply in full.
- **B-roll is muted by default.** A clip carries its own sound only when it earns it (sirens, presser sound, survivor voice); then
  Paul does not narrate over the same words, one voice at a time. lint_timeline fails any track-1 video that is neither `muted`
  nor `data-has-audio` (day-1 miss: a stranded-passenger interview played under Paul and a quote card, 15 Sep 26).
- **Narration windows = wav lengths.** lint_timeline fails any `nx-*` audio whose data-duration is shorter than its wav (day-1
  truncation: a retime moved starts and left the old lengths, cutting the last words of six segments).
- **Hard foreign names leave the voice and live on screen (owner 15 Sep 26, Hawaii review).** Kilauea, Hanalei, Kaumalapau,
  Moloaa, Haena, Wainiha, Nawiliwili, Puu Lua read as AI slop even respelled. Paul says "two elementary schools on the North
  Shore", "Lanai's only cargo harbor", "the utility"; the map tags, chips and cards carry the real names. Keep only names an
  American senior already says (Kauai, Lanai, Oahu, Krakatoa). Indonesian names: owner decides after hearing the phonetic pass.
- **Screen text uses numerals, the voice uses words.** Close card "81% restored. 3 names." while Paul says "eighty one percent".
- **Composition layout zones (map them before the first comp, not after 20 videos):** top-left eyebrow (110,60) + big title
  below it; top-right big number (right 110, top 56); left glass cards x 110–1090; map/diagram plates x 700–1700; NO text in the
  bottom 100 px (news bug) or in the presenter-circle corner x ≥ 1600 / y ≥ 680 (references/mg-quickref.md). No gate checks either zone yet.
- **Grouped reveals.** A stat and its caption are one element and appear together (the Kauai map showed captions before their
  numbers when only the numbers were hidden).
- **Pronunciation gate before timing.** After TTS, read every proper noun back from words.json; respell in plain lowercase
  phonetics (no hyphens, no caps: the clone read "DAH" and "-" as words) and re-synthesise before the cut list exists.
- **Packaging:** proper noun (volcano, storm, place) dominant in title and thumb, a number in the title, present tense,
  thumb spell-checked at 300 px, e.g. "Anak Krakatau Erupts Again... And Now Three More" (EarthDesk shape, 175–225k).
- **Publish window:** GWN's uploads land 00:00–07:00 UTC (US evening); target the same.
- **Tests before the format is called done:** (1) beat table in packaging.md sums to the target runtime (`scripts/word_budget.py`);
  (2) humanise pass green; (3) the quote line exists with a source URL in edit_script.md; (4) sweep/overlap/audio gates
  green; (5) Studio impressions read at 48 h and logged in `ops/tracker.json` before the bucket's next video.
Formats A and B below remain available for evergreen and explainer topics.

## Structure (owner rule 2026-09-08)
HOOK **3–5 s** (one present-tense sentence paying off the title, spoken + red popfig) → INTRO to
~1:10 (stakes numbers, open loops, promise) → CHAPTERS → PAYOFF → WARM CLOSE → subscribe.
Size every section in words before TTS with `scripts/word_budget.py` at the shipping tempo (CLAUDE.md Voice). Table goes in packaging.md.

## Retention architecture (owner + GPT pass on Krakatau #4, 2026-09-11)
Measured against a 14-minute cut that scored 5.5/10 on stakes-per-90-seconds before the rewrite.
1. **The voice never narrates what the MG shows.** Dates, clock times, place names and counts go on screen; the
   voice says the human version ("Two days before Christmas" while the card reads DEC 22, 2018 · 9:03 PM). Owner:
   "that's the engagement manipulation you are missing." Exception: a countdown device where the voice reads the
   clock on purpose (9:03 → 9:27 → 9:30).
2. **Stakes order, not chronology.** Order chapters by rising stakes for the viewer at home; a strong chapter after
   the CTA, a question before it. Time-order (this week → 2018 → 1883 → 1958) puts the peaks in the wrong places.
3. **One open question at all times.** Every chapter ends by asking the next one ("Then where?", "So did they fix
   it?", "And here is why faster is not enough"). Re-mention each macro-loop once mid-way; pay it explicitly
   ("The wrong number was the plume. The right number is the tilt.").
4. **No roadmap, no structure announcements.** Never "in the next fourteen minutes you will see…", "the record
   first", "now the honest part". A reveal that was announced is not a reveal.
5. **Hook = confirm the click with something more specific than the title**, in the present tense, with a person
   or a place, then the question ("Is history going to repeat? Let's find out."). Not a restatement of the title,
   not a proper noun the audience does not know (a US senior has never heard "Sunda Strait").
6. **One named person per tragedy.** Numbers bank the scale; a name banks the emotion (the singer who lived and his
   wife who did not; Ulrich and his son on the Edrie). The best-scoring chapter always had one.
7. **Clock, scorecard, equation.** Turn fact dumps into devices: the 2018 timeline as a countdown card, "what was
   fixed" as a FIXED / STILL MISSING scorecard, the warning maths as one equation on one card. Cut 25–35 % of the
   technical detail from any chapter that carries more than six numbers.
8. **"And you" inside the first 60 s (tightened 2026-09-14, audience audit; was "second minute").** The US viewer's stake (Alaska, the same physics at home) is promised early and
   paid at the mid-point, not discovered at minute seven.
9. **"What is NOT happening" is one line inside the payoff, not a chapter.** Two consecutive de-escalations
   (fix list, not-happening list) in the last third are an exit ramp.
10. **The ending lands the thesis, then the END CTA spine.** "2018 happened. The system got better. The physics did
    not change." One sentence of thesis, one quote callback, then the fixed spine. The mountain does not need to
    repeat 1883; it only needs to repeat 2018.
11. **Chain with conjunctions.** but / because / which means / and yet carry the viewer across every seam; full-stop
    lists are places to leave.

## Hook + intro (0–1:10)
1. The hook sentence says the title's headline number or claim (3–5 s), spoken and popped.
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

## On-screen text layer
- **Every overlay time is a word cue, never an estimate (owner 2026-09-10, Krakatau draft):** the popfig,
  chip, quote and source-label starts are resolved from `audio/<seg>.words.json` (first occurrence of a cue
  phrase, minus 0.12 s lead), and the build FAILS on an unmatched cue. Times guessed at words-per-second drift
  2–4 s either way within a segment (measured on Krakatau v1: "25 HOURS" 3.5 s early, "437 DEAD" 3 s early).
  Same for card rows. Pick cue words that whisper spells stably (avoid spelled-out numbers; whisper writes digits).
- **CTA first frame:** the clip starts 0.1 s BEFORE the 1.0 s dip-in black lifts (blackouts on their own track above
  the clip) and every audio/CTA start is frame-aligned (ceil to 1/30 s); otherwise the first syllable ("Mo…st people")
  is clipped. Dip-out after the CTA is 0.5 s.
- **TTS sentences over 24 words split and can repeat a fragment** ("drifting west, drifting west") or mangle a word
  ("affected" → "lifted", "not a wave" → "not if if"): read every transcript for repeated bigrams and nonsense before
  the timeline, re-synthesise the segment with the sentence split.
- Numbers: red popfig (Abril, text-shadow, ≤3 words) synced to the spoken word, PLUS a bottom-left
  data chip for the running stat ("50,000 feet", "6 airports"). Never a colour-block card.
- **Text width caps (measured on the Krakatau #4 slices, 2026-09-11):** popfig big line ≤ 16 characters (150 px
  Abril, nowrap: "IT LISTENS FOR THE GROUND" at 25 chars ran off both frame edges), chip ≤ 52 characters (34 px
  Arial Black from x=110 must stay left of the circle keep-out at x=1600), bug headline ≤ 60 characters (34 px bold,
  overflow hidden after the BREAKING tag + channel name). A sentence-length thought is a chip, never a popfig;
  the popfig is the number or the two-word verdict. The builder asserts all three before writing index.html.
- **A popfig never sits inside a card window:** the card's row carries that beat (the "listens for the ground"
  popfig collided with row 1 of the siren-chain card).
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
**Scope: Formats A and B. Format C keeps Paul's ebook CTA at the story break but replaces the END CTA spine and the
mid-video beats with its own soft close (one comment + subscribe line after the tracking line).**
- **Paul's ebook CTA** — every video, from `config.yaml channel.cta`, position and dips from `config.yaml channel.cta`, film layer off.
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

- **Homographs are a TTS trap:** list, senses and the probe-before-respelling rule live in
  `references/homographs.md`, gated by `scripts/homograph_scan.py`. Owner's phrases are verbatim — never
  paraphrase a line he wrote.
## Presenter circle — Paul PiP, phase 2 (owner 2026-09-09: standard on every mini-storm from Texas onward)
- 240 px circle, bottom-right (left 1640, top 708 on 1080p), 4 px red ring, above the news-bug strip. Present from the
  intro to the end of the last narration line, except in motion-graphics-only scenes, where he is not shown (owner
  26 Sep 26; `references/mg-quickref.md` "Frame and safe zones"); HIDDEN in the hook, in Paul's full-frame CTA window (the CTA has its
  own higher-quality face and lip-sync) and under the close card.
- Source = the CTA master, no generation: 410 px square crop centred on his face (he sits 205 px from the frame edge, so
  the crop starts at x=0 and the left margin is his own background blurred and extended), face ≈ 70 % of the circle.
- Two loops from HIS OWN speech spans (transcribe the CTA with word timestamps): `paul-talk` = his talking stretches
  joined; `paul-idle` = his pauses joined forward+back. Cut per window to the exact `data-duration` (media_budget),
  crf ~30 at 240 px (≈2 MB per window). Tracks 6 (idle) and 7 (talk); never share a track with anything else. **Mount as a bare timed `<video class="pip">` whose
  geometry is `!important` (the renderer's own `video{inset:0}` otherwise wins and the circle lands at 0,0), plus a separate
  timed `<section>` carrying the red ring (box-shadow is not copied in the renderer's frame swap). A `<video>` nested
  inside a timed section is treated as UNTIMED, always-on media and is drawn at 0,0 — never do that (measured 2026-09-09
  on two 6 s test renders).
- Talk-sync: merge narration words with gaps < 0.35 s into spans; the talk layer fades in (0.1 s) at each span start and
  out at each span end, idle underneath. One-shot helper computes the lines; never committed.
- Corner conflict: broadcaster bugs (NBC, WFAA, KTLA) also live bottom-right — accepted for now; revisit if it reads badly.
- Recipe files: `episodes/ms-elnino-texas/_framesweep/pip/` (crop, ring, mask, loops) until it moves to `library/mini-storms/presenter/`.

## Audio
- Narration pace: CLAUDE.md Voice (tempo per lane in `config.yaml channel.tempo`). Verify by ear on segment 1.
- One tense music bed at −24 LUFS under narration, ducked 6 dB under popfigs; master −14 LUFS.

## Topic selection (Stefan Burns / Hidden Constructions lesson)
- Be first with credentialed coverage of whatever hazard is live this week; speed is the moat.
- Uncontested angle beats channel size: unrest-mystery framing ("doing something it shouldn't")
  took a 1,150-sub channel to 148k views.
- Search sweep recipe (no NexLev needed): `yt-dlp "https://www.youtube.com/results?search_query=<q>&sp=CAISBAgCEAE%253D" --flat-playlist --playlist-end 20 --print ...`
  (this-week filter), rank ≥5-min uploads by views; see `ytsearch-outliers-2026-09-08.tsv`.
