#!/usr/bin/env python3
"""One snapshot queue: builders write HTML and submit frame jobs; one worker renders them, one at a time.

Why: 22 Oct 26 three episodes' builders each ran `npx hyperframes snapshot` (a headless Chrome tree,
about 1.3 GB) on the 16 GB ASUS beside each other: 60 snapshots, 0 on the ZBook, a 55 min stall at
1.05 GB free (skeptic review finding 10). With one queue the browser count is one, whatever the builder
count, and the worker runs on the ZBook (CLAUDE.md "Heavy local jobs").

  submit episodes/<slug> --at <t1>,<t2>,... [--label <comp id>]   no browser; prints the job id and PNG dir
  run [--host zbook]       the worker: drains the queue oldest first, one snapshot run at a time, then exits
  status                   pending / done counts and the last results

The spool is `.snapq/` in the MAIN checkout, so every worktree on this laptop feeds the same queue. PNGs land in
`<episode>/.qc-tmp/snapq/<job>/`; `.snapq/done/<job>.json` holds the exit code and the PNG list.
Batching: one snapshot run costs about 44 s before its first frame (node, bundling the whole episode with fonts, Chrome
launch, page settle) and about 2 s per frame after (measured on the ZBook 26 Oct 26). So each run takes the oldest job
and every other pending job for the same episode folder, captures the union of their times in one browser, and hands
each job its own frames. The union is sorted, so every frame is still reached by forward seeks from a fresh page.
A job whose times go backwards or repeat (the seek-order check: forward, then seek 0, past it, back) runs alone, in its
own order, on a fresh page.
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
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)   # each ssh/scp from a console-less parent otherwise opens a window on the owner's screen
import sys
import tarfile
import tempfile
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from render_preflight import parse_pin  # noqa: E402

ZBOOK_REPO = r"C:\Users\Sidhartha\Automation Projects\storm-market"
SNAP_TIMEOUT = 600   # fixed part: a run reaches its first frame in about 44 s; ten times that is a hung Chrome
FRAME_TIMEOUT = 20   # added per frame: a frame takes about 2 s
SETTLE = 3           # seconds a run waits before picking its batch, so a burst of submits shares one run
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
    return subprocess.run(["ssh", "-n", "zbook", cmd], capture_output=True, text=True, timeout=timeout, creationflags=NO_WINDOW)


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
            subprocess.run(["scp", "-q", str(tar), f"zbook:{mirror}\\ship.tar".replace("\\", "/")], check=True, timeout=1800, creationflags=NO_WINDOW)
            r = ssh(f'tar -xf "{mirror}\\ship.tar" -C "{mirror}" && del "{mirror}\\ship.tar"', 600)
            if r.returncode:
                raise RuntimeError(f"ssh untar: {r.stderr.strip()}")
    seen_p.parent.mkdir(parents=True, exist_ok=True)
    seen_p.write_text(json.dumps(now), encoding="utf-8")
    return len(todo), len(now)


def limit(times):
    return SNAP_TIMEOUT + FRAME_TIMEOUT * len(times)


def snap_local(ep, times, pin, name, out):
    gate = subprocess.run([sys.executable, str(SCRIPTS / "render_busy.py")], creationflags=NO_WINDOW)
    if gate.returncode:
        return gate.returncode, "render_busy refused"
    cmd = [shutil.which("npx") or "npx", "--yes", f"hyperframes@{pin}", "snapshot", str(ep), "--at", ",".join(map(str, times)),
           "--no-end", "--describe", "false", "-o", str(out)]
    with tempfile.TemporaryFile("w+", encoding="utf-8", errors="replace") as log:   # a file, not a pipe: an orphan Chrome holding a pipe hangs the worker
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            rc = p.wait(timeout=limit(times))
        except subprocess.TimeoutExpired:
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True, creationflags=NO_WINDOW)   # the whole tree: npx, node, Chrome
            p.wait()
            rc = 1
            log.write(f" | killed after {limit(times)} s")
        log.seek(0)
        return rc, log.read()[-400:]


KILL_REMOTE = ("powershell -NoProfile -Command \"Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and "
               "$_.CommandLine -like '*.snapq\\mirror*' } | ForEach-Object { taskkill /T /F /PID $_.ProcessId }\"")


def kill_remote():
    """Stop the node tree of any snapshot still running from the ZBook mirror (a timed-out job), so jobs never overlap."""
    ssh(KILL_REMOTE, 120)


POLL = 20            # seconds between status calls to the ZBook
POLL_FAILS = 15      # consecutive failed status calls before the run is given up (one ssh reset must not kill a healthy run)


def run_detached(name, body, deadline):
    """Run a cmd script on the ZBook outside the ssh session (CIM spawn), then poll for its exit code with short fresh ssh calls.
    One ssh held open for 6+ min was reset by the ZBook (`Connection reset by peer`, 26 Oct 26) and took the whole 180-frame batch with it."""
    base = rf"{ZBOOK_REPO}\.snapq\out"
    cmd_f, rc_f, log_f = (rf"{base}\{name}.{x}" for x in ("cmd", "rc", "log"))
    with tempfile.TemporaryDirectory() as d:
        local = Path(d) / f"{name}.cmd"
        local.write_text(f'@echo off\r\n({body}) > "{log_f}" 2>&1\r\necho %errorlevel% > "{rc_f}.tmp" & move /y "{rc_f}.tmp" "{rc_f}" >nul\r\n', encoding="ascii")
        r = ssh(f'mkdir "{base}" 2>nul & del "{rc_f}" 2>nul & exit 0', 60)
        if r.returncode:
            raise RuntimeError(f"ssh mkdir: {r.stderr.strip()}")
        subprocess.run(["scp", "-q", str(local), f"zbook:{cmd_f}".replace("\\", "/")], check=True, timeout=300, creationflags=NO_WINDOW)
    start = ("powershell -NoProfile -Command \"(Invoke-CimMethod -ClassName Win32_Process -MethodName Create "
             f"-Arguments @{{CommandLine='cmd.exe /c {name}.cmd'; CurrentDirectory='{base}'}}).ReturnValue\"")   # relative name: the repo path has a space
    r = ssh(start, 120)
    if r.stdout.strip() != "0":
        raise RuntimeError(f"ZBook start failed: {(r.stdout + r.stderr).strip()[-200:]}")
    t0, fails = time.time(), 0
    while time.time() - t0 < deadline:
        time.sleep(POLL)
        try:
            r = ssh(f'if exist "{rc_f}" (type "{rc_f}") else (echo RUNNING)', 120)
            fails = 0 if r.returncode == 0 else fails + 1
        except subprocess.TimeoutExpired:
            fails += 1
            continue
        if fails >= POLL_FAILS:
            raise RuntimeError(f"ZBook status call failed {fails} times in a row: {r.stderr.strip()[-200:]}")
        if r.returncode == 0 and r.stdout.strip() != "RUNNING":
            tail = ssh(f'powershell -NoProfile -Command "Get-Content -Tail 12 \'{log_f}\'"', 120)
            return int(r.stdout.strip()), tail.stdout[-400:]
    raise subprocess.TimeoutExpired(name, deadline)


def snap_zbook(ep, times, pin, name, out):
    sent, total = ship(ep)
    mirror = rf"{ZBOOK_REPO}\.snapq\mirror\{ep.name}"
    rout = rf"{ZBOOK_REPO}\.snapq\out\{name}"
    # `python`, not `python3`: on the ZBook python3 is the WindowsApps redirector that hung TTS jobs (22 Oct 26); python is Python312
    body = (f'python "{ZBOOK_REPO}\\scripts\\render_busy.py" && set "HYPERFRAMES_BROWSER_PATH={ZBOOK_CHROME}" && '
            f'call npx --yes hyperframes@{pin} snapshot "{mirror}" --at {",".join(map(str, times))} --no-end --describe false -o "{rout}"')
    try:
        rc, tail = run_detached(name, body, limit(times))
    except (subprocess.TimeoutExpired, RuntimeError) as e:   # a lost status call or failed start can leave the batch running: stop it, and never rerun per job
        kill_remote()
        return 1, f"shipped {sent} of {total} files; killed after {limit(times)} s ({type(e).__name__}: {str(e)[:150]})"
    log = f"shipped {sent} of {total} files; " + tail
    if rc:
        return rc, log
    g = subprocess.run(["scp", "-q", "-r", f"zbook:{rout}/*".replace("\\", "/"), str(out)], capture_output=True, text=True, timeout=600, creationflags=NO_WINDOW)
    return g.returncode, log + g.stderr[-200:]


def load(p):
    job = json.loads(p.read_text(encoding="utf-8"))
    job["at"] = [float(t) for t in job["at"]]
    str(job["ep"]), str(job["out"])   # a job missing a key fails here, alone
    return job


def frames(stage):
    """hyperframes names frame i of an --at list `frame-<i, 2+ digits>-at-<t>s.png`."""
    return {int(f.name.split("-")[1]): f for f in Path(stage).glob("frame-*-at-*.png")}


def deliver(by_index, times, job):
    """Copy this job's frames out of the run, numbered as a run of its own would number them."""
    out = Path(job["out"])
    out.mkdir(parents=True, exist_ok=True)
    pngs = []
    for k, t in enumerate(job["at"]):
        src = by_index.get(k if job["at"] == times else times.index(t))   # a solo run keeps repeats in place
        if src:
            dst = out / f"frame-{k:02d}-at-{src.name.split('-at-', 1)[1]}"
            shutil.copy2(src, dst)
            pngs.append(str(dst))
    return pngs


