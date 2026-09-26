@echo off
REM One-off preview of the WebGL tornado template demo (owner ask 26 Sep 26). 30 fps, 1 worker.
set RENDER_WORKERS=1
set RENDER_FPS=30
set RENDER_CRF=18
call "%~dp0render.cmd" demo-webgl-tornado draft tornado-preview
