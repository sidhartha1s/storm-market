"""Self-check for scripts/sfx_peak.py: python3 scripts/test_sfx_peak.py
Peak-finding is verified against a synthetic wav with a single sample-exact impulse (ffmpeg
lavfi aevalsrc), never against a real SFX file. eligible_hits() is verified against synthetic
index.html fragments covering the riser/bed/narration/insert exclusions.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
from sfx_peak import eligible_hits, find_peak_time  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


HAVE_FFMPEG = subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode == 0
if HAVE_FFMPEG:
    with tempfile.TemporaryDirectory() as d:
        # a mono wav, 2s @ 22050Hz, silent except one sample = 1.0 at n=22050 (t=1.000s exactly)
        wav = Path(d) / "impulse.wav"
        r = subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
             "-i", "aevalsrc=exprs='if(eq(n\\,22050)\\,1\\,0)':s=22050:d=2",
             "-ac", "1", str(wav)],
            capture_output=True, text=True)
        check("sfx_peak-01 fixture: synthetic impulse wav built", r.returncode == 0 and wav.exists(), r.stderr[-300:])

        peak = find_peak_time(wav)
        check("sfx_peak-02 find_peak_time locates a known impulse within one sample period",
              abs(peak - 1.0) < 0.01, f"peak={peak}")
else:
    print("SKIP sfx_peak-01/02: ffmpeg not on PATH")

HTML = (
    '<audio id="sx-stamp-ef5" src="media/sfx/stamp.wav" data-start="1.70" data-duration="3"></audio>\n'
    '<audio id="sx-riser-a1" src="media/sfx/riser.mp3" data-start="10" data-duration="4"></audio>\n'
    '<audio id="sx-mus-a" src="media/beds/bed.mp3" data-bed="" data-start="0" data-duration="100"></audio>\n'
    '<audio id="nx-001" src="media/audio/001.wav" data-start="0" data-duration="5"></audio>\n'
    '<video id="ins-dispatch" src="media/inserts/x.mp4" data-start="20" data-duration="8"></video>\n'
    '<audio id="sx-stamp-ef3" src="media/sfx/stamp.wav" data-start="4.44" data-duration="3"></audio>\n'
)
rows = list(eligible_hits(HTML))
check("sfx_peak-03 eligible_hits keeps only one-shot hits (excludes riser/bed/nx-/ins-)",
      [r[0] for r in rows] == ["sx-stamp-ef5", "sx-stamp-ef3"], rows)
check("sfx_peak-04 eligible_hits reports the cue (data-start) unchanged",
      rows[0] == ("sx-stamp-ef5", "media/sfx/stamp.wav", 1.70), rows)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("sfx_peak self-check: ALL PASS")
