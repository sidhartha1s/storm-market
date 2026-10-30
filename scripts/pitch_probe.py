"""Median speaking pitch (F0, Hz) of audio files, by autocorrelation on 40 ms frames (voiced = energy above a tenth
of the file's peak frame). Used to compare a Paul clip's voice with the narration: python3 scripts/pitch_probe.py <files>"""
import subprocess
import sys

import numpy as np

SR = 16000


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def f0_median(path, lo=60, hi=320):
    x = load(path)
    n = int(0.04 * SR)
    hop = n // 2
    frames = [x[i:i + n] for i in range(0, len(x) - n, hop)]
    energy = np.array([float(np.dot(f, f)) for f in frames])
    voiced = [f for f, e in zip(frames, energy) if e > energy.max() * 0.1]
    f0 = []
    for f in voiced:
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[n - 1:]
        lag_lo, lag_hi = SR // hi, SR // lo
        seg = ac[lag_lo:lag_hi]
        if seg.size and ac[0] > 0:
            k = int(np.argmax(seg)) + lag_lo
            if ac[k] / ac[0] > 0.5:
                f0.append(SR / k)
    return float(np.median(f0)) if f0 else 0.0, len(f0)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        m, k = f0_median(p)
        print(f"{m:6.1f} Hz  ({k} voiced frames)  {p}")
