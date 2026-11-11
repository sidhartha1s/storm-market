"""Self-check for scripts/episode.py: python3 scripts/test_episode.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import episode as e

# kinds: the e10- form CLAUDE.md step 7 asks for is a documentary under the current contract
for slug in ("e10-hattiesburg-2013", "ep-galveston-1900"):
    assert e.is_documentary(slug) and e.is_current_documentary(slug), slug
for slug in ("ep4-el-reno", "ep1-joplin"):
    assert e.is_documentary(slug) and not e.is_current_documentary(slug), slug
for slug in ("ms-krakatoa-1883", "sh-hawaii-lowell-1", "br-elnino-california", "demo-pin", "episode-x", "e-foo", "expo-1"):
    assert not e.is_documentary(slug), slug
assert e.is_mini("ms-krakatoa-1883") and not e.is_mini("ep-galveston-1900")

with tempfile.TemporaryDirectory() as t:
    eps = Path(t)
    for slug, meta in (("ep4-el-reno", "E01-el-reno-2013-metadata.md"), ("ep-galveston-1900", "E09-galveston-1900-metadata.md"),
                       ("e10-hattiesburg-2013", None), ("ep-enderlin-2025", "metadata.md"), ("ms-krakatoa-1883", None)):
        (eps / slug).mkdir()
        if meta:
            (eps / slug / meta).write_text("x", encoding="utf-8")
    assert e.identity(eps / "ep4-el-reno") == (1, "el-reno-2013")
    assert e.label(eps / "ep-galveston-1900") == "E09-galveston-1900"
    assert e.label(eps / "e10-hattiesburg-2013") == "E10-hattiesburg-2013"
    assert e.identity(eps / "ep-enderlin-2025") is None and e.label(eps / "ms-krakatoa-1883") is None
    assert sorted(e.numbered(eps)) == [1, 9, 10]
    assert e.next_number(eps) == 11

    # two folders on one number, or two numbers in one folder, stop the run
    probe = "import sys; sys.path.insert(0, sys.argv[1]); import episode; episode.numbered(sys.argv[2])"
    run = lambda: subprocess.run([sys.executable, "-c", probe, str(Path(__file__).resolve().parent), t],
                                 capture_output=True, text=True)
    assert run().returncode == 0
    (eps / "e9-dup").mkdir()
    r = run()
    assert r.returncode != 0 and "E09 is claimed by both" in r.stderr, r.stderr
    (eps / "e9-dup").rmdir()
    (eps / "ep4-el-reno" / "E03-other-metadata.md").write_text("x", encoding="utf-8")
    r = run()
    assert r.returncode != 0 and "one episode, one number" in r.stderr, r.stderr

# the real repo: E01 to E09 are the nine shipped documentaries, each on its own number
real = e.numbered(Path(__file__).resolve().parent.parent / "episodes")
assert [n for n in sorted(real) if n <= 9] == list(range(1, 10)), sorted(real)
assert real[1].name == "ep4-el-reno" and real[9].name == "ep-galveston-1900", real

print("[test_episode] PASS")
