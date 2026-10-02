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
    calls["tempo"].append((sped_wav.stem, tempo))
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


def make_episode(tmp, script_text, voice_ref, name="ep"):
    ep = tmp / name
    ep.mkdir()
    (ep / "edit_script.md").write_text(script_text, encoding="utf-8")

    def fake_cfg():
        return {"external": {"pocket_venv_python": "python3", "tts_clone_py": "noop.py",
                             "voice_ref": str(voice_ref)},
               "channel": {"tempo": 1.10, "tempo_by_prefix": {"sh-": 1.16}}}
    tts_episode.load_cfg = fake_cfg
    return ep


# 3b. resolve_tempo: shorts (sh-) get the per-lane override, everything else the default.
_CFG = {"channel": {"tempo": 1.10, "tempo_by_prefix": {"sh-": 1.16}}}
check("resolve_tempo: sh- slug resolves to the shorts override (1.16)",
      tts_episode.resolve_tempo(_CFG, "sh-hawaii-lowell-1") == 1.16)
check("resolve_tempo: ms- slug resolves to the default (1.10)",
      tts_episode.resolve_tempo(_CFG, "ms-elnino-texas") == 1.10)
check("resolve_tempo: ep- slug resolves to the default (1.10)",
      tts_episode.resolve_tempo(_CFG, "ep3-tristate") == 1.10)


