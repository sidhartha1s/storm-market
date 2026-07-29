@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\episodes\ep3-tristate"
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
rem Use the SHARED ffmpeg build. This box runs Defender + McAfee + CrowdStrike, all of which
rem scan every process creation, and the scan cost tracks the binary size: the 97 MB static
rem ffprobe.exe costs 1.165s per spawn, the 224 KB shared one costs 0.102s. A render fires
rem roughly 200 probes, so that is 200s of pure scanning versus 20s - and the 200s version is
rem what pushed a single probe past its deadline and killed thirteen renders.
set HYPERFRAMES_FFPROBE_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin\ffmpeg.exe
if not exist renders mkdir renders
rem A render sharing this box with the Playwright QC gates starves at video_extract
rem and dies with 'ffprobe deadline with code 0', which looks like a bad asset.
python3 "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\scripts\render_preflight.py" "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\episodes\ep3-tristate" >> renders\render_v3_draft.log 2>&1
if errorlevel 1 (
  echo 90 > renders\render_v3_draft_done.marker
  exit /b 90
)
call npx hyperframes@0.7.81 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps 15 --workers 3 -o renders/ep3-tristate-v3-draft.mp4 >> renders/render_v3_draft.log 2>&1
echo %ERRORLEVEL% > renders\render_v3_draft_done.marker
