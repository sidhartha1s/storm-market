# CLAUDE.md — storm-market (US weather/disaster documentary channel)

Faceless YouTube channel: **narrated US weather/natural-disaster retrospectives** (tornado,
hurricane, blizzard; expand MoE-style later — Dark Horizon model). US-English, 13–23 min episodes (default band, not a cap — owner ordered 30 min for ep2; confirm per episode).
**Separate from JP-market** — no shared code, only the same external tool pattern.

## Why this niche (validated 2026-07-21, references/)
- Proven small-channel outliers: SkyWhisper 13 videos → 441K avg views in 9 months ($6.69 RPM);
  Dark Horizon 23 videos → 271K avg. Formula teardown in `references/script-teardown.md`.
- Per-video economics beat cadence: quality > volume. Target 2–4 episodes/month.

## Graphics & editorial taste
- **Motion graphics must have motion.** No frozen full-frame hold. Every composition carries a
  continuous element across its whole window; measured by `beat_density.py` — target zero
  compositions with a motionless stretch ≥ 4s (ep3 v3 ships at 0/38, worst gap 1.6s).
- **SHOW, don't make the viewer "look at stuff."** Put the thing in the middle or across the
  whole RHS the way ep2 does. A stat asserted as text over b-roll is a miss.
- **Any spatial claim gets a MAP.** "400 miles", "seven hours", "three states" — a map, not
  cloud footage. Reference: `references/editing-patterns/ep3-map-route-fit.html` (fitting a
  route onto a real map plate: anchor on measurable landmarks, fit on the mileage column).
- **No ambiguous labels.** "what they knew" and an unexplained cone were both flagged. Name
  the thing on screen: "WHAT THEY EXPECTED · ROPE FUNNEL" vs "WHAT ARRIVED · A WALL OF DEBRIS".
- **The picture must not contradict the voice.** ep3 narrated March 2025 over 1925 wreckage
  photos for 27s. If no asset exists, build an honest designed card — never fabricate footage.
- **Match the shipped panel anatomy, and CHECK it — don't assume it.** Owner: *"I'm damn sure
  you didn't check. You assumed it."* The reference comps live in
  `references/editing-patterns/`. Episode folders get DELETED after publish, so docs never
  cite `episodes/<slug>/...` for a pattern — copy shipped patterns into that folder same
  session. **Never edit a shipped episode.**
- **Cut for retention — but duration is EARNED.** Video beats may run
  **up to 12-15s** when the clip genuinely matches the narration; motion earns time. Cadence
  anxiety is retired; per-beat matching is not. **Stills: 3-6s MAX, always with motion
  (zoom/pan), then cut — "this is not a PowerPoint presentation."** Prefer video over stills
  everywhere; maximum video segments.
- **Content-ID discipline for long pulls:** any claim-risk clip (news/broadcast/YouTuber) held
  longer than ~12-15s needs narration over it; TRANSCRIBE such clips first and cut at the best
  moment. News clips WITH their commentary audio are allowed — the audio mix (TTS alone, clip
  audio alone, both interleaved) is a per-cut editor decision, made with reasoning.
- **SFX is default-ON:** one base
  tone/bed across the episode + swells at peak moments (~every 45-60s as the script peaks).
  Library (`assets/sfx/`), owner-provided Pixabay downloads (`assets/sfx/owner-2026-08-13/`),
  DeAPI-generated tracks (keys in repo-root `.env`, recipe in LEARNINGS.md), or ffmpeg-synthesized.
  NEVER YouTube-ripped/unlicensed music; audio Content ID is fatal (a claimed clip can be cut; a
  claimed music bed poisons the whole video). Verify the layer post-render (volumedetect) AND
  pre-render via the full audio-mixdown gate (LEARNINGS.md).
- **Grading:** unified subtle grade template on all broadcast/news/private clips (anti-flag +
  look consistency); stock/PD exempt. When doubtful about a grade or a claim risk — stop and ask.
- **Audio-first open:** the episode MUST open with audio — mid-action, high
  curiosity, high impact. A clip without audio is dead; never open on black or a silent visual.
