"""The one place that knows how to run PowerShell on a lane host (local or the zbook ssh alias).

Moved out of lanes.py unchanged so reap_chrome.py can reach the same hosts without importing lanes.py, which imports it.
"""
import base64
import subprocess


def ps(host, script, timeout=90):
    """(exit code, output) of a PowerShell script on host: the one place that knows how to reach a host."""
    argv = ["powershell", "-NoProfile", "-NonInteractive", "-EncodedCommand",
            base64.b64encode(script.encode("utf-16-le")).decode()]  # encoded, so no quoting has to survive ssh and cmd
    if host != "local":  # shortcut: the remote shell caps a line at 8191 chars (about a 2,500-char script)
        argv = ["ssh", "-n", "-o", "ConnectTimeout=15", host, " ".join(argv)]
    try:
        r = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           stdin=subprocess.DEVNULL, timeout=timeout)
    except subprocess.TimeoutExpired:
        return 124, f"timed out after {timeout}s"
    return r.returncode, r.stdout if r.returncode == 0 else r.stdout + r.stderr  # stderr carries CLIXML progress noise


def quote(s):
    return "'" + s.replace("'", "''") + "'"  # a PowerShell literal string
