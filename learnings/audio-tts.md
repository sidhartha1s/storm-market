# learnings/audio-tts.md: audio and TTS: pace, pocket-TTS, whisper, levels, beds, mixdown

Newest first. New entries go at the top, under this line. Superseded lines point at their current home.

## 14 Oct 26 - ep-palm-sunday-1965: one small.en transcript that matches the script does not prove the words are heard right

- **What happened:** the owner watched draft v2 and heard Paul's first clip differ from the script. The build check
  (small.en, one pass) had read all 26 words. "Garbled or misspelled words, whisper it" was his criterion for the SPOKEN
  words of every Paul clip; the lead read it as lettering in the picture and checked the wrong thing.
- **Measured:** four recognisers (tiny.en, base, small, small.en; no prompt, `condition_on_previous_text=False`,
  temperature 0, word probabilities) on the mounted clip: first word "City" came back as "Equity" (tiny.en, 0.03) and
  "Activity" (small), and at 0.16 and 0.14 in the two that still wrote "City". Omni's own audio reads "City" at 0.75 to
  0.96. Speech starts 0.04 s into the clip, so the converter (OpenVoice V2, `convert_one.py`) has no sound before the
  first word. Converting with a 0.6 s lead-in of the clip's own room tone and cutting it off again gives "City" at
  0.82 to 0.98 in all four, same level (mean -16.4 dB).
- **Also found by the same pass:** clip 5's `data-srt-label` held an older sentence than the one Paul speaks (the
  script file had the spoken one). The caption would have been wrong. Fixed in `index.html`.
- **Do next time:** (1) a converted clip or segment whose first word starts inside the first 0.3 s gets a lead-in
  before conversion; (2) every Paul clip is read by all four cached recognisers from the RENDERED draft audio, and any
  word under 0.60 or any disagreement goes on the review page with a player, since the lead cannot hear; (3) each
  clip's `data-srt-label` is compared with the script line by a command, not by eye.
- **Narration, same four-recogniser pass (123 segments):** 46 segments had two or more recognisers disagree with the
  build transcript; most are number formats and place names. Steady ones worth an ear if the owner asks: "teletype"
  at 1043.30 s (read as "teletime" / "teletyne"), "Starke" at 345.64 s (read as "star"), "County A's" at 371.45 s.
  List: `episodes/ep-palm-sunday-1965/.qc-tmp/speech-read/sweep.log` (git-ignored).

## 12 Oct 26 - ep-palm-sunday-1965: a voice conversion after TTS leaves every words.json stale, and the transcriber moves words on the new voice

- **What happened:** `tts_episode.py` wrote each words.json from the TTS wav. The conversion to the owner's voice then
  wrote new wavs over the same names and nothing re-transcribed them. Twelve graphics were cued and frame-checked
  against the old stamps before `sweep_episode.py` printed "words.json is older than its wav" for all 15 segments.
