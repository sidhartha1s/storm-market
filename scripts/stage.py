#!/usr/bin/env python3
"""Every episode's stage and what it waits on, plus the record of the owner's approvals.

  python3 scripts/stage.py                       # the board: one row per episode folder with angle.md or gates.md
  python3 scripts/stage.py episodes/<slug>       # one episode in detail, every gates.md line verbatim
  python3 scripts/stage.py record episodes/<slug> <gate> --words "<his words, verbatim>" --shown "<file or URL>" [--where chat|devq]

The record: `episodes/<slug>/gates.md`, tracked, append-only, one line per event, written only by `record`:
  - <gate> | <YYYY-MM-DD> | "<words>" | <where> | shown: <what>
Gates (CLAUDE.md "Owner gates"): angle, packaging (title and thumbnail), hook-intro, draft, retake; the event
`published` is not a gate. `defer:<gate>` records a "picks later" and does not close the gate. The angle also counts as
approved from angle.md's `## Angle (locked by the owner, <d Mon yy>: ...)` heading. Nothing else is ever inferred.

Machine stage, first unmet of: script (edit_script.md) -> build (every lanes.py job DONE) -> draft (renders/*draft*.mp4
here or in the main checkout) -> master (main renders/<label>-final-master.mp4) -> uploads (main uploads/<label>/ holds
the master) -> published (a `published` line). A later artifact proves the earlier steps (drafts are deleted at master
time), so the search runs from the end. Owner gates block: angle always, hook-intro the build, draft the master,
packaging only the published step. Retake is never due from disk: it is asked for in chat, so it only shows its record.

Checkouts: the main checkout (first `git worktree list` entry) and every worktree. A slug in several checkouts is read
from the worktree whose branch-only commits (not on main's HEAD) touched it last; with none, from the main checkout, or
the first worktree that has it. The main checkout is the only place masters and uploads are looked for.
The board always exits 0: it is a report.
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import episode  # noqa: E402
import lanes  # noqa: E402

GATES = ("angle", "packaging", "hook-intro", "draft", "retake")
EVENTS = GATES + ("published",) + tuple(f"defer:{g}" for g in GATES)
WHERE = ("chat", "devq")
BLOCKS = {"build": "hook-intro", "master": "draft", "published": "packaging"}
LINE = re.compile(r'- (\S+) \| (\d{4}-\d{2}-\d{2}) \| "(.*)" \| (chat|devq) \| shown: (.*)')
ANGLE = re.compile(r"^## Angle \(locked by the owner, (\d{1,2} \w{3} \d{2})", re.M)
HEADER = "# Owner gates: append-only, one line per event, written only by `python3 scripts/stage.py record`\n"


def format_line(gate, day, words, where, shown):
    return f'- {gate} | {day} | "{words}" | {where} | shown: {shown}'


def parse_lines(text):
    """[(gate, date, words, where, shown)]; the greedy words group lets words hold quotes and pipes."""
    return [m.groups() for m in map(LINE.fullmatch, text.splitlines()) if m]


def angle_lock(text):
    """ISO date of the owner's lock heading in angle.md, or None."""
    m = ANGLE.search(text)
    return datetime.datetime.strptime(m.group(1), "%d %b %y").date().isoformat() if m else None


def gate_states(events, angle_date, has_record):
    """{gate: 'ok <date>' | 'deferred <date>' | 'OPEN' | 'no record' | '-'} from gates.md events and the angle heading."""
    out = {}
    for g in GATES:
        ok = [e[1] for e in events if e[0] == g] + ([angle_date] if g == "angle" and angle_date else [])
        deferred = [e[1] for e in events if e[0] == f"defer:{g}"]
        if ok:
            out[g] = f"ok {max(ok)}"
        elif deferred:
            out[g] = f"deferred {max(deferred)}"
        else:
            out[g] = "-" if g == "retake" else "OPEN" if has_record else "no record"
    return out


