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

# Every line below is copied VERBATIM from a real episode's index.html (source noted per line) —
# the fixture that hid the original data-bed bug used markup with data-bed stripped off, which no
# real episode ever has (audio_levels.py:19-20: every sx- element carries data-bed).
HTML = (
    # episodes/ep-enderlin-2025/index.html:166-167 (real one-shot stamp hits, both carry data-bed)
    '<audio id="sx-stamp-ef5" src="media/sfx/stamp-boom.wav" data-bed="" data-start="1.70" data-duration="3" data-volume="0.28"></audio>\n'
    '<audio id="sx-stamp-ef3" src="media/sfx/stamp-boom.wav" data-bed="" data-start="4.44" data-duration="3" data-volume="0.2" data-callback="second stamp: the struck EF3 thumps on its name"></audio>\n'
    # episodes/sh-hawaii-lowell-1/index.html:78 (real riser, must stay excluded)
    '<audio id="sx-riser-hook" src="media/sfx/riser-1s2.wav" data-bed="" data-start="2.78" data-duration="1.2" data-volume="0.40"></audio>\n'
    # episodes/ep-enderlin-2025/index.html (real continuous bed, also carries data-bed)
    '<audio id="sx-mus-bed-1" src="media/beds/bed-darkambient-long.mp3" data-bed="" data-start="22.8" data-duration="1307.352" data-volume="0.13"></audio>\n'
    # episodes/ep-enderlin-2025/index.html (real narration line, excluded by nx- prefix)
    '<audio id="nx-h1-s1" src="audio/h1-s1.wav" data-start="0.0" data-duration="5.691" data-volume="1"></audio>\n'
    # a <video> element with an sx- id must never match — blocker #2 (video b-roll dwarfed real hits)
    '<video id="sx-broll-fake" src="media/broll/fake.mp4" data-start="20" data-duration="8"></video>\n'
    # episodes/ep-enderlin-2025/index.html (real trimmed-into-file element, media_start != 0)
    '<audio id="sx-drone" src="media/sfx/drone-hook.mp3" data-bed="" data-start="0" data-media-start="1.04" data-duration="27.61" data-volume="0.13"></audio>\n'
)
rows = list(eligible_hits(HTML))
check("sfx_peak-03 eligible_hits finds the real stamp hits despite data-bed on every sx- element",
      [r[0] for r in rows] == ["sx-stamp-ef5", "sx-stamp-ef3", "sx-mus-bed-1", "sx-drone"], rows)
check("sfx_peak-03b eligible_hits excludes riser/nx- ids and never matches <video>",
      not any(r[0] in ("sx-riser-hook", "nx-h1-s1", "sx-broll-fake") for r in rows), rows)
check("sfx_peak-04 eligible_hits reports the cue (data-start) and media_start unchanged",
      rows[0] == ("sx-stamp-ef5", "media/sfx/stamp-boom.wav", 1.70, 0.0), rows)
check("sfx_peak-05 eligible_hits parses data-media-start for a trimmed-into-file element",
      rows[3] == ("sx-drone", "media/sfx/drone-hook.mp3", 0.0, 1.04), rows)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("sfx_peak self-check: ALL PASS")
