"""Self-check for scripts/lanes.py: python3 scripts/test_lanes.py

Builds throwaway episode fixtures in a temp dir. Each case proves a job reaches the state the gate relies on;
a READY job that reads DONE, or a dead lane that reads RUNNING, is exactly the idle-lane failure this guards.
"""
import contextlib
import io
import json
import os
import socket
import subprocess
import threading
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
REAL_PROBE, REAL_SPAWN, REAL_PS = lanes.probe, lanes.spawn, lanes.ps
REAL_PROFILES, REAL_READ_LANE = lanes.profiles, lanes.read_lane
lanes.probe = lanes.spawn = lanes.read_lane = lanes.ps = never
lanes.free_gb = lambda host: 64.0
socket.gethostname = lambda: "TESTBOX"  # neither laptop: zbook and asus are remote hosts in every test that does not say otherwise
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
        # L8: a shared pool (cta, shared) can never be "run": it shows, but never blocks the Stop gate
        check("a folder matching no group is reported, BLOCKED (never READY)", states(ep).get("orphan:briefs/zz") == "BLOCKED")
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
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            lanes.main(["claim", e, "--session", "S1"])
        check("L12: a re-claim by the same session says nothing about a takeover", "takes over" not in said.getvalue())
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            lanes.main(["claim", e, "--session", "S9"])
        check("L12: a second session's claim names the session it took the episode from",
              "takes over from session S1" in said.getvalue())
        lanes.main(["claim", e, "--session", "S1"])
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
    lanes.profiles = lambda host: ["claude1", "claude2", "claude5"]  # the profiles that can run on the host (test_l1 reads real ones)
    return ep


def fakes(answering, free=16.0, log="", running=True):
    calls = {"probe": [], "spawn": []}
    lanes.probe = lambda host, p: calls["probe"].append(p) or p in answering
    lanes.spawn = lambda host, cmd, log_path, cwd: calls["spawn"].append((host, cmd, log_path, cwd))
    lanes.free_gb = lambda host: free
    lanes.read_lane = lambda host, path: (running, log)
    return calls


def real_probe_replying(replies, listing=None):
    """The real probe parser, fed the captured reply of the profile whose wrapper its script runs (exit 0 even on a
    limit). A script that is no probe (the profile listing) runs for real on this machine when listing allows it."""
    asked = []

    def ps(host, script, timeout=90):
        if "reply with the single word ok" not in script:
            return REAL_PS("local", script) if listing else never(script)
        p = next(p for p in replies if f"& {p} -p " in script)
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
            return asked if f".EndsWith({lanes.quote(lanes.redirect(log) + chr(34))})" in script else (0, "0\n")
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


def test_alive_finds_the_lane_root_never_a_command_that_mentions_its_log(tmp_path):
    """29 Oct 26: alive() matched any command line holding the log path, so a shell or python -c that only mentioned it
    read as a running lane. Real processes, real alive(); NO_WINDOW decoys."""
    lanes.ps, lanes.spawn = REAL_PS, REAL_SPAWN
    real, other = str(tmp_path / "real.log"), str(tmp_path / "other.log")
    # decoy 1 is a str command line: the redirect reaches cmd.exe verbatim, exactly what the old kill() matched
    decoys = [subprocess.Popen(f"cmd /c ping -n 40 127.0.0.1 > nul & rem {lanes.redirect(other)}", creationflags=lanes.NO_WINDOW),
              subprocess.Popen([sys.executable, "-c", f"import time; time.sleep(40)  # {lanes.redirect(other)} {other}"], creationflags=lanes.NO_WINDOW)]
    try:
        lanes.spawn("local", "ping -n 40 127.0.0.1", real, str(tmp_path))
        time.sleep(2)
        assert lanes.alive("local", real) is True  # the lane root spawn() started
        assert lanes.alive("local", other) is False  # only decoys that mention the log
        assert lanes.kill("local", other) == 0  # kill() uses the same exact root match: a decoy cmd.exe is not taskkill'd
        assert all(d.poll() is None for d in decoys)
    finally:
        lanes.kill("local", real)
        lanes.ps, lanes.spawn = never, never  # the tests after this one never reach a real host
        for d in decoys:
            d.kill()


