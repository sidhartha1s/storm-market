@echo off
REM Draft render wrapper for ep-palm-sunday-1965 on the ZBook (14 cores, hidden schtasks path in the owner's logged-on session).
REM Owner 13 Oct 26: "render on zbook." and "just core max that": 4 workers there (first use; this laptop's wrapper keeps 2).
set RENDER_WORKERS=4
call "%~dp0render.cmd" ep-palm-sunday-1965 draft ep-palm-sunday-1965-draft-v2
