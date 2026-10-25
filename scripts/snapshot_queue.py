#!/usr/bin/env python3
"""One snapshot queue: builders write HTML and submit frame jobs; one worker renders them, one at a time.

Why: 22 Oct 26 three episodes' builders each ran `npx hyperframes snapshot` (a headless Chrome tree,
about 1.3 GB) on the 16 GB ASUS beside each other: 60 snapshots, 0 on the ZBook, a 55 min stall at
1.05 GB free (skeptic review finding 10). With one queue the browser count is one, whatever the builder
count, and the worker runs on the ZBook (CLAUDE.md "Heavy local jobs").

  submit episodes/<slug> --at <t1>,<t2>,... [--label <comp id>]   no browser; prints the job id and PNG dir
  run [--host zbook]       the worker: drains the queue oldest first, one job at a time, then exits
  status                   pending / done counts and the last results

The spool is `.snapq/` in the MAIN checkout, so every worktree on this laptop feeds the same queue. PNGs land in
`<episode>/.qc-tmp/snapq/<job>/`; `.snapq/done/<job>.json` holds the exit code and the PNG list.
With --host zbook the worker copies the files the timeline references (changed ones only) to
`.snapq/mirror/<slug>/` in the ZBook's main checkout, snapshots there and copies the PNGs back.
"""
import argparse
import json
import msvcrt
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from render_preflight import parse_pin  # noqa: E402

ZBOOK_REPO = r"C:\Users\Sidhartha\Automation Projects\storm-market"
SNAP_TIMEOUT = 600   # a 3-frame snapshot takes about a minute; ten times that is a hung Chrome
ZBOOK_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Smart App Control blocks hyperframes' own shell (learnings/render.md 10 Oct 26, item 3)
REF = re.compile(r"""(?:src|href)="([^"#?]+)"|url\(['"]?([^'")#?]+)""")


def main_checkout(repo):
    """A worktree's .git is a file naming .git/worktrees/<name>; the main checkout is three levels up from there."""
    git = repo / ".git"
    if git.is_file():
        return Path(git.read_text(encoding="utf-8").split("gitdir:")[1].strip()).parents[2]
    return repo


SPOOL = main_checkout(SCRIPTS.parent) / ".snapq"


def submit(ep, at, label):
    ep = Path(ep).resolve()
    if not (ep / "index.html").is_file():
        sys.exit(f"[snapq] FAIL: no index.html in {ep}")
    times = [float(t) for t in at.split(",")]
    job = f"{time.time_ns()}" + (f"-{label}" if label else "")   # 19 digits until 2286, so names sort oldest first
    (SPOOL / "pending").mkdir(parents=True, exist_ok=True)
    out = ep / ".qc-tmp" / "snapq" / job
    tmp = SPOOL / "pending" / f"{job}.json.tmp"   # the worker globs *.json, so it never reads a half-written job
    tmp.write_text(json.dumps({"ep": str(ep), "at": times, "out": str(out)}), encoding="utf-8")
    os.replace(tmp, tmp.with_suffix(""))
    print(f"[snapq] queued {job}: {len(times)} frame(s) -> {out}")
    print(f"[snapq] result: {SPOOL / 'done' / (job + '.json')}")


def referenced(ep):
    """index.html, everything under compositions/, and every file those pages name that exists in the episode."""
    ep = ep.resolve()
    pages = [ep / "index.html", *sorted((ep / "compositions").glob("**/*"))] if (ep / "compositions").is_dir() else [ep / "index.html"]
    files = {p for p in pages if p.is_file()}
    for page in [p for p in files if p.suffix in (".html", ".css", ".js")]:
        for a, b in REF.findall(page.read_text(encoding="utf-8", errors="replace")):
            ref = (a or b).strip()
            if "://" in ref or ref.startswith(("data:", "/")):
                continue
            for base in (page.parent, ep):   # comps use ../media/x or media/x (<base href="../">)
                f = (base / ref).resolve()
                if f.is_file() and ep in f.parents:
                    files.add(f)
    return sorted(files)


def ssh(cmd, timeout):
    return subprocess.run(["ssh", "-n", "zbook", cmd], capture_output=True, text=True, timeout=timeout)


def ship(ep):
    """Copy the referenced files that changed since the last ship (size + mtime) to the ZBook mirror."""
    ep = ep.resolve()
    seen_p = SPOOL / "shipped" / f"{ep.name}.json"
    seen = json.loads(seen_p.read_text(encoding="utf-8")) if seen_p.exists() else {}
    now = {f.relative_to(ep).as_posix(): [f.stat().st_size, f.stat().st_mtime_ns] for f in referenced(ep)}
    todo = [r for r, v in now.items() if seen.get(r) != v]
    if todo:
        with tempfile.TemporaryDirectory() as d:
            tar = Path(d) / f"{ep.name}.tar"
            with tarfile.open(tar, "w") as t:
                for r in todo:
                    t.add(ep / r, arcname=r)
            mirror = rf"{ZBOOK_REPO}\.snapq\mirror\{ep.name}"
            r = ssh(f'mkdir "{mirror}" 2>nul & exit 0', 60)
            if r.returncode:
                raise RuntimeError(f"ssh mkdir: {r.stderr.strip()}")
            subprocess.run(["scp", "-q", str(tar), f"zbook:{mirror}\\ship.tar".replace("\\", "/")], check=True, timeout=1800)
            r = ssh(f'tar -xf "{mirror}\\ship.tar" -C "{mirror}" && del "{mirror}\\ship.tar"', 600)
            if r.returncode:
                raise RuntimeError(f"ssh untar: {r.stderr.strip()}")
    seen_p.parent.mkdir(parents=True, exist_ok=True)
    seen_p.write_text(json.dumps(now), encoding="utf-8")
    return len(todo), len(now)


