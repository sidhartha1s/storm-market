@echo off
REM ep-1974 FULL render wrapper (hidden schtasks path). Workers 2: 16 GB box, 2 GB free at draft time.
REM RENDER_PIN_STALE_OK is the owner-logged override for a stale pin on a full render (LEARNINGS, ep6).
set RENDER_PIN_STALE_OK=1
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-1974-super-outbreak full
