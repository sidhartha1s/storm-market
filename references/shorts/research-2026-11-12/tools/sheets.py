"""Two contact sheets per reel: <code>.whole.jpg (12 frames across the video, first at 0.1 s)
and <code>.open.jpg (12 frames, every 0.25 s of the first 3 s). Usage: python3 sheets.py <media_dir>"""
import glob, subprocess, sys, os, json

for mp4 in sorted(glob.glob(os.path.join(sys.argv[1], "*", "*.mp4"))):
    base = mp4[:-4]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4],
                               capture_output=True, text=True).stdout.strip() or 0)
    if not dur:
        print("no duration", mp4)
        continue
    json.dump({"duration": round(dur, 1)}, open(base + ".dur.json", "w"))
    plans = {"whole": [0.1] + [dur * i / 12 for i in range(1, 12)], "open": [i * 0.25 for i in range(12)]}
    for name, times in plans.items():
        out = f"{base}.{name}.jpg"
        if os.path.exists(out):
            continue
        ins, filt = [], []
        for i, t in enumerate(times):
            ins += ["-ss", f"{min(t, dur - 0.1):.2f}", "-i", mp4]
            filt.append(f"[{i}:v]scale=270:480:force_original_aspect_ratio=decrease,pad=270:480:(ow-iw)/2:(oh-ih)/2[v{i}]")
        graph = ";".join(filt) + ";" + "".join(f"[v{i}]" for i in range(12)) + "xstack=inputs=12:layout=" + \
            "|".join(f"{(i % 6) * 270}_{(i // 6) * 480}" for i in range(12)) + "[o]"
        subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", graph, "-map", "[o]", "-frames:v", "1",
                        "-q:v", "4", out])
    print(os.path.basename(base), round(dur, 1), flush=True)
