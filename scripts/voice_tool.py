#!/usr/bin/env python3
"""Where the narration voice tool lives, and whether every piece of it is present.

Owner 7 Oct 26: everything storm-market uses stays inside the repo folder. The voice tool is
  scripts/tts_clone.py           tracked
  external.pocket_venv_python    .venv-pocket/ in the MAIN checkout (gitignored, 4.9 GB;
                                 package list and rebuild lines: scripts/voice_requirements.txt)
  external.voice_ref             tracked, md5 pinned in external.voice_ref_md5
  external.hf_home               .models/hf in the MAIN checkout (gitignored): the cloning
                                 weights (gated repo kyutai/pocket-tts), the faster-whisper
                                 model and the Hugging Face login token
Paths in config.yaml are absolute into the main checkout so every worktree shares one copy.

  python3 scripts/voice_tool.py     one PASS/FAIL line per piece, exit 1 if any is missing
"""
import hashlib
import os
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
WEIGHTS = "hub/models--kyutai--pocket-tts/snapshots/*/languages/english*/model.safetensors"


def load_ext():
    # Own loader, not tts_episode.load_cfg: tts_clone.py imports this under the voice venv, and
    # tts_episode imports this module.
    return yaml.safe_load((REPO / "config.yaml").read_text(encoding="utf-8"))["external"]


def use_repo_models():
    """Point every Hugging Face download and lookup in this process at the repo. Call it before
    the first import that pulls in huggingface_hub (it reads HF_HOME at import)."""
    os.environ["HF_HOME"] = load_ext()["hf_home"]


def voice_md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def checks(ext, allow_download=False):
    """[(piece, ok, what to do when it is not)]. With allow_download the weights count as present
    when the login that can fetch them is there: the narration run downloads them itself."""
    hf, ref = Path(ext["hf_home"]), Path(ext["voice_ref"])
    has_login = (hf / "token").is_file()
    weights_fix = f"no kyutai/pocket-tts weights under {hf}; the next narration run downloads them" if has_login else (
        f'no kyutai/pocket-tts weights under {hf} and no login: run HF_HOME="{hf.as_posix()}" hf auth login '
        "on the account that accepted the terms at https://huggingface.co/kyutai/pocket-tts")
    return [
        ("voice venv", Path(ext["pocket_venv_python"]).is_file(),
         f"{ext['pocket_venv_python']} is missing: rebuild lines are at the top of scripts/voice_requirements.txt"),
        ("clone script", (REPO / "scripts" / "tts_clone.py").is_file(), "scripts/tts_clone.py is missing: git checkout it"),
        ("voice reference", ref.is_file() and voice_md5(ref) == ext["voice_ref_md5"],
         f"{ref} is missing or its md5 is not {ext['voice_ref_md5']}"),
        ("cloning weights", any(hf.glob(WEIGHTS)) or (allow_download and has_login), weights_fix),
    ]


def missing(ext, allow_download=False):
    return [f"{piece}: {fix}" for piece, ok, fix in checks(ext, allow_download) if not ok]


if __name__ == "__main__":
    rows = checks(load_ext())
    for piece, ok, fix in rows:
        print(f"{'PASS' if ok else 'FAIL'}  {piece}" + ("" if ok else f" — {fix}"))
    sys.exit(0 if all(ok for _, ok, _ in rows) else 1)
