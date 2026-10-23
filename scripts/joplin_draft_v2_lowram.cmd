@echo off
REM [FALLBACK] one-off, not committed: render.cmd recipe minus the 4 GB RAM preflight, on the owner order 18 Oct 26 20:27-20:50
REM ("render here", "the preview is light"). ASUS had 3.29 GB free at 21:01. Everything else is render.cmd verbatim.
set HYPERFRAMES_NO_TELEMETRY=1
REM 0.8.41 streamed captured frames straight into ffmpeg only for comps <= 240 s; longer comps fell back to
REM disk capture (~8 MB per frame: 131 GB for a 17.6-min draft, C: had 22 GB; ep-1974 21 Sep 26), so this line
REM raised the cap. 0.8.51 turned that cap off by default; the line stays as a harmless belt for any version
REM that brings a cap back (pin_ritual.render_cmd_env() still reads it).
set PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200
REM With --workers > 1 streaming also needs the parallel-capture router (cli.js shouldStreamParallelCapture),
REM else the gate logs enabled:false and the render dies at 'Disk capture may need ~131 GB'.
set HF_CAPTURE_PARALLEL_STREAM=true
set DO_NOT_TRACK=1
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
cd /d "%~dp0..\episodes\ep-joplin-2011"
del /q render_draft_done.marker 2>nul
del /q _*_tmp.html 2>nul
echo [FALLBACK] RAM preflight skipped, owner order > render_draft_preflight.log
echo 15 > render_draft.fps
call npx hyperframes@0.8.149 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps 15 --workers 2 -o "renders/ep-joplin-2011-draft-v2.mp4" > render_draft.log 2>&1
echo %ERRORLEVEL% > render_draft_done.marker
