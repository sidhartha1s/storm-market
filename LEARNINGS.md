# LEARNINGS.md — storm-market

Every owner correction / measured surprise lands here same session. Newest first.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)

**Editorial (owner corrections):**
- **Broadcast variety:** TV/broadcast pulls stay short and MEANINGFUL — never a 12-24s single
  pull; length itself is editor judgment ("4,4,4" was an owner example, not a formula — don't
  hardwire it). Different sources, different cuts, different chapters; never reuse the same
  broadcast cut twice. Grade every broadcast/private-rec clip (unified grade = transformational
  + look-glue); stock/PD exempt.
- **SFX beds must be diegetically motivated and SHORT.** A 136s wind loop over analysis
  narration read to the owner as inexplicable "steady wind"; crickets running under a blackout
  read as "grey sound." Bed enters with the storm beat, leaves when the beat does.
- **Bare static stills >10s = retention risk.** Motion video tolerates 12-15s; a bare still
  doesn't. Split with another visual or overlay an info beat — but never force filler.
- **Insert/AV cuts on sentence boundaries via transcript, always.** 8-14s, complete meaningful
  statement (emotional or informational), never mid-sentence. "80% is the cut; the last 20% is
  knowing what to leave out."
- **Every act's episode outro carries the episode number** (match ep1: "Episode N — Title").
- **Cold-open clips need per-beat volumedetect** — one silent source beat (towercam) muted the
  opening 3.6s of a cuts-on-audio montage.

**Composition contract:**
- **Exit animations must end fully gone** (autoAlpha:0 + overshoot the slide). `x:660` on an
  820px panel left a stuck sliver for ~1s until the host window closed — owner caught it at
  three timestamps. Snapshot host-end−0.5s to verify every panel exit.
- Panel gradients: `box-sizing:border-box`, text starts inside the SOLID zone; every
  text-over-media element gets a dark backing chip.

**Process:**
- **Provenance notes are load-bearing at COMPOSE time.** cullman-aftermath.mp4 carried a
  "2017-era footage" warning in provenance.csv and still got wired into a 2011 documentary
  (twice). Rule: before wiring any clip, re-read its provenance row; a "backup only"/era
  mismatch note disqualifies it.
- **Owner meta-principle (from 6 channels):** do NOT pre-constrain the editor-AI with scripts
  and hard-coded rules before it sees the problem. Scripts = deterministic checks only (lint);
  pacing/grading/placement stay AI judgment per-case. "Do not draw lines before AI even sees
  the problem."
- **QC density:** 18 frames on a 28-min video is not a review. Dense sweep ≈ 1 frame / 15-20s
  plus targeted checks on every region you changed.

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)

- **Snapshot `--timeout` covers ONLY runtime init; page navigation is a separate 10s default**
  that kills media-heavy comps with "Navigation timeout of 10000 ms exceeded". Fix: env var
  `PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000` (found in cli.js `resolveDiagnosticNavigationTimeoutMs`).
  Applies to snapshot AND render — set it on every invocation for big comps.
- **Harness background Bash tasks die at the 120s default timeout / on compaction** — long
  snapshot/render jobs go DETACHED: `Start-Process cmd.exe '/c <ABSOLUTE path>.cmd'` writing a
  log + `done.marker`, polled via wakeups. Relative .cmd path silently no-ops (process spawns,
  script never runs). One npx call per .cmd — a second `call npx` after the first never ran.
- **Snapshot's video-frame extraction can fail per-frame** ("could not be extracted — will appear
  black/stale") while the composition is fine — the RENDER captures live playback and is unaffected.
  Verify suspects by ffmpeg-extracting frames from the source media at the mapped offsets
  (data-start/trim math), not by rerunning snapshot.
- `scripts/tts_episode.py --only` REWRITES manifest.json with only those segments — re-run a full
  pass (existing wavs skip fast) after any `--only` patch. `transcribe_episode.py` skips existing
  words.json — delete stale ones after re-TTS or timings go stale.
- yt-dlp `--print` implies `--simulate` — subtitle downloads silently skip; run without `--print`.
- Subagents can go idle without reporting (2 of 6 tonight) — poll with SendMessage pings; if still
  silent, verify their on-disk output yourself and take over the reporting step.
- `.lt-loc` lower-third relied on text-shadow alone — unreadable over white map graphics; all
  text-over-media cards get a dark backing chip (`background: rgba(5,8,12,0.78)`) from ep2 on.

## 2026-07-26 — draft-proxy render validated (timed on ep1 v3d, 17:17 comp)

`--quality draft --crf 32 --fps 15 --workers 3`: **21m 16s vs 39m 32s** standard (46% faster),
258 MB vs 1775 MB. 1080p at 15fps — quote/graphic text fully readable in extracted frames;
review-quality confirmed by eyeball. Capture dominates render time (fps halving ≈ halves capture;
encode/pipeline overhead is the floor), so don't expect draft to scale below ~half. This is THE
review path per CLAUDE.md; full-quality render only after owner approves the draft.
Monitor gotcha: "render finished" check via `tasklist ... node.exe` is too broad — other node
processes keep it true forever; watch for the log's "Render complete" line instead.

