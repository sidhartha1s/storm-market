#!/usr/bin/env python3
"""Report every flagged homograph in an episode's narration so the builder probes it before TTS/render.

Single source of truth is `references/homographs.md` — this script never hardcodes the word
list, only the parser for that table (Word(s) | Scan | Sense A | Sense B | Hint), mirroring
`scripts/flag_words.py`'s table-driven design (no separate framework). Only `Scan: yes` rows
are gated; `Scan: no` rows are reference-only heteronyms kept for a human writing a script, not
worth a per-episode probe line (see the table's own "Scan column" note for why — an unscoped
scan of every listed word is noise, not a checklist).

pocket-TTS picks a pronunciation from spelling alone; a heteronym like "lives" (noun vs. verb)
can render wrong even when the script's wording is exactly right. This gate does not guess
which sense is meant — it reports each flagged word with an occurrence count and its first
sentence, and the builder decides by probing the TTS (listen, or measure F1 onset / vowel
length), never by guessing a respelling. Measured 2026-09-27 on ep-enderlin
(`learnings/audio-tts.md`): a blind respelling ("lyvz") caused the defect; the plain word
("lives") was already correct.

Severity: every hit is a WARN, never a FAIL — matching how flag_words.py treats a "soft" hit.
Whether a reported occurrence actually needs a respell depends on the sense used in that
sentence, which this script cannot judge; hard-failing every occurrence would block a render on
lines that are already correct and make the gate impossible to keep green. A malformed
wordlist (an unknown Scan value, or 0 usable Scan=yes terms) IS a hard failure (exit 2) — a
broken table must never read as "nothing to flag".

Scans narration only (edit_script.md, via the same tts_episode.parse_segments used by
word_budget.py and flag_words.py), not on-screen text or metadata — a homograph is a spoken-
word defect, on-screen text is always read visually, never voiced.

Output is one line per flagged word (occurrence count + its first sentence), not one line per
occurrence — the point is a short probe checklist, not a transcript dump.

Usage: python3 scripts/homograph_scan.py episodes/<slug> [--wordlist PATH]
Exit 0 = ran cleanly (0 or more WARN lines printed). Exit 2 = the wordlist itself is broken, or
the narration doesn't parse.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tts_episode import parse_segments, SegmentParseError  # noqa: E402

DEFAULT_WORDLIST = Path(__file__).resolve().parent.parent / "references" / "homographs.md"
SENTENCE_RE = re.compile(r"[^.!?]*[.!?]|[^.!?]+$")


class WordlistError(Exception):
    """references/homographs.md (or a --wordlist override) doesn't parse into usable terms."""


def load_terms(wordlist_path):
    """Parse the markdown table into a list of row dicts for the Scan=yes rows only:
    {"label": <first listed form>, "patterns": [compiled regex per literal form],
     "sense_a": ..., "sense_b": ..., "hint": ...}. Scan=no rows are reference-only, skipped."""
    text = wordlist_path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("Word(s)",):
            continue
        word_cell, scan, sense_a, sense_b, hint = cells[0], cells[1].lower(), cells[2], cells[3], cells[4]
        if scan not in ("yes", "no"):
            raise WordlistError(
                f"unknown Scan value {cells[1]!r} (want 'yes' or 'no') on row: {line}")
        if scan == "no":
            continue
        forms = [f.strip() for f in word_cell.split("/") if f.strip()]
        if not forms:
            continue
        patterns = [re.compile(r"\b" + re.escape(f) + r"\b", re.IGNORECASE) for f in forms]
        rows.append({"label": forms[0], "patterns": patterns,
                     "sense_a": sense_a, "sense_b": sense_b, "hint": hint})
    if not rows:
        raise WordlistError(
            f"0 usable Scan=yes terms parsed from {wordlist_path} — refusing a no-op gate")
    return rows


def sentences(text):
    return [s.strip() for s in SENTENCE_RE.findall(text.replace("\n", " ")) if s.strip()]


def scan_sentences(loc, text, rows):
    """Mutate each matched row in place: count += 1, first = (loc, sentence) on the first hit
    only, so document order (segments in parse order, sentences within a segment in order)
    decides which sentence a word's report line quotes."""
    for sent in sentences(text):
        for row in rows:
            if any(p.search(sent) for p in row["patterns"]):
                row["count"] = row.get("count", 0) + 1
                row.setdefault("first", (loc, sent))


def scan_narration(script_md, rows):
    """SegmentParseError propagates to the caller — an ambiguous script block is a loud, hard
    failure, never a silent skip (same contract as flag_words.py)."""
    text = script_md.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return
    segs = parse_segments(text)
    if segs:
        for sid, seg_text in segs:
            scan_sentences(f"{script_md}:{sid}", seg_text, rows)
        return
    print(f"[FALLBACK] 0 narration segments parsed from {script_md} (non-blockquote script "
          f"format) — scanning the whole file text instead of per-segment.")
    scan_sentences(str(script_md), text, rows)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 scripts/homograph_scan.py episodes/<slug> [--wordlist PATH]")
    ep = Path(sys.argv[1])
    if not ep.is_dir():
        sys.exit(f"not a directory: {ep}")
    wordlist_path = DEFAULT_WORDLIST
    if "--wordlist" in sys.argv:
        wordlist_path = Path(sys.argv[sys.argv.index("--wordlist") + 1])

    try:
        rows = load_terms(wordlist_path)
    except WordlistError as e:
        print(f"HOMOGRAPH_SCAN FAIL - bad wordlist {wordlist_path}: {e}")
        sys.exit(2)

    script_md = ep / "edit_script.md"
    if script_md.is_file():
        try:
            scan_narration(script_md, rows)
        except SegmentParseError as e:
            print(f"HOMOGRAPH_SCAN FAIL - could not parse narration in {script_md}: {e}")
            sys.exit(2)

    flagged = [r for r in rows if r.get("count")]
    for r in flagged:
        loc, sent = r["first"]
        print(f'"{r["label"]}" - {r["count"]} occurrence(s); first {loc}: {sent} '
              f'| sense A: {r["sense_a"]} | sense B: {r["sense_b"]} | {r["hint"]}')

    print()
    if flagged:
        total = sum(r["count"] for r in flagged)
        print(f"HOMOGRAPH_SCAN WARN - {len(flagged)} word(s) flagged, {total} occurrence(s) "
              f"total. Probe each with the TTS (listen, or measure F1 onset / vowel length) and "
              f"pick the respelling by measurement, never by guess, before this episode renders.")
    else:
        print("HOMOGRAPH_SCAN PASS - 0 homograph occurrences.")
    sys.exit(0)


if __name__ == "__main__":
    main()