- **Measured:** the speech did not move. The loudness envelopes (10 ms hop) of the unconverted and converted wavs line
  up within 0.01 s over each whole segment and around each word. Re-transcribing the converted wavs still moved word
  stamps by up to 0.49 s in 7 of 15 segments, nearly all on a word that follows a pause ("City", "Named", "Many").
  Against the acoustic edge (30 dB under the segment's peak RMS) the old stamp was the closer one at 11 of the 16 word
  edges measured; the worst old stamp was 0.17 s off a word start, the worst new one 0.32 s.
- **Rule:** any step that rewrites a narration wav re-transcribes it before it reports done; the step order is in
  CLAUDE.md "Voice".
- **Observation, not a rule yet:** a transcriber stamp on a word that follows a pause can sit up to 0.32 s off the
  sound. Where such a cue matters, check it against the loudness envelope of the wav. No script does this today; the
  cue rule's home is `references/mg-quickref.md` "Text doctrine".
- **Homograph probe without Praat:** "lives" in "lost their lives" measured as the noun with LPC formants on the final
  wav (F1 peak about 877 Hz, vowel about 0.16 s; the short-i signature is F1 under about 500 Hz and about 60 ms).
- **Open:** the conversion script still sits in an El Reno scratch folder outside the tracked repo (`ops/tasks.md` "Housekeeping").

## 2026-09-27 - ep-enderlin: the "lyvz" respelling voiced "livs"; plain "lives" is correct; gate shipped 2026-09-28

- **Owner:** "lives" (lost their lives) came out /lɪvz/, must be /laɪvz/. The TTS copy had respelled it "lyvz".
- **Measured** (pocket-TTS + atempo 1.10, "Three people lost their ___ that night.", Praat F1 of the vowel after /l/):
  "lyvz" F1 peak 506 Hz / 60 ms, "lighvz" 509 / 55, "laivz" 512 / 80 = /ɪ/. Plain "lives" 769 Hz / 215 ms,
  "lyves" 693 / 195, "lighves" 735 / 235 = /aɪ/. "lie-vz" is /aɪ/ but adds a syllable (whisper: "liveys").
  All 9 enderlin segments re-recorded with plain "lives" measured /aɪ/ (F1 peak 739-882 Hz, 225-305 ms).
- **Rule:** the noun "lives" after their/took/take needs no respelling. A respelling ending in a bare "y"+consonant
  cluster ("lyvz") reads as short /ɪ/. Decide a respelling by probing candidates and measuring F1/duration
  (/aɪ/ opens to F1 about 650-850 Hz for 150-250 ms, /ɪ/ stays under about 500 Hz), not by guessing. Pocket-TTS looks
  deterministic (z1-s1 re-record: silence timings identical to the microsecond up to the changed word), so a line
  probably cannot be re-rolled for a shorter read; 3 of 9 re-records ran 5.9-9.2 % long and need index.html retiming.
- **Gate (2026-09-28):** `references/homographs.md` is the single home for the word list (both senses + a hint,
  scoped to the ones actually known to go wrong in TTS narration on this channel); `scripts/homograph_scan.py`
  reads it, scans an episode's narration through the same `tts_episode.parse_segments` every other narration tool
  uses, and prints one line per flagged word (occurrence count + its first sentence) so the builder probes it
  before the render. WARN, never FAIL, matching how `flag_words.py` treats a soft hit — whether an occurrence
  actually needs a respell depends on the sense used in that sentence, which a script cannot judge, so hard-failing
  every hit would block a render on lines that are already correct. Wired into `run_gates.py` right after
  `flag_words.py`. The rule above is what the gate exists to enforce for every future homograph, not just "lives":
  a blind respelling caused this defect, the plain word was right, and a respelling is picked by measurement, never
  by guess.

## 2026-09-22 - ep-1974 shipped 17:30 against a 22:00 target: three guesses stacked

- **Measured:** script 3,027 words; raw TTS 18.4 min (165 wpm native, not the 152 assumed); atempo 1.10 made it
  16.7 min of voice (181 wpm is script words over voice minutes; words.json over the wav measures 176.0 wpm); non-voice time 48 s, not the 2.2 min constant. 22:00 became 17:40, then
  17:30 after the owner's cuts. Owner: "you under delivered the minutes of last video."
- **Why:** the budget line in edit_script.md multiplied a guessed pace by a guessed overhead, and the probes the
  plan asked for were made but never fed back into the count. wordcount.py's own footer printed 20.3 min and the
  script was locked anyway.
- **Fix:** `scripts/word_budget.py` measures pace from probe wavs at the shipping tempo and takes the real
  non-voice seconds; it FAILS outside target +/- 1 min. Nothing goes to full TTS while it fails. Checked against
  ep-1974's own audio: it predicts 16:53 for the shipped script (actual 17:30; the two probes ran 4 % faster than
  the episode average, so probe with two segments of different sentence length).
- **Rule of thumb at this voice and tempo:** about 180 words per delivered minute; a 25:00 documentary needs
  about 4,400 narration words.

## 2026-09-22 - ep-1974 draft 2 review: narrator opens the video, banned audio is gated by hash, holds need a reason
- **A banned sound came back under its other filename.** `wind-loop.mp3` was marked banned in `assets/sfx/provenance.md` on
  16 Aug 26; the builder mounted its source file `02_wind_ominous_steady.mp3` three times (4:00, 4:58, 10:06). A ban written
  as prose on one filename is a suggestion. Fix: `assets/sfx/BANNED.md5` lists banned audio by content hash and
  `lint_timeline.py` fails on a match, so a rename or a copy cannot dodge it. Proven: the old timeline fails with three
  findings, the new one passes. A future ban is one line in that file.
- **A `hold` whose only content is a bed reads as a mute stretch.** Owner at 5:03 to 5:08: "its mute, with only bgm. why?"
  It was an authored 4 s hold on a lone still with the banned wind under it. A hold earns its place only with diegetic sound
  that belongs to the picture (a siren over the siren, the tape over the tape). Otherwise close it to a 0.3 s breath.
  Two more holds remain (3.0 s at 237.09 s and 3.5 s at 599.71 s in the new cut); both sit under a moving map and were not named.

