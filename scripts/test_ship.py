"""Self-check for scripts/ship.py: python3 scripts/test_ship.py (temp dirs only, never the real checkout)"""
import contextlib
import io
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ship
import stage


def refused(*args):
    try:
        ship.plan(*args)
    except SystemExit as e:
        return str(e)
    raise AssertionError(f"plan{args} was not refused")


def tree(t):
    """A main checkout and a worktree, the episode built in the worktree: tiny fake master, SRT, metadata, thumbs."""
    main, ep = t / "main", t / "wt" / "episodes" / "ep-test-1900"
    (main / "episodes" / ep.name).mkdir(parents=True)
    (ep / "renders").mkdir(parents=True)
    (ep / "thumbs").mkdir()
    (ep / "renders" / "test-final-master.mp4").write_bytes(b"MASTER")
    (ep / "renders" / "test-final.srt").write_bytes(b"1\r\n00:00 --> 00:01\r\nhi\r\n")
    (ep / "renders" / "test-final.mp4").write_bytes(b"PRE-MASTER")
    (ep / "renders" / "test-draft.mp4").write_bytes(b"DRAFT")
    (ep / "E10-test-1900-metadata.md").write_bytes(
        b"# meta\r\n\r\n## Title\r\nTBD by owner.\r\n1. A \"quoted\" | title\r\n\r\n## Thumbnail\r\nlater\r\n")
    (ep / "thumbs" / "E10-test-1900-thumb-a-gen.png").write_bytes(b"PNG")
    (ep / "thumbs" / "E10-test-1900-thumb-a-prompt.txt").write_bytes(b"prompt")  # a prompt is not a candidate
    (ep / "thumbs" / "other.png").write_bytes(b"no prefix")
    return main, ep


def snapshot(root):
    return {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


with tempfile.TemporaryDirectory() as t:
    main, ep = tree(Path(t))
    up = main / "uploads" / "E10-test-1900"

    # dry run: every action printed, nothing changed
    stage.checkouts = lambda: [(main, "main", "")]
    before = snapshot(Path(t))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        ship.main([str(ep), "test-final", "--dry-run"])
    assert snapshot(Path(t)) == before, "dry run changed files"
    assert out.getvalue().count("[dry-run] ") == 8 and "move" in out.getvalue(), out.getvalue()

    steps, others = ship.plan(ep, "test-final", main)
    assert [op for op, _, _ in steps] == ["move", "move", "link", "link", "write", "write", "write", "write"], steps
    assert {p.name for p in others} == {"test-final.mp4", "test-draft.mp4"}, others
    ship.apply(steps)

    rend = main / "episodes" / ep.name / "renders"
    assert sorted(p.name for p in rend.iterdir()) == [
        "E10-test-1900-final-master.mp4", "E10-test-1900-final-master.srt", "E10-test-1900-metadata.md"]
    assert sorted(p.name for p in up.iterdir()) == [
        "E10-test-1900-final-master.mp4", "E10-test-1900-final-master.srt", "E10-test-1900-metadata.md",
        "E10-test-1900-thumb-a-gen.png", "E10-test-1900-titles.txt"]
    assert os.path.samefile(up / "E10-test-1900-final-master.mp4", rend / "E10-test-1900-final-master.mp4")
    assert os.path.samefile(up / "E10-test-1900-final-master.srt", rend / "E10-test-1900-final-master.srt")
    assert (rend / "E10-test-1900-final-master.mp4").read_bytes() == b"MASTER"
    assert not (ep / "renders" / "test-final-master.mp4").exists()  # moved, not copied
    assert (ep / "renders" / "test-draft.mp4").exists() and (ep / "renders" / "test-final.mp4").exists()  # never deleted
    assert (up / "E10-test-1900-titles.txt").read_bytes() == b'## Title\r\nTBD by owner.\r\n1. A "quoted" | title\r\n'
    assert (up / "E10-test-1900-metadata.md").read_bytes() == (ep / "E10-test-1900-metadata.md").read_bytes()

    # second run: a no-op
    after = snapshot(Path(t))
    steps, _ = ship.plan(ep, "test-final", main)
    assert {op for op, _, _ in steps} == {"keep"}, steps
    ship.apply(steps)
    assert snapshot(Path(t)) == after

    # an edited metadata is refreshed in place, in renders and uploads, and the titles follow it
    (ep / "E10-test-1900-metadata.md").write_bytes(b"## Title\n\"Picked\" title\n\n## Thumbnail\n")
    steps, _ = ship.plan(ep, "test-final", main)
    assert [s[2].name for s in steps if s[0] == "write"] == [
        "E10-test-1900-metadata.md", "E10-test-1900-metadata.md", "E10-test-1900-titles.txt"], steps
    ship.apply(steps)
    assert (up / "E10-test-1900-titles.txt").read_bytes() == b'## Title\n"Picked" title\n'

    # a different incoming master never overwrites the final: FAIL naming both, nothing touched
    (ep / "renders" / "test-final-master.mp4").write_bytes(b"OTHER MASTER")
    before = snapshot(Path(t))
    msg = refused(ep, "test-final", main)
    assert "E10-test-1900-final-master.mp4 exists and differs" in msg and "test-final-master.mp4" in msg, msg
    assert snapshot(Path(t)) == before
    (ep / "renders" / "test-final-master.mp4").write_bytes(b"MASTER")  # the same bytes again: fine, and left in place
    assert {op for op, _, _ in ship.plan(ep, "test-final", main)[0]} == {"keep"}

    # an uploads file that is not the final master is a FAIL too, never replaced
    (up / "E10-test-1900-final-master.srt").unlink()
    (up / "E10-test-1900-final-master.srt").write_bytes(b"stale")
    assert "differs (md5)" in refused(ep, "test-final", main)

with tempfile.TemporaryDirectory() as t:
    main, ep = tree(Path(t))
    # no E number: refused, says how one is assigned
    (ep / "E10-test-1900-metadata.md").rename(ep / "metadata.md")
    msg = refused(ep, "test-final", main)
    assert "no E number" in msg and "e<nn>-" in msg and "E<nn>-<topic>-metadata.md" in msg, msg
    # a numbered slug without its metadata file: refused
    num = ep.parent / "e10-test-1900"
    ep.rename(num)
    assert "E10-test-1900-metadata.md is missing" in refused(num, "test-final", main)
    # nothing to ship: refused
    (num / "E10-test-1900-metadata.md").write_text("## Title\nx\n", encoding="utf-8")
    assert "no E10-test-1900-final-master.mp4" in refused(num, "nope", main)

print("[test_ship] PASS")
