# Retention (AVD) study: The Warning Hour, 24 Sep 2026

> Doc homes changed 26 Sep 26: the DESIGN.md graphics sections quoted below (type scale, "max 3 s of no change") now live in
> `references/mg-quickref.md` (the 3 s wording is gone; stillness fails at 4 s), and LEARNINGS.md is split into `learnings/`.

Independent study. Phase 1 (outside research) was done before reading the repo's script rules. Phase 2 read CLAUDE.md,
DESIGN.md, references/script-os.md, script-framework.md, script-scaling.md, humanise-rules.md, packaging-rules.md,
mini-storms/FORMAT.md, channel-audit-2026-09-19/ (Studio export + thumbs), the teardown syntheses, ops/ROADMAP.md,
the LEARNINGS.md entries on hooks, CTA and pace, config.yaml `channel.tempo` and `channel.cta`, and the owner feedback
memories named in the brief.

Evidence labels used throughout:
- **[data]** a study, platform statistic or measured dataset.
- **[vendor]** a creator-tool company's own benchmark: useful, not peer reviewed, sample not public.
- **[blog]** creator or agency opinion.
- **[repo]** our own Studio export or measured repo fact.
- **[judgment]** my inference; no source.

---

## 0. The one caveat that governs everything below

Our own retention evidence is one video deep. In the Studio export
(`references/channel-audit-2026-09-19/studio/Table data.csv`, local Studio export, not committed), the 2011 Super Outbreak doc (28.2 min, 40.92 % average
percentage viewed, 11:32 AVD, 6.48 % CTR on 11,845 impressions) holds 75.8 % of the channel's 281.9 watch hours
[repo]. Joplin (17.1 min, 25.04 %) and Tri-State (34.9 min, 20.87 %) are the only other videos with more than a few
hundred views. Every mini below 100 views is noise. The repo has no per-second retention curves, no key-moments
report, no device or age split per video: rules claiming "viewers leave at 10 s" or "AVD dropped with the 35 % CTA"
(config.yaml comment on `window_ms`) are not provable from what is on disk. Pulling those reports (section 8) is the
first change, because it decides whether the rest of this study is right.

Second caveat: "Walt" and "Ray", the two seniors quoted across `references/teardowns/2026-09-14-*` and
`packaging-rules.md`, are AI role-play personas (`01-senior-texas.md` opens "Answer as Ray"; packaging-rules.md calls them
"two senior personas"). They are useful as a structured skeptic, but they are not audience data, and several repo rules
cite them as if they were.

---

## 1. Who the audience really is, and what that implies

**Facts**
- Owner's Studio export: the El Niño minis drew about 100 % US viewers aged 65+ (brief; ops/ROADMAP.md) [repo]. The best
  doc's audience was 75 % US, 34 to 75 (teardown `00-senior-ohio.md`, owner 2026-09-13) [repo]. Per-video age for the
  docs has not been pulled.
- 64 % of US adults 65+ use YouTube in 2025, up from 38 % in 2019
  ([Pew, Nov 2025](https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/)) [data].
