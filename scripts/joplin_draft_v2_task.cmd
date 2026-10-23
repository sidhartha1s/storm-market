@echo off
REM Draft v2 (ASUS): fixes after draft-v1 review (empty openings, cellar push, score bed + swells). Workers 2.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-joplin-2011 draft ep-joplin-2011-draft-v2