## 2026-07-26 — ep2 design review (owner corrections, all wired into CLAUDE.md/DESIGN.md same session)

1. **Broadcast-clip rehook cadence**: core audience 40–70+ watched these disasters on live TV —
   real broadcast/news/PD/survivor clips every 45–60s as rehooks; stock fills BETWEEN real clips,
   never the reverse. Network clips 3–4s, narrated-over, credited (credit ≠ license, ≠ claim immunity).
2. **Claims-vs-strikes ruling (Oldshue)**: network material = revenue claims (budgeted OK);
   independent chaser/streamer footage = manual strikes (channel-fatal) → NEVER-without-license
   covers streamers too. Disguising a source (grain/crops/short cuts) to dodge Content ID is
   prohibited — structural immunity, not obfuscation. The story can be narrated over our radar
   re-plots + network tower-cam instead of the streamer's frames.
3. **Burned-in radar timestamps: map to narration OR crop out of frame** — cropping now an
   approved alternative to honest-labeling when the clock isn't the story. UTC-vs-local trap stands.
4. **Cold-open montage grammar**: clips enter MID-ACTION (the hit, not wind-up/aftermath), cuts
   land ON the audio event (scream/crash/dispatch line), 911 audio as one scene in the chain.
   Never re-rip clips from competitor videos — trace to original sources (their edit carries
   their Content ID fingerprint + VO bleed); refs are a shot list only.
5. **Conditional-fact rule**: a proposed distinctive fact ships ONLY if verification confirms it
   (e.g. "Wrangler plant never reopened") — drop entirely on failure, never soften into "reportedly".
6. **Runtime**: 13–23 min band is a default, not a cap — owner explicitly ordered 30 min for ep2
   (high-demand topic). Word formula scales: minutes × 0.9 × wpm (see 7).
7. **The "137 wpm" planning figure was WRONG** (caught by ep2 probe): ep1's own audio manifest
   says 2,519 words / 16.4 min = **153.5 wpm delivered**; ep2 probe segments ran 159–168 wpm.
   Plan at ~158 and ALWAYS probe 2 segments before locking script length — provenance ladder in
   action: disk manifest > LEARNINGS claim. (How "137" got recorded is unresolved; possibly an
   earlier script revision's word count divided by a later duration.)

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)

A 4-agent Workflow sweep (media-contract / timeline-contract / sync-audit / snapshot-eyeball)
before the v3 render found 10 issues, 3 blockers — **keep this sweep as a standing pre-render
step for every episode**:
1. **`rain-wall-parked-cars.mp4` showed a MALAYSIAN license plate** — shipped in v1 AND v2
   unnoticed. Lesson: vision-verify every inherited/act-dir clip too, not just newly sourced
   ones; foreign tells (plates, signage, architecture) are the #1 stock hazard. Replaced with
   `rain-wall-downpour-generic.mp4` (anonymous pavement closeup). Tainted file kept on disk for
   v2 provenance but must never be re-used.
2. **`data-media-start` on a clip broke snapshot frame extraction** (funnel beat rendered black
   in snapshots though the file was healthy). Robust pattern: pre-trim the segment into its own
   file (`tornado-funnel-hold-4s.mp4`) and drop data-media-start when a beat uses a mid-file window.
3. **CDN GSAP caused 10s navigation timeouts** in validate/snapshot — vendor `gsap.min.js` into
   the episode dir and reference it relatively. Deterministic + faster.
4. Honest-label rule reconfirmed: watch-beat popup must narrate the radar's burned-in clocks
   ("watch 1:30 PM → by 5 PM this appears"), never caption footage with a time it contradicts.
5. Namecards need scrim bars (`display: table; margin: auto` per line — inline-block puts
   name+sub on ONE row; transform-centering fights GSAP y-tweens).
6. Every intentional dead-frame beat gets an explicit track-4 blackout section — an undocumented
   coverage gap is indistinguishable from a bug in review.
7. **SFX bed volumes must compensate for source loudness — never copy the music-bed ducking
   numbers.** First v3 render shipped a completely inaudible SFX layer: sources (rain −29.7dB,
   wind −30.4dB mean) are ~15dB quieter than the ACE music beds (~−14dB), so `volume 0.05-0.14`
   buried them ~-40dB under the mix. Caught only by a differential band-energy check against the
   v2 render (same section, no SFX) — identical spectra = layer silent. Rule: `volumedetect`
   every audio source, set element volume from (target mix level − source mean), and VERIFY the
   layer post-render by differential comparison, not by assuming the keyframes worked.

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
