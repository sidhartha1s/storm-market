# CLAUDE.md: storm-market (The Warning Hour, US weather and disaster documentaries)

Narrated US weather and natural-disaster retrospectives, US English. Self-contained: no code, tool, model or file shared
with any other project (see "everything lives in this folder"), and an answer about it names no other project. One fact, one home: a rule lives here OR in the file named below, never both. If two
files disagree, fix it in the same PR and say which one won.

**This repo's docs outrank the global `~/.claude/CLAUDE.md`.** Where this file, a doc it names, `ops/decisions.md` or the
owner's instruction for the episode says something, that wins over any global default (subagent model, effort, review
flow). Read `ops/decisions.md` before choosing a model or a flow.

**Chain of command for motion graphics.** Split by depth (owner 16 Oct 26). The deep graphics, roughly the top 5 to 15
of an episode (a map with the tornado path moving, zoom-ins and zoom-outs, multi-layer explainers), are built, retimed,
fixed and redesigned by Opus 5.5 at high effort or above. Every other graphic (a stat card, a ringing doorbell, a label
over footage) goes to Sonnet 5.5 at high effort with a full brief on `references/mg-brief-template.md`; a brief that
leaves the builder guessing is the defect. The plan lists
each graphic with its model. The builder never verifies its own work: the orchestrator reads a settled frame of every
new or changed graphic over the footage it will sit on before any render. A Sonnet graphic that fails the read twice
goes to Opus. Gates passing is not verification. Subagents and side sessions in this repo start without the owner's
approval (owner 28 Oct 26: "you dont need my approval for subagents, inside strom market repo").

