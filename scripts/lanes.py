#!/usr/bin/env python3
"""Episode job ledger: which jobs are DONE, RUNNING, FAILED, BLOCKED, HELD, or READY to launch right now.

Why: the orchestrator ran episode jobs one after another and waited, while other jobs had every input on disk.
The Stop hook `~/.claude/hooks/lane-gate.py` runs `status --json` for every episode this session claimed and
refuses to end the turn while any job is READY, STALE or FAILED. HOLD (with a reason, lapsing after HOLD_H) is the only
way past it.

State comes from disk; `<ep>/lanes.json` (gitignored) adds only what disk cannot show: which session orchestrates,
which jobs were launched and when they ended, and which are held.

  python3 scripts/lanes.py claim  episodes/<slug>            # this Claude session orchestrates the episode
  python3 scripts/lanes.py start  episodes/<slug> verify:a4 brief:a4 [--host zbook] [--minutes 60]   # records lanes run elsewhere
  python3 scripts/lanes.py start  episodes/<slug> brief:a4 --host zbook --cmd "type b.md | {cli} -p --model opus" --log <path on zbook> --cwd <zbook checkout> [--profile claude2]
  python3 scripts/lanes.py end    episodes/<slug> verify:a4   # the lane stopped (its output may still need syncing back)
  python3 scripts/lanes.py hold   episodes/<slug> source:z1|all --reason "z1 media sits in the a6 folder"
  python3 scripts/lanes.py unhold episodes/<slug> source:z1
  python3 scripts/lanes.py status episodes/<slug> [--json]   # exit 2 while any job is READY, STALE or FAILED; read-only
  python3 scripts/lanes.py relaunch episodes/<slug>          # put every FAILED lane on the next profile that answers
  python3 scripts/lanes.py stop   episodes/<slug> all|<job>  # stop-all: end each RUNNING, STALE or FAILED lane's tree; ended only once stopped

Launching (why: lanes sat dead for hours on an exhausted profile or a full ZBook). `start --cmd` runs one job's command
itself, hidden and detached, on host local or zbook, with {cli} replaced by the profile (claudeN, the wrapper that sets
CLAUDE_CONFIG_DIR), started in --cwd (default: this checkout; required on zbook) and all output sent to --log.
It refuses a job already RUNNING or DONE, and an ssh drop during the launch is never a reason to launch again:
the host is asked whether the lane's process runs, and one that cannot be read is recorded as RUNNING. The three rules:
  1. it first probes the profile (`claude -p 'reply with the single word ok' --model haiku` under its
     CLAUDE_CONFIG_DIR); any reply but "ok" (a limit, a logged-out profile, an error) moves it to the next
     ~/.claude-accounts/claude* profile. It never waits for a reset.
  2. every start refuses while the host has MIN_FREE_GB or less free (a RAM floor, not a lane cap: lanes run on the API)
  3. a running lane whose log tail says it hit a limit is FAILED (blocking). `status` only reports it, since the Stop
     hook calls status; `relaunch` moves it to the next profile that answers, and backs off if another lanes.py
     holds the lock
Every command but status reads and writes the ledger only while holding <ep>/lanes.json.lock (created exclusively; a
write waits up to LOCK_WAIT_S for it; one older than LOCK_MIN minutes belongs to a dead holder and is taken over).

Groups: one per segment prefix (a1 = A1-S*), except H1, T1 and I1, which form `intro`. Jobs per group g:
  voice:g   every segment of g is locked (no open [verify] in its heading block) and has audio/<id>.wav, and
            audio/<id>.txt equals its script text (an edited line is not voiced until re-synthesised);
            BLOCKED once the locked ones are voiced and an open one remains
  words:g   ...and audio/<id>.words.json
  source:g  media/candidates/<g>/provenance.csv plus the sourcer's report (sourcer.md or candidates.md)
  verify:g  every provenance.csv row has a "verified" value, and no row has more fields than the header
  brief:g   briefs/<g>/_list.md (needs voice:g and words:g DONE)
  build:<comp>  compositions/<comp>.html, one per briefs/<g>/<comp>.md (needs voice:g and words:g DONE)
"""
import argparse
import base64
import csv
import json
import os
import re
import socket
import subprocess
import sys
import time