- **Risers/builds land WITH the narration:** a riser peaks and ends exactly
  where the narration line stops (or a few ms after) — never still climbing after the voice is
  done. Hits under speech mount ~0.4 volume (0.6 stacks to 0 dBFS — measured ep5).
- **Non-narration audio budget:** ~30s of external audio in a 32-min episode
  is failure-thin. Source assertion AUDIO like clips: 911 calls, presser sound, survivor voice,
  sirens/ambience — and per-act music with real character (known-good tracks + recipe live in
  `assets/sfx/deapi/README.md`; owner Pixabay pack in `assets/sfx/owner-2026-08-13/`).
- **Siren terminology (owner 2026-08-13, STANDING):** "siren" = tornado/civil-defense siren
  (the wailing air-raid type, e.g. `soundreality-civil-defense-siren-128262.mp3`); "weewoo" =
  ambulance/police/firetruck siren. When the owner asks for a siren, it is the tornado siren
  unless he says weewoo.
- **Preview = 98% production quality (owner):** a "rough draft" preview is a full-quality cut at
  draft encode settings — never a placeholder. Before ANY render: full audio-mixdown listen +
  hook watch (the experience pass); a known-below-spec layer means STOP and report, not render.
- **Script never references its own structure (owner):** no "concluding", "summarizing", "in
  this video" — reads as a seam, instant viewer skip.
- **Graphics text discipline (owner, ep3-ep5 recurring):** proper case, never all-lowercase;
  reduce text per frame (one idea at a time, no disjointed stat spray); a graphic holds until
  its point fully lands (never cut early) and never starts before its trigger moment or after a
  blank gap; ≥3 type tiers per designed card (graphics_qc flat-type gate: small <26 / mid /
  big ≥52 px must all appear).
- **Sourcing bar (owner 2026-08-12): find 3-4x more candidates than you need.** Millions of PD
  and news clips exist — "short of clips" means stop everything and source better. Use
  PySceneDetect (validate install first) to split long sources into scene cuts instead of
  burning agent passes; spread the cuts ACROSS the episode, never back-to-back.
- Reference floors from the shipped cuts: ep2 = 187 windows / 10.0s median / 2 picture gaps.
  Uncovered picture gaps in the dozens is a bug, not a style.
- **Chapter blackout is mandatory (owner order 2026-07-31; durations re-set 2026-08-16).** A
  hard black cut between acts is what makes ep1/ep2 read like a documentary; ep3 dropped it.
  Owner's duration table: **0.6–0.9s = chapter break · 1.0–1.3s = dramatic punctuation ·
  1.5s+ = dead air** (hook-end void: 1.5s). Seamless butt-cuts need no blackout at all. See
  DESIGN.md "Chapter blackout" — every builder hand-places act-boundary blackouts.
- **On-screen text rules (owner, ep6 v2 review 2026-08-22) — DESIGN.md "On-screen text rules":**
  one text element per zone per window (`overlap_check.mjs` v2 enforces), one fact one instance,
  no decorative eyebrows, reveals in narration order/wording, `.glasscard` under any text over
  footage, small text never carries a moment alone (BFMG). Dates/figures = Abril `popfig`
  popups (red, ≤3 words, mid-screen), never colour-block date cards.
- **No visible windows, ever (owner 2026-08-21):** every scheduled/background command runs via
  `scripts/run_hidden.vbs`; a render or ritual that opens a visible Chrome/cmd window is killed
  on sight and reported, not retried. hyperframes 0.8.x opens a Windows Terminal tab per
  ffprobe/ffmpeg spawn on this box (measured 2026-08-23, LEARNINGS "ep6 ship") — pin stays
  0.7.109 until an upstream version spawns them hidden; full renders on the stale pin use the
  owner's logged override `RENDER_PIN_STALE_OK=1` (`scripts/ep6_full_task.cmd` is the pattern).
- **Panels slide out, never vanish (owner order 2026-07-31).** RHS fact panels exit `x:980,
  autoAlpha:0` timed to the hard cut (comp duration ≥ host window). ep3 v5 removed the exit as a
  one-off; ep4+ restore the timed slide-right exit. See DESIGN.md §5 "Panel exit TIMING".
