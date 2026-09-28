#!/usr/bin/env python3
"""Report every homograph in an episode's narration so the builder probes it before TTS/render.

Single source of truth is `references/homographs.md` — this script never hardcodes the word
list, only the parser for that table (Word(s) | Sense A | Sense B | Hint), mirroring
`scripts/flag_words.py`'s table-driven design (no separate framework).

pocket-TTS picks a pronunciation from spelling alone; a heteronym like "lives" (noun vs. verb)
can render wrong even when the script's wording is exactly right. This gate does not guess
which sense is meant — it reports every occurrence with its sentence and both possible sounds,
and the builder decides by probing the TTS (listen, or measure F1 onset / vowel length), never
by guessing a respelling (references/homographs.md, LEARNINGS.md 2026-09-28).

Severity: every hit is a WARN, never a FAIL — matching how flag_words.py treats a "soft" hit.
Whether a reported occurrence actually needs a respell depends on the sense used in that
sentence, which this script cannot judge; hard-failing every occurrence would block a render on
lines that are already correct and make the gate impossible to keep green. A malformed
wordlist (0 usable terms) IS a hard failure (exit 2) — a broken table must never read as
"nothing to flag".

Scans narration only (edit_script.md, via the same tts_episode.parse_segments used by
word_budget.py and flag_words.py), not on-screen text or metadata — a homograph is a spoken-
word defect, on-screen text is always read visually, never voiced.

Usage: python3 scripts/homograph_scan.py episodes/<slug> [--wordlist PATH]
Exit 0 = ran cleanly (0 or more WARN occurrences printed). Exit 2 = the wordlist itself is
broken, or the narration doesn't parse.
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
    """Parse the markdown table into [(pattern, sense_a, sense_b, hint, display_form), ...]."""
    text = wordlist_path.read_text(encoding="utf-8")
    terms = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0] in ("Word(s)",):
            continue
        word_cell, sense_a, sense_b, hint = cells[0], cells[1], cells[2], cells[3]
        for form in [f.strip() for f in word_cell.split("/") if f.strip()]:
            pattern = re.compile(r"\b" + re.escape(form) + r"\b", re.IGNORECASE)
            terms.append((pattern, sense_a, sense_b, hint, form))
    if not terms:
        raise WordlistError(f"0 usable terms parsed from {wordlist_path} — refusing a no-op gate")
    return terms


def sentences(text):
    return [s.strip() for s in SENTENCE_RE.findall(text.replace("\n", " ")) if s.strip()]


def scan_text(loc_label, text, terms, hits):
    for sent in sentences(text):
        for pattern, sense_a, sense_b, hint, form in terms:
            if pattern.search(sent):
                hits.append((loc_label, form, sent, sense_a, sense_b, hint))


def scan_narration(script_md, terms, hits):
    """SegmentParseError propagates to the caller — an ambiguous script block is a loud, hard
    failure, never a silent skip (same contract as flag_words.py)."""
    text = script_md.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return
    segs = parse_segments(text)
    if segs:
        for sid, seg_text in segs:
            scan_text(f"{script_md}:{sid}", seg_text, terms, hits)
        return
    print(f"[FALLBACK] 0 narration segments parsed from {script_md} (non-blockquote script "
          f"format) — scanning the whole file text instead of per-segment.")
    scan_text(str(script_md), text, terms, hits)


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
        terms = load_terms(wordlist_path)
    except WordlistError as e:
        print(f"HOMOGRAPH_SCAN FAIL - bad wordlist {wordlist_path}: {e}")
        sys.exit(2)

    hits = []
    script_md = ep / "edit_script.md"
    if script_md.is_file():
        try:
            scan_narration(script_md, terms, hits)
        except SegmentParseError as e:
            print(f"HOMOGRAPH_SCAN FAIL - could not parse narration in {script_md}: {e}")
            sys.exit(2)

    for loc, form, sent, sense_a, sense_b, hint in hits:
        print(f'{loc}: "{form}" in: {sent}')
        print(f"    sense A: {sense_a}")
        print(f"    sense B: {sense_b}")
        print(f"    {hint}")

    print()
    if hits:
        print(f"HOMOGRAPH_SCAN WARN - {len(hits)} homograph occurrence(s). Probe each with the "
              f"TTS (listen, or measure F1 onset / vowel length) and pick the respelling by "
              f"measurement, never by guess, before this episode renders.")
    else:
        print("HOMOGRAPH_SCAN PASS - 0 homograph occurrences.")
    sys.exit(0)


if __name__ == "__main__":
    main()
