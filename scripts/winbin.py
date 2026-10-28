"""Find a real program on PATH, skipping the Microsoft Store stubs in WindowsApps.

A hidden launch (schtasks, run_hidden.vbs) can put %LOCALAPPDATA%\\Microsoft\\WindowsApps ahead of the real tools.
There `bash` is WSL's launcher (rc 127 on a Windows path) and `python3` is the Store stub (exit 9009). On
29 Oct 26 both failed the PR 239 e2e as if the code were broken. render.cmd names the same trap.
"""
import os
import shutil


def real(name, path=None):
    """Full path of the first `name` on PATH (or `path`) outside WindowsApps; SystemExit naming WindowsApps if none."""
    for d in (os.environ.get("PATH", "") if path is None else path).split(os.pathsep):
        hit = d and "windowsapps" not in d.lower() and shutil.which(name, path=d)
        if hit:
            return hit
    raise SystemExit(f"{name}: no copy on PATH outside WindowsApps (the Microsoft Store stub); "
                     "put the real install folder ahead of it")
