@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2"
:loop
python3 scripts\tts_episode.py episodes\ep3-tristate >> episodes\ep3-tristate\audio\tts_v2.log 2>&1
if errorlevel 1 goto loop
"C:\Users\Sidhartha\Automation Projects\JP-market\.venv\Scripts\python.exe" scripts\transcribe_episode.py episodes\ep3-tristate >> episodes\ep3-tristate\audio\tts_v2.log 2>&1
if errorlevel 1 goto loop
echo done > episodes\ep3-tristate\audio\tts_v2.done.marker
