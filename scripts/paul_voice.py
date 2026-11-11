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

Usage: <pocket python> scripts/paul_voice.py <episode dir>            every mounted ins-paul-N clip in index.html
       <pocket python> scripts/paul_voice.py <clip.mp4> [<clip.mp4> ...]
Writes <clip base without -vN or -v5eq>-vc.mp4 beside each clip (never overwrites) at the episode's narration level
(median mean_volume of the nx- wavs; a bare clip keeps its own level), plus <out>.vc.json: voice_ref_md5, levels,
gain. render_preflight.py reads the sidecar and the level (the "Paul's voice" layer), so an unconverted or stale
clip never renders. Prints source and output duration and mean level per clip.
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


def main_checkout(repo):
    """A worktree's .git is a file naming .git/worktrees/<name>; the main checkout holds .models (same rule as snapshot_queue.py)."""
    git = os.path.join(repo, ".git")
    if os.path.isfile(git):
        return os.path.dirname(os.path.dirname(os.path.dirname(open(git, encoding="utf-8").read().split("gitdir:")[1].strip())))
    return repo


MAIN = main_checkout(HERE)
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


def md5(path):
    import hashlib
    return hashlib.md5(open(path, "rb").read()).hexdigest()


MOUNT = re.compile(r'<video[^>]*id="(ins-paul-\d+)"[^>]*src="([^"]+)"', re.I)


def bands(path, sr=16000):
    """(1 to 4 kHz, 4 to 8 kHz) energy over 0 to 1 kHz, in dB: the voice colour the owner hears as pitch."""
    x, _ = ff_load(path, sr)
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    f = np.fft.rfftfreq(len(x), 1 / sr)
    e = lambda lo, hi: float(spec[(f >= lo) & (f < hi)].sum())
    return 10 * np.log10(e(1000, 4000) / e(0, 1000)), 10 * np.log10(e(4000, 8000) / e(0, 1000))


def median(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2]


def episode_clips(episode):
    """(mount id, clip path) for every live ins-paul-N mount, and the narration's median level (dB) and colour (dB, dB)."""
    html = open(os.path.join(episode, "index.html"), encoding="utf-8").read()
    live = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    clips = [(i, os.path.join(episode, src)) for i, src in MOUNT.findall(live)]
    wavs = sorted(glob.glob(os.path.join(episode, "audio", "*.wav")))
    if not wavs:
        sys.exit(f"no narration wavs in {episode}/audio")
    level = median(mean_db(w) for w in wavs)
    sample = wavs[:: max(1, len(wavs) // 12)]  # the colour is stable across segments; the FFT is not free
    cols = [bands(w) for w in sample]
    return clips, level, (median(c[0] for c in cols), median(c[1] for c in cols))


def original(clip):
    """The Omni take behind a mounted file: a -vcN file names its source in its sidecar (never convert a conversion)."""
    if re.search(r"-vc\d*\.mp4$", clip):
        side = clip + ".vc.json"
        if not os.path.exists(side):
            sys.exit(f"{clip} is a converted file with no sidecar: name the Omni take instead")
        import json
        return os.path.join(os.path.dirname(clip), json.load(open(side, encoding="utf-8"))["source"])
    return clip


def eq_for(wav, col):
    """Two peaking filters that move wav's 1 to 4 kHz and 4 to 8 kHz bands onto the narration's."""
    c1, c2 = bands(wav)
    return f"equalizer=f=2000:t=o:w=2:g={col[0] - c1:.2f},equalizer=f=5657:t=o:w=1:g={col[1] - c2:.2f}"


def next_free(base):
    """<base>-vc.mp4, else -vc2, -vc3 ...: a converted file is never overwritten (owner: generated media gets -v2)."""
    n = 1
    while True:
        out = base + ("-vc.mp4" if n == 1 else f"-vc{n}.mp4")
        if not os.path.exists(out):
            return out
        n += 1


def main(targets):
    conv = ToneColorConverter(os.path.join(CKPT, "config.json"), device="cpu")
    conv.load_ckpt(os.path.join(CKPT, "checkpoint.pth"))
    tgt = conv.extract_se([VOICE_REF])
    jobs = []  # (clip, target level or None, target colour or None)
    for t in [t for t in targets if not t.startswith("--")]:
        if os.path.isdir(t):
            clips, nar, col = episode_clips(t)
            print(f"{os.path.basename(t)}: {len(clips)} ins-paul mounts, narration median {nar:.1f} dB, colour 1-4k {col[0]:.1f} dB, 4-8k {col[1]:.1f} dB")
            jobs += [(c, nar, col) for _, c in clips]
        else:
            jobs.append((t, None, None))
    import json
    for clip, nar, col in jobs:
        if re.search(r"-vc\d*\.mp4$", clip) and os.path.exists(clip + ".vc.json") and "--again" not in sys.argv:
            print("already converted:", clip); continue
        clip = original(clip)
        base = re.sub(r"(-v\d+(eq)?)?\.mp4$", "", clip)
        out = next_free(base)
        wav = base + "-vc-src.wav"; cwav = base + "-vc.wav"; ewav = base + "-vc-eq.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-ac", "1", "-ar", "22050", wav], check=True, creationflags=NT)
        src = conv.extract_se([wav])
        conv.convert(audio_src_path=wav, src_se=src, tgt_se=tgt, output_path=cwav)
        # the tone-colour conversion closes about 2 of the 5 dB between Omni's 1 to 4 kHz band and the narration's
        # (measured 30 Oct 26 on 18 clips); two peaking filters close the rest, measured again after.
        eq = ""
        if col is not None:
            eq = eq_for(cwav, col)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cwav, "-af", eq, ewav], check=True, creationflags=NT)
            eq += "," + eq_for(ewav, col)  # a peaking filter is not flat over its band: one residual pass
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cwav, "-af", eq or "anull", ewav], check=True, creationflags=NT)
        src_db = mean_db(clip)
        conv_db = mean_db(ewav)
        target = src_db if nar is None else nar
        gain = target - conv_db
        # apad + -shortest: the sound runs exactly as long as the picture, so a mount window sized on the take still fits
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-i", ewav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-af", f"volume={gain:.2f}dB,alimiter=limit=0.95,apad", "-c:a", "aac", "-b:a", "192k", "-shortest", out], check=True, creationflags=NT)
        os.remove(wav); os.remove(cwav); os.remove(ewav)
        out_db, out_col = mean_db(out), bands(out)
        json.dump({"voice_ref_md5": md5(VOICE_REF), "source": os.path.basename(clip), "source_db": src_db, "target_db": target,
                   "gain_db": round(gain, 2), "eq": eq, "out_db": out_db, "out_colour_db": [round(out_col[0], 2), round(out_col[1], 2)],
                   "narration_colour_db": col and [round(col[0], 2), round(col[1], 2)], "duration_s": duration(out)},
                  open(out + ".vc.json", "w", encoding="utf-8"), indent=1)
        print(f"{os.path.basename(out)}  src {duration(clip):.3f} s {src_db:.1f} dB -> out {duration(out):.3f} s {out_db:.1f} dB (target {target:.1f})"
              f"  colour 1-4k {out_col[0]:.1f} 4-8k {out_col[1]:.1f}" + (f" (narration {col[0]:.1f} {col[1]:.1f})" if col else "") + f"  {os.path.getsize(out)} B")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    import render_busy  # the heavy lock: one heavy job per machine (owner 26 Oct 26)
    with render_busy.heavy_lock("paul_voice " + os.path.basename(sys.argv[1].rstrip("\\/"))):
        main(sys.argv[1:])
