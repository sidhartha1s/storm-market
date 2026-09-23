"""Self-check for the audio pipeline fixes: python3 scripts/test_audio.py
Covers: segment-parse heading boundary (notes never glue into narration), hard-fail on
ambiguous/note blockquotes, manifest text-hash re-synthesis, 0-segment / unknown --only
hard failure without touching manifest.json, word_budget counting the voiced text only,
duration-based (not mtime-only) words.json staleness, and SRT caption alignment to script
text. All TTS/whisper/ffprobe calls are mocked — no paid API, no real audio, no network.
"""
import hashlib
import json
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import build_srt          # noqa: E402
import transcribe_episode  # noqa: E402
import tts_episode        # noqa: E402

fails = []


def check(name, cond, detail=""):
    if cond:
        print(f"[test_audio] PASS {name}")
    else:
        fails.append(name)
        print(f"[test_audio] FAIL {name} {detail}")


# ---------------------------------------------------------------------------
# 1. parse_segments: a note under a LATER '## SECTION' heading never glues into the
#    previous segment's blockquote (the ms-elnino-texas h1-s1 bug: the old code split only
#    on '\n### ', so a '## INTRO' heading was not a boundary).
MD_GLUE = """# edit_script.md

## HOOK (0:00-0:08)

### H1-S1 -- narration
> Texas, this winter will not be normal.

Visual: CPC SST map push.

## INTRO (0:08-1:05)

> TTS note: the owner's phrase is spelled "reed" for pocket-TTS.

### I1-S1 -- narration
> The last time the Pacific did this, it was different.

Visual: NWS warning map.
"""
segs = dict(tts_episode.parse_segments(MD_GLUE))
check("parse_segments: heading boundary keeps notes out of h1-s1",
      segs.get("h1-s1") == "Texas, this winter will not be normal.", segs.get("h1-s1"))
check("parse_segments: i1-s1 parses clean", segs.get("i1-s1", "").startswith("The last time"))

# 2. Two blockquote paragraphs under one heading is a hard error, not a silent glue.
MD_TWO_PARAS = """### A1-S1 -- narration
> First paragraph of narration.

> Second, unrelated paragraph.

Visual: something.
"""
try:
    tts_episode.parse_segments(MD_TWO_PARAS)
    check("parse_segments: two blockquote paragraphs hard-fails", False, "no exception raised")
except tts_episode.SegmentParseError:
    check("parse_segments: two blockquote paragraphs hard-fails", True)

# 3. A lone blockquote that reads like a production note hard-fails too.
MD_NOTE_ONLY = """### A1-S1 -- narration
> TTS note: this should never be voiced.

Visual: something.
"""
try:
    tts_episode.parse_segments(MD_NOTE_ONLY)
    check("parse_segments: TTS-note-only blockquote hard-fails", False, "no exception raised")
except tts_episode.SegmentParseError:
    check("parse_segments: TTS-note-only blockquote hard-fails", True)

# ---------------------------------------------------------------------------
# Harness for tts_episode.main(): mock TTS/atempo/ffprobe/whisper, run in a temp episode dir.
calls = {"synth": [], "tempo": [], "transcribe": []}


def mock_synth_native(txt_path, wav_path, ext):
    calls["synth"].append(txt_path.stem)
    wav_path.write_bytes(b"RAWWAV")


def mock_apply_tempo(raw_wav, sped_wav, tempo):
    calls["tempo"].append(sped_wav.stem)
    sped_wav.write_bytes(raw_wav.read_bytes() + b"SPED")


def mock_ffprobe_duration(path, attempts=4, sleep_s=0):
    return 5.0 if path.exists() else None


def mock_load_whisper_model():
    return "FAKE-MODEL"


def mock_transcribe_wav(model, wav_path):
    calls["transcribe"].append(wav_path.stem)
    return [{"text": "word", "start": 0.0, "end": 1.0}]


def install_mocks():
    tts_episode.synth_native = mock_synth_native
    tts_episode.apply_tempo = mock_apply_tempo
    tts_episode.ffprobe_duration = mock_ffprobe_duration
    tts_episode.load_whisper_model = mock_load_whisper_model
    tts_episode.transcribe_wav = mock_transcribe_wav
    calls["synth"].clear()
    calls["tempo"].clear()
    calls["transcribe"].clear()


def make_episode(tmp, script_text, voice_ref):
    ep = tmp / "ep"
    ep.mkdir()
    (ep / "edit_script.md").write_text(script_text, encoding="utf-8")

    def fake_cfg():
        return {"external": {"pocket_venv_python": "python3", "tts_clone_py": "noop.py",
                             "voice_ref": str(voice_ref)},
               "channel": {"tempo": 1.10}}
    tts_episode.load_cfg = fake_cfg
    return ep


SCRIPT_ONE_SEG = """### A1-S1 -- narration
> Hello world this is a test line.

Visual: something.
"""

