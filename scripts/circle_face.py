"""One long face pass for the presenter circle: Paul's portrait speaking a narration wav, on the ZBook's card.

SoulX-FlashHead Lite as its makers ship it (4 steps, 512 px, 25 fps, streaming audio in 0.96 s chunks, each chunk
carrying on from the last; no text prompt, nothing to batch). Two changes from their generate_video.py, neither to
the model: each chunk is written to the mp4 as it is made (theirs holds every chunk in memory until the end, about
75 MB per 0.96 s, which a 16 GB machine cannot hold for minutes of video), and the finished file keeps its whole last
chunk (theirs trims the picture to the sound).

Runs with the FlashHead venv's own Python, never the system one. The install sits in the main checkout under
.models\\lipsync\\flashhead (gitignored; learnings/render.md "Presenter circle face" says how it was built) and is
found from the interpreter's path. Measured times: learnings/render.md "Presenter circle face".

Usage: <main checkout>\\.models\\lipsync\\flashhead\\venv\\Scripts\\python.exe scripts\\circle_face.py <narration.wav> <out.mp4>
       (the wav comes from circle_audio.py; launch it hidden like a render, scripts\\run_hidden.vbs. The portrait is
       assets\\paul\\circle-portrait-560.jpg: circle_cut.py's crop is measured on that framing)
"""
import os
import subprocess
import sys
import time
from collections import deque
from pathlib import Path

HOME = Path(sys.executable).resolve().parents[3]  # ...\.models\lipsync
REPO = HOME / "flashhead" / "repo"
os.environ.setdefault("HF_HOME", str(HOME / "hf"))
os.environ.setdefault("HF_HUB_OFFLINE", "1")
ARGS = [str(Path(a).resolve()) for a in sys.argv[1:]]  # resolved before the chdir below
os.chdir(REPO)  # the model reads its yaml configs by relative path
sys.path.insert(0, str(REPO))

import imageio  # noqa: E402
import librosa  # noqa: E402
import numpy as np  # noqa: E402
import torch  # noqa: E402
from flash_head.inference import get_audio_embedding, get_base_data, get_infer_params, get_pipeline, run_pipeline  # noqa: E402

PORTRAIT = Path(__file__).resolve().parents[1] / "assets" / "paul" / "circle-portrait-560.jpg"
SEED = 42
# The RTX A2000 has 8 GB. A pass holds about 5.6 GB; with less free, Windows spills it into shared system memory and it
# runs about 10x slower (24 s per second of face instead of 2.0 to 2.3) without failing. Over the rate limit the pass
# alarms with one [SLOW] line and keeps running; the operator decides whether to free the card or stop it. Free memory
# read before start-up is not a usable test (Windows reported 4.6 GB free while passes ran at full speed).
MAX_S_PER_FACE_S = 4.5


def card_holders():
    """The processes on the card, as nvidia-smi lists them: what to close to free it."""
    try:  # the alarm must never stop the pass it reports on
        r = subprocess.run(["nvidia-smi", "--query-compute-apps=pid,process_name", "--format=csv,noheader"],
                           capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired) as e:
        return f"(nvidia-smi failed: {e})"
    return r.stdout.strip() or "(nvidia-smi listed none)"


def slow_line(i, face_rate, alarmed_at, holders=card_holders):
    """The [SLOW] alarm for chunk i, or None: from chunk 10 on, over the limit, at most once per 50 chunks."""
    if i < 10 or face_rate <= MAX_S_PER_FACE_S or (alarmed_at is not None and i - alarmed_at < 50):
        return None
    return (f"[SLOW] {face_rate:.1f} s per second of face after {i + 1} chunks (normal 2.0 to 2.3, limit {MAX_S_PER_FACE_S}): "
            f"the card is short of memory, still running. On the card now: {holders()}")


def main():
    audio, out = ARGS[0], ARGS[1]
    t_start = time.time()
    pipeline = get_pipeline(world_size=1, ckpt_dir=str(HOME / "flashhead" / "models" / "SoulX-FlashHead-1_3B"),
                            wav2vec_dir=str(HOME / "flashhead" / "models" / "wav2vec2-base-960h"), model_type="lite")
    get_base_data(pipeline, cond_image_path_or_dir=str(PORTRAIT), base_seed=SEED, use_face_crop=False)
    p = get_infer_params()
    rate, fps, window_s = p["sample_rate"], p["tgt_fps"], p["cached_audio_duration"]
    keep = p["frame_num"] - p["motion_frames_num"]  # new frames per chunk; the rest repeat the previous chunk's motion
    speech, _ = librosa.load(audio, sr=rate, mono=True)
    per_chunk = keep * rate // fps
    if len(speech) % per_chunk:
        speech = np.concatenate([speech, np.zeros(per_chunk - len(speech) % per_chunk, dtype=speech.dtype)])
    chunks = speech.reshape(-1, per_chunk)
    heard = deque([0.0] * (rate * window_s), maxlen=rate * window_s)  # the model always hears the last window_s seconds
    t_ready = time.time()
    alarmed_at = None
    recent = deque([t_ready], maxlen=21)  # chunk end times: the rate is the last 20 chunks', so a spill mid-pass shows
    print(f"start-up {t_ready - t_start:.1f} s | {len(chunks)} chunks of {keep} frames | audio {len(speech) / rate:.1f} s", flush=True)

    tmp = out[:-4] + "_tmp.mp4"  # picture only; the narration is muxed in below so a pass can be played and judged with its sound
    with imageio.get_writer(tmp, format="mp4", mode="I", fps=fps, codec="h264", ffmpeg_params=["-bf", "0"]) as writer:
        for i, chunk in enumerate(chunks):
            heard.extend(chunk.tolist())
            embedding = get_audio_embedding(pipeline, np.array(heard), window_s * fps - p["frame_num"], window_s * fps)
            for frame in run_pipeline(pipeline, embedding)[p["motion_frames_num"]:].cpu().numpy().astype(np.uint8):
                writer.append_data(frame)
            recent.append(time.time())
            alarm = slow_line(i, (recent[-1] - recent[0]) / ((len(recent) - 1) * keep / fps), alarmed_at)
            if alarm:
                print(alarm, flush=True)
                alarmed_at = i
            if i % 50 == 0:
                print(f"chunk {i}/{len(chunks) - 1} | {time.time() - t_ready:.0f} s | card peak {torch.cuda.max_memory_allocated() / 2**20:.0f} MiB", flush=True)
    # no -shortest: the picture keeps its whole last chunk, so it is never shorter than the wav it was made from
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", audio, "-c:v", "copy", "-c:a", "aac", out], check=True)
    os.remove(tmp)
    made = len(chunks) * keep / fps
    print(f"DONE {out}: {made:.1f} s of face in {time.time() - t_start:.1f} s ({(time.time() - t_ready) / made:.2f} s per second of face after start-up)", flush=True)


if __name__ == "__main__":
    import render_busy  # the heavy lock: one heavy job per machine (owner 26 Oct 26)
    with render_busy.heavy_lock("face pass " + Path(ARGS[0]).name):
        main()
