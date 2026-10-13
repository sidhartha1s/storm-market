# learnings/render.md: render and box ops: hyperframes versions, launchers, RAM/disk, encode, verify_render

Newest first. New entries go at the top, under this line. Superseded lines point at their current home.

## 13 Oct 26: rendering on the ZBook (draft v1 and v2 of ep-palm-sunday-1965)

Owner: "render on zbook." That is the whole order: sync, gates and launch there, no method question back to him, and no
fallback to the build laptop (the draft sat about 5 hours on this laptop's 4 GB floor before it was moved).
1. Code: GitHub login fails over ssh on the ZBook, so commits travel as a bundle. Here: `git bundle create <f>
   <zbook head>..<branch>`; `scp <f> zbook:`; there: `git -C <worktree> pull --ff-only <f> <branch>`. An untracked
   copy of a file the branch now tracks blocks the pull: remove that copy there first.
2. Media and audio are git-ignored: compare md5 manifests of the episode folder on both laptops (filter on the path
   relative to the episode folder: a filter on the full path drops everything under `.worktrees`), send only the
   differences (tar or single files by scp).
3. Never pipe a script into `ssh zbook powershell -Command -`. `scp` a `.ps1` to the ZBook home folder and run
   `ssh zbook powershell -NoProfile -ExecutionPolicy Bypass -File <name>.ps1`, one plain command per call.
4. Gates there first: `python.exe scripts\run_gates.py episodes\<slug>` over ssh took 2 min 42 s (17:23:58 to
   17:26:40) against about 5 min on the build laptop. A log written with `*>>` in PowerShell 5 mixes encodings: drop
   the null bytes before searching it.
5. Launch: a scheduled task with NO trigger (a once-trigger refires), `New-ScheduledTaskPrincipal -UserId
   ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive` (`$env:USERDOMAIN\$env:USERNAME`
   fails over ssh with "No mapping between account names and security IDs"), action `wscript.exe "<scripts>\run_hidden.vbs"
   cmd.exe /c "<scripts>\<ep>_draft_zbook_task.cmd"`, then `Start-ScheduledTask`. The wrapper sets `RENDER_WORKERS=4`.
   Unregister the task when the render ends.
6. Measured, 19 min 44.7 s of video at 4 workers, A2000 through Direct3D11, `streaming-encode gate ... enabled:true`:
   draft v1 `rendered in 28m 58.6s`, draft v2 `rendered in 20m 56.6s`. Free memory on draft v2: 4.85 GB at launch,
   2.0 GB at 73 %, 6.8 GB after.
7. The draft is copied back to the build laptop (`scp "zbook:<path>" <local>`): the owner reviews previews there; the
   final may stay on the ZBook (owner 13 Oct 26).
8. Claude Code's permission system refused the remote task three times as "Unauthorized Persistence" until the owner had
   `~/.claude/settings.json` name the ZBook as his own machine (`permissions.allow` for `ssh zbook` and `scp *zbook*`,
   one `autoMode.allow` and one `autoMode.environment` line). A refusal goes to him as the exact command the same minute.

## 12 Oct 26: verify_render judged every draft as a final

1. Measured on a real 113 s draft: `FAIL: fps 15 != composition 30fps (a draft mastered by mistake?)`, exit non-zero.
   `render.cmd` renders drafts at `_FPS=15` and the check compared the file with the composition's `data-fps`. A draft
   named `ep-palm-sunday-1965-preview-v1` was also checked against `render_full.log` (the log was picked by "draft" in
   the basename) and failed the GPU probe for a log that was not its own.
2. Fix: `verify_render.sh <episode-dir> <basename> <draft|full>` takes the mode you gave `render.cmd`, and it is
   required (missing or unknown: usage line, exit 1; the name guess is gone). The mode picks `render_<mode>.log` and the
   frame rate. `render.cmd` now writes the rate it launched with (`RENDER_FPS` included) to `render_<mode>.fps`; a draft
   must have exactly that rate, and a draft with no `render_draft.fps` (it predates this check, or never reached the
   render step) exits 1 with one FAIL line naming the file. A full render is still held to the composition's `data-fps`,
   so a 15 fps file checked as `full` FAILs and a draft shipped as the final is still caught.
   The recorded rate is per mode, not per output name: two drafts of one episode at different rates share
   `render_draft.fps`, the same limit as `render_draft.log`, so verify a draft before rendering the next.
3. Rule: pass the mode every time, and read the rate from what the render recorded, never from a constant typed in the
   checker (a draft rendered with `RENDER_FPS` set would fail it). The file name says neither.

## 12 Oct 26: pin 0.8.143 to 0.8.149 before Palm Sunday 1965's first render

1. Ritual on demo-pin (hidden task, exit 0): duration 24.000/24.000 s, black 0/0, RMS -21.602701/-21.602708 dB,
   workers 2/2, SSIM 0.9948, video-region SSIM 0.9977. Bumped clean. The SSIM figures sit a little under the 0.8.143
   bump (0.9969 and 0.9990); the ritual's own thresholds passed them.
2. 6 releases are in the range (0.8.144 to 0.8.149, all notes read on the upstream GitHub releases). The ones that can
   change a render: 0.8.144 (audio duration is recovered by decoding the final frame; a data script in a
   sub-composition no longer stops every timeline; a missing timeline is waited for once per render, not once per
   browser; Windows renders stop cancelling when an old parent's pid is reused), 0.8.145 (the audio duration probe reads
   to the end on Windows; long exports with many clips no longer stall at 90 % or hide a timeout), 0.8.146 (exports no
   longer fail on a video clip that sits outside the composition's length; the replacement video frame keeps the
   element's border; re-renders reuse the extracted frames of remote videos; ffmpeg and ffprobe installed by the
   project's npm installer packages are found), 0.8.147 (a render stall names the step Chrome hung in), 0.8.148 (MP4,
   MOV and TS exports keep sound and picture in sync when a file's streams start apart). 0.8.149 only adds an importable
   `hyperframes/api` entry (transcribe, removeBackground): nothing for a render.
3. No seek or font change in this range. The audio duration, stream-start sync and long-export items touch
   what El Reno-length episodes meet, but demo-pin has one tone and a 4 s clip, so it cannot see them: first seen in
   Palm Sunday 1965's draft render. The second A/B in the 0.8.143 entry (snapshot both pins on a real episode) was not
   run for this bump.

## 10 Oct 26: Presenter circle face, SoulX-FlashHead Lite on the ZBook (RTX A2000 8 GB, 15.6 GB RAM)

1. Three local lip-sync models were installed and timed on the same 3.6 s and 10 s lines, wall time from launch to
   finished file: MuseTalk 1.5 105.8 s and 154.6 s (7290 MiB), FlashHead Lite 91.4 s and 121.3 s (6045 MiB), JoyVASA
   lips-only 53.0 s and 93.3 s (2031 MiB). Most of each is start-up. The owner picked FlashHead on the look.
2. One long pass is how FlashHead is built: a portrait and a wav, no text prompt, the audio walked in 0.96 s chunks, each
   chunk carrying on from the last. Measured on 319.3 s of El Reno narration: 782.0 s wall, 53.2 s of it start-up
   (Python and libraries 19.2, model load 26.1, portrait and audio 6.3), then 2.28 s per second of face, 2.11 s per
   chunk and flat over all 333 chunks; card peak 6043 MiB, RAM peak 14.2 GB. The face did not drift or smear over
   the pass, and mouth movement stayed one frame (40 ms) from the voice in the first minute and the last.
3. The makers' `generate_video.py` holds every chunk in RAM until the end (75 MB per 0.96 s, about 25 GB for that
   pass). `scripts/circle_face.py` is the same loop writing each chunk to the mp4 as it is made; it reproduced the
   short clip (SSIM 0.9846). Their 2-step setting saves 17 s on a short clip and smears the face: not used.
4. The install is hand-built and lives only on the ZBook, in the main checkout: `.models\lipsync\` holds a uv-managed
   Python 3.10.20 (`python\`, it runs under Smart App Control), the uv cache and `flashhead\` (`venv\` with torch
   2.7.1+cu128, `repo\` = github.com/Soul-AILab/SoulX-FlashHead at 9bc03de0, `models\SoulX-FlashHead-1_3B` and
   `models\wav2vec2-base-960h`). Three local edits to the repo, none to the model: `COMPILE_MODEL` and `COMPILE_VAE`
   set False in `flash_head/src/pipeline/flash_head_pipeline.py` (no C compiler on Windows), the `xfuser` import in
   `flash_head/src/modules/flash_head_model.py` wrapped in try/except (multi-GPU only), and
   `infer_params['sample_steps']` read from `FH_STEPS` with default 4 in `flash_head/inference.py`.
5. A face pass that stops with the last word leaves the last circle window short: two El Reno windows ran 0.3 s past
   their pass and the pass's last frame was held for them. `circle_audio.py` now pads the wav to the asked end and
   `circle_face.py` keeps its whole last chunk.
6. Launch a pass hidden like a render (`scripts\run_hidden.vbs`), one heavy job at a time on the box: the pass fills
   the card and RAM, so no render beside it.

## 10 Oct 26: first render on the ZBook (hostname Sidhartha, RTX A2000), driven from the ASUS over `ssh zbook`

ep4-el-reno draft, 1333.38 s, 20001 frames at 15 fps, 3 workers: compile 20.2 s, audio 4 min 15.3 s, capture
25 min 11.4 s (13.2 frames/s), assemble 4 min 41.9 s, 34.6 min in all. Output matched the ASUS snapshot frames of all 69 graphics
(SSIM min 0.8837, median 0.9849; the three lowest are moving footage under a card, read side by side). What it took:

1. **Transport.** `git fetch` from GitHub fails in the ssh session (Windows credential store). Ship commits as a
   `git bundle` by scp, fetch from the bundle, fast-forward the worktree. Gitignored media goes by
   `tar -cf - ... | ssh zbook 'tar -xf - -C "<dir>"'`. Before the render, md5 every file the timeline references on
   both laptops: 124 of 124 matched.
2. **First run of a new pin.** `npx hyperframes@X` stops on "Ok to proceed? (y)" in a hidden task and hangs for ever.
   Run `npx --yes hyperframes@X --version` once over ssh first.
3. **Smart App Control is on** and blocks hyperframes' unsigned `chrome-headless-shell.exe` ("Chrome cannot start",
   CodeIntegrity events 3077 and 3118). Set `HYPERFRAMES_BROWSER_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe`
   for the render: the signed Chrome runs headless on the A2000 (`ANGLE (NVIDIA ...)` in the log). Turning Smart App
   Control off is one-way until a reset and is the owner's call.
4. **The GPU needs the logged-on session.** Launch as on the ASUS: a once-only scheduled task through
   `run_hidden.vbs`, then delete the task (a once trigger refires).
5. **The audio mix timed out at 20 %** (`audio_processing_failed`, reason `ffmpeg_timeout`, stage `mix`, 304570 ms).
   hyperframes mixes every audible element in ONE ffmpeg pass under `ffmpegProcessTimeout`, default 300 s. The same
   mix of El Reno's 112 tracks, timed alone: ASUS 23.9x (57.4 s), ZBook 4.8x (about 278 s). Cause on the ZBook: the
   power overlay was "Best power efficiency" (`961cc777-2547-4f9d-8174-7d86181b8a7a`) while on the charger, so the
   single-threaded mix ran on efficiency cores (logical 12 to 19) at 68 % of nominal speed. `FFMPEG_PROCESS_TIMEOUT_MS=900000`
   for that render carried it; the power mode is the owner's setting. Mix time grows with tracks x duration, so check
   it before the first render of any episode on a new box.
6. **ffmpeg differs by session.** Over ssh `ffmpeg -version` is 8.1.1 essentials; the logged-on session's PATH gives
   hyperframes `ffmpeg-8.1.2-full_build-shared` (WinGet). Read the version from the render's own process, not from ssh.
7. **hyperframes' own lint runs inside the render** and printed "12 error(s), 20 warning(s) ... Continuing render":
   `subcomposition_root_styled_by_class` on 8 graphics and `font_family_without_font_face` (AbrilFig, declared once in
   `index.html`) on 4. Both are static guesses: the snapshot frames and the draft show the root styles and the font
   applied. `npx hyperframes@X lint <episode> --verbose` lists them; it also flags `_blank_tmp.html` as a second root
   until `render.cmd` deletes it.
8. `.venv-pocket` is not on the ZBook and `.models` is partial, so voice work stays on the ASUS. A render needs neither.

## 10 Oct 26: pin 0.8.114 to 0.8.143 before El Reno's first render; a real episode's frames as the second A/B

1. Ritual on demo-pin (hidden task, 159 s): duration 24.000/24.000 s, black 0/0, RMS -21.602701/-21.602701 dB,
   workers 2/2, SSIM 0.9969, video-region SSIM 0.9990. Bumped clean.
2. 29 releases were skipped. The ones that can change a render: 0.8.116 (a seek onto a tween's start shows that tween),
   0.8.117 (the render fails when an injected video frame cannot decode), 0.8.122 (composition scripts start after web
   fonts are ready), 0.8.135 (the render fails when a composition's script throws before its timeline binds), 0.8.139
   (renders keep a fromTo's from-only values from the frame it starts on), 0.8.143 (the CLI normalizes the audio
   passage a clip plays; long videos are extracted in segments).
3. The demo has one tone and a handful of tweens, so it cannot see most of that list. Second A/B, cheap and worth
   repeating on every bump made with an episode in hand: `npx hyperframes@<old> snapshot` and `@<new> snapshot` of the
   same episode at one time per composition host, then ffmpeg `ssim` per pair. ep4-el-reno, 69 hosts at 72 % of each
   window: min 0.995305, median 0.999786, none under 0.98. From the first captured frame to the written compare: 156 s.
   It reads stills only: audio and seeks during playback are still first seen in the draft render.

## 26 Sep 26: pin 0.8.41 to 0.8.78; currency moves to episode kickoff; the ritual demo is demo-pin

1. **Owner: "I always prefer the latest version because they will be adding fixes on the go".** The pin LOCK stays
   (preflight drift exit 5); the full-render currency block and its owner override are gone. Kickoff runs
   `pin_ritual.py --check-only` and bumps before the first render, so an episode never changes version mid-way.
2. **demo-joplin-90 could not run the ritual:** 11 of its 17 media/audio files existed nowhere after publish cleanup.
   `episodes/demo-pin` (24 s, every file tracked, under 2 MB) replaces it: tanker MG 0-14 s, WebGL probe 14-24 s, plus
   two ffmpeg-made probes. `clips/probe.webm` (854x480, 30 fps, burned timecode and a sliding white square) mounts at
   16-18 s with `data-media-start 1`, so capture must seek into it. `sfx/tone.ogg` (440 Hz, 4 s) mounts at 3-7 s, gain 0.5.
3. **What `compare()` checks, baseline vs candidate:** worker count equal; duration within 0.05 s; blackdetect segments
   within 0.10 s; tone RMS read over 3.1-6.9 s only (so a moved tone drifts), within 0.20 dB, and a silent render on
   either side is drift; the per-frame luma of a 40x80 tracer strip the square crosses (16.1-17.9 s) within 2.0 levels
   per frame, same frame count; full-frame and video-region SSIM at least 0.99 when the baseline mp4 is on disk.
   `--baseline` measures, validates, and only then writes `pin_baseline.json`: it also refuses a trace spanning under
   50 luma levels, because a flat trace equals itself. Read straight from probe.webm the tracer spans 97.7 levels.
4. **The 0.8.78 A/B predates the probes** (draft crf18, 1 worker): 720/720 frames, 24.000 s both, SSIM mean 0.9973,
   min 0.9930 in the WebGL half vs 0.9905 same-version noise; ritual SSIM 0.9948, PASS. The committed
   `pin_baseline.json` has no `video_luma` or `workers`, so the next ritual run re-records the baseline first.
5. **0.8.78 logs the gate as `"enabled":true,"reason":"single_worker",...`**; the ritual regex still matches. 0.8.51 made
   the streaming duration cap off by default, so render.cmd's 7200 s cap (entry below) is now redundant, harmless.

## 21 Sep 26 — first long render on 0.8.41: streaming needs two env vars, and the harness reaps renders

1. **0.8.41 streams captured frames into ffmpeg only for comps up to 240 s.** Anything longer takes the disk
   capture path and asks for ~8.3 MB per frame of temp space: 131 GB for a 17.6-min draft at 15 fps on a C: with
   22 GB free, so the render dies at "Starting frame capture" with `Disk capture may need ~131756 MB`. The shorts
   final and the pin-ritual demo (29 s, 84 s) never met this. `render.cmd` now sets
   `PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200` and `HF_CAPTURE_PARALLEL_STREAM=true`; the second one
   is required with `--workers` above 1 (`shouldStreamParallelCapture` in cli.js), without it the log still says
   `streaming-encode gate enabled:false`. Read that gate line in every render log: `enabled:true` or the render
   will not finish on this disk.
2. **Harness background Bash is not a render launcher** (already in this file's index line, ignored under
   deadline pressure). The harness kills background tasks when free RAM drops near 2 GB, and the kill takes the
   whole cmd/npx/chrome tree: the 05:28 attempt died 35 min in with the log frozen at 25 % and nine orphan
   chromes. `schtasks /create ... /tr "wscript.exe <abs>\scripts\run_hidden.vbs cmd.exe /c <abs>\scripts\<task>.cmd"`
   plus `/run` (with `MSYS2_ARG_CONV_EXCL='*'` under Git Bash) is the only launcher; the `/tr` string has a
   261-char cap, so the per-episode wrapper `.cmd` (workers, overrides) keeps it short. Delete the task after.
3. **Draft timing on this box at 0.8.41, streaming, 2 workers:** 15 885 frames in about 13 min (frame 600 at
   06:08, complete 06:21), 186 MB at crf 32 / 15 fps. Two workers, not three, when free RAM is under 5 GB.
4. **A render preflight refusal for `ffprobe spawns in 0.40s` is a load reading, not a binary problem**, when
   the env already names the shared build: three whisper transcribers and two ffmpeg cutters from sourcing
   agents pushed a 0.17 s spawn to 0.40 s. Quiet the box (agents' jobs killed by their owners), re-measure.

## 16 Sep 26 — pin bumped to 0.8.41 on owner order; the ritual's RMS drift is a flat mixer offset
- `pin_ritual.py` against 0.8.41: duration 84.000/84.000 s, black map 2/2 identical, RMS −16.91 → −18.04 dB,
  exit 3 (no bump, human decides). Evidence for the decision came from the shorts final, which exists on disk
  at both versions: 0.7.109 draft −12.9 LUFS, 0.8.41 final −14.5 LUFS. Windowed volumedetect on the same cut:
  narration windows −1.3 / −1.7 / −1.8 dB, the bed-only window −1.6 dB; narration-to-bed spacing 30.8 vs
  31.1 dB. Every stem moved together, the balance did not: a flat output-gain change in the 0.8 mixer, and
  `master_deliverables.py` measures and corrects the master to −14 LUFS regardless. Owner: "bump the pin".
- Bumped with the ritual's own `bump_pins()` (config.yaml + render.cmd) and the baseline record rewritten
  from the 0.8.41 demo render (`scripts/pin_baseline.json`: rms −18.04, peak −1.56); the next ritual run
  compares against 0.8.41, not 0.7.109. The demo mp4 is cached at
  `episodes/demo-joplin-90/renders/pin-baseline-0.8.41.mp4` for SSIM.
- New in 0.8.41 and worth reading in every render log: `audio_volume_tween_overrides_gain` (a gsap `volume`
  tween now REPLACES `data-volume`, it does not scale it; demo-joplin-90's bgm trips it) and
  `audio_src_not_found` blocks the render instead of shipping a silent track.
- Ritual gotcha: it prechecked only `media/`, but `audio/` is gitignored too; two launches were wasted in a
  fresh worktree before the narration wavs were copied. The precheck now covers both.

## 16 Sep 26 — hyperframes 0.8.41 full render on this box: no visible windows, clean
Owner asked for the latest hyperframes on the shorts final instead of the 0.7.109 pin. Same flags as
render.cmd, `npx hyperframes@0.8.41`, sh-hawaii-lowell-1 (29.4 s, 1080×1920, 5 clips, 3 workers): rendered in
1m 18.7s, GPU probe NVIDIA, 0 black / 0 silent stretches, 4-frame subagent read identical to the 0.7.109 draft,
master -14.01 LUFS. Owner watched it: "didnt start opening 200 CMD windows … its smooth", so the 0.8.x
visible-terminal-tab problem that froze the pin is gone on this box at 0.8.41. Not a pin bump by itself: run
`scripts/pin_ritual.py` against 0.8.41 (the demo A/B on a 48-clip comp is the test that matters, a 5-clip
short is not) and bump on identical metrics.

## 2026-09-15 — Renders were on the Intel iGPU; pin headless Chrome to the GTX 1650
- **Every render up to 15 Sep captured on the Intel UHD iGPU.** `--browser-gpu` only asks Chrome for
  hardware D3D11; Windows hands an unpinned headless exe the integrated adapter. Measured on
  ms-elnino-cpc-today full (7:47, 2 workers): 26 min, CPU 100 %, render RSS peak 5.7 GB (the iGPU's
  frame buffers live in system RAM), GTX 1650 at 0 %. The owner could not multitask.
- **Fix is a per-user registry pin, no package patch:** `HKCU\Software\Microsoft\DirectX\UserGpuPreferences`,
  value = full exe path, data `GpuPreference=2;`. Chromium reads it; `--force_high_performance_gpu` adds
  nothing on top (probed both). Trap: hyperframes launches its OWN Chrome from
  `~/.cache/hyperframes/chrome/chrome-headless-shell/<ver>/…`, not the Playwright one, and every new
  build is a new exe path. `render_busy.py --launch` now pins every chrome-headless-shell.exe under
  both trees on every launch; `verify_render.sh` fails (exit 2) unless the log's
  `browserGpuMode probe →` line names NVIDIA.
- Still CPU by design in 0.7.109: ffmpeg frame extraction (~70 s for 48 clips) and audio; no hw-decode switch exists.
- RAM floor stays 4 GB: the GPU run's capture RSS is ~4 GB vs ~5–6 GB on the iGPU (k2 logs in the 15 Sep session).

## 15 Sep 26 — first two Format C (rolling update) builds, ms-indonesia-four-volcanoes + ms-hawaii-lowell-outages
- **Two-worker draft render + Firefox = 0.8 GB free.** render_busy's floor is right; nothing else launches during a render.

## 2026-09-11 · OOM: the gate suite ran on top of a live draft render
- Draft (2 capture workers ≈ 2 Chromiums + node) + blank_scan + graphics_qc (2 more headless Chromiums) +
  optimize_clips (ffmpeg batch) + the owner's browser = 16 GB gone; the owner saw the OOM before I did.
- render_preflight only guards the render's own start, and direct launches skip it. New guard
  `scripts/render_busy.py` (exit 3 while any `hyperframes … render` node is alive; RENDER_BUSY_OK=1 override)
  is called from playwright_env.mjs (covers both Chromium gates), optimize_clips --apply, and the slice/draft
  launchers. Rule: one heavy job at a time; gates BEFORE the render, verify_render AFTER it, never beside it.

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts
- **CTA v5 (owner "newest paul CTA sep 6", 2560x1440 source) is transcoded to 1080p30 as the versioned
  asset** `assets/cta/paul-storm-ready-v5-sep6.mp4` (md5 in config.yaml); media_budget refuses 1440p
  sources. hyperframes validator wants `data-has-audio="true"` on the audible CTA video.
- **Render waiters get killed by the harness under memory pressure** (3 headless workers ≈ 3.8 GB);
  use one `Monitor` until-loop on the done marker, never several polling shells.
- Draft render of a 9:45 cut: 13 min wall-clock at 3 workers (frames ~9 fps at 15 fps draft).
- **Full renders refuse (exit 2) while a TTS run or a sourcing agent's ffmpeg is alive** (heavy-process
  limit 2). Sequence: TTS → sourcing → gates → render; never overlap them on this 16 GB box.
- **A full render is never a test (owner 2026-09-09, three wasted Texas full renders):** a mount/layout change is
  verified in this order and no other: read the renderer's runtime path in the pinned package → draft-render a
  20–30 s slice of the REAL index.html (`T0` window, ~1 min) and read one contact strip → re-run the static gate
  suite on the final file → post a one-message plan and wait for "go" → ONE full render. "The previous render
  looked fine" is void once the file changed; never launch a second full render to find out what the first did.
- **Check free disk before every full render, and delete a killed render's spool (2026-09-09, Texas):** the capture
  spool lives in `%LOCALAPPDATA%\Temp\hf-render-*` and reaches ~9–10 GB for a 10-min 30 fps full. Render #1 captured
  all 18690 frames and then died in the encode with ffmpeg exit 4294967268 (= -28, ENOSPC) at 98 % disk; hyperframes
  deletes its own spool on failure, so the frames are gone too and the whole render reruns. Three stale spools from
  killed renders (14.6 GB) plus the extract cache had eaten the headroom. Rule: `df` ≥ 30 GB free before a full;
  killing a render includes deleting its `hf-render-*` dir the same minute; a failure report says what was LOST first.
- **Capture rate on this box is 9–12 fps at 2 workers, content-independent (measured 2026-09-09 from the log
  checkpoints):** a 623 s / 18690-frame timeline takes ~31 min capture + ~4 min encode. The presenter-circle layers
  cost nothing measurable. ETAs come from the log checkpoint fps, never from a window that includes the 4-min extract
  phase (that mistake produced a 58-min ETA for a 35-min render).

## 2026-08-29 — 1440p upload file is HEVC now (owner order, ep2 CTA re-cut session)
1. 1440p HEVC upload file: superseded 2026-09-09 (the 1080p `-master.mp4` is the upload file, no upscale; CLAUDE.md Pipeline step 7). Measured then: h264 cq19/24M 1440p 4.8 GB for 28 min vs hevc_nvenc p7 cq22 3.5 GB, 16 Mbps.
2. **Owner-recut episodes arrive with hot audio.** Ep2 v2 from the external editor measured
   −14.24 LUFS but **+0.30 dBTP** (the July master was −1.0). Always re-run the master step
   (gain + alimiter, video copy) on an owner-supplied cut before the 2K upscale, never
   bit-copy its audio.
3. **Locating edits in an owner re-cut: audio cross-correlation, not frame diffs.** A
   re-export changes grain/grading enough that 32×18 frame hashes disagree (~15–18 mean
   diff) even on identical content; 4 s narration windows cross-correlated at 8 kHz gave
   corr ≥0.98 and pinned every cut to 0.1 s (ep2 v2: trims 2.4 s @0:21, 3.2 s @5:45,
   CTA +15.0 s @8:26, trim 2.2 s after). Map SRT + chapters piecewise through that table and
   split any cue that straddles the inserted segment.

## 2026-08-24 — 1440p upload tier + NVENC-first for mp4 surgery (owner orders, ep1 insert session)
1. 1440p upload tier (h264_nvenc p5 cq19 24M upscale): superseded 2026-09-09 (1080p master is the upload file). Measured claim then: YouTube feeds a 1080p upload ~2.5-4 Mbps VP9, a 1440p upload ~9-20 Mbps.
2. **mp4 surgery on finished renders = h264_nvenc FIRST, never libx264 (measured 2026-08-24).**
   Ep1 15s-insert job on the 17-min master: h264_nvenc p5 cq19 ≈ 7 min; libx264 preset slow
   crf16 was on pace for ~90 min (killed at 0.2x realtime). At 14–16 Mbps consumer-master
   bitrates the quality difference does not survive YouTube's transcode. The PATH ffmpeg
   (Gyan 8.1.1) has working NVENC on this box — same build caveat as the `--hevc` step.
3. **Frame-accurate insert/splice recipe (proven on ep1):** find the true cut with
   `select='gt(scene,0.25)',showinfo` + eyeball extracted frames; single-pass filter_complex
   trim/concat from the ORIGINALS (never a second generation from an intermediate); verify
   splice frames + duration on the output; shift SRT cues and chapter timestamps by the net
   insert-minus-removed delta.

## ep6 ship (2026-08-23) — hyperframes 0.8.x, the hidden-console chain, and a preflight bug
- **hyperframes 0.8.x opens a visible Windows Terminal tab per ffprobe/ffmpeg spawn on this
  box; 0.7.109 does not.** Measured with a process watcher during a hidden demo render: every
  `ffprobe.exe`/`ffmpeg.exe` child of the 0.8.10 render node got its own `conhost.exe` (a new
  console) and `OpenConsole.exe` (a Windows Terminal tab) appeared at the same instants — with
  the render launched through `run_hidden.vbs` exactly like the 0.7.109 renders that show
  nothing. Owner saw "lots of CMDs, 4 at a time". 0.8.10 spawns its ffmpeg/ffprobe children with
  different flags than 0.7.109 (eight `windowsHide:true` sites vs two, new stdio shapes) and
  under node 24's libuv those allocate a fresh console. The telemetry opt-out
  (`HYPERFRAMES_NO_TELEMETRY=1` / `DO_NOT_TRACK=1`) was a red herring — one detached `node -e
  fetch` per run, not the tab source; the env stays set (harmless) but is not the fix.
  **Decision (owner):** ep6 full render on 0.7.109 with the explicit, logged override
  `RENDER_PIN_STALE_OK=1` (render_preflight.py prints `[OVERRIDE]`; override removed 26 Sep 26); pin stayed 0.7.109 (superseded 16 Sep 26: 0.8.41) until an
  upstream version spawns ffmpeg hidden. The 0.8.10 demo render itself PASSED (4m08s, mp4 on
  disk) — the blocker is the windows, not the output. Kill rule: stop the TASK and kill its
  process TREE from the task's root pid; `*hyperframes*`/`*pin_ritual*` command-line matches also
  hit this session's own bash tool shells (and other sessions') — done twice, never again.
- **render.cmd ran preflight BEFORE its own `set HYPERFRAMES_FF*_PATH` lines** → media_budget.py
  measured the slow PATH ffprobe and refused the full render (marker 3). Reordered 2026-08-23:
  env first, then preflight. The draft path had passed only because the PATH spawn happened to be
  under the threshold that day.
- **16 GB is not "room for everything".** frame composites (80 videos in one page) +
  overlap_check + a demo render + faster-whisper concurrently → `mkl_malloc`, `uv_spawn EAGAIN`,
  "Unable to capture screenshot" at frame 390. One browser-heavy job at a time; check
  `FreePhysicalMemory` before launching (2.5 GB free → `RENDER_WORKERS=2`, 7.5 GB → 3).
  Separately: the faster-whisper `small.en` cache on this box is corrupt (`mkl_malloc` regardless
  of RAM) — use `base.en` int8.
- **Gate noise to expect on a finished episode:** `sweep_episode.py` FAILs on src-less `<section>`
  gradients (`?` rows: same-track overlap, adjacent duplicate, asset reuse, media exists) and on
  stills >6s that the lint pacing report already lists; lint is the hard gate. `verify_render`
  exempts black and freeze only inside declared blackout sections and the CTA dips (silence also in
  holds and the CTA body); a dark card that sits still anywhere else, holds included, is a real defect.

## No visible windows, ever (owner 2026-08-21)
- schtasks interactive tasks pop a cmd window on the desktop. ALL scheduled/background
  commands run through `scripts/run_hidden.vbs` (wscript, window style 0 — no flash):
  `/tr "wscript.exe <abs>\scripts\run_hidden.vbs cmd.exe /c <abs>\scripts\render.cmd <slug> <mode>"`.
  Never a bare `cmd /c` task action, never foreground `cmd //c` runs of render.cmd either.
- render.cmd preflight also refuses when ≥3 heavy processes (e.g. leftover headless chrome
  from QC runs) are alive — exit 2 with marker written but log untouched; kill QC browsers
  first, then relaunch.

## 2026-08-16 — ep6 render-failure ledger (3 compile failures, each root-caused)

A. **Animated GIFs kill the compile — never mount a .gif.** hyperframes transcodes every
   GIF at compile with a hardcoded 300s timeout; a 1.6 MB 24-frame radar GIF blew it
   (fail #1). Convert before wiring: single-frame GIF → PNG (`-frames:v 1`), animated GIF
   → mp4. Two of ep6's three "animated" GIFs were actually single-frame — probe
   `nb_frames` first.

B. **Every mounted video needs an audio stream in hyperframes ≥0.7.109 — even muted
   b-roll can be registered as an audio slot.** Fail #3 was `kb-radarloop-audio`: a
   `-an` mp4 I created got an audio reference and compile threw
   `ASSET_MEDIA_TYPE_MISMATCH (expected: audio)`. The CLI does NOT name the culprit —
   found it by temporarily instrumenting `mismatches.push` in the npx-cached cli.js
   (revert after). Fix: mux silence — `-f lavfi -i anullsrc=r=48000:cl=stereo -shortest
   -c:v copy -c:a aac`. (SUPERSEDED 2026-08-17: `optimize_clips.py` no longer strips
   audio — it preserves the source track and muxes silence into mute clips itself. The
   re-mux ritual is retired; the anullsrc recipe stays useful for one-off assets.)

C. **Audio slots longer than their file are silently truncated (compile WARN, not fail)
   — read the WARNs of a FAILED render, they're real defects.** Fail #2's log exposed 5
   beds shorter than their wired windows (worst: 33.5s drone on a 345.4s slot = 5min of
   missing bed that lint/sweep never see). Fix: loop-extend the file to the wired length
   (`-stream_loop N -t <dur>` + 2.5s afade out), or correct data-duration to the true
   file length when the shortfall is a natural tail.

D. **schtasks tasks do NOT start on battery by default** — a /run leaves them "Queued"
   forever. After /create, always:
   `Set-ScheduledTask -Settings (New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries
   -DontStopIfGoingOnBatteries)`. Battery also power-throttles extract/encode — plug in
   for renders.

E. **Clip windows must never exceed real clip length** (draft-blocking freeze class):
   7 ep6 clips were wired longer than their footage (worst +4.8s). Detector: ffprobe
   every `<video>` src vs its data-duration. Fixes by size: big overshoot → re-extract
   longer from the source reel (per-segment cropdetect again); small (<1s) → setpts
   speed-stretch ≤10% (+ atempo on audible clips).

## 2026-08-15 — ep6 TTS + sourcing (measured surprises)
6. **schtasks under Git Bash needs `MSYS2_ARG_CONV_EXCL='*'`** or `/Create`/`/Run` get mangled
   into paths.

## Full-render stability on this box (ep5 v5c, two attempts, 2026-08-14)
- **Close studios/headless browsers before a full render.** Attempt 1 died at frame 29553
  (capture page hung 4+ min, then Page.captureScreenshot protocol error) with 2 studio servers +
  8 chrome-headless shells resident. Attempt 2, same comp, clean box: completed. Free-RAM dipped
  to 0.4GB mid-render and survived — contention, not the comp, is the killer.
- **No resume exists** (0.7.81): captured frames stream to the encoder and are deleted; a crashed
  run leaves nothing reusable. Budget a full restart into any crash.
- **Baseline speed: ~600-900 frames/min at 1080p30, 2 workers** (0.3-0.5x realtime) — matches
  ep2's 75-min/28-min history. 3000fpm/1.1x-realtime expectations don't hold on this box.
- **Delete `render_*_done.marker` BEFORE relaunching a same-name render** — a stale marker from
  the failed attempt made the watcher report the new run dead (false "exit=1").
- **schtasks wrappers: never bare `python3`** — cmd resolves it to the Microsoft Store stub
  (exit 9009). Use the full `...\Python312\python.exe` path.
- **Harness reaping applies to ALL long background jobs, not just renders** — a 10-min master
  build got killed mid-measure. Anything over ~2 min goes schtasks + done-marker + Monitor.

## HF studio (`hyperframes preview`) — capabilities and traps (ep5 v5c, 2026-08-14)
- **Studio cannot preview a full media-heavy episode.** Opening the 32-min comp fired 2,200+
  media requests at once — canvas stays black, audio never starts, node server crawls. For an
  audio/hook check, build a trimmed scaffold comp instead (junction media/audio, subtree-filter
  index to the window, clamp root data-duration).
- **Runtime comp length = max(element windows, LAST GSAP TWEEN POSITION)** — data-duration alone
  doesn't clamp playback. Trimming a comp means trimming the script's tween/kb positions too.
- **`data-composition-id` is a contract with the timeline JS** — renaming it breaks the runtime
  (`StaticGuard: Timeline registered as X but no element has data-composition-id=X`).
- **Studio MUTATES index.html** (stamps `data-hf-id` on every element). Harmless to renders, but
  any script matching tag shapes must not assume attribute order (build_srt.py fixed 2026-08-14).
  Diff index.html after any studio session before trusting downstream tooling.
- **Studio realtime playback jitters video under a transform tween** (per-tick video seeks) —
  looks like violent shake; the seek-by-frame RENDER is clean. Verify motion complaints against
  render frames (tblend diff series: shake = sawtooth; smooth = flat bands) before "fixing".

## Harness background tasks get reaped — long renders need schtasks (measured ep5, 2026-08-06)

Two draft renders launched via the harness's background Bash died mid-capture (41% and 33%)
when the harness killed the task — the CHILD TREE dies too, a few minutes later (the log
keeps heartbeating briefly, which reads as "survived" and isn't). `Start-Process` was already
known-fatal (ep3 attempt 11). The reliable launcher on this box is a one-shot **Windows
scheduled task** (the bare `cmd /c` action below is superseded by `scripts/run_hidden.vbs`, 2026-08-21): `schtasks /create /tn ep5draft /tr "cmd /c cd /d <worktree> &&
scripts\render.cmd <slug> draft" /sc once /st 23:59 /f && schtasks /run /tn ep5draft` —
fully detached, survives the session. Watch it with a log-mtime stall monitor (>10 min
silent = dead), never with a process-name count (MCP daemons match loose filters).

## optimize_clips.py strips audio and ignores bitrate (measured ep5, 2026-08-06)

Two silent failure modes in one script, both hit on ep5:
- **`-an` is unconditional** — it stripped the audio track from all 4 owner-gated INSERT
  clips (the whole point of an insert is its audio). Nothing warned. Restored from
  `media/_orig/` with `-c:a aac`. Rule: after ANY optimize pass, ffprobe the insert clips
  for an audio stream before rendering. (2026-08-17: optimize_clips.py itself now preserves
  audio + muxes silence for mute clips — see "Audio levels + media budget hardening". The
  ffprobe-before-render rule stands for any ad-hoc batch.)
  **RECURRED on ep5 v3 (2026-08-12):** an ad-hoc media-budget crf pass re-encoded every
  mounted mp4 >900KB with `-an` and stripped ins-mckay again; render failed loud at
  `audio_processing_failed` (hyperframes' extractAudioFromVideo, stage "extract", found no
  audio stream — that error code means AN AUDIBLE VIDEO ELEMENT, not a corrupt file). The
  rule is not about optimize_clips.py — it is about `-an` in ANY batch: exclude every
  element mounted un-muted / data-has-audio from the batch, and ffprobe all audible
  elements for an audio stream as the last step before any render.
  (2026-08-17: optimize_clips.py itself now preserves audio + muxes silence for mute
  clips — see "Audio levels + media budget hardening". The any-ad-hoc-batch rule stands.)
  **Corollary (ep5 v4, 2026-08-12): a "lost" source is probably in `media/_orig/`.**
  Two audio-stripped sources triggered a re-download hunt (Wayback CDX + Brightcove id
  spelunking for a Gannett CDN mp4) while byte-identical audio-bearing originals sat in
  `media/_orig/` the whole time — optimize passes MOVE originals there. Check `_orig/`
  (and `_orig_media/`) before any re-download. Bonus fact recovered anyway: the dozer-911
  mp4 URL is `media.gannett-cdn.com/28911775001/28911775001_5851158634001_5851141890001.mp4`
  (still live; provenance.csv row elided it with `...`— never elide URLs in provenance).
- **It only checks resolution and window-length, not bitrate.** ffmpeg scene cuts made with
  stream-copy keep the source's 15-19 Mbps, so 78 within-spec clips still totalled 645 MB
  against the 150 MB decode budget. Fix: re-encode cuts at libx264 crf 23-27 when cutting
  (~0.5 MB/s lands the budget); crf 27-32 passes cost little on graded b-roll.

## Duplicate element ids render BLACK — and no gate caught it (measured ep5, 2026-08-06)

Two `<video>` windows shared `id="vx-carrwaterb2"` (a copy-paste slip during the retention
re-cut). hyperframes keys frame placement by element id, so the FIRST window (581.9s, 8s)
rendered **pure black** while every static gate passed — sweep, lint, blank_scan and
graphics_qc all read attributes, none checks id uniqueness. Found only by post-render
`verify_render.sh` blackdetect + eyeballing the frame. **Check before every render:**
`grep -o ' id="[^"]*"' index.html | sort | uniq -d` must print nothing. (Now `sweep_episode.py` check 5b.)

## Render size + HEVC compression (measured ep3 v5, 2026-07-30)

A full render at `--crf 16 --fps 30` is ~20 Mbps → **5.08 GB for 34m56s**. That is near-lossless
overkill for graphics/stills content. Two ways to ship smaller **without visible quality loss**:

- **Single-pass (no extra step) — the "compress during render" answer:** hyperframes emits
  **H.264 only** for mp4 (vp9 for webm); there is **no HEVC output flag**. But `--crf`, `--fps`,
  and `--video-bitrate` are all render-time flags. Render the final at `--crf 19-20` and author
  at **24 fps** (most YouTube docs) → ~1.5-2 GB H.264 in one pass, no transcode. The slow part is
  frame *capture* (~1.2x realtime, ~98 min here); the encode target is nearly free to change.
- **HEVC (extra shrink) needs a transcode** — hyperframes can't emit it. But the transcode only
  decodes+encodes, it does NOT re-capture frames, so on GPU it is a ~6-min add-on, not a second render.

**NVENC driver gotcha (cost an hour to spot):** the pinned **Gyan.FFmpeg.Shared 8.1.2** build's
`hevc_nvenc` fails with `Driver does not support the required nvenc API version. Required: 13.1
Found: 13.0` (exit -40) — its NVENC needs Nvidia driver 610+. The older **Gyan.FFmpeg.Essentials
8.1.1** build on PATH has a compatible NVENC and works. Use 8.1.1 for NVENC, or update the driver.

Measured HEVC transcode of the −14 LUFS master (5097 MB, `-c:a copy`, audio untouched):

| encoder | speed on this box (GTX 1650) | wall time (35 min vid) | output |
|---|---|---|---|
| `libx265 -preset slow -crf 22` | **0.15x** | **~4 hours** | ~1.2 GB |
| `hevc_nvenc -preset p7 -cq 22` (ffmpeg 8.1.1) | **5.96x** | **~6 min** | **2.19 GB** |

**Takeaway:** software x265 `preset slow` is a non-starter for a review loop (0.15x). GPU
`hevc_nvenc p7 cq22` gives a 2.3x shrink in 6 minutes, visually lossless, audio bit-copied. For
future episodes the cleanest is to render at a higher CRF + 24 fps so the small file falls out of
the render itself; reach for the GPU-HEVC pass only when you want the extra shrink.

## ep3 v3 — stop rendering to find things a script can find (2026-07-29)

- **Owner correction, and the sharpest one of this episode: renders 7, 8 and 9 all died to
  defects I could have found before starting them.** I rendered, thought of a new check,
  killed the render, rendered again. Every check I invented reactively is now a script that
  runs in seconds — `scripts/sweep_episode.py`, `beat_density.py`, `blank_scan.mjs`,
  `clip_report.py`. The rule: **exhaust every static gate, THEN render once.** A render is
  the last step, not a diagnostic tool.
- **The `ffprobe deadline with code 0` failure was never a bad asset — the deadline was 120s,
  hardcoded (30 s since 0.7.81, see below).** hyperframes 0.7.64 wraps its probes in `deadlineAtMs: Date.now() + 12e4` with
  no env override, and the probe it runs at `video_extract` is not the cheap duration read —
  it is `-count_packets`, which walks every packet. Measured on an idle box with the exact
  arguments: worst clip 3.05s, whole 16-clip pass 29.9s. The
  failed render spent 274s inside `video_extract` before a single probe blew 120s, i.e. the
  box was running roughly 40x slower than idle. Cost does NOT track file size — the 57 MB
  transcode probes in 2.0s while a 10 MB lightning clip takes 3.05s — so the "4K asset"
  theory was wrong twice over. The fix is `render_preflight.py` plus an otherwise-idle box.
- **Coverage tools must name their picture tracks.** `clip_report.py` counted every track,
  so nine overlay windows (date card, source chip, quote cards, lower-thirds) papered over
  the black underneath them; the date card alone hid 0.30-14.3s. Whitelist the picture
  tracks, then prove the check can still fail by deleting one still from a scratch copy.
**Render (2026-07-27, ep2 full render):**
- Full-quality render died at 74% with `Protocol error: Target closed` after a burst of
  `net::ERR_NETWORK_CHANGED` on the localhost media server — a host network-interface change
  (Wi-Fi/VPN flip) mid-capture kills the Puppeteer browser's media fetches. Environmental, not
  a comp defect (same comp draft-rendered clean). Fix: relaunch with
  `PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000` alongside the nav-timeout var; avoid network
  changes during long renders. A ~28-min comp at standard/30fps ≈ 75+ min capture on this box —
  budget 2h wall-clock when the machine is also running other sessions.
- **Check the hyperframes version before production starts, and read what changed.** Bumped
  0.7.64 -> 0.7.81 on 2026-07-29 (owner order). The upgrade **shortens the ffprobe deadline
  from 120s to 30s** (`Date.now() + 12e4` became `+ 3e4`) — the exact deadline twelve ep3 v3
  renders died on. A newer version can be STRICTER, not just better, so every timing measured
  against the old pin has a 4x smaller margin. `npm view hyperframes version` is one command
  and belongs at the top of a production run, not after a failure. Bumped 0.7.81 -> 0.7.107 on
  2026-08-14 after the ritual: changelog audit (827 commits; relevant = extraction memory
  bounding, hidden-audio excluded from render mix, WebGPU capture fixes; ffprobe 30s deadline
  UNCHANGED, verified in dist) + A/B render of demo-joplin-90 at full quality — identical
  duration/blackdetect, RMS delta 0.006 dB, SSIM 0.997, spot frames clean. No behavior change
  observed; the hidden-audio mix change did not alter loudness on a comp using visible audio tags.
  **Ritual scripted 2026-08-14 (owner: manual refresh was "stupid" — pin rotted 26 versions in
  2 weeks while the warn-only banner fired unheard):** `scripts/pin_ritual.py` runs the whole
  thing (npm view, candidate render of demo-joplin-90, metric diff vs committed
  `pin_baseline.json`, auto-bump on identical metrics, exit 3 + no bump on drift), and
  `render_preflight.py` — now actually invoked by `render.cmd` — hard-blocks FULL renders on a
  stale pin (exit 6) while drafts only warn (superseded 26 Sep 26: preflight checks drift only, currency
  moves to episode kickoff, demo is episodes/demo-pin). npm unreachable never blocks. Baseline mp4 is an
  on-disk cache (`episodes/demo-joplin-90/renders/pin-baseline-<ver>.mp4`); when absent, the
  ritual re-renders the baseline too (metrics-only compare if that ever fails to keep SSIM).
  **Gotcha that cost 40 min:** `npx hyperframes@<uncached-version>` prompts "Ok to proceed?"
  and a detached run hangs on stdin until the timeout — every scripted npx call needs `-y`
  AND `stdin=DEVNULL`. (The schtasks cmd wrappers dodged this by accident; python
  subprocess did not.)
- **THE ep3 v3 render RCA, after thirteen failures: process-spawn scanning, not media.**
  Security software on this box scans every process creation, and the cost tracks
  BINARY SIZE, not work done:

  | binary | size | spawn |
  |---|---|---|
  | `cmd /c echo` | tiny, system | 0.063s |
  | `where.exe` | small, signed | 0.172s |
  | `python.exe` | medium | 0.251s |
  | `ffprobe.exe` (Gyan essentials, static) | **97 MB** | **1.165s** |
  | `ffprobe.exe` (Gyan **shared**) | **224 KB** | **0.102s** |

  A render fires roughly 200 ffprobe spawns (21 video windows x ~3 probe types, ~70 audio
  files x 2). At 1.2s each that is ~200s of pure scanning — and the observed `video_extract`
  stage durations were 193s and 204s. When spawns collide the scanner serialises them and one
  probe waits past its deadline, which is the `ffprobe deadline with code 0` failure.
  **Fix: `winget install Gyan.FFmpeg.Shared` and point hyperframes at it with
  `HYPERFRAMES_FFPROBE_PATH` / `HYPERFRAMES_FFMPEG_PATH`** (both render scripts now do).
  Measured on the real probe over all 16 clips: 1.32s each -> 0.40s each, ~263s -> ~80s
  projected per render.

  **Why it took thirteen renders:** every earlier theory was about the MEDIA (a 4K asset,
  contention, worker count, the deadline value). Cutting media 72%, halving workers, and
  changing the deadline 120s->30s each changed NOTHING, and that was the signal — a
  performance fix that moves the needle zero means the model of the problem is wrong. The
  question that cracked it was "how long does ffprobe take when it opens no file at all?"
  (1.4s, versus 0.06s for `cmd`). **When three independent fixes change nothing, stop fixing
  and go measure the thing every attempt has in common.**

## ep3 v3 — the defects no code gate was looking for (2026-07-29)

- **Run `blackdetect` on every render. The picture track can be empty and every static gate will
  still pass.** ep3's segment scheduler advanced by `seg_dur + GAP` but only covered `seg_dur`
  with picture windows, so the 0.75s breath between narration segments had nothing on tracks 1/2.
  `ffmpeg -vf blackdetect=d=0.1:pix_th=0.10` on the draft found **81 black spans, 63 at segment
  boundaries**; sampled frames were pure black. lint_timeline PASSED, graphics_qc PASSED,
  hyperframes check found nothing — because none of them ask "is anything on screen at time t".
  The gate that catches it is a union-coverage sweep of every element carrying
  `data-start`+`data-duration`+`data-track-index`, compared against the comp duration.
  Reference floor: ep2 (shipped) has 2 uncovered gaps, ep1 has 6. Anything in the dozens is a bug.
- **Corollary: a coverage report must read the ELEMENT, not the animation array.** My first pass
  parsed only the ken-burns `KB` array and the sub-composition hosts, and reported 63 gaps *plus*
  16s phantom holes — because `<video>` clips carry their timing on the element itself and never
  appear in KB. Same-shaped bug, opposite direction: it invented gaps that did not exist while
  missing 32 real windows. Enumerate by attribute, never by animation bookkeeping.
- **`blackdetect` false-positives on dark graphics.** Half the flagged spans were title cards on a
  near-black background, correctly rendering. Verdict requires eyeballing a frame from each span
  (dispatch a subagent — never Read frames into the main context). File size is a decent triage
  signal: the truly-black JPEGs were 13KB, the content ones 38–47KB.
- **"ffprobe deadline with code 0" is a size problem, not a corruption problem.** Render #7 died at
  10% of `video_extract` after 141s. All 18 video assets probed clean. The cause was one 365MB
  3840x2160 stock clip feeding 12.9s of a 1080p comp — 10x every other asset. Transcoding it to
  1080p (365MB -> 54MB) is the durable fix; retrying the render is not. Cap source assets at the
  composition's own resolution before wiring them.
- **`hyperframes check` reports `data-end without data-duration` for every `<audio>`/`<video>` in
  a composition whose source contains zero `data-end`.** It is validating a normalized DOM, not the
  source. Verified pre-existing by running `check` against the git-HEAD index.html. It does not
  block `render`. Don't burn a cycle chasing it — but do re-verify it is pre-existing rather than
  assuming, by checking out the prior file and re-running.

## ep3 v3 - second audit round (2026-07-29)
- **`ffprobe` on a still image reports ~0.04s.** Any clamp that treats that as a clip duration will
  cut a window into single-frame slivers. Guard duration probes by file extension and fail loud
  when a non-video is typed as a clip.

## ep3 v3 (2026-07-29) — the "check the code, not the frames" rebuild
- **`hyperframes check` (not the deprecated `validate`) is the real static gate.** It caught 19
  errors a frame sweep never would. Run it before every render, not after.
- **Quantize the timeline to the decimal grid you print at.** Accumulating `ct += w` in float
  while emitting `{ct:.2f}` makes a window's printed end land 0.01s past the next window's
  printed start — 44 same-track overlap errors. Round every start and duration to 2dp and
  accumulate the rounded values, so end == next start bit-for-bit.
- **Clamp every clip window to the clip's own length at BUILD time** (`ffprobe`, cached). This is
  the ep3-v2 frame-coverage failure caught one stage earlier, deterministically, instead of 20
  minutes into a render.
- Hand-declared beat weights bypassing the pacing clamps: superseded by the generator purge (2026-08-02); timelines are hand-authored and stills cap at 6 s (sweep check 9).

## ep3 v2 (2026-07-28)
- **`loop` attribute does NOT survive render**: hyperframes 0.7.64 video extraction ignores `loop`; a looped clip window longer than the source fails the 95% frame-coverage gate ("captured N of expected M frames"). Fix at the asset level: pre-loop the file with `ffmpeg -stream_loop N -i src -t <maxwin+2> -g 30 -keyint_min 30` and keep the filename. Never set `HF_VIDEO_COVERAGE_THRESHOLD=0` — the gate is right, the encode would freeze/blank.
- **Don't run whisper transcription concurrently with a render**: CPU starvation made hyperframes' ffprobe miss its deadline ("[FFmpeg] ffprobe deadline with code 0") during video_extract. Sequence them.
- **`hyperframes snapshot` accepts only one `--at`** — repeated flags silently collapse (and add a stray extra frame); loop one invocation per timestamp for fixchecks.

## 2026-07-27 — ep2 hook rebuild + ship (hook contract now in DESIGN.md)

**Pipeline / tooling (all reproduced):**
3. **`--workers` must be pinned on full renders** — omitted, hyperframes "auto" resolved to 1
   worker on a loaded box (2× slower than the 3-worker draft). Recipe in CLAUDE.md/DESIGN.md
   now pins `--workers 3`.
4. **`render . <file.html>` entry arg is IGNORED by hyperframes 0.7.64** — it silently renders
   the default composition. There is no partial/preview render via entry file; use duration
   overrides or sub-comp renders instead.
5. **Start-Process ArgumentList quoting:** a .cmd path containing spaces must carry embedded
   escaped quotes (`'\"C:\...path with spaces...\.cmd\"'`) — unquoted, cmd.exe silently no-ops
   and no log ever appears.
6. **Harness kills long-running background Bash watchers between turns** — completion watches
   on renders must use the Monitor tool (poll a done-marker every ~120s), and the filter must
   emit on ALL terminal states (complete AND error/fail lines), not just success.
7. **Master pass numbers (ep2):** full-comp mix landed −13.13 LUFS / TP +0.05 (hot). Master =
   `-c:v copy -af volume=-1.05dB -c:a aac -b:a 256k` → −14.19 LUFS / TP −1.01, verified with a
   second loudnorm read. Plain gain beats dynamic loudnorm when input LRA is already tight (3.4).

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)
- **QC density:** 18 frames on a 28-min video is not a review. Dense sweep ≈ 1 frame / 15-20s
  plus targeted checks on every region you changed.

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)

- **Snapshot `--timeout` covers ONLY runtime init; page navigation is a separate 10s default**
  that kills media-heavy comps with "Navigation timeout of 10000 ms exceeded". Fix: env var
  `PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000` (found in cli.js `resolveDiagnosticNavigationTimeoutMs`).
  Applies to snapshot AND render — set it on every invocation for big comps.
- Harness background Bash dies at the 120 s timeout or on compaction; the Start-Process launcher that followed is superseded by schtasks + `scripts/run_hidden.vbs` (2026-08-21). Relative .cmd paths silently no-op; one npx call per .cmd.
- **Snapshot's video-frame extraction can fail per-frame** ("could not be extracted — will appear
  black/stale") while the composition is fine — the RENDER captures live playback and is unaffected.
  Verify suspects by ffmpeg-extracting frames from the source media at the mapped offsets
  (data-start/trim math), not by rerunning snapshot.

## 2026-07-26 — draft-proxy render validated (timed on ep1 v3d, 17:17 comp)

`--quality draft --crf 32 --fps 15 --workers 3`: **21m 16s vs 39m 32s** standard (46% faster),
258 MB vs 1775 MB. 1080p at 15fps — quote/graphic text fully readable in extracted frames;
review-quality confirmed by eyeball. Capture dominates render time (fps halving ≈ halves capture;
encode/pipeline overhead is the floor), so don't expect draft to scale below ~half. This is THE
review path per CLAUDE.md; full-quality render only after owner approves the draft.
Monitor gotcha: "render finished" check via `tasklist ... node.exe` is too broad — other node
processes keep it true forever; watch for the log's "Render complete" line instead.

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)
A 4-agent Workflow sweep before the v3 render found 10 issues, 3 blockers; the "standing pre-render step" is superseded by `scripts/run_gates.py` plus the settle-frame pass (references/mg-quickref.md "Verify").
2. **`data-media-start` on a clip broke snapshot frame extraction** (funnel beat rendered black
   in snapshots though the file was healthy). Robust pattern: pre-trim the segment into its own
   file (`tornado-funnel-hold-4s.mp4`) and drop data-media-start when a beat uses a mid-file window.
