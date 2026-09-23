# CLAUDE.md: storm-market (The Warning Hour, US weather and disaster documentaries)

Narrated US weather and natural-disaster retrospectives, US English. Separate from JP-market: no shared code, only
the same external tool pattern. One fact, one home: a rule lives here OR in the file named below, never both. If two
files disagree, fix it in the same PR and say which one won.

| Need | Home |
|---|---|
| Kickoff preflight, phase map, library-first graphics flow | `skills/storm-episode/SKILL.md`, `skills/mini-storms/SKILL.md` (junctioned into `~/.claude/skills/`, so a skill edit is a repo commit) |
| Editing architecture, hook contract, CTA contract, chapter blackout table, on-screen text rules, panel anatomy and exits, Content ID protocol, insert gate | `DESIGN.md` (read before any episode work) |
| Script method, hook wording, humanise pass, scaling | `references/script-os.md`, `script-framework.md`, `script-scaling.md`, `humanise-rules.md` |
| Titles and thumbnails | `references/packaging-rules.md` |
| News-lane rulebook, templates, clip pools | `references/mini-storms/FORMAT.md`, `library/mini-storms/`, `library/mini-storms/<event>/` (pools are reused across angles) |
| Shorts spec, slugs `sh-<parent>-<n>`, weekly scan | `references/shorts/PLAN.md`, `references/shorts/competitors-2026-09-15.md`, templates `library/shorts/`, `scripts/shorts_scan.py`, gate `node scripts/shorts_lint.mjs episodes/<slug>` |
| Niche proof, teardowns, slate | `references/script-teardown.md`, `references/teardowns/`, `references/roadmap-2026-09.md` |
| Measured gotchas, newest first | `LEARNINGS.md`: read before every build, update the same session as any owner correction or measured surprise |
| Pins, paths, CTA file and window | `config.yaml` |

## Two lanes, two skills
- `/storm-episode`: the documentary. 13 to 23 min is the default band, not a cap. Confirm length per episode.
- `/mini-storms`: 8 to 12 min seasonal, breaking and outlier videos shipped in 3 h or less. Stitched news, public
  domain and stock clips, red popfigs with a local scrim, news bug, NO chapter cards, one owner gate (packaging). Slugs `ms-<topic>`.
- Narration sits above every bed in both lanes: score 0.13, ambience 0.20 or less, checked with ebur128 per 15 s window.
- Shorts: planned, pilot pending the owner's go. No skill until about ten shorts stabilise.

## Owner gates: rules inherited from the owner's other channels (never claim or infer approval)
- Design sign-off before paid spend or bulk sourcing. Paid API railguards per the global CLAUDE.md.
- Every review cut is a DRAFT render at 98 % production quality: a full-quality cut at draft encode settings, never a
  placeholder. Post the absolute path in one line and PARK. His chat approval resumes. Full render only after that.
- Studio preview cannot play 15 min media-heavy compositions in real time. Do not offer it for review.
- When he calls the remaining defects minor, the open work is the items he named. Anything else is a note in the summary.
- When his named items are done, hand over the file and stop.
- The ebook CTA is must-keep in every episode, hook then CTA then payoff, mounted from `config.yaml channel.cta`. Its
  position is the config window (`window`, `window_ms`, `window_by_slug`). Only the owner moves it. `sweep_episode.py` fails a missing or misplaced CTA.
- His phrases are verbatim. Never paraphrase a line he wrote.
- The defects he names are a sample of that KIND of defect. Find the rest of that kind. This is not licence to invent new kinds.

## Graphics & editorial taste
- **Motion graphics must have motion.** Every composition carries a continuous element across its whole window. A long
  hold keeps something alive (lines, pulses, drift). `beat_density.py` target: zero compositions with a motionless stretch of 4 s or more.
- **Show it.** Put the thing mid-frame or across the right side. A stat as text over b-roll is a miss.
- **Any spatial claim gets a map.** Fit routes to real landmarks: `references/editing-patterns/ep3-map-route-fit.html`.
- **No ambiguous labels.** Name the thing on screen ("WHAT THEY EXPECTED · ROPE FUNNEL").
- **The picture must not contradict the voice.** No asset means an honest designed card, never fabricated footage.
- **Match the shipped panel anatomy, and check it.** Reference compositions live in `references/editing-patterns/`.
  Episode folders are deleted after publish, so copy a shipped pattern there the same session. Never edit a shipped episode.