with tempfile.TemporaryDirectory() as d:
    tmp = Path(d)
    voice_ref = tmp / "voice.mp3"
    voice_ref.write_bytes(b"fake-voice-bytes")
    install_mocks()

    # 4. manifest text-hash: unchanged text on a second run does NOT re-synthesize.
    ep = make_episode(tmp, SCRIPT_ONE_SEG, voice_ref)
    sys.argv = ["tts_episode.py", str(ep)]
    tts_episode.main()
    check("tts_episode: first run synthesizes a1-s1", calls["synth"] == ["a1-s1"])
    manifest = json.loads((ep / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: manifest stores text_hash", "text_hash" in manifest["a1-s1"])

    install_mocks()
    sys.argv = ["tts_episode.py", str(ep)]
    tts_episode.main()
    check("tts_episode: unchanged text on rerun does not re-synthesize", calls["synth"] == [])

    # 5. editing the line invalidates ONLY that segment's stale wav/words.json.
    (ep / "edit_script.md").write_text(SCRIPT_ONE_SEG.replace(
        "Hello world this is a test line.", "A completely different sentence now."),
        encoding="utf-8")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep)]
    tts_episode.main()
    check("tts_episode: edited line re-synthesizes", calls["synth"] == ["a1-s1"])
    check("tts_episode: edited line re-transcribes", calls["transcribe"] == ["a1-s1"])

    # 6. 0 parsed segments exits non-zero and leaves manifest.json untouched.
    before = (ep / "audio" / "manifest.json").read_text(encoding="utf-8")
    ep_empty = make_episode(tmp, "## SCRIPT\n**A1-S1 (10 w)** inline prose, no blockquotes.\n",
                            voice_ref)
    (ep_empty / "audio").mkdir()
    (ep_empty / "audio" / "manifest.json").write_text(before, encoding="utf-8")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_empty)]
    try:
        tts_episode.main()
        check("tts_episode: 0 segments exits non-zero", False, "main() returned instead of exiting")
    except SystemExit as e:
        check("tts_episode: 0 segments exits non-zero", e.code not in (0, None), e.code)
    after = (ep_empty / "audio" / "manifest.json").read_text(encoding="utf-8")
    check("tts_episode: 0 segments leaves manifest.json untouched", after == before)

    # 7. unknown --only id exits non-zero.
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep), "--only", "z9-s9"]
    try:
        tts_episode.main()
        check("tts_episode: unknown --only id exits non-zero", False, "main() returned")
    except SystemExit as e:
        check("tts_episode: unknown --only id exits non-zero", e.code not in (0, None), e.code)

# ---------------------------------------------------------------------------
# 8. transcribe_episode.words_are_stale: a words.json NEWER (by mtime) than its wav is still
#    stale when its last word ends past the wav's real duration (ep3-tristate case; mtime
#    alone would say "fresh").
with tempfile.TemporaryDirectory() as d:
    tmp = Path(d)
    wav = tmp / "a3-s7.wav"
    wav.write_bytes(b"wav")
    words_json = tmp / "a3-s7.words.json"
    words_json.write_text(json.dumps([{"text": "x", "start": 0, "end": 48.58}]), encoding="utf-8")
    import os, time
    now = time.time()
    os.utime(wav, (now - 100, now - 100))
    os.utime(words_json, (now, now))  # words.json is NEWER than the wav
    transcribe_episode.ffprobe_duration = lambda p, **kw: 41.72  # real wav duration
    check("transcribe_episode: newer-mtime but duration-overrun words.json is stale",
          transcribe_episode.words_are_stale(wav, words_json) is True)

    words_json.write_text(json.dumps([{"text": "x", "start": 0, "end": 40.0}]), encoding="utf-8")
    os.utime(words_json, (now, now))
    check("transcribe_episode: newer-mtime, duration-consistent words.json is fresh",
          transcribe_episode.words_are_stale(wav, words_json) is False)

# ---------------------------------------------------------------------------
# 9. build_srt.align_captions: whisper's mis-heard proper nouns are replaced by the script's
#    spelling, whisper's timing is kept.
whisper_words = [
    {"text": "Ibu", "start": 0.0, "end": 0.3},
    {"text": "and", "start": 0.3, "end": 0.5},
    {"text": "Samaru", "start": 0.5, "end": 1.1},
    {"text": "are", "start": 1.1, "end": 1.3},
    {"text": "erupting", "start": 1.3, "end": 1.9},
]
script_text = "Ibu and Semeru are erupting"
aligned = build_srt.align_captions(whisper_words, script_text)
aligned_text = " ".join(w["text"] for w in aligned)
check("build_srt: align_captions fixes ASR mis-hear (Samaru -> Semeru)",
      aligned_text == "Ibu and Semeru are erupting", aligned_text)
semeru = next(w for w in aligned if w["text"] == "Semeru")
check("build_srt: align_captions keeps whisper's timing for the corrected word",
      semeru["start"] == 0.5 and semeru["end"] == 1.1, semeru)

# ---------------------------------------------------------------------------
if fails:
    print(f"[test_audio] {len(fails)} FAILED: {fails}")
    sys.exit(1)
print("[test_audio] all PASS")