from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from tts_episode import open_verify_ids, parse_segments  # noqa: E402

INTRO = {"h1", "t1", "i1"}
HOLD_H = 3          # a hold lapses after this many hours, so a wait is re-decided, never forgotten
DEFAULT_MIN = 60    # a lane with no end recorded this many minutes after its start is presumed dead (STALE)
BLOCKING = ("READY", "STALE", "FAILED")
MACHINES = {"zbook": "SIDHARTHA", "asus": "SPTL-184"}  # each laptop's ssh alias -> its Windows hostname
HOSTS = ("local", *MACHINES)
MIN_FREE_GB = 4     # a lane never starts on a host with this much free memory or less
LIMIT = re.compile(r"hit your (\w+ )?limit|session limit|usage limit reached", re.I)
LOCK_MIN = 10      # a ledger lock older than this is a dead holder's
LOCK_WAIT_S = 120  # a ledger write waits this long for the lock before it gives up
NO_LOG = "[lanes: no log]"  # read_lane's answer for a log that does not exist; the launch redirect creates it at once
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)  # no console window for the stop hook's children
NO_LOG_MIN = 5     # a RUNNING lane with no log this many minutes after its start never ran (an unconfirmed launch)


def is_local(host):
    """True when host is this machine: "local", or this laptop's own alias (zbook, seen from the ZBook)."""
    return host == "local" or MACHINES.get(host, "").lower() == socket.gethostname().lower()


def ps(host, script, timeout=90):
    """(exit code, output) of a PowerShell script on host: the one place that knows how to reach a host."""
    argv = ["powershell", "-NoProfile", "-NonInteractive", "-EncodedCommand",
            base64.b64encode(script.encode("utf-16-le")).decode()]  # encoded, so no quoting has to survive ssh and cmd
    if not is_local(host):  # shortcut: the remote shell caps a line at 8191 chars (about a 2,500-char script)
        argv = ["ssh", "-n", "-o", "ConnectTimeout=15", host, " ".join(argv)]
    try:
        r = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           stdin=subprocess.DEVNULL, timeout=timeout, creationflags=NO_WINDOW)
    except subprocess.TimeoutExpired:
        return 124, f"timed out after {timeout}s"
    return r.returncode, r.stdout if r.returncode == 0 else r.stdout + r.stderr  # stderr carries CLIXML progress noise


def quote(s):
    return "'" + s.replace("'", "''") + "'"  # a PowerShell literal string


def probe(host, profile):
    """Rule 1: True only if the profile replies "ok"; a limit, a logged-out profile or an error is False.
    It runs the profile's wrapper by name, as the lane's {cli} does, so the probe tests the credential the lane uses."""
    code, out = ps(host, f"& {profile} -p 'reply with the single word ok' --model haiku",
                   timeout=30)  # a relaunch may probe several profiles in a row
    return code == 0 and out.strip().strip(".").lower() == "ok"


def profiles(host):
    """The profiles that can run on host: each %USERPROFILE%\\bin\\claude*.cmd wrapper with a credential, a token in
    ~/.claude-tokens (claude1-5, 7) or a login folder's .credentials.json (claude6, claudemax). The probe still decides."""
    code, out = ps(host, "Get-ChildItem \"$env:USERPROFILE\\bin\\claude*.cmd\" | ForEach-Object BaseName | Where-Object { "
                         "(Test-Path \"$env:USERPROFILE\\.claude-tokens\\$_\") -or "
                         "(Test-Path \"$env:USERPROFILE\\.claude-accounts\\$_\\.credentials.json\") }", timeout=30)
    if code:
        sys.exit(f"[lanes] FAIL: cannot list the claude profiles on {host}: {out.strip()[-200:]}")
    return sorted(out.split())


