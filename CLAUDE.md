# CLAUDE.md — storm-market (US weather/disaster documentary channel)

Faceless YouTube channel: **narrated US weather/natural-disaster retrospectives** (tornado,
hurricane, blizzard; expand MoE-style later — Dark Horizon model). US-English, 13–23 min episodes.
**Separate from JP-market** — no shared code, only the same external tool pattern.

## Why this niche (validated 2026-07-21, references/)
- Proven small-channel outliers: SkyWhisper 13 videos → 441K avg views in 9 months ($6.69 RPM);
  Dark Horizon 23 videos → 271K avg. Formula teardown in `references/script-teardown.md`.
- Per-video economics beat cadence: quality > volume. Target 2–4 episodes/month.

## Graphics & editorial taste (owner review of ep3 v2, 2026-07-29 — 2/10)
- **Motion graphics must have motion.** No frozen full-frame hold. Every composition carries a
  continuous element across its whole window; measured by `beat_density.py` — target zero
  compositions with a motionless stretch ≥ 4s (ep3 v3 ships at 0/38, worst gap 1.6s).
- **SHOW, don't make the viewer "look at stuff."** Put the thing in the middle or across the
  whole RHS the way ep2 does. A stat asserted as text over b-roll is a miss.
- **Any spatial claim gets a MAP.** "400 miles", "seven hours", "three states" — a map, not
  cloud footage. ep3's `g-lone` is the reference; it also shows the pattern for fitting a
  route onto a real map plate (anchor on measurable landmarks, fit on the mileage column).
- **No ambiguous labels.** "what they knew" and an unexplained cone were both flagged. Name
  the thing on screen: "WHAT THEY EXPECTED · ROPE FUNNEL" vs "WHAT ARRIVED · A WALL OF DEBRIS".
- **The picture must not contradict the voice.** ep3 narrated March 2025 over 1925 wreckage
  photos for 27s. If no asset exists, build an honest designed card — never fabricate footage.
- **Match ep2's anatomy, and CHECK it — don't assume it.** Owner: *"I'm damn sure you didn't
  check. You assumed it."* **Never edit ep2. It is shipped.**
- **Cut for retention.** Segments and clips do not deserve long lengths by default.
- Reference floors from the shipped cuts: ep2 = 187 windows / 10.0s median / 2 picture gaps.
  Uncovered picture gaps in the dozens is a bug, not a style.

## The formula (from measured teardowns — follow, don't reinvent)
- Hook in 10–15s: cold-open on found footage/audio OR present-tense stat. Thesis/foreshadow line
  at 60–90s that the whole video pays off.
- ~129–148 wpm delivered (pocket-TTS + Pharaoh ref lands here natively — no atempo needed).
- Stats through the middle (each translated to human scale), **emotion banked at the END**
  (survivor vignettes as the close). Location-by-location "march" structure for tornado eps.
- Meteorology-explainer layer every episode (the net-info-gain wedge + reused-content safety).
- Titles: "The [Superlative] [Disaster] Ever Recorded — [Place] [Year]". Thumbnails: cinematic
  AI disaster shot + bold place/year text.
- Net-info-gain sources (differentiator): NWS Service Assessments, NIST reports, NEXRAD archive
  re-plots, 911 audio, day-after newspaper archives. At least 2 facts per episode no competitor video has.

## Voice (locked 2026-07-21)
- **Kyutai pocket-TTS, cloned from `assets/voice/pharaoh_wisdom_bearer.mp3`**
  (md5 2d8ea8f14763932f3f76da67d7fd1612, ElevenLabs "The Pharaoh" @ 0.98 speed, 159 wpm ref).
  Delivered pace ≈ 129 wpm — in the niche's 136±10 target zone. No atempo by default.
- Invoked via JP-market's venv, tools stay external (config.yaml `external.*`):
  `<external.pocket_venv_python> <external.tts_clone_py> --text-file ... --out ... --voice <external.voice_ref>`
- TTS-safe text: spell out ALL dates/times/numbers ("five forty-one PM", never "5:41 PM");
  no paired dashes; sentences under 24 words; full stops = hard breaks (write flowing connective
  sentences, not chopped fragments).