def stage_of(facts):
    """facts: script, draft, master, uploads, published (bools) and jobs (lanes states) -> first unmet step or DONE."""
    if facts["published"]:
        return "DONE"
    for step, done in (("published", "uploads"), ("uploads", "master"), ("master", "draft")):
        if facts[done]:
            return step
    if not facts["script"]:
        return "script"
    jobs = facts["jobs"]
    return "draft" if jobs and all(s == "DONE" for s in jobs) else "build"


def next_command(stage, slug):
    return {"script": f"write episodes/{slug}/edit_script.md",
            "build": f"lanes.py status episodes/{slug}",
            "draft": f"run_gates.py episodes/{slug}, then render.cmd {slug} draft",
            "master": f"render.cmd {slug} full, then master_deliverables.py",
            "uploads": f"ship.py episodes/{slug} <basename>",
            "published": f"upload, then stage.py record episodes/{slug} published"}[stage]


def waiting_on(stage, states, slug):
    """OWNER <open gates that block this step> | MACHINE <next command> | DONE."""
    if stage == "DONE":
        return "DONE"
    open_ = [g for g in ("angle", BLOCKS.get(stage)) if g and not states[g].startswith("ok")]
    return f"OWNER {' '.join(open_)}" if open_ else f"MACHINE {next_command(stage, slug)}"


def deliverables(main_root, slug, label):
    """The final names (CLAUDE.md step 7) in the main checkout; ship.py writes them, stage.py reads them."""
    renders = Path(main_root) / "episodes" / slug / "renders"
    up = Path(main_root) / "uploads" / str(label)
    return {"renders": renders, "uploads": up,
            "master": renders / f"{label}-final-master.mp4", "srt": renders / f"{label}-final-master.srt",
            "metadata": renders / f"{label}-metadata.md",
            "up_master": up / f"{label}-final-master.mp4", "up_srt": up / f"{label}-final-master.srt",
            "up_metadata": up / f"{label}-metadata.md", "up_titles": up / f"{label}-titles.txt"}


def read_episode(ep, main_root):
    """Everything the board shows for one episode folder: plain values."""
    rec = ep / "gates.md"
    events = parse_lines(rec.read_text(encoding="utf-8")) if rec.exists() else []
    angle = ep / "angle.md"
    states = gate_states(events, angle_lock(angle.read_text(encoding="utf-8")) if angle.exists() else None, rec.exists())
    label = episode.label(ep)
    d = deliverables(main_root, ep.name, label) if label else None
    facts = {"script": (ep / "edit_script.md").exists(),
             "draft": any(any((root / "episodes" / ep.name / "renders").glob("*draft*.mp4"))
                          for root in (ep.parent.parent, Path(main_root))),
             "master": bool(d and d["master"].exists()),
             "uploads": bool(d and d["up_master"].exists()),
             "published": any(e[0] == "published" for e in events), "jobs": []}
    if facts["script"] and not any(facts[k] for k in ("draft", "master", "uploads", "published")):
        facts["jobs"] = [j["state"] for j in lanes.job_states(ep, lanes.load_ledger(ep))]
    stage = stage_of(facts)
    shown = stage
    if stage == "build":
        shown = f"build {facts['jobs'].count('DONE')}/{len(facts['jobs'])}"
    return {"label": label or "-", "slug": ep.name, "stage": shown, "states": states,
            "waiting": waiting_on(stage, states, ep.name), "events": events}


def checkouts():
    """[(path, branch, head)] from `git worktree list --porcelain`; the first is the main checkout."""
    out = subprocess.run(["git", "-C", str(SCRIPTS), "worktree", "list", "--porcelain"],
                         capture_output=True, text=True, check=True).stdout
    found = []
    for block in out.strip().split("\n\n"):
        f = dict(line.split(" ", 1) for line in block.splitlines() if " " in line)
        found.append((Path(f["worktree"]), f.get("branch", "").removeprefix("refs/heads/"), f.get("HEAD", "")))
    return found


def branch_touches(path, main_head):
    """{slug: newest commit time} over this checkout's commits that main's HEAD does not have."""
    out = subprocess.run(["git", "-C", str(path), "log", "--format=@%ct", "--name-only", f"{main_head}..HEAD",
                          "--", "episodes"], capture_output=True, text=True, check=True).stdout
    newest, t = {}, 0
    for line in out.splitlines():
        if line.startswith("@"):
            t = int(line[1:])
        elif line.startswith("episodes/"):
            slug = line.split("/")[1]
            newest[slug] = max(newest.get(slug, 0), t)
    return newest


