"""Self-check for scripts/flag_words.py: python3 scripts/test_flag_words.py

Builds a throwaway episode fixture and a throwaway wordlist in a temp dir (style of
test_gates.py). Never touches the real references/flag-words.md or a real episode.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
FAILS = []

WORDLIST = """# fixture flag-words.md

| Term(s) | Severity | Alternatives | Reason |
|---|---|---|---|
| kill / killed | hard | lost their lives; did not survive | test row |
| victims | soft | those who died | test row |
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


def make_episode(root, name, edit_script_body):
    ep = root / name
    ep.mkdir()
    (ep / "edit_script.md").write_text(edit_script_body, encoding="utf-8")
    return ep


with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    wordlist = root / "flag-words.md"
    wordlist.write_text(WORDLIST, encoding="utf-8")

    # 1. a hard hit fails with alternatives printed
    ep_hard = make_episode(root, "ep-hard", "> The tornado killed twelve people that night.\n")
    rc, out = run_gate(ep_hard, wordlist)
    check("hard hit: exit 1", rc == 1, f"rc={rc}")
    check("hard hit: prints file:line", f"{ep_hard / 'edit_script.md'}:1:" in out, out)
    check("hard hit: prints alternatives", "lost their lives; did not survive" in out, out)

    # 2. a clean script passes
    ep_clean_dir = root / "ep-clean"
    ep_clean_dir.mkdir()
    (ep_clean_dir / "edit_script.md").write_text("> The tornado struck the town at dusk.\n", encoding="utf-8")
    rc, out = run_gate(ep_clean_dir, wordlist)
    check("clean script: exit 0", rc == 0, f"rc={rc}")
    check("clean script: no HARD/SOFT hits", "HARD" not in out and "SOFT" not in out, out)

    # 3. a soft word warns but passes
    ep_soft_dir = root / "ep-soft"
    ep_soft_dir.mkdir()
    (ep_soft_dir / "edit_script.md").write_text("> The victims were remembered at a service.\n", encoding="utf-8")
    rc, out = run_gate(ep_soft_dir, wordlist)
    check("soft word: exit 0 (warns, does not fail)", rc == 0, f"rc={rc}")
    check("soft word: prints a SOFT warning", "SOFT" in out and "victims" in out, out)

    # 4. editing the md table changes the result (proves single source, no duplicated list in code)
    rc_before, out_before = run_gate(ep_soft_dir, wordlist)  # "victims" soft, passes
    wordlist2 = root / "flag-words-2.md"
    wordlist2.write_text(WORDLIST.replace("| victims | soft |", "| victims | hard |"), encoding="utf-8")
    rc_after, out_after = run_gate(ep_soft_dir, wordlist2)
    check("editing md table changes severity: was pass, now fails",
          rc_before == 0 and rc_after == 1, f"before rc={rc_before} after rc={rc_after}")
    check("editing md table changes tag printed: was SOFT, now HARD",
          "SOFT \"victims\"" in out_before and "HARD \"victims\"" in out_after,
          f"before={out_before!r} after={out_after!r}")

print()
if FAILS:
    print(f"test_flag_words: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_flag_words: all PASS")
