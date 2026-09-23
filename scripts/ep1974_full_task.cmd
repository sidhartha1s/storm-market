@echo off
REM ep-1974 FULL render wrapper (hidden schtasks path). Workers 2: 16 GB box, 2 GB free at draft time.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-1974-super-outbreak full
