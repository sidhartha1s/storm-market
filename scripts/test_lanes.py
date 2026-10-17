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
> A claim we still check.

**Rows:** [verify: source]
"""


def check(name, cond):
    if not cond:
        FAILS.append(name)
    print(("ok   " if cond else "FAIL ") + name)


def states(ep, ledger=None, now=None):
    return {s["job"]: s["state"] for s in lanes.job_states(ep, ledger or {}, now)}


def touch(p, text=""):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def voice(ep, sid, line):
    touch(ep / "audio" / f"{sid}.wav")
    touch(ep / "audio" / f"{sid}.txt", line)
    touch(ep / "audio" / f"{sid}.words.json", "[]")


def raises(fn):
    try:
        fn()
    except SystemExit:
        return True
    return False


with tempfile.TemporaryDirectory() as tmp:
    fx = S.parent / ".worktrees" / "_test-lanes-fixture"  # inside this checkout and a .worktrees dir, so `claim` accepts it
    ep = fx / "episodes" / "ep-fx"
    if fx.exists():
        sys.exit(f"[test_lanes] FAIL: {fx} already exists; remove it by hand")
    try:
        touch(ep / "edit_script.md", SCRIPT)
        st = states(ep)
        check("H1/T1/I1 form the intro group", "voice:intro" in st and "voice:h1" not in st and "voice:i1" not in st)
        check("fresh episode: voice READY", st["voice:a1"] == "READY")
        check("fresh episode: words BLOCKED until voice", st["words:a1"] == "BLOCKED")
        check("fresh episode: brief BLOCKED until voice+words", st["brief:a1"] == "BLOCKED")
        check("fresh episode: source READY from the start (never waits for voice)", st["source:a1"] == "READY")
        check("fresh episode: verify BLOCKED until sourcing is done", st["verify:a1"] == "BLOCKED")

        touch(ep / "audio" / "a1-s1.wav")
        check("wav without its voiced text is not DONE", states(ep)["voice:a1"] == "READY")
        touch(ep / "audio" / "a1-s1.txt", "An old wording.")
        check("wav voiced from an edited line is not DONE", states(ep)["voice:a1"] == "READY")
        touch(ep / "audio" / "a1-s1.txt", "Act one line.")
        st = states(ep)
        check("a [verify] on the Rows line keeps a group from DONE: voice BLOCKED once the rest is voiced",
              st["voice:a1"] == "BLOCKED" and "a1-s2" in next(x["note"] for x in lanes.job_states(ep, {}) if x["job"] == "voice:a1"))
        check("words READY once the locked wavs exist", st["words:a1"] == "READY")
        touch(ep / "audio" / "a1-s1.words.json", "[]")
        st = states(ep)
        check("open segment: words BLOCKED and brief BLOCKED (no graphic on an unlocked section)",
              st["words:a1"] == "BLOCKED" and st["brief:a1"] == "BLOCKED")
        touch(ep / "edit_script.md", SCRIPT.replace("[verify: source]", "checked"))
        check("the [verify] resolved: voice READY for the newly locked segment", states(ep)["voice:a1"] == "READY")
        voice(ep, "a1-s2", "A claim we still check.")
        st = states(ep)
        check("brief READY once voice+words DONE", st["voice:a1"] == "DONE" and st["brief:a1"] == "READY")

        cand = ep / "media" / "candidates" / "a1"
        touch(cand / "provenance.csv", "file,source_url,license\nx.jpg,u,PD\n")
        check("a ledger alone (sourcer still writing) is not source DONE", states(ep)["source:a1"] == "READY")
        touch(cand / "sourcer.md", "report")
        st = states(ep)
        check("source DONE once ledger + sourcer report exist", st["source:a1"] == "DONE")
        check("verify READY when the csv has no verified column", st["verify:a1"] == "READY")
        touch(cand / "provenance.csv", "file,source_url,license,verified\nx.jpg,u,PD,Y\ny.jpg,u,PD,\n")
        check("verify READY while one row is blank", states(ep)["verify:a1"] == "READY")
        touch(cand / "provenance.csv", "file,source_url,license,verified\nx.jpg,u,PD, with comma,Y\n")
        check("a row with an unquoted comma is not verified", states(ep)["verify:a1"] == "READY")
        touch(cand / "provenance.csv", "file,source_url,license,verified\nx.jpg,u,PD,Y\ny.jpg,u,PD,FAIL watermark\n")
        check("verify DONE when every row has a value", states(ep)["verify:a1"] == "DONE")
        touch(cand / "provenance.csv", "file,source_url,license,verified\n")
        check("a header-only csv is not verified", states(ep)["verify:a1"] == "READY")

        touch(ep / "briefs" / "a1" / "_list.md")
        touch(ep / "briefs" / "a1" / "g-a1-map.md")
        st = states(ep)
        check("brief DONE once _list.md exists", st["brief:a1"] == "DONE")
        check("build READY per brief file, _list.md is not a comp", st.get("build:g-a1-map") == "READY" and "build:_list" not in st)
        touch(ep / "compositions" / "g-a1-map.html")
        check("build DONE once the comp exists", states(ep)["build:g-a1-map"] == "DONE")
        (ep / "briefs" / "zz").mkdir()
        check("a folder matching no group is reported", states(ep).get("orphan:briefs/zz") == "READY")
        (ep / "briefs" / "zz").rmdir()

        now = time.time()
        voice(ep, "h1-s1", "Hook line one.")
        voice(ep, "i1-s1", "Intro line one.")
        run = {"jobs": {"brief:intro": {"started": now - 60, "host": "zbook", "minutes": 50}}}
        check("started, no end: RUNNING", states(ep, run, now)["brief:intro"] == "RUNNING")
        check("past its own minutes, no end: STALE", states(ep, run, now + 50 * 60)["brief:intro"] == "STALE")
        run["jobs"]["brief:intro"]["ended"] = now
        check("ended, output not here: READY again (a limit hit or an unsynced lane never hides)",
              states(ep, run, now)["brief:intro"] == "READY")
        run["holds"] = {"brief:intro": {"reason": "owner gate", "at": now}}
        check("live hold wins over READY", states(ep, run, now)["brief:intro"] == "HELD")
        check("a hold lapses after HOLD_H: READY again", states(ep, run, now + lanes.HOLD_H * 3600)["brief:intro"] == "READY")

        e = str(ep)
        check("claim without a session id fails", raises(lambda: lanes.main(["claim", e, "--session", ""]))
              and not (ep / "lanes.json").exists())
        outside = Path(tmp) / "episodes" / "ep-out"
        touch(outside / "edit_script.md", SCRIPT)
        check("claim refuses an episode outside this checkout", raises(lambda: lanes.main(["claim", str(outside), "--session", "S1"])))
        real, lanes.SCRIPTS = lanes.SCRIPTS, Path(tmp) / "scripts"  # pretend tmp is a main checkout
        check("claim refuses an episode outside .worktrees (the hook never reads it)",
              raises(lambda: lanes.main(["claim", str(outside), "--session", "S1"])) and not (outside / "lanes.json").exists())
        lanes.SCRIPTS = real
        check("claim records the session", lanes.main(["claim", e, "--session", "S1"]) == 0
              and json.loads((ep / "lanes.json").read_text())["orchestrator"] == "S1")
        check("start rejects an unknown job", raises(lambda: lanes.main(["start", e, "brief:nope", "--session", "S1"])))
        check("start rejects --minutes past HOLD_H (a lane cannot read RUNNING for days)",
              raises(lambda: lanes.main(["start", e, "source:intro", "--minutes", str(lanes.HOLD_H * 60 + 1), "--session", "S1"])))
        check("hold rejects a blank reason", raises(lambda: lanes.main(["hold", e, "voice:intro", "--reason", " ", "--session", "S1"])))
        lanes.main(["start", e, "source:intro", "--session", "S2"])
        check("only claim stamps the orchestrator: a sibling's start never takes the gate",
              json.loads((ep / "lanes.json").read_text())["orchestrator"] == "S1")
        lanes.main(["end", e, "source:intro", "--session", "S2"])
        check("end marks the lane stopped: READY again while its output is missing",
              states(ep, lanes.load_ledger(ep))["source:intro"] == "READY")
        lanes.main(["hold", e, "source:intro", "--reason", "owner", "--session", "S2"])
        lanes.main(["unhold", e, "source:intro", "--session", "S2"])
        check("unhold clears the hold", states(ep, lanes.load_ledger(ep))["source:intro"] == "READY")
        check("status exits 2 while a job is READY", lanes.main(["status", e]) == 2)
        lanes.main(["hold", e, "all", "--reason", "fixture", "--session", "S2"])
        check("status exits 0 once every ready job is held", lanes.main(["status", e]) == 0)
    finally:
        import shutil
        shutil.rmtree(fx, ignore_errors=True)

if FAILS:
    sys.exit(f"[test_lanes] FAIL: {FAILS}")
print("[test_lanes] all checks passed")