- **Duration is earned.** A video beat may run 12 to 15 s when it matches the narration. A still runs 3 to 6 s, always
  with zoom or pan, then cuts. Prefer video everywhere. Floor from shipped cuts: ep2 had 187 windows, 10.0 s median,
  2 picture gaps. Uncovered picture gaps in the dozens is a bug.
- **Grading:** one subtle grade on all broadcast, news and private clips; stock and public domain exempt. Doubt about a grade or a claim risk: stop and ask.
- **Audio-first open:** the episode opens with audio, mid-action. Never on black or a silent visual.
- **Sound:** one bed across the episode plus swells at script peaks (about every 45 to 60 s) is the default. WHICH
  sounds is the editor's choice per episode; nothing is auto-wired into future episodes. Sources: `assets/sfx/`,
  `assets/sfx/owner-2026-08-13/`, DeAPI tracks (`assets/sfx/deapi/README.md`, keys in the repo `.env`), or ffmpeg-made.
  Never ripped or unlicensed audio: a claimed bed poisons the whole video. Volumedetect the source, compensate gain,
  verify before the mixdown and after the render.
- **Risers land with the narration:** a riser ends where the line ends. Hits under speech mount near 0.4 (0.6 stacks to 0 dBFS).
- **Non-narration audio is a budget, not an afterthought.** About 30 s of outside audio in a 32 min episode is
  failure-thin. Source audio like clips: 911 calls, presser sound, survivor voice, sirens, ambience, per-act music with character.
- **"Siren"** means the tornado or civil-defence siren (`soundreality-civil-defense-siren-128262.mp3`). **"Weewoo"** means an emergency-vehicle siren.
- **The script never refers to its own structure.** No "in this video", no recap, no outro summary.
- **Graphics text:** proper case, never all-lowercase. One idea per frame, no stat spray. A graphic holds until its
  point lands, never starts before its trigger or after a blank gap. Three type tiers per designed card (small under
  26 px, mid, big 52 px and up). Dates and figures are red Abril popfigs, 3 words or fewer, mid-screen.
- **Chapter blackout is mandatory** between acts and hand-placed. Duration table in DESIGN.md "Chapter blackout".
- **Panels slide out, never vanish.** Timing in DESIGN.md section 5.
- **Sourcing bar:** find 3 to 4 times more candidates than needed. "Short of clips" means stop and source better.
  Split long sources with PySceneDetect (validate the install first). Spread cuts across the episode, never back to back.
- **No visible windows, ever.** Every scheduled or background command runs through `scripts/run_hidden.vbs`. A run that
  opens a visible Chrome or cmd window is killed from its root process and reported, not retried.

## The formula
Script method and hook wording live in `references/script-os.md` and `script-framework.md`; titles and thumbnails in
`references/packaging-rules.md`. What stays true for every episode:
- Stats run through the middle, each translated to human scale. Emotion is banked at the END (survivor vignettes close).
- Tornado episodes march location by location. Stakes descend in order. Micro-loops every 30 to 45 s. No-spoiler metadata.
- A meteorology explainer layer in every episode, and at least two facts no competitor video has (NWS Service
  Assessments, NIST reports, NEXRAD replots, 911 audio, day-after newspapers).
- Reused-content safety is scripted original narration with analysis. A clip reel is a channel killer.

## Voice
- Kyutai pocket-TTS cloned from `assets/voice/pharaoh_wisdom_bearer.mp3` (md5 2d8ea8f14763932f3f76da67d7fd1612).
  Run it through the external venv: `<external.pocket_venv_python> <external.tts_clone_py> --text-file ... --out ... --voice <external.voice_ref>`.
- Pace is measured, never assumed. Probe-TTS two segments AT THE SHIPPING TEMPO, then
  `python3 scripts/word_budget.py episodes/<slug> --target <min> --probe <wav> <wav>` sizes the script from that
  pace and the real non-voice seconds. It fails outside target +/- 1 min; a script is not locked while it fails.
- Documentaries and minis take atempo 1.10. Order: TTS, tempo, re-transcribe, THEN time graphics. words.json must be younger than its wav.
- TTS-safe text: spell out ALL dates, times and numbers, no paired dashes, sentences under 24 words, flowing connective sentences.
- Homographs (read, lead, live, wind, tear, bass, close, present, record): respell the TTS copy phonetically ("reed"),
  keep the script's wording, and listen to every such line once after TTS.

