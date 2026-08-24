@echo off
set PYTHONUNBUFFERED=1
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep6-katrina"
"C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" scripts\tts_episode.py episodes\ep6-katrina-2005 > episodes\ep6-katrina-2005\tts_run.log 2>&1
echo %ERRORLEVEL% > episodes\ep6-katrina-2005\tts_done.marker