def pick_checkout(have, newest):
    """Index of the checkout a slug is read from. have: indexes holding it (0 = main); newest: per index, the time of
    its newest branch-only commit on the slug (0 = none). The newest wins; with none, the lowest index (main first)."""
    return -max((newest[i], -i) for i in have)[1]


def board_rows():
    cos = checkouts()
    main_root, main_head = cos[0][0], cos[0][2]
    where = {}
    for i, (path, _, _) in enumerate(cos):
        eps = path / "episodes"
        for ep in sorted(eps.iterdir()) if eps.is_dir() else []:
            if (ep / "angle.md").exists() or (ep / "gates.md").exists():
                where.setdefault(ep.name, []).append(i)
    touches = [{}] + [branch_touches(p, main_head) for p, _, _ in cos[1:]]
    rows = []
    for slug in sorted(where):
        i = pick_checkout(where[slug], [touches[j].get(slug, 0) for j in range(len(cos))])
        row = read_episode(cos[i][0] / "episodes" / slug, main_root)
        row["from"] = "main" if i == 0 else cos[i][0].name
        rows.append(row)
    return rows


def render_board(rows):
    head = ["label", "slug", "next step", *GATES, "waiting on", "from"]
    table = [head] + [[r["label"], r["slug"], r["stage"], *(r["states"][g] for g in GATES), r["waiting"], r["from"]]
                      for r in rows]
    widths = [max(len(t[c]) for t in table) for c in range(len(head))]
    return "\n".join("  ".join(v.ljust(w) for v, w in zip(t, widths)).rstrip() for t in table)


def record(ep, gate, words, shown, where, today=None):
    """Append one event line to ep/gates.md; refuses an unknown gate, empty words or empty shown."""
    if gate not in EVENTS:
        sys.exit(f"[stage] FAIL: unknown gate {gate!r}; one of {', '.join(EVENTS)}")
    if where not in WHERE:
        sys.exit(f"[stage] FAIL: --where is chat or devq, not {where!r}")
    if not words.strip() or not shown.strip():
        sys.exit("[stage] FAIL: --words (the owner's words, verbatim) and --shown (what he was shown) are both required")
    if "\n" in words or "\n" in shown:
        sys.exit("[stage] FAIL: one line per event; the words or shown text holds a line break")
    if not ep.is_dir():
        sys.exit(f"[stage] FAIL: no episode folder {ep}")
    line = format_line(gate, today or datetime.date.today().isoformat(), words, where, shown)
    rec = ep / "gates.md"
    # a hand-saved file without a final newline would otherwise get this line glued onto its last one
    prefix = HEADER if not rec.exists() else "" if rec.read_bytes().endswith(b"\n") else "\n"
    with open(rec, "a", encoding="utf-8", newline="\n") as f:
        f.write(prefix + line + "\n")
    return line


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["record"]:
        ap = argparse.ArgumentParser(prog="stage.py record")
        ap.add_argument("ep", type=Path)
        ap.add_argument("gate")
        ap.add_argument("--words", required=True)
        ap.add_argument("--shown", required=True)
        ap.add_argument("--where", default="chat")
        a = ap.parse_args(argv[1:])
        print(record(a.ep, a.gate, a.words, a.shown, a.where))
        return 0
    if argv:
        ep = Path(argv[0]).resolve()
        if not ep.is_dir():
            sys.exit(f"[stage] FAIL: no episode folder {ep}")
        r = read_episode(ep, checkouts()[0][0])
        print(f"{r['label']}  {r['slug']}  ({ep})\nnext step:  {r['stage']}\nwaiting on: {r['waiting']}")
        for g in GATES:
            print(f"  {g:<11}{r['states'][g]}")
        rec = ep / "gates.md"
        print(f"{rec}:\n" + (rec.read_text(encoding="utf-8").rstrip() if rec.exists() else "  (none)"))
        return 0
    print(render_board(board_rows()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
