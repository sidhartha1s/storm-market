#!/usr/bin/env python3
"""English TTS via Kyutai Pocket-TTS, cloning an owner-supplied voice reference.

Uses the *english* model (english_2026-04). The voice reference is passed via
--voice (set in config.yaml) and normalized to 24kHz mono PCM here, so any input
format works (e.g. an ElevenLabs mp3). One segment per sentence of the text
file -> concat -> stereo, loudness-normalized wav.

MUST run in this repo's voice venv (`config.yaml external.pocket_venv_python`); `tts_episode.py`
calls it. The model files and the Hugging Face login live in `external.hf_home` (voice_tool.py).
"""
import argparse, hashlib, os, re, shutil, subprocess, sys
from pathlib import Path

import voice_tool

HERE = Path(__file__).resolve().parent.parent
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
# probe() runs once per sentence segment — without this flag each spawn flashes a new console
# window on Windows even though the parent already has one.
NT_FLAGS = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0

# Heteronyms Kyutai voices with the wrong default reading, respelled SYNTH-ONLY as homophones of
# the intended sound. script.txt stays canonical (captions/factcheck read it), and validate_tts can
# NEVER catch these — whisper writes the same letters whichever way the word was voiced, so the
# transcript diff is blind to them (ep5 shipped "wind down" as /wɪnd/ 5 times; only an ear-check or
# this map prevents it). Matched on word boundaries, case-insensitive; extend as episodes surface more.
HETERONYM_RESPELL = {
    "wind down": "wined down", "winds down": "wines down", "winding down": "wining down",
    "wind up": "wined up", "winds up": "wines up", "winding up": "wining up",
}


def normalize_for_synth(raw):
    """SYNTH-ONLY text normalization (the on-disk script is never rewritten).

    - em/en dashes -> commas: pocket-TTS renders a dash as an over-long dead pause (robotic — the
      ep4 hook), and dash-chained sentences are exactly the overlong segments that hallucinate at
      the tail. NOTE: the substituted comma is still voiced as a HARD break (the ep5 hook's paired
      dashes read as three separate sentences) — this model has no softer pause, so a paired-dash
      parenthetical whose break is unwanted must be rephrased at authoring time.
    - heteronym respell per HETERONYM_RESPELL, preserving a leading capital.
    """
    raw = re.sub(r"\s*[—–]+\s*", ", ", raw)
    raw = re.sub(r",(\s*,)+", ",", raw)          # "— ," chains -> a single comma
    raw = re.sub(r",\s*([.?!])", r"\1", raw)     # a dash that closed a sentence -> drop the comma
    for phrase, spoken in HETERONYM_RESPELL.items():
        def _sub(m, spoken=spoken):
            return spoken[0].upper() + spoken[1:] if m.group(0)[0].isupper() else spoken
        raw = re.sub(rf"\b{phrase}\b", _sub, raw, flags=re.IGNORECASE)
    return raw


def segment_htag(text: str, voice_md5: str) -> str:
    """The per-segment cache stamp: a changed sentence gets a changed tag, so a reworded script
    regenerates that segment instead of silently reusing the byte-identical old clip at the same
    index (index-only caching shipped stale audio once). The voice reference is part of the stamp
    for the same reason: a new voice must never reuse a sentence the old voice spoke."""
    return hashlib.sha1(f"{text}\x1f{voice_md5}".encode("utf-8")).hexdigest()[:8]


def probe(p: Path) -> float:
    try:
        out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                              "-of", "default=nk=1:nw=1", str(p)], capture_output=True, text=True,
                             creationflags=NT_FLAGS)
        return float(out.stdout.strip())
    except (ValueError, FileNotFoundError):
        return 0.0


# Split into SENTENCES: pocket-TTS silently truncates inputs over ~50 tokens,
# so each segment must stay short. Sentences longer than MAX_WORDS are further
# sub-split on clause punctuation (the model drops words otherwise -> mis-voiced figures).
MAX_WORDS = 24   # spelled-out numbers inflate token count; keep chunks well under the ~50-token
                 # cap. Was 34: a 29-word two-dash sentence still degenerated into tail babble
                 # (ep4 "sixty-five degrees Fahrenheit" -> 4s of gibberish), so the cap now
                 # forces a clause split well before the danger zone.


def subsplit(sent):
    if len(sent.split()) <= MAX_WORDS:
        return [sent]
    out, cur = [], ""
    for part in [p.strip() for p in re.split(r"[,;:]", sent) if p.strip()]:
        if cur and len((cur + " " + part).split()) > MAX_WORDS:
            out.append(cur); cur = part
        else:
            cur = f"{cur}, {part}" if cur else part
    if cur:
        out.append(cur)
    # a clause with no punctuation at all can still blow the cap — hard-split it on word count
    final = []
    for seg in out:
        ws = seg.split()
        while len(ws) > MAX_WORDS:
            final.append(" ".join(ws[:MAX_WORDS])); ws = ws[MAX_WORDS:]
        final.append(" ".join(ws))
    return final


