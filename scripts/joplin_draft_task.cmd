@echo off
REM Draft render wrapper (hidden schtasks path) for ep-joplin-2011. Workers 2: 16 GB box, stay clear of OOM.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-joplin-2011 draft ep-joplin-2011-draft-v1
