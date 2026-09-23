@echo off
REM render.cmd — the ONE render recipe (draft-proxy + full-quality), per repo CLAUDE.md step 5.
REM Usage:   scripts\render.cmd <episode-slug> <draft|full> [out-basename]
REM Example: scripts\render.cmd ep2-2011-super-outbreak full ep2-final
REM Launch DETACHED (harness bg tasks get killed):
REM   powershell Start-Process cmd.exe -ArgumentList '/c','"<ABS path>\scripts\render.cmd" <slug> <mode>' -WindowStyle Hidden
REM Writes episodes\<slug>\render_<mode>.log, render_<mode>_preflight.log (gate output, so a
REM hidden/schtasks launch still leaves a refusal reason on disk) and render_<mode>_done.marker
REM (contains the exit code; deleted at the start of every run so a poller never reads a stale one).
REM Version pin must match config.yaml hyperframes_version — pin_ritual.py bumps both together.
REM Stale-pin full renders need RENDER_PIN_STALE_OK=1 (owner override, printed by preflight).
setlocal
set SLUG=%~1
set MODE=%~2
set OUTBASE=%~3
if "%SLUG%"=="" goto :usage
set EP=%~dp0..\episodes\%SLUG%
if not exist "%EP%\index.html" (
  echo ERROR: no index.html in %EP%
  echo 1 no-index-html %SLUG% %MODE%> "%~dp0render_last_error.marker"
  exit /b 1
)
REM Delete BEFORE any gate runs (LEARNINGS.md:449) — a poller must never read the previous
REM run's marker as this run's result. Every error path below (including :usage) writes a
REM fresh one, so "done" is never silently stale.
del /q "%EP%\render_%MODE%_done.marker" 2>nul

REM CRF/FPS are tunable per render. Defaults reproduce the tested recipe (full crf16/30fps,
REM draft crf32/15fps). For a smaller single-pass full render, author at 24fps and set
REM RENDER_CRF=20 — visually lossless for this content, ~half the size, no transcode. See
REM LEARNINGS.md "Render size + HEVC compression".
if "%MODE%"=="draft" (
  set QUAL=draft
  set _CRF=32
  set _FPS=15
  if "%OUTBASE%"=="" set OUTBASE=%SLUG%-draft
) else if "%MODE%"=="full" (
  set QUAL=standard
  set _CRF=16
  set _FPS=30
  if "%OUTBASE%"=="" set OUTBASE=%SLUG%-final
) else (
  goto :usage
)
if defined RENDER_CRF set _CRF=%RENDER_CRF%
if defined RENDER_FPS set _FPS=%RENDER_FPS%
set QFLAGS=--quality %QUAL% --crf %_CRF% --fps %_FPS%

cd /d "%EP%"
REM Shared ffmpeg build: security software on this box scans every process creation and the
REM cost tracks binary size (96.6 MB static ffprobe = 1.337s per spawn, 224 KB shared =
REM 0.100s). A render fires ~200 probes. These two paths MUST resolve — media_budget.py
REM fails the render if they do not, because a bad path silently falls back to the slow
REM ffprobe on PATH and the deadline failure comes straight back. See LEARNINGS.md.
REM hyperframes >=0.8 telemetry spawns DETACHED `node -e fetch(...)` children with no windowsHide
REM = a visible console window per flush (owner 2026-08-23). Opt out unconditionally.
set HYPERFRAMES_NO_TELEMETRY=1
REM 0.8.41 streams captured frames straight into ffmpeg only for comps <= 240 s; longer comps fall back to
REM disk capture (~8 MB per frame: 131 GB for a 17.6-min draft, C: had 22 GB; ep-1974 21 Sep 26). Raise the cap
REM so every episode streams. Streaming is the path the 0.8.41 shorts final and the pin-ritual demo used.
set PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200
REM With --workers > 1 streaming also needs the parallel-capture router (cli.js shouldStreamParallelCapture),
REM else the gate logs enabled:false and the render dies at 'Disk capture may need ~131 GB'.
set HF_CAPTURE_PARALLEL_STREAM=true
set DO_NOT_TRACK=1
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
REM Preflight gate (busy box / media budget / pin drift / pin currency). CLAUDE.md has always
REM said "the render script calls this file" — as of 2026-08-14 it actually does. Full python
REM path: under schtasks/cmd, bare python3 resolves to the MS Store stub (exit 9009).
REM MUST run AFTER the FF*_PATH lines above: media_budget.py measures the ffprobe the env names,
REM and with no env it measures the slow PATH build and refuses (ep6 full attempt 1, 2026-08-23).
"C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" "%~dp0render_preflight.py" "%EP%" %MODE%
if errorlevel 1 (
  echo PREFLIGHT REFUSED exit %ERRORLEVEL% — see output above
  echo %ERRORLEVEL% > "render_%MODE%_done.marker"
  exit /b %ERRORLEVEL%
)
REM QC tools (blank_scan.mjs, graphics_qc.mjs) stage _*_tmp.html in the episode root; if one is
REM left behind, hyperframes discovers it as a second root composition and warns of duplicate
REM audio. Sweep them before every render — a render dir must contain exactly one root index.html.
del /q _*_tmp.html 2>nul
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
REM worker count is tunable for RAM-tight full renders (fps30 workers use more memory than
REM draft); default 3 as tested for draft, drop to 2 on a low-free-RAM box. Set RENDER_WORKERS.
if not defined RENDER_WORKERS set RENDER_WORKERS=3
call npx hyperframes@0.8.41 render . --gpu --browser-gpu --experimental-fast-capture=true %QFLAGS% --workers %RENDER_WORKERS% -o "renders/%OUTBASE%.mp4" > "render_%MODE%.log" 2>&1
set RC=%ERRORLEVEL%
echo %RC% > "render_%MODE%_done.marker"
exit /b %RC%

:usage
echo usage: render.cmd ^<episode-slug^> ^<draft^|full^> [out-basename]
exit /b 1