## Footage rules (claim-proof stack, never violate)
- Spine: US government public domain (NOAA, NWS, NHC, FEMA, USGS, Coast Guard), Pexels and Pixabay, self-made radar and
  map graphics, AI b-roll (`scripts/gen_ai_stills.py`). Courtesy credits in the description.
- 911 audio, FEMA survivor interviews and government hearings are the emotional layer: public domain, claim-free.
- News footage: transcribe first, cut at the best moment. Keep pulls short and meaningful; anything held past 12 to
  15 s needs narration over it. Clips WITH their commentary audio are allowed, and the mix (voice alone, clip alone,
  interleaved) is a per-cut editor decision. Expect Content ID revenue claims on these (claims are not strikes). Never
  build a segment that dies if claimed. Vary sources and chapters, never reuse a broadcast cut.
- Read the clip's `provenance.csv` row BEFORE wiring it. Era-mismatch or "backup only" notes disqualify it.
- A REAL clip (broadcast, public domain, survivor) every 45 to 60 s. The core audience saw these events live. Stock only fills between.
- Storm-chaser and independent streamer footage: NEVER without a licence. Credit is not a licence. Never disguise a
  source to slip unlicensed footage past detection. Grain or grade on footage you may legitimately use is fine.
- No AI-generated witnesses, no fabricated quotes. Real quotes come from NWS assessments or news archives, shown as attributed text.

## Pipeline
Per episode in `episodes/<slug>/`. The skill's phase map points at these step numbers.
1. `edit_script.md`: typed segment list plus per-beat visual intent, written on `references/script-scaling.md`. Zero open
   `[verify]` markers before TTS. The CTA hinge is named (segment before, segment after, estimated time). Owner signs off.
2. TTS per narration segment: wavs plus per-segment words.json (faster-whisper).
3. Sourcing: the agent downloads everything itself, 2 to 3 frame-checked candidates per key beat. The owner confirms only `insert` clips.
4. Compose `index.html` by hand as a hyperframes composition, one sub-composition per act. JS or WAAPI animation only:
   CSS @keyframes disables fast-capture. Assets in `media/`, CTA staged into `media/cta/`.
5. Render: see "the render is the LAST step".
6. QC, in order: (a) walk every graphic, card and clip as a viewer and fix what idles; (b) `lint_timeline.py` exit 0,
   including the no-repeat rule (reuse needs `data-callback="reason"`, 2 uses max, last 90 s exempt); (c) the static
   suite, all green; (d) verify changed compositions per "Verifying graphics"; (e) after the render only,
   `scripts/verify_render.sh <episode-dir> <basename>`. Never call a rule fixed from your shot map: re-run the gates on the final `index.html`.
7. Deliverables: `python3 scripts/master_deliverables.py episodes/<slug> <basename> --hevc` makes the 1080p master at
   -14 LUFS, the EN SRT (needs the `nx-*` id on narration audio) and the HEVC archive (needs the PATH ffmpeg 8.1.1, not
   the 8.1.2 shared build). The 1080p `-master.mp4` IS the upload file, no upscale. `metadata.md` at publish: first URL
   is `channel.cta.first_link`, then the "book mentioned at mm:ss" line, no chapter marker at the CTA, category Education, type Overview.
- Chunk a render only if a single render proves unstable.
- Graphics are library-first: browse `library/` (`python3 -m http.server 8765` from `library/`, then `/gallery/`), copy the
  closest match into the episode by hand and retune per beat. `npx hyperframes add <name>` lands in `library/official/`, never
  in an episode. Worked example: `library/inhouse/examples/joplin-stat-panel.html`.

## Verifying graphics: read the code, do not photograph it
- Anything the code states is verified by reading the code: duration, tween presence and coverage, position, size,
  colour, type tiers, text. The gates assert these in the DOM. HTML cannot have garbled text.
- A frame confirms, it never discovers. Take frames only for what code cannot state: how a NEW composition looks as a
  whole, and real footage. 4 to 6 frames, once, read by a subagent, never into the main context, never an episode-wide sweep.
- Never build a measuring rig for a property the code or an existing gate already answers.
- A hole in a gate gets fixed in the gate, not worked around with a render.

## HARD RULE: worktree isolation
Never build or edit in the main checkout; parallel sessions share it. First action of any session: `git worktree list`
and `git status`. Before the first write: `git worktree add .worktrees/<task> -b <branch> origin/main`.

