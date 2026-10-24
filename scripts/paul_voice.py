#!/usr/bin/env python3
"""Put the narrator's cloned voice on Paul's on-camera clips, timing kept (owner 10 Oct 26: "On-camera Paul
clips (Flow) must end up in the same voice as the narrator"; 24 Oct 26: "you can change that to the cloned
voice, right?").

Route A from the El Reno voice work: OpenVoice V2 tone-colour conversion of the clip's own audio to the voice in
config.yaml external.voice_ref. The words, pace and timing are the clip's own, so Omni's lips stay in sync; only the
voice colour changes. No credits, no lipsync pass.

Runs with the pocket venv's Python (config.yaml external.pocket_venv_python); the OpenVoice source sits in
.models/openvoice/src and its converter weights in the Hugging Face cache (external.hf_home). librosa and soundfile
are not in that venv: the two calls OpenVoice makes are stubbed below with ffmpeg and the wave module.

Usage: <pocket python> scripts/paul_voice.py <clip.mp4> [<clip.mp4> ...]
Writes <clip base without -vN or -v5eq>-vc.mp4 beside each clip (never overwrites), loudness matched to the source
clip, and prints source and output duration and mean level per clip.
"""
import glob
import os
import re
import subprocess
import sys
import types
import wave

import numpy as np
import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = yaml.safe_load(open(os.path.join(HERE, "config.yaml"), encoding="utf-8"))["external"]
MAIN = os.path.dirname(os.path.dirname(os.path.dirname(HERE))) if os.sep + ".claude" + os.sep in HERE + os.sep else HERE
OV_SRC = os.path.join(MAIN, ".models", "openvoice", "src")
CKPT = glob.glob(os.path.join(CFG["hf_home"], "hub", "models--myshell-ai--OpenVoiceV2", "snapshots", "*", "converter"))[0]
VOICE_REF = CFG["voice_ref"]
NT = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def ff_load(path, sr=22050, **_):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True, check=True, creationflags=NT).stdout
    return np.frombuffer(raw, dtype=np.float32).copy(), sr


def wav_write(path, audio, sr):
    pcm = (np.clip(audio, -1, 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


librosa = types.ModuleType("librosa"); librosa.load = ff_load
librosa.filters = types.ModuleType("librosa.filters"); librosa.filters.mel = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("mel not stubbed"))
sys.modules["librosa"] = librosa; sys.modules["librosa.filters"] = librosa.filters
soundfile = types.ModuleType("soundfile"); soundfile.write = wav_write; sys.modules["soundfile"] = soundfile
# api.py imports the TTS text front end (inflect, eng_to_ipa ...); the converter never calls it.
ov_text = types.ModuleType("openvoice.text"); ov_text.text_to_sequence = None; sys.modules["openvoice.text"] = ov_text
# the converter's enable_watermark=False kwarg crashes its base class (upstream bug); a wavmark stub whose model is
# None makes add_watermark() a no-op instead.
wavmark = types.ModuleType("wavmark"); wavmark.load_model = lambda: type("NoMark", (), {"to": lambda self, d: None})(); sys.modules["wavmark"] = wavmark
sys.path.insert(0, OV_SRC)
import torch  # noqa: E402
from openvoice.api import ToneColorConverter  # noqa: E402


def mean_db(path):
    out = subprocess.run(["ffmpeg", "-i", path, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True, creationflags=NT).stderr
    return float(re.search(r"mean_volume: ([-\d.]+)", out).group(1))


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True, creationflags=NT).stdout.strip())


def main(clips):
    conv = ToneColorConverter(os.path.join(CKPT, "config.json"), device="cpu", enable_watermark=False)
    conv.load_ckpt(os.path.join(CKPT, "checkpoint.pth"))
    tgt = conv.extract_se([VOICE_REF])
    for clip in clips:
        base = re.sub(r"(-v\d+(eq)?)?\.mp4$", "", clip)
        out = base + "-vc.mp4"
        if os.path.exists(out):
            print("exists, kept:", out); continue
        wav = base + "-vc-src.wav"; cwav = base + "-vc.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-ac", "1", "-ar", "22050", wav], check=True, creationflags=NT)
        src = conv.extract_se([wav])
        conv.convert(audio_src_path=wav, src_se=src, tgt_se=tgt, output_path=cwav)
        gain = mean_db(clip) - mean_db(cwav)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-i", cwav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-af", f"volume={gain:.2f}dB,alimiter=limit=0.95", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True, creationflags=NT)
        os.remove(wav); os.remove(cwav)
        print(f"{os.path.basename(out)}  src {duration(clip):.3f} s {mean_db(clip):.1f} dB -> out {duration(out):.3f} s {mean_db(out):.1f} dB  {os.path.getsize(out)} B")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