- **Ship a compressed HEVC master.** Full renders are ~5 GB at crf16/30fps; run
  `master_deliverables.py … --hevc` for a ~2 GB GPU-HEVC master (visually lossless), or render
  a smaller single pass with `RENDER_CRF=20` + author at 24fps. See LEARNINGS.md "Render size".
- **Upload the 1440p file, not the 1080p master (owner order 2026-08-24).** Deliverables
  produce `-master-1440p.mp4` by default — that is the YouTube upload artifact. The 1080p
  copy-master stays the archive; the 1440p upscale can be deleted after upload.

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
- News footage (AP/Getty/network): transcribe first, cut at the best moment; up to ~12-15s per
  pull when narrated over (short 3-5s cutters still the default rhythm), courtesy credit in
  description — expect Content ID revenue claims on those segments (claims ≠ strikes); never
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
   off design BEFORE paid spend or bulk sourcing. **Script is written on the retention lattice —
   `references/script-scaling.md` (owner-ordered 2026-08-05): read it first.** It carries the
   scaling method (acts, not stretched beats), the pre-TTS fact-QC layer (zero open `[verify]`
   markers before TTS), and the insert-transcription rule. **Length planning: narration words =
   target_total_minutes × 0.9 × ~158** (measured 2026-07-26: ep1 manifest ground truth 153.5 wpm,
   ep2 probe 159-168 — the old "137" figure was stale/wrong; ALWAYS probe-TTS 2 segments and
   recompute before finalizing script length; ep5 measured a 139–158 spread by sentence style,
   blended 145 — punchy prose runs slower, budget on the blend). **The CTA hinge is named in
   the design (segment before / segment after, est. timestamp) — DESIGN.md "CTA contract".**
2. TTS **per narration segment** → wavs + per-segment words.json (faster-whisper).
3. Sourcing: agent downloads all clips itself (archive.org/FEMA/NOAA/yt-dlp/stock-fetch/NEXRAD);
   2-3 candidates per key beat, frame-checked. Owner only confirms `insert` clips (audio-carrying).
4. Compose `index.html` **directly as a hyperframes composition** — the agent authors the edit
   like a human editor (JS/WAAPI animation ONLY — CSS @keyframes disables fast-capture). Assets
   in `episodes/<slug>/media/`. Mount the CTA from `config.yaml channel.cta` (staged into
   `media/cta/`, wiring in DESIGN.md "CTA contract").
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
      LAST step"): `sweep_episode.py`, `blank_scan.mjs`, `beat_density.py`, `graphics_qc.mjs`,
      `overlap_check.mjs` v2 (text collisions incl. comp-internal + mid-tween, duplicate
      facts), `audio_levels.py` (exit 0 — insert/narration/bed level gate, run before every
      mixdown build). `sweep_episode.py` also FAILS a missing/misplaced CTA (config window,
      duration, own audio, SRT label, md5 vs `assets/cta/`).
   d. Per-composition snapshot of anything NEW or changed (stage into a bare page, seek,
      screenshot 4-6 points, subagent reads them) — never a whole-episode frame sweep.
   e. Post-render only: `scripts/verify_render.sh <episode-dir> <basename>` — blackdetect,
      silencedetect, freezedetect on the finished mp4 (JP checklist: anatomy, garbled text,
      blank frames, captions; sync rule: frame must not contradict narration).
   **Never claim an editorial rule "fixed" from your shot map — re-run the lint + self-audit
   on the final index.html; verify the artifact, not your memory (ep1 v2 RCA).**
   **The defects the owner names are a SAMPLE, not the set — dig for the rest yourself.**