## 20 Sep 26 — El Reno v3 post-mortem: stock footage was audible and no gate saw it
- Owner rejected v3 partly for "a lot of audio for the stock footages". Root cause: `<video>` elements
  mounted with neither `muted` nor `data-volume`. hyperframes plays such a track at 1.0, but
  `audio_levels.py` treated "no data-volume" as muted by convention and skipped them, so the levels gate
  passed a mix with unlevelled clip audio under narration.
- Fix (this PR): `audio_levels.py` now skips a video only when it carries `muted` (or data-volume 0) and
  levels every other video at its data-volume, default 1.0; `sweep_episode.py` check 5e fails any `<video>`
  that declares neither. Verified: ep6 trips on `kb-radarloop` (silence-muxed, harmless, but undeclared);
  ms-krakatau-sirens passes both gates with the same 19 audible elements as before.
- Rule: every `<video>` says what its audio is. `muted` for b-roll, `data-volume` for inserts and the CTA.

## 15 Sep 26 — first two Format C (rolling update) builds, ms-indonesia-four-volcanoes + ms-hawaii-lowell-outages
- **Pronunciation gate before timing.** Read every proper noun back from the whisper words.json after TTS (Arupadhatu came out
  "Aeropoda 2-1", KIUC as "Kaiyo Sea", Haena as "Hina"). Respell phonetically in the narration blockquote only, re-synthesise, then
  time. Doing it after the timeline existed cost a full mechanical retime (~40 min). Probe-TTS the name list first next time.
- **words.json must be younger than its wav.** transcribe ran on one native wav before atempo in a crashed chain; the tell is
  words end > wav duration. Check before cueing anything.

## 2026-09-08 — breaking lane v1 (br-elnino-california, /mini-storms first run)
- **Pharaoh pace on short news sentences = 158 wpm native** (1,426 words → 9:01). atempo 1.15
  pushed it to 182 wpm / 7:50 and was reverted. Measure before applying any atempo.

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts
- **Pharaoh voice ran 158 wpm native on short news sentences** (1,426 words → 9.0 min). No atempo needed
  in this lane; the 129 wpm figure is a documentary-sentence number. Measure, then decide.
- **Homographs are a TTS trap (owner 2026-09-09, "AI-slop radar"):** pocket-TTS read "I read all the comments" as
  "I red" (past tense). (Superseded 2026-09-28: "scan and always respell" was itself incomplete — a respelling
  picked without measuring can be as wrong as the plain word, see the 2026-09-28 entry above. Current home:
  `references/homographs.md` + `scripts/homograph_scan.py`.) Owner's phrases are verbatim — never paraphrase a
  line he wrote.
- **The TTS driver skips a segment whose wav exists** (`tts_episode.py --only` reuses the old file silently): delete
  the wav AND its words.json before any re-synthesis, or the "fix" never happens (Krakatau v2 c2/c7, 2026-09-10).
- **CTA first syllable clipped + post-CTA black too long (owner 2026-09-10):** CTA start was off the 30 fps grid and
  the blackout sat on the same track ending at the same instant. Fix: blackouts on their own track, CTA audio starts
  0.1 s under the black, all starts ceil-aligned to 1/30 s, dip-out 0.5 s. z1 hiss/long pauses: TTS gaps > 0.55 s
  replaced with 0.4 s digital silence via a words.json-driven ffmpeg concat, then re-transcribed.
- **A sleeping laptop kills TTS and sourcing agents silently (2026-09-09→10):** pocket-TTS hung at 4/13 segments for
  12 h with 6 orphan python processes; the sourcing agent's report never landed. After any overnight gap: check
  `audio/*.wav` count and the pool's provenance.csv before trusting either. Also: a `> TTS note` blockquote placed
  between a `##` heading and the next `###` is parsed as narration of the PREVIOUS segment by tts_episode.py — notes
  are plain lines, never blockquotes.

## Audio levels + media budget hardening (ep6, 2026-08-17)
- **Insert audibility is a FILE problem, not an attr problem.** NPR hook insert sat at
  data-volume 1.0 and was still 6.8 dB under narration — the source wav was quiet.
  Gain-normalize insert FILES to the narration median (measure with volumedetect) before the
  mixdown gate. `alimiter` boosts by default (`level=1`); pass `level=0` or check the result —
  it overshot two inserts +5 dB before correction.
- **`scripts/audio_levels.py` is the gate for this** (run before every mixdown build):
  effective dB = file mean_volume + 20·log10(data-volume); narration median is the reference;
  inserts must land ±2.5 dB of it; music beds fail if >30 dB under; beds warn when competing
  with voice. Catches the ep6 NPR defect and the ep6-v1 "score at 0.08 = silent" defect.