# Designed pauses (owner 15 Oct 26: "periods, commas have same mute length"). Each sentence is voiced
# alone, so the gap between two of them used to be the model's own edge silence: measured 0.87 s at
# EVERY sentence end (0.45 lead + 0.42 trail), whatever the sentence did. synth_file now trims each
# clip's edges and puts this chosen gap between them instead. The owner picked these values by ear
# on the Joplin hook (designed vs tight 0.28 s vs untouched 0.87 s).
# Bump PAUSES on any change to gap_after or TRIM_EDGES: tts_episode folds it into its stale hash,
# so every segment re-joins with the new pauses instead of silently keeping the old ones.
PAUSES = "designed-1"


def gap_after(lines, i):
    """Seconds of silence after lines[i]; 0 after the last line."""
    if i == len(lines) - 1:
        return 0.0
    cur = lines[i].rstrip()
    if not cur.endswith((".", "?", "!")):
        return 0.18     # a subsplit clause boundary inside one sentence: a comma-length breath
    if sum(any(c.isalpha() for c in w) for w in lines[i + 1].split()) <= 3:  # a stray quote is not a word
        return 0.65     # a beat before a short kicker ("Not one.")
    if cur.endswith("?"):
        return 0.55     # let a question land
    return 0.32


TRIM_EDGES = ("silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.03,areverse,"
              "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.06,areverse")


def prepare_lines(text_file):
    """Text file -> the synth lines, with the prosody report printed before any synthesis."""
    orig = " ".join(Path(text_file).read_text(encoding="utf-8").split())
    raw = normalize_for_synth(orig)
    sentences = [s.strip() for s in re.findall(r"[^.?!]+[.?!]+", raw) if s.strip()]
    lines = [seg for s in sentences for seg in subsplit(s)]
    if not lines:
        sys.exit(f"empty text file: {text_file}")

    # Prosody report — LOUD, before synthesis, so mis-phrased authoring is caught while a rewrite
    # is still a script edit, not a re-record. Both constructs voice as sentence-like breaks:
    # paired dashes become hard-break commas, and every subsplit boundary is a separate segment.
    paired = [s.strip() for s in re.findall(r"[^.?!]+[.?!]+", orig) if len(re.findall(r"[—–]", s)) >= 2]
    split_n = sum(1 for s in sentences if len(subsplit(s)) > 1)
    if paired:
        print(f"[tts_clone] PROSODY WARNING: {len(paired)} paired-dash parenthetical(s) will voice "
              f"as separate sentences (no soft pause in this model) — rephrase at authoring if "
              f"unwanted. First: {paired[0][:90]!r}", flush=True)
    if split_n:
        print(f"[tts_clone] PROSODY WARNING: {split_n} sentence(s) over {MAX_WORDS} words synthesize "
              f"as 2+ segments with sentence-like breaks at the split points.", flush=True)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-file", default=str(HERE / "audio" / "script.txt"))
    ap.add_argument("--out", default=str(HERE / "audio" / "narration.wav"))
    ap.add_argument("--batch", help="TSV file, one '<text-file>\\t<out-wav>' per line: load the model "
                                    "and clone the voice ONCE for all of them (replaces --text-file/--out)")
    ap.add_argument("--voice", required=True, help="path to the voice reference wav (from config.yaml; no in-code default to keep this repo isolated)")
    ap.add_argument("--no-quantize", action="store_true")
    args = ap.parse_args()

    if args.batch:
        pairs = [l.split("\t") for l in Path(args.batch).read_text(encoding="utf-8").splitlines() if l.strip()]
        if not pairs or any(len(p) != 2 for p in pairs):
            sys.exit(f"--batch {args.batch}: need one '<text-file>\\t<out-wav>' per line")
    else:
        pairs = [(args.text_file, args.out)]
    # every text is split (and its prosody report printed) before the model loads, so a bad
    # input fails in seconds rather than after the load
    jobs = [(prepare_lines(t), Path(o).resolve()) for t, o in pairs]

    voice_ref = Path(args.voice)
    if not voice_ref.exists():
        sys.exit(f"voice ref not found: {voice_ref}")
    voice_md5 = voice_tool.voice_md5(voice_ref)

    seg_dir = jobs[0][1].parent / "_segments"
    seg_dir.mkdir(parents=True, exist_ok=True)

    # Normalize the reference to the format pocket-TTS clones cleanly from: 24kHz mono PCM,
    # capped at 30s. Accepts any input (e.g. a 44.1k mp3). A long prompt (>~40s) makes
    # get_state_for_audio_prompt emit gibberish (verified: 72s ref -> "AAAA"); 30s clones clean.
    ref_wav = seg_dir / "_voiceref_24k.wav"
    cv = subprocess.run([FFMPEG, "-y", "-i", str(voice_ref), "-t", "30", "-ac", "1", "-ar", "24000",
                         "-c:a", "pcm_s16le", str(ref_wav)], capture_output=True, text=True,
                        creationflags=NT_FLAGS)
    if cv.returncode != 0 or not ref_wav.exists():
        sys.exit(f"voice-ref normalize failed: {cv.stderr}")
    voice_ref = ref_wav

    voice_tool.use_repo_models()  # before pocket_tts: huggingface_hub reads HF_HOME at import
    from pocket_tts.models.tts_model import TTSModel
    from pocket_tts.data.audio import stream_audio_chunks
    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    # int8 dynamic quantization (torch's `quantized::linear_dynamic` op) has no CUDA kernel --
    # it is CPU-only by PyTorch design. Force it off on GPU rather than crash mid-clone.
    quantize = (not args.no_quantize) and device == "cpu"
    print(f"Loading pocket-TTS (english, quantize={quantize}, device={device})...", flush=True)
    model = TTSModel.load_model(language="english", quantize=quantize)
    model.to(device)
    print(f"Cloning voice from {voice_ref.name}...", flush=True)
    voice_state = model.get_state_for_audio_prompt(str(voice_ref))
    sr = model.config.mimi.sample_rate

    for lines, out in jobs:
        synth_file(model, voice_state, voice_md5, sr, stream_audio_chunks, lines, out)


