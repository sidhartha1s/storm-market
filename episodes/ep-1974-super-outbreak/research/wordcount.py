"""Tag-stripped narration word count per segment of edit_script.md. python3 wordcount.py [edit_script.md]"""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent.parent / "edit_script.md")
s = p.read_text(encoding="utf8").split("## SCRIPT", 1)[1].split("## Fact register", 1)[0]
tot = 0
for seg in re.split(r"\n### ", s)[1:]:
    name, body = seg.split("\n", 1)
    body = re.sub(r"\*\*A\d-S\d[^*]*\*\*", "", body); body = re.sub(r"\*\([^)]*\)\*", "", body); body = re.sub(r"\[[^\]]*\]", "", body)
    w = len(re.findall(r"[A-Za-z0-9']+", body)); tot += w
    print(f"{name[:30]:30} {w:4}")
print(f"TOTAL {tot}  voice at 152 wpm x1.10 ≈ {tot/152/1.10:.1f} min; total ≈ {tot/152/1.10 + 2.2:.1f} min with inserts, CTA, void, blackouts")
