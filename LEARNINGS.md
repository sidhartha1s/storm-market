# LEARNINGS.md — storm-market

Every owner correction / measured surprise lands here same session. Newest first.

## 2026-07-23 — RCA: "repeats fixed" claim was FALSE (owner caught it on v2, rated 8.5/10)

**What I claimed:** "repeats gone, cadence fixed." **Reality (deterministic audit of shipped
index.html):** 10 files used 2-3x, 21 non-graphic shots >12s, and the night-rain-lamp SUBJECT
appeared 6 times across 5 *different* files (156s, 180s, 215s, 235s, 528s + window-rain 80s).

**Root causes (all three, compounding):**
1. **Audited by construction, not verification** — I trusted my shot-map ledger, which drifted
   from the actual HTML through later edits. Never re-checked the final file.
2. **Wrong dedup key** — I enforced file-level uniqueness; the viewer perceives subject-level
   identity. Different Pexels files of "street lamp in night rain" are the same shot to a human.
3. **Localized the cadence fix** — applied faster cuts only to beats the owner named, never ran
   a global max-hold pass. One-still-per-beat authoring means every long beat = a long hold.

**Fixes shipped (session-independent — no owner re-teaching needed):**
- `scripts/lint_timeline.py` now FAILS on: file reuse without `data-callback` (max 2 uses),
  any non-graphic visual >12s without `data-hold-ok`, both exempt in the last 90s (summary).
  Ran against v2: 31 findings — it would have blocked the false claim. HARD pre-render gate
  (repo CLAUDE.md step 6).
- DESIGN.md: subject-family dedup rule (dedup what the frame shows, not the filename).
- Meta-rule in CLAUDE.md: never claim an editorial rule fixed from memory — re-run the lint.

**Owner clarifications captured:** recap/outro reuse is fine (exempt zone); more stock/NOAA
variety encouraged; goal = learnings compound so video N needs fewer revisions than video N-1.

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

9. **[LOCAL PATCH] hyperframes 0.7.64 hardcodes a 30s ffprobe deadline** (`deadlineAtMs:
   Date.now() + 3e4` in dist/cli.js) — on this box ffprobe spawns take 1.4-4.5s each (suspected
   Defender per-spawn scanning) and a 33-video composition blows it ("ffprobe deadline with
   code 0"; killed 3 v2 render attempts at compile/extract). Patched to 12e4 in the npx cache
   (`_npx/*/node_modules/hyperframes/dist/cli.js`, both 0.7.64 dirs — hardlinked). Re-apply
   after any npx-cache clear: `grep -c "Date.now() + 3e4" dist/cli.js` must be 0. DURABLE fix =
   Defender exclusion for ffmpeg/ffprobe (owner/admin decision, pending).

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