def finish(p, job, host, rc, log, t0, pngs):
    (SPOOL / "done" / p.name).write_text(json.dumps({**job, "host": host, "rc": rc, "secs": round(time.time() - t0, 1),
                                                      "pngs": pngs, "log": log}, indent=1), encoding="utf-8")
    p.unlink()
    print(f"[snapq] {p.stem}: rc {rc}, {len(pngs)} PNG(s), {time.time() - t0:.0f} s on {host}")


def shoot(snap, ep, times, pin, name, batch, host, t0):
    """One snapshot run for every job in the batch. Records the jobs (unless a multi-job batch failed) and returns rc, log."""
    with tempfile.TemporaryDirectory() as stage:
        try:
            rc, log = snap(Path(ep), times, pin, name, stage)
        except Exception as e:
            rc, log = 1, f"{type(e).__name__}: {e}"
        log = f"batch of {len(batch)} job(s), {len(times)} frame(s); {log}"
        if rerun(rc, log, batch):
            return rc, log
        by_index = frames(stage) if rc == 0 else {}
        for p, j in batch.items():
            try:
                pngs = deliver(by_index, times, j)
                miss = rc == 0 and len(pngs) < len(j["at"])
                jrc, jlog = (1, log + f" | exit 0 but {len(pngs)} of {len(j['at'])} PNG(s) written") if miss else (rc, log)
            except Exception as e:   # a bad out path is this job's rc 1, never a dead worker with the job still first in line
                pngs, jrc, jlog = [], 1, log + f" | {type(e).__name__}: {e}"
            finish(p, j, host, jrc, jlog, t0, pngs)
    return rc, log