SCRIPT_ONE_SEG = """# edit_script.md

### A1-S1 -- narration
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

    # 4b. end-to-end: an episode dir named sh-* is synthesized at the shorts tempo (1.16),
    #     recorded in its manifest; a non-sh- episode (ep/, above) stays at the default (1.10).
    ep_short = make_episode(tmp, SCRIPT_ONE_SEG, voice_ref, name="sh-test-1")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_short)]
    tts_episode.main()
    short_manifest = json.loads((ep_short / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: sh- episode manifest records tempo 1.16",
          short_manifest["a1-s1"]["tempo"] == 1.16, short_manifest["a1-s1"])
    check("tts_episode: non-sh- episode manifest records the default tempo 1.10",
          manifest["a1-s1"]["tempo"] == 1.10, manifest["a1-s1"])

    # 4c. '(tempo 1.0)' on one heading slows that segment only; the untagged one keeps the lane
    #     tempo. Adding the tag later re-synthesizes just the tagged segment.
    two = SCRIPT_ONE_SEG + "\n### A1-S2 -- narration\n> Then it grew.\n"
    ep_pace = make_episode(tmp, two, voice_ref, name="ep-pace")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_pace)]
    tts_episode.main()
    (ep_pace / "edit_script.md").write_text(two.replace("### A1-S2 -- narration", "### A1-S2 -- narration (tempo 1.0)"),
                                           encoding="utf-8")
    install_mocks()
    tts_episode.main()
    pace = json.loads((ep_pace / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: (tempo 1.0) heading records 1.0 for that segment only",
          pace["a1-s2"]["tempo"] == 1.0 and pace["a1-s1"]["tempo"] == 1.10, pace)
    check("tts_episode: adding a tempo tag re-synthesizes only the tagged segment", calls["synth"] == ["a1-s2"], calls)
    check("tts_episode: the tagged segment's wav is sped at 1.0, not the lane tempo",
          calls["tempo"] == [("a1-s2", 1.0)], calls["tempo"])

    # 4d. a heading that mentions tempo in an unreadable form fails loudly, never voices at the lane tempo.
    (ep_pace / "edit_script.md").write_text(two.replace("### A1-S2 -- narration", "### A1-S2 -- narration (tempo: 1.0)"),
                                           encoding="utf-8")
    try:
        tts_episode.main()
        check("tts_episode: malformed tempo tag exits non-zero", False, "no exit")
    except SystemExit as e:
        check("tts_episode: malformed tempo tag exits non-zero", "unreadable tempo tag" in str(e.code), e.code)

    # 5b. legacy manifest (no text_hash) whose wav's .txt matches the current parsed text is
    #     ADOPTED, not re-synthesized — a fresh run over every already-shipped episode must
    #     not blow away every duration under already-timed graphics.
    ep_legacy = make_episode(tmp, SCRIPT_ONE_SEG, voice_ref, name="ep_legacy")
    (ep_legacy / "audio").mkdir()
    (ep_legacy / "audio" / "a1-s1.txt").write_text("Hello world this is a test line.",
                                                    encoding="utf-8")
    (ep_legacy / "audio" / "a1-s1.wav").write_bytes(b"OLD-RAW-WAV")
    (ep_legacy / "audio" / "a1-s1.words.json").write_text(
        json.dumps([{"text": "old", "start": 0.0, "end": 1.0}]), encoding="utf-8")
    (ep_legacy / "audio" / "manifest.json").write_text(json.dumps(
        {"a1-s1": {"wav": "audio/a1-s1.wav", "duration": 5.0, "words": 7}}), encoding="utf-8")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_legacy)]
    tts_episode.main()
    check("tts_episode: legacy manifest with matching .txt is adopted, not re-synthesized",
          calls["synth"] == [] and calls["transcribe"] == [])
    legacy_manifest = json.loads((ep_legacy / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: adopted entry is honestly marked tempo='legacy' (tempo is UNKNOWN, "
          "never claim it matches the current config tempo)",
          legacy_manifest["a1-s1"]["tempo"] == "legacy", legacy_manifest["a1-s1"])
    check("tts_episode: adopted entry's text_hash is over the TEXT ONLY (sha1 of the parsed "
          "text), not text+tempo+voice — tempo isn't known, so it can't be in the hash",
          legacy_manifest["a1-s1"]["text_hash"] ==
          hashlib.sha1("Hello world this is a test line.".encode("utf-8")).hexdigest())
    check("tts_episode: adopted entry keeps the OLD wav bytes (never touched)",
          (ep_legacy / "audio" / "a1-s1.wav").read_bytes() == b"OLD-RAW-WAV")

    # 5c. re-running over an ALREADY-adopted legacy entry (tempo="legacy", a stored text-only
    #     hash) with unchanged text stays adopted — the text-only hash path, not just the
    #     one-time old-.txt-comparison path, must also recognize "nothing changed".
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_legacy)]
    tts_episode.main()
    check("tts_episode: re-running an already-adopted legacy entry stays adopted (no synth)",
          calls["synth"] == [])
    legacy_manifest2 = json.loads((ep_legacy / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: still marked tempo='legacy' after a second unchanged run",
          legacy_manifest2["a1-s1"]["tempo"] == "legacy")

    # 5d. legacy manifest whose .txt DIFFERS from the current parsed text is NOT adopted — the
    #     text really changed since the last hash-less run, so it re-synthesizes AT THE LANE
    #     TEMPO, and the manifest entry stops being "legacy" (a real, known tempo now applies).
    ep_legacy_diff = make_episode(tmp, SCRIPT_ONE_SEG, voice_ref, name="ep_legacy_diff")
    (ep_legacy_diff / "audio").mkdir()
    (ep_legacy_diff / "audio" / "a1-s1.txt").write_text("An old, since-edited sentence.",
                                                         encoding="utf-8")
    (ep_legacy_diff / "audio" / "a1-s1.wav").write_bytes(b"OLD-RAW-WAV")
    (ep_legacy_diff / "audio" / "a1-s1.words.json").write_text(
        json.dumps([{"text": "old", "start": 0.0, "end": 1.0}]), encoding="utf-8")
    (ep_legacy_diff / "audio" / "manifest.json").write_text(json.dumps(
        {"a1-s1": {"wav": "audio/a1-s1.wav", "duration": 5.0, "words": 7}}), encoding="utf-8")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_legacy_diff)]
    tts_episode.main()
    check("tts_episode: legacy manifest with a DIFFERING .txt re-synthesizes",
          calls["synth"] == ["a1-s1"])
    legacy_diff_manifest = json.loads(
        (ep_legacy_diff / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: re-synthesized entry gets a real numeric tempo, not 'legacy'",
          legacy_diff_manifest["a1-s1"]["tempo"] == 1.10, legacy_diff_manifest["a1-s1"])

    # 5e. a crash DURING synthesis (tts_clone/ffmpeg/ffprobe failure, Ctrl-C) for a legacy
    #     manifest entry (no text_hash) must not corrupt the next run's adoption check. The
    #     bug: writing the new text to <id>.txt BEFORE synth used to make a post-crash rerun
    #     see old_txt == new text, adopt the entry, and silently keep the OLD wav for the NEW
    #     line. Fixed: <id>.txt is only replaced after synth + tempo succeed.
    ep_crash = make_episode(tmp, SCRIPT_ONE_SEG.replace(
        "Hello world this is a test line.", "A totally new line for the crash test."),
        voice_ref, name="ep_crash")
    (ep_crash / "audio").mkdir()
    (ep_crash / "audio" / "a1-s1.txt").write_text("Hello world this is a test line.",
                                                    encoding="utf-8")
    (ep_crash / "audio" / "a1-s1.wav").write_bytes(b"OLD-RAW-WAV")
    (ep_crash / "audio" / "a1-s1.words.json").write_text(
        json.dumps([{"text": "old", "start": 0.0, "end": 1.0}]), encoding="utf-8")
    (ep_crash / "audio" / "manifest.json").write_text(json.dumps(
        {"a1-s1": {"wav": "audio/a1-s1.wav", "duration": 5.0, "words": 7}}), encoding="utf-8")

    def mock_synth_native_crash(txt_path, wav_path, ext):
        # simulates tts_clone dying mid-segment, same as the real synth_native's sys.exit
        sys.exit("[test_audio] simulated tts_clone crash")

    install_mocks()
    tts_episode.synth_native = mock_synth_native_crash
    sys.argv = ["tts_episode.py", str(ep_crash)]
    try:
        tts_episode.main()
        check("tts_episode: crash mid-synthesis exits non-zero", False, "main() returned")
    except SystemExit:
        check("tts_episode: crash mid-synthesis exits non-zero", True)
    check("tts_episode: crash leaves <id>.txt holding the OLD text (not the new, unsynthesized one)",
          (ep_crash / "audio" / "a1-s1.txt").read_text(encoding="utf-8") ==
          "Hello world this is a test line.")
    check("tts_episode: crash leaves the OLD wav untouched",
          (ep_crash / "audio" / "a1-s1.wav").read_bytes() == b"OLD-RAW-WAV")

    # Rerun with a working synth: the entry must now be recognized as changed and re-synthesized.
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_crash)]
    tts_episode.main()
    check("tts_episode: rerun after a synth crash DOES re-synthesize (root bug: would silently "
          "adopt the old wav instead)", calls["synth"] == ["a1-s1"])
    check("tts_episode: rerun after a synth crash produces new wav bytes, not the old wav",
          (ep_crash / "audio" / "a1-s1.wav").read_bytes() != b"OLD-RAW-WAV")
    crash_manifest = json.loads((ep_crash / "audio" / "manifest.json").read_text(encoding="utf-8"))
    check("tts_episode: re-synthesized crash entry gets a real numeric tempo, not 'legacy'",
          crash_manifest["a1-s1"]["tempo"] == 1.10, crash_manifest["a1-s1"])

    # 6. 0 parsed segments exits non-zero and leaves manifest.json untouched.
    before = (ep / "audio" / "manifest.json").read_text(encoding="utf-8")
    ep_empty = make_episode(tmp, "## SCRIPT\n**A1-S1 (10 w)** inline prose, no blockquotes.\n",
                            voice_ref, name="ep_empty")
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

    # 7b. a section can't reach TTS with an open [verify] marker still on it (the mechanical
    #     backstop for script-scaling.md's "a section locks, then goes to TTS" rule): whether
    #     the whole script or an --only slice is selected, any segment whose text still has
    #     "[verify" is a hard fail, and nothing gets synthesized.
    ep_verify = make_episode(tmp, SCRIPT_ONE_SEG.replace(
        "Hello world this is a test line.",
        "The tornado killed [verify: exact toll] people that night."),
        voice_ref, name="ep_verify")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_verify)]
    try:
        tts_episode.main()
        check("tts_episode: open [verify] marker exits non-zero", False, "main() returned")
    except SystemExit as e:
        check("tts_episode: open [verify] marker exits non-zero", e.code not in (0, None), e.code)
    check("tts_episode: open [verify] marker never reaches synth",
          calls["synth"] == [], calls["synth"])

    # 7c. a CLEAN segment with no open marker still passes (sanity check the guard isn't
    #     flagging every segment).
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep)]
    tts_episode.main()
    check("tts_episode: a clean segment (no [verify]) is not blocked by the guard",
          calls["synth"] == [])  # unchanged text from run #2 above, so no re-synth either way

    # 7d. section lock, the actual point of the guard: a LOCKED section (--only, clean) still
    #     reaches TTS while a LATER, unselected section still carries an open [verify] marker
    #     — the whole script never waits on the slowest act's fan-out.
    SCRIPT_TWO_SEG_ONE_OPEN = """# edit_script.md

