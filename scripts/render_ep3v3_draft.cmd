@echo off
rem ep3 v3 draft render. Launch DETACHED so this session cannot reap it:
rem   Invoke-CimMethod Win32_Process Create -Arguments @{CommandLine='cmd.exe /c ""<abs path>""'}
rem Absolute exe paths throughout: a detached process does not inherit this shell's PATH,
rem so bare `python3` hits the Microsoft Store stub and `npx` is not found at all.
rem Shared ffmpeg build: scan cost tracks binary size (96.6 MB static ffprobe = 1.337s per
rem spawn, 224 KB shared = 0.100s) and a render fires ~200 probes. See LEARNINGS.md.
setlocal
set EP=C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\episodes\ep3-tristate
set SC=C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\scripts
set PY=C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe
set NPX=C:\Program Files\nodejs\npx.cmd
set FFDIR=C:\Users\Sidhartha\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build-shared\bin

cd /d "%EP%"
if not exist renders mkdir renders
set LOG=renders\render_v3_draft.log
rem First write, so an empty/absent log always means the script itself never started.
echo [start] %DATE% %TIME%> "%LOG%"

set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
set HYPERFRAMES_FFPROBE_PATH=%FFDIR%\ffprobe.exe
set HYPERFRAMES_FFMPEG_PATH=%FFDIR%\ffmpeg.exe

call "%PY%" "%SC%\render_preflight.py" "%EP%" >> "%LOG%" 2>&1
if errorlevel 1 (
  echo 90> renders\render_v3_draft_done.marker
  exit /b 90
)

call "%NPX%" hyperframes@0.7.81 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps 15 --workers 2 -o renders/ep3-tristate-v3-draft.mp4 >> "%LOG%" 2>&1
echo %ERRORLEVEL%> renders\render_v3_draft_done.marker
