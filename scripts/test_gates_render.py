"""Self-check for the gate stamp and for gates beside a render: python3 scripts/test_gates_render.py

A: run_gates.py, all green, stamps the timeline it checked (timeline.digest); render_preflight.py refuses a render
   whose stamp is missing or whose timeline changed since; a failing gate removes an old stamp.
B: while a render holds the heavy lock, run_gates.py runs only the file-only gates, and only above
   config.yaml render.gates_beside_render_min_free_gb; browser gates are reported waiting, exit 3, no stamp.
Every gate is a stub that logs its name; the lock holder is a fake record (this process's own pid, so it reads as
alive) in a temp HEAVY_LOCK_FILE; free memory is injected (render_busy.free_gb replaced). No render, no browser."""
import contextlib
import io
import os
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import render_busy  # noqa: E402
import render_preflight  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


FILE_ONLY = ["render_preflight.py", "paul_start_frame.py", "sweep_episode.py", "lint_timeline.py", "build_srt.py",
             "narration_picture_check.py", "flag_words.py", "hook_shape.py", "homograph_scan.py", "audio_levels.py"]
# wait for the render: the browser gates, and media_budget.py (it times ffprobe spawns, so beside a render it measures load)
WAITS = ["beat_density.py", "media_budget.py", "blank_scan.mjs", "overlap_check.mjs", "occlusion_check.mjs", "graphics_qc.mjs"]

d = Path(tempfile.mkdtemp())
stubs, log = d / "scripts", d / "order.log"
stubs.mkdir()
(stubs / "run_gates.py").write_bytes((S / "run_gates.py").read_bytes())
(d / "config.yaml").write_text("render:\n  gates_beside_render_min_free_gb: 2\n", encoding="utf-8")
ep = d / "episodes" / "ms-stamp-test"  # ms-: no documentary layers, so preflight reaches the stamp
(ep / "compositions").mkdir(parents=True)
(ep / "index.html").write_text("<html></html>", encoding="utf-8")
(ep / "compositions" / "g-a.html").write_text("<div>a</div>", encoding="utf-8")
os.environ["HEAVY_LOCK_FILE"] = str(d / "heavy.lock")


def stub_all(fail=None, edit=None):
    """Every gate a stub logging its name; `fail` exits 1, `edit` appends to index.html (an edit mid-run)."""
    for n in FILE_ONLY + WAITS:
        if n.endswith(".py"):
            touch = f'open(r"{ep / "index.html"}", "a").write("<p>edit</p>")\n' if n == edit else ""
            (stubs / n).write_text(f'import sys\nopen(r"{log}", "a").write("{n}\\n")\n{touch}sys.exit({int(n == fail)})\n', encoding="utf-8")
        else:
            (stubs / n).write_text(f'import {{ appendFileSync }} from "fs"; appendFileSync(String.raw`{log}`, "{n}\\n");', encoding="utf-8")


def gates(free=(8.0,), run_all=False):
    """run_gates.py in-process on ep with free_gb() reading `free` in turn (the last value repeats)."""
    log.unlink(missing_ok=True)
    seq = list(free)
    render_busy.free_gb = lambda: seq.pop(0) if len(seq) > 1 else seq[0]
    sys.argv, buf, code = [str(stubs / "run_gates.py"), str(ep), *(["--all"] if run_all else [])], io.StringIO(), 0
    with contextlib.redirect_stdout(buf):
        try:
            runpy.run_path(str(stubs / "run_gates.py"), run_name="__main__")
        except SystemExit as e:
            code = e.code
    return code, buf.getvalue(), log.read_text(encoding="utf-8").splitlines() if log.exists() else []