| Need | Home |
|---|---|
| Kickoff preflight, phase map | `skills/storm-episode/SKILL.md`, `skills/mini-storms/SKILL.md` (junctioned into `~/.claude/skills/`, so a skill edit is a repo commit) |
| Editing architecture, hook contract, CTA contract, end ask, chapter blackout table, cadence and sync rules, Content ID protocol, insert gate | `DESIGN.md` (read before any episode work) |
| Every motion-graphics rule: file contract, safe zones and the presenter circle, glass card, motion, exits, on-screen text, what each gate parses, verification | `references/mg-quickref.md` (goes into every MG builder's brief) |
| Channel palette, fonts, type-tier px values, TV-readability floor, CSS custom properties | `library/inhouse/snippets/tokens.md` (swatch: `library/inhouse/snippets/brand-swatch.html`) |
| The angle: what it is, how candidates are found and tested, the owner lock. Comes before any title, thumbnail, hook or script line | `references/angle.md` |
| Script method, hook wording, humanise pass, scaling | `references/script-os.md`, `script-framework.md`, `script-scaling.md`, `humanise-rules.md` |
| The one condensed brief a script writer opens (a copy: on conflict its source file wins) | `references/script-quickref.md` |
| Violence/death words that trip YouTube's transcript scan, with alternatives; gate `scripts/flag_words.py episodes/<slug>` | `references/flag-words.md` |
| Hook shapes menu and the rule that a hook never repeats the last 2 episodes' shape; gate `scripts/hook_shape.py episodes/<slug>` | `references/script-quickref.md` "The hook" |
| Heteronyms (word, both senses, a hint) that pocket-TTS can mispronounce by guessing the wrong sense; gate `scripts/homograph_scan.py episodes/<slug>` (WARN-only, reports for a probe, never fails) | `references/homographs.md` |
| Titles and thumbnails; fill-in prompts for a thumbnail with Paul on it | `references/packaging-rules.md`; `references/thumbnail-prompts.md` |
| News-lane rulebook, templates, clip pools | `references/mini-storms/FORMAT.md`, `library/mini-storms/`, `library/mini-storms/<event>/` (pools are reused across angles) |
| Shorts spec, slugs `sh-<parent>-<n>`, weekly scan | `references/shorts/PLAN.md`, `references/shorts/competitors-2026-09-15.md`, `scripts/shorts_scan.py`, gate `node scripts/shorts_lint.mjs episodes/<slug>` |
| Other platforms the videos can go to, their payout programs, and the posting tool (a first check, nothing built) | `references/distribution.md` |
| Niche proof, teardowns | `references/script-teardown.md`, `references/teardowns/` |
| What viewers say under every reference video: the rule, the pull commands, the entries | `references/comment-bank.md` |
| Measured gotchas, newest first | `learnings/` (`README.md` says which file serves which job): read yours before building |
| Pins, paths, CTA file and window | `config.yaml` |
| Open tooling and pipeline work, questions waiting on the owner; dated decisions (read both at session start, update the same session) | `ops/tasks.md`, `ops/decisions.md` |
| Every episode's E number and the next free one | `python3 scripts/episode.py` |
| Every episode's stage, what it waits on, and the record of the owner's approvals (`episodes/<slug>/gates.md`) | `python3 scripts/stage.py` (usage in its docstring) |
| Which episode jobs are ready, running, held or done, and the lane launcher (profile probe, free-memory gate, no lane-count cap, `relaunch`, `stop <ep> all`) | `scripts/lanes.py` (job model in its docstring); its Stop hook `~/.claude/hooks/lane-gate.py` is not installed on the ZBook |

An owner correction or a measured surprise lands in its single home (`references/mg-quickref.md`, a gate, or the right
`learnings/` file) the same session.

## Two lanes, two skills
- `/storm-episode`: the documentary. Length is set per episode by the story and confirmed with the owner. No default band.
- `/mini-storms`: 8 to 12 min seasonal, breaking and outlier videos shipped in 3 h or less. Stitched news, public
  domain and stock clips, red popfigs with a local scrim, news bug, NO chapter cards, two owner gates (angle, then packaging). Slugs `ms-<topic>`.
- Narration sits above every bed in both lanes: score 0.13, ambience 0.20 or less, checked with ebur128 per 15 s window.
- Shorts: one demo built (`episodes/sh-hawaii-lowell-1`, 16 Sep 26), three Joplin shorts unrendered in open PR #179; no pilot go on record. No skill until about ten shorts stabilise.

## Owner gates: rules inherited from the owner's other channels (never claim or infer approval)
- His gates per documentary, in this order and no others: the angle; the title and thumbnail (`references/packaging-rules.md`);
  the hook+intro; the draft preview; any paid retake. Acts are never his gate (`references/script-scaling.md` "Section
  lock"); a plan or ETA that waits on him for anything else is wrong (owner 28 Oct 26: "why I sign off the scripts
  because I don't read it", and the titles of 3 videos never reached him). `stage.py` lets title and thumbnail block
  only the publish; whether they close before the hook+intro, and whether insert clips and the voice pick are gates,
  is open (`ops/tasks.md` "Waiting on the owner").
- Every approval or deferral is recorded the turn his words arrive: `python3 scripts/stage.py record episodes/<slug>
  <gate> --words "<his words, verbatim>" --shown "<file or URL>"` (`defer:<gate>` for "picks later" leaves the gate
  open). Nothing else counts as approval. `python3 scripts/stage.py` shows what every episode waits on.
- Paid spend and bulk sourcing ride on the hook+intro gate (Paul's Flow clips with their credit total, skill phase 3);
  a retake is the paid-retake gate. Paid API railguards per the global CLAUDE.md. Free candidate sourcing
  (public domain and stock downloads, no spend, nothing licensed) is not bulk sourcing: it starts from each act's Picture
  lines without waiting for that gate (owner 17 Oct 26, flow page f1). A paid or licensed buy still waits for it.
- Every review cut is a DRAFT render at 98 % production quality: a full-quality cut at draft encode settings, never a
  placeholder. Post the absolute path in one line and PARK. His chat approval resumes. Full render only after that.
- Studio preview cannot play 15 min media-heavy compositions in real time. Do not offer it for review.
- When he calls the remaining defects minor, the open work is the items he named. Anything else is a note in the summary.
- When his named items are done, hand over the file and stop.
- The ebook CTA is must-keep in every episode outside `channel.cta.exempt`, mounted from `config.yaml channel.cta`. Where it goes is DESIGN.md "CTA contract";
  its position is the config window (`window`, `window_ms`, `window_by_slug`). Only the owner moves it. `sweep_episode.py` fails a missing or misplaced CTA.
- His phrases are verbatim. Never paraphrase a line he wrote.
- The defects he names are a sample of that KIND of defect. Find the rest of that kind. This is not licence to invent new kinds.

## Editorial and sound taste
- **Grading:** one subtle grade on all broadcast, news and private clips; stock and public domain exempt. Doubt about a grade or a claim risk: stop and ask.
- **Sound:** one bed across the episode plus swells at script peaks (about every 45 to 60 s) is the default. WHICH
  sounds is the editor's choice per episode; nothing is auto-wired into future episodes. Sources: `assets/sfx/`,
  `assets/sfx/owner-2026-08-13/`, DeAPI tracks already made (`assets/sfx/deapi/README.md`; both accounts suspended since 10 Oct 26), or ffmpeg-made.
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
- The angle is locked by the owner before anything else, in documentaries and minis alike, chosen from several true candidates (`references/angle.md`). The video is built on the angle, not on the subject.
- Stats run through the middle, each translated to human scale. Human moments go where they hit hardest (script-scaling.md "Emotion").
- Tornado episodes may march location by location (editor's call per episode). Micro-loops every 30 to 45 s. No-spoiler metadata.
- A meteorology explainer layer in every episode, and at least two facts no competitor video has (NWS Service
  Assessments, NIST reports, NEXRAD replots, 911 audio, day-after newspapers).
- Reused-content safety is scripted original narration with analysis. A clip reel is a channel killer.

## Voice
- Kyutai pocket-TTS cloned from on-camera Paul: `config.yaml external.voice_ref` (file and md5), so the narrator and the presenter are one voice.
  The whole voice tool sits inside this repo folder (venv, clone script, model files, Hugging Face login: `scripts/voice_tool.py`
  lists the pieces, and `python3 scripts/voice_tool.py` checks them). Run `<external.pocket_venv_python> scripts/tts_clone.py --text-file ... --out ... --voice <external.voice_ref>`
  for one probe; `tts_episode.py` passes every stale segment in one `--batch <tsv>` call so the model loads once per run.
- Pace is measured, never assumed. Probe-TTS two segments AT THE SHIPPING TEMPO, then
  `python3 scripts/word_budget.py episodes/<slug> --target <min> --probe <wav> <wav>` sizes the script from that
  pace and the real non-voice seconds. It fails outside target +/- 1 min; a script is not locked while it fails.
- Tempo per lane lives in `config.yaml channel.tempo`; `tts_episode.py` applies it. The number belongs to the voice: a new
  voice reference gets a new tempo that keeps the delivered pace (config comment shows the sum). A key reveal can slow to 0.85:
  give it its own segment and put `(tempo 0.85)` on that segment's heading. The editor picks which lines; no quota (owner 2 Oct 26). Order: TTS, tempo, any later step that rewrites the wav (a voice conversion), re-transcribe, THEN time graphics. `sweep_episode.py` fails a words.json or `data-duration` that runs past its wav.
- TTS-safe text: `references/script-quickref.md` "Voice". `tts_episode.py` refuses digits, abbreviation periods, initials and
  symbols before voicing (patterns: `tts_clone.UNSAFE`, test `scripts/test_tts_text.py`).
- Homographs: list, senses and the probe-before-respelling rule live in `references/homographs.md`, gated by
  `scripts/homograph_scan.py` (in `run_gates.py`).
- Retake bar (owner 18 Oct 26): retake a narration segment only when it is "absolutely bullshit and garbled" (nonsense
  sounds, clicks) or has a "totally wrong pronunciation". A swapped word that keeps the meaning (you/we, in/and) stays:
  "not a big deal ... it's fine. Go ahead." Flag the first two; never retake the third.

## Footage rules (claim-proof stack, never violate)
- Spine: US government public domain (NOAA, NWS, NHC, FEMA, USGS, Coast Guard), Pixabay (Pexels keys dead, DESIGN.md
  "Sourcing"), self-made radar and map graphics. AI b-roll has no working tool (`scripts/gen_ai_stills.py` is a
  hardcoded ep2 one-off on the suspended DeAPI). Courtesy credits in the description.
- 911 audio, FEMA survivor interviews and government hearings are the emotional layer: public domain, claim-free.
- News footage: transcribe first, cut at the best moment. Keep pulls short and meaningful; anything held past 12 to
  15 s needs narration over it. Clips WITH their commentary audio are allowed, and the mix (voice alone, clip alone,
  interleaved) is a per-cut editor decision. Expect Content ID revenue claims on these (claims are not strikes). Never
  build a segment that dies if claimed. Vary sources and chapters, never reuse a broadcast cut.
- Read the clip's `provenance.csv` row BEFORE wiring it. Era-mismatch or "backup only" notes disqualify it.
- REAL clips (broadcast, public domain, survivor) come in the way a friend telling the story stops and says "hang on, look
  at this" and shows a video: wherever the story reaches a moment someone filmed, show the film. More real clips than
  graphics alone, placed by judgment, never by a quota (owner 15 Oct 26; about every 45 to 60 s is a floor, not a target).
  The core audience saw these events live. Stock only fills between.
- Storm-chaser and independent streamer footage: NEVER without a licence. Credit is not a licence. Never disguise a
  source to slip unlicensed footage past detection. A grade on footage you may legitimately use is fine; no grain (DESIGN.md "Look: no grain").
- No AI-generated witnesses, no fabricated quotes. Real quotes come from NWS assessments or news archives, shown as attributed text.

## Pipeline
Per episode in `episodes/<slug>/`. The skill's phase map points at these step numbers. Never edit a shipped episode.
1. `edit_script.md`: started only once `episodes/<slug>/angle.md` holds the owner's locked angle (`references/angle.md`). Typed segment list plus per-beat visual intent, written on `references/script-scaling.md`. A
   section goes to TTS only once LOCKED (`references/script-scaling.md` "Section lock"; hook+intro first), never the
   whole script waiting on the last act. The CTA hinge is named (segment before, segment after, estimated time).
2. TTS: `python3 scripts/tts_episode.py episodes/<slug>` makes per-segment wavs at the lane tempo plus words.json (faster-whisper) in one pass.
3. Sourcing: runs beside the script from the first Picture lines (lanes and roles: skill phase 5). The owner confirms only `insert` clips.
4. Compose `index.html` by hand as a hyperframes composition, one sub-composition per act, graphics library-first and built to
   `references/mg-quickref.md` (worked example: `library/inhouse/examples/joplin-stat-panel.html`). Assets in `media/`, CTA staged into `media/cta/`.
5. Render: see "the render is the LAST step".
6. QC, in order: (a) walk every graphic, card and clip as a viewer and fix what idles; (b) `run_gates.py` all green
   (clip reuse: DESIGN.md "Cadence + sync rules"); checker output is a list to eyeball, not a work order; (c) verify changed compositions per `references/mg-quickref.md` "Verify"; (d) after the render only,
   `scripts/verify_render.sh <episode-dir> <basename> <draft|full>` (required: the mode you gave `render.cmd`). Never call a rule fixed from your shot map: re-run the gates on the final `index.html`.
7. Deliverables: `python3 scripts/master_deliverables.py episodes/<slug> <basename>` makes the 1080p master at
   -14 LUFS and the EN SRT (needs the `nx-*` id on narration audio; English only, YouTube translates). No HEVC archive (owner 28 Sep 26: disk). The 1080p
   `-master.mp4` IS the upload file, no upscale. Finals are `E<nn>-<topic>-final-master.mp4` and `.srt` (owner 1 Nov 26:
   "E01 or E02 then the topic name and then the final master, keep it simple"). A new documentary takes its number at
   kickoff: slug `e<nn>-<topic>`, the next free number `python3 scripts/episode.py` prints. The metadata and thumbnails
   carry the same prefix (`E<nn>-<topic>-metadata.md`, `thumbs/E<nn>-<topic>-thumb-<name>`, owner 2 Nov 26) and stay
   tracked in the episode folder. Then `python3 scripts/ship.py episodes/<slug> <basename> [--dry-run]`, in the MAIN
   checkout: master and SRT move into `episodes/<slug>/renders/` under the final names (md5 checked), the metadata is
   copied beside them (owner 2 Nov 26: "I still don't see the metadata"), and `uploads/E<nn>-<topic>/` at the repo root
   (gitignored), what he opens to upload and pick (owner 4 Nov 26), gets hard links to master and SRT, the metadata, every
   thumbnail and the titles. It never deletes: delete the other renders it lists, never the master. The same finals go to
   the other laptop, md5 checked after every copy. After publish, `stage.py record ... published`, then commit, PR and
   merge the episode branch and remove the worktree. The metadata file at publish: first URL
   is `channel.cta.first_link`, then the "book mentioned at mm:ss" line, no chapter marker at the CTA, category Education, type Overview.
- Render by act (owner 26 Oct 26, sk_4): `python3 scripts/render_acts.py <slug> <draft|full> <basename> [--reuse <older-basename>]`,
  launched hidden like a render; how it cuts at the blackouts and stitches is its docstring. With `--reuse`, an unchanged
  act is taken from the older run, so a fix re-renders only its act. `--plan` lists the seams. The act file is staged
  render input, never episode HTML (TRIPWIRE below). The whole run
  holds the heavy lock; poll `render_acts_<basename>_done.marker`, never `render_<mode>_done.marker` (written after every act).
- Heavy local jobs run on the ZBook by default (owner 17 Oct 26): transcription, voice conversion, clip downloads and
  frame extraction for sourcing, captures, gates and renders. The ZBook's driver is 616.92 and an ffmpeg `h264_nvenc`
  test passed on it (11 Nov 26); no real render has run on it since, so the first one must pass `stream_gate.py check`. Sourcing lanes on the rendering machine pause while it renders (one heavy job per machine). The ASUS GPU runs the owner's live dictation and its RAM is shared with his work (learnings/render.md 11 Nov 26).

## HARD RULE: everything lives in this folder
Owner 7 Oct 26: "i want all stuff related to storm market within the repo. exceptions, u gotta let me know."
- Every tool, venv, model, login, key, source project and asset this channel uses sits inside this repo folder: tracked, or
  gitignored in the MAIN checkout when it is too big or secret (`.venv-pocket/`, `.models/`, `.env`, episode media). Never a
  path into another project, a shared user cache or a scratch folder.
- An outside dependency is an exception. Tell the owner before using a new one and add it to this list in the same PR.
- Exceptions on record: installed programs (Python with its packages such as pyyaml, faster-whisper and uv, Node and the npx
  cache that holds hyperframes, ffmpeg, Chrome, git, gh, yt-dlp); online accounts and their local logins (GitHub, Cloudflare
  for the site deploy, Gumroad CLI, YouTube, Flow); the skills' junction into `~/.claude/skills/` (the files are tracked
  here); the Stop hook `~/.claude/hooks/lane-gate.py` (a harness hook; the job model it asks is `scripts/lanes.py`); the Claude profiles `lanes.py` launches lanes on
  (the `%USERPROFILE%\bin\claudeN.cmd` wrappers and their credentials: tokens in `~/.claude-tokens/`, login folders under `~/.claude-accounts/` for claude6 and claudemax) and the `zbook` and `asus` ssh aliases;
  the channel's Google accounts (`config.yaml channel`); stock-fetch keys in `~/.claude/.env`; ChatGPT image generation for thumbnails, driven by the webgen browser
  tool in `~/Automation Projects/webgen` (a separate project). What is still to move in: `ops/tasks.md`.

## HARD RULE: worktree isolation
Never build or edit in the main checkout; parallel sessions share it. First action of any session: `git worktree list`
and `git status`. Before the first write: `git worktree add .worktrees/<task> -b <branch> origin/main`.

## HARD RULE: the pin stays current
The owner runs the latest hyperframes (upstream ships fixes daily). Episode kickoff runs `python3 scripts/pin_ritual.py
--check-only`; stale means run the ritual (A/B on `episodes/demo-pin`) and PR the bump before the first render, never mid-episode.
The pin is locked: `config.yaml render.hyperframes_version` and every `npx hyperframes@X` in `scripts/*.cmd` agree, and only the
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
The gate list and its order live in `scripts/run_gates.py` (minis add a freeze scan: mini-storms skill).
- Before any render: listen to the full audio mixdown and watch the hook. A layer known to be below spec means stop and report.
- Every MG builder's brief carries `references/mg-quickref.md` BEFORE the build, so the draft is never the first place a collision shows up.
- Do not start a render while any builder is still editing. No live subagent, quiet `git status`, then launch.
- `render_preflight.py` refuses an `ep-` documentary missing a layer the owner already asked for (circle, bed, Paul's
  clips; owner 18 Oct 26) or whose circle clip is a still stand-in, not a moving face (test
  `python3 scripts/test_frozen_circle.py`). Its `LAYERS` table is the list and holds the thresholds; `run_gates.py` runs it too.
- One heavy job per machine at a time: render.cmd, `render_acts.py`, the pin ritual (not `--check-only`), TTS (`tts_episode.py`, `tts_clone.py`), the face pass (`circle_face.py`) and `e2e.py`
  book the heavy lock (`~/.storm-heavy.lock`) and wait their turn, also when started over ssh; a dead holder's lock is taken over.
  `paul_voice.py` and `transcribe_episode.py` do not book it yet (`ops/tasks.md`).
  Launch long waits detached, never in a 10 min tool call (an e2e can wait behind a 75 min render).
  How it works and how a new heavy job books it: the `scripts/render_busy.py` docstring (test `python3 scripts/test_render_busy.py`).
  No gates, Playwright or subagent browsers beside a render, except one `freeze_scan.mjs` page (`render_busy.py --light`).
- Render only with `scripts\render.cmd <slug> <draft|full> [out-basename]`; it keeps each render's own `renders\<basename>.log` and `.fps`, the only ones `verify_render.sh` reads. The dojo-ops dashboard starts a draft only through `scripts\dojo_draft.cmd` (how: its header; test `python3 scripts/test_dojo_draft.py`). Default 3 workers; `render_busy.py` lowers
  `RENDER_WORKERS` to what fits free RAM. No free-disk floor (owner 30 Oct 26: "2 fucking workers"; removed 4 Nov 26). `RENDER_CRF=20` gives a smaller single pass. Planning numbers: a 17 min draft took 36 min, a 28 min full took about 75 min at 2 workers.
- Launch hidden through a scheduled task, deleted in the same command: `schtasks /create /tn <T> /tr "wscript.exe
  <abs>\scripts\run_hidden.vbs cmd.exe /c <abs>\scripts\<task>.cmd" /sc once /st 23:59 /f && schtasks /run /i /tn <T> &&
  schtasks /delete /tn <T> /f`. A one-time trigger stays armed after `/run` and fires a second copy at its `/st` time; the
  started job survives the delete. `/i` ignores the on-battery constraint (else the run stays queued and is deleted unstarted). The `schtasks-once` hook in `~/.claude/hooks` blocks a create without the delete.
  A harness background job is reaped at low RAM, and `Start-Process` dies with its tool call.
- `streaming-encode gate ... enabled:true` must be in the log. Without it a long composition captures to disk and fills it (Camille: 75 GB; learnings/render.md 26 Oct 26). `scripts/stream_gate.py`, called by render.cmd, stops a render whose gate line says enabled:false or is missing 8 min in (test `python3 scripts/test_stream_gate.py`).
- A render runs on what it asked for or it fails: `stream_gate.py check` (render.cmd after the render, verify_render.sh) prints a `[FALLBACK]` line and exits 1 when `--gpu` did not encode on nvenc (the mp4's encoder tag, or a failed nvenc probe: render.cmd sets `HYPERFRAMES_DEBUG_GPU_PROBE=1`), a capture worker was not on NVIDIA, or frames went to disk. The watch stops such a render at the gate line. Cause on record: the ZBook's driver 595.95 was too old for ffmpeg 8.1.2's NVENC, so hyperframes encoded six episodes on Intel QSV without a word.
- Liveness: `python3 scripts/render_busy.py --jobs` (exit 0 idle / 1 busy / 2 process table unreadable, never idle), judged by exe name plus argv, never by process count or a regex over command lines. A wait script calls it and carries no pattern of its own.
- `ffprobe deadline` means slow, never corrupt. The deadline is 30 s and no env var raises it. Cap every source asset at
  the composition's resolution: `media_budget.py` refuses the render otherwise, `optimize_clips.py <episode> --apply` fixes it and never re-encodes the md5-pinned CTA or end-ask clips (test `python3 scripts/test_optimize_clips.py`).
- Owner timestamps against an older cut are mapped by you, never sent back to him: `git show <sha>:episodes/<slug>/index.html`
  into a temp dir, then `clip_report.py` resolves them exactly.

## Git
All git and gh as `sidhartha1s`. Small PRs: `/simplify`, tests + E2E, then `code-reviewer` on Opus; merge only after the owner's OK; rebase-merge, docs sweep in the same PR. `python3`, never
`python`. Node 22 or newer. Before opening and before merging any PR that touches `scripts/`, run
`python3 scripts/e2e.py` (the pinned fixture `scripts/fixtures/e2e/ep-e2e-moore`, or pass `episodes/<slug>` instead for a live one): every self-check green and every run_gates gate run and PASS. A gate that fails or never runs fails e2e. It runs the browser gates, so not beside a render.
