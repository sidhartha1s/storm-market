@echo off
REM dojo_draft.cmd: the only way the dojo-ops dashboard starts a Storm render (a draft, 2 workers).
REM dojo-ops reporter/render.py (sidhartha1s/dojo-ops PR #41, design B) writes the episode slug to
REM %LOCALAPPDATA%\dojo-ops\render-request.txt and starts this file with no arguments, so no dashboard
REM text is ever on a command line. The slug was checked there against this laptop's own Storm episode
REM list; it is data from outside, so it is checked again here before render.cmd sees it.
REM Exit codes: 2 no request, 3 request refused, 4 no such episode, else render.cmd's own.
REM Every check fails closed: a step that errors goes to :refuse, never on (Opus review, 18 Oct 2026).
setlocal EnableExtensions DisableDelayedExpansion
set "REQ=%LOCALAPPDATA%\dojo-ops\render-request.txt"
if not exist "%REQ%" exit /b 2
REM find and findstr by full path: with Git on PATH, a bare find or findstr can resolve to the GNU tools
REM (a bare find hung the test, 18 Oct 2026).
set "FIND=%SystemRoot%\System32\find.exe"
set "FINDSTR=%SystemRoot%\System32\findstr.exe"
REM Check and read one copy, so the bytes checked are the bytes used. The copy ends in CRLF: findstr /x
REM never matches a last line with no line end, and dojo-ops writes the slug without one.
set "CHK=%REQ%.chk"
>"%CHK%" type "%REQ%" || goto :refuse
>>"%CHK%" echo( || goto :refuse
del /q "%REQ%"
REM Exactly one line, and it is 1+ of A-Z a-z 0-9 _ - (letters spelled out: findstr's [A-Z] also
REM matches accented letters).
set "LINES="
for /f %%n in ('""%FIND%" /c /v "" < "%CHK%""') do set "LINES=%%n"
if not "%LINES%"=="1" goto :refuse
"%FINDSTR%" /r /x /c:"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-][ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-]*" "%CHK%" >nul || goto :refuse
set "SLUG="
set /p SLUG=<"%CHK%"
del /q "%CHK%"
if not defined SLUG exit /b 3
if not exist "%~dp0..\episodes\%SLUG%\index.html" exit /b 4
REM 2 workers: the owner's pick (dojo-ops devq round 3, 18 Oct 2026); render.cmd's own draft default is 3.
set RENDER_WORKERS=2
call "%~dp0render.cmd" %SLUG% draft
exit /b %ERRORLEVEL%

:refuse
REM A directory squatting on either name is left alone: del on a directory would empty it.
if exist "%REQ%" if not exist "%REQ%\" del /q "%REQ%"
if exist "%CHK%" if not exist "%CHK%\" del /q "%CHK%"
exit /b 3
