# CLAUDE.md — storm-market (US weather/disaster documentary channel)

Faceless YouTube channel: **narrated US weather/natural-disaster retrospectives** (tornado,
hurricane, blizzard; expand MoE-style later — Dark Horizon model). US-English, 13–23 min episodes.
**Separate from JP-market** — no shared code, only the same external tool pattern.

## Why this niche (validated 2026-07-21, references/)
- Proven small-channel outliers: SkyWhisper 13 videos → 441K avg views in 9 months ($6.69 RPM);
  Dark Horizon 23 videos → 271K avg. Formula teardown in `references/script-teardown.md`.
- Per-video economics beat cadence: quality > volume. Target 2–4 episodes/month.

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
- News footage (AP/Getty/network): sparingly, short, narrated over — expect Content ID revenue
  claims on those segments (claims ≠ strikes); never build a segment that dies if claimed.
- **Storm-chaser footage: NEVER without a license** — they claim and strike aggressively.
- NO AI-generated "witnesses" or fabricated survivor quotes, ever. Real quotes come from NWS
  service assessments / news archives, shown as on-screen text with attribution.
- Reused-content safety = scripted original narration with analysis. A clip reel is a channel killer.

## Pipeline (hyperframes-heavy, minimal code — deliberate contrast to JP-market)
**Read `DESIGN.md` before any episode work — it is the editing architecture (owner-settled
2026-07-22): timeline-is-master, typed edit script (narration / hold / insert / graphic),
per-segment TTS, LLM-as-editor placement, muted-clips default, owner gate on every insert.**
Per episode in `episodes/<slug>/`:
1. `edit_script.md` — typed segment list (see DESIGN.md) + per-beat visual intent. Owner signs
   off design BEFORE paid spend or bulk sourcing.
2. TTS **per narration segment** → wavs + per-segment words.json (faster-whisper).
3. Sourcing: agent downloads all clips itself (archive.org/FEMA/NOAA/yt-dlp/stock-fetch/NEXRAD);
   2-3 candidates per key beat, frame-checked. Owner only confirms `insert` clips (audio-carrying).
4. Compose `index.html` **directly as a hyperframes composition** — the agent authors the edit
   like a human editor (JS/WAAPI animation ONLY — CSS @keyframes disables fast-capture). Assets
   in `episodes/<slug>/media/`.
5. Render: `npx hyperframes@<pin> render . --gpu --browser-gpu --experimental-fast-capture=true
   --quality standard --crf 16 --fps 30` (pin in config.yaml; NEVER @latest).
   20-min ≈ 30–60 min on this box (GTX 1650 + 16GB, measured 2026-07-21).
6. QC: `scripts/lint_timeline.py` + eyeball actual frames (JP checklist: anatomy, garbled text,
   blank frames, caption issues) + owner preview gate before full render. Done = final.mp4 path
   the owner can play.
- Long episodes: chunk renders only if a single render proves unstable — don't pre-build JP's
  chunk machinery until an episode actually needs it.

## Rules inherited from the owner's other channels (apply here from day 1)
- Preview gate is PROCESS: post preview path in one line and PARK; owner's chat approval resumes.
- Never claim/infer owner approval. Design lock before paid generation.
- Paid API railguards (budget caps, dry-run first, incremental progress) per global CLAUDE.md.
- No recap/outro; descending stakes order; micro-loops every 30–45s; no-spoiler metadata.
- All git/gh as `sidhartha1s`. PRs small, rebase-merge, docs sweep in same PR.
- python3 never python. Node ≥ 22 for hyperframes.

## Open items (video 1)
- Pilot topic: Joplin 2011 or 2011 Super Outbreak (owner to pick).
- hyperframes version pin: set on first render (start at 0.7.64 — validated on this box).
- Channel name/branding: TBD.
- LEARNINGS.md starts at episode 1 — every owner correction lands there same session.