6. Every intentional dead-frame beat gets an explicit track-4 blackout section — an undocumented
   coverage gap is indistinguishable from a bug in review.

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)
8. Detached Start-Process render path: superseded by schtasks + `scripts/run_hidden.vbs` (2026-08-21). Kill orphan chromes before rendering; chunked rendering stays out until a single render fails.
9. Local npx-cache patch of the 0.7.64 ffprobe deadline: superseded by the shared ffprobe build (2026-07-29) and later pins (0.8.41 since 16 Sep 26).

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")

**Hyperframes 0.7.64 gotchas (cost a lint/fix cycle each — pre-empt next time):**
- Every `<audio>`/`<video>` with `data-start` NEEDS an `id` — silently SILENT/FROZEN in render without it.
- `window.__timelines = window.__timelines || {}` before assignment (lint error otherwise).
- Root composition div needs `data-start="0"`.
- No layout-property tweens (letterSpacing) — transforms/opacity only.
- Same-track time overlap = lint error; give crossfade/blackout elements their own track.
- StaticGuard "uses data-end without data-duration" on validate = **false positive** in 0.7.64
  (reproduced on JP-market's known-good probe fixture) — ignore, don't chase.
- `hyperframes transcribe` silently produced nothing on this box — use faster-whisper
  (`scripts/transcribe_episode.py`; since 7 Oct 26 its model lives in `config.yaml external.hf_home`).
**QC:**
- xstack contact sheets pad undefined regions GREEN — padding, not video content; don't panic.
- Snapshot sweep (~13 frames) as the mandatory pre-render gate: superseded by code gates + settle frames (2026-07-29, references/mg-quickref.md "Verify").
