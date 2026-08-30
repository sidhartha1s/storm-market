#!/usr/bin/env python3
"""Pre-trim approved BEST_CUTS.md rows into standalone files in media/broadcast/cuts/.
Exact in/out points were derived from word-level timestamps in research/transcripts/*.json
(re-verified against source, not copied blind from BEST_CUTS.md's approximate table).
"""
import subprocess, sys
from pathlib import Path

EP = Path(__file__).resolve().parent.parent
SRC = EP / "media" / "broadcast"
OUT = SRC / "cuts"
OUT.mkdir(parents=True, exist_ok=True)
FFMPEG = "C:/Users/Sidhartha/AppData/Local/Microsoft/WinGet/Links/ffmpeg.exe"

# (row, source_clip, start, end, quote) -- start/end already padded (~0.15s pre / ~0.2s post)
ROWS = [
    (1,  "cnn-ethics-of-chasing", 14.53, 17.16, "The safest place to be is right here in this vehicle."),
    (2,  "cnn-storm-reporting-dangerous", 155.95, 160.30, "There's just no one safer than Tim. Tim, he would never put himself in danger."),
    (3,  "cnn-storm-reporting-dangerous", 49.85, 52.82, "That's my life. And I don't want to give that up just yet."),
    (4,  "twc-bettes-suv-toss-hookcut", 0.00, 3.52, "...heading right at Bettes and his team."),
    (5,  "cnn-ethics-of-chasing", 26.51, 30.12, "I just couldn't ever think it would ever happen to him because of his level of expertise."),
    (6,  "cnn-ethics-of-chasing", 7.15, 14.55, "A veteran storm chaser, Tim Samaras, made a living getting inside the storm, studying tornadoes and their fury for the past 25 years."),
    (7,  "cnn-ethics-of-chasing", 45.23, 49.70, "The erratic track of this storm, sudden left turn, caught many off guard."),
    (8,  "cnn-storm-reporting-dangerous", 65.19, 72.10, "They are Tim Samaras, who worked with the Discovery Channel program Stormchasers, his son Paul Samaras, and their colleague Carl Young."),
    (9,  "kfor-sutton-very-close-call-hookcut", 0.00, 4.01, "Please do not ride this out in any interior closet or bathroom."),
    (10, "koco-survivor-testimony-b", 0.00, 1.46, "I thought we were going to die."),
    (11, "koco-survivor-testimony-b", 18.21, 21.88, "I opened the front door and I said it's too late. It's already here."),
    (12, "koco-survivor-testimony-b", 23.61, 27.56, "I held onto her and as soon as I grabbed her it picked us up."),
    (13, "koco-survivor-testimony-c", 0.00, 2.14, "We only had about 30 seconds."),
    (14, "koco-survivor-testimony-c", 12.87, 18.38, "When it got to about 20, 30 feet in the air, it exploded and we all fell to the ground."),
    (15, "koco-survivor-testimony-c", 18.47, 24.58, "When you're flying around like a piece of paper, that's all you can do is cry to God and beg Him to help you."),
    (16, "koco-survivor-testimony-c", 59.77, 63.64, "When you hear those warnings, take it serious, go get shelter."),
    (17, "kfor-2019-survivor-testimony", 31.79, 39.64, "Closed my eyes and I remember feeling myself going through something that I thought was the wall, but we found out it was actually the roof."),
    (18, "kfor-2019-survivor-testimony", 47.42, 50.36, "[...] honestly do not understand how we survived. I don't."),
    (19, "kfor-2019-survivor-testimony", 87.95, 95.74, "I had internal bleeding, my spleen ruptured, my broken ribs, and I had a concussion."),
    (20, "koco-one-year-ago", 4.25, 10.14, "The record-setting two-and-a-half-mile-wide tornado, taking lives and too many homes to count."),
    (21, "koco-one-year-ago", 65.57, 71.50, "Four storm chasers and four others died with a tornado. Toss their cars. It's just truly unbelievable."),
    (22, "koco-one-year-ago", 79.45, 83.20, "If it was one more mile over, it would have took the whole community of El Reno out."),
    (23, "kfor-sutton-studio-interview", 56.49, 59.38, "And sure enough, you see it turning into this big wedge."),
    (24, "kfor-sutton-studio-interview", 96.17, 99.82, "I feel stuff hitting my back and I know that's not right."),
    (25, "kfor-sutton-studio-interview", 122.19, 125.94, "So those winds, I would estimate at least a hundred miles per hour."),
    (26, "kfor-retrospective-2026", 1286.67, 1293.84, "The vortex briefly stalls over their Chevy Cobalt. But it tumbles over five times. They do not survive."),
    (27, "kfor-retrospective-2026", 1028.65, 1035.44, "Henderson stops with brutal force. The tornado overtakes him. He does not survive."),
    (28, "kfor-retrospective-2026", 814.97, 821.06, "Meanwhile, Richard Henderson is trying to beat the tornado to the east, his progress waylaid by a chaser traffic jam."),
]

def cutname(row, clip, t0, t1):
    return f"{clip}__{t0:07.2f}-{t1:07.2f}.mp4".replace(" ", "0")

results = []
for row, clip, t0, t1, quote in ROWS:
    src = SRC / f"{clip}.mp4"
    if not src.exists():
        print(f"row {row}: MISSING SOURCE {src}")
        continue
    dur = round(t1 - t0, 2)
    name = cutname(row, clip, t0, t1)
    dst = OUT / name
    # coarse fast seek 5s before target (only matters for the 27-min file), then accurate -ss after -i
    coarse = max(0.0, t0 - 5.0)
    refine = t0 - coarse
    cmd = [
        FFMPEG, "-y", "-ss", f"{coarse:.3f}", "-i", str(src),
        "-ss", f"{refine:.3f}", "-t", f"{dur:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
        "-c:a", "aac", "-b:a", "192k",
        str(dst),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and dst.exists()
    results.append((row, clip, t0, t1, dur, name, ok, quote))
    print(f"row {row}: {'OK' if ok else 'FAIL'} -> {name} ({dur:.2f}s)")
    if not ok:
        print(r.stderr[-2000:])

print("\n--- summary ---")
for row, clip, t0, t1, dur, name, ok, quote in results:
    print(f"{row:>2} {name:<70} {dur:>5.2f}s {'OK' if ok else 'FAIL'}")
