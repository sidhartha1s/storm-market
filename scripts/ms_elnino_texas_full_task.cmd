@echo off
REM ms-elnino-texas FULL render wrapper (hidden schtasks/wscript path). Owner order 2026-09-09 "ship texas":
REM render on pin 0.7.109 although npm latest is newer (0.8.x opens visible terminal tabs on this box, LEARNINGS).
REM RENDER_PIN_STALE_OK=1 is the explicit, logged override for THIS run.
set RENDER_PIN_STALE_OK=1
set RENDER_WORKERS=2
call "%~dp0render.cmd" ms-elnino-texas full
