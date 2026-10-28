"""Refuse a Flow job file before any spend when a Paul clip would not start from his locked start frame.

Swapping the character sheet in as the frame, or rewriting the room in the prompt, gave every clip a different
background. The frame is the room; the sheet is only an ingredient.
"""
import re

LOCKED_FRAME = "assets/paul/paul-start-frame-omni-v2.png"  # owner-made 22 Oct 26 evening; v1 .jpg is history
# An episode may carry its own owner-picked start frame (Buffalo's Christmas look C, owner devq 27 Oct 26);
# scripts/paul_start_frame.py then holds every clip of that episode to the one frame.
EPISODE_FRAME = re.compile(r"/episodes/[^/]+/media/paul/paul-start-frame-[^/]+\.(png|jpg)$")
BANNED = ("quiet study",)


def errors(cfg):
    out = []
    for job in cfg["jobs"]:
        frame = job["frame"].replace("\\", "/").lower()
        if "paul" in frame and LOCKED_FRAME not in frame and not EPISODE_FRAME.search(frame):
            out.append(f"{job['name']}: frame {job['frame']} is not Paul's locked start frame ({LOCKED_FRAME}) "
                       "or an episode's media/paul/paul-start-frame-*")
        if job.get("ingredients"):  # Buffalo 28 Oct 26: First Frame takes one image; Flow asked instead of quoting, 0 spent
            out.append(f"{job['name']}: has ingredients; a start-frame clip takes the frame only")
        for phrase in BANNED:
            if phrase in job["prompt"].lower():
                out.append(f"{job['name']}: prompt rewrites the room ('{phrase}'); keep the start frame's room")
    return out


MIN_FREE_GB = 1.5  # a Flow run on a laptop under this froze Chrome three times in a row (0 credits each)


def free_gb():
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # scripts/, this checkout
    from render_busy import free_gb as repo_free_gb
    return repo_free_gb()


def ram_refusal(free=None):
    """The one-line refusal when the laptop is too low on memory for a Flow run, else None."""
    free = free_gb() if free is None else free
    return f"refused, nothing spent: {free:.2f} GB free, a Flow run needs {MIN_FREE_GB} GB" if free < MIN_FREE_GB else None


def assert_responsive(page, timeout_ms=15000):
    """Raise when the Flow tab is up but frozen (CDP answers, the page does not): a run against it spends nothing and hangs."""
    try:
        page.wait_for_function("1", timeout=timeout_ms)
    except Exception:
        raise RuntimeError(f"Flow Chrome on port 9333 is frozen (no reply in {timeout_ms // 1000} s); restart it, nothing spent")


def line_in_prompt(prompt):
    import re
    m = re.search(r'(?:Line|exactly these words and nothing else):\s*["“](.+?)["”]', prompt, re.S)
    return m.group(1) if m else None


def clip_verdict(path, cfg, jobs_path):
    """A clip counts only once checked: opening frame against the start frame, words against the line.
    Threshold 28 from calibration: own-frame clips 7.8 and 18.4, wrong rooms and the collage defect 39.4 to 71.1."""
    import os, subprocess, sys
    from framematch import distance
    if len(cfg["jobs"]) != 1:
        return ("UNVERIFIED", path, "one job per file is needed to check a clip")
    job = cfg["jobs"][0]
    problems = []
    d = distance(path, job["frame"])
    if d > 28:
        problems.append(f"background off the start frame ({d:.1f} > 28)")
    line = job.get("line") or line_in_prompt(job["prompt"])
    if line:
        import json
        here = os.path.dirname(os.path.abspath(__file__))
        tmp = os.path.splitext(path)[0] + ".line.json"  # beside the clip: one per lane, inside the repo
        json.dump({"jobs": [{"line": line}]}, open(tmp, "w", encoding="utf8"))
        words = subprocess.run([sys.executable, os.path.join(here, "clip_check.py"), tmp, path], capture_output=True, text=True)
        if words.returncode and not words.stdout.strip():  # the checker itself failed (missing file, no model): never read as a mismatch
            problems.append("word check crashed: " + words.stderr.strip().splitlines()[-1][:160] if words.stderr.strip() else "word check crashed")
        elif words.returncode:
            problems.append("words differ from the line")
    else:
        problems.append("no line found in the job, words unchecked")
    return ("REJECTED", path, "; ".join(problems)) if problems else ("VERIFIED", path, f"frame {d:.1f}, words exact")


if __name__ == "__main__":
    import json, sys
    bad = {"jobs": [{"name": "sheet-as-frame", "frame": "C:/x/assets/paul/paul-sheet-c.png", "prompt": "line"},
                    {"name": "quiet", "frame": "C:/x/assets/paul/paul-start-frame-omni-v2.png", "prompt": "a man in a quiet study"},
                    {"name": "old-frame", "frame": "C:/x/assets/paul/paul-start-frame-omni.jpg", "prompt": "line"}]}
    assert len(errors(bad)) == 3, errors(bad)
    good = json.load(open(r"C:\Users\Sidhartha\Videos\paul-v2-test\compare\omni\jobs.json", encoding="utf8"))
    for job in good["jobs"]:  # that run predates the v2 lock; the check is the job shape, not the old frame
        job["frame"] = "C:/x/assets/paul/paul-start-frame-omni-v2.png"
    assert errors(good) == [], errors(good)
    print("self-test ok")
