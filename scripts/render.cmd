@echo off
REM render.cmd — the ONE render recipe (draft-proxy + full-quality), per repo CLAUDE.md step 5.
REM Usage:   scripts\render.cmd <episode-slug> <draft|full> [out-basename]
REM Example: scripts\render.cmd ep2-2011-super-outbreak full ep2-final
REM Launch DETACHED (harness bg tasks get killed):
REM   powershell Start-Process cmd.exe -ArgumentList '/c','"<ABS path>\scripts\render.cmd" <slug> <mode>' -WindowStyle Hidden
REM Writes episodes\<slug>\render_<mode>.log and render_<mode>_done.marker (contains npx exit code).
REM Version pin 0.7.64 must match config.yaml hyperframes_version — bump both together.
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
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
call npx hyperframes@0.7.64 render . --gpu --browser-gpu --experimental-fast-capture=true %QFLAGS% --workers 3 -o "renders/%OUTBASE%.mp4" > "render_%MODE%.log" 2>&1
echo %ERRORLEVEL% > "render_%MODE%_done.marker"
exit /b 0

:usage
echo usage: render.cmd ^<episode-slug^> ^<draft^|full^> [out-basename]
exit /b 1