- **`optimize_clips.py` now escalates crf (23→27→31) until under the 150 MB media budget and
  PRESERVES audio** (aac copy-encode; silent track muxed for mute clips). The old `-an` pass
  forced a 15-clip re-mux ritual + 36-clip silent-track patch every optimize run — retired.
  Measured ep6: 51 clips crf23 = 194 MB, crf27 = 143 MB; crf27 invisible under archival grain.
  CAVEAT (ep1 session, 2026-08-24 merge): optimize_clips re-encodes from `media/_orig/`
  backups, so a rerun reverts any per-file gain fix applied after a previous pass —
  audio_levels.py catches this.

## 2026-08-15 — ep6 TTS + sourcing (measured surprises)

1. **Probe-TTS can undershoot the delivered pace by 10+ wpm.** ep6 probes measured a 137.5
   blend; the 46-segment manifest ground truth came out 149.1 wpm (ep1's 153.5 was the better
   prior). The probe segments were unrepresentatively slow-styled. Budget scripts on the
   manifest wpm of the PREVIOUS episode, then verify against the new manifest after the first
   full TTS run and expand/trim THEN — the probe only catches gross errors.
2. **QC gate that caught a real gap: diff whisper-heard words.json against the source .txt per
   segment** (normalize digits + number-words + homophones like Corps/core; flag <0.90
   similarity or >8% word-count drift). BUT verify a flag before re-synthesizing: whisper
   small.en deterministically swallowed a whole mid-file sentence (a5-s4, 6s of clean audio
   heard as one token) while the AUDIO was complete — chunk-level transcription of
   `audio/_segments/*.wav` + the concat.txt order proves which side is broken. Fix for a bad
   words.json: re-transcribe per chunk and offset by cumulative ffprobe durations
   (deterministic, exact) — do NOT re-run TTS for a whisper mishearing.
3. **tts_clone.py caches sentence chunks in `audio/_segments/` ("exists, skip").** Sidelining a
   segment's output wav does NOT force re-synthesis — the concat rebuilds byte-identical audio
   from cached chunks. To truly regenerate, clear that segment's chunk wavs too. (Also means
   text edits within a segment re-synthesize only changed sentences — cheap.)
4. **pocket-TTS intermittently dies at CUDA init/clone with a native crash** (no traceback,
   ~1 in 8 segments on the GTX 1650, same input passes on rerun). `tts_episode.py` now does one
   loud `[FALLBACK]`-logged retry per segment and hard-fails on a second consecutive failure.

## Audio mixdown as a pre-render gate (ep5 v5, 2026-08-13)
Build the full audio mix from index.html (atrim+adelay+volume+amix, normalize=0) and scan 30s
windows with volumedetect BEFORE rendering. Caught: kick hit (vol 0.6) stacking with narration
start at an act boundary = 0dB clip. Hits under speech need ~0.4. Target: mix mean ≈ -19,
window peaks ≤ -1.5. Also: sparse-keyframe warnings in the render log (dvbhawk-helipov,
calfire-itf-willhappenagain) cause freezes — re-encode with -g 30 before the next full render.

## Music policy update (owner order 2026-08-13, supersedes "never downloaded music")
Owner-provided Pixabay downloads (assets/sfx/owner-2026-08-13/) and DeAPI-generated tracks are
ALLOWED as music/SFX. Still forbidden: anything ripped from YouTube/unlicensed. DeAPI recipe:
POST /api/v2/audio/music (multipart; model AceStep_1_5_Turbo, guidance_scale exactly 1,
inference_steps exactly 8, lyrics "[Instrumental]", format mp3, max 300s) — poll
GET /api/v2/jobs/{request_id} (NOT /requests/ — that 404s). ~$0.0009 per 60s. Generated tracks
pad ~3s of tail silence — trim/fade before mounting. Keys in repo-root .env (gitignored).

## Owner pivot 2026-08-12 — cadence, sourcing, SFX, durable references
- **SFX is default-ON now** (base tone + peak swells, library/ffmpeg-synth only) — ep5 v2 shipped
  with a single wind bed the owner heard as "buzzing"; a low-volume steady loop under silence
  reads as a defect, not atmosphere. Design per scene, verify post-render.

## 2026-08-05 — ep5 kickoff: the retention lattice + script fact-QC layer (owner orders, all standing from ep5 on)
**Measured / sourced this session:**
7. **Probe-TTS: punchy prose runs SLOWER.** Long-sentence segment 158 wpm, short-sentence segment
   139 wpm, blended ≈145. Budget words at the measured blend of the episode's actual style —
   the single planning figure (158) over-budgets a punchy script by ~9%.

