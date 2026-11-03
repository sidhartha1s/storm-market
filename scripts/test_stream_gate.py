"""Self-check for stream_gate.py: python3 scripts/test_stream_gate.py

Camille's full render (25 Oct 26, learnings/render.md on claude/ep-mayfield-2021-a6d084): RENDER_WORKERS=2,
71.5 GB free, gate `enabled:false, reason: multi_worker`, 75.0 GB of disk capture asked. Its failed log was overwritten
by the 1-worker rerun, so the failing gate line is that rerun's real line (fixtures/stream_gate/camille-full-1worker.txt)
with the logged 2-worker values put back. Moore's real 2-worker line (parallel_forced) must pass.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import stream_gate  # noqa: E402

FIX = S / "fixtures" / "stream_gate"
camille_ok = (FIX / "camille-full-1worker.txt").read_text(encoding="utf-8")
camille_bad = (camille_ok.replace('"enabled":true', '"enabled":false').replace('"single_worker"', '"multi_worker"')
               .replace('"workerCount":1', '"workerCount":2'))
moore = (FIX / "moore-full-2workers.txt").read_text(encoding="utf-8")
render_cmd = (S / "render.cmd").read_text(encoding="utf-8")
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


check("Camille's multi_worker gate line stops the render", "multi_worker" in stream_gate.log_verdict(camille_bad, 60))
check("Camille's 1-worker rerun line passes", stream_gate.log_verdict(camille_ok, 60) == "ok")
check("Moore's 2-worker parallel_forced line passes", stream_gate.log_verdict(moore, 60) == "ok")
check("no gate line yet is pending", stream_gate.log_verdict("Checking browser", 60) == "pending")
check("no gate line after the watch window stops the render", stream_gate.log_verdict("Checking browser", 600) != "pending")
watch, npx = render_cmd.find('stream_gate.py" watch'), render_cmd.find("call npx hyperframes")
check("render.cmd runs watch after the worker count is final and before npx, and no disk-size launch refusal",
      render_cmd.find("render_%MODE%.workers\" set /p") < watch < npx and 'stream_gate.py" launch' not in render_cmd)

# Used vs asked (Oct 26): the ZBook's driver 595.95 is too old for ffmpeg 8.1.2's NVENC; every ZBook render printed
# "[gpuEncoder] nvenc probe failed" and hyperframes encoded on Intel QSV. Real excerpts: the ZBook bench render
# (scratch/renderspeed/bench1/log_D_w4_ss_gpu.txt) and Moore's ASUS full render, whose mp4 tag reads h264_nvenc.
zbook = (FIX / "zbook-bench-qsv-fallback.txt").read_text(encoding="utf-8")
asus = (FIX / "moore-full-asus-nvenc.txt").read_text(encoding="utf-8")
NVENC_TAG = "Lavc62.28.102 h264_nvenc"
check("ZBook bench render (nvenc probe failed) is a [FALLBACK] encoder",
      any(l.startswith("[FALLBACK] encoder") for l in stream_gate.used_vs_asked(zbook)))
check("Moore's ASUS NVENC render ran as asked", stream_gate.used_vs_asked(asus, NVENC_TAG) == [])
check("an output encoded by h264_qsv fails even with no probe line (debug off)",
      any("h264_qsv" in l for l in stream_gate.used_vs_asked(asus, "Lavc62.28.102 h264_qsv")))
check("a capture worker on the Intel iGPU fails",
      any(l.startswith("[FALLBACK] browser") for l in stream_gate.used_vs_asked(
          asus.replace("NVIDIA", "Intel", 3), NVENC_TAG)))
check("Camille's multi_worker disk capture fails as a capture fallback",
      any("multi_worker" in l for l in stream_gate.used_vs_asked(
          asus.replace('"enabled":true,"reason":"parallel_forced"', '"enabled":false,"reason":"multi_worker"'), NVENC_TAG)))
check("a log with no GPU: ask line fails", stream_gate.used_vs_asked(camille_ok) != [])
r = subprocess.run([sys.executable, str(S / "stream_gate.py"), "check", str(FIX / "zbook-bench-qsv-fallback.txt")],
                   capture_output=True, text=True)
check("CLI check exits 1 on the ZBook log and prints [FALLBACK]", r.returncode == 1 and "[FALLBACK] encoder" in r.stdout)
with tempfile.TemporaryDirectory() as d:
    log, marker, out = Path(d) / "render_full.log", Path(d) / "done.marker", Path(d) / "preflight.log"
    log.write_text(zbook, encoding="utf-8")
    killed = []
    stream_gate.kill_renders = lambda: killed.append(1)
    rc = stream_gate.watch(log, marker, out)
    check("watch stops the ZBook render at the gate line, not after 80 min",
          rc == 1 and killed and "[FALLBACK] encoder" in out.read_text(encoding="utf-8"))
debug, check_at, done_at = (render_cmd.find("set HYPERFRAMES_DEBUG_GPU_PROBE=1"), render_cmd.find('stream_gate.py" check'),
                            render_cmd.find('echo %RC% > "render_%MODE%_done.marker"'))
check("render.cmd turns on probe logging before npx and runs check after npx, before the done marker",
      0 < debug < npx < check_at < done_at)

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all stream-gate checks passed")
