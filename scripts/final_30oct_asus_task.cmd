@echo off
REM Final renders of batch A on the ASUS, 30 Oct 26 (owner 16:43: "asus is good to start. check ram and start render here").
REM Per episode, in order: run_gates (Paul's-voice layer included), render_acts full, verify_render, master_deliverables.
REM 2 workers by owner order (16:53: "2 fucking workers") with 67 GB free on C:, under the 100 GB stream_gate floor:
REM STREAM_GATE_OVERRIDE carries his order past the pre-launch refusal only. The gate watcher still stops a render whose
REM gate line says enabled:false, and render by act caps any disk capture to one act at a time.
set RENDER_WORKERS=2
set STREAM_GATE_OVERRIDE=owner 30 Oct 26 16:53, ASUS, 67 GB free
set S=C:\Users\Sidhartha\Automation Projects\storm-market
set PY=C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe
set PATH=C:\Program Files\Git\bin;%PATH%
set LOG=%TEMP%\final-30oct-asus.log
echo ===== final batch start %date% %time% >> "%LOG%"
for %%e in (ep-buffalo-2022 ep-galveston-1900 ep-appalachian-1950) do call :one %%e
echo ===== final batch end %date% %time% >> "%LOG%"
exit /b 0

:one
set W=%S%\.worktrees\%1
set B=%1-final-1030
echo == %1 gates start %date% %time% >> "%LOG%"
"%PY%" "%W%\scripts\run_gates.py" "%W%\episodes\%1" >> "%LOG%" 2>&1
if errorlevel 1 (
  echo == %1 GATES FAIL %date% %time% >> "%LOG%"
  exit /b 0
)
echo == %1 render start %date% %time% >> "%LOG%"
start "" /b /wait /belownormal cmd /c ""%PY%" "%W%\scripts\render_acts.py" %1 full %B%" >> "%LOG%" 2>&1
if not exist "%W%\episodes\%1\renders\%B%.mp4" (
  echo == %1 RENDER FAIL no %B%.mp4 %date% %time% >> "%LOG%"
  exit /b 0
)
echo == %1 verify start %date% %time% >> "%LOG%"
bash "%W%\scripts\verify_render.sh" "%W%\episodes\%1" %B% full >> "%LOG%" 2>&1
if errorlevel 1 (
  echo == %1 VERIFY FAIL %date% %time% >> "%LOG%"
  exit /b 0
)
echo == %1 master start %date% %time% >> "%LOG%"
"%PY%" "%W%\scripts\master_deliverables.py" "%W%\episodes\%1" %B% >> "%LOG%" 2>&1
if errorlevel 1 (
  echo == %1 MASTER FAIL %date% %time% >> "%LOG%"
  exit /b 0
)
echo == %1 DONE %date% %time% >> "%LOG%"
exit /b 0