def free_gb(host):
    code, out = ps(host, "[math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1MB,1)")
    try:
        return float(out.strip())
    except ValueError:
        sys.exit(f"[lanes] FAIL: cannot read free memory on {host}: {out.strip()[-200:]}")


def root_filter(log):
    """PowerShell Where-Object body that selects only the cmd.exe root spawn() wrote for this log: its command line starts
    `cmd /s /c "(` and ends with the redirect. A shell, tail or agent command that only MENTIONS the log never matches
    (29 Oct 26: same bug class as render_busy's job scan). StartsWith/EndsWith, not -like: "[" in a path is a -like wildcard."""
    return ("$_.Name -eq 'cmd.exe' -and $_.CommandLine -and $_.CommandLine.StartsWith('cmd /s /c \"(') -and "
            f"$_.CommandLine.EndsWith({quote(redirect(log) + chr(34))})")


def alive(host, log):
    """True or False: the lane's root cmd.exe runs on host; None when the host cannot be read."""
    code, out = ps(host, f"@(Get-CimInstance Win32_Process | Where-Object {{ {root_filter(log)} }}).Count", timeout=20)
    return int(out.strip()) > 0 if code == 0 and out.strip().isdigit() else None


def redirect(log):
    """The output redirect spawn() writes into a lane's command line; kill() finds the lane by it."""
    return f'> "{log}" 2>&1'


def kill(host, log):
    """Count of lane trees ended on host (None: host unreadable). Only the cmd.exe root spawn() starts matches (the same
    root_filter alive() uses), so a viewer, a tail, a decoy cmd or a lane whose log path extends this one is never hit."""
    code, out = ps(host, f"$n = 0; Get-CimInstance Win32_Process | Where-Object {{ {root_filter(log)} }} | "
                         "ForEach-Object { taskkill /T /F /PID $_.ProcessId | Out-Null; $n++ }; $n", timeout=60)
    last = out.strip().splitlines()[-1] if out.strip() else ""
    return int(last) if code == 0 and last.isdigit() else None


def spawn(host, cmd, log, cwd):
    """Start cmd in cwd on host hidden, as a WMI process (it outlives this call and the ssh session), output to log.
    Exits only when the lane is known not to run: an ssh drop after a good launch started p4 twice (18 Oct 26)."""
    # shortcut: an unquoted ")" in cmd closes the ( ) group early; quote it ("Bash(rm:*)"), as every claude flag is
    line = f'cmd /s /c "({cmd}) {redirect(log)}"'
    code, out = ps(host, "$si = New-CimInstance -ClassName Win32_ProcessStartup -ClientOnly -Property @{ShowWindow=[uint16]0}; "
                         "(Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments "
                         f"@{{CommandLine={quote(line)}; CurrentDirectory={quote(cwd)}; ProcessStartupInformation=$si}}).ReturnValue")
    if code == 0 and out.strip() == "0":
        return
    # code 0: the host answered and refused it. Local has no ssh to drop, and its query would find this lanes.py, whose
    # own command line holds the log. Else ssh dropped mid-call and the Create may have run: ask the host
    # shortcut: a Create still in flight when the host answers reads as not running; a ~1 s window, rare enough here
    up = False if code == 0 or is_local(host) else alive(host, log)
    if up is False:
        sys.exit(f"[lanes] FAIL: launch on {host} failed: {out.strip()[-300:]}")
    if up is None:
        print(f"[lanes] WARN: ssh dropped while launching on {host} and the host cannot be read; recorded as RUNNING "
              f"so it is never launched twice; `status` calls it FAILED if its log never appears ({out.strip()[-120:]})")


