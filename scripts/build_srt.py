#!/usr/bin/env python3
"""Build an SRT from an episode's per-segment words.json files.

Reads episodes/<slug>/index.html for <audio id="nx-*" src="audio/X.wav" data-start="T">,
loads audio/X.words.json (faster-whisper word timestamps, segment-relative), offsets to
timeline time, groups words into caption cues (<=42 chars per line, break on punctuation
or 3.5s), writes renders/<out>.srt.

Caption TEXT comes from audio/X.txt (the script text that was actually voiced), aligned to
the whisper words via difflib on normalized tokens; only the TIMING comes from words.json.
This fixes captions built straight from whisper's guesses at proper nouns (measured on
ms-indonesia-four-volcanoes: 'Ibu and Samaru'/'Samiru' for Semeru, 'Luutobi Lakilaki'/'Eli
Luatolak' for Lewotobi/Lewotolok, 'Besarnas' for Basarnas). KNOWN GAP: audio/X.txt itself
sometimes holds a phonetic TTS respelling ('Bassarnass', 'Lewotobi Lakee Lakee') rather than
the proper display spelling — there is no separate display-text/respell-map source in this
repo today, so those specific words still ship imperfect. This still removes pure ASR
mis-hears, which are the majority of the mismatch.

Usage: python3 scripts/build_srt.py episodes/<slug> <out-basename>
"""
import difflib
import json
import re
import sys
from pathlib import Path

_PUNCT = re.compile(r"[^\w']+")


def _norm(tok):
    return _PUNCT.sub("", tok).lower()


def align_captions(whisper_words, script_text):
    """Re-spell whisper's per-word timings with the script text that was actually voiced.
    Keeps whisper's timing boundaries; swaps in the script's word forms via a difflib
    alignment on normalized (lowercased, punctuation-stripped) tokens. Words whisper heard
    that aren't in the script are dropped; script words whisper missed are time-interpolated
    across the whisper span they replace."""
    script_tokens = script_text.split()
    if not whisper_words or not script_tokens:
        return whisper_words
    w_norm = [_norm(w.get("word", w.get("text", ""))) for w in whisper_words]
    s_norm = [_norm(t) for t in script_tokens]
    sm = difflib.SequenceMatcher(a=w_norm, b=s_norm, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "delete":
            continue  # whisper heard extra words the script doesn't have — drop them
        w_block = whisper_words[i1:i2]
        s_block = script_tokens[j1:j2]
        if tag == "equal":
            for w, t in zip(w_block, s_block):
                out.append({"text": t, "start": w["start"], "end": w["end"]})
            continue
        # 'replace' or 'insert': re-spell s_block, timed across the whisper span it replaces
        if w_block:
            start, end = w_block[0]["start"], w_block[-1]["end"]
        elif out:
            start = end = out[-1]["end"]
        else:
            # a leading insert (script has words before whisper's first word) spans the
            # segment's own lead-in, 0.0 to the first whisper word — not a single point AT
            # that word's start, which collapsed every such word to zero duration.
            start = 0.0
            end = whisper_words[0]["start"] if whisper_words else 0.0
        step = max(end - start, 0.01) / len(s_block)
        for k, t in enumerate(s_block):
            out.append({"text": t, "start": round(start + k * step, 3),
                       "end": round(start + (k + 1) * step, 3)})
    return out


def ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"


def main():
    ep = Path(sys.argv[1])
    out_base = sys.argv[2]
    html = (ep / "index.html").read_text(encoding="utf-8")

    cues = []
    # inserts (archival audio, no transcript): label each from its data-srt-label attribute.
    # An insert WITHOUT a label is a hard error — a silent skip shipped ep5's SRT with no
    # 911 caption (the old code hardcoded another episode's nx-ins1/Jasper County values).
    # <video id="ins…" data-volume="1"> inserts (ep6 WWL/C-SPAN cuts, the CTA) carry their own
    # audio on the picture track — they get a cue too (2026-08-30; muted videos are skipped).
    for ins in re.finditer(r'<(?:audio|video) [^>]*?id="(?:nx-)?ins[^"]*"[^>]*>', html):
        if ins.group(0).startswith("<video") and not re.search(r'data-volume="1(?:\.0+)?"', ins.group(0)):
            continue
        st = re.search(r'data-start="([\d.]+)"', ins.group(0))
        du = re.search(r'data-duration="([\d.]+)"', ins.group(0))
        lab = re.search(r'data-srt-label="([^"]+)"', ins.group(0))
        if not (st and du):
            continue
        if not lab:
            sys.exit(f"insert audio has no data-srt-label (SRT caption text): {ins.group(0)[:120]}")
        s = float(st.group(1))
        cues.append((s + 0.4, s + float(du.group(1)) - 0.2, lab.group(1)))

    for m in re.finditer(r'<audio [^>]*?id="nx-(?!ins)[^"]*" src="(audio/[^"]+)\.wav" data-start="([\d.]+)"', html):
        wj = ep / f"{m.group(1)}.words.json"
        if not wj.exists():
            sys.exit(f"missing words.json: {wj}")
        txt_path = ep / f"{m.group(1)}.txt"
        if not txt_path.exists():
            sys.exit(f"missing script text for caption alignment: {txt_path}")
        off = float(m.group(2))
        words = json.loads(wj.read_text(encoding="utf-8"))
        if isinstance(words, dict):
            words = words.get("words", [])
        words = align_captions(words, txt_path.read_text(encoding="utf-8"))
        line, start = [], None
        for w in words:
            txt = w["word" if "word" in w else "text"].strip()
            if start is None:
                start = w["start"] + off
            line.append(txt)
            end = w["end"] + off
            joined = " ".join(line)
            if (len(joined) >= 42 or txt.endswith((".", "?", "!", ","))
                    and len(joined) >= 24) or end - start > 3.5:
                cues.append((start, end, joined))
                line, start = [], None
        if line:
            cues.append((start, end, " ".join(line)))

    if not cues:
        sys.exit(f"no narration <audio id=\"nx-*\"> tags found in {ep}/index.html — "
                 "episode doesn't follow the nx-* audio naming convention (see DESIGN.md)")
    cues.sort()
    out = ep / "renders" / f"{out_base}.srt"
    with out.open("w", encoding="utf-8") as f:
        for i, (s, e, txt) in enumerate(cues, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(max(e, s + 0.8))}\n{txt}\n\n")
    print(f"{out} — {len(cues)} cues, last ends {ts(cues[-1][1])}")


if __name__ == "__main__":
    main()
