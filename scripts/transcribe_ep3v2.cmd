@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2"
set HF_HUB_OFFLINE=1
set PYTHONUTF8=1
"C:\Users\Sidhartha\Automation Projects\JP-market\.venv\Scripts\python.exe" scripts\transcribe_episode.py episodes\ep3-tristate >> episodes\ep3-tristate\audio\transcribe_v2.log 2>&1
if %ERRORLEVEL%==0 echo done > episodes\ep3-tristate\audio\tts_v2.done.marker
echo %ERRORLEVEL% > episodes\ep3-tristate\audio\transcribe_v2_exit.marker
