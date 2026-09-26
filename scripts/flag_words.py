"""Fail the build on violence/death vocabulary that trips YouTube's transcript scan.

Single source of truth is `references/flag-words.md` — this script never hardcodes the word
list, only the parser for that table (Term(s) | Severity | Alternatives | Reason) and a generic
English suffix group (s/es/d/ed/ing) appended to every term so "kill" also catches "kills" and
"killing" without a duplicate row. Irregular inflections that suffix concatenation gets wrong
(bloody -> bloodied, terror[ize] -> terrorized) are listed as their own literal form in the
table instead — a suffix rule can't fix English spelling, a row can.

Scans:
  - narration: episodes/<slug>/edit_script.md, via tts_episode.parse_segments (the same parser
    tts_episode.py and word_budget.py use) so a term is reported by segment id, the way the
    voice track is keyed. A script that parses to 0 segments (the inline-bold '## SCRIPT' prose
    layout, ep-1974-super-outbreak) is a genuine unsupported-but-real format, not an error: this
    gate falls back to scanning the whole file text and says so with a `[FALLBACK]` line, every
    time it engages. A script that parses to segments but hits an ambiguous block
    (SegmentParseError) is a hard, loud failure (exit 2) — never silently skipped.
  - metadata.md (title/description) whole text, when the file exists.
  - on-screen text: visible text in index.html and compositions/*.html, scripts/styles stripped.

Word-boundary, case-insensitive. Hard hits print with their alternatives and fail the gate
(exit 1). Soft hits print as warnings and do not fail it. A malformed wordlist (a row with a
severity that isn't hard/soft, or a wordlist that yields 0 usable terms) is exit 2, not a
silent pass — a broken table must never read as "nothing to flag".

Usage: python3 scripts/flag_words.py episodes/<slug> [--wordlist PATH]
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tts_episode import parse_segments, SegmentParseError  # noqa: E402

DEFAULT_WORDLIST = Path(__file__).resolve().parent.parent / "references" / "flag-words.md"
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
# English inflections that are plain concatenation (kill+s, murder+ed, bomb+ing). Irregular
# forms (y -> ied, -ize infixes) are NOT covered here on purpose — see module docstring; they
# get their own literal row in flag-words.md instead of a smarter, harder-to-audit regex.
SUFFIX = r"(?:s|es|d|ed|ing)?"


class WordlistError(Exception):
    """references/flag-words.md (or a --wordlist override) doesn't parse into usable terms."""


def load_terms(wordlist_path):
    """Parse the markdown table into [(pattern, severity, alternatives, display_term), ...]."""
    text = wordlist_path.read_text(encoding="utf-8")
    terms = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("Term(s)",):
            continue
        term_cell, severity, alternatives = cells[0], cells[1].lower(), cells[2]
        if severity not in ("hard", "soft"):
            raise WordlistError(
                f"unknown severity {cells[1]!r} (want 'hard' or 'soft') on row: {line}")
        for form in [f.strip() for f in term_cell.split("/") if f.strip()]:
            body = re.sub(r"\s+", r"\\s+", re.escape(form))
            pattern = re.compile(r"\b" + body + SUFFIX + r"\b", re.IGNORECASE)
            terms.append((pattern, severity, alternatives, form))
    if not terms:
        raise WordlistError(f"0 usable terms parsed from {wordlist_path} — refusing a no-op gate")
    return terms


def strip_html(html_text):
    """Return visible text per source line; a <script>/<style> block collapses to blank lines
    (same newline count, so line numbers of everything after it stay correct)."""
    no_script = SCRIPT_STYLE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), html_text)
    lines = []
    for raw in no_script.split("\n"):
        visible = TAG_RE.sub(" ", raw)
        lines.append(html.unescape(visible))
    return lines


def scan_text_lines(path, lines, terms, hits):
    for lineno, line in enumerate(lines, start=1):
        for pattern, severity, alternatives, form in terms:
            m = pattern.search(line)
            if m:
                hits.append((path, str(lineno), severity, m.group(0), alternatives))


def scan_narration(script_md, terms, hits):
    """SegmentParseError propagates to the caller — an ambiguous script block is a loud, hard
    failure, never a silent skip."""
    text = script_md.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return
    segs = parse_segments(text)
    if segs:
        for sid, seg_text in segs:
            for pattern, severity, alternatives, form in terms:
                m = pattern.search(seg_text)
                if m:
                    hits.append((script_md, sid, severity, m.group(0), alternatives))
        return
    # Genuine unsupported-but-real format (ep-1974's inline-bold '## SCRIPT' prose, no
    # blockquotes) — never silently skip a non-empty script, but never pretend it's the
    # normal path either.
    print(f"[FALLBACK] 0 narration segments parsed from {script_md} (non-blockquote script "
          f"format) — scanning the whole file text instead of per-segment.")
    scan_text_lines(script_md, text.split("\n"), terms, hits)


def scan_episode(ep_dir, terms):
    hits = []
    script_md = ep_dir / "edit_script.md"
    if script_md.is_file():
        scan_narration(script_md, terms, hits)

    metadata_md = ep_dir / "metadata.md"
    if metadata_md.is_file():
        lines = metadata_md.read_text(encoding="utf-8", errors="replace").split("\n")
        scan_text_lines(metadata_md, lines, terms, hits)

    html_files = []
    index_html = ep_dir / "index.html"
    if index_html.is_file():
        html_files.append(index_html)
    html_files.extend(sorted((ep_dir / "compositions").glob("*.html")))
    for html_file in html_files:
        lines = strip_html(html_file.read_text(encoding="utf-8", errors="replace"))
        scan_text_lines(html_file, lines, terms, hits)

    return hits


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 scripts/flag_words.py episodes/<slug> [--wordlist PATH]")
    ep = Path(sys.argv[1])
    if not ep.is_dir():
        sys.exit(f"not a directory: {ep}")
    wordlist_path = DEFAULT_WORDLIST
    if "--wordlist" in sys.argv:
        wordlist_path = Path(sys.argv[sys.argv.index("--wordlist") + 1])

    try:
        terms = load_terms(wordlist_path)
    except WordlistError as e:
        print(f"FLAG_WORDS FAIL - bad wordlist {wordlist_path}: {e}")
        sys.exit(2)

    try:
        hits = scan_episode(ep, terms)
    except SegmentParseError as e:
        print(f"FLAG_WORDS FAIL - could not parse narration in {ep / 'edit_script.md'}: {e}")
        sys.exit(2)

    hard_count = 0
    soft_count = 0
    for path, loc, severity, form, alternatives in hits:
        tag = "HARD" if severity == "hard" else "SOFT"
        print(f"{path}:{loc}: {tag} \"{form}\" -> {alternatives}")
        if severity == "hard":
            hard_count += 1
        else:
            soft_count += 1

    print()
    if hard_count:
        print(f"FLAG_WORDS FAIL - {hard_count} hard hit(s), {soft_count} soft warning(s). "
              f"Fix narration/on-screen text before render.")
        sys.exit(1)
    print(f"FLAG_WORDS PASS - 0 hard hits, {soft_count} soft warning(s).")
    sys.exit(0)


if __name__ == "__main__":
    main()
