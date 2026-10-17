#!/usr/bin/env python3
"""TTS driver: extract narration segments from an episode's edit_script.md, then for each
segment run pocket-TTS (native pace) -> ffmpeg atempo (config.yaml channel.tempo, per-lane
override in channel.tempo_by_prefix matched against the episode slug, e.g. shorts 'sh-';
CLAUDE.md Voice + references/shorts/PLAN.md; tempo BEFORE timing)
-> faster-whisper word timestamps on the SPED wav. One driver, one pass per segment.

Segment = a heading ('### <ID> — narration', any '#' depth) followed by exactly one
blockquote paragraph. ID like 'A3-S5'. Splitting on EVERY heading (not just '### ') means a
later '## SECTION' and anything under it — including a stray production note — can never glue
onto an earlier segment's blockquote (the ms-elnino-texas h1-s1/TTS-note bug).

Outputs per segment: audio/<id>.txt (voiced text), audio/_raw/<id>.wav (native pace),
audio/<id>.wav (post-atempo, what ships), audio/<id>.words.json (timestamps on the sped wav),
audio/manifest.json (duration/words/text_hash/tempo per id, merged — a run never shrinks it).

Re-synthesis: a segment is only re-run (new _raw + sped wav, words.json deleted and
retranscribed) when sha1(text + tempo + voice md5) changes from the manifest's stored hash for
that id. Editing one script line invalidates only that line's stale audio, nothing else.

Per-segment tempo: '(tempo X)' on a segment heading overrides the lane tempo for that segment
only (rule: CLAUDE.md "Voice").

Usage: python3 scripts/tts_episode.py episodes/<slug> [--only A3-S5,...]
Exits non-zero, and leaves manifest.json untouched, when the script parses to 0 segments (an
unsupported format — see parse_segments docstring) or an --only id isn't in the script.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import tts_clone
import voice_tool

REPO = Path(__file__).resolve().parent.parent
SEG_ID = r"([A-Z]\d+-S\d+[a-z]?)\b"  # segment id at the start of a heading, e.g. 'A3-S5'


def segment_blocks(md: str):
    """(segment id, heading line, body) for every heading whose text starts with a segment id. Splits on ANY
    markdown heading, so a '## SECTION' boundary (and any note under it) never leaks into the previous segment."""
    for b in re.split(r"\n#{1,6} ", "\n" + md.replace("\r\n", "\n"))[1:]:
        header, _, rest = b.partition("\n")
        m = re.match(SEG_ID, header)
        if m:
            yield m.group(1).lower(), header, rest


def open_verify_ids(md: str):
    """Segment ids whose heading block (narration, Picture, Rows, notes) still carries an open [verify] marker.
    script-scaling.md "Section lock" counts every marker on the section, not only those in the spoken line."""
    return {sid for sid, header, rest in segment_blocks(md) if "[verify" in header + rest}


class SegmentParseError(Exception):
    """A segment's markdown doesn't parse unambiguously into narration text."""


def load_cfg():
    import yaml  # storm venv-less: pyyaml via python312 site or fallback parse
    return yaml.safe_load(open(REPO / "config.yaml", encoding="utf-8"))


def parse_segments(md: str):
    """Split on ANY markdown heading, not just '### ' — a '## SECTION' boundary (and any note
    under it) can never leak into the previous segment. Only headings whose text starts with an
    ID like 'A3-S5' are segments; everything else (act headings, notes sections) is skipped.
    A segment keeps its own blockquote paragraph, wherever it sits relative to a 'Visual:'
    note (before the quote in ep3-tristate/ep1-joplin, after it in ms-*/br-*). A SECOND
    blockquote paragraph under the same heading, or a paragraph that reads like a production
    note, is a hard error — never silently voiced.

    Only understands the '### <ID> — narration' + '> quote' layout used across
    ep1/ep2/.../ep6/ep8 and ms-*/br-*/sh-*, where <ID> is a letter+number pair like 'A3-S5'.
    NOT supported: ep-1974-super-outbreak's '## SCRIPT' inline-bold-marker prose layout
    ('**A1-S1 (100 w)** text [VE ...] ...'), which has no blockquotes at all; and
    demo-joplin-90, whose bare 'S2 — narration' headings (no letter prefix) don't match the ID
    regex either — same 0-segment result under the OLD parser too, so this is a pre-existing
    gap, not a regression. Both correctly return 0 segments rather than guessing — callers
    must hard-fail on 0, not skip loud.
    """
    segs = []
    for sid, _, rest in segment_blocks(md):
        # Scan the WHOLE block (already heading-delimited, so this can never cross into a
        # later segment or section) for blockquote paragraphs — 'Visual:' notes sit BEFORE
        # the quote in some episodes (ep3-tristate, ep1-joplin) and AFTER it in others
        # (ms-*/br-*), so position relative to other prose can't be the paragraph boundary;
        # only a non-quote line breaks one paragraph from the next.
        paragraphs, cur = [], []
        for line in rest.splitlines():
            if line.startswith(">"):
                cur.append(line[2:] if line.startswith("> ") else line[1:])
            elif cur:
                paragraphs.append(cur)
                cur = []
        if cur:
            paragraphs.append(cur)
        if not paragraphs:
            continue
        if len(paragraphs) > 1:
            raise SegmentParseError(
                f"{sid}: {len(paragraphs)} blockquote paragraphs under one heading — "
                f"ambiguous which is narration")
        text = re.sub(r"\s+", " ", " ".join(paragraphs[0])).strip()
        if re.match(r"(?i)^(TTS note|NOTE)\b", text):
            raise SegmentParseError(
                f"{sid}: blockquote reads like a production note, not narration: {text[:80]!r}")
        if text:
            segs.append((sid, text))
    return segs


def segment_tempos(md: str):
    """{segment id: tempo} for headings carrying '(tempo X)', e.g. '### A2-S4 — narration (tempo 0.85)'.
    A segment heading that mentions tempo in any other form is a hard error, never silently ignored."""
    tempos = {}
    for m in re.finditer(r"^#{1,6} " + SEG_ID + r"(.*)$", md, re.M):
        if "tempo" not in m.group(2).lower():
            continue
        t = re.search(r"\(tempo (\d+(?:\.\d+)?)\)", m.group(2))
        if not t:
            raise SegmentParseError(f"{m.group(1)}: unreadable tempo tag in heading {m.group(0)!r} "
                                    f"(write it as '(tempo 0.85)', the number from CLAUDE.md Voice)")
        tempos[m.group(1).lower()] = float(t.group(1))
    return tempos


def resolve_tempo(cfg, slug):
    """Per-lane tempo, matched against the episode slug's prefix. config.yaml
    channel.tempo_by_prefix (e.g. 'sh-' for shorts, references/shorts/PLAN.md "Pace") overrides
    channel.tempo (docs + minis, CLAUDE.md Voice) for any slug starting with that prefix."""
    channel = cfg.get("channel", {})
    for prefix, t in (channel.get("tempo_by_prefix") or {}).items():
        if slug.startswith(prefix):
            return t
    return channel.get("tempo")


def sha1_text(text, tempo, voice_md5):
    # tts_clone.PAUSES: a pause-policy change re-joins every segment (cached sentences are reused)
    return hashlib.sha1(f"{text}\x1f{tempo}\x1f{voice_md5}\x1f{tts_clone.PAUSES}".encode("utf-8")).hexdigest()


def ffprobe_duration(path, attempts=4, sleep_s=3):
    # ffprobe immediately after write can return empty on this box (Defender scan lock);
    # retry briefly before failing loud.
    d = None
    for _ in range(attempts):
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "default=nw=1:nk=1", str(path)],
                             capture_output=True, text=True).stdout.strip()
        if out:
            d = float(out)
            break
        time.sleep(sleep_s)
    return d


def synth_native(pairs, ext):
    # One tts_clone.py process for every stale segment (--batch): the model loads and the voice
    # clones once per run instead of once per segment. tts_clone.py intermittently dies at CUDA
    # init/clone with a native crash (no traceback, non-zero exit; ep6 measured ~1 in 8 calls,
    # same input passes on rerun). One loud retry; tts_clone caches finished sentences by text
    # and voice hash in <out dir>/_segments, so the retry only re-pays the load. A second consecutive
    # failure is real. Exit 2 is argparse (e.g. a tts_clone without --batch): deterministic, no retry.
    gaps = voice_tool.missing(ext, allow_download=True)
    if gaps:
        sys.exit("[tts_episode] FAIL voice tool incomplete:\n  " + "\n  ".join(gaps))
    batch_file = pairs[0][1].parent / "batch.tsv"
    batch_file.write_text("".join(f"{t}\t{w}\n" for t, w in pairs), encoding="utf-8")
    r = None
    for attempt in (1, 2):
        r = subprocess.run([ext["pocket_venv_python"], str(REPO / "scripts" / "tts_clone.py"),
                            "--batch", str(batch_file), "--voice", ext["voice_ref"]],
                           env={**os.environ, "PYTHONUTF8": "1", "PYTHONUNBUFFERED": "1"})
        if r.returncode == 0:
            batch_file.unlink()
            return
        if r.returncode == 2:
            break
        print(f"[tts_episode] [FALLBACK] batch of {len(pairs)} attempt {attempt} exited "
              f"{r.returncode} (0x{r.returncode & 0xFFFFFFFF:08X})", flush=True)
    sys.exit(f"[tts_episode] FAIL on the batch of {len(pairs)} (attempt {attempt}), exit {r.returncode} "
             f"(exit 2 is argparse: scripts/tts_clone.py rejected its arguments)")


def apply_tempo(raw_wav, sped_wav, tempo):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw_wav),
                        "-filter:a", f"atempo={tempo}", "-ar", "48000", str(sped_wav)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"[tts_episode] ffmpeg atempo failed on {sped_wav.stem}: {r.stderr[-300:]}")


def load_whisper_model():
    voice_tool.use_repo_models()  # the whisper model lives in the repo too
    from faster_whisper import WhisperModel
    return WhisperModel("small.en", device="cpu", compute_type="int8")


def transcribe_wav(model, wav_path):
    segments, _ = model.transcribe(str(wav_path), word_timestamps=True, language="en")
    return [{"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)}
            for s in segments for w in (s.words or [])]


def main():
    ep = Path(sys.argv[1])
    only = None
    if "--only" in sys.argv:
        only = set(s.strip().lower() for s in sys.argv[sys.argv.index("--only") + 1].split(","))
    cfg = load_cfg()
    ext = cfg["external"]
    tempo = resolve_tempo(cfg, ep.name)
    if not tempo:
        sys.exit("[tts_episode] config.yaml channel.tempo is not set "
                  "(CLAUDE.md Voice: documentaries and minis share one lane tempo)")
    voice_md5 = voice_tool.voice_md5(ext["voice_ref"])
    (ep / "audio").mkdir(exist_ok=True)
    (ep / "audio" / "_raw").mkdir(exist_ok=True)
    try:
        script_md = (ep / "edit_script.md").read_text(encoding="utf-8")
        segs = parse_segments(script_md)
        tempos = segment_tempos(script_md)
    except SegmentParseError as e:
        sys.exit(f"[tts_episode] FAIL parsing edit_script.md: {e}")
    if not segs:
        sys.exit(f"[tts_episode] FAIL — 0 narration segments parsed from {ep}/edit_script.md "
                 f"(unsupported script format — see parse_segments docstring); "
                 f"manifest.json left untouched")
    seg_ids = {sid for sid, _ in segs}
    if only:
        missing = only - seg_ids
        if missing:
            sys.exit(f"[tts_episode] FAIL — --only id(s) not in edit_script.md: {sorted(missing)}")
    # A section locks (script-scaling.md "Script fact-QC layer") only once every [verify]
    # marker on it is resolved. TTS is the mechanical backstop for that rule: never voice a
    # segment that still carries one, whether it's in the --only set or the whole script.
    selected = [(sid, text) for sid, text in segs if not only or sid in only]
    unresolved = sorted(sid for sid, text in selected if "[verify" in text)
    if unresolved:
        sys.exit(f"[tts_episode] FAIL — {len(unresolved)} segment(s) still carry an open "
                 f"[verify] marker, not TTS-safe: {unresolved} (script-scaling.md 'Script "
                 f"fact-QC layer' — resolve or cut the claim before this section locks)")
    print(f"[tts_episode] {len(segs)} narration segments found")

    mpath = ep / "audio" / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    model = None
    todo, stale_pairs = [], []
    for sid, text in segs:
        if only and sid not in only:
            continue
        txt = ep / "audio" / f"{sid}.txt"
        txt_tmp = ep / "audio" / f"{sid}.tmp"
        raw_wav = ep / "audio" / "_raw" / f"{sid}.wav"
        wav = ep / "audio" / f"{sid}.wav"
        words_json = ep / "audio" / f"{sid}.words.json"
        # old_txt must be read BEFORE any write below, and <id>.txt itself must not be
        # touched until synthesis succeeds (see the "stale" branch). A legacy manifest
        # entry (no text_hash) is adopted by comparing old_txt to the new text; writing the
        # new text here early would make that comparison lie after a crash mid-segment (tts
        # clone failure, ffmpeg/ffprobe failure, Ctrl-C): the rerun would see old_txt == new
        # text, adopt the entry, and silently keep the OLD wav for the NEW line.
        old_txt = txt.read_text(encoding="utf-8") if txt.exists() else None
        seg_tempo = tempos.get(sid, tempo)

        h = sha1_text(text, seg_tempo, voice_md5)
        h_text = hashlib.sha1(text.encode("utf-8")).hexdigest()
        prior = manifest.get(sid, {})
        prior_tempo = prior.get("tempo")
        # A legacy manifest entry (tempo missing, or already marked "legacy" by an earlier
        # adoption) was made by SOME wav we can't identify the tempo of: the old native-pace
        # driver, a hand-sped wav (ms-indonesia), or ep-1974's separate tts_run.py. Its tempo
        # is UNKNOWN — never claim it matches the current config tempo by stamping a numeric
        # tempo + a tempo-dependent hash; that would freeze a possibly-wrong pace forever.
        # Adopt it honestly instead: keep the wav/words.json untouched, hash the TEXT only,
        # and only invalidate it when the text itself changes (then re-synth at the current
        # lane tempo, which replaces the "legacy" marker with a real one). Without adoption at
        # all, the first full run after this fix would re-synthesize every existing episode's
        # segments and shift every duration under already-timed graphics.
        # An explicit '(tempo X)' tag is a known tempo, so it is never adopted as legacy: the
        # tagged segment re-synthesizes at that tempo (else the tag is silently ignored).
        is_legacy = sid not in tempos and prior_tempo in (None, "legacy") and wav.exists()
        if is_legacy:
            prior_text_hash = prior.get("text_hash")
            text_changed = (prior_text_hash != h_text) if prior_text_hash is not None \
                else (old_txt != text)
            adopted = not text_changed
            stale = text_changed
        else:
            adopted = False
            stale = prior.get("text_hash") != h or not wav.exists()
        todo.append((sid, text, txt, txt_tmp, raw_wav, wav, words_json, h, h_text,
                     is_legacy, adopted, stale, seg_tempo))
        if stale:
            # tts_clone reads from a TEMP text file. <id>.txt (the file old_txt/adoption
            # compares against) is only replaced with the new text after synth + tempo both
            # succeed, so a crash anywhere in between leaves it holding the text of the wav
            # that's actually on disk.
            txt_tmp.write_text(text, encoding="utf-8")
            stale_pairs.append((txt_tmp, raw_wav))

    if stale_pairs:
        synth_native(stale_pairs, ext)

    for (sid, text, txt, txt_tmp, raw_wav, wav, words_json, h, h_text, is_legacy, adopted, stale,
         seg_tempo) in todo:
        if stale:
            apply_tempo(raw_wav, wav, seg_tempo)
            txt_tmp.replace(txt)
            if words_json.exists():
                words_json.unlink()

        d = ffprobe_duration(wav)
        if d is None:
            sys.exit(f"[tts_episode] ffprobe returned empty for {wav} after 4 attempts")

        if stale or not words_json.exists():
            if model is None:
                model = load_whisper_model()
            words = transcribe_wav(model, wav)
            words_json.write_text(json.dumps(words), encoding="utf-8")
            print(f"[tts_episode] {sid}: transcribed, {len(words)} words, last end "
                 f"{words[-1]['end'] if words else 0}s", flush=True)

        if is_legacy and adopted:
            manifest[sid] = {"wav": f"audio/{sid}.wav", "duration": round(d, 3),
                             "words": len(text.split()), "text_hash": h_text, "tempo": "legacy"}
            tag = " [adopted: legacy tempo unknown]"
        else:
            manifest[sid] = {"wav": f"audio/{sid}.wav", "duration": round(d, 3),
                             "words": len(text.split()), "text_hash": h, "tempo": seg_tempo}
            tag = " [re-synth]" if stale else ""
        print(f"[tts_episode] {sid}: {d:.1f}s ({len(text.split())} words){tag}", flush=True)

    mpath.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    total = sum(v["duration"] for v in manifest.values())
    print(f"[tts_episode] DONE — {len(manifest)} segments, {total/60:.1f} min narration")


if __name__ == "__main__":
    main()
