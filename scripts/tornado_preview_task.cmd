@echo off
REM One-off preview of the WebGL tornado template demo (owner ask 26 Sep 26). 30 fps, 1 worker.
REM Owner go 26 Sep 26 ("go ahead with the render") while free RAM sat under the 4 GB floor:
REM the floor is lowered for this run only, and the override is written to disk.
set RENDER_WORKERS=1
set RENDER_FPS=30
set RENDER_CRF=18
set RENDER_MIN_FREE_GB=0
echo [OVERRIDE] owner go 26 Sep 26: 4 GB RAM floor skipped for this preview > "%~dp0..\episodes\demo-webgl-tornado\render_override.log"
call "%~dp0render.cmd" demo-webgl-tornado draft tornado-preview