## Footage rules (claim-proof stack — never violate)
- Spine: **US-govt public domain** (NOAA/NWS/NHC, FEMA media library, USGS, Coast Guard) — no
  usage cap, courtesy credit in description. + Pexels/Pixabay stock. + self-made radar/map
  graphics (NEXRAD archive data). + AI b-roll (LTX / z-image via DeAPI).
- 911 audio + FEMA survivor interviews + govt hearings = the emotional layer. PD, claim-free.
- News footage (AP/Getty/network): sparingly, short (3–4s/use), narrated over, courtesy credit
  in description — expect Content ID revenue claims on those segments (claims ≠ strikes); never
  build a segment that dies if claimed. **Rehook cadence (owner 2026-07-26): a REAL clip
  (broadcast/PD/survivor) every 45–60s — core audience 40–70+ saw these events live; stock only
  fills between real clips.** Full rule in DESIGN.md.
  **Broadcast variety rule (owner 2026-07-26): keep broadcast pulls SHORT and MEANINGFUL —
  length is editor judgment (a few seconds, not 12s+ single pulls; "4,4,4" was an example, not
  a formula); vary sources, cuts, and chapters; never reuse the same broadcast cut twice; grade
  all broadcast/private-rec clips with a unified look (stock/PD exempt). Re-read the clip's
  provenance.csv row BEFORE wiring it — era-mismatch/"backup only" notes disqualify.**
- **Storm-chaser footage: NEVER without a license** — they claim and strike aggressively.
  Includes independent streamers/videographers (Oldshue class), not just chasers by job title;
  credit ≠ license; never disguise a source (grain/crop/short-cut) to sneak UNLICENSED footage
  past detection. (Grain/grade on legitimately-usable assets to unify the look stays fine —
  the sin is obfuscating provenance, not styling.)
- NO AI-generated "witnesses" or fabricated survivor quotes, ever. Real quotes come from NWS
  service assessments / news archives, shown as on-screen text with attribution.
- Reused-content safety = scripted original narration with analysis. A clip reel is a channel killer.
- **SFX is a LIBRARY, not a mandate (owner 2026-07-26):** `assets/sfx/` holds reusable beds
  (rain/wind loops, siren recordings, rumble, crickets). The editor CHOOSES per episode whether
  and which to use — never hardcode an SFX layer into future episodes. When used: volumedetect
  the source, compensate gain, verify the layer post-render (LEARNINGS item 7).

## Pipeline (hyperframes-heavy, minimal code — deliberate contrast to JP-market)
**Read `DESIGN.md` before any episode work — it is the editing architecture (owner-settled
2026-07-22): timeline-is-master, typed edit script (narration / hold / insert / graphic),
per-segment TTS, LLM-as-editor placement, muted-clips default, owner gate on every insert.**
Per episode in `episodes/<slug>/`:
1. `edit_script.md` — typed segment list (see DESIGN.md) + per-beat visual intent. Owner signs
   off design BEFORE paid spend or bulk sourcing. **Length planning: narration words =
   target_total_minutes × 0.9 × ~158** (measured 2026-07-26: ep1 manifest ground truth 153.5 wpm,
   ep2 probe 159-168 — the old "137" figure was stale/wrong; ALWAYS probe-TTS 2 segments and
   recompute before finalizing script length).
2. TTS **per narration segment** → wavs + per-segment words.json (faster-whisper).
3. Sourcing: agent downloads all clips itself (archive.org/FEMA/NOAA/yt-dlp/stock-fetch/NEXRAD);
   2-3 candidates per key beat, frame-checked. Owner only confirms `insert` clips (audio-carrying).
4. Compose `index.html` **directly as a hyperframes composition** — the agent authors the edit
   like a human editor (JS/WAAPI animation ONLY — CSS @keyframes disables fast-capture). Assets
   in `episodes/<slug>/media/`.
