#!/usr/bin/env python3
"""Episode job ledger: which jobs are DONE, RUNNING, BLOCKED, HELD, or READY to launch right now.

Why: the orchestrator ran episode jobs one after another and waited, while other jobs had every input on disk.
The Stop hook `~/.claude/hooks/lane-gate.py` runs `status --json` for every episode this session claimed and
refuses to end the turn while any job is READY or STALE. HOLD (with a reason) is the only way past it.

State comes from disk; `<ep>/lanes.json` (gitignored) adds only what disk cannot show: who orchestrates, which
jobs were launched and ended, which are held, and optional segment groups.

  python3 scripts/lanes.py claim  episodes/<slug>            # this Claude session orchestrates the episode
  python3 scripts/lanes.py start  episodes/<slug> verify:a4 brief:a4 [--host zbook]
  python3 scripts/lanes.py end    episodes/<slug> verify:a4 --result ok|error
  python3 scripts/lanes.py hold   episodes/<slug> source:z1 --reason "media sits in the a6 folder"
  python3 scripts/lanes.py unhold episodes/<slug> source:z1
  python3 scripts/lanes.py status episodes/<slug> [--json]   # exit 2 while any job is READY or STALE

Jobs per group g (default: one group per segment prefix, e.g. a1 = A1-S*; lanes.json "groups" merges prefixes):
  voice:g   every segment of g without an open [verify] has audio/<id>.wav
  words:g   ...and audio/<id>.words.json
  source:g  media/candidates/<g>/provenance.csv exists
  verify:g  every provenance.csv row has a non-empty "verified" value
  brief:g   briefs/<g>/_list.md exists (needs voice:g and words:g DONE)
  build:<comp>  compositions/<comp>.html exists, one per briefs/<g>/<comp>.md (needs voice:g and words:g DONE)
"""
import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tts_episode import has_open_verify, parse_segments  # noqa: E402

STALE_S = 3 * 3600  # a lane started this long ago with no end recorded is presumed dead
BLOCKING = ("READY", "STALE")


def load_ledger(ep):
    p = ep / "lanes.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_ledger(ep, ledger):
    tmp = ep / "lanes.json.tmp"
    tmp.write_text(json.dumps(ledger, indent=1), encoding="utf-8")
    os.replace(tmp, ep / "lanes.json")


def group_segments(segs, groups):
    """{group: [(sid, text)]}. A prefix named in `groups` joins that group; every other prefix is its own group."""
    by_prefix = {p: g for g, prefixes in groups.items() for p in prefixes}
    out = {}
    for sid, text in segs:
        prefix = sid.split("-")[0]
        out.setdefault(by_prefix.get(prefix, prefix), []).append((sid, text))
    return out


def verified_complete(csv_path):
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return bool(rows) and all((r.get("verified") or "").strip() for r in rows)


def job_table(ep, ledger):
    """[(job, done, inputs_ok, note)] for every job the episode's files imply. Pure read of disk."""
    segs = parse_segments((ep / "edit_script.md").read_text(encoding="utf-8"))
    table = []
    for g, members in group_segments(segs, ledger.get("groups", {})).items():
        lockable = [sid for sid, text in members if not has_open_verify(text)]
        unvoiceable = [sid for sid, text in members if has_open_verify(text)]
        wav_ok = bool(lockable) and all((ep / "audio" / f"{s}.wav").exists() for s in lockable)
        words_ok = wav_ok and all((ep / "audio" / f"{s}.words.json").exists() for s in lockable)
        note = f"open [verify]: {', '.join(unvoiceable)}" if unvoiceable else ""
        table.append((f"voice:{g}", wav_ok, bool(lockable), note))
        table.append((f"words:{g}", words_ok, wav_ok, note))
        prov = ep / "media" / "candidates" / g / "provenance.csv"
        table.append((f"source:{g}", prov.exists(), True, ""))
        table.append((f"verify:{g}", prov.exists() and verified_complete(prov), prov.exists(), ""))
        briefs = ep / "briefs" / g
        table.append((f"brief:{g}", (briefs / "_list.md").exists(), words_ok, ""))
        for b in sorted(briefs.glob("*.md")) if briefs.is_dir() else []:
            if b.name != "_list.md":
                table.append((f"build:{b.stem}", (ep / "compositions" / f"{b.stem}.html").exists(), words_ok, ""))
    return table


