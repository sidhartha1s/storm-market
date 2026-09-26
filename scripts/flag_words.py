"""Fail the build on violence/death vocabulary that trips YouTube's transcript scan.

Single source of truth is `references/flag-words.md` — this script never hardcodes the word
list, only the parser for that table (Term(s) | Severity | Alternatives | Reason). Scans:
  - narration: lines starting with "> " in episodes/<slug>/edit_script.md
  - on-screen text: visible text in index.html and compositions/*.html, scripts/styles stripped

Word-boundary, case-insensitive. Hard hits print with their alternatives and fail the gate
(exit 1). Soft hits print as warnings and do not fail it.

Usage: python3 scripts/flag_words.py episodes/<slug> [--wordlist PATH]
"""
import re
import sys
from pathlib import Path

DEFAULT_WORDLIST = Path(__file__).resolve().parent.parent / "references" / "flag-words.md"
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
ENTITIES = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&nbsp;": " ", "&#39;": "'", "&quot;": '"'}


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
            continue
        for form in [f.strip() for f in term_cell.split("/") if f.strip()]:
            pattern = re.compile(r"\b" + re.sub(r"\s+", r"\\s+", re.escape(form)) + r"\b", re.IGNORECASE)
            terms.append((pattern, severity, alternatives, form))
    return terms


def strip_html(html_text):
    """Return (line_text_or_None) per source line, None where the line is inside <script>/<style>."""
    no_script = SCRIPT_STYLE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), html_text)
    lines = []
    for raw in no_script.split("\n"):
        visible = TAG_RE.sub(" ", raw)
        for ent, ch in ENTITIES.items():
            visible = visible.replace(ent, ch)
        lines.append(visible)
    return lines


def scan_text_lines(path, lines, terms, hits):
    for lineno, line in enumerate(lines, start=1):
        for pattern, severity, alternatives, form in terms:
            if pattern.search(line):
                hits.append((path, lineno, severity, form, alternatives))


def scan_episode(ep_dir, terms):
    hits = []
    script_md = ep_dir / "edit_script.md"
    if script_md.is_file():
        narration_lines = []
        for line in script_md.read_text(encoding="utf-8", errors="replace").split("\n"):
            narration_lines.append(line[2:] if line.startswith("> ") else "")
        scan_text_lines(script_md, narration_lines, terms, hits)

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

    terms = load_terms(wordlist_path)
    hits = scan_episode(ep, terms)

    hard_count = 0
    soft_count = 0
    for path, lineno, severity, form, alternatives in hits:
        tag = "HARD" if severity == "hard" else "SOFT"
        print(f"{path}:{lineno}: {tag} \"{form}\" -> {alternatives}")
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