def test_rule2_start_refuses_low_memory_and_never_counts_lanes(tmp_path):
    """no lane-count cap (owner 13 Oct 26: agents run on the API, not on local cores); only the RAM floor refuses"""
    ep = lane_episode(tmp_path)
    calls = fakes(answering={"claude1"}, free=lanes.MIN_FREE_GB)
    assert raises(lambda: lanes.main(["start", str(ep), "source:a1", *LANE])) and not calls["spawn"]
    now = time.time()
    six = ("source:a1", "source:intro", "voice:a1", "voice:intro", "source:a2", "voice:a2")
    lanes.save_ledger(ep, {"jobs": {j: {"started": now, "host": "zbook"} for j in six}})
    calls = fakes(answering={"claude1"}, free=lanes.MIN_FREE_GB + 0.1)
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


def test_stop_all_ends_every_running_lane_by_its_log(tmp_path):
    """Owner 27 Oct 26 asked for one stop-all; a lane is found the way alive() finds it, by its log path."""
    ep = lane_episode(tmp_path)
    fakes(answering={"claude1"})
    assert lanes.main(["start", str(ep), "source:a1", *LANE]) == 0
    assert lanes.main(["start", str(ep), "voice:a1", "--host", "zbook"]) == 0  # recorded only: no log to find it by
    killed = []
    lanes.ps = lambda host, script, timeout=90: (killed.append((host, script)) or (0, "noise\n2\n"))
    try:
        assert lanes.main(["stop", str(ep), "all"]) == 0
    finally:
        lanes.ps = never
    assert len(killed) == 1 and killed[0][0] == "zbook" and "taskkill /T /F" in killed[0][1]
    assert """'> "C:\\x\\lane.log" 2>&1"'""" in killed[0][1] and "StartsWith('cmd /s /c" in killed[0][1] and "$_.Name -eq 'cmd.exe'" in killed[0][1]  # only the lane's root
    jobs = lanes.load_ledger(ep)["jobs"]
    assert "ended" in jobs["source:a1"] and "ended" not in jobs["voice:a1"]  # unfindable: never marked as stopped
    # an unreachable host: nothing marked ended, so the Stop gate never relaunches a lane that may still run
    assert lanes.main(["start", str(ep), "source:intro", *LANE]) == 0
    lanes.ps = lambda host, script, timeout=90: (255, "Connection reset by peer")
    try:
        lanes.main(["stop", str(ep), "source:intro"])
    finally:
        lanes.ps = never
    assert "ended" not in lanes.load_ledger(ep)["jobs"]["source:intro"]


def test_l1_a_profile_is_probed_on_its_wrapper_and_only_profiles_with_a_credential_are_tried(tmp_path):
    """L1 (11 Nov 26): the rotation listed ~/.claude-accounts and probed claude.exe under CLAUDE_CONFIG_DIR, while the
    lane ran the claudeN wrapper on its token, so claude3 (a token, no accounts folder) was never tried. The listing
    runs for real (PowerShell on this machine) over a fake %USERPROFILE%; only the probe replies are fakes."""
    ep = lane_episode(tmp_path)
    lanes.profiles = REAL_PROFILES
    home = tmp_path / "home"
    for p in ("claude1", "claude3", "claude4", "claude6", "claude-token"):  # the wrappers in %USERPROFILE%\bin
        touch(home / "bin" / f"{p}.cmd")
    touch(home / ".claude-tokens" / "claude1")
    touch(home / ".claude-tokens" / "claude3")  # a token and no accounts folder: probed and used
    touch(home / ".claude-accounts" / "claude6" / ".credentials.json")  # a wrapper run on a login folder
    (home / ".claude-accounts" / "claude2").mkdir(parents=True)  # a folder, no wrapper, no credential
    # claude4: a wrapper with neither a token nor a login folder; claude-token is a helper: neither is ever probed
    calls = fakes(answering=set())
    asked = real_probe_replying({"claude1": CLAUDE1_REPLY, "claude3": CLAUDE2_REPLY, "claude6": CLAUDE2_REPLY}, listing=True)
    old, os.environ["USERPROFILE"] = os.environ["USERPROFILE"], str(home)
    try:
        assert lanes.main(["start", str(ep), "source:a1", *LANE]) == 0
        assert lanes.profiles("zbook") == ["claude1", "claude3", "claude6"]
    finally:
        os.environ["USERPROFILE"] = old
    assert asked == ["claude1", "claude3"], asked  # claude1 at its limit, claude3 answers
    assert calls["spawn"] == [("zbook", "type b.md | claude3 -p --model opus", r"C:\x\lane.log", r"C:\wt")]
    assert lanes.load_ledger(ep)["jobs"]["source:a1"]["profile"] == "claude3"


