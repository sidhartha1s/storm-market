"""Measure what each pipeline stage costs on this box: wall time, CPU, RAM and GPU, sampled every 2 s.

    py -3.12 scripts/stage_cost.py episodes/<slug> ops/measure/<box>-<date>.json [--stages tts,transcribe,gates,snapshot,render]

Why: the admission rule (how many stages may run at once on the ZBook or the ASUS) must come from measured
costs, not guesses. Writes the JSON after every stage, so a crash keeps what was measured. GPU numbers need
the logged-in session (an ssh session gets no GPU): run it as a scheduled task that runs only when the user is
logged on. TTS and transcription run on a scratch copy of the script (episodes/_measure-tts), so no shipped
wav is touched; gates, snapshot and the draft render run on the real episode with their own output names.
"""
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

import psutil

ROOT = Path(__file__).resolve().parent.parent
PIN = next(l.split('"')[1] for l in open(ROOT / "config.yaml", encoding="utf-8") if "hyperframes_version:" in l)


def gpu():
    """(util %, mem MiB) from nvidia-smi, or (None, None) when the GPU is not reachable from this session."""
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=10).stdout.strip().split("\n")[0]
        u, m = out.split(",")
        return int(u), int(m)
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None, None


class Sampler(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.rows, self.stop = [], threading.Event()

    def run(self):
        psutil.cpu_percent(None)
        while not self.stop.is_set():
            time.sleep(2)
            u, m = gpu()
            self.rows.append((psutil.cpu_percent(None), psutil.virtual_memory().used / 2**30, u, m))

    def summary(self, base_gb):
        if not self.rows:
            return {}
        cpu = [r[0] for r in self.rows]
        ram = [r[1] for r in self.rows]
        gu = [r[2] for r in self.rows if r[2] is not None]
        gm = [r[3] for r in self.rows if r[3] is not None]
        return {"samples": len(self.rows), "cpu_avg_pct": round(sum(cpu) / len(cpu), 1), "cpu_max_pct": max(cpu),
                "ram_peak_gb": round(max(ram), 2), "ram_added_gb": round(max(ram) - base_gb, 2),
                "gpu_util_max_pct": max(gu) if gu else None, "gpu_mem_max_mb": max(gm) if gm else None}


def stages(ep):
    slug = ep.name
    tmp = ROOT / "episodes" / "_measure-tts"
    seg = "H1-S4,A1-S1"
    snap_out = ep / ".qc-tmp" / "measure-snap"
    return {
        "tts": {"setup": lambda: (shutil.rmtree(tmp, ignore_errors=True), tmp.mkdir(), shutil.copy(ep / "edit_script.md", tmp)),
                "cmd": [sys.executable, "scripts/tts_episode.py", f"episodes/{tmp.name}", "--only", seg],
                "what": f"voice for 2 segments ({seg}) + tempo + word timing"},
        "transcribe": {"setup": lambda: [p.unlink() for p in (tmp / "audio").glob("*.words.json")],
                       "cmd": [sys.executable, "scripts/transcribe_episode.py", f"episodes/{tmp.name}"],
                       "what": "word timing for those 2 wavs (faster-whisper)"},
        "gates": {"cmd": [sys.executable, "scripts/run_gates.py", f"episodes/{slug}"], "what": "every pre-render gate"},
        # the suite stops at the first red gate, so a shipped episode that predates a rule hides the cost of the rest:
        # gate:<name> stages run each gate on its own and record its cost whatever it exits
        **{f"gate:{g}": {"cmd": [sys.executable, f"scripts/{g}", f"episodes/{slug}"] + (["--check"] if g == "build_srt.py" else []),
                         "what": f"one gate, {g}"} for g in ("render_preflight.py", "sweep_episode.py", "lint_timeline.py", "build_srt.py",
                                                            "narration_picture_check.py", "flag_words.py", "homograph_scan.py", "beat_density.py",
                                                            "media_budget.py", "audio_levels.py")},
        **{f"gate:{g}": {"cmd": ["node", f"scripts/{g}", str(ep.resolve())], "what": f"one gate, {g}"}
           for g in ("blank_scan.mjs", "overlap_check.mjs", "occlusion_check.mjs")},
        "snapshot": {"cmd": ["npx", f"hyperframes@{PIN}", "snapshot", f"episodes/{slug}", "--at", "60,120,180",
                             "--no-end", "--describe", "false", "-o", str(snap_out)], "what": "3 settle frames (headless Chromium)"},
        "render": {"cmd": ["cmd", "/c", str(ROOT / "scripts" / "render.cmd"), slug, "draft", "measure-draft"],
                   "what": "draft render of the whole episode"},
    }


def run_stage(name, st, log):
    if "setup" in st:
        st["setup"]()
    base = psutil.virtual_memory().used / 2**30
    s = Sampler()
    s.start()
    t0 = time.time()
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"\n===== {name} {time.strftime('%H:%M:%S')} {' '.join(st['cmd'])}\n")
        f.flush()
        r = subprocess.run(st["cmd"], cwd=ROOT, stdout=f, stderr=subprocess.STDOUT, shell=(st["cmd"][0] == "npx"))
    wall = round(time.time() - t0, 1)
    s.stop.set()
    s.join()
    return {"what": st["what"], "cmd": " ".join(st["cmd"]), "exit": r.returncode, "wall_s": wall, "ram_base_gb": round(base, 2),
            **s.summary(base)}


def main():
    ep, out = Path(sys.argv[1]), Path(sys.argv[2])
    wanted = sys.argv[sys.argv.index("--stages") + 1].split(",") if "--stages" in sys.argv else list(stages(ep))
    out.parent.mkdir(parents=True, exist_ok=True)
    log = out.with_suffix(".log")
    gu, gm = gpu()
    rec = {"box": os.environ.get("COMPUTERNAME"), "episode": ep.name, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
           "cpus": psutil.cpu_count(), "ram_total_gb": round(psutil.virtual_memory().total / 2**30, 1),
           "gpu_seen": gu is not None, "pin": PIN, "stages": {}}
    for name in wanted:
        rec["stages"][name] = run_stage(name, stages(ep)[name], log)
        rec["stages"][name]["finished"] = time.strftime("%H:%M:%S")
        out.write_text(json.dumps(rec, indent=1), encoding="utf-8")
        print(name, rec["stages"][name])
    rec["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    out.write_text(json.dumps(rec, indent=1), encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:  # the sampler measures a known 4 s busy loop: wall about 4 s, cpu above idle
        st = {"cmd": [sys.executable, "-c", "import time;t=time.time()\nwhile time.time()-t<4: pass"], "what": "selftest"}
        r = run_stage("selftest", st, Path(os.devnull))
        assert 3.5 < r["wall_s"] < 8 and r["samples"] >= 1 and r["cpu_max_pct"] > 0, r
        print("stage_cost self-test ok", r)
    else:
        main()