5. Render: **`scripts\render.cmd <slug> <draft|full>`** — the whole recipe (version pin, both
   timeout env vars, `--workers 3`, log + exit-code marker) is baked in; launch it DETACHED
   (Start-Process, see the script header — quote the space-containing path). E2E-tested
   2026-07-27. Don't hand-type npx render commands anymore; don't run other heavy sessions
   during a final render. 20-min ≈ 30–60 min on this box (GTX 1650 + 16GB); ep2's 28-min full
   took ~75 min at 2 workers.
6. QC gates, in order (all mandatory before render):
   a. **Graphics/pacing self-audit (AI judgment, owner order 2026-07-23):** re-walk every
      graphic, text card, quote, and clip as a viewer — landing / idling / minor fix? — and
      apply fixes. Info beat every 2-3s on graphics; pacing baselines in DESIGN.md are
      guidance for reasoning, never script-enforced.
   b. `scripts/lint_timeline.py` **exit 0 — HARD gate** for deterministic checks only:
      missing media, windows, audio overlap, and the no-repeat rule (reuse needs
      `data-callback="reason"`, max 2 uses, last-90s recap zone exempt). It also PRINTS a
      pacing report for step (a)'s reasoning — report lines never fail the run.
   c. **The static suite — all green BEFORE any render** (see "HARD RULE — the render is the
      LAST step"): `sweep_episode.py`, `blank_scan.mjs`, `beat_density.py`, `graphics_qc.mjs`.
   d. Per-composition snapshot of anything NEW or changed (stage into a bare page, seek,
      screenshot 4-6 points, subagent reads them) — never a whole-episode frame sweep.
   e. Post-render only: `scripts/verify_render.sh <episode-dir> <basename>` — blackdetect,
      silencedetect, freezedetect on the finished mp4 (JP checklist: anatomy, garbled text,
      blank frames, captions; sync rule: frame must not contradict narration).
   **Never claim an editorial rule "fixed" from your shot map — re-run the lint + self-audit
   on the final index.html; verify the artifact, not your memory (ep1 v2 RCA).**
   **The defects the owner names are a SAMPLE, not the set — dig for the rest yourself.**
7. Deliverables per render, unasked: **`python3 scripts/master_deliverables.py
   episodes/<slug> <render-basename>`** — one command produces the −14 LUFS master
   (`-c:v copy` + measured gain, verified) AND the SRT (calls build_srt.py; requires the
   `nx-*` narration audio-id convention). E2E-tested on ep2 2026-07-27. Plus updated
   `metadata.md` (titles,
   description, tags, chapters, AEO/SEO block, Education metadata: category Education, type
   Overview; credits; socials/handles) at publish time.
- Long episodes: chunk renders only if a single render proves unstable — don't pre-build JP's
  chunk machinery until an episode actually needs it. From ep2 on, AUTHOR compositions as
  sub-compositions (one per act) so per-act re-renders are native (owner-approved 2026-07-26).
- **Draft-proxy review loop (owner order 2026-07-26): every review cut ships as a DRAFT render
  first** — `scripts\render.cmd <slug> draft [out-basename]` (draft = crf 32 / 15fps / 3
  workers baked in; measured 2026-07-26 on ep1 17:17 comp: 21m 16s vs 39m 32s full; 258 MB vs
  1775 MB; 1080p15, text fully readable).
  Studio preview cannot realtime-play 15+ min media-heavy comps — don't offer it for review.
  Full-quality render ONLY after owner approves the draft.

## HARD RULE — worktree isolation (owner correction 2026-07-28, ep3 v1 violation)
**NEVER build or edit in the main checkout. EVERY episode/feature session starts with
`git worktree add .worktrees/<task> -b <branch>` BEFORE the first file write.** The main
checkout is shared by parallel sessions; v1 of ep3 was built directly in it while another
session held uncommitted changes — owner-flagged, do not repeat. First action of any
storm-market session: `git worktree list` + `git status` → if you are in the main checkout
and about to write, STOP and make a worktree.

## HARD RULE — the render is the LAST step (owner correction 2026-07-29, ep3 v3)
**Never use a render as a diagnostic tool.** ep3 v3 burned nine render attempts; three were
killed for defects that were sitting in the code the whole time. Owner: *"no fucking 9000
renders on any fucking video ever."*

Run ALL of these to green BEFORE launching a render, every time:
```
python3 scripts/sweep_episode.py episodes/<slug>     # 10 structural checks
node    scripts/blank_scan.mjs   <abs episode dir>   # pre-render blackdetect
python3 scripts/beat_density.py  episodes/<slug>     # motionless stretches
node    scripts/graphics_qc.mjs  .                   # from the episode dir
python3 scripts/lint_timeline.py episodes/<slug>     # exit 0, hard gate
```
Plus, for any NEW or changed composition: stage it into a bare page with gsap, seek its
timeline, screenshot 4-6 points and have a subagent read them (never Read frames into the
main context). That loop caught eight defects in two new graphics in about ten minutes.

**QC the CODE, not a frame sweep** (owner, same round): *"You can't really do a one hundred
and five image frame sweep for graphics… You should check the code because this is HTML. How
can I have garbled text? in HTML."* A 105-frame render sweep is not a QC method for graphics.

**Owner timestamps against an older cut get mapped by YOU, from git** — never ask the owner to
re-point them. `git show <sha>:episodes/<slug>/index.html` into a temp dir + `clip_report.py`
resolves them exactly.

**Cap every source asset at the composition's resolution before wiring it — and the gate
that enforces it is `scripts/media_budget.py`, called by `render_preflight.py`.** This rule
existed in prose through TWELVE failed ep3 v3 renders while seven clips sat at 1920x1440 in a
1920x1080 comp and 240 MB of source fed 90s of screen time. A rule with no gate is a
suggestion. The gate checks three numbers and refuses the render: clip resolution vs the
composition, clip length vs the longest window that uses it, and total megabytes to decode.
`scripts/optimize_clips.py <episode> --apply` fixes all three (originals move to media/_orig/).

`ffprobe deadline with code 0` means SLOW, never corrupt. The deadline is 120s per probe,
hardcoded in hyperframes 0.7.64 (`deadlineAtMs: Date.now() + 12e4`) — no env var raises it.
The probe itself is fast (3.18s worst serial, 8.18s at six-way concurrency, measured with
hyperframes' own `-count_packets` arguments by `scripts/probe_timing.py`); it blows the
deadline queued behind the extract stage decoding oversized source. An idle box does NOT
prevent this — attempt 12 failed with the machine quiet.

**Launch a render as a harness-tracked background job.** `Start-Process` from a foreground
tool call is killed when that call returns: attempt 11 logged its preflight line and died
silently, no marker, no mp4. Verify liveness by COMMAND LINE
(`Get-CimInstance Win32_Process | Where CommandLine -like '*hyperframes*'`), never by a
process count — stale node/chrome processes read as a healthy render and cost an hour.

## Rules inherited from the owner's other channels (apply here from day 1)
- Preview gate is PROCESS: post preview path in one line and PARK; owner's chat approval resumes.
- Never claim/infer owner approval. Design lock before paid generation.
- Paid API railguards (budget caps, dry-run first, incremental progress) per global CLAUDE.md.
- No recap/outro; descending stakes order; micro-loops every 30–45s; no-spoiler metadata.
- All git/gh as `sidhartha1s`. PRs small, rebase-merge, docs sweep in same PR.
- python3 never python. Node ≥ 22 for hyperframes.

## Learnings discipline (owner order 2026-07-22)
**`LEARNINGS.md` is updated the same session as any owner correction or measured surprise** —
hyperframes gotchas, sourcing findings, editorial rules. Read it before every episode build,
alongside DESIGN.md. When patterns stabilize (~2-3 episodes), promote the stable workflow into
a proper skill via /skill-creator — do not hand-write a SKILL.md before then.

## Open items (video 1)
- Pilot topic: Joplin 2011 or 2011 Super Outbreak (owner to pick).
- hyperframes version pin: set on first render (start at 0.7.64 — validated on this box).
- Channel name/branding: TBD.
- LEARNINGS.md starts at episode 1 — every owner correction lands there same session.
