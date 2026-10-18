"""Self-check for scripts/lanes.py: python3 scripts/test_lanes.py

Builds throwaway episode fixtures in a temp dir. Each case proves a job reaches the state the gate relies on;
a READY job that reads DONE, or a dead lane that reads RUNNING, is exactly the idle-lane failure this guards.
"""
import json
import os
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import lanes  # noqa: E402


def never(*a):
    raise AssertionError(f"a test reached a real host call {a}")


# no test ever probes claude, reads a host or launches a lane: each test that needs one installs its own fake
REAL_PROBE, REAL_SPAWN = lanes.probe, lanes.spawn
lanes.probe = lanes.spawn = lanes.read_log = never
lanes.free_gb = lambda host: 64.0
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


# --- launch path: the three capacity rules, run by pytest or by this script ---
LANE = ["--host", "zbook", "--cmd", "type b.md | {cli} -p --model opus", "--log", r"C:\x\lane.log", "--cwd", r"C:\wt"]
# real probe replies, captured on the ZBook 18 Oct 26 02:08 by `claude -p 'reply with the single word ok' --model haiku`
CLAUDE1_REPLY = "You've hit your session limit · resets 4:10am (Asia/Kolkata)"
CLAUDE2_REPLY = "ok"
LIMIT_LOG = '{"type":"result","is_error":true,"result":"You\'ve hit your session limit · resets 3pm"}'


def lane_episode(tmp):
    ep = Path(tmp) / "ep"
    touch(ep / "edit_script.md", SCRIPT)
    lanes.ACCOUNTS = Path(tmp) / "accounts"
    for p in ("claude1", "claude2", "claude5", "design"):  # design is no claude* profile: never probed
        (lanes.ACCOUNTS / p).mkdir(parents=True)
    return ep


def fakes(answering, free=16.0, log=""):
    calls = {"probe": [], "spawn": []}
    lanes.probe = lambda host, p: calls["probe"].append(p) or p in answering
    lanes.spawn = lambda host, cmd, log_path, cwd: calls["spawn"].append((host, cmd, log_path, cwd))
    lanes.free_gb = lambda host: free
    lanes.read_log = lambda host, path: log
    return calls


def real_probe_replying(replies):
    """The real probe parser, fed the captured reply of the profile named in its script (exit 0 even on a limit)."""
    asked = []

    def ps(host, script, timeout=90):
        p = next(p for p in replies if f"claude-accounts\\{p}" in script)
        asked.append(p)
        return 0, replies[p] + "\n"
    lanes.probe, lanes.ps = REAL_PROBE, ps
    return asked


def test_rule1_start_skips_a_profile_that_does_not_answer(tmp_path):
    ep = lane_episode(tmp_path)
    calls = fakes(answering=set())
    asked = real_probe_replying({"claude1": CLAUDE1_REPLY, "claude2": CLAUDE2_REPLY, "claude5": CLAUDE2_REPLY})
    assert lanes.main(["start", str(ep), "source:a1", "--profile", "claude1", *LANE]) == 0
    assert asked == ["claude1", "claude2"]
    assert calls["spawn"] == [("zbook", "type b.md | claude2 -p --model opus", r"C:\x\lane.log", r"C:\wt")]
    assert lanes.load_ledger(ep)["jobs"]["source:a1"]["profile"] == "claude2"
    calls = fakes(answering={"claude5"})
    assert raises(lambda: lanes.main(["start", str(ep), "source:a1", *LANE])) and not calls["spawn"]  # already RUNNING
    calls = fakes(answering=set())
    assert raises(lambda: lanes.main(["start", str(ep), "voice:a1", *LANE])) and not calls["spawn"]


def test_an_ssh_drop_after_a_good_launch_never_launches_twice(tmp_path):
    """p4 ran twice on 18 Oct 26: ssh dropped after the Create had run, and the launcher retried."""
    drop = (255, "Read from remote host 100.102.121.75: Connection reset by peer")
    log = r"C:\x\lane[a1].log"  # "[" is a wildcard to PowerShell's -like: such a query reads a running lane as dead
    lane = LANE[:5] + [log] + LANE[6:]
    for i, (asked, recorded) in enumerate((((0, "1\n"), True), (drop, True), ((0, "0\n"), False))):
        ep, creates = lane_episode(tmp_path / str(i)), []

        def ps(host, script, timeout=90):
            if "-MethodName Create" in script:
                creates.append(host)
                return drop  # the Create ran on the host, then the session dropped before its reply
            # the liveness query: lane seen running, host unreadable, lane not running; only a literal match finds it
            return asked if f".Contains({lanes.quote(log)})" in script else (0, "0\n")
        fakes(answering={"claude2"})
        lanes.spawn, lanes.ps = REAL_SPAWN, ps
        assert raises(lambda: lanes.main(["start", str(ep), "source:a1", *lane])) != recorded
        assert ("source:a1" in lanes.load_ledger(ep).get("jobs", {})) == recorded
        if recorded:  # a second start, the retry that doubled p4, refuses before any Create
            assert raises(lambda: lanes.main(["start", str(ep), "source:a1", *lane])) and creates == ["zbook"]

    # local has no ssh to drop, and a query there would find the lanes.py process itself: a failed Create is a FAIL
    ep = lane_episode(tmp_path / "local")
    lanes.ps = lambda host, script, timeout=90: (124, "timed out after 90s") if "-MethodName Create" in script else never(script)
    assert raises(lambda: lanes.main(["start", str(ep), "source:a1", "--cmd", "{cli} -p", "--log", log]))
    assert "source:a1" not in lanes.load_ledger(ep).get("jobs", {})


