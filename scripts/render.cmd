@echo off
REM render.cmd — the ONE render recipe (draft-proxy + full-quality), per repo CLAUDE.md step 5.
REM Usage:   scripts\render.cmd <episode-slug> <draft|full> [out-basename]
REM Example: scripts\render.cmd ep2-2011-super-outbreak full ep2-final
REM Launch DETACHED (harness bg tasks get killed):
REM   powershell Start-Process cmd.exe -ArgumentList '/c','"<ABS path>\scripts\render.cmd" <slug> <mode>' -WindowStyle Hidden
REM Writes episodes\<slug>\render_<mode>.log and render_<mode>_done.marker (contains npx exit code).
REM Version pin 0.7.81 must match config.yaml hyperframes_version — bump both together.
setlocal
set SLUG=%~1
set MODE=%~2
set OUTBASE=%~3
if "%SLUG%"=="" goto :usage
set EP=%~dp0..\episodes\%SLUG%
if not exist "%EP%\index.html" echo ERROR: no index.html in %EP% & exit /b 1

if "%MODE%"=="draft" (
  set QFLAGS=--quality draft --crf 32 --fps 15
  if "%OUTBASE%"=="" set OUTBASE=%SLUG%-draft
) else if "%MODE%"=="full" (
  set QFLAGS=--quality standard --crf 16 --fps 30
  if "%OUTBASE%"=="" set OUTBASE=%SLUG%-final
) else (
  goto :usage
)

cd /d "%EP%"
REM QC tools (blank_scan.mjs, graphics_qc.mjs) stage _*_tmp.html in the episode root; if one is
REM left behind, hyperframes discovers it as a second root composition and warns of duplicate
REM audio. Sweep them before every render — a render dir must contain exactly one root index.html.
del /q _*_tmp.html 2>nul
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
REM Shared ffmpeg build: security software on this box scans every process creation and the
REM cost tracks binary size (96.6 MB static ffprobe = 1.337s per spawn, 224 KB shared =
REM 0.100s). A render fires ~200 probes. These two paths MUST resolve — media_budget.py
REM fails the render if they do not, because a bad path silently falls back to the slow
REM ffprobe on PATH and the deadline failure comes straight back. See LEARNINGS.md.
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
REM worker count is tunable for RAM-tight full renders (fps30 workers use more memory than
REM draft); default 3 as tested for draft, drop to 2 on a low-free-RAM box. Set RENDER_WORKERS.
if not defined RENDER_WORKERS set RENDER_WORKERS=3
call npx hyperframes@0.7.81 render . --gpu --browser-gpu --experimental-fast-capture=true %QFLAGS% --workers %RENDER_WORKERS% -o "renders/%OUTBASE%.mp4" > "render_%MODE%.log" 2>&1
set RC=%ERRORLEVEL%
echo %RC% > "render_%MODE%_done.marker"
exit /b %RC%

:usage
echo usage: render.cmd ^<episode-slug^> ^<draft^|full^> [out-basename]
exit /b 1