7. Deliverables per render, unasked: **`python3 scripts/master_deliverables.py
   episodes/<slug> <render-basename> [--hevc] [--no-2k]`** — one command produces the −14 LUFS
   master (`-c:v copy` + measured gain, verified), the SRT (calls build_srt.py; requires the
   `nx-*` narration audio-id convention), AND — default ON (owner order 2026-08-24) — the
   **1440p YouTube upload file** (`-master-1440p.mp4`: hevc_nvenc p7 cq22 lanczos upscale, ~3.5 GB / 16 Mbps
   for 28 min, audio bit-copied; a 1440p upload gets YouTube's higher VP9 bitrate tier —
   visibly cleaner playback than the same content uploaded at 1080p; ~8 min at 3.5×
   realtime on the GTX 1650 (ep2 v2 measured 2026-08-29), skip with `--no-2k`). Drafts
   and previews stay 1080p as-is. `--hevc` adds a ~2 GB GPU-HEVC master (hevc_nvenc,
   audio bit-copied). Both GPU steps need the PATH ffmpeg 8.1.1, not the 8.1.2 shared
   build — see LEARNINGS.
   E2E-tested on ep2 2026-07-27. Plus updated
   `metadata.md` (titles,
   description, tags, chapters, AEO/SEO block, Education metadata: category Education, type
   Overview; credits; socials/handles) at publish time. **Description contract: the FIRST URL
   is `channel.cta.first_link` (Paul says "first link in the description" on camera) + the
   "📘 The book mentioned at mm:ss" line; no chapter marker at the CTA (DESIGN.md "CTA contract").**
- Long episodes: chunk renders only if a single render proves unstable — don't pre-build JP's
  chunk machinery until an episode actually needs it. From ep2 on, AUTHOR compositions as
  sub-compositions (one per act) so per-act re-renders are native (owner-approved 2026-07-26).
- **MG library-first (owner order 2026-08-27):** `library/` holds the motion-graphics library —
  `catalog-index.json` (in-house exemplars + snippets + ~195 storm-triaged official HyperFrames
  catalog items, 82 with local source in `library/official/`), browseable via
  `python3 -m http.server 8765` from `library/` → `http://localhost:8765/gallery/`. Before
  hand-authoring any graphic: search the index (grep/read — it's one JSON) and/or
  `npx hyperframes catalog --query "<intent>"`, copy the closest match into the episode,
  hand-retune per beat. `npx hyperframes add <name>` lands new official items into
  `library/official/` (hyperframes.json paths) — it never writes into an episode; copying
  into `episodes/<slug>/compositions/` is always a hand step. A worked example of the full
  flow lives at `library/inhouse/examples/joplin-stat-panel.html`. Scratch-authoring allowed
  with a one-line reason in edit_script.md. The generator tripwire is untouched — the
  library is starting points, never builders.
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

## HARD RULE — the pin stays current, and the machine enforces it (owner 2026-08-14,
supersedes the 2026-07-29 warn-only ruling)
**The pin policy is deliberate** — renders run the version that was reviewed; upstream ships
~1.6 releases/day with behavior changes in minor bumps (0.7.81 cut the ffprobe deadline 4x;
0.7.107 changed the hidden-audio mix). **The refresh is no longer manual.** Three pieces:
- **`render_preflight.py`** (now actually called by `render.cmd`, both modes): pin drift
  between config.yaml and any live `npx hyperframes@<pin>` = hard fail (exit 5); **stale pin
  = hard fail for FULL renders (exit 6)**, loud warning for drafts; npm unreachable NEVER
  blocks (currency unknown ≠ stale).
