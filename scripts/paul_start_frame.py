#!/usr/bin/env python3
"""Every Paul full-frame clip in an episode must come from one start frame.

Mayfield clip 1 (22 Oct 26) was made from the character sheet in a study while clips 2 to 6 came from the desk
start frame; owner 25 Oct 26: "it's not even my face" (retaken in Mayfield commit 4e606b56). The frame each clip was
made from is the "frame" field of the jobs.json beside it (media/paul/<clip dir>/jobs.json, written by the Flow/Omni
driver). A batch run keeps one jobs.json for several clips (Palm Sunday media/paul/acts-2-6/): a clip with none beside
it takes the jobs named after it ("<clip id>" or "...-<clip id>") from any media/paul/**/jobs.json. Frames are compared by file name, since the same file sits under different worktree paths.

Usage: python3 scripts/paul_start_frame.py episodes/<slug>   exit 0 = one start frame, 1 = differ or missing.
"""
import json
import re
import sys
from pathlib import Path

import timeline


def _jobs(path):
    return json.loads(path.read_text(encoding="utf-8"))["jobs"]


def start_frames(episode):
    """{clip id: start-frame file name, or None when no jobs.json gives it exactly one frame}."""
    out = {}
    # attributes in any order (timeline.mounts); ins-paul-e1/e2 are the end-ask clips from assets/, not Flow clips
    clips = [(a["id"], a["src"]) for _, a in timeline.mounts((episode / "index.html").read_text(encoding="utf-8"), "video")
             if re.fullmatch(r"ins-paul-\d+", a.get("id", "")) and "src" in a]
    for cid, src in clips:
        beside = (episode / src).parent / "jobs.json"
        if beside.is_file():
            jobs = _jobs(beside)
        else:
            jobs = [j for f in sorted((episode / "media" / "paul").glob("**/jobs.json")) for j in _jobs(f)
                    if j.get("name") == cid or str(j.get("name", "")).endswith("-" + cid)]
        frames = {Path(j["frame"]).name for j in jobs if j.get("frame")}
        out[cid] = frames.pop() if len(frames) == 1 else None
    return out


def problems(frames):
    bad = [f"{cid}: no single start frame in its jobs.json" for cid, f in frames.items() if f is None]
    names = {f for f in frames.values() if f}
    if len(names) > 1:
        bad.append("clips use different start frames: " + ", ".join(f"{c}={f}" for c, f in sorted(frames.items())))
    return bad


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/paul_start_frame.py episodes/<slug>")
    frames = start_frames(Path(sys.argv[1]))
    bad = problems(frames)
    for b in bad:
        print("FAIL", b)
    if not bad:
        print(f"PASS Paul start frame: {len(frames)} clip(s), {set(frames.values()) or 'none mounted'}")
    sys.exit(1 if bad else 0)
