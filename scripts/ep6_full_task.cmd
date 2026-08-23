@echo off
REM ep6 FULL render wrapper for the hidden schtasks path (wscript run_hidden.vbs cmd /c <this>).
REM Owner decision 2026-08-23: render on pin 0.7.109 although npm latest is 0.8.10 —
REM 0.8.x opens a visible Windows Terminal tab per ffprobe/ffmpeg spawn on this box
REM (LEARNINGS). RENDER_PIN_STALE_OK=1 is the explicit, logged override for THIS run.
set RENDER_PIN_STALE_OK=1
REM 2 workers: box had ~2.5 GB free at launch (other sessions + browsers resident).
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep6-katrina-2005 full
