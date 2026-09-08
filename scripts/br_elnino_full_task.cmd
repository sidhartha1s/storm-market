@echo off
REM br-elnino-california FULL render wrapper (hidden schtasks/wscript path), ep6_full_task.cmd pattern.
REM Owner order 2026-09-08 ("ship final"): render on pin 0.7.109 while npm latest is newer -
REM RENDER_PIN_STALE_OK=1 is the explicit, logged override for THIS run.
set RENDER_PIN_STALE_OK=1
REM 2 workers: box carries the Texas TTS + a sourcing agent alongside this render.
set RENDER_WORKERS=2
call "%~dp0render.cmd" br-elnino-california full br-elnino-california-final