def read_lane(host, log):
    """(running, last lines of its log): running is whether the lane's root cmd.exe still runs (alive()'s match), the
    lines NO_LOG when the log does not exist. None when the host cannot be read. One call, as status runs under the
    Stop hook's 120 s and an offline host costs one ssh ConnectTimeout per lane."""
    code, out = ps(host, f"@(Get-CimInstance Win32_Process | Where-Object {{ {root_filter(log)} }}).Count; $p = {quote(log)}; "
                         f"if (Test-Path -LiteralPath $p) {{ Get-Content -Tail 5 -LiteralPath $p }} else {{ '{NO_LOG}' }}",
                   timeout=20)
    n, _, tail = out.strip().partition("\n")
    return (int(n) > 0, tail.strip()) if code == 0 and n.strip().isdigit() else None


def profile_order(host, first=None, skip=None):
    """The profiles that can run on host, starting at first, without skip."""
    names = profiles(host)
    i = names.index(first) if first in names else 0
    return [n for n in names[i:] + names[:i] if n != skip]


def gate(host):
    """Rule 2: why a lane may not start on host now, or None."""
    gb = free_gb(host)
    return f"{host} has {gb} GB free (needs more than {MIN_FREE_GB})" if gb <= MIN_FREE_GB else None


def take_lock(lock, now):
    """True once this process holds lock, created exclusively; a lock older than LOCK_MIN is taken over."""
    for _ in range(2):
        try:
            os.close(os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            return True
        except FileExistsError:
            try:
                if now - lock.stat().st_mtime < LOCK_MIN * 60:
                    return False
                dead = lock.with_name(f"{lock.name}.{os.getpid()}.stale")
                os.replace(lock, dead)  # the holder died; shortcut: two takers within ms can still both win, rare enough here
                os.remove(dead)
            except FileNotFoundError:
                pass  # its holder released it, or another taker won the rename: try again
    return False


def release(lock):
    try:
        os.remove(lock)
    except FileNotFoundError:
        pass  # a run past LOCK_MIN was taken over; the taker owns the lock now


def launch(run, order):
    """Rule 1: run the lane on the first profile in order that answers; its ledger entry, or None if none answers."""
    for p in order:
        if probe(run["host"], p):
            spawn(run["host"], run["cmd"].replace("{cli}", p), run["log"], run["cwd"])
            return dict(run, profile=p)
    return None


def load_ledger(ep):
    p = ep / "lanes.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_ledger(ep, ledger):
    tmp = ep / "lanes.json.tmp"
    tmp.write_text(json.dumps(ledger, indent=1), encoding="utf-8")
    # a status run reads lanes.json lock-free, and while it has the file open Windows refuses the replace (WinError 5);
    # its read lasts ms, so the replace waits up to 5 s for it. The last try raises: a longer hold is no reader
    for _ in range(50):
        try:
            return os.replace(tmp, ep / "lanes.json")
        except PermissionError:
            time.sleep(0.1)
    os.replace(tmp, ep / "lanes.json")


def group_of(sid):
    prefix = sid.split("-")[0]
    return "intro" if prefix in INTRO else prefix


def verified_complete(csv_path):
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    # an unquoted comma pushes fields past the header (DictReader keys them None), so "verified" may be misread
    return bool(rows) and all(None not in r and (r.get("verified") or "").strip() for r in rows)


def job_table(ep):
    """[(job, done, inputs_ok, note)] for every job the episode's files imply. Pure read of disk."""
    md = (ep / "edit_script.md").read_text(encoding="utf-8")
    unlocked = open_verify_ids(md)
    groups = {}
    for sid, text in parse_segments(md):
        groups.setdefault(group_of(sid), []).append((sid, text))
    table = []
    for g, members in groups.items():
        held_back = sorted(sid for sid, _ in members if sid in unlocked)
        locked = [(sid, text) for sid, text in members if sid not in unlocked]
        audio = ep / "audio"
        locked_voiced = bool(locked) and all((audio / f"{s}.wav").exists() and (audio / f"{s}.txt").exists()
                                             and (audio / f"{s}.txt").read_text(encoding="utf-8").strip() == t.strip()
                                             for s, t in locked)
        locked_words = locked_voiced and all((audio / f"{s}.words.json").exists() for s, _ in locked)
        # a group is DONE only with every segment voiced (script-scaling.md "Section lock"); while one is still open,
        # its locked segments can be worked (READY), and once they are, the job waits on the open one (BLOCKED)
        voiced, words = locked_voiced and not held_back, locked_words and not held_back
        note = f"open [verify]: {', '.join(held_back)}" if held_back else ""
        table.append((f"voice:{g}", voiced, bool(locked) and not locked_voiced, note))
        table.append((f"words:{g}", words, locked_voiced and not locked_words, note))
        cand = ep / "media" / "candidates" / g
        prov = cand / "provenance.csv"
        sourced = prov.exists() and ((cand / "sourcer.md").exists() or (cand / "candidates.md").exists())
        table.append((f"source:{g}", sourced, True, ""))
        table.append((f"verify:{g}", sourced and verified_complete(prov), sourced, ""))
        briefs = ep / "briefs" / g
        table.append((f"brief:{g}", (briefs / "_list.md").exists(), words, ""))
        for b in sorted(briefs.glob("*.md")) if briefs.is_dir() else []:
            if b.name != "_list.md":
                table.append((f"build:{b.stem}", (ep / "compositions" / f"{b.stem}.html").exists(), words, ""))
    for root in (ep / "media" / "candidates", ep / "briefs"):
        for d in sorted(p for p in root.iterdir() if p.is_dir()) if root.is_dir() else []:
            if d.name not in groups:
                # BLOCKED, not READY: nothing can run it (a shared pool or cta folder is legitimate), so it shows but never blocks
                table.append((f"orphan:{root.name}/{d.name}", False, False, "folder matches no segment group: move it if it belongs to one"))
    return table


def job_states(ep, ledger, now=None):
    """[{job, state, note}], state by first match: DONE > HELD > BLOCKED > FAILED > RUNNING > STALE > READY.
    Reads the log tail of every launched lane still running, on its host."""
    now = time.time() if now is None else now
    runs, holds = ledger.get("jobs", {}), ledger.get("holds", {})
    out = []
    for job, done, inputs_ok, note in job_table(ep):
        run, hold = runs.get(job, {}), holds.get(job)
        live_hold = hold and now < hold["at"] + HOLD_H * 3600
        if done:
            state = "DONE"
        elif live_hold:
            state, note = "HELD", hold["reason"]
        elif not inputs_ok:
            state = "BLOCKED"
        elif run.get("started") and not run.get("ended"):
            stale = now - run["started"] >= run.get("minutes", DEFAULT_MIN) * 60
            state = "STALE" if stale else "RUNNING"
            note = f"on {run.get('host', '?')} since {time.strftime('%H:%M', time.localtime(run['started']))}"
            got = read_lane(run["host"], run["log"]) if run.get("log") else (True, "")
            up, log = got or (True, "")  # an unreadable host is unknown, never dead
            if got is None:
                note += " (its host is unreadable: process and log unknown)"
            elif LIMIT.search(log):
                state, note = "FAILED", f"{run.get('profile')} hit its limit on {run['host']}: run `lanes.py relaunch`"
            elif log == NO_LOG:  # no log yet: the launch may still be starting, so only NO_LOG_MIN decides
                if now - run["started"] >= NO_LOG_MIN * 60:
                    state, note = "FAILED", f"its log never appeared on {run['host']}: the launch did not run; run `lanes.py relaunch`"
            elif not up:  # same as an ended lane: its output may sit unsynced on its host, so never FAILED (relaunch would redo it)
                state, note = "READY", f"its process exited on {run['host']} and its output is not here: relaunch it, or sync its output back"
        else:
            state = "READY"
            if run.get("ended"):
                note = "lane ended but its output is not here: relaunch it, or sync its output back"
            elif hold:
                note = f"hold lapsed ({hold['reason']}): re-decide"
        out.append({"job": job, "state": state, "note": note})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["claim", "start", "end", "hold", "unhold", "status", "relaunch", "stop"])
    ap.add_argument("episode")
    ap.add_argument("jobs", nargs="*")
    ap.add_argument("--host", default="local", choices=HOSTS)
    ap.add_argument("--cmd", dest="lane_cmd", help="start: the lane's command, {cli} where the profile goes")
    ap.add_argument("--log", help="start --cmd: the lane's log path on its host")
    ap.add_argument("--profile", help="start --cmd: the profile to try first")
    ap.add_argument("--cwd", help="start --cmd: the lane's working folder on its host (default: this checkout, local only)")
    ap.add_argument("--minutes", type=int, default=DEFAULT_MIN)
    ap.add_argument("--reason", default="")
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    ep = Path(a.episode).resolve()
    if not (ep / "edit_script.md").exists():
        sys.exit(f"[lanes] FAIL: {ep / 'edit_script.md'} not found")
    if a.cmd == "status":  # read-only and lock-free: the Stop hook calls it
        ledger = load_ledger(ep)
        states = job_states(ep, ledger, time.time())
        if a.json:
            print(json.dumps({"orchestrator": ledger.get("orchestrator"), "jobs": states,
                              "blocking": [f"{s['state']} {s['job']}" + (f" ({s['note']})" if s["note"] else "")
                                           for s in states if s["state"] in BLOCKING]}))
        else:
            for s in states:
                print(f"{s['state']:8} {s['job']:28} {s['note']}")
        return 2 if any(s["state"] in BLOCKING for s in states) else 0

    lock = ep / "lanes.json.lock"  # every ledger write holds it, so two writers never lose each other's update
    deadline = time.time() + (0 if a.cmd == "relaunch" else LOCK_WAIT_S)
    while not take_lock(lock, time.time()):
        if time.time() >= deadline:
            if a.cmd == "relaunch":
                print(f"[lanes] relaunch {ep.name}: another lanes.py holds {lock}; backing off")
                return 0
            sys.exit(f"[lanes] FAIL: another lanes.py held {lock} for {LOCK_WAIT_S} s; retry")
        time.sleep(1)
    try:
        return write(a, ep, lock)
    finally:
        release(lock)