## ep3 v2 (2026-07-28)
- **tts_ep3v2.cmd chained transcribe stage died silently after TTS DONE** (no marker, no log lines) — give each detached stage its OWN log + exit marker; a chained `goto`-loop .cmd hides which stage failed.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)
- **SFX beds must be diegetically motivated and SHORT.** A 136s wind loop over analysis
  narration read to the owner as inexplicable "steady wind"; crickets running under a blackout
  read as "grey sound." Bed enters with the storm beat, leaves when the beat does.
- **Cold-open clips need per-beat volumedetect** — one silent source beat (towercam) muted the
  opening 3.6s of a cuts-on-audio montage.

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)
- `scripts/tts_episode.py --only` REWRITES manifest.json with only those segments — re-run a full
  pass (existing wavs skip fast) after any `--only` patch. `transcribe_episode.py` skips existing
  words.json — delete stale ones after re-TTS or timings go stale.

## 2026-07-26 — ep2 design review (owner corrections, all wired into CLAUDE.md/DESIGN.md same session)
7. **The "137 wpm" planning figure was WRONG** (caught by ep2 probe): ep1's own audio manifest
   says 2,519 words / 16.4 min = **153.5 wpm delivered**; ep2 probe segments ran 159–168 wpm.
   Plan at ~158 (superseded by `scripts/word_budget.py`, 22 Sep 26) and ALWAYS probe 2 segments before locking script length — provenance ladder in
   action: disk manifest > learnings claim. (How "137" got recorded is unresolved; possibly an
   earlier script revision's word count divided by a later duration.)

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)
7. **SFX bed volumes must compensate for source loudness — never copy the music-bed ducking
   numbers.** First v3 render shipped a completely inaudible SFX layer: sources (rain −29.7dB,
   wind −30.4dB mean) are ~15dB quieter than the ACE music beds (~−14dB), so `volume 0.05-0.14`
   buried them ~-40dB under the mix. Caught only by a differential band-energy check against the
   v2 render (same section, no SFX) — identical spectra = layer silent. Rule: `volumedetect`
   every audio source, set element volume from (target mix level − source mean), and VERIFY the
   layer post-render by differential comparison, not by assuming the keyframes worked.

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)
7. Script length = minutes × 0.9 × 137: superseded by `scripts/word_budget.py` (22 Sep 26; about 180 words per delivered minute at the doc tempo).

## 2026-07-22 — ep1-joplin full-episode build (overnight ship-it)

- **Word-count annotations in edit_script overestimate ~30%**: planned ~2,460 words / "20.4 min";
  delivered TTS = 13.2 min narration → 14.0 min episode. Pharaoh pocket-TTS runs ~137 wpm
  delivered on long segments (not 129). Next episode: target word count = minutes × 137 (superseded by `scripts/word_budget.py`, 22 Sep 26), and
  TTS a 2-segment probe before annotating the whole script.
- **TTS driver header regex must match ALL segment types carrying a blockquote** — `— narration`
  matching missed graphic-with-VO segments (a1-s2, a3-s3). Fixed: match on the segment ID.
- **120s ACE beds loop cleanly with ffmpeg `acrossfade=d=3` self-concat** — build per-act loop
  files (media/music/*-loop.mp3); no audible seam at documentary duck levels.

## 2026-07-22 — owner feedback on demo-joplin-90 (overall: "incredible")
3. **Cold-open pacing: slow is fine, silence is not.** 4s to first audible dispatch sound read as
   dead air. Fix = loudness-normalize the insert to narration level (ffmpeg loudnorm, ≈ -15dB
   mean) and bring first sound in by ~1s. Keep the cinematic visual pace — owner explicitly liked
   it; tighten the AUDIO attack, not the edit.
4. **Music is a LIBRARY, not per-episode**: assets/music/ holds owned ACE-generated beds
   (5 moods); reuse/loop/duck across episodes. Generate new moods only when the library lacks one.

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")
- Insert audio needs loudness normalization before compositing — dispatch tone-out sat at
  −26dB mean vs narration −15; normalize inserts to ≈ narration level (ffmpeg loudnorm) next time.
- Music: **DeAPI ACE-Step 1.5 XL Turbo works** (endpoint + request ids in the episode's
  media/music/provenance.txt). Prompt for "no drums" may still return beat-driven takes —
  generate 2, spectrogram-check, keep the drone.
