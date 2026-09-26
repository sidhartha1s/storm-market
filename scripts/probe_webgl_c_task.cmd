@echo off
REM Probe run-c: direct hyperframes render, fast capture OFF, no --gpu (encoder), env block copied from render.cmd.
setlocal
set EP=%~dp0..\episodes\probe-webgl
del /q "%EP%\render_draft_done.marker" 2>nul
cd /d "%EP%"
set HYPERFRAMES_NO_TELEMETRY=1
set PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200
set HF_CAPTURE_PARALLEL_STREAM=true
set DO_NOT_TRACK=1
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
echo start %DATE% %TIME% > "timing_run-c.txt"
call npx hyperframes@0.8.41 render . --browser-gpu --experimental-fast-capture=false --quality draft --crf 18 --fps 30 --workers 1 -o "renders/run-c.mp4" > "render_run-c.log" 2>&1
set RC=%ERRORLEVEL%
echo end %DATE% %TIME% >> "timing_run-c.txt"
echo %RC% > "render_draft_done.marker"
exit /b %RC%