def trim_and_pad(seg, gap):
    """seg's edge silence cut to a few hundredths, then gap seconds of silence appended."""
    out = seg.with_name(f"paused_{seg.name}")
    r = subprocess.run([FFMPEG, "-y", "-i", str(seg), "-af", f"{TRIM_EDGES},apad=pad_dur={gap}",
                        "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le", str(out)],
                       capture_output=True, text=True, creationflags=NT_FLAGS)
    if r.returncode != 0:
        sys.exit(f"edge trim failed for {seg.name}: {r.stderr}")
    return out


def synth_file(model, voice_state, voice_md5, sr, stream_audio_chunks, lines, out):
    """Synthesize the lines sentence by sentence into out, then concat + loudnorm."""
    seg_dir = out.parent / "_segments"
    seg_dir.mkdir(parents=True, exist_ok=True)
    seg_paths, failed = [], []
    for i, text in enumerate(lines, 1):
        seg = seg_dir / f"segment_{i:02d}_{segment_htag(text, voice_md5)}.wav"
        if seg.exists() and probe(seg) > 1.0:
            print(f"  [{i}] exists, skip", flush=True); seg_paths.append(seg); continue
        print(f"  [{i}] {text[:60]}...", flush=True)
        try:
            chunks = model.generate_audio_stream(model_state=voice_state, text_to_generate=text)
            stream_audio_chunks(str(seg), chunks, sr)
            if probe(seg) <= 0.35:  # short sentences ("Their offer?") are valid; only flag near-silent
                raise RuntimeError(f"suspicious duration {probe(seg):.2f}s")
            seg_paths.append(seg)
        except Exception as e:
            print(f"  [{i}] FAILED ({e})", file=sys.stderr, flush=True); failed.append(i)

    if failed:
        sys.exit(f"FAILED segments: {failed}")

    # trim every clip's edge silence and pad its designed gap (gap_after) in one pass; the cached
    # segments stay untouched, so a gap change never re-voices anything
    seg_paths = [trim_and_pad(seg, gap_after(lines, i)) for i, seg in enumerate(seg_paths)]

    concat = seg_dir / "concat.txt"
    concat.write_text("".join(f"file '{p.name}'\n" for p in seg_paths))
    # -ar/-ac pinned (2026-07-17 mute-tail RCA): loudnorm internally resamples to 192kHz; without an
    # explicit output rate ffmpeg once wrote a corrupted 192kHz/stereo wav whose real content covered
    # only ~28% of the narration — the silent-tail final. Mono 24k matches the segment spec.
    r = subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
                        "-af", "loudnorm=I=-16:TP=-1.5",
                        "-ar", "24000", "-ac", "1",
                        "-c:a", "pcm_s16le", str(out)],
                       capture_output=True, text=True, cwd=str(seg_dir), creationflags=NT_FLAGS)
    if r.returncode != 0 or not out.exists():
        sys.exit(f"ffmpeg concat error: {r.stderr}")
    seg_durs = [probe(p) for p in seg_paths]
    if any(d <= 0 for d in seg_durs):
        bad = [p.name for p, d in zip(seg_paths, seg_durs) if d <= 0]
        sys.exit(f"segment probe failed (0s duration) for: {bad[:5]} — refusing to concat")
    seg_total = sum(seg_durs)
    out_dur = probe(out)
    if abs(out_dur - seg_total) > 2.0:
        sys.exit(f"concat output {out_dur:.1f}s != segment total {seg_total:.1f}s — "
                 "corrupted concat (2026-07-17 mute-tail class); refusing to write short narration")
    print(f"\nSaved {out} ({out_dur:.1f}s, segments {seg_total:.1f}s)")


if __name__ == "__main__":
    main()
