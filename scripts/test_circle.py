"""Self-check for the presenter-circle tools: python3 scripts/test_circle.py

circle_audio.py must pick only narration inside the asked span and place each segment after the first one;
circle_cut.py must read only pip videos, seek each window inside the pass that covers it, and name a window no pass
covers. Plain values in, plain values out: no ffmpeg, no model.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import circle_audio  # noqa: E402
import circle_cut  # noqa: E402

FAILS = []
HTML = """
<audio id="nx-a1-s1" src="audio/a1-s1.wav" data-start="10.5" data-duration="4.0"></audio>
<audio id="nx-a1-s2" src="audio/a1-s2.wav" data-start="20.0" data-duration="5.0"></audio>
<audio id="bed-1" src="audio/bed.mp3" data-start="12.0" data-duration="60"></audio>
<audio id="nx-a2-s1" src="audio/a2-s1.wav" data-start="40.0" data-duration="3.0"></audio>
<video id="v-road" class="clip" src="media/road.mp4" data-start="10" data-duration="8" muted></video>
<video id="pip-w1" class="pip" src="media/pip/paul-w1.mp4" data-start="12.0" data-duration="10.0" data-track-index="7" muted></video>
<video id="pip-w2" class="pip" src="media/pip/paul-w2.mp4" data-start="41.0" data-duration="2.0" data-track-index="7" muted></video>
"""


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


segs = circle_audio.narration(HTML, 10, 30)
check("circle-01 only nx-* narration that starts inside the span is picked (the bed and the later act are left out)",
      [s[2] for s in segs] == ["audio/a1-s1.wav", "audio/a1-s2.wav"])
check("circle-02 the second segment is delayed by its distance from the first (20.0 - 10.5 s = 9500 ms), the first by 0",
      "adelay=0:all=1" in circle_audio.mix_graph(segs) and "adelay=9500:all=1" in circle_audio.mix_graph(segs))
check("circle-03 a span holding no narration returns nothing (main exits FAIL on it)", circle_audio.narration(HTML, 50, 60) == [])

wins = circle_cut.windows(HTML)
check("circle-04 only <video class=\"pip\"> elements are windows (the b-roll clip is not)",
      wins == [("media/pip/paul-w1.mp4", 12.0, 10.0), ("media/pip/paul-w2.mp4", 41.0, 2.0)])
cuts, uncovered = circle_cut.plan(wins, [("a.mp4", 10.5, 14.5), ("b.mp4", 40.0, 3.0)])
check("circle-05 each window seeks to its timeline start minus the start of the pass that covers it",
      cuts == [("media/pip/paul-w1.mp4", "a.mp4", 1.5, 10.0), ("media/pip/paul-w2.mp4", "b.mp4", 1.0, 2.0)] and not uncovered)
cuts, uncovered = circle_cut.plan(wins, [("a.mp4", 10.5, 11.0)])
check("circle-06 a window that runs past the end of its pass, or that no pass reaches, is named and not cut",
      cuts == [] and uncovered == ["media/pip/paul-w1.mp4", "media/pip/paul-w2.mp4"])

sys.exit(1 if FAILS else 0)
