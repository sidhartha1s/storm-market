#!/usr/bin/env python3
"""Frame-diff spike detector: reads raw 180x180 8-bit grayscale frames from stdin (as produced
by ffmpeg's `scale=180:180,format=gray`, sampled at the render's own fps so it stays CPU-light —
no full-resolution decode) and flags a frame that differs sharply from BOTH its neighbours while
those neighbours look alike each other: a single-frame pop, flash or capture glitch.

REPORTS ONLY, never fails: verify_render.sh's other checks (gpu/composition/black/silence/
freeze) all hard-FAIL on a defect. This one does not, on purpose — a quick intentional cut or
flash-edit can trip the same "differs sharply from both neighbours" signature as a real glitch,
so a human call is required; see the PR body for why this is the one report-only check in the
script.

Flag rule for candidate frame i (neighbours i-1, i+1):
  d_prev = mean(|frame[i-1] - frame[i]|)      (0-255 gray-level units)
  d_next = mean(|frame[i]   - frame[i+1]|)
  d_skip = mean(|frame[i-1] - frame[i+1]|)    (how alike the neighbours are to EACH OTHER)
  flag when d_prev > floor AND d_next > floor AND d_prev > ratio*d_skip AND d_next > ratio*d_skip

Usage:
  ffmpeg -hide_banner -v error -i <render.mp4> -vf "fps=<render fps>,scale=180:180,format=gray" \\
      -f rawvideo - | python3 scripts/pop_scan.py --fps <render fps> [--ratio 3.0] [--floor 8.0]
"""
import argparse
import sys
from collections import deque

import numpy as np

W = H = 180
FRAME_BYTES = W * H


def read_frames(stream):
    while True:
        buf = stream.read(FRAME_BYTES)
        if len(buf) < FRAME_BYTES:
            return
        yield np.frombuffer(buf, dtype=np.uint8).astype(np.int16)


def find_pops(frames_iter, ratio=3.0, floor=8.0):
    """Streams a 3-frame window over frames_iter; returns [(frame_index, d_prev, d_next, d_skip)]
    for every flagged frame. frame_index is 0-based into the sequence yielded by frames_iter."""
    window = deque(maxlen=3)
    pops = []
    for i, frame in enumerate(frames_iter):
        window.append(frame)
        if len(window) < 3:
            continue
        prev, mid, nxt = window
        d_prev = float(np.abs(mid - prev).mean())
        d_next = float(np.abs(nxt - mid).mean())
        d_skip = float(np.abs(nxt - prev).mean())
        baseline = max(d_skip, 0.5)  # avoid a div-by-near-zero false trigger on a static frame
        if d_prev > floor and d_next > floor and d_prev > ratio * baseline and d_next > ratio * baseline:
            pops.append((i - 1, d_prev, d_next, d_skip))
    return pops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fps", type=float, required=True)
    ap.add_argument("--ratio", type=float, default=3.0)
    ap.add_argument("--floor", type=float, default=8.0)
    args = ap.parse_args()

    pops = find_pops(read_frames(sys.stdin.buffer), ratio=args.ratio, floor=args.floor)
    if not pops:
        print("[pop_scan] no spike frames found")
        return
    print(f"[pop_scan] {len(pops)} candidate spike frame(s) — REPORT only, a real defect vs an "
          f"intentional cut/flash-edit is a human call:")
    for fi, dp, dn, ds in pops:
        t = fi / args.fps
        print(f"  frame {fi} @ {t:.2f}s  diff-to-prev={dp:.1f}  diff-to-next={dn:.1f}  "
              f"neighbour-baseline={ds:.1f}")


if __name__ == "__main__":
    main()