def snap_local(job, pin):
    gate = subprocess.run([sys.executable, str(SCRIPTS / "render_busy.py")])
    if gate.returncode:
        return gate.returncode, "render_busy refused"
    cmd = [shutil.which("npx") or "npx", "--yes", f"hyperframes@{pin}", "snapshot", job["ep"], "--at", ",".join(map(str, job["at"])),
           "--no-end", "--describe", "false", "-o", job["out"]]
    with tempfile.TemporaryFile("w+", encoding="utf-8", errors="replace") as log:   # a file, not a pipe: an orphan Chrome holding a pipe hangs the worker
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            rc = p.wait(timeout=SNAP_TIMEOUT)
        except subprocess.TimeoutExpired:
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True)   # the whole tree: npx, node, Chrome
            p.wait()
            rc = 1
            log.write(f" | killed after {SNAP_TIMEOUT} s")
        log.seek(0)
        return rc, log.read()[-400:]


KILL_REMOTE = ("powershell -NoProfile -Command \"Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and "
               "$_.CommandLine -like '*.snapq\\mirror*' } | ForEach-Object { taskkill /T /F /PID $_.ProcessId }\"")


def kill_remote():
    """Stop the node tree of any snapshot still running from the ZBook mirror (a timed-out job), so jobs never overlap."""
    ssh(KILL_REMOTE, 120)


def snap_zbook(job, pin, name):
    ep = Path(job["ep"])
    sent, total = ship(ep)
    mirror = rf"{ZBOOK_REPO}\.snapq\mirror\{ep.name}"
    rout = rf"{ZBOOK_REPO}\.snapq\out\{name}"
    # `python`, not `python3`: on the ZBook python3 is the WindowsApps redirector that hung TTS jobs (22 Oct 26); python is Python312
    try:
        r = ssh(f'python "{ZBOOK_REPO}\\scripts\\render_busy.py" && set "HYPERFRAMES_BROWSER_PATH={ZBOOK_CHROME}" && '
                f'npx --yes hyperframes@{pin} snapshot "{mirror}" --at {",".join(map(str, job["at"]))} --no-end --describe false -o "{rout}"',
                SNAP_TIMEOUT)
    except subprocess.TimeoutExpired:
        kill_remote()
        return 1, f"shipped {sent} of {total} files; killed after {SNAP_TIMEOUT} s"
    log = f"shipped {sent} of {total} files; " + (r.stdout + r.stderr)[-400:]
    if r.returncode:
        return r.returncode, log
    Path(job["out"]).mkdir(parents=True, exist_ok=True)
    g = subprocess.run(["scp", "-q", "-r", f"zbook:{rout}/*".replace("\\", "/"), job["out"]], capture_output=True, text=True, timeout=600)
    return g.returncode, log + g.stderr[-200:]


def run(host):
    (SPOOL / "done").mkdir(parents=True, exist_ok=True)
    lock = open(SPOOL / "worker.lock", "a")
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)   # released by the OS when this process ends
    except OSError:
        sys.exit("[snapq] a worker is already running; the job waits in its queue")
    pin = parse_pin(SCRIPTS.parent)
    if not pin:
        sys.exit("[snapq] FAIL: config.yaml has no hyperframes_version")
    if host == "zbook":
        try:
            kill_remote()   # a worker that died mid-job leaves its Chrome behind
        except subprocess.TimeoutExpired:
            print("[snapq] ZBook did not answer the cleanup call in 120 s; jobs will report their own ssh errors")
    while jobs := sorted((SPOOL / "pending").glob("*.json")):
        p = jobs[0]
        job, t0, pngs = {}, time.time(), []
        try:   # any failure is this job's rc 1 in done/, never a dead worker with the bad job still first in line
            job = json.loads(p.read_text(encoding="utf-8"))
            rc, log = snap_zbook(job, pin, p.stem) if host == "zbook" else snap_local(job, pin)
            pngs = sorted(str(f) for f in Path(job["out"]).glob("*.png")) if rc == 0 else []
        except Exception as e:
            rc, log = 1, f"{type(e).__name__}: {e}"
        if rc == 0 and not pngs:
            rc, log = 1, log + " | exit 0 but no PNG written"
        (SPOOL / "done" / p.name).write_text(json.dumps({**job, "host": host, "rc": rc, "secs": round(time.time() - t0, 1),
                                                          "pngs": pngs, "log": log}, indent=1), encoding="utf-8")
        p.unlink()
        print(f"[snapq] {p.stem}: rc {rc}, {len(pngs)} PNG(s), {time.time() - t0:.0f} s on {host}")
    print("[snapq] queue empty")


def status():
    pend = sorted((SPOOL / "pending").glob("*.json"))
    done = sorted((SPOOL / "done").glob("*.json"))
    print(f"[snapq] {len(pend)} pending, {len(done)} done ({SPOOL})")
    for d in done[-5:]:
        j = json.loads(d.read_text(encoding="utf-8"))
        print(f"  {d.stem}: rc {j['rc']}, {len(j['pngs'])} PNG(s), {j['secs']} s on {j['host']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("submit")
    s.add_argument("ep")
    s.add_argument("--at", required=True)
    s.add_argument("--label", default="")
    sub.add_parser("run").add_argument("--host", choices=["local", "zbook"], default="zbook")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "submit":
        submit(a.ep, a.at, re.sub(r"[^\w-]", "", a.label))
    elif a.cmd == "run":
        run(a.host)
    else:
        status()