## HARD RULE: the pin stays current
`config.yaml hyperframes_version` is changed only by `scripts/pin_ritual.py`, run from a worktree, bump committed by PR.
`render_preflight.py` hard-fails on pin drift and hard-fails a FULL render on a stale pin; an unreachable npm never
blocks. `RENDER_PIN_STALE_OK=1` is the owner's override, never yours. A newer version can be stricter, not just better:
read the changelog on a multi-version bump.

## HARD RULE: do not write code for what reasoning already does
- A script earns its place only when the check is mechanical, repeated, and must never be forgotten: hard gates, batch
  transforms, anything guarding money or a 40 min render. Taste and context belong to reasoning. A script that needs a
  hand-tuned stoplist is judgment wearing a regex.
- TRIPWIRE: no script may author episode HTML (`index.html`, `compositions/*.html`): cuts, holds, graphics, text, asset
  picks, timing design. Delete it on sight. The test: if the script must know what a beat MEANS, it is authoring.
- Allowed: a one-shot mechanical transform of decisions already made by hand (global retime, uniform arithmetic,
  rename) when it is content-blind, the diff is reviewed, the full static suite passes after, the script is never
  committed, and the PR body declares it. A transform that fails verification gets root-caused, not re-run blind.
- Checkers that only READ episode HTML are always fine.

## HARD RULE: the render is the LAST step
Never use a render as a diagnostic. All green before ANY render, from the worktree:
```
python3 scripts/sweep_episode.py  episodes/<slug>     # structure + CTA gate
python3 scripts/lint_timeline.py  episodes/<slug>     # exit 0, hard gate
python3 scripts/beat_density.py   episodes/<slug>
python3 scripts/media_budget.py   episodes/<slug>
python3 scripts/audio_levels.py   episodes/<slug>
node    scripts/blank_scan.mjs    <abs episode dir>
node    scripts/overlap_check.mjs <abs episode dir>
node    scripts/occlusion_check.mjs <abs episode dir>   # a card on a higher track over another comp's text
node    scripts/graphics_qc.mjs   .                   # from the episode dir
```
- Before any render: listen to the full audio mixdown and watch the hook. A layer known to be below spec means stop and report.
- Every rule a builder needs (safe zones, the presenter circle box, type tiers) goes in the builder's brief BEFORE the
  build, so the draft is never the first place a collision shows up.
- Do not start a render while any builder is still editing. No live subagent, quiet `git status`, then launch.
- One heavy job at a time; `scripts/render_busy.py` guards it. No gates, Playwright or subagent browsers beside a render.
- Render only with `scripts\render.cmd <slug> <draft|full> [out-basename]`. Default 3 workers; full renders on this box
  set `RENDER_WORKERS=2` in a per-episode wrapper (`scripts/<ep>_full_task.cmd`). `RENDER_CRF=20` gives a smaller single pass. Planning numbers: a 17 min draft took 36 min, a 28 min full took about 75 min at 2 workers.
- Launch hidden through a scheduled task: `schtasks /create ... /tr "wscript.exe <abs>\scripts\run_hidden.vbs cmd.exe /c
  <abs>\scripts\<task>.cmd"` then `/run`. A harness background job is reaped at low RAM, and `Start-Process` dies with its tool call.
- Read the log for `streaming-encode gate ... enabled:true`. Without it a long composition captures to disk and fills it.
- Liveness is judged by command line (`Get-CimInstance Win32_Process | Where CommandLine -like '*hyperframes*'`), never by process count.
- `ffprobe deadline` means slow, never corrupt. The deadline is 30 s and no env var raises it. Cap every source asset at
  the composition's resolution: `media_budget.py` refuses the render otherwise, `optimize_clips.py <episode> --apply` fixes it.
- Owner timestamps against an older cut are mapped by you, never sent back to him: `git show <sha>:episodes/<slug>/index.html`
  into a temp dir, then `clip_report.py` resolves them exactly.

## Git
All git and gh as `sidhartha1s`. Small PRs, code-reviewer, rebase-merge, docs sweep in the same PR. `python3`, never
`python`. Node 22 or newer. Before opening and before merging any PR that touches `scripts/`, run
`python3 scripts/e2e.py episodes/<slug>` on a live episode: every self-check green and no tool crash.
