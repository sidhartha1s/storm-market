@echo off
REM Full render wrapper for ep-palm-sunday-1965 on the ZBook (hidden schtasks path in the owner's logged-on session).
REM 3 workers: the draft at 4 workers left 2.0 GB free at its low point there, and 30 fps workers use more memory than draft.
set RENDER_WORKERS=3
call "%~dp0render.cmd" ep-palm-sunday-1965 full ep-palm-sunday-1965-final