def preflight():
    r = subprocess.run([sys.executable, str(S / "render_preflight.py"), str(ep), "draft"], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def hold(job):
    pid = os.getpid()
    (d / "heavy.lock").write_text(f'{{"job": "{job}", "pid": {pid}, "created": {render_busy.created(pid)}, "token": "x"}}', encoding="utf-8")


stub_all()

# --- A: the stamp ---
code, out = preflight()
check("A preflight refuses an episode run_gates never passed, naming the command", code == 7 and "run_gates.py" in out, f"exit {code}\n{out[-400:]}")

code, out, ran = gates()
stamp = [p.name for p in ep.glob("*.marker")]
check("A run_gates all green writes the stamp", code == 0 and len(ran) == 16 and stamp, f"exit {code} ran {len(ran)} stamp {stamp}")
code, out = preflight()
check("A preflight passes the stamp on the timeline the gates checked", stamp and code != 7 and "[stamp] OK" in out, f"exit {code}\n{out[-400:]}")

(ep / "compositions" / "g-a.html").write_text("<div>b</div>", encoding="utf-8")
code, out = preflight()
check("A preflight refuses once a composition changed after the gates", code == 7 and "run_gates.py" in out, f"exit {code}\n{out[-400:]}")

gates()  # re-stamp the edited timeline, then let a gate fail: the old stamp must go
had = list(ep.glob("*.marker"))
stub_all(fail="lint_timeline.py")
code, out, ran = gates()
check("A a failing gate removes the stamp", had and code == 1 and not list(ep.glob("*.marker")), f"exit {code} {list(ep.glob('*.marker'))}")

stub_all(edit="lint_timeline.py")
code, out, ran = gates()
check("A the timeline changes while the gates run: exit 1, says so, no stamp",
      code == 1 and "changed while the gates ran" in out and not list(ep.glob("*.marker")), f"exit {code}\n{out[-400:]}")
stub_all()

try:
    r = render_preflight.stamp_refusal(ep, unchecked="any reason")
except TypeError as e:
    r = e
check("A stamp_refusal has no unchecked= bypass", isinstance(r, TypeError), f"{r!r}")

import timeline  # noqa: E402
before = timeline.digest(ep)
(ep / "compositions" / "data").mkdir()
(ep / "compositions" / "data" / "track.geojson").write_text('{"type": "LineString"}', encoding="utf-8")
check("A a file under compositions/data/ is in the digest", timeline.digest(ep) != before)
for name in ("grain.js", "page.css"):
    before = timeline.digest(ep)
    (ep / name).write_text("/* x */", encoding="utf-8")
    check(f"A an episode-root {name} is in the digest", timeline.digest(ep) != before)
before = timeline.digest(ep)
(ep / "media").mkdir()
(ep / "media" / "still.png").write_bytes(b"\x89PNG")
(ep / "compositions" / "data" / "clip.mp4").write_bytes(b"\0")
check("A media stays out of the digest", timeline.digest(ep) == before)

# --- B: beside a render ---
stub_all()
hold("render ep-other draft")
code, out, ran = gates(free=(8.0,))
check("B render holds the lock, 8 GB free: only the file-only gates run, in order", ran == FILE_ONLY, f"ran={ran}")
check("B browser gates are reported waiting for the render, exit 3, no stamp",
      code == 3 and all(f"{n}" in out.split("waiting for the render", 1)[-1] for n in ("beat_density.py", "graphics_qc.mjs"))
      and not list(ep.glob("*.marker")), f"exit {code}\n{out[-600:]}")

code, out, ran = gates(free=(1.0,))
check("B below the floor nothing runs and it says why", ran == [] and code == 3 and "gates_beside_render_min_free_gb" in out, f"exit {code} ran={ran}\n{out[-400:]}")

code, out, ran = gates(free=(8.0, 8.0, 8.0, 1.0))
check("B memory falls below the floor mid-run: the run stops there", ran == FILE_ONLY[:3] and code == 3, f"exit {code} ran={ran}")

(d / "heavy.lock").unlink()
print(f"\n{'ALL PASS' if not FAILS else f'{len(FAILS)} FAILED: ' + ', '.join(FAILS)}")
sys.exit(1 if FAILS else 0)
