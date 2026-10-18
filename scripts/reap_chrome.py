#!/usr/bin/env python3
"""Reap orphan Playwright Chromes on a lane host: resume them, kill them, delete their temp profiles. Dry run unless --apply.

Why: on 18 Oct 26 the ZBook held 94 frozen orphan Playwright Chromes in session 0 (parent node dead, every thread
Suspended, 2.8 GB commit) and 285 %TEMP%\\playwright_chromiumdev_profile-* dirs (1.2 GB), left by gates whose node
was hard-killed mid-run. A suspended process ignores Stop-Process, so each one is resumed (NtResumeProcess) first.

What it touches, and nothing else:
  - chrome.exe in session 0 (where WMI-launched lanes run; the owner's own browsers live in his desktop session) whose
    command line holds playwright_chromiumdev_profile and whose parent is dead: no process has its parent's pid, or
    the one that has it started later (a reused pid). Plus every session-0 chrome.exe below such a root.
  - %TEMP% profile dirs named by a reaped Chrome, and ones no live Chrome names that are PROFILE_MIN_AGE_MIN old
    (a gate starting now has made its dir and not yet its Chrome).
Each pid is checked again right before the kill (still chrome.exe, same start time), so a pid reused meanwhile is spared.

  python3 scripts/reap_chrome.py [--host zbook] [--apply]
lanes.py runs it with --apply on a lane's host before every launch and after every `end`.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from host_ps import ps, quote  # noqa: E402

MARK = "playwright_chromiumdev_profile"
PROFILE = re.compile(MARK + r"-[A-Za-z0-9]+")
PROFILE_MIN_AGE_MIN = 30  # an unnamed profile younger than this may belong to a gate that is still launching
CHUNK = 25                # items per host call: an ssh command line caps near a 2,500-char script (host_ps.ps)

LIST = r"""$p = Get-CimInstance Win32_Process | ForEach-Object { [pscustomobject]@{ pid = $_.ProcessId; ppid = $_.ParentProcessId;
  session = $_.SessionId; name = $_.Name; created = $(if ($_.CreationDate) { $_.CreationDate.ToFileTimeUtc() } else { 0 });
  cmd = $(if ($_.Name -eq 'chrome.exe') { $_.CommandLine }) } }
$d = Get-ChildItem -LiteralPath $env:TEMP -Directory -Filter '""" + MARK + r"""-*' -ErrorAction SilentlyContinue |
  ForEach-Object { [pscustomobject]@{ name = $_.Name; created = $_.CreationTimeUtc.ToFileTimeUtc() } }
@{ procs = @($p); dirs = @($d); now = [DateTime]::UtcNow.ToFileTimeUtc() } | ConvertTo-Json -Depth 3 -Compress"""

KILL = r"""Add-Type -Namespace W -Name N -MemberDefinition '[DllImport("ntdll.dll")] public static extern int NtResumeProcess(IntPtr h);
[DllImport("kernel32.dll")] public static extern IntPtr OpenProcess(uint a, bool i, int p); [DllImport("kernel32.dll")] public static extern bool CloseHandle(IntPtr h);'
$alive = @{}; Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" | ForEach-Object { $alive[[int]$_.ProcessId] = $_.CreationDate.ToFileTimeUtc() }
$a = @(TARGETS); $n = 0; for ($k = 0; $k -lt $a.Count; $k += 2) { $id = [int]$a[$k]; if ($alive[$id] -ne $a[$k + 1]) { continue }
  $h = [W.N]::OpenProcess(0x0800, $false, $id); if ($h -ne [IntPtr]::Zero) { [void][W.N]::NtResumeProcess($h); [void][W.N]::CloseHandle($h) }
  Stop-Process -Id $id -Force -ErrorAction SilentlyContinue; $n++ }
$n"""

DELETE = r"""Start-Sleep -Seconds 1; $n = 0; foreach ($d in @(NAMES)) { $p = Join-Path $env:TEMP $d
  Remove-Item -LiteralPath $p -Recurse -Force -ErrorAction SilentlyContinue; if (-not (Test-Path -LiteralPath $p)) { $n++ } }
$n"""


def select(procs, dirs, now, min_age_min=PROFILE_MIN_AGE_MIN):
    """(chromes to kill as [(pid, created)], profile dir names to delete) from one host reading. Pure."""
    by_pid = {p["pid"]: p for p in procs}
    chrome = [p for p in procs if (p["name"] or "").lower() == "chrome.exe" and p["session"] == 0]

    def orphan(p):
        parent = by_pid.get(p["ppid"])
        return parent is None or parent["created"] > p["created"]

    kill = {p["pid"] for p in chrome if MARK in (p["cmd"] or "") and orphan(p)}
    grew = True
    while grew:  # the root's renderers and gpu process die with it
        below = {p["pid"] for p in chrome if p["ppid"] in kill and not orphan(p)} - kill
        kill |= below
        grew = bool(below)
    named = lambda ps_: {n.lower() for p in ps_ for n in PROFILE.findall(p["cmd"] or "")}
    reaped = named(p for p in chrome if p["pid"] in kill)
    live = named(p for p in procs if (p["name"] or "").lower() == "chrome.exe" and p["pid"] not in kill)
    old = lambda d: (now - d["created"]) / 1e7 >= min_age_min * 60  # FILETIME: 100 ns ticks
    gone = [d["name"] for d in dirs if d["name"].lower() not in live and (d["name"].lower() in reaped or old(d))]
    return sorted((p["pid"], p["created"]) for p in chrome if p["pid"] in kill), sorted(gone)


def reap(host, apply):
    """One line saying what was (or, without apply, would be) reaped on host. Raises RuntimeError if host cannot be read."""
    code, out = ps(host, LIST, timeout=60)
    try:
        reading = json.loads(out)
    except ValueError:
        raise RuntimeError(f"cannot read processes on {host} (exit {code}): {out.strip()[-200:]}")
    targets, dirs = select(reading["procs"], [d for d in reading["dirs"] if d], reading["now"])  # @($null) is one null
    if not apply:
        return f"[reap_chrome] {host}: would kill {len(targets)} orphan chrome, delete {len(dirs)} profiles (dry run; --apply does it)"
    killed = deleted = 0
    for i in range(0, len(targets), CHUNK):
        pairs = ", ".join(f"{pid}, {created}" for pid, created in targets[i:i + CHUNK])  # flat: pid, start time, ...
        code, out = ps(host, KILL.replace("TARGETS", pairs), timeout=60)
        killed += int(out.strip()) if code == 0 and out.strip().isdigit() else 0
    for i in range(0, len(dirs), CHUNK):
        code, out = ps(host, DELETE.replace("NAMES", ", ".join(quote(d) for d in dirs[i:i + CHUNK])), timeout=60)
        deleted += int(out.strip()) if code == 0 and out.strip().isdigit() else 0
    return f"[reap_chrome] {host}: killed {killed} of {len(targets)} orphan chrome, deleted {deleted} of {len(dirs)} profiles"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--host", default="local", choices=("local", "zbook"))
    ap.add_argument("--apply", action="store_true", help="kill and delete; without it, only report")
    a = ap.parse_args(argv)
    try:
        print(reap(a.host, a.apply))
    except RuntimeError as e:
        sys.exit(f"[reap_chrome] FAIL: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
