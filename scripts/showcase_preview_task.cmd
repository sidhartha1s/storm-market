@echo off
REM One-off preview of the no-house-rules showcase MG (owner ask 26 Sep 26).
REM OWNER OVERRIDE 26 Sep 26 ("override"): skips the 4 GB free-RAM preflight for this 14 s, no-video comp only.
REM Same env and render flags as render.cmd; 30 fps so motion reads; 1 worker for low RAM.
setlocal
cd /d "%~dp0..\episodes\demo-mg-showcase"
del /q render_draft_done.marker _*_tmp.html 2>nul
set HYPERFRAMES_NO_TELEMETRY=1
set DO_NOT_TRACK=1
set PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200
set HF_CAPTURE_PARALLEL_STREAM=true
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
echo [OVERRIDE] owner skipped the 4 GB RAM floor for this preview > render_draft_preflight.log
call npx hyperframes@0.8.41 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 20 --fps 30 --workers 1 -o "renders/showcase-preview.mp4" > render_draft.log 2>&1
echo %ERRORLEVEL% > render_draft_done.marker