def test_a_recorded_launch_whose_log_never_appears_fails(tmp_path):
    """the host-unreadable case records RUNNING; a lane that never started must not sit RUNNING until STALE"""
    ep = lane_episode(tmp_path)
    fakes(answering=set(), log=lanes.NO_LOG)
    for minutes_ago, state in ((1, "RUNNING"), (lanes.NO_LOG_MIN + 1, "FAILED")):
        run = {"started": time.time() - minutes_ago * 60, "host": "zbook", "minutes": 60, "log": r"C:\x\lane.log"}
        st = {s["job"]: s["state"] for s in lanes.job_states(ep, {"jobs": {"source:a1": run}})}
        assert st["source:a1"] == state, (minutes_ago, st["source:a1"])


def test_rule2_start_refuses_low_memory_and_a_full_lane_count(tmp_path):
    ep = lane_episode(tmp_path)
    calls = fakes(answering={"claude1"}, free=lanes.MIN_FREE_GB)
    assert raises(lambda: lanes.main(["start", str(ep), "source:a1", *LANE])) and not calls["spawn"]
    now = time.time()
    four = ("source:a1", "source:intro", "voice:a1", "voice:intro")
    lanes.save_ledger(ep, {"jobs": {j: {"started": now, "host": "zbook"} for j in four}})
    calls = fakes(answering={"claude1"}, free=lanes.MIN_FREE_GB + 0.1)
    assert raises(lambda: lanes.main(["start", str(ep), "words:a1", *LANE])) and not calls["spawn"]
    lanes.save_ledger(ep, {"jobs": {j: {"started": now, "host": "zbook"} for j in four[:3]}})
    assert lanes.main(["start", str(ep), "words:a1", *LANE]) == 0 and len(calls["spawn"]) == 1


def limited_lane(tmp):
    ep = lane_episode(tmp)
    run = {"started": time.time() - 60, "host": "zbook", "minutes": 60, "cmd": "type b.md | {cli} -p",
           "log": r"C:\x\lane.log", "cwd": r"C:\wt", "profile": "claude1"}
    lanes.save_ledger(ep, {"jobs": {"source:a1": run}})
    return ep, run


def test_status_launches_nothing_even_with_a_limited_lane(tmp_path):
    ep, run = limited_lane(tmp_path)
    calls = fakes(answering={"claude1", "claude2", "claude5"}, log=LIMIT_LOG)
    assert lanes.main(["status", str(ep)]) == 2 and lanes.main(["status", str(ep), "--json"]) == 2
    assert not (ep / "lanes.json.lock").exists() and not calls["probe"] and not calls["spawn"] and lanes.load_ledger(ep)["jobs"]["source:a1"] == run


def test_relaunch_backs_off_while_another_holds_the_lock(tmp_path):
    ep, run = limited_lane(tmp_path)
    calls = fakes(answering={"claude2"}, log=LIMIT_LOG)
    lock = ep / "lanes.json.lock"
    lock.touch()
    assert lanes.main(["relaunch", str(ep)]) == 0 and not calls["spawn"] and lock.exists()
    lanes.LOCK_WAIT_S = 0  # a start meanwhile must not write the ledger it read before the holder saved
    assert raises(lambda: lanes.main(["start", str(ep), "words:a1", *LANE])) and not calls["spawn"]
    assert lanes.load_ledger(ep)["jobs"] == {"source:a1": run}
    old = time.time() - lanes.LOCK_MIN * 60 - 1
    os.utime(lock, (old, old))  # a dead relaunch's lock is taken over
    assert lanes.main(["relaunch", str(ep)]) == 0 and len(calls["spawn"]) == 1 and not lock.exists()


def test_rule3_relaunch_moves_a_limited_lane_to_the_next_profile(tmp_path):
    ep, run = limited_lane(tmp_path)
    calls = fakes(answering=set(), log=LIMIT_LOG)
    st = {s["job"]: s["state"] for s in lanes.job_states(ep, lanes.load_ledger(ep))}
    assert st["source:a1"] == "FAILED" and "FAILED" in lanes.BLOCKING
    assert lanes.main(["relaunch", str(ep)]) == 2 and not calls["spawn"]  # nobody answers: it stays FAILED
    calls = fakes(answering={"claude1", "claude5"}, log=LIMIT_LOG)
    assert lanes.main(["relaunch", str(ep)]) == 0
    assert calls["probe"] == ["claude2", "claude5"]  # never back onto the profile that hit its limit
    assert calls["spawn"] == [("zbook", "type b.md | claude5 -p", r"C:\x\lane.log", r"C:\wt")]
    new = lanes.load_ledger(ep)["jobs"]["source:a1"]
    assert new["profile"] == "claude5" and new["started"] > run["started"]


if __name__ == "__main__":
    for t in (test_rule1_start_skips_a_profile_that_does_not_answer,
              test_an_ssh_drop_after_a_good_launch_never_launches_twice,
              test_rule2_start_refuses_low_memory_and_a_full_lane_count,
              test_status_launches_nothing_even_with_a_limited_lane,
              test_relaunch_backs_off_while_another_holds_the_lock,
              test_rule3_relaunch_moves_a_limited_lane_to_the_next_profile):
        with tempfile.TemporaryDirectory() as d:
            try:
                t(Path(d))
                check(t.__name__, True)
            except AssertionError:
                check(t.__name__, False)

if FAILS:
    sys.exit(f"[test_lanes] FAIL: {FAILS}")
print("[test_lanes] all checks passed")