- **`scripts/pin_ritual.py`** — the unblock. Scripted A/B: renders demo-joplin-90 at the
  candidate version, diffs against the committed baseline record (`scripts/pin_baseline.json`
  + cached baseline mp4 for SSIM), and on identical metrics (duration / blackdetect map /
  RMS ±0.2 dB / SSIM ≥0.99) bumps config.yaml + every live scripts/*.cmd and refreshes the
  baseline. Metric drift = exit 3, NO bump — a human reads the changelog and decides.
  ~10-13 min when the baseline record is current, ~25 when it isn't. Run it from a worktree;
  commit + PR the bump it makes.
- **Read the changelog anyway** when the ritual bumps across many versions — a passing demo
  A/B proves render identity, not that no new flag or timeout matters for a 32-min episode.
Pin history: 0.7.64 → 0.7.81 (2026-07-29; **ffprobe deadline 120s → 30s** — margins shrank
4x) → 0.7.107 (2026-08-14, hand A/B) → ritual-managed from here. A newer version can be
STRICTER, not just better.

## HARD RULE — do not write code for what reasoning already does (owner 2026-07-29)
**"Keep code headache low."** Before adding a script, a check, or a flag, answer one question:
*can an agent reading the artifact do this at least as well?* If yes, it is a docs line, not a
file. Run this gate the way `/simplify` is run — on every script this repo grows, including
the ones written to fix a crisis.

Code earns its place when the check is **mechanical, repeated, and must never be forgotten**:
deterministic numbers, hard gates, batch transforms, anything guarding money or a 40-minute
render. Reasoning owns everything that needs taste or context: *is this photograph the right
photograph, does this cut land, does the picture contradict the voice.*

The tell for a script that should have been a docs line: it needs a hand-tuned stoplist to
stop being wrong. That is judgment wearing a regex.

**TRIPWIRE (owner 2026-08-02, amended 2026-08-16):** any script that AUTHORS episode HTML —
generates, chooses, or alters cuts, holds, graphics, on-screen text, asset picks, or the
relative design of timings in `index.html` or `compositions/*.html` — is forbidden. Delete it
on sight. Every editorial decision is hand-authored by the session via Edit/Write with
per-cut judgment (the ep1/ep2 method). This is why ep1/ep2 were 9/10 and generator-built ep3
was 2/10. The deleted generators (`build_ep3.py`, `gen_*.py`) are the banned pattern; do not
resurrect it. **The test: if the script must know what a beat MEANS, it is authoring.**
**Allowed (owner 2026-08-16): one-shot MECHANICAL TRANSFORMS of already-hand-authored
decisions** — global retimes, uniform attribute arithmetic, mechanical renames — under ALL of
these conditions: (1) deterministic and content-blind (pure math/renames, zero editorial
choice); (2) the session reviews the resulting diff; (3) the full static gate suite passes
after (lint_timeline exit 0, blank_scan, beat_density, graphics_qc, overlap_check, driver
check, media_budget); (4) the script is one-shot — run from scratch space, never committed,
gone after use, never promoted into pipeline machinery; (5) the transform is declared in the
PR body. A transform that fails verification gets root-caused, not re-run blind.
Checkers that READ episode HTML (sweep/lint/blank_scan/beat_density/graphics_qc/
overlap_check) remain always fine — they check, they don't author.

Applied to this repo's own gates, 2026-07-29:
- `media_budget.py` **stays code** — three numbers, run before every render, guards against
  repeating twelve failed renders. Exactly the mechanical-and-must-not-be-forgotten case.
- `optimize_clips.py` **stays code** — a repeatable ffmpeg batch over sixteen files.
- `probe_timing.py` **deleted** — it was a one-shot diagnostic. Its answer now lives in
  LEARNINGS.md, and a number that has already been measured is not a tool.
- `narration_picture_check.py` **kept the era check, dropped the place check** — the era test
  is mechanical (a spoken year against an asset's era). The place test needed a growing
  stoplist of words that are not towns and still produced thirteen false positives to three
  real ones. Whether a photograph of the next town along the track belongs under this sentence
  is an editorial call — it belongs in the segment read, not in a regex.

## HARD RULE — the render is the LAST step (owner correction 2026-07-29, ep3 v3)
**Never use a render as a diagnostic tool.** ep3 v3 burned nine render attempts; three were
killed for defects that were sitting in the code the whole time. Owner: *"no fucking 9000
renders on any fucking video ever."*

Run ALL of these to green BEFORE launching a render, every time:
```
python3 scripts/sweep_episode.py episodes/<slug>     # 15 structural checks incl. the CTA gate
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

`ffprobe deadline with code 0` means SLOW, never corrupt. The deadline is 30s per probe,
hardcoded since hyperframes 0.7.81 (`deadlineAtMs: Date.now() + 3e4`; 120s back in 0.7.64) —
no env var raises it.
The probe itself is fast (3.18s worst serial, 8.18s at six-way concurrency, measured with
hyperframes' own `-count_packets` arguments, measured 2026-07-29); it blows the
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
- **The ebook CTA is must-keep (owner 2026-08-30):** every episode, 30–40% in, hook > CTA >
  payoff, from `config.yaml channel.cta` — DESIGN.md "CTA contract". Never skipped or moved.
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
