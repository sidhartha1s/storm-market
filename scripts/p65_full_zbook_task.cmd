@echo off
REM Full render wrapper for ep-palm-sunday-1965 on the ZBook (hidden schtasks path in the owner's logged-on session).
REM Owner 13 Oct 26: "just core max that": 4 workers, as in the draft wrapper. Free memory at launch 14 Oct 26: 7.49 GB
REM (the draft at 4 workers started at 4.85 GB and bottomed at 2.0 GB). If a full render dies for memory, drop to 3.
set RENDER_WORKERS=4
call "%~dp0render.cmd" ep-palm-sunday-1965 full ep-palm-sunday-1965-final
