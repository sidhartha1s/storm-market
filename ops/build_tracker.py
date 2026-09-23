"""Render ops/tracker.json into ops/tracker.html: one page, every video, its phase, status, blocker.

Usage: python3 ops/build_tracker.py            # rebuild the page
       python3 ops/build_tracker.py set <slug> <phase> <status> ["note"]   # move a card, then rebuild
       python3 ops/build_tracker.py add <slug> <lane> <due DD Mon YY> "<title>"   # new card at idea/todo, then rebuild
Phases run left to right; a card sits in exactly one. Status: todo | doing | blocked | failed | done. Dates DD Mon YY.
"""
import html, json, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DATA = ROOT / "tracker.json"
OUT = ROOT / "tracker.html"
# plain words (owner 2026-09-14): checks = static gate suite, preview = draft render the owner eyeballs,
# render = the final full render, upload = -14 LUFS master + SRT + metadata delivered and published
PHASES = ["idea", "packaging", "script", "tts", "sourcing", "assemble", "checks", "preview", "render", "upload"]
STATUSES = {"todo", "doing", "blocked", "failed", "done"}
COLOR = {"todo": "#e8eef5", "doing": "#cfe3ff", "blocked": "#ffe2b8", "failed": "#ffc9c9", "done": "#cfeedd"}


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def save(d):
    DATA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def set_card(slug, phase, status, note=None):
    assert phase in PHASES, f"phase must be one of {PHASES}"
    assert status in STATUSES, f"status must be one of {sorted(STATUSES)}"
    d = load()
    card = next((c for c in d["videos"] if c["slug"] == slug), None)
    if card is None:
        sys.exit(f"no such slug: {slug}")
    card.update(phase=phase, status=status, updated=datetime.datetime.now().strftime("%d %b %y %H:%M"))
    if note is not None:
        card["note"] = note
    save(d)


def add_card(slug, lane, due, title):
    datetime.datetime.strptime(due, "%d %b %y")  # render() sorts on this; fail now, not later
    d = load()
    if any(c["slug"] == slug for c in d["videos"]):
        sys.exit(f"slug already exists: {slug}")
    d["videos"].append(dict(slug=slug, lane=lane, due=due, title=title, phase="idea", status="todo",
                            updated=datetime.datetime.now().strftime("%d %b %y %H:%M")))
    save(d)


def render():
    d = load()
    for c in d["videos"]:
        if c["phase"] not in PHASES or c["status"] not in STATUSES:
            sys.exit(f'{c["slug"]}: phase {c["phase"]!r} / status {c["status"]!r} not in {PHASES} / {sorted(STATUSES)}')
    rows = []
    for c in sorted(d["videos"], key=lambda c: (datetime.datetime.strptime(c["due"], "%d %b %y"), c["slug"])):
        cells = []
        for p in PHASES:
            if p == c["phase"]:
                cells.append(f'<td class="on" style="background:{COLOR[c["status"]]}">{c["status"]}</td>')
            elif PHASES.index(p) < PHASES.index(c["phase"]):
                cells.append('<td class="past">✓</td>')
            else:
                cells.append("<td></td>")
        rows.append(
            f'<tr><td class="slug"><b>{html.escape(c["slug"])}</b><br><small>{html.escape(c.get("lane",""))} · {html.escape(c.get("bucket",""))}</small></td>'
            f'<td>{html.escape(c.get("title",""))}</td><td>{html.escape(c.get("owner",""))}</td><td>{html.escape(c.get("due",""))}</td>'
            + "".join(cells)
            + f'<td class="note">{html.escape(c.get("note",""))}</td><td><small>{html.escape(c.get("updated",""))}</small></td></tr>'
        )
    agents = "".join(f'<li><b>{html.escape(a["name"])}</b> · {html.escape(a["role"])} · {html.escape(a.get("status",""))}</li>' for a in d.get("agents", []))
    blockers = [c for c in d["videos"] if c["status"] in ("blocked", "failed")]
    bl = "".join(f'<li><b>{html.escape(c["slug"])}</b> · {c["phase"]} {c["status"]} · {html.escape(c.get("note",""))}</li>' for c in blockers) or "<li>none</li>"
    now = datetime.datetime.now().strftime("%d %b %y %H:%M")
    page = f"""<!doctype html><meta charset="utf-8"><title>Warning Hour · ops tracker</title>
<style>
body{{font:14px/1.4 system-ui,Segoe UI,sans-serif;background:#f3f8fd;color:#123;margin:24px}}
h1{{color:#1c5fb8;margin:0 0 4px}} .sub{{color:#567;margin-bottom:16px}}
table{{border-collapse:collapse;width:100%;background:#fff;box-shadow:0 1px 3px #0002}}
th,td{{border:1px solid #d8e3ef;padding:6px 8px;text-align:left;vertical-align:top}}
th{{background:#e3efff;color:#1c5fb8;font-weight:600;white-space:nowrap}}
td.on{{font-weight:700;text-align:center}} td.past{{color:#7a9;text-align:center}} td.slug{{white-space:nowrap}} td.note{{max-width:320px}}
.box{{background:#fff;border:1px solid #d8e3ef;padding:10px 14px;margin:14px 0;box-shadow:0 1px 3px #0002}}
.box h2{{margin:0 0 6px;font-size:15px;color:#1c5fb8}} ul{{margin:0;padding-left:18px}}
</style>
<h1>The Warning Hour · ops tracker</h1>
<div class="sub">rebuilt {now} · {len(d["videos"])} videos · {len(blockers)} blocked/failed · renders run in the main chat and are announced before launch</div>
<div class="box"><h2>Blockers &amp; failures</h2><ul>{bl}</ul></div>
<table><tr><th>video</th><th>working title</th><th>owner</th><th>due</th>{"".join(f"<th>{p}</th>" for p in PHASES)}<th>note</th><th>updated</th></tr>
{"".join(rows)}</table>
<div class="box"><h2>Crew</h2><ul>{agents}</ul></div>
<div class="box"><h2>Standing rules</h2><ul>{"".join(f"<li>{html.escape(r)}</li>" for r in d.get("rules", []))}</ul></div>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT} ({len(d['videos'])} videos)")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "set":
        set_card(*sys.argv[2:6])
    elif len(sys.argv) > 1 and sys.argv[1] == "add":
        add_card(*sys.argv[2:6])
    render()