def test_l3_a_host_alias_that_names_this_machine_is_local(tmp_path):
    """L3: on the ZBook, `zbook` is this machine (no ssh to itself) and the ASUS is `asus`; on the ASUS the reverse."""
    argv, real_run, real_name = [], subprocess.run, socket.gethostname
    subprocess.run = lambda a, **k: argv.append(a) or subprocess.CompletedProcess(a, 0, "1", "")
    try:
        for me, mine, other in (("Sidhartha", "zbook", "asus"), ("SPTL-184", "asus", "zbook")):
            socket.gethostname = lambda: me
            argv.clear()
            for h in ("local", mine, other):
                REAL_PS(h, "1")
            assert [a[0] for a in argv] == ["powershell", "powershell", "ssh"] and other in argv[2], (me, argv)
    finally:
        subprocess.run, socket.gethostname = real_run, real_name
    ep = lane_episode(tmp_path)
    assert lanes.main(["status", str(ep), "--host", "asus"]) == 2  # the other laptop is a host name argparse accepts
    socket.gethostname = lambda: "SIDHARTHA"
    calls = fakes(answering={"claude1"})
    try:  # a lane on zbook from the ZBook is local: no --cwd needed, it starts in this checkout
        assert lanes.main(["start", str(ep), "source:a1", "--host", "zbook", "--cmd", "{cli} -p", "--log", r"C:\x\l.log"]) == 0
    finally:
        socket.gethostname = real_name
    assert calls["spawn"] == [("zbook", "claude1 -p", r"C:\x\l.log", str(lanes.SCRIPTS.parent))]


def test_l4_a_lane_whose_process_died_is_not_running(tmp_path):
    """L4: status read only the log tail, so a crashed lane read RUNNING until its minutes ran out. One call per lane
    reads the root process and the tail (the Stop hook's 120 s); an unreadable host is unknown, never dead."""
    ep = lane_episode(tmp_path)
    fakes(answering=set())
    lanes.read_lane = REAL_READ_LANE
    scripts = []
    run = {"started": time.time() - 60, "host": "asus", "minutes": 60, "log": r"C:\x\lane.log", "profile": "claude1"}
    for answer, state, note in (((0, "0\nTraceback: boom\n"), "READY", "exited"),
                                ((0, "1\nworking\n"), "RUNNING", "on asus"),
                                ((255, "ssh: connect to host asus port 22: Connection timed out"), "RUNNING", "unreadable"),
                                ((0, f"0\n{lanes.NO_LOG}\n"), "RUNNING", "on asus")):  # no log yet: the NO_LOG_MIN grace rules
        lanes.ps = lambda host, script, timeout=90: scripts.append((script, timeout)) or answer
        s = next(s for s in lanes.job_states(ep, {"jobs": {"source:a1": dict(run)}}) if s["job"] == "source:a1")
        assert s["state"] == state and note in s["note"], (answer, s)
    lanes.ps = never
    assert all("Get-CimInstance Win32_Process" in sc and "Get-Content -Tail" in sc and t <= 20 for sc, t in scripts), scripts


def test_l5_a_ledger_save_waits_out_a_reader_holding_the_file(tmp_path):
    """L5: os.replace fails (WinError 5) while a status run has lanes.json open, and `start --cmd` saves after the lane
    is already running, so the lane went unrecorded. A reader holds it for ms; here one holds it 1 s."""
    ep = lane_episode(tmp_path)
    lanes.save_ledger(ep, {"jobs": {}})
    f = open(ep / "lanes.json", encoding="utf-8")
    threading.Timer(1.0, f.close).start()
    try:
        lanes.save_ledger(ep, {"jobs": {"source:a1": {"started": 1}}})
    finally:
        time.sleep(1.2)  # the timer has closed it either way
    assert lanes.load_ledger(ep)["jobs"] == {"source:a1": {"started": 1}}


def test_l6_a_shipped_episode_has_no_jobs_and_exits_0(tmp_path):
    """L6: a shipped episode read from a checkout without its audio listed READY voice and source jobs and exited 2.
    Shipped is stage.shipped: an E number plus the final master in the main checkout (a worktree's own copy is no proof)."""
    import stage
    ep = lane_episode(tmp_path)
    main = tmp_path / "main"
    real, stage.checkouts = stage.checkouts, lambda: [(main, "main", "")]
    try:
        assert lanes.main(["status", str(ep)]) == 2  # no E number yet: its jobs are READY
        touch(ep / "E10-fixture-metadata.md")
        assert lanes.main(["status", str(ep)]) == 2  # numbered, not shipped
        touch(ep / "renders" / "E10-fixture-final-master.mp4")
        assert lanes.main(["status", str(ep)]) == 2  # a master only in this worktree is not the shipped one
        touch(main / "episodes" / ep.name / "renders" / "E10-fixture-final-master.mp4")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            assert lanes.main(["status", str(ep)]) == 0
        assert out.getvalue().count("\n") == 1 and "shipped" in out.getvalue() and "READY" not in out.getvalue()
        with contextlib.redirect_stdout(out := io.StringIO()):
            assert lanes.main(["status", str(ep), "--json"]) == 0
        assert json.loads(out.getvalue())["blocking"] == []
    finally:
        stage.checkouts = real


