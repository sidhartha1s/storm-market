"""Self-check for scripts/snapshot_queue.py: python3 scripts/test_snapshot_queue.py

Builders submit without a browser; one worker runs the jobs one at a time; a second worker refuses;
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

    # the worker runs jobs strictly one at a time, oldest first, and records the PNGs
    live, peak, order = [0], [0], []

    def fake_snap(job, pin):
        live[0] += 1
        peak[0] = max(peak[0], live[0])
        order.append(job["at"])
        Path(job["out"]).mkdir(parents=True, exist_ok=True)
        for t in job["at"]:
            (Path(job["out"]) / f"frame-at-{t}s.png").write_bytes(b"png")
        time.sleep(0.05)
        live[0] -= 1
        return 0, "ok"

    q.snap_local = fake_snap
    q.run("local")
    done = sorted((q.SPOOL / "done").glob("*.json"))
    assert peak[0] == 1 and order == [[1.5, 6.0], [2.0]], (peak, order)
    assert not list((q.SPOOL / "pending").glob("*.json"))
    rec = json.loads(done[0].read_text())
    assert rec["rc"] == 0 and len(rec["pngs"]) == 2, rec

    # exit 0 with no PNG is a failed job, not a pass
    q.submit(str(ep), "3", "empty")
    q.snap_local = lambda job, pin: (0, "ok")
    q.run("local")
    rec = json.loads(sorted((q.SPOOL / "done").glob("*empty.json"))[0].read_text())
    assert rec["rc"] == 1 and "no PNG" in rec["log"], rec

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
    q.submit(str(ep), "5", "after")
    q.snap_local = lambda job, pin: (_ for _ in ()).throw(ValueError("boom")) if job["at"] == [4.0] else fake_snap(job, pin)
    q.run("local")
    res = {f.stem.split("-", 1)[1]: json.loads(f.read_text()) for f in (q.SPOOL / "done").glob("*.json") if "-" in f.stem}
    assert res["bad"]["rc"] == 1 and "JSONDecodeError" in res["bad"]["log"], res["bad"]
    assert res["raises"]["rc"] == 1 and "boom" in res["raises"]["log"], res["raises"]
    assert res["after"]["rc"] == 0 and len(res["after"]["pngs"]) == 1, res["after"]

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
    job = {"ep": str(ep), "at": [1.5, 6.0], "out": str(ep / ".qc-tmp" / "snapq" / "J1")}
    rc, log = q.snap_zbook(job, "0.8.185", "J1")
    q.subprocess.run = real_run
    remote = calls[0]
    assert rc == 0 and remote.startswith(f'python "{q.ZBOOK_REPO}\\scripts\\render_busy.py" && '), remote
    assert f'set "HYPERFRAMES_BROWSER_PATH={q.ZBOOK_CHROME}"' in remote and "npx --yes hyperframes@0.8.185 snapshot" in remote, remote
    assert f'"{q.ZBOOK_REPO}\\.snapq\\mirror\\ep-x" --at 1.5,6.0 --no-end --describe false -o "{q.ZBOOK_REPO}\\.snapq\\out\\J1"' in remote, remote
    assert calls[1][:3] == ["scp", "-q", "-r"] and calls[1][3] == "zbook:" + f"{q.ZBOOK_REPO}/.snapq/out/J1/*".replace("\\", "/"), calls[1]
    assert calls[1][4] == job["out"], calls[1]

    # a remote run past the timeout kills the mirror's snapshot tree on the ZBook before the next job
    calls.clear()
    q.ssh = lambda cmd, timeout: (calls.append(cmd), (_ for _ in ()).throw(subprocess.TimeoutExpired(cmd, timeout)) if "snapshot" in cmd else None)[1]
    rc, log = q.snap_zbook(job, "0.8.185", "J2")
    assert rc == 1 and "killed after" in log and calls[-1] == q.KILL_REMOTE, (rc, log, calls)

print("snapshot_queue self-check PASS (no-browser submit, one job at a time, lock, empty-PNG fail, bad and raising jobs recorded, referenced-only delta ship, ZBook command, scp and timeout kill)")
