"""One long face pass for the presenter circle: Paul's portrait speaking a narration wav, on the ZBook's card.

SoulX-FlashHead Lite as its makers ship it (4 steps, 512 px, 25 fps, streaming audio in 0.96 s chunks, each chunk
carrying on from the last; no text prompt, nothing to batch). The one change from their generate_video.py: each chunk
is written to the mp4 as it is made. Theirs holds every chunk in memory until the end, about 75 MB per 0.96 s, which
a 16 GB machine cannot hold for minutes of video.

Runs with the FlashHead venv's own Python, never the system one. The install sits in the main checkout under
.models\\lipsync\\flashhead (gitignored; learnings/render.md "Presenter circle face" says how it was built) and is
found from the interpreter's path. Measured 10 Oct 26 on the RTX A2000: 53 s start-up, then 2.28 s per second of face.

Usage: <main checkout>\\.models\\lipsync\\flashhead\\venv\\Scripts\\python.exe scripts\\circle_face.py <narration.wav> <out.mp4> [portrait.jpg]
       (the wav comes from circle_audio.py; launch it hidden like a render, scripts\\run_hidden.vbs)
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


def main():
    audio, out = ARGS[0], ARGS[1]
    portrait = ARGS[2] if len(ARGS) > 2 else str(PORTRAIT)
    t_start = time.time()
    pipeline = get_pipeline(world_size=1, ckpt_dir=str(HOME / "flashhead" / "models" / "SoulX-FlashHead-1_3B"),
                            wav2vec_dir=str(HOME / "flashhead" / "models" / "wav2vec2-base-960h"), model_type="lite")
    get_base_data(pipeline, cond_image_path_or_dir=portrait, base_seed=SEED, use_face_crop=False)
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
    print(f"start-up {t_ready - t_start:.1f} s | {len(chunks)} chunks of {keep} frames | audio {len(speech) / rate:.1f} s", flush=True)

    tmp = out.replace(".mp4", "_tmp.mp4")
    with imageio.get_writer(tmp, format="mp4", mode="I", fps=fps, codec="h264", ffmpeg_params=["-bf", "0"]) as writer:
        for i, chunk in enumerate(chunks):
            heard.extend(chunk.tolist())
            embedding = get_audio_embedding(pipeline, np.array(heard), window_s * fps - p["frame_num"], window_s * fps)
            for frame in run_pipeline(pipeline, embedding)[p["motion_frames_num"]:].cpu().numpy().astype(np.uint8):
                writer.append_data(frame)
            if i % 50 == 0:
                print(f"chunk {i}/{len(chunks) - 1} | {time.time() - t_ready:.0f} s | card peak {torch.cuda.max_memory_allocated() / 2**20:.0f} MiB", flush=True)
    # no -shortest: the picture keeps its whole last chunk, so it is never shorter than the wav it was made from
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", audio, "-c:v", "copy", "-c:a", "aac", out], check=True)
    os.remove(tmp)
    made = len(chunks) * keep / fps
    print(f"DONE {out}: {made:.1f} s of face in {time.time() - t_start:.1f} s ({(time.time() - t_ready) / made:.2f} s per second of face after start-up)", flush=True)


if __name__ == "__main__":
    main()
