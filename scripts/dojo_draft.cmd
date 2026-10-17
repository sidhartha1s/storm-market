@echo off
REM dojo_draft.cmd: the only way the dojo-ops dashboard starts a Storm render (a draft, 2 workers).
REM dojo-ops reporter/render.py (sidhartha1s/dojo-ops PR #41, design B) writes the episode slug to
REM %LOCALAPPDATA%\dojo-ops\render-request.txt and starts this file with no arguments, so no dashboard
REM text is ever on a command line. The slug was checked there against this laptop's own Storm episode
REM list; it is data from outside, so it is checked again here before render.cmd sees it.
REM Exit codes: 2 no request, 3 request refused, 4 no such episode, else render.cmd's own.
setlocal EnableExtensions DisableDelayedExpansion
set "REQ=%LOCALAPPDATA%\dojo-ops\render-request.txt"
if not exist "%REQ%" exit /b 2
REM findstr by full path: with Git on PATH, a bare find or findstr can resolve to the GNU tools (a bare
REM find hung the test, 18 Oct 2026).
set "FINDSTR=%SystemRoot%\System32\findstr.exe"
REM At most one line, and every line is 1+ of A-Z a-z 0-9 _ - (letters spelled out: findstr's [A-Z]
REM also matches accented letters). /v /x lists lines that do NOT match whole; any such line refuses.
"%FINDSTR%" /n "^" "%REQ%" | "%FINDSTR%" /b /c:"2:" >nul && goto :refuse
"%FINDSTR%" /r /v /x /c:"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-]*" "%REQ%" >nul && goto :refuse
set "SLUG="
set /p SLUG=<"%REQ%"
del /q "%REQ%"
if not defined SLUG exit /b 3
if not exist "%~dp0..\episodes\%SLUG%\index.html" exit /b 4
REM 2 workers: the owner's pick (dojo-ops devq round 3, 18 Oct 2026); render.cmd's own draft default is 3.
set RENDER_WORKERS=2
call "%~dp0render.cmd" %SLUG% draft
exit /b %ERRORLEVEL%

:refuse
del /q "%REQ%"
exit /b 3