def write(a, ep, lock):
    """Every command but status, run while holding lock; the ledger is read here, under it."""
    ledger = load_ledger(ep)
    now = time.time()
    if a.cmd == "relaunch":  # rule 3: a FAILED lane moves to the next profile that answers, never waits for a reset
        states = job_states(ep, ledger, now)
        left = 0
        for s in (s for s in states if s["state"] == "FAILED"):
            run = ledger["jobs"][s["job"]]
            why = gate(run["host"])
            new = None if why else launch(dict(run, started=now), profile_order(run["host"], run.get("profile"), skip=run.get("profile")))
            os.utime(lock)  # still alive: a long relaunch is never taken over
            if new:
                ledger["jobs"][s["job"]] = new
                s["state"] = "RUNNING"
                save_ledger(ep, ledger)  # saved per lane, so a later failure never forgets a launched one
            left += not new
            print(f"[lanes] relaunch {s['job']}: {'on ' + new['profile'] if new else 'not relaunched: ' + (why or 'no other profile answers')}")
        return 2 if left else 0

    if a.cmd == "claim":
        # the Stop hook runs the lanes.py of the episode's own checkout; claiming from another checkout would leave it none
        if SCRIPTS.parent not in ep.parents:
            sys.exit(f"[lanes] FAIL: run the lanes.py inside {ep}'s own checkout (merge main into its branch first)")
        if ".worktrees" not in ep.parts:
            sys.exit(f"[lanes] FAIL: {ep} is not in a worktree; the Stop hook reads only .worktrees/*/episodes/*/lanes.json")
        if not a.session:
            sys.exit("[lanes] FAIL: no session id (CLAUDE_CODE_SESSION_ID unset); pass --session")
    elif not a.jobs:
        sys.exit(f"[lanes] FAIL: {a.cmd} needs a job name, e.g. verify:a4 (`status` lists them)")
    else:
        states = job_states(ep, ledger, now)
        known = {s["job"] for s in states}
        if a.cmd == "start" and not 0 < a.minutes <= HOLD_H * 60:
            sys.exit(f"[lanes] FAIL: --minutes must be 1 to {HOLD_H * 60}; a longer lane is held with a reason instead")
        if a.jobs == ["all"] and a.cmd == "hold":
            a.jobs = [s["job"] for s in states if s["state"] in BLOCKING]
        if a.jobs == ["all"] and a.cmd == "stop":
            a.jobs = [s["job"] for s in states if s["state"] in ("RUNNING", "STALE", "FAILED")]  # all may still run
        unknown = sorted(set(a.jobs) - known)
        if unknown:
            sys.exit(f"[lanes] FAIL: unknown job(s) {unknown}; `status` lists the real names")
        if a.cmd == "hold" and not a.reason.strip():
            sys.exit("[lanes] FAIL: hold needs --reason; it shows in every status")
        if a.lane_cmd and (a.cmd != "start" or len(a.jobs) != 1 or not a.log or "{cli}" not in a.lane_cmd
                           or not (a.cwd or is_local(a.host))):
            sys.exit("[lanes] FAIL: --cmd is for start with one job, a --log, {cli} where the profile goes, and --cwd off local")
        busy = [s["job"] for s in states if s["job"] in a.jobs and s["state"] in ("RUNNING", "DONE")]
        if a.lane_cmd and busy:
            sys.exit(f"[lanes] FAIL: {busy[0]} is already RUNNING or DONE; a second launch would double it")
        if a.cmd == "start":
            why = gate(a.host)
            if why:
                sys.exit(f"[lanes] FAIL: not starting: {why}")
            run = {"started": now, "host": a.host, "minutes": a.minutes}
            if a.lane_cmd:
                run = launch(dict(run, cmd=a.lane_cmd, log=a.log, cwd=a.cwd or str(SCRIPTS.parent)), profile_order(a.profile))
                if not run:
                    sys.exit(f"[lanes] FAIL: no profile in {ACCOUNTS} answers on {a.host}")
    if a.cmd == "claim":
        ledger["orchestrator"] = a.session  # only claim stamps it, so a sibling session's start/end never takes the gate
    for job in a.jobs:
        if a.cmd == "start":
            ledger.setdefault("jobs", {})[job] = dict(run)
        elif a.cmd == "stop":  # a lane recorded without --log runs elsewhere and is not ours to find
            run = ledger.get("jobs", {}).get(job)
            n = kill(run.get("host", "local"), run["log"]) if run and run.get("log") else None
            print(f"[lanes] stop {job}: " + (f"{n} lane tree(s) ended" if n is not None else "not stopped: no log recorded or host unreadable; stop it where it runs"))
            if n is not None:  # marked ended only once stopped: an ended job reads READY and would be launched twice
                run["ended"] = now
        elif a.cmd == "end":
            ledger.setdefault("jobs", {}).setdefault(job, {"started": now, "host": a.host})["ended"] = now
        elif a.cmd == "hold":
            ledger.setdefault("holds", {})[job] = {"reason": a.reason.strip(), "at": now}
        elif a.cmd == "unhold":
            ledger.get("holds", {}).pop(job, None)
    save_ledger(ep, ledger)
    print(f"[lanes] {a.cmd} {ep.name}: {', '.join(a.jobs) or 'session ' + str(a.session)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
