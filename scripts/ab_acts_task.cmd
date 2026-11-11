@echo off
REM A/B part B: the same Appalachian index.html rendered by act (render_acts.py), 2 workers, on the ZBook, right after
REM the whole-render pass. Full Python path: on the ZBook a bare python3 inside a hidden cmd hits the Store stub.
set RENDER_WORKERS=2
set W=C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep-appalachian-1950
set LOG=%W%\episodes\ep-appalachian-1950\renders\ab-1029.log
echo acts start %date% %time% >> "%LOG%"
start "" /b /wait /belownormal cmd /c ""C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" "%W%\scripts\render_acts.py" ep-appalachian-1950 draft ab-acts-1029" >> "%LOG%" 2>&1
echo acts end %date% %time% >> "%LOG%"
