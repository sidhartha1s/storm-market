@echo off
REM Draft render wrapper (hidden schtasks path) for ep-palm-sunday-1965, full-episode draft v1.
REM The 12 Oct 26 override for the hook-and-intro preview (free-memory floor 0, 1 worker, below-normal priority)
REM was for that run only and is gone: this run keeps the preflight's own floor.
REM 2 workers: this laptop's planning number for long renders (CLAUDE.md "the render is the LAST step").
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-palm-sunday-1965 draft ep-palm-sunday-1965-draft-v1