def test_l11_a_launch_starts_on_the_least_loaded_profile_across_episodes(tmp_path):
    """L11: every lane of every episode started on the first profile, so concurrent episodes piled onto claude1.
    Two worktrees: ep1 runs two lanes on claude1 and one on claude2 (an ended lane, a lapsed lane and a lane with no
    profile count nothing); a launch from ep2 must probe claude5 first, then claude2, then claude1; --profile still leads."""
    now = time.time()
    root = tmp_path / "repo"
    ep1, ep2 = (root / ".worktrees" / w / "episodes" / "ep" for w in ("wt1", "wt2"))
    for ep in (ep1, ep2):
        touch(ep / "edit_script.md", SCRIPT)
    run = lambda p, **k: {"started": now - 60, "host": "zbook", "minutes": 60, "profile": p, **k}  # noqa: E731
    lanes.save_ledger(ep1, {"jobs": {"source:a1": run("claude1"), "source:intro": run("claude1"), "words:a1": run("claude2"),
                                     "voice:a1": run("claude5", ended=now), "voice:intro": run("claude5", started=now - 7200),
                                     "brief:a1": {"started": now - 60, "host": "asus"}}})
    lanes.profiles = lambda host: ["claude1", "claude2", "claude5"]
    assert lanes.running_load(ep2, now) == {"claude1": 2, "claude2": 1}
    calls = fakes(answering={"claude1", "claude2", "claude5"})
    assert lanes.main(["start", str(ep2), "source:a1", *LANE]) == 0
    assert calls["probe"] == ["claude5"] and lanes.load_ledger(ep2)["jobs"]["source:a1"]["profile"] == "claude5"
    calls = fakes(answering={"claude1"})  # the ledger now holds claude5 once: claude2 and claude5 tie at 1, name order breaks it
    assert lanes.main(["start", str(ep2), "words:a1", *LANE[:-2], "--cwd", r"C:\wt"]) == 0
    assert calls["probe"] == ["claude2", "claude5", "claude1"], calls["probe"]
    calls = fakes(answering={"claude1", "claude2", "claude5"})
    assert lanes.main(["start", str(ep2), "voice:a1", "--profile", "claude1", *LANE]) == 0 and calls["probe"] == ["claude1"]


if __name__ == "__main__":
    for t in (test_l11_a_launch_starts_on_the_least_loaded_profile_across_episodes,
              test_l6_a_shipped_episode_has_no_jobs_and_exits_0,
              test_l1_a_profile_is_probed_on_its_wrapper_and_only_profiles_with_a_credential_are_tried,
              test_l3_a_host_alias_that_names_this_machine_is_local,
              test_l4_a_lane_whose_process_died_is_not_running,
              test_l5_a_ledger_save_waits_out_a_reader_holding_the_file,
              test_stop_all_ends_every_running_lane_by_its_log,
              test_rule1_start_skips_a_profile_that_does_not_answer,
              test_an_ssh_drop_after_a_good_launch_never_launches_twice,
              test_a_recorded_launch_whose_log_never_appears_fails,
              test_alive_finds_the_lane_root_never_a_command_that_mentions_its_log,
              test_rule2_start_refuses_low_memory_and_never_counts_lanes,
              test_status_launches_nothing_even_with_a_limited_lane,
              test_relaunch_backs_off_while_another_holds_the_lock,
              test_rule3_relaunch_moves_a_limited_lane_to_the_next_profile):
        with tempfile.TemporaryDirectory() as d:
            try:
                t(Path(d))
                check(t.__name__, True)
            except Exception as e:  # a crash is a FAIL too, never an abort that hides the tests after it
                print(f"     {type(e).__name__}: {str(e)[:300]}")
                check(t.__name__, False)

if FAILS:
    sys.exit(f"[test_lanes] FAIL: {FAILS}")
print("[test_lanes] all checks passed")
