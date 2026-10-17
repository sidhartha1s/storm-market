"""Self-check for scripts/lanes.py: python3 scripts/test_lanes.py

Builds throwaway episode fixtures in a temp dir. Each case proves a job reaches the state the gate relies on;
a READY job that reads DONE, or a dead lane that reads RUNNING, is exactly the idle-lane failure this guards.
"""
import json
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import lanes  # noqa: E402

FAILS = []
SCRIPT = """# fixture
### H1-S1 · narration
**Picture:** a map.
> Hook line one.

### I1-S1 · narration
**Picture:** a card.
> Intro line one.

### A1-S1 · narration
**Picture:** a NIST photo.
> Act one line.

### A1-S2 · narration
**Picture:** a strip.
> A claim we still check [verify: source].
"""


def check(name, cond):
    if not cond:
        FAILS.append(name)
    print(("ok   " if cond else "FAIL ") + name)


def episode(tmp):
    ep = Path(tmp) / "episodes" / "ep-fixture"
    (ep / "audio").mkdir(parents=True)
    (ep / "edit_script.md").write_text(SCRIPT, encoding="utf-8")
    return ep


def states(ep, ledger=None, now=None):
    return {s["job"]: s["state"] for s in lanes.job_states(ep, ledger or {}, now)}


def touch(p, text=""):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


with tempfile.TemporaryDirectory() as tmp:
    ep = episode(tmp)
    st = states(ep)
    check("fresh episode: voice READY", st["voice:a1"] == "READY")
    check("fresh episode: words BLOCKED until voice", st["words:a1"] == "BLOCKED")
    check("fresh episode: brief BLOCKED until voice+words", st["brief:a1"] == "BLOCKED")
    check("fresh episode: source READY from the start (never waits for voice)", st["source:a1"] == "READY")
    check("fresh episode: verify BLOCKED until a ledger exists", st["verify:a1"] == "BLOCKED")

    touch(ep / "audio" / "a1-s1.wav")
    st = states(ep)
    check("open [verify] segment is not required for voice DONE", st["voice:a1"] == "DONE")
    check("words READY once the lockable wavs exist", st["words:a1"] == "READY")
    touch(ep / "audio" / "a1-s1.words.json", "[]")
    check("brief READY once voice+words DONE", states(ep)["brief:a1"] == "READY")

    g = {"groups": {"intro": ["h1", "i1"]}}
    st = states(ep, g)
    check("groups merge prefixes", "voice:intro" in st and "voice:h1" not in st and "voice:i1" not in st)

    prov = ep / "media" / "candidates" / "a1" / "provenance.csv"
    touch(prov, "file,source_url,license\nx.jpg,u,PD\n")
    st = states(ep)
    check("source DONE once provenance.csv exists", st["source:a1"] == "DONE")
    check("verify READY when the csv has no verified column", st["verify:a1"] == "READY")
    touch(prov, "file,source_url,license,verified\nx.jpg,u,PD,Y\ny.jpg,u,PD,\n")
    check("verify READY while one row is blank", states(ep)["verify:a1"] == "READY")
    touch(prov, "file,source_url,license,verified\nx.jpg,u,PD,Y\ny.jpg,u,PD,FAIL watermark\n")
    check("verify DONE when every row has a value", states(ep)["verify:a1"] == "DONE")
    touch(prov, "file,source_url,license,verified\n")
    check("verify not DONE on a header-only csv", states(ep)["verify:a1"] == "READY")

    touch(ep / "briefs" / "a1" / "_list.md")
    touch(ep / "briefs" / "a1" / "g-a1-map.md")
    st = states(ep)
    check("brief DONE once _list.md exists", st["brief:a1"] == "DONE")
    check("build READY per brief file, _list.md is not a comp", st.get("build:g-a1-map") == "READY" and "build:_list" not in st)
    touch(ep / "compositions" / "g-a1-map.html")
    check("build DONE once the comp exists", states(ep)["build:g-a1-map"] == "DONE")

    now = time.time()
    run = {"jobs": {"brief:i1": {"started": now - 60, "host": "zbook"}}}
    touch(ep / "audio" / "i1-s1.wav"); touch(ep / "audio" / "i1-s1.words.json", "[]")
    check("started, no end: RUNNING", states(ep, run, now)["brief:i1"] == "RUNNING")
    check("started 3 h ago, no end: STALE", states(ep, run, now + lanes.STALE_S)["brief:i1"] == "STALE")
    run["jobs"]["brief:i1"].update(ended=now, result="error")
    check("ended with error, no output: READY again (a limit hit never hides)", states(ep, run, now)["brief:i1"] == "READY")
    run["jobs"]["brief:i1"]["result"] = "ok"
    check("ended ok but output not synced back: READY", states(ep, run, now)["brief:i1"] == "READY")
    run["holds"] = {"brief:i1": "owner gate"}
    check("hold wins over READY", states(ep, run, now)["brief:i1"] == "HELD")

    # CLI round trip: claim, start, hold, status exit code
    e = str(ep)
    try:
        lanes.main(["claim", e, "--session", ""])
        check("claim without a session id fails", False)
    except SystemExit:
        check("claim without a session id fails", not (ep / "lanes.json").exists())
    check("claim records the session", lanes.main(["claim", e, "--session", "S1"]) == 0
          and json.loads((ep / "lanes.json").read_text())["orchestrator"] == "S1")
    try:
        lanes.main(["start", e, "brief:nope"])
        check("start rejects an unknown job", False)
    except SystemExit:
        check("start rejects an unknown job", True)
    try:
        lanes.main(["hold", e, "voice:h1", "--reason", " "])
        check("hold rejects a blank reason", False)
    except SystemExit:
        check("hold rejects a blank reason", True)
    check("status exits 2 while a job is READY", lanes.main(["status", e]) == 2)
    ready = [j for j, s in states(ep, lanes.load_ledger(ep)).items() if s in lanes.BLOCKING]
    lanes.main(["hold", e, *ready, "--reason", "fixture"])
    check("status exits 0 once every ready job is held", lanes.main(["status", e]) == 0)

if FAILS:
    sys.exit(f"[test_lanes] FAIL: {FAILS}")
print("[test_lanes] all checks passed")
