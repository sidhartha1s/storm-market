"""Self-check for scripts/snapshot_queue.py: python3 scripts/test_snapshot_queue.py

Builders submit without a browser; one worker runs one snapshot at a time, batching every pending job for one episode; a second worker refuses;
only the files the timeline names are shipped, and only once until they change. No browser, no ssh.
"""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import snapshot_queue as q  # noqa: E402

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    q.SPOOL = d / ".snapq"
    q.SETTLE = 0
    ep = d / "episodes" / "ep-x"
    (ep / "compositions").mkdir(parents=True)
    (ep / "media" / "stills").mkdir(parents=True)
    ep = ep.resolve()
    (ep / "index.html").write_text('<script src="gsap.min.js"></script><div data-composition-src="compositions/g-a.html"></div>'
                                   '<video src="media/clip.mp4"></video><img src="https://x.org/y.png">', encoding="utf-8")
    (ep / "gsap.min.js").write_text("//", encoding="utf-8")
    (ep / "media" / "clip.mp4").write_bytes(b"0")
    (ep / "media" / "unused.mp4").write_bytes(b"0")
    (ep / "media" / "stills" / "a.jpg").write_bytes(b"0")
    (ep / "compositions" / "g-a.html").write_text('<img src="../media/stills/a.jpg"><div style="background:url(media/missing.png)">',
                                                  encoding="utf-8")

    # submit opens no browser and only writes a job file
    q.submit(str(ep), "1.5,6", "g-a")
    q.submit(str(ep), "2", "")
    jobs = sorted((q.SPOOL / "pending").glob("*.json"))
    assert len(jobs) == 2 and json.loads(jobs[0].read_text())["at"] == [1.5, 6.0], jobs

    # the worker runs one snapshot at a time, oldest first; every pending job for one episode folder rides one run
    # (the union of their times, deduped), and each job gets back only its own frames, numbered from 00
    ep2 = d / "episodes" / "ep-y"
    ep2.mkdir()
    (ep2 / "index.html").write_text("<div></div>", encoding="utf-8")
    ep2 = ep2.resolve()
    q.submit(str(ep2), "9", "other-ep")
    q.submit(str(ep), "6,7", "same-ep-later")
    live, peak, runs = [0], [0], []

    def fake_snap(e, times, pin, name, out):
        live[0] += 1
        peak[0] = max(peak[0], live[0])
        runs.append((Path(e).name, times))
        for i, t in enumerate(times):
            (Path(out) / f"frame-{i:02d}-at-{t:g}s.png").write_bytes(f"{i}:{t}".encode())
        time.sleep(0.05)
        live[0] -= 1
        return 0, "ok"

    q.snap_local = fake_snap
    q.run("local")
    assert peak[0] == 1 and runs == [("ep-x", [1.5, 2.0, 6.0, 7.0]), ("ep-y", [9.0])], (peak, runs)
    assert not list((q.SPOOL / "pending").glob("*.json"))
    res = {(f.stem.split("-", 1) + ["unlabeled"])[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json")}
    assert set(res) == {"g-a", "unlabeled", "same-ep-later", "other-ep"}, res
    assert [Path(x).name for x in res["unlabeled"]["pngs"]] == ["frame-00-at-2s.png"], res["unlabeled"]
    first = res["g-a"]
    assert first["rc"] == 0 and [Path(x).name for x in first["pngs"]] == ["frame-00-at-1.5s.png", "frame-01-at-6s.png"], first
    assert Path(first["pngs"][1]).read_bytes() == b"2:6.0", "a job got another job's frame"
    later = res["same-ep-later"]
    assert [Path(x).name for x in later["pngs"]] == ["frame-00-at-6s.png", "frame-01-at-7s.png"] and "batch of 3 job(s), 4 frame(s)" in later["log"], later
    assert res["other-ep"]["rc"] == 0 and len(res["other-ep"]["pngs"]) == 1, res["other-ep"]

    # a seek-order job (times go back and repeat) runs alone in its own order on a fresh page; forward jobs still batch
    q.submit(str(ep), "8,9", "fwd-a")
    q.submit(str(ep), "5,0,7,5", "seek")
    q.submit(str(ep), "1", "fwd-b")
    runs.clear()
    q.run("local")
    assert runs == [("ep-x", [1.0, 8.0, 9.0]), ("ep-x", [5.0, 0.0, 7.0, 5.0])], runs
    seek = json.loads(next((q.SPOOL / "done").glob("*-seek.json")).read_text())
    assert [Path(x).read_bytes() for x in seek["pngs"]] == [b"0:5.0", b"1:0.0", b"2:7.0", b"3:5.0"], seek

    # a job whose PNG dir cannot be made is its own rc 1; the worker carries on
    (d / "blocker").write_text("a file, not a dir", encoding="utf-8")
    q.submit(str(ep), "3", "badout")
    bad = next((q.SPOOL / "pending").glob("*-badout.json"))
    bad.write_text(json.dumps({**json.loads(bad.read_text()), "out": str(d / "blocker" / "x")}), encoding="utf-8")
    q.submit(str(ep2), "4", "fine")
    q.run("local")
    res = {f.stem.split("-", 1)[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json") if "-" in f.stem}
    assert res["badout"]["rc"] == 1 and "Error" in res["badout"]["log"] and res["fine"]["rc"] == 0, (res["badout"], res["fine"])

    # exit 0 with a frame missing is a failed job, not a pass
    q.submit(str(ep), "3", "empty")
    q.snap_local = lambda e, times, pin, name, out: (0, "ok")
    q.run("local")
    rec = json.loads(sorted((q.SPOOL / "done").glob("*empty.json"))[0].read_text())
    assert rec["rc"] == 1 and "0 of 1 PNG(s)" in rec["log"], rec

    # a second worker refuses while one holds the lock
    holder = subprocess.Popen([sys.executable, "-c",
                               "import msvcrt,sys,time;f=open(sys.argv[1],'a');msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1);print('held',flush=True);time.sleep(30)",
                               str(q.SPOOL / "worker.lock")], stdout=subprocess.PIPE, text=True)
    assert holder.stdout.readline().strip() == "held"
    try:
        q.run("local")
        raise AssertionError("second worker should refuse")
    except SystemExit as e:
        assert "already running" in str(e), e
    finally:
        holder.kill()
        holder.wait()

    # only referenced files that exist in the episode: comp, its still (../media), the clip, gsap; no unused media, no URLs
    got = {f.relative_to(ep).as_posix() for f in q.referenced(ep)}
    assert got == {"index.html", "gsap.min.js", "compositions/g-a.html", "media/clip.mp4", "media/stills/a.jpg"}, got

    # ship sends only what changed since the last ship
    calls = []
    q.ssh = lambda cmd, timeout: (calls.append(cmd), subprocess.CompletedProcess(cmd, 0, "", ""))[1]
    real_run = subprocess.run
    q.subprocess.run = lambda cmd, **k: (calls.append(cmd), subprocess.CompletedProcess(cmd, 0))[1] if cmd[0] == "scp" else real_run(cmd, **k)
    assert q.ship(ep) == (5, 5)
    assert q.ship(ep) == (0, 5)
    time.sleep(0.02)
    (ep / "compositions" / "g-a.html").write_text('<img src="../media/stills/a.jpg">changed', encoding="utf-8")
    assert q.ship(ep) == (1, 5)
    q.subprocess.run = real_run

    # a corrupt job file and a job that raises are each recorded as rc 1; the job after them still runs
    (q.SPOOL / "pending" / "0000000000000000001-bad.json").write_text('{"ep": ', encoding="utf-8")
    q.submit(str(ep), "4", "raises")
    q.submit(str(ep2), "5", "after")
    q.snap_local = lambda e, times, pin, name, out: (_ for _ in ()).throw(ValueError("boom")) if times == [4.0] else fake_snap(e, times, pin, name, out)
    q.run("local")
    res = {f.stem.split("-", 1)[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json") if "-" in f.stem}
    assert res["bad"]["rc"] == 1 and "JSONDecodeError" in res["bad"]["log"], res["bad"]
    assert res["raises"]["rc"] == 1 and "boom" in res["raises"]["log"], res["raises"]
    assert res["after"]["rc"] == 0 and len(res["after"]["pngs"]) == 1, res["after"]

    # one builder's bad time fails the batch run; each job then runs alone, so only the bad job fails
    q.submit(str(ep), "8", "good")
    q.submit(str(ep), "99", "badtime")
    runs.clear()
    q.snap_local = lambda e, times, pin, name, out: (1, "past the end") if 99.0 in times else fake_snap(e, times, pin, name, out)
    q.run("local")
    res = {f.stem.split("-", 1)[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json") if "-" in f.stem}
    assert res["good"]["rc"] == 0 and len(res["good"]["pngs"]) == 1 and res["badtime"]["rc"] == 1, (res["good"], res["badtime"])
    assert runs == [("ep-x", [8.0])], runs

    # a hung batch is not rerun job by job (that would be one more timeout per job)
    q.submit(str(ep), "1", "hung-a")
    q.submit(str(ep), "2", "hung-b")
    tries = []
    q.snap_local = lambda e, times, pin, name, out: (tries.append(times), (1, f"killed after {q.limit(times)} s"))[1]
    q.run("local")
    res = {f.stem.split("-", 1)[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json") if "-" in f.stem}
    assert tries == [[1.0, 2.0]] and res["hung-a"]["rc"] == 1 and res["hung-b"]["rc"] == 1, (tries, res["hung-a"])

    # the ZBook path: remote command runs the RAM gate, then the pinned snapshot on the mirror with the signed Chrome,
    # and scp brings that job's PNGs back into the job's own out dir
    calls = []
    q.ship = lambda e: (0, 5)

    def fake_ssh(cmd, timeout):
        calls.append(cmd)
        return subprocess.CompletedProcess(cmd, 0, "", "")

    def fake_scp(cmd, **k):
        calls.append(cmd)
        Path(cmd[-1]).mkdir(parents=True, exist_ok=True)
        (Path(cmd[-1]) / "frame-00-at-1.5s.png").write_bytes(b"png")
        return subprocess.CompletedProcess(cmd, 0, "", "")

    q.ssh, q.subprocess.run = fake_ssh, fake_scp
    stage = d / "stage"
    rc, log = q.snap_zbook(ep, [1.5, 6.0], "0.8.185", "J1", stage)
    q.subprocess.run = real_run
    remote = calls[0]
    assert rc == 0 and remote.startswith(f'python "{q.ZBOOK_REPO}\\scripts\\render_busy.py" && '), remote
    assert f'set "HYPERFRAMES_BROWSER_PATH={q.ZBOOK_CHROME}"' in remote and "npx --yes hyperframes@0.8.185 snapshot" in remote, remote
    assert f'"{q.ZBOOK_REPO}\\.snapq\\mirror\\ep-x" --at 1.5,6.0 --no-end --describe false -o "{q.ZBOOK_REPO}\\.snapq\\out\\J1"' in remote, remote
    assert calls[1][:3] == ["scp", "-q", "-r"] and calls[1][3] == "zbook:" + f"{q.ZBOOK_REPO}/.snapq/out/J1/*".replace("\\", "/"), calls[1]
    assert calls[1][4] == str(stage), calls[1]

    # a remote run past the timeout kills the mirror's snapshot tree on the ZBook before the next job
    calls.clear()
    q.ssh = lambda cmd, timeout: (calls.append(cmd), (_ for _ in ()).throw(subprocess.TimeoutExpired(cmd, timeout)) if "snapshot" in cmd else None)[1]
    rc, log = q.snap_zbook(ep, [1.5, 6.0], "0.8.185", "J2", stage)
    assert rc == 1 and f"killed after {q.SNAP_TIMEOUT + 2 * q.FRAME_TIMEOUT} s" in log and calls[-1] == q.KILL_REMOTE, (rc, log, calls)

print("snapshot_queue self-check PASS (no-browser submit, one run at a time, per-episode batches with each job's own frames, lock, empty-PNG fail, bad and raising jobs recorded, a bad time sinks only its own job, no per-job rerun of a hung batch, seek-order jobs alone and in order, a bad out dir is one job's rc 1, referenced-only delta ship, ZBook command, scp and timeout kill)")
