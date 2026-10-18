"""dojo_draft.cmd: a good request reaches render.cmd as `<slug> draft` with 2 workers; every bad request is refused
before render.cmd runs. Runs the real wrapper against a stub render.cmd in a temp copy, so no render starts.
Windows only (cmd.exe): python3 scripts/test_dojo_draft.py"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

WRAPPER = Path(__file__).with_name("dojo_draft.cmd")
STUB = '@echo off\r\n>"%~dp0called.txt" echo args=[%*] workers=[%RENDER_WORKERS%]\r\n'


@unittest.skipUnless(os.name == "nt", "cmd.exe")
class DojoDraft(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "scripts").mkdir()
        shutil.copy(WRAPPER, self.root / "scripts" / "dojo_draft.cmd")
        (self.root / "scripts" / "render.cmd").write_text(STUB, encoding="ascii")
        for ep in ("ep-good_1", "-dash"):
            (self.root / "episodes" / ep).mkdir(parents=True)
            (self.root / "episodes" / ep / "index.html").write_text("x")
        self.lad = self.root / "lad"
        (self.lad / "dojo-ops").mkdir(parents=True)
        self.req = self.lad / "dojo-ops" / "render-request.txt"
        self.called = self.root / "scripts" / "called.txt"

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def run_wrapper(self, request: bytes | None) -> int:
        self.called.unlink(missing_ok=True)
        if request is not None:
            self.req.write_bytes(request)
        env = {**os.environ, "LOCALAPPDATA": str(self.lad)}
        env.pop("RENDER_WORKERS", None)
        return subprocess.run(["cmd.exe", "/d", "/c", str(self.root / "scripts" / "dojo_draft.cmd")], env=env,
                              capture_output=True, timeout=30).returncode

    def test_good_slugs_reach_render_cmd(self):
        # A trailing CR is dropped by set /p; a leading dash is only a folder name.
        for request, slug in ((b"ep-good_1", "ep-good_1"), (b"ep-good_1\r", "ep-good_1"), (b"-dash", "-dash")):
            with self.subTest(request=request):
                self.assertEqual(self.run_wrapper(request), 0)
                self.assertEqual(self.called.read_text().strip(), f"args=[{slug} draft] workers=[2]")
                self.assertFalse(self.req.exists())
                self.assertFalse(Path(str(self.req) + ".chk").exists())

    def test_bad_requests_never_reach_render_cmd(self):
        bad = [b"", b"ep good", b"ep&calc", b"ep|x", b'ep"x', b"ep%PATH%", b"ep^x", b"..\\ep-good_1", b"ep/x",
               "epé".encode(), b"ep-good_1\nep&calc", b"ep&calc\nep-good_1", b"ep-good_1\r\nep-good_1",
               b"ep-good_1\x00", b"ep(x)", b"ep!x", b"ep<x", b"ep>x", b"ep-good_1\n"]
        for request in bad:
            with self.subTest(request=request):
                self.assertEqual(self.run_wrapper(request), 3)
                self.assertFalse(self.called.exists())
                self.assertFalse(self.req.exists())

    def test_a_check_that_cannot_run_refuses(self):
        # Opus review 18 Oct 2026: a directory on the .chk name made the old checks fail open.
        chk = Path(str(self.req) + ".chk")
        chk.mkdir()
        (chk / "keep.txt").write_text("x")
        self.assertEqual(self.run_wrapper(b"x\\..\\ep-good_1"), 3)
        self.assertFalse(self.called.exists())
        self.assertTrue((chk / "keep.txt").exists())

    def test_overlong_line_never_reaches_render_cmd(self):
        # set /p keeps 1023 bytes; the cut name must never reach render.cmd.
        self.assertIn(self.run_wrapper(b"a" * 9000), (3, 4))
        self.assertFalse(self.called.exists())

    def test_no_request_and_unknown_episode(self):
        self.assertEqual(self.run_wrapper(None), 2)
        self.assertEqual(self.run_wrapper(b"ep-missing"), 4)
        self.assertFalse(self.called.exists())


if __name__ == "__main__":
    sys.exit(unittest.main())
