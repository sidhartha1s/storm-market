@echo off
REM stage_cost_task.cmd: start the stage measurement hidden, in the logged-in session (GPU visible), as a one-shot task
REM that is deleted in the same command (repo CLAUDE.md "the render is the LAST step": create && run /i && delete).
REM Usage: scripts\stage_cost_task.cmd <slug> <out-json-relative>
setlocal
set R=%~dp0..
schtasks /create /tn storm-stage-cost /tr "wscript.exe \"%R%\scripts\run_hidden.vbs\" cmd.exe /c \"%R%\scripts\stage_cost.cmd\" %~1 %~2" /sc once /st 23:59 /f && schtasks /run /i /tn storm-stage-cost && schtasks /delete /tn storm-stage-cost /f
