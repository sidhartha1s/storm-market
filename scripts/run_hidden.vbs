' run_hidden.vbs <command> [args...] — run a command with NO visible window.
' Why: schtasks interactive tasks pop a cmd window on the desktop (owner 2026-08-21:
' never spawn visible windows). Window style 0 = hidden, no flash.
Dim args, i, cmd
If WScript.Arguments.Count = 0 Then WScript.Quit 2
cmd = ""
For i = 0 To WScript.Arguments.Count - 1
    If InStr(WScript.Arguments(i), " ") > 0 Then
        cmd = cmd & """" & WScript.Arguments(i) & """ "
    Else
        cmd = cmd & WScript.Arguments(i) & " "
    End If
Next
CreateObject("WScript.Shell").Run cmd, 0, False