- Nielsen: US viewers 65+ watched 96 % more YouTube on TV sets in Feb 2025 than a year earlier, and now watch nearly as
  much YouTube on TVs as kids 2 to 11 ([Tubefilter on Nielsen The Gauge](https://www.tubefilter.com/2025/03/25/nielsen-the-gauge-tv-viewing-report-youtube/);
  [Nielsen](https://www.nielsen.com/news-center/2025/youtube-achieves-best-monthly-performance-to-date-and-pulls-ahead-in-nielsens-february-media-distributor-gauge/)) [data].
- The living-room TV is now the top US screen for YouTube, and about half of YouTube viewing is on TV
  ([Deadline](https://deadline.com/2025/02/youtube-viewership-tv-screens-exceeds-mobile-for-first-time-in-u-s-1236284781/);
  [YouTube blog on podcasts in the living room](https://blog.youtube/news-and-events/podcasts-living-room-in-2025/)) [data].
- Older viewers still favor local TV weather during severe events, and adults 50+ are the core of local TV news
  ([HellerWeather survey note](https://hellerweather.com/new-research-preferred-source-for-weather-is-not-local-tv-newscasts/);
  [TVREV](https://www.tvrev.com/news/whos-actually-watching-local-tv-news)) [data, secondary].

**What aging research says about how they listen and watch**
- Comfortable speech rate is 150 to 200 wpm for young and old alike, but when speech is artificially sped up
  (time-compressed), older listeners lose far more than younger ones; inserting pauses at clause and sentence ends brings
  older listeners' recall back near normal ([ASHA Leader, "Aging in a Fast-Paced World"](https://leader.pubs.asha.org/doi/10.1044/leader.FTR7.10092005.12);
  [PubMed 8972446, time-compressed speech, age and complexity](https://pubmed.ncbi.nlm.nih.gov/8972446/);
  [PubMed 19449242](https://pubmed.ncbi.nlm.nih.gov/19449242/)) [data]. Our atempo 1.10 is exactly this manipulation
  (9.1 % time compression).
- Background music and noise hurt TV speech intelligibility more for seniors and the hearing impaired; a BBC survey found
  60 % of viewers had some difficulty with TV speech, with background music one of four named causes
  ([Big Pictures and Little Screens, BBC R&D](https://www.researchgate.net/publication/321213357_Big_Pictures_and_Little_Screens_How_television_sound_research_can_work_with_and_for_hard_of_hearing_viewers);
  [SVT enhanced-speech paper](https://arxiv.org/pdf/2208.08960)). Listeners rated understanding better at +12 dB
  dialogue-to-background than at +7 dB ([JSLHR 2026](https://pubs.asha.org/doi/10.1044/2026_JSLHR-25-00127)) [data].
- Only 27 % of viewers over 65 use captions always or often, versus nearly 60 % of 18 to 24 year olds; older users who do
  turn them on cite accents and hearing loss ([TV Tech](https://www.tvtechnology.com/insights/analysis/study-nearly-half-of-americans-always-or-often-watch-video-with-captions);
  [AP-NORC](https://apnorc.org/projects/closed-captioning-on-its-a-generational-thing/)) [data]. Implication: the voice
  must carry the video on its own; captions are a backup, not the delivery channel.
- Older adults show a positivity effect and report less interest in content that induces fear or sadness, more interest
  in contemplative and heartwarming content ([Carstensen and Mikels 2005](https://journals.sagepub.com/doi/10.1111/j.0963-7214.2005.00348.x);
  [positivity-effect theory review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3459016/)) [data].
- Patronizing, simplified "elderspeak" is rated as demeaning by cognitively intact older adults and does not improve
  their comprehension ([Kemper research summary, Merrill Center](https://merrill.ku.edu/news/article/2022/01/05/elderspeak-it-helpful-or-just-baby-talk);
  [Innovation in Aging concept analysis](https://academic.oup.com/innovateage/article/5/3/igab023/6314228)) [data].
- Older adults are worse than younger adults at telling TTS from human voices, but across ages human voices are rated
  more natural and more trustworthy than synthetic ones ([ScienceDirect, attractive synthetic voices](https://www.sciencedirect.com/science/article/pii/S2949882125000957);
  [Springer, older adults and AI voice agents](https://link.springer.com/chapter/10.1007/978-3-032-30833-7_44)) [data, mixed].
- TV viewing distance: Android TV designs at 960 x 540 dp for a 1080p screen (1 dp = 2 px at 1080p), with a 5 % safe
  margin ([Android TV layouts](https://developer.android.com/design/ui/tv/guides/styles/layouts)); the minimum
  recommended TV font is 12 sp and the default is 18 sp ([Android "Style for TV", archived](https://spot.pcc.edu/~mgoodman/developer.android.com/preview/tv/design/style.html)) [data].
  That is 24 px minimum and 36 px default on a 1080p frame.

**Implications**
1. Design for a lean-back TV viewer at ten feet with some hearing loss, not a phone viewer. [judgment from the data above]
2. Speed is a cost for this audience, pauses are a gift. Slower delivery plus clause pauses beats denser speech.
3. Plain words, yes; child register, no. The audience knows weather (65+ read forecast information more correctly than
   adults under 30, [PLOS/AMS summary](https://par.nsf.gov/servlets/purl/10174315)), and talking down to them costs trust.
4. Fear should arrive as sourced fact and resolve into agency (what you can do), which the channel's preparedness close
   already does.
5. Trust signals that work for this group: named agencies and people, real archive they remember, a human voice or face,
   correct spelling, no fake chyrons.

---

## 2. What we do wrong for retention

Each item: the rule or practice, the evidence, severity.

1. **Docs run at atempo 1.10: 176.0 wpm delivered on ep-1974** (config.yaml `tempo: 1.10`; measured from words.json
   over the tempo'd wav). The only doc that held its room (Super Outbreak, 40.92 %) ran 150.9 wpm measured the same
   way [repo]; the 137 to 143 figures in the teardowns are a probe planning number and words over total runtime. Time-compressed speech is the one speech change that
   hurts older listeners disproportionately [data, section 1]. EarthDesk's three winners cluster at 143 to 148 wpm
   (`three-channel-top12/06-synthesis.md`) [repo]. Severity: high. This is the single most evidence-backed change here.
2. **No retention curves on disk.** Rules are set from AVD totals and owner impressions. Severity: high (process).
3. **Graphics small text is below TV-legible size.** DESIGN.md type scale: row label 19 px, counter label 20 px, eyebrow
   22 px, and a required "small under 26 px" tier. At 1080p the TV minimum is 24 px and default 36 px [data]. For a
   65+ viewer at ten feet, 19 to 22 px labels are unreadable. Severity: medium to high (every graphic).
4. **Information density tuned for phones.** script-scaling.md: "something NEW lands every 2 to 3 s on graphics; every
   6 to 10 s in narration"; DESIGN.md: "max 3 s of no change inside any graphic window". Older viewers need processing
   time [data]; nobody pauses a TV to read. [judgment] The density rule should apply to motion, not to new facts.
5. **The CTA is a 15 s AI-avatar insert plus, in minis, a spoken like/subscribe spine.** FORMAT.md END CTA spine ("If
   you enjoyed this video, like and subscribe for more! ... Good day.") and the "where are you watching from" beat
   near 1:00. Zero of the twelve niche top performers close with a subscribe ask (`three-channel-top12/06-synthesis.md`)
   [repo]; an early comment ask contradicts script-os voice rule 3 ("no comment ask before the closing CTA"). Viewers
   leave during outros; YouTube tells creators to plan the last 20 s around end screens
   ([YouTube Help, end screens](https://support.google.com/youtube/answer/6388789?hl=en)) [data]. Severity: medium.
6. **The Paul presenter circle on docs** (owner 21 Sep 26): a looped crop of the AI CTA avatar whose lips flap on
   narration spans (FORMAT.md "Presenter circle"). Mismatched lip-sync on a synthetic face is an uncanny cue; the niche
   comment evidence shows "is this AI?" suspicion is the main trust tax (`szone-spacedesk-50/14-synthesis.md`,
   `critical-latitude-krakatau-2026/teardown.md`) [repo]. AI avatars can trigger higher eeriness and lower credibility
   ([JTAER experiment](https://doi.org/10.3390/jtaer21050141)), though a science-communication study found no uncanny
   valley ([JCOM 2025](https://jcom.sissa.it/article/pubid/JCOM_2402_2025_A03/)) [data, mixed]. Severity: medium, and it
   collides with the corner where broadcaster bugs sit.
7. **Hook contract bans the archive audio the only hit used.** ep2's hook used Spann's live "tornado emergency" by
   about 2.5 s (LEARNINGS 2026-07-27); DESIGN.md now bans any archive audio in the hook (owner 22 Sep 26). The audience
   "saw these events live" (CLAUDE.md footage rules). Severity: medium, see section 5.
8. **Music bed level is set by feel.** Score gain 0.13 and "ducked about -14 dB" (DESIGN.md Music) is roughly in range,
   but there is no per-window dialogue-to-bed check at +12 dB or better [data]. The FORMAT.md mini bed is -24 LUFS under
   a -14 LUFS master, which is about 10 LU [repo], under the +12 dB the hearing-loss study rated best. Severity: medium.
9. **Internal rule conflicts that let a writer do either thing** (each is a retention coin flip):
   - "Never spend curiosity early. No 'in the next 14 minutes'" (script-os Layer 1 rule 3) vs "Inside 45 s one
     direct-address fact promise ('Inside twenty minutes you will know...')" (script-os voice rule 3).
   - "Every chapter ends by asking the next one" (FORMAT.md retention rule 3) vs "No chapter-exit questions" (owner
     decision in script-os, 2026-09-14) vs "at most 3 per documentary" (voice rule 9).
   - "Where are you watching from, near the one-minute mark" (FORMAT.md CTA beat B) vs "no comment ask before the closing
     CTA" (script-os voice rule 3).
   - "Exact figures, never rounded" (humanise rule 11) vs "feat numbers are said roughly" (LEARNINGS 2026-09-23).
   - DESIGN.md signature close "This was The Warning Hour" vs script-os rule 13 "no sign-off line".
   - "Hook is 3 to 10 s" (memory feedback-hook-is-3-to-10-seconds, minis) vs "hook is 45 to 60 words, 20 to 25 s"
     (memory feedback-hook-payoff-first, docs).
   - "4th-grader readable" (script-scaling.md) vs "keep the term, define it in 12 words or fewer, reuse it 3+ times"
     (script-os voice rule 11).
   Severity: medium; resolved in the ruleset in section 6.
10. **Length set by the story, not by the retention curve.** Tri-State ran 34.9 min for 20.87 %, the fire tornado 32.5
    min for 5.76 % on day one [repo]. The 13 to 23 min band is right; the two 30+ min uploads broke it. Vendor data shows
    APV falls as length rises (5 to 10 min videos hold best at 31.5 %) ([Retention Rabbit 2025 report](https://translate.google.com/translate?u=https://www.retentionrabbit.com/blog/2025-youtube-audience-retention-benchmark-report&hl=es&sl=en&tl=es&client=srp)) [vendor].
    Severity: medium.

---

## 3. What we do not do at all

1. **Pull the per-second retention curve and "Key moments for audience retention"** (intro at 0:30, top moments,
   spikes, dips, continuous segments) for every video with 100+ views
   ([YouTube Help 9314415](https://support.google.com/youtube/answer/9314415?hl=en)) [data]. Also the typical-retention
   overlay (your last 10 videos of similar length) and the new vs returning viewer split
   ([Search Engine Journal](https://www.searchenginejournal.com/youtube-typical-audience-retention/421700/);
   [Social Media Today](https://www.socialmediatoday.com/news/youtube-tests-audience-filters-video-retention-stats/710915/)).
2. **Split AVD by device type and viewer age** in Studio Advanced mode, to know how much of the doc audience is on TV.
   [judgment: verify the exact menu in Studio]
3. **A human voice or face anywhere in the video.** The narration is a cloned TTS voice; the only face is an AI avatar.
   Critical Latitude's Krakatau piece (404k views in 3 days) spent 28 % of frames on a real presenter ("I'm Gwen" at
   1:05) and drew repeated "not AI" praise in comments (`critical-latitude-krakatau-2026/teardown.md`) [repo].
4. **Clause-level pauses as a writing tool.** The pipeline times graphics to narration but never inserts 0.3 to 0.6 s
   pauses after clauses that carry a number or a place.
5. **A TV-legibility check** on text size and the 5 % safe area in `graphics_qc.mjs`.
6. **Playlists built for autoplay** on TV (the series is the session). packaging-rules.md lists playlist and end screen as
   a checklist item that was unshipped on ep2 (`08-showrunner-synthesis.md` finding 3) [repo].
7. **A dialogue-to-bed ratio gate** (ebur128 checks exist; a ratio target does not).
8. **The AI disclosure decision.** YouTube requires a label for realistic altered or synthetic content, including a
   realistic synthetic person
   ([YouTube blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content/)) [data]. The repo does not
   record whether the Paul avatar videos are disclosed.
9. **A written measurement plan** tying each rule to the Studio metric that would prove it wrong.

---

## 4. What can be better

1. **Intro target.** YouTube's "Intro" metric is the share still watching at 0:30; the vendor benchmark says strong
   first-minute retention (65 %+) correlates with 58 % higher AVD and that viewers decide in about 8 s on average
   ([Retention Rabbit](https://translate.google.com/translate?u=https://www.retentionrabbit.com/blog/2025-youtube-audience-retention-benchmark-report&hl=es&sl=en&tl=es&client=srp)) [vendor].
   The owner's payoff-first hook rule matches this. Add a promise sentence by 0:15 and the US stake by 0:30
   ([1of10, first 30 s](https://1of10.com/blog/how-to-hook-viewers-in-the-first-30-seconds-of-a-youtube-video/)) [blog].
2. **Minutes 1 to 6.** MrBeast's leaked production memo treats minute 1, minutes 1 to 3, and minutes 3 to 6 as separately
   engineered blocks ([Simon Willison on the memo](https://simonwillison.net/2024/Sep/15/how-to-succeed-in-mrbeast-production/))
   [blog, but first-party]. Our lattice is uniform per minute; front-load the two strongest real clips inside minutes
   1 to 6.
3. **Open loops.** Curiosity is driven by a known information gap ([Loewenstein 1994, via summary](https://chunks.app/blog/the-curiosity-gap-explained)) [data, secondary].
   The loop table is good. Loops should be stated as facts with a missing piece, which the repo already prefers.
4. **Repetition.** The personas and real comments both punish restated material ("It repeats itself over and over",
   `szone-spacedesk-50/14-synthesis.md` comments section) [repo]. Callback, never recap: keep.
5. **Emotion.** "Emotion banked at the end" plus the warm preparedness close fits the positivity effect [data]. Keep the
   survivor vignette, then the forward-looking action line.
6. **Sound.** Keep the bed, raise the gap to +12 dB minimum, +15 dB under number-dense narration [data, judgment on 15].
7. **Captions.** Upload an accurate SRT (already in the pipeline). Do not burn word-highlight karaoke captions into docs:
   older viewers rarely use captions [data] and the repo's own shorts persona note says word-pop tested badly with 55+
   (`05-shorts.md`, persona claim) [repo, weak].
8. **Chapters.** Use YouTube chapters on docs (first stamp 0:00, at least three, each 10 s or longer, else the whole list
   fails; [YouTube Help 9884579](https://support.google.com/youtube/answer/9884579?hl=en)) [data]. No study shows
   chapters raise or lower APV [data gap]; they help TV scrubbing and re-watch. Name chapters by place and time, not by
   subject, so chapter titles do not spoil reveals.

---

## 5. Owner-stated rules that research suggests are harmful or weak

The owner asked for directness. These are the rules where the outside evidence or our own one hit points the other way.

**5.1 "Docs get atempo 1.10 like the minis" (20 Sep 26). HARMFUL.**
- Evidence: time-compressed speech hurts older listeners disproportionately; pauses restore recall [data, section 1].
  The only retained doc ran at 150.9 wpm; ep-1974 at 1.10 delivered 176.0 wpm [repo, words.json over wav]. EarthDesk's long-form winners:
  143 to 148 wpm [repo]. The owner's own atempo note says above 1.13 "sounds rushed"; the audience is older than the
  owner's ear.
- Softer alternative: docs at tempo 1.00 (native 158 to 165 wpm), and write shorter instead of speeding up. If runtime
  must shrink, cut words, not milliseconds. Keep 1.10 on the news lane only as a test arm (section 8).

**5.2 "No broadcast, radio or archive audio anywhere in the hook" (22 Sep 26). WEAK as written.**
- Evidence: the owner's reason ("if only 40 % wait till it starts at 10 secs") is not measured on disk; there is no
  retention curve for ep2 or ep-1974. The only hit opened on an archive anchor line by about 2.5 s. For an audience that
  watched these events live, the real broadcast sound is the strongest authenticity cue we have [judgment]. The owner is
  right that muddy audio under a spoken hook hurts intelligibility for older ears [data on background sound].
- Softer alternative: narrator line one at 0:00 (keep), then allow one clean, loudness-matched archive line of 3 s or
  less between 0:05 and 0:15, captioned on screen, only if it is intelligible on a TV speaker. Test it against the
  narrator-only hook on the next two docs using the 0:30 intro metric.

**5.3 Paul's presenter circle on docs (21 Sep 26). HARMFUL for trust, and moot if Paul retires.**
- Evidence: synthetic face, lip motion not driven by the words, sits on screen for the whole video; realistic synthetic
  people need a disclosure label; AI suspicion is the main niche trust tax [data + repo].
- Softer alternative: remove the circle from docs now. Keep the brand bug instead. Revisit only with a real human host
  (section 7).

**5.4 "Talk like a third grader" (20 Sep 26) and "4th-grader readable" (script-scaling.md). WEAK.**
- Evidence: plain words help, but condescension is rated demeaning by older adults and does not help comprehension
  [data, elderspeak]. The owner's real complaint ("quarter to five", "Oxford English", riddles) is about clarity, not
  reading level. The same rule produced the "Same town. One mile to the west." fragments he then banned.
- Softer alternative: "Plain spoken American: common words, literal times and numbers, one idea per sentence, adult
  content and adult respect. Keep the real term and define it once." That keeps every example the owner gave.

**5.5 Humanise rule 7 ban on the thesis opener ("this is the story of"). WEAK.**
- Evidence: ep2, the only hit, uses it (`07-refute-skeptic.md` item 20) [repo]. No outside evidence against a one-line
  orientation sentence; YouTube-creator guidance says clarify the promise by 0:15 [blog].
- Softer alternative: allow one orientation sentence before 1:00 in documentaries; the ban stays for anywhere later.

**5.6 Humanise rule 8 "No rhetorical questions" plus the 2026-09-14 "no chapter-exit questions" decision. WEAK.**
- Evidence: information-gap curiosity is the strongest documented retention mechanism in this study [data, secondary];
  niche transcripts run 0 to 5 spoken questions each (refutation item 21) [repo]; FORMAT.md rule 3 still requires them.
- Softer alternative: at most 3 genuine open-fact questions per doc, 2 per mini, each answered within the next chapter;
  no questions addressed to the viewer ("have you ever..."). This is the showrunner's recommendation the owner declined.

**5.7 Mini-storms END CTA spine, verbatim ("If you enjoyed this video, like and subscribe for more! I truly appreciate
it... Good day.") plus the "where are you watching from" beat near 1:00. HARMFUL for the tail and weak up front.**
- Evidence: 0 of 12 niche top performers end on a subscribe ask; the owner's own Format C already replaced it with one
  soft line [repo]. The last 20 s should hand the viewer to an end screen [data]. An early comment ask at about 1:00
  lands inside the intro window the whole channel is fighting for.
- Softer alternative: move "where are you watching from" to the pinned comment only (the owner's upload routine already
  pins it). Close in 10 s or less: one line naming the next video, then the end screen over the brand card.

**5.8 Must-keep 15 s avatar CTA at 85 to 95 % in every video. KEEP the placement, CHANGE the asset.**
- Evidence: late placement protects AVD; it is the right call for retention. The weak part is the asset: an AI face
  selling a book, with no stated credentials (`szone-spacedesk-50/14-synthesis.md` section 6 item 3) [repo].
- Softer alternative: keep the window. Replace the avatar clip with a 10 to 12 s narrator-voiced card (the book cover,
  the QR, "first link in the description") until a real host exists.

**5.9 Graphics type scale (DESIGN.md section 3). HARMFUL on TV.**
- Evidence: 19 to 22 px labels versus a 24 px TV minimum and 36 px default at 1080p [data].
- Softer alternative: raise the floor to 28 px, labels 30 px, body values 36 px; keep the three-tier contrast by
  raising the top tier too.

**5.10 "Info beat every 2 to 3 s on graphics" (script-scaling.md) and "max 3 s of no change" (DESIGN.md). WEAK for 65+.**
- Evidence: older listeners need processing time [data]; the owner's own review wanted ambient motion, not more facts
  (LEARNINGS 21 Sep 26 item 1).
- Softer alternative: motion every 2 to 3 s (ambient, as the owner asked), a new fact every 5 to 8 s, and never a new
  on-screen fact while the voice is saying a different number.

Rules I checked and found sound: payoff-first hook; no roadmap of the structure; no recap; named agencies and people on
screen; US stake inside 60 s; feet, miles and Fahrenheit; one named victim per tragedy; spelling gate on thumbs; no
fake chyrons; late CTA; B-roll muted by default; narration above every bed; the preparedness close.

---

## 6. The combined ruleset ("best of both")

KEEP = already in the repo and supported. CHANGE = in the repo, amended. NEW = not in the repo.
Every rule names its test.

**Voice and pace**
1. CHANGE. Docs narrate at tempo 1.00 (native pace; ep2, the retained doc, measured 150.9 wpm). News lane stays 1.10 until the
   test in section 8 reads out. Test: `word_budget.py` probe at the shipping tempo; config `tempo_by_prefix`.
2. NEW. After any sentence carrying a death count, a date plus place, or a number that matters, insert a 0.4 to 0.6 s
   pause (a written `hold` of that length or a TTS break). Target 1 per 20 to 30 s of narration. Test: count gaps of
   0.35 s or more in words.json per minute.
3. KEEP. Sentences 10 to 22 words, joined by and / but / because / so; 10 to 15 % may run 25 to 35 words as fact
   chains, split only at the TTS layer. Test: grader census.
4. CHANGE. Register: plain spoken American, adult content, no child register. Keep the real term, define it once in 12
   words or fewer, reuse it 3+ times. Test: grader flags any definition-less term and any condescending simplification.
5. KEEP. Literal clock times with AM/PM; feet, miles, Fahrenheit, dollars; US landmark comparators.
6. CHANGE. Numbers: exact for the record (deaths, dates, dollars); rounded for feats (weights, distances). Resolves the
   humanise rule 11 vs 23 Sep conflict. Test: grader.

**Hook and intro (first 60 s)**
7. KEEP. Sentence one pays the title and thumbnail, numbers first, spoken by the narrator at 0:00, 10 s or less.
8. CHANGE. By 0:15, one promise sentence of what the viewer will know (no list of chapters, no "in the next N
   minutes"). This resolves the script-os rule 3 conflict: a promise is allowed, a roadmap is not.
9. KEEP. US state or region named by 0:30 (tightened from 60 s), with the stake.
10. CHANGE. Optional: one clean archive line of 3 s or less between 0:05 and 0:15, captioned, only if intelligible on a
    TV speaker. A/B against narrator-only (section 8).
11. KEEP. Real clip with motion inside the first 5 s; date and place popfig in the first second.
12. NEW. Target: 70 % or more still watching at 0:30 (the Studio "Intro" metric), 55 % or more at 1:00. Below that on
    two videos in a row, the next script's hook is rewritten before anything else changes.

**Structure and retention devices**
13. KEEP. One dominant question; consequence before mechanism; escalating stakes; biggest reveal in the final act.
14. KEEP. Loop table: one episode loop, one loop per act, every loop paid. Callback, never recap.
15. CHANGE. Open questions: at most 3 per doc, 2 per mini, each a real open fact answered in the next chapter; never
    addressed to the viewer. Replaces FORMAT.md rule 3 and the 2026-09-14 "no chapter-exit questions" decision.
16. KEEP. A real clip (broadcast, public domain, survivor, 911) every 45 to 60 s.
17. NEW. Minutes 1 to 6 carry the two strongest real clips of the episode after the hook's. Test: edit_script marks
    them.
18. KEEP. Acts 3 to 6 min; chapter blackout 0.6 to 0.9 s or a hold, never both.
19. CHANGE. Graphics: continuous visible motion always; a new fact every 5 to 8 s, not 2 to 3 s; no new on-screen number
    while the voice says a different one. Test: `beat_density.py` motion check stays; add a fact-spacing check to the
    grader.
20. KEEP. One thesis opener ("this is the story of") allowed before 1:00 in docs only.

**On-screen text and picture (TV first)**
21. CHANGE. Minimum text 28 px at 1080p; labels 30 px; body values 36 px; headline 52 px and up. Test: `graphics_qc.mjs`
    fails any rendered text under 28 px.
22. NEW. All text inside the 5 % safe area (96 px sides, 54 px top and bottom at 1080p). Test: `graphics_qc.mjs`.
23. KEEP. One text element per zone; narration words, narration order; glass under text over footage.
24. CHANGE. Remove the Paul presenter circle from docs now; minis follow once section 7's test starts.
25. NEW. Upload an accurate SRT on every video; no burned-in karaoke captions on docs.

**Sound**
26. CHANGE. Dialogue at least +12 dB above bed and ambience in every 15 s window, +15 dB under number-dense narration.
    Test: extend the existing ebur128 window check to report the difference.
27. KEEP. B-roll muted by default; one voice at a time; banned sounds gated by hash.

**CTA, close and length**
28. KEEP. Ebook CTA at 85 to 95 %, hinge tease before and payoff after.
29. CHANGE. CTA asset: 10 to 12 s narrator-voiced book card until a real host exists. Owner-gated (asset swap).
30. CHANGE. Close is 10 s or less: fact plus dated forward line, then "next: <title>", over a 15 to 20 s end screen
    pointing at the next video in the series playlist. No like/subscribe spine; comment prompts live in the pinned
    comment. Test: metadata checklist plus end-screen click-through in Studio.
31. NEW. Length cap 25 min for docs unless the retention curve on the last two docs is flat past minute 15. Test:
    `word_budget.py` target.

**Measurement discipline**
32. NEW. No rule changes on videos under 1,000 views or 100 retention-curve viewers; log them, do not learn from them.
33. NEW. Every video gets the section 8 pull at 48 h and 7 days, logged in `ops/tracker.json`.

---

## 7. The future format: partially face-included intros, Paul retired, "The Warning Hour" kept

**What the evidence says**
- Human voices are rated more trustworthy than synthetic ones [data]; older adults are less able to spot synthetic
  voices, so a synthetic face that is later discovered costs more trust than it earned [judgment].
- In this niche, the fastest recent breakout on our topic (Critical Latitude, Krakatau) used a real presenter for 28 % of
  frames and was praised as "not AI"; the Szone same-avatar-every-topic channel drew "Who is this guy? ... I'm thinking
  AI" comments (`szone-spacedesk-50/14-synthesis.md`) [repo].
- The only face-vs-faceless dataset I found covers short-form video (7,431 videos; face-on-camera took 84 % of the 100k+
  hits) ([The Content Labs](https://thecontentlabs.app/blog/faceless-vs-face-on-camera-data-study)) [vendor, short-form
  only]. There is no good public long-form study; treat face-in-intro as a hypothesis to test.
- YouTube's July 2025 "inauthentic content" update targets mass-produced, low-variation output, not faceless or AI-assisted
  production as such ([Gulf News on the policy](https://gulfnews.com/technology/youtube-updates-monetisation-policies-ai-and-repetitive-content-ban-begins-july-15-1.500192660);
  [policy explainer](https://moshion.app/resources/youtube-demonetization-ai-faceless-channels)) [data, secondary].
  A real human presence and original analysis are the safest side of that line.
- Realistic synthetic people need the altered-content label; a real person on camera does not
  ([YouTube blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content/)) [data].

**Recommended shape** [judgment]
1. The brand stays the constant: "The Warning Hour" name, sonic spine, bug, palette, graphics grammar, preparedness
   close. The face is a contributor to the brand, not the brand.
2. The face never opens the video. Sentence one stays the narrator's payoff over real footage (rule 7). The host
   appears between about 0:15 and 0:45 for one or two sentences: who they are, why the viewer can trust this
   (a real credential or a real reason: "I've read every NWS assessment of this outbreak"), and the promise sentence.
3. After the intro the host returns only at act seams (5 to 10 s, at most 3 times) and in the CTA slot. The body stays
   narrated over footage, which is what the audience came for.
4. The voice problem: a real host on camera with a cloned TTS narrator is a mismatch viewers will hear. Either the host
   records the narration (best for trust), or the host is clearly a different person ("a presenter") from the narrator.
   Do not put a real face on the TTS voice.
5. Paul retires in steps, never all at once: (a) remove the circle from docs (now); (b) swap the CTA avatar for a
   narrator-voiced book card (rule 29); (c) the new host takes the CTA slot first (lowest-risk position, 85 to 95 %),
   then the intro.
6. Humanise rule "never I" must change for the host segments only: first person is natural for a human host. The
   narrator track keeps the rule.

**How to test it without tanking retention**
- YouTube's built-in A/B test (Test & Compare, now called A/B Testing) compares only titles, thumbnails, or both, and
  scores them by watch time share ([YouTube Help 16391400](https://support.google.com/youtube/answer/16391400?hl=en);
  [YouTube Help 13861714](https://support.google.com/youtube/answer/13861714?hl=en_ID)) [data]. It cannot test an intro,
  a voice, or a presenter inside the video. You can test a host face in the thumbnail with it.
- For the intro itself, use a sequential, matched design:
  1. Stage 1 (CTA slot only, 2 docs): host in the CTA; compare the retention-curve drop across the CTA window against the
     avatar CTA on prior docs (same position). Pass: drop across the CTA no worse than the avatar's.
  2. Stage 2 (Shorts, cheap): 6 to 10 Shorts, alternating host-first vs footage-first openings on matched topics; read
     "Viewed vs swiped away" per Short. Pass: host-first within 5 points of footage-first.
  3. Stage 3 (docs, ABAB): alternate host-intro and narrator-only intros on four consecutive docs of similar topic
     weight and length. Compare the Studio Intro metric (0:30), 1:00 retention, and relative retention against the
     "typical" band. Pass: host arm at least equal on 0:30 and 1:00 across both pairs.
  4. Kill switch: if a host-intro doc's 0:30 retention falls 10 points below the channel's typical band, the next doc
     reverts to narrator-only.
- Small samples are the risk: with our view counts, decisions need at least 100 viewers in the retention curve per video
  (YouTube shows key moments only at 100+ views, [YouTube Help 9314415](https://support.google.com/youtube/answer/9314415?hl=en)).

---

## 8. How to measure

**Pull per video, at 48 h and 7 days** (Studio, Content, video, Analytics, Engagement, plus Advanced mode)
1. Audience retention curve, exported (absolute and relative). Note the typical-retention band.
2. Key moments: Intro (share at 0:30), top moments, spikes, dips, continuous segments, each with its timestamp.
3. Retention split: new vs returning, subscribed vs not (where available).
4. AVD and APV by device type (TV vs mobile vs computer) and by viewer age.
5. Traffic source: impressions, CTR, and AVD per source (Browse, Suggested, Search).
6. End-screen element click rate; card clicks; the CTA window: share of starters still present at the CTA start, and
   the drop across its 15 s.
7. Log each in `ops/tracker.json` beside the script's rules version, tempo and hook type.

**Channel targets for this format** (vendor and blog benchmarks, not YouTube's; YouTube publishes none)
- Docs 15 min and longer: 35 to 45 % APV is strong ([prepublish benchmarks](https://prepublish.ai/blog/youtube-retention-benchmarks-2026);
  [vidIQ](https://vidiq.com/blog/post/increase-audience-retention-youtube/)) [vendor]. Our one hit sits at 40.92 %.
- Minis 8 to 12 min: 40 to 50 % APV is strong [judgment]. Our best minis sit at about 30 to 35 % on under 300 views.
- Intro: 70 % or more at 0:30 [blog: "below 70 % in the first 30 s, nothing later matters",
  [socialrails](https://socialrails.com/blog/youtube-audience-retention-complete-guide)].

**A/B plan**
- Built-in: Test & Compare / A/B Testing covers titles and thumbnails only, measured by watch time share. That is true
  as of the current Help pages [data]. Use it on every doc with 2,000+ expected impressions (it cannot resolve at our
  mini impression levels; `07-refute-skeptic.md` item 28 [repo]).
- In-video variables (tempo, hook type, archive line, host intro, CTA asset, text size) need sequential tests:
  - Match pairs on topic weight, length band (plus or minus 3 min) and publish slot.
  - Change one variable per pair. Run ABAB, not AB, to cancel drift.
  - Primary metric: 0:30 and 1:00 retention for intro variables; APV and relative retention for pace and text size;
    drop across the CTA window for CTA variables.
  - Minimum sample: 100 viewers in the curve per video; ignore anything below.
  - First queue: (1) tempo 1.00 vs 1.10 on docs; (2) narrator-only hook vs narrator plus 3 s archive line; (3) avatar CTA
    vs book card; (4) host intro (section 7).
- Shorts as a cheap pre-test for openings: "Viewed vs swiped away" per Short, matched topics
  ([prepublish explainer](https://prepublish.ai/blog/viewed-vs-swiped-away-youtube-shorts)) [vendor].

---

## Sources not used for decisions
- Faceless-channel monetization blogs and AI-voiceover vendor pages were read for context only; none is cited for a rule.
- The "chapters raise retention" claim found in several blogs has no data behind it
  ([teleprompter.com guide](https://www.teleprompter.com/blog/youtube-audience-retention)); chapters are recommended
  above for navigation, not retention.