### H1-S1 -- narration
> The tornado hit at eleven PM sharp.

### A3-S5 -- narration
> The death toll reached [verify: exact count] by morning.
"""
    ep_section = make_episode(tmp, SCRIPT_TWO_SEG_ONE_OPEN, voice_ref, name="ep_section")
    install_mocks()
    sys.argv = ["tts_episode.py", str(ep_section), "--only", "h1-s1"]
    tts_episode.main()
    check("tts_episode: a locked section reaches TTS while a later act's [verify] is still open",
          calls["synth"] == ["h1-s1"], calls["synth"])

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

# 9b. a leading 'insert' (script has a word before whisper's first token, e.g. whisper missed
# it) spans 0.0 -> the first whisper word's start, not a single point AT that start (which
# collapsed the inserted word to zero duration).
whisper_words_lead = [{"text": "Ibu", "start": 0.5, "end": 0.8}]
aligned_lead = build_srt.align_captions(whisper_words_lead, "Well Ibu")
well = next(w for w in aligned_lead if w["text"] == "Well")
check("build_srt: a leading insert spans 0.0 to the first whisper word's start",
      well["start"] == 0.0 and well["end"] == 0.5, well)
check("build_srt: a leading insert is not zero-duration",
      well["end"] - well["start"] > 0, well)

# ---------------------------------------------------------------------------
# 10. word_budget: BOTH real script formats present on main, counted correctly, read-only
#     (no writes under episodes/). ep3-tristate is the blockquote format (real probe wavs
#     already on disk); ep-1974-super-outbreak is the inline-bold '## SCRIPT' format (no
#     blockquotes, no real probe wavs on disk here — a synthetic probe wav/txt pair, built
#     in a temp dir from the REAL probe text, stands in just for the pace measurement; the
#     narration COUNT itself still comes from the real, unmodified edit_script.md on disk).
import subprocess
MAIN = Path(r"C:\Users\Sidhartha\Automation Projects\storm-market\episodes")

r = subprocess.run([sys.executable, str(S / "word_budget.py"), str(MAIN / "ep3-tristate"),
                    "--target", "26", "--probe", "audio/probe1.wav", "audio/probe2.wav"],
                   capture_output=True, text=True)
print("[test_audio] word_budget on real ep3-tristate (blockquote format):")
print(r.stdout)
check("word_budget: ep3-tristate (blockquote format) uses the parse_segments path",
      "counted via blockquote parser" in r.stdout, r.stdout)

ep1974 = MAIN / "ep-1974-super-outbreak"
real_probe_txt = (ep1974 / "audio" / "probe" / "hook_plain.txt").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory() as d:
    tmp = Path(d)
    probe_wav = tmp / "hook_plain.wav"
    probe_wav.write_bytes(b"synthetic-probe-standin")
    (tmp / "hook_plain.txt").write_text(real_probe_txt, encoding="utf-8")
    import wave as _wave
    with _wave.open(str(probe_wav), "wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(24000)
        wf.writeframes(b"\x00\x00" * (24000 * 10))  # 10 s of silence, real word count above
    r = subprocess.run([sys.executable, str(S / "word_budget.py"), str(ep1974),
                        "--target", "20", "--probe", str(probe_wav)],
                       capture_output=True, text=True)
    print("[test_audio] word_budget on real ep-1974-super-outbreak ('## SCRIPT' format):")
    print(r.stdout)
    check("word_budget: ep-1974 (inline-bold format) falls back to the '## SCRIPT' counter",
          "counted via '## SCRIPT' fallback" in r.stdout, r.stdout)

# ---------------------------------------------------------------------------
if fails:
    print(f"[test_audio] {len(fails)} FAILED: {fails}")
    sys.exit(1)
print("[test_audio] all PASS")
