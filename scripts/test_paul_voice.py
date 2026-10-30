"""The "Paul's voice" layer in render_preflight.py catches an ins-paul clip that did not go through paul_voice.py:
python3 scripts/test_paul_voice.py

Cases on a throwaway episode made with ffmpeg tone generators (a 120 Hz "narration" wav with a fixed colour):
an unconverted mount (-v3), a -vc file with no sidecar, a sidecar from another voice_ref, a converted file 6 dB
hot, a converted file whose colour is still Omni's (same level, 1 to 4 kHz boosted 6 dB), and a proper one (pass).
Why: on 30 Oct 26 three episodes had rendered drafts with Omni's own voice on all 18 clips; nothing had checked.
"""
import json
import yaml
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import render_preflight as rp  # noqa: E402

VOICE = "anoisesrc=color=pink:seed=7:duration=4,volume=-20dB"  # one fixed spectrum the narration wavs and the clips share


def make_wav(path, extra=""):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", VOICE + extra, "-ar", "16000", "-ac", "1", str(path)], check=True)


def make_mp4(path, extra=""):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=black:s=64x64:d=4", "-f", "lavfi", "-i", VOICE + extra,
                    "-c:v", "libx264", "-c:a", "aac", "-shortest", str(path)], check=True)


def mount(src):
    return f'<video id="ins-paul-1" src="{src}" data-start="0" data-duration="3" data-track-index="1" data-volume="1"></video>'


def main():
    root = Path(tempfile.mkdtemp(prefix="pv-test-"))
    try:
        ep = root / "episodes" / "ep-test-voice"
        (ep / "audio").mkdir(parents=True)
        (ep / "media" / "paul").mkdir(parents=True)
        shutil.copy(HERE.parent / "config.yaml", root / "config.yaml")
        md5 = yaml.safe_load((root / "config.yaml").read_text(encoding="utf-8"))["external"]["voice_ref_md5"]
        for n in range(3):
            make_wav(ep / "audio" / f"a1-s{n}.wav")
        paul = ep / "media" / "paul"
        make_mp4(paul / "ins-paul-1-v3.mp4", ",equalizer=f=2000:t=o:w=2:g=12")  # Omni: bright
        make_mp4(paul / "ins-paul-1-vc.mp4")  # a proper conversion: same colour and level as the narration
        make_mp4(paul / "ins-paul-1-vc2.mp4", ",volume=6dB")
        make_mp4(paul / "ins-paul-1-vc3.mp4", ",equalizer=f=2000:t=o:w=2:g=12")
        good = {"voice_ref_md5": md5, "source": "ins-paul-1-v3.mp4"}
        for name in ("ins-paul-1-vc.mp4", "ins-paul-1-vc2.mp4", "ins-paul-1-vc3.mp4"):
            (paul / (name + ".vc.json")).write_text(json.dumps(good), encoding="utf-8")

        def gap(src, sidecar=None):
            if sidecar is not None:
                (paul / (Path(src).name + ".vc.json")).write_text(json.dumps(sidecar), encoding="utf-8")
            return rp._voice_gap(rp._mounts(mount(src)), ep)

        cases = [
            ("unconverted -v3 mount", gap("media/paul/ins-paul-1-v3.mp4"), "not a -vc file"),
            ("converted 6 dB hot", gap("media/paul/ins-paul-1-vc2.mp4"), "level"),
            ("converted, still Omni's colour", gap("media/paul/ins-paul-1-vc3.mp4"), "colour"),
            ("sidecar from another voice_ref", gap("media/paul/ins-paul-1-vc.mp4", {"voice_ref_md5": "0" * 32, "source": "x"}), "another voice_ref"),
        ]
        for label, finding, word in cases:
            assert finding and word in finding, f"{label}: expected '{word}', got {finding!r}"
            print(f"  blocks: {label}: {finding[:90]}")
        os.remove(paul / "ins-paul-1-vc.mp4.vc.json")
        finding = gap("media/paul/ins-paul-1-vc.mp4")
        assert finding and "no ins-paul-1-vc.mp4.vc.json" in finding, finding
        print(f"  blocks: -vc with no sidecar: {finding[:90]}")
        (paul / "ins-paul-1-vc.mp4.vc.json").write_text(json.dumps(good), encoding="utf-8")
        finding = gap("media/paul/ins-paul-1-vc.mp4")
        assert finding is None, f"a proper conversion must pass, got {finding!r}"
        print("  passes: a -vc file with the current voice_ref sidecar at the narration's level and colour")
        print("[test_paul_voice] ok: 5 blocked, 1 passed")
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    main()
