#!/usr/bin/env python3
"""Episode job ledger: which jobs are DONE, RUNNING, BLOCKED, HELD, or READY to launch right now.

Why: the orchestrator ran episode jobs one after another and waited, while other jobs had every input on disk.
The Stop hook `~/.claude/hooks/lane-gate.py` runs `status --json` for every episode this session claimed and
refuses to end the turn while any job is READY or STALE. HOLD (with a reason, lapsing after HOLD_H) is the only
way past it.

State comes from disk; `<ep>/lanes.json` (gitignored) adds only what disk cannot show: which session orchestrates,
which jobs were launched and when they ended, and which are held.

  python3 scripts/lanes.py claim  episodes/<slug>            # this Claude session orchestrates the episode
  python3 scripts/lanes.py start  episodes/<slug> verify:a4 brief:a4 [--host zbook] [--minutes 60]
  python3 scripts/lanes.py end    episodes/<slug> verify:a4   # the lane stopped (its output may still need syncing back)
  python3 scripts/lanes.py hold   episodes/<slug> source:z1|all --reason "z1 media sits in the a6 folder"
  python3 scripts/lanes.py unhold episodes/<slug> source:z1
  python3 scripts/lanes.py status episodes/<slug> [--json]   # exit 2 while any job is READY or STALE

Groups: one per segment prefix (a1 = A1-S*), except H1, T1 and I1, which form `intro`. Jobs per group g:
  voice:g   every locked segment of g (no open [verify] in its heading block) has audio/<id>.wav, and
            audio/<id>.txt equals its script text (an edited line is not voiced until re-synthesised)
  words:g   ...and audio/<id>.words.json
  source:g  media/candidates/<g>/provenance.csv plus the sourcer's report (sourcer.md or candidates.md)
  verify:g  every provenance.csv row has a "verified" value, and no row has more fields than the header
  brief:g   briefs/<g>/_list.md (needs voice:g and words:g DONE)
  build:<comp>  compositions/<comp>.html, one per briefs/<g>/<comp>.md (needs voice:g and words:g DONE)
"""
import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from tts_episode import open_verify_ids, parse_segments  # noqa: E402

INTRO = {"h1", "t1", "i1"}
HOLD_H = 3          # a hold lapses after this many hours, so a wait is re-decided, never forgotten
DEFAULT_MIN = 60    # a lane with no end recorded this many minutes after its start is presumed dead (STALE)
BLOCKING = ("READY", "STALE")


def load_ledger(ep):
    p = ep / "lanes.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_ledger(ep, ledger):
    tmp = ep / "lanes.json.tmp"
    tmp.write_text(json.dumps(ledger, indent=1), encoding="utf-8")
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
        voiced = bool(locked) and all((audio / f"{s}.wav").exists() and (audio / f"{s}.txt").exists()
                                      and (audio / f"{s}.txt").read_text(encoding="utf-8").strip() == t.strip()
                                      for s, t in locked)
        words = voiced and all((audio / f"{s}.words.json").exists() for s, _ in locked)
        note = f"open [verify]: {', '.join(held_back)}" if held_back else ""
        table.append((f"voice:{g}", voiced, bool(locked), note))
        table.append((f"words:{g}", words, voiced, note))
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
                table.append((f"orphan:{root.name}/{d.name}", False, True, "folder matches no segment group: move it or hold this"))
    return table


def job_states(ep, ledger, now=None):
    """[{job, state, note}], state by first match: DONE > HELD > BLOCKED > RUNNING > STALE > READY."""
    now = time.time() if now is None else now
    runs, holds = ledger.get("jobs", {}), ledger.get("holds", {})
    out = []
    for job, done, inputs_ok, note in job_table(ep):
        run, hold = runs.get(job, {}), holds.get(job)
        live_hold = hold and now < hold["until"]
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
    ap.add_argument("cmd", choices=["claim", "start", "end", "hold", "unhold", "status"])
    ap.add_argument("episode")
    ap.add_argument("jobs", nargs="*")
    ap.add_argument("--host", default="local")
    ap.add_argument("--minutes", type=int, default=DEFAULT_MIN)
    ap.add_argument("--reason", default="")
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    ep = Path(a.episode).resolve()
    if not (ep / "edit_script.md").exists():
        sys.exit(f"[lanes] FAIL: {ep / 'edit_script.md'} not found")
    ledger = load_ledger(ep)
    now = time.time()

    if a.cmd == "status":
        states = job_states(ep, ledger, now)
        if a.json:
            print(json.dumps({"orchestrator": ledger.get("orchestrator"), "jobs": states,
                              "blocking": [f"{s['state']} {s['job']}" + (f" ({s['note']})" if s["note"] else "")
                                           for s in states if s["state"] in BLOCKING]}))
        else:
            for s in states:
                print(f"{s['state']:8} {s['job']:28} {s['note']}")
        return 2 if any(s["state"] in BLOCKING for s in states) else 0

    if a.cmd == "claim":
        # the Stop hook runs the lanes.py of the episode's own checkout; claiming from another checkout would leave it none
        if SCRIPTS.parent not in ep.parents:
            sys.exit(f"[lanes] FAIL: run the lanes.py inside {ep}'s own checkout (merge main into its branch first)")
        if not a.session:
            sys.exit("[lanes] FAIL: no session id (CLAUDE_CODE_SESSION_ID unset); pass --session")
    elif not a.jobs:
        sys.exit(f"[lanes] FAIL: {a.cmd} needs a job name, e.g. verify:a4 (`status` lists them)")
    else:
        states = job_states(ep, ledger, now)
        known = {s["job"] for s in states}
        if a.jobs == ["all"] and a.cmd == "hold":
            a.jobs = [s["job"] for s in states if s["state"] in BLOCKING]
        unknown = sorted(set(a.jobs) - known)
        if unknown:
            sys.exit(f"[lanes] FAIL: unknown job(s) {unknown}; `status` lists the real names")
        if a.cmd == "hold" and not a.reason.strip():
            sys.exit("[lanes] FAIL: hold needs --reason; it shows in every status")
    if a.session:
        ledger["orchestrator"] = a.session  # every write re-stamps it, so a resumed or forked session keeps the gate
    for job in a.jobs:
        if a.cmd == "start":
            ledger.setdefault("jobs", {})[job] = {"started": now, "host": a.host, "minutes": a.minutes}
        elif a.cmd == "end":
            ledger.setdefault("jobs", {}).setdefault(job, {"started": now, "host": a.host})["ended"] = now
        elif a.cmd == "hold":
            ledger.setdefault("holds", {})[job] = {"reason": a.reason.strip(), "until": now + HOLD_H * 3600}
        elif a.cmd == "unhold":
            ledger.get("holds", {}).pop(job, None)
    save_ledger(ep, ledger)
    print(f"[lanes] {a.cmd} {ep.name}: {', '.join(a.jobs) or 'session ' + str(a.session)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
