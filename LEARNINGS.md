# LEARNINGS.md — storm-market

Every owner correction / measured surprise lands here same session. Newest first.

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)

1. **Cadence is REASONED per clip, never defaulted**: the editor-agent must justify each hold —
   "1.5s stinger or 12s land-the-beat" is an editorial decision per beat; anything >8s needs a
   reason written in the edit script. Overlong offenders in v1: hook porch-swing, cloud shots,
   siren still at 11:05 (14.6s), outro title dwell.
2. **No visual repeats within an episode** (owner caught all three: lamp-post rain ×2,
   rain-window ×2 within 2 min, St John's facade ×2). One reuse allowed ONLY as an intentional
   callback: different crop/grade, >5 min apart, flagged in the edit script.
3. **Sync rule — the frame must not contradict the narration**: "died in the dark" over a
   daylight photo; "Walmart" over a Walgreens aerial; "1:30 PM watch" over a 22:43 UTC radar
   stamp. Named entity / time-of-day / timestamp in VO ⇒ matching visual or a neutral one.
4. **Graphics never idle**: ≤3s from graphic-on-screen to first payoff element (v1 polygon sat
   ~10s). Reveal ON the word (match cut) — owner loved the UNSURVIVABLE match cut, flagged
   CATASTROPHIC landing 5s before its word.
5. **Number reveals**: never pre-reveal in an eyebrow/fine-print (v1 spoiled 161); counter rolls
   fast then dramatically slows into the final number; secondary stat (158) appears AFTER.
6. **Lower-third sub-line readability**: dark-amber italic serif fails on busy ground — bump
   contrast/weight or give it a backing bar.
7. **Script length planning: words = target_total_minutes × 0.9 × 137** (pocket-TTS Pharaoh
   delivered rate). 20-min ask ⇒ ~2,450 narration words.
8. **Detached render (Start-Process + log poll) is the render path** — harness background tasks
   were killed by RAM pressure from orphan chromes; kill orphans before rendering. Chunked
   rendering (JP machinery) stays out until a single render of a 20-min episode actually fails.

## 2026-07-22 — ep1-joplin full-episode build (overnight ship-it)

- **Word-count annotations in edit_script overestimate ~30%**: planned ~2,460 words / "20.4 min";
  delivered TTS = 13.2 min narration → 14.0 min episode. Pharaoh pocket-TTS runs ~137 wpm
  delivered on long segments (not 129). Next episode: target word count = minutes × 137, and
  TTS a 2-segment probe before annotating the whole script.
- **TTS driver header regex must match ALL segment types carrying a blockquote** — `— narration`
  matching missed graphic-with-VO segments (a1-s2, a3-s3). Fixed: match on the segment ID.
- **120s ACE beds loop cleanly with ffmpeg `acrossfade=d=3` self-concat** — build per-act loop
  files (media/music/*-loop.mp3); no audible seam at documentary duck levels.
- **Real-radar frames carry burned-in scan times (UTC)** — any popup naming a different clock
  time contradicts the frame. Label honestly (fine-print provenance line) or match the scan.
- **NASA ASTER false-color reads as alarming red** — always add a one-line false-color
  explainer popup; the gray scar IS the story.
- **NEXRAD via GCP mirror, not AWS**: `gcp-public-data-nexrad-l2` allows anonymous listing
  (AWS bucket is GetObject-only); pyart `plot_ppi_map` creates a NEW GeoAxes (style
  `fig.axes[-1]`); velocity lives on sweep 1 (split-cut VCP), not sweep 0.
  Render script kept at `C:/nexrad-t/render_radar.py`.
- **Compaction summaries lie about artifacts** (rule 12 confirmed): "words.json exists" was
  false — always `ls` the actual files on resume before building on them.

## 2026-07-22 — owner feedback on demo-joplin-90 (overall: "incredible")

1. **Memorial/character beats: prefer a REAL photo where one publicly exists** (news/memorial
   coverage — an editorial-respect judgment per case); else make the STAT carry the emotion —
   e.g. the death toll as a rising red counter (Joplin = 161, NWS-verified; owner recalled 178 —
   always verify the number). Symbolic stock (grad cap) reads weakest of the three options.
2. **Radar/graphic beats: REAL data beats stylized animation.** Owner loved the sweep but wants
   the actual storm: render real NEXRAD Level-II archive data (AWS open data, free) for the event,
   or use NWS archived radar imagery (PD) — stylized radar only when no real data exists.
3. **Cold-open pacing: slow is fine, silence is not.** 4s to first audible dispatch sound read as
   dead air. Fix = loudness-normalize the insert to narration level (ffmpeg loudnorm, ≈ -15dB
   mean) and bring first sound in by ~1s. Keep the cinematic visual pace — owner explicitly liked
   it; tighten the AUDIO attack, not the edit.
4. **Music is a LIBRARY, not per-episode**: assets/music/ holds owned ACE-generated beds
   (5 moods); reuse/loop/duck across episodes. Generate new moods only when the library lacks one.

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")

**Hyperframes 0.7.64 gotchas (cost a lint/fix cycle each — pre-empt next time):**
- Every `<audio>`/`<video>` with `data-start` NEEDS an `id` — silently SILENT/FROZEN in render without it.
- `window.__timelines = window.__timelines || {}` before assignment (lint error otherwise).
- Root composition div needs `data-start="0"`.
- No layout-property tweens (letterSpacing) — transforms/opacity only.
- Same-track time overlap = lint error; give crossfade/blackout elements their own track.
- StaticGuard "uses data-end without data-duration" on validate = **false positive** in 0.7.64
  (reproduced on JP-market's known-good probe fixture) — ignore, don't chase.
- `hyperframes transcribe` silently produced nothing on this box — use faster-whisper via
  JP-market `.venv` with `HF_HUB_OFFLINE=1` (models cached: small.en, medium.en).

**Editorial/pipeline:**
- Word-timestamp cuts work exactly as designed: transcribe each TTS segment, cut on the word.
- Stock tonal mismatch is real: sunny clips need a static CSS `filter` grade (brightness/saturate)
  to sit in a documentary cut — grade at composition, not ffmpeg.
- Insert audio needs loudness normalization before compositing — dispatch tone-out sat at
  −26dB mean vs narration −15; normalize inserts to ≈ narration level (ffmpeg loudnorm) next time.
- Music: **DeAPI ACE-Step 1.5 XL Turbo works** (endpoint + request ids in the episode's
  media/music/provenance.txt). Prompt for "no drums" may still return beat-driven takes —
  generate 2, spectrogram-check, keep the drone.
- Grain/vignette/dust as a timeline-driven seeded canvas = deterministic and cheap; reseed ~12/s.
- Sourcing workflow pattern (5 parallel download agents + vision-verify stage) delivered 100%
  usable assets in ~14 min — keep for episodes; scale agents per act.
- Owner delegation note: insert selection was owner-delegated for the demo; REAL episodes keep
  the owner gate (frames + transcript + source, yes/no).

**QC:**
- xstack contact sheets pad undefined regions GREEN — padding, not video content; don't panic.
- Snapshot pre-render QC caught both grade issues before paying for a render — keep snapshot
  sweep (≈13 frames) as the mandatory pre-render gate; post-render frame sweep stays too.
