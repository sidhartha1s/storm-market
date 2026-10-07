# CLAUDE.md: storm-market (The Warning Hour, US weather and disaster documentaries)

Narrated US weather and natural-disaster retrospectives, US English. Separate from JP-market: no shared code, only
the same external tool pattern. One fact, one home: a rule lives here OR in the file named below, never both. If two
files disagree, fix it in the same PR and say which one won.

**This repo's docs outrank the global `~/.claude/CLAUDE.md`.** Where this file, a doc it names, `ops/decisions.md` or the
owner's instruction for the episode says something, that wins over any global default (subagent model, effort, review
flow). The global file only fills what this repo leaves open. Read `ops/decisions.md` before choosing a model or a flow.

**Chain of command for motion graphics.** Every subagent that builds, retimes, fixes, redesigns or verifies a graphic runs
on Opus 5.5 at high effort or above (blind-judged Opus 43/50 vs Sonnet 26/50; Sonnet passes every gate with broken
work). Sonnet is for shot logs, sourcing and read-only probes, never graphics. The builder never verifies its own work:
the orchestrator reads a settled frame of every new or changed graphic over the footage it will sit on before any render.
A fix goes back to an Opus builder, never to the model that made the defect. Gates passing is not verification.

| Need | Home |
|---|---|
| Kickoff preflight, phase map | `skills/storm-episode/SKILL.md`, `skills/mini-storms/SKILL.md` (junctioned into `~/.claude/skills/`, so a skill edit is a repo commit) |
| Editing architecture, hook contract, CTA contract, chapter blackout table, cadence and sync rules, Content ID protocol, insert gate | `DESIGN.md` (read before any episode work) |
| Every motion-graphics rule: file contract, safe zones and the presenter circle, glass card, motion, exits, on-screen text, what each gate parses, verification | `references/mg-quickref.md` (goes into every MG builder's brief) |
| Channel palette, fonts, type-tier px values, TV-readability floor, CSS custom properties | `library/inhouse/snippets/tokens.md` (swatch: `library/inhouse/snippets/brand-swatch.html`) |
| Script method, hook wording, humanise pass, scaling | `references/script-os.md`, `script-framework.md`, `script-scaling.md`, `humanise-rules.md` |
| The one condensed brief a script writer opens (wins for writers) | `references/script-quickref.md` |
| Violence/death words that trip YouTube's transcript scan, with alternatives; gate `scripts/flag_words.py episodes/<slug>` | `references/flag-words.md` |
| Heteronyms (word, both senses, a hint) that pocket-TTS can mispronounce by guessing the wrong sense; gate `scripts/homograph_scan.py episodes/<slug>` (WARN-only, reports for a probe, never fails) | `references/homographs.md` |
| Titles and thumbnails | `references/packaging-rules.md` |
| News-lane rulebook, templates, clip pools | `references/mini-storms/FORMAT.md`, `library/mini-storms/`, `library/mini-storms/<event>/` (pools are reused across angles) |
| Shorts spec, slugs `sh-<parent>-<n>`, weekly scan | `references/shorts/PLAN.md`, `references/shorts/competitors-2026-09-15.md`, templates `library/shorts/` (not created yet), `scripts/shorts_scan.py`, gate `node scripts/shorts_lint.mjs episodes/<slug>` |
| Niche proof, teardowns, slate | `references/script-teardown.md`, `references/teardowns/`, `references/roadmap-2026-09.md` |
| Measured gotchas, newest first | `learnings/` (`README.md` says which file serves which job): read yours before building |
| Pins, paths, CTA file and window | `config.yaml` |
| Open tooling and pipeline work; dated decisions (read both at session start, update the same session) | `ops/tasks.md`, `ops/decisions.md` |

An owner correction or a measured surprise lands in its single home (`references/mg-quickref.md`, a gate, or the right
`learnings/` file) the same session.

## Two lanes, two skills
- `/storm-episode`: the documentary. Length is set per episode by the story and confirmed with the owner (El Reno: about 25 to 30 min, owner 3 Oct 26). No default band.
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
- The ebook CTA is must-keep in every episode, placed late (85 to 95 %), mounted from `config.yaml channel.cta`. Its
  position is the config window (`window`, `window_ms`, `window_by_slug`). Only the owner moves it. `sweep_episode.py` fails a missing or misplaced CTA.
- His phrases are verbatim. Never paraphrase a line he wrote.
- The defects he names are a sample of that KIND of defect. Find the rest of that kind. This is not licence to invent new kinds.

## Editorial and sound taste
- **Grading:** one subtle grade on all broadcast, news and private clips; stock and public domain exempt. Doubt about a grade or a claim risk: stop and ask.
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
- **Chapter blackout is mandatory** between acts and hand-placed (DESIGN.md "Editing grammar").
- **Sourcing bar:** find 3 to 4 times more candidates than needed. "Short of clips" means stop and source better.
  Split long sources with PySceneDetect (validate the install first). Spread cuts across the episode, never back to back.
- **No visible windows, ever.** Every scheduled or background command runs through `scripts/run_hidden.vbs`. A run that
  opens a visible Chrome or cmd window is killed from its root process and reported, not retried.

## The formula
Script method and hook wording live in `references/script-os.md` and `script-framework.md`; titles and thumbnails in
`references/packaging-rules.md`. What stays true for every episode:
- Stats run through the middle, each translated to human scale. Human moments go where they hit hardest (script-scaling.md "Emotion").
- Tornado episodes may march location by location (editor's call per episode). Micro-loops every 30 to 45 s. No-spoiler metadata.
- A meteorology explainer layer in every episode, and at least two facts no competitor video has (NWS Service
  Assessments, NIST reports, NEXRAD replots, 911 audio, day-after newspapers).
- Reused-content safety is scripted original narration with analysis. A clip reel is a channel killer.

## Voice
- Kyutai pocket-TTS cloned from `assets/voice/pharaoh_wisdom_bearer.mp3` (md5 2d8ea8f14763932f3f76da67d7fd1612).
  Run it through the external venv: `<external.pocket_venv_python> <external.tts_clone_py> --text-file ... --out ... --voice <external.voice_ref>`
  for one probe; `tts_episode.py` passes every stale segment in one `--batch <tsv>` call so the model loads once per run (about 19 s saved per segment, measured 1 Oct 26).
- Pace is measured, never assumed. Probe-TTS two segments AT THE SHIPPING TEMPO, then
  `python3 scripts/word_budget.py episodes/<slug> --target <min> --probe <wav> <wav>` sizes the script from that
  pace and the real non-voice seconds. It fails outside target +/- 1 min; a script is not locked while it fails.
- Tempo per lane lives in `config.yaml channel.tempo`; `tts_episode.py` applies it. A key reveal can slow to 1.0:
  give it its own segment and put `(tempo 1.0)` on that segment's heading. The editor picks which lines; no quota (owner 2 Oct 26). Order: TTS, tempo, re-transcribe, THEN time graphics. `sweep_episode.py` fails a words.json or `data-duration` that runs past its wav.
- TTS-safe text: spell out ALL dates, times and numbers, no paired dashes, sentences under 24 words, flowing connective sentences.
- Homographs: list, senses and the probe-before-respelling rule live in `references/homographs.md`, gated by
  `scripts/homograph_scan.py` (in `run_gates.py`).

## Footage rules (claim-proof stack, never violate)
- Spine: US government public domain (NOAA, NWS, NHC, FEMA, USGS, Coast Guard), Pexels and Pixabay, self-made radar and
  map graphics, AI b-roll (nanobanana; `scripts/gen_ai_stills.py` is hardcoded to ep2). Courtesy credits in the description.
- 911 audio, FEMA survivor interviews and government hearings are the emotional layer: public domain, claim-free.
- News footage: transcribe first, cut at the best moment. Keep pulls short and meaningful; anything held past 12 to
  15 s needs narration over it. Clips WITH their commentary audio are allowed, and the mix (voice alone, clip alone,
  interleaved) is a per-cut editor decision. Expect Content ID revenue claims on these (claims are not strikes). Never
  build a segment that dies if claimed. Vary sources and chapters, never reuse a broadcast cut.
- Read the clip's `provenance.csv` row BEFORE wiring it. Era-mismatch or "backup only" notes disqualify it.
- A REAL clip (broadcast, public domain, survivor) about every 45 to 60 s is the aim, not a hard rule (owner 4 Oct 26). The core audience saw these events live. Stock only fills between.
- Storm-chaser and independent streamer footage: NEVER without a licence. Credit is not a licence. Never disguise a
  source to slip unlicensed footage past detection. Grain or grade on footage you may legitimately use is fine.
- No AI-generated witnesses, no fabricated quotes. Real quotes come from NWS assessments or news archives, shown as attributed text.

## Pipeline
Per episode in `episodes/<slug>/`. The skill's phase map points at these step numbers. Never edit a shipped episode.
1. `edit_script.md`: typed segment list plus per-beat visual intent, written on `references/script-scaling.md`. A
   section goes to TTS only once LOCKED (hook+intro locks and moves first; the one lock definition is
   `references/script-scaling.md` "Section lock — the ONE definition" — never restated here) — never the whole
   script waiting on the last act. The CTA hinge is named (segment before, segment after, estimated time). Owner
   signs off on story/register in parallel with the fact-check fan-out, not serially after it.
2. TTS: `python3 scripts/tts_episode.py episodes/<slug>` makes per-segment wavs at the lane tempo plus words.json (faster-whisper) in one pass.
3. Sourcing: the agent downloads everything itself, 2 to 3 frame-checked candidates per key beat. The owner confirms only `insert` clips.
4. Compose `index.html` by hand as a hyperframes composition, one sub-composition per act, graphics library-first and built to
   `references/mg-quickref.md` (worked example: `library/inhouse/examples/joplin-stat-panel.html`). Assets in `media/`, CTA staged into `media/cta/`.
5. Render: see "the render is the LAST step".
6. QC, in order: (a) walk every graphic, card and clip as a viewer and fix what idles; (b) `lint_timeline.py` exit 0,
   including the no-repeat rule (reuse needs `data-callback="reason"`, 3 uses max, last 90 s exempt); (c) the static
   suite, all green; (d) verify changed compositions per `references/mg-quickref.md` "Verify"; (e) after the render only,
   `scripts/verify_render.sh <episode-dir> <basename>`. Never call a rule fixed from your shot map: re-run the gates on the final `index.html`.
7. Deliverables: `python3 scripts/master_deliverables.py episodes/<slug> <basename>` makes the 1080p master at
   -14 LUFS and the EN SRT (needs the `nx-*` id on narration audio). No HEVC archive (owner 28 Sep 26: disk). The 1080p
   `-master.mp4` IS the upload file, no upscale. The moment the final master exists: move the master and SRT (both
   gitignored) into the MAIN checkout's `episodes/<slug>/renders/` and delete every other render (drafts, the
   pre-master final, previews). Never delete the master. `metadata.md` stays tracked in the episode folder. After
   publish, commit, PR and merge the episode branch, then remove the worktree. `metadata.md` at publish: first URL
   is `channel.cta.first_link`, then the "book mentioned at mm:ss" line, no chapter marker at the CTA, category Education, type Overview.
- Chunk a render only if a single render proves unstable.

## HARD RULE: worktree isolation
Never build or edit in the main checkout; parallel sessions share it. First action of any session: `git worktree list`
and `git status`. Before the first write: `git worktree add .worktrees/<task> -b <branch> origin/main`.

## HARD RULE: the pin stays current
The owner runs the latest hyperframes (upstream ships fixes daily). Episode kickoff runs `python3 scripts/pin_ritual.py
--check-only`; stale means run the ritual (A/B on `episodes/demo-pin`) and PR the bump before the first render, never mid-episode.
The pin is locked: `config.yaml hyperframes_version` and every `npx hyperframes@X` in `scripts/*.cmd` agree, and only the
ritual changes them. `render_preflight.py` fails on drift, never on currency. Read the changelog on every bump.

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
python3 scripts/run_gates.py episodes/<slug>   # the whole pre-render suite in order; stops on the first failure
```
The gate list and its order live in `scripts/run_gates.py`. Minis also run `node scripts/freeze_scan.mjs episodes/<slug>` (mini-storms skill).
- Before any render: listen to the full audio mixdown and watch the hook. A layer known to be below spec means stop and report.
- Every MG builder's brief carries `references/mg-quickref.md` BEFORE the build, so the draft is never the first place a collision shows up.
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
All git and gh as `sidhartha1s`. Small PRs: `/simplify`, tests + E2E, then `code-reviewer` on Opus; merge only after the owner's OK; rebase-merge, docs sweep in the same PR. `python3`, never
`python`. Node 22 or newer. Before opening and before merging any PR that touches `scripts/`, run
`python3 scripts/e2e.py episodes/<slug>` on a live episode: every self-check green and no tool crash.
