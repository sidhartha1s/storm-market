"""transcribe_episode.py and paul_voice.py book the heavy lock like every other heavy job (audit L10, 11 Nov 26):
python3 scripts/test_heavy_booked.py

transcribe_episode.py runs for real against an empty episode folder while a temp lock is held: it must print the
heavy-lock wait and only then finish. paul_voice.py cannot be imported on a machine without the OpenVoice weights
(ops/tasks.md row 45), so its `__main__` block is read as source: main() must run inside render_busy.heavy_lock.
Uses a temp HEAVY_LOCK_FILE; the real lock and every other job are left alone.
"""
import ast
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
NW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
FAILS = []


def check(name, cond, detail=""):
    if not cond:
        FAILS.append(name)
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else f"  {detail}"))


def main_block_books_lock(path):
    """True when the file's `if __name__ == "__main__":` block calls main() inside `with render_busy.heavy_lock(...)`."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    block = next(n for n in tree.body if isinstance(n, ast.If) and ast.unparse(n.test) == "__name__ == '__main__'")
    for w in (n for n in ast.walk(block) if isinstance(n, ast.With)):
        calls = [ast.unparse(i.context_expr) for i in w.items]
        if any(c.startswith("render_busy.heavy_lock(") for c in calls) and "main(" in ast.unparse(w):
            return True
    return False


check("paul_voice.py runs main() inside render_busy.heavy_lock", main_block_books_lock(S / "paul_voice.py"))
check("transcribe_episode.py runs main() inside render_busy.heavy_lock", main_block_books_lock(S / "transcribe_episode.py"))

with tempfile.TemporaryDirectory() as d:
    lock = Path(d) / "heavy.lock"
    ep = Path(d) / "ep-empty"
    ep.mkdir()
    env = {**os.environ, "HEAVY_LOCK_FILE": str(lock)}
    env.pop("HEAVY_LOCK_TOKEN", None)  # a token from an e2e would let the job through as the holder's child
    holder = subprocess.Popen(
        [sys.executable, "-c", f"import sys, time; sys.path.insert(0, {str(S)!r}); import render_busy\n"
                               "with render_busy.heavy_lock('render ep-test full'):\n time.sleep(3)"],
        env=env, stdout=subprocess.DEVNULL, creationflags=NW)
    t0 = time.time()
    while not lock.exists() and time.time() - t0 < 20:
        time.sleep(0.1)
    t0 = time.time()
    r = subprocess.run([sys.executable, str(S / "transcribe_episode.py"), str(ep)], env=env, capture_output=True,
                       text=True, timeout=60, creationflags=NW)
    waited = time.time() - t0
    holder.wait()
    check("transcribe_episode.py waits for a held heavy lock, then runs",
          r.returncode == 0 and "WAITING to start transcribe ep-empty" in r.stdout and "render ep-test full" in r.stdout
          and r.stdout.rstrip().endswith("DONE") and waited > 1.0, f"rc={r.returncode} waited={waited:.1f}s {r.stdout!r} {r.stderr[-300:]}")
    check("transcribe_episode.py releases the lock when done", not lock.exists())

if FAILS:
    print(f"\n{len(FAILS)} FAILED")
    sys.exit(1)
print("\nall passed")