def job_states(ep, ledger, now=None):
    """[{job, state, note}], state by first match: DONE > HELD > BLOCKED > RUNNING > STALE > READY."""
    now = time.time() if now is None else now
    runs, holds = ledger.get("jobs", {}), ledger.get("holds", {})
    out = []
    for job, done, inputs_ok, note in job_table(ep, ledger):
        run = runs.get(job, {})
        if done:
            state = "DONE"
        elif job in holds:
            state, note = "HELD", holds[job]
        elif not inputs_ok:
            state = "BLOCKED"
        elif run.get("started") and not run.get("ended"):
            state = "RUNNING" if now - run["started"] < STALE_S else "STALE"
            note = note or f"on {run.get('host', '?')} since {time.strftime('%H:%M', time.localtime(run['started']))}"
        else:
            state = "READY"
            if run.get("ended"):  # launched and ended, yet no output on this machine: failed or never synced back
                note = f"lane ended ({run.get('result', '?')}) but its output is not here: relaunch, or sync it back"
        out.append({"job": job, "state": state, "note": note})
    return out


def known_jobs(ep, ledger):
    return {job for job, *_ in job_table(ep, ledger)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["claim", "start", "end", "hold", "unhold", "status"])
    ap.add_argument("episode")
    ap.add_argument("jobs", nargs="*")
    ap.add_argument("--host", default="local")
    ap.add_argument("--result", choices=["ok", "error"])
    ap.add_argument("--reason")
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    ep = Path(a.episode).resolve()
    if not (ep / "edit_script.md").exists():
        sys.exit(f"[lanes] FAIL: {ep / 'edit_script.md'} not found")
    ledger = load_ledger(ep)

    if a.cmd == "status":
        states = job_states(ep, ledger)
        if a.json:
            print(json.dumps({"orchestrator": ledger.get("orchestrator"), "jobs": states}))
        else:
            for s in states:
                print(f"{s['state']:8} {s['job']:28} {s['note']}")
        return 2 if any(s["state"] in BLOCKING for s in states) else 0

    if a.cmd == "claim":
        if not a.session:
            sys.exit("[lanes] FAIL: no session id (CLAUDE_CODE_SESSION_ID unset); pass --session")
        ledger["orchestrator"] = a.session
        save_ledger(ep, ledger)
        print(f"[lanes] {ep.name} orchestrated by session {a.session}")
        return 0

    if not a.jobs:
        sys.exit(f"[lanes] FAIL: {a.cmd} needs at least one job name, e.g. verify:a4")
    unknown = sorted(set(a.jobs) - known_jobs(ep, ledger))
    if unknown:
        sys.exit(f"[lanes] FAIL: unknown job(s) {unknown}; `status` lists the real names")
    now = time.time()
    for job in a.jobs:
        if a.cmd == "start":
            ledger.setdefault("jobs", {})[job] = {"started": now, "host": a.host}
        elif a.cmd == "end":
            if not a.result:
                sys.exit("[lanes] FAIL: end needs --result ok|error")
            ledger.setdefault("jobs", {}).setdefault(job, {"started": now, "host": a.host}).update(ended=now, result=a.result)
        elif a.cmd == "hold":
            if not (a.reason or "").strip():
                sys.exit("[lanes] FAIL: hold needs --reason, shown in every status")
            ledger.setdefault("holds", {})[job] = a.reason.strip()
        elif a.cmd == "unhold":
            ledger.get("holds", {}).pop(job, None)
    save_ledger(ep, ledger)
    print(f"[lanes] {a.cmd}: {', '.join(a.jobs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
