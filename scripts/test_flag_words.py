"""Self-check for scripts/flag_words.py: python3 scripts/test_flag_words.py

Builds throwaway episode fixtures in a temp dir (style of test_gates.py). Never touches the
real references/flag-words.md or a real episode, except the two fixtures that deliberately
check the SHIPPED wordlist (irregular-inflection coverage, explosion-is-soft) since those are
facts about the real table, not the parser.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
REAL_WORDLIST = S.parent / "references" / "flag-words.md"
FAILS = []

WORDLIST = """# fixture flag-words.md

| Term(s) | Severity | Alternatives | Reason |
|---|---|---|---|
| kill / killed | hard | lost their lives; did not survive | test row |
| victims | soft | those who died | test row |
| explode | hard | tore through in an instant | test row |
| bomb | hard | hit with sudden force | test row |
| murder | hard | took the life of | test row |
| gun | hard | (none) | test row |
| horror | soft | the scene | test row |
| body | soft | remains | test row |
"""

BAD_SEVERITY_WORDLIST = """| Term(s) | Severity | Alternatives | Reason |
|---|---|---|---|
| kill | medium | lost their lives | bad severity |
"""

ZERO_TERMS_WORDLIST = """| Term(s) | Severity | Alternatives | Reason |
|---|---|---|---|
"""


def check(label, cond, detail=""):
    if cond:
        print(f"PASS {label}")
    else:
        FAILS.append(label)
        print(f"FAIL {label} {detail}")


def run_gate(ep_dir, wordlist_path):
    r = subprocess.run(
        [sys.executable, str(S / "flag_words.py"), str(ep_dir), "--wordlist", str(wordlist_path)],
        capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def make_episode(root, name, edit_script_body=None, metadata_body=None, composition_html=None):
    ep = root / name
    ep.mkdir()
    if edit_script_body is not None:
        (ep / "edit_script.md").write_text(edit_script_body, encoding="utf-8")
    if metadata_body is not None:
        (ep / "metadata.md").write_text(metadata_body, encoding="utf-8")
    if composition_html is not None:
        (ep / "compositions").mkdir()
        (ep / "compositions" / "g-test.html").write_text(composition_html, encoding="utf-8")
    return ep


with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    wordlist = root / "flag-words.md"
    wordlist.write_text(WORDLIST, encoding="utf-8")

    # 1. a hard hit fails with alternatives printed (blockquote narration, per-segment id)
    ep_hard = make_episode(root, "ep-hard", "### A1-S1 — narration\n> The tornado killed twelve people.\n")
    rc, out = run_gate(ep_hard, wordlist)
    check("hard hit: exit 1", rc == 1, f"rc={rc}")
    check("hard hit: reports the segment id, not a raw line number",
          f"{ep_hard / 'edit_script.md'}:a1-s1:" in out, out)
    check("hard hit: prints alternatives", "lost their lives; did not survive" in out, out)

    # 2. a clean script passes
    ep_clean = make_episode(root, "ep-clean", "### A1-S1 — narration\n> The tornado struck the town at dusk.\n")
    rc, out = run_gate(ep_clean, wordlist)
    check("clean script: exit 0", rc == 0, f"rc={rc}")
    check("clean script: no HARD/SOFT hits", "HARD" not in out and "SOFT" not in out, out)

    # 3. a soft word warns but passes
    ep_soft = make_episode(root, "ep-soft", "### A1-S1 — narration\n> The victims were remembered at a service.\n")
    rc, out = run_gate(ep_soft, wordlist)
    check("soft word: exit 0 (warns, does not fail)", rc == 0, f"rc={rc}")
    check("soft word: prints a SOFT warning", "SOFT" in out and "victims" in out, out)

    # 4. editing the md table changes the result (single source, no duplicated list in code)
    rc_before, out_before = run_gate(ep_soft, wordlist)
    wordlist2 = root / "flag-words-2.md"
    wordlist2.write_text(WORDLIST.replace("| victims | soft |", "| victims | hard |"), encoding="utf-8")
    rc_after, out_after = run_gate(ep_soft, wordlist2)
    check("editing md table changes severity: was pass, now fails",
          rc_before == 0 and rc_after == 1, f"before rc={rc_before} after rc={rc_after}")
    check("editing md table changes tag printed: was SOFT, now HARD",
          "SOFT \"victims\"" in out_before and "HARD \"victims\"" in out_after,
          f"before={out_before!r} after={out_after!r}")

    # 5. word-boundary: substrings inside other words stay clean (skill/deadline/nobody/bodyguard)
    ep_boundary = make_episode(
        root, "ep-boundary",
        "### A1-S1 — narration\n> He learned the skill near the deadline, and nobody warned the bodyguard.\n")
    rc, out = run_gate(ep_boundary, wordlist)
    check("word boundary: skill/deadline/nobody/bodyguard stay clean (exit 0)", rc == 0, f"rc={rc}")
    check("word boundary: no HARD/SOFT hits", "HARD" not in out and "SOFT" not in out, out)

    # 6. regular English inflections are caught via the suffix group (kill has no -d row here,
    #    explode/bomb/murder/gun/horror do not list their inflected forms either)
    ep_inflect = make_episode(
        root, "ep-inflect",
        "### A1-S1 — narration\n"
        "> The house exploded. Investigators found bombs. Two men were murdered. He carried guns.\n")
    rc, out = run_gate(ep_inflect, wordlist)
    check("inflections: exit 1", rc == 1, f"rc={rc}")
    for form in ("exploded", "bombs", "murdered", "guns"):
        check(f"inflections: catches {form!r}", f'"{form}"' in out, out)

    # 7. metadata.md (title/description) is scanned
    ep_meta = make_episode(root, "ep-meta", edit_script_body="### A1-S1 — narration\n> A calm evening.\n",
                            metadata_body="# Killer Storm: The Night Nobody Slept\n")
    rc, out = run_gate(ep_meta, wordlist)
    check("metadata.md: exit 1", rc == 1, f"rc={rc}")
    check("metadata.md: hit reported against metadata.md", f"{ep_meta / 'metadata.md'}:" in out, out)

    # 8. a composition HTML carrying a hard word (mirrors ep-1974's "330 KILLED" popfig) fails.
    #    Line 4 (inside <script>) also says "killed" in a JS string — must NOT be what triggers
    #    it; only line 6 (the visible span) may produce a hit.
    ep_comp = make_episode(
        root, "ep-comp", edit_script_body="### A1-S1 — narration\n> A calm evening.\n",
        composition_html=(
            '<!DOCTYPE html>\n<html><body><template>\n<script>\nvar x = "killed";\n</script>\n'
            '<div class="popfig"><span class="pf-big">330 KILLED</span></div>\n</template></body></html>'))
    rc, out = run_gate(ep_comp, wordlist)
    comp_path = ep_comp / "compositions" / "g-test.html"
    check("composition HTML: exit 1", rc == 1, f"rc={rc}")
    check("composition HTML: hit reported at line 6 (the visible span, not the script)",
          f"{comp_path}:6:" in out, out)
    check("composition HTML: no hit reported at line 4 (inside <script>)",
          f"{comp_path}:4:" not in out, out)
    check("composition HTML: exactly one HARD \"kill\" and one HARD \"killed\" (not double-counted)",
          out.count('HARD "kill"') == 1 and out.count('HARD "killed"') == 1, out)

    # 9. [FALLBACK] path: inline-bold '## SCRIPT' prose (ep-1974 layout) has no blockquotes,
    #    so parse_segments returns 0 segments on non-empty text — must fall back, loudly, and
    #    still catch the word.
    ep_fallback = make_episode(
        root, "ep-fallback",
        "# some episode\n\n## SCRIPT (readable form)\n\n**A1-S1 (10 w)** The mob murdered three "
        "people that night. [VE something]\n")
    rc, out = run_gate(ep_fallback, wordlist)
    check("fallback: prints a line starting [FALLBACK]",
          any(line.startswith("[FALLBACK]") for line in out.splitlines()), out)
    check("fallback: still catches the hard word", rc == 1 and '"murder"' in out, out)

    # 10. SegmentParseError (two blockquote paragraphs under one heading) is a loud exit 2
    ep_ambiguous = make_episode(
        root, "ep-ambiguous",
        "### A1-S1 — narration\n> First paragraph.\n\nsome note breaking it up\n\n> Second paragraph.\n")
    rc, out = run_gate(ep_ambiguous, wordlist)
    check("SegmentParseError: exit 2", rc == 2, f"rc={rc}")
    check("SegmentParseError: message names the episode script", "edit_script.md" in out, out)

    # 11. a wordlist row with an unknown severity is exit 2, not a silent drop
    bad_wordlist = root / "bad-severity.md"
    bad_wordlist.write_text(BAD_SEVERITY_WORDLIST, encoding="utf-8")
    rc, out = run_gate(ep_clean, bad_wordlist)
    check("unknown severity: exit 2", rc == 2, f"rc={rc}")
    check("unknown severity: message names the bad value", "medium" in out, out)

    # 12. a wordlist that yields 0 usable terms is exit 2, not a silent PASS
    zero_wordlist = root / "zero-terms.md"
    zero_wordlist.write_text(ZERO_TERMS_WORDLIST, encoding="utf-8")
    rc, out = run_gate(ep_clean, zero_wordlist)
    check("0 terms: exit 2 (not a silent PASS)", rc == 2, f"rc={rc}")

    # 13. against the SHIPPED wordlist: irregular inflections not reachable by plain suffix
    #     concatenation (bloody -> bloodied, terror -> terrorized) are listed as their own form
    ep_real_inflect = make_episode(
        root, "ep-real-inflect",
        "### A1-S1 — narration\n"
        "> The building exploded. Investigators found bombs. Two men were murdered. The "
        "livestock were slaughtered. He carried guns. Survivors described the horrors. She "
        "still has nightmares. There were shootings downtown. The mob terrorized the town. "
        "His shirt was bloodied.\n")
    rc, out = run_gate(ep_real_inflect, REAL_WORDLIST)
    check("shipped wordlist: exit 1 (all ten are hard)", rc == 1, f"rc={rc}")
    for form in ("exploded", "bombs", "murdered", "slaughtered", "guns", "horrors", "nightmares",
                 "shootings", "terrorized", "bloodied"):
        check(f"shipped wordlist: catches {form!r}", f'"{form}"' in out, out)

    # 14. against the SHIPPED wordlist: "explosion" is soft (literal event OK, never a simile) —
    #     the volcano fact and a paraphrased quote must not hard-fail the gate
    ep_explosion = make_episode(
        root, "ep-explosion",
        "### A1-S1 — narration\n> The report described a volcanic explosion that reshaped the island.\n")
    rc, out = run_gate(ep_explosion, REAL_WORDLIST)
    check("shipped wordlist: volcanic 'explosion' is SOFT, exit 0", rc == 0, f"rc={rc}")
    check("shipped wordlist: 'explosion' tagged SOFT, not HARD",
          'SOFT "explosion"' in out and 'HARD "explosion"' not in out, out)

print()
if FAILS:
    print(f"test_flag_words: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_flag_words: all PASS")
