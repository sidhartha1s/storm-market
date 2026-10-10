"""Self-check for the presenter-circle tools: python3 scripts/test_circle.py

circle_audio.py must pick only narration inside the asked span (never insert audio), place each segment after the
first one and run the wav to the asked end; circle_cut.py must read only the circle's own windows, seek each one
inside the pass that covers it, and name a window no pass covers. Plain values in, plain values out: no ffmpeg run,
no model.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import circle_audio  # noqa: E402
import circle_cut  # noqa: E402

FAILS = []
HTML = """
<audio id="nx-a1-s1" src="audio/a1-s1.wav" data-start="10.5" data-duration="4.0"></audio>
<audio id="nx-ins1" src="media/insert/s1.wav" data-start="15.0" data-duration="3.0"></audio>
<audio id="nx-a1-s2" src="audio/a1-s2.wav" data-start="20.0" data-duration="5.0"></audio>
<audio id="bed-1" src="audio/bed.mp3" data-start="12.0" data-duration="60"></audio>
<audio id="nx-a2-s1" src="audio/a2-s1.wav" data-start="40.0" data-duration="3.0"></audio>
<video id="v-road" class="clip" src="media/road.mp4" data-start="10" data-duration="8" muted></video>
<video id="v-safe" class="clip pip-safe" src="media/safe.mp4" data-start="18" data-duration="4" muted></video>
<video id="pip-idle-w1" class="pip" src="media/pip/paul-idle-w1.mp4" data-start="12.0" data-duration="10.0" data-track-index="6" muted></video>
<video id="pip-w1" class="pip" src="media/pip/paul-w1.mp4" data-start="12.0" data-duration="10.0" data-track-index="7" muted></video>
<video id="pip-w2" class="pip" src="media/pip/paul-w2.mp4" data-start="41.0" data-duration="2.0" data-track-index="7" muted></video>
"""


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def after(args, flag):
    return args[args.index(flag) + 1]


segs = circle_audio.narration(HTML, 10, 30)
check("circle-01 only nx-* narration that starts inside the span is picked (the insert's voice, the bed and the later act are left out)",
      [s[2] for s in segs] == ["audio/a1-s1.wav", "audio/a1-s2.wav"])
check("circle-02 the second segment is delayed by its distance from the first (20.0 - 10.5 s = 9500 ms), the first by 0",
      "adelay=0:all=1" in circle_audio.mix_graph(segs) and "adelay=9500:all=1" in circle_audio.mix_graph(segs))
args = circle_audio.ffmpeg_args("ep", segs, 30, "out.wav")
check("circle-07 the wav is padded with silence and runs from the first word to the asked end (30 - 10.5 = 19.5 s), not to the last word",
      circle_audio.mix_graph(segs).endswith(",apad[m]") and after(args, "-t") == "19.500" and args.count("-i") == 2)
check("circle-03 a span holding no narration returns nothing (main exits FAIL on it)", circle_audio.narration(HTML, 50, 60) == [])

wins = circle_cut.windows(HTML)
check("circle-04 only <video id=\"pip-w..\" class=\"pip\"> elements are windows (not b-roll, not a pip-safe class, not the older idle loop)",
      wins == [("media/pip/paul-w1.mp4", 12.0, 10.0), ("media/pip/paul-w2.mp4", 41.0, 2.0)])
cuts, uncovered = circle_cut.plan(wins, [("a.mp4", 10.5, 14.5), ("b.mp4", 40.0, 3.0)])
check("circle-05 each window seeks to its timeline start minus the start of the pass that covers it",
      cuts == [("media/pip/paul-w1.mp4", "a.mp4", 1.5, 10.0), ("media/pip/paul-w2.mp4", "b.mp4", 1.0, 2.0)] and not uncovered)
cuts, uncovered = circle_cut.plan(wins, [("a.mp4", 10.5, 11.0)])
check("circle-06 a window that runs past the end of its pass, or that no pass reaches, is named and not cut",
      cuts == [] and uncovered == ["media/pip/paul-w1.mp4", "media/pip/paul-w2.mp4"])
args = circle_cut.cut_args("a.mp4", 1000, 1.5, 10.0, "o.mp4")
check("circle-08 a cut seeks before the input, lasts one frame past its window and crops by the face clip's width (1000 px: 868 px square at 66, 12)",
      args.index("-ss") < args.index("-i") and after(args, "-ss") == "1.500" and after(args, "-t") == "10.040"
      and after(args, "-vf") == "crop=868:868:66:12,scale=240:240:flags=lanczos")

sys.exit(1 if FAILS else 0)
