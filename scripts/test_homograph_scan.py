"""Self-check for scripts/homograph_scan.py: python3 scripts/test_homograph_scan.py

Runs against the SHIPPED references/homographs.md, not a private fixture wordlist -- this
locks in the real "lives" row (the exact defect this gate exists to catch, learnings/audio-tts.md
2026-09-27/28), not just a parser detail that could stay green while the shipped table went
blank or dropped the row.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
FAILS = []


def check(label, cond, detail=""):
    if cond:
        print(f"PASS {label}")
    else:
        FAILS.append(label)
        print(f"FAIL {label} {detail}")


def run_gate(ep_dir, wordlist=None):
    cmd = [sys.executable, str(S / "homograph_scan.py"), str(ep_dir)]
    if wordlist:
        cmd += ["--wordlist", str(wordlist)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


with tempfile.TemporaryDirectory() as d:
    root = Path(d)

    # 1. the required regression: "lives" in "they lost their lives" must be flagged, one line
    #    naming the count and the sentence it first appears in.
    ep = root / "ep-lives"
    ep.mkdir()
    (ep / "edit_script.md").write_text(
        "### A1-S1 — narration\n> Seven tornadoes touched down that day. They lost their lives "
        "before the sirens ever sounded.\n", encoding="utf-8")
    rc, out = run_gate(ep)
    check("lives: exit 0 (WARN, never blocks a render on its own)", rc == 0, f"rc={rc}")
    check('lives: one line names the count and first sentence',
          '"lives" - 1 occurrence(s); first' in out
          and "They lost their lives before the sirens ever sounded." in out, out)
    check("lives: prints both senses on that line", "sense A:" in out and "sense B:" in out, out)
    check("lives: WARN summary names the count and measurement-not-guess rule",
          "HOMOGRAPH_SCAN WARN - 1 word(s) flagged, 1 occurrence(s) total" in out
          and "measurement, never by guess" in out, out)

    # 2. a sentence with no homograph passes clean, 0 occurrences (sanity check the gate isn't
    #    flagging everything).
    ep_clean = root / "ep-clean"
    ep_clean.mkdir()
    (ep_clean / "edit_script.md").write_text(
        "### A1-S1 — narration\n> The storm moved north overnight.\n", encoding="utf-8")
    rc2, out2 = run_gate(ep_clean)
    check("clean sentence: exit 0", rc2 == 0, f"rc={rc2}")
    check("clean sentence: PASS with 0 occurrences",
          "HOMOGRAPH_SCAN PASS - 0 homograph occurrences." in out2, out2)

    # 3. a reference-only (Scan: no) row, like "survey", is never flagged even though it's a
    #    real heteronym in the table -- the gate is scoped to the known-risk rows only.
    ep_survey = root / "ep-survey"
    ep_survey.mkdir()
    (ep_survey / "edit_script.md").write_text(
        "### A1-S1 — narration\n> The NWS team began a damage survey the next morning.\n",
        encoding="utf-8")
    rc3, out3 = run_gate(ep_survey)
    check("Scan=no row (survey): not flagged", '"survey"' not in out3, out3)
    check("Scan=no row (survey): still PASS", "HOMOGRAPH_SCAN PASS" in out3, out3)

    # 4. a wordlist with one flagged (Scan: yes) row and one reference-only (Scan: no) row --
    #    the reference row is parsed without error but produces no term.
    wordlist_ok = root / "wordlist-ok.md"
    wordlist_ok.write_text(
        "| Word(s) | Scan | Sense A | Sense B | Hint |\n|---|---|---|---|---|\n"
        "| bow | yes | verb bow down | noun bow and ribbon | test row |\n"
        "| row | no | line of houses | argument | reference only |\n",
        encoding="utf-8")
    ep_bow = root / "ep-bow"
    ep_bow.mkdir()
    (ep_bow / "edit_script.md").write_text(
        "### A1-S1 — narration\n> He gave a small bow before the crowd.\n", encoding="utf-8")
    rc4, out4 = run_gate(ep_bow, wordlist_ok)
    check("mixed wordlist: Scan=yes row flags", rc4 == 0 and '"bow"' in out4, out4)

    # 5. a malformed wordlist (unknown Scan value) is a hard exit 2, not a silent pass.
    bad_scan = root / "bad-scan.md"
    bad_scan.write_text(
        "| Word(s) | Scan | Sense A | Sense B | Hint |\n|---|---|---|---|---|\n"
        "| bow | maybe | a | b | bad scan value |\n", encoding="utf-8")
    rc5, out5 = run_gate(ep_clean, bad_scan)
    check("malformed wordlist (bad Scan value): exit 2", rc5 == 2, f"rc={rc5}")
    check("malformed wordlist: message names the bad value", "'maybe'" in out5, out5)

    # 6. a wordlist with 0 Scan=yes rows is also a hard exit 2, not a silent no-op PASS.
    zero_scanned = root / "zero-scanned.md"
    zero_scanned.write_text(
        "| Word(s) | Scan | Sense A | Sense B | Hint |\n|---|---|---|---|---|\n"
        "| row | no | line of houses | argument | reference only |\n", encoding="utf-8")
    rc6, out6 = run_gate(ep_clean, zero_scanned)
    check("0 Scan=yes rows: exit 2 (not a silent PASS)", rc6 == 2, f"rc={rc6}")

print()
if FAILS:
    print(f"test_homograph_scan: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_homograph_scan: all PASS")