def rerun(rc, log, batch):
    """A multi-job batch that failed fast (one builder's bad time) reruns its jobs one at a time, so the rest still pass.
    A hung run is not rerun: 20 jobs would hold the worker for 20 more timeouts."""
    return rc and len(batch) > 1 and "killed after" not in log


def forward(job):
    return all(a < b for a, b in zip(job["at"], job["at"][1:]))


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
    snap = snap_zbook if host == "zbook" else snap_local
    while sorted((SPOOL / "pending").glob("*.json")):
        time.sleep(SETTLE)
        pending = sorted((SPOOL / "pending").glob("*.json"))
        jobs, t0 = {}, time.time()
        for p in pending:
            try:
                jobs[p] = load(p)
            except Exception as e:   # a half-written or corrupt job is its own rc 1, never a dead worker
                finish(p, {}, host, 1, f"{type(e).__name__}: {e}", t0, [])
        if not jobs:
            continue
        first, j0 = next(iter(jobs.items()))   # the oldest job picks the episode; the batch is every forward-only job for that folder
        batch = {p: j for p, j in jobs.items() if j["ep"] == j0["ep"] and forward(j)} if forward(j0) else {first: j0}
        ep = j0["ep"]
        times = sorted({t for j in batch.values() for t in j["at"]}) if forward(j0) else j0["at"]
        name = next(iter(batch)).stem + (f"-x{len(batch)}" if len(batch) > 1 else "")   # never the out dir a solo rerun reuses
        rc, log = shoot(snap, ep, times, pin, name, batch, host, t0)
        if rerun(rc, log, batch):
            print(f"[snapq] [FALLBACK] batch of {len(batch)} failed (rc {rc}); running its jobs one at a time. Batch log: {log[-600:]}")
            for p, j in batch.items():
                shoot(snap, ep, j["at"], pin, p.stem, {p: j}, host, time.time())
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
