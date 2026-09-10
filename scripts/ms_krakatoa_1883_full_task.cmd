@echo off
REM ms-krakatoa-1883 FULL render wrapper (hidden wscript path). Owner go 2026-09-10 13:2x.
REM Pin 0.7.109 stays (0.8.x opens visible terminal tabs on this box, LEARNINGS); RENDER_PIN_STALE_OK=1 is the owner's logged override for THIS run.
set RENDER_PIN_STALE_OK=1
set RENDER_WORKERS=2
call "%~dp0render.cmd" ms-krakatoa-1883 full
