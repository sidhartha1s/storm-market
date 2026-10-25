#!/usr/bin/env python3
"""Every Paul full-frame clip in an episode must come from one start frame.

Mayfield clip 1 (22 Oct 26) was made from the character sheet in a study while clips 2 to 6 came from the desk
start frame; owner 25 Oct 26: "it's not even my face" (retaken in Mayfield commit 4e606b56). The frame each clip was
made from is the "frame" field of the jobs.json beside it (media/paul/<clip dir>/jobs.json, written by the Flow/Omni
driver). Frames are compared by file name, since the same file sits under different worktree paths.

Usage: python3 scripts/paul_start_frame.py episodes/<slug>   exit 0 = one start frame, 1 = differ or missing.
"""
import json
import re
import sys
from pathlib import Path

MOUNT = re.compile(r'<video\b[^>]*\bid="(ins-paul-\d+)"[^>]*\bsrc="([^"]+)"')


def start_frames(episode):
    """{clip id: start-frame file name, or None when its jobs.json or frame field is missing}."""
    live = re.sub(r"<!--.*?-->", "", (episode / "index.html").read_text(encoding="utf-8"), flags=re.S)
    out = {}
    for cid, src in MOUNT.findall(live):
        jobs = (episode / src).parent / "jobs.json"
        frames = {Path(j["frame"]).name for j in json.loads(jobs.read_text(encoding="utf-8"))["jobs"]
                  if j.get("frame")} if jobs.is_file() else set()
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
