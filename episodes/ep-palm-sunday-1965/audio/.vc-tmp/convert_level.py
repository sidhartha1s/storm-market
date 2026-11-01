# One-off glue (never committed): convert every backed-up narration wav with the El Reno convert_one.py,
# then pad to the source length and level to the source's ffmpeg mean_volume. Writes audio/<id>.wav.
import json, re, subprocess, sys
from pathlib import Path

A = Path(sys.argv[1])
PY = r"C:\Users\Sidhartha\Automation Projects\storm-market\.venv-pocket\Scripts\python.exe"
CONV = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep-el-reno-v4b\episodes\ep4-el-reno\.qc-tmp\voice-sid\convert_one.py"
T = A / ".vc-tmp"


def mean_vol(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(p), "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume: (-?[\d.]+) dB", r).group(1))


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True, check=True).stdout.strip())


rep = {}
for src in sorted((A / ".algenib-backup").glob("*.wav")):
    raw = T / f"{src.stem}.raw.wav"
    subprocess.run([PY, "-I", CONV, str(src), str(raw)], capture_output=True, check=True)
    target, d = mean_vol(src), dur(src)
    gain = target - mean_vol(raw)
    out = A / src.name
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", f"volume={gain:.2f}dB,alimiter=limit=0.93,apad", "-t", f"{d:.6f}",
                    "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(out)], check=True)
    rep[src.stem] = {"src_s": round(d, 4), "out_s": round(dur(out), 4), "src_mean": target, "out_mean": mean_vol(out), "gain": round(gain, 2)}
    print(src.stem, rep[src.stem], flush=True)
(T / "convert_report.json").write_text(json.dumps(rep, indent=1))
