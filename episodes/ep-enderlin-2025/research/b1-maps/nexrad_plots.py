"""Self-made NEXRAD Level II re-plots for the g-radar family (B1).

Data: NOAA NEXRAD Level II, AWS open data (bucket unidata-nexrad-level2, the successor of noaa-nexrad-level2),
lowest tilt (0.5 deg). Decoder: l2.py (message 31). Run: python3 nexrad_plots.py <dir with the .ar2 files>
  KMVX20250621_040803_V06            -> media/nexrad/kmvx-20250621-0408utc-vel.png, -cc.png   (g-radar-a3)
  K{BIS,MVX,MBX,ABR}20250621_{~0200,0300,0405,0500,0600}  -> media/nexrad/nd-refl-20250621-HHMMutc.png (g-radar)
Velocity is dealiased only inside the couplet box (median-reference unfold), a display step; values are unchanged
elsewhere. Timestamps printed here are the sweep start times read from the data (UTC).
"""
import math, os, sys, glob
import numpy as np
from PIL import Image
from l2 import sweep

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "media", "nexrad")
RAD = {"KMVX": (47.5278, -97.3253), "KBIS": (46.7708, -100.7603), "KMBX": (48.3925, -100.8644), "KABR": (45.4558, -98.4131)}


def sample(sw, radar, lat, lon, rmax=None):
    rl, ro = RAD[radar]
    dy = (lat - rl) * 111320.0
    dx = (lon - ro) * 111320.0 * np.cos(np.radians((lat + rl) / 2))
    rng = np.hypot(dx, dy); az = (np.degrees(np.arctan2(dx, dy)) + 360) % 360
    order = np.argsort(sw["az"]); A = sw["az"][order]; D = sw["data"][order]
    Ae = np.concatenate([A - 360, A, A + 360]); idx = np.clip(np.searchsorted(Ae, az), 1, len(Ae) - 1)
    idx = np.where(az - Ae[idx - 1] < Ae[idx] - az, idx - 1, idx) % len(A)
    g = np.round((rng - sw["g0"]) / sw["gs"]).astype(int)
    ok = (g >= 0) & (g < D.shape[1])
    if rmax:
        ok &= rng < rmax
    out = np.full(lat.shape, np.nan, np.float32); out[ok] = D[idx[ok], g[ok]]
    return out


def grid(lat0, lat1, lon0, lon1, W, H):
    LO, LA = np.meshgrid(np.linspace(lon0, lon1, W), np.linspace(lat1, lat0, H)); return LA, LO


def cmap(vals, stops, alpha_stops=None):
    v = np.array([s[0] for s in stops], float); c = np.array([s[1] for s in stops], float)
    out = np.zeros(vals.shape + (4,), np.uint8); f = np.isfinite(vals)
    for ch in range(3):
        out[..., ch][f] = np.interp(vals[f], v, c[:, ch]).astype(np.uint8)
    if alpha_stops:
        av = np.array([s[0] for s in alpha_stops], float); aa = np.array([s[1] for s in alpha_stops], float)
        out[..., 3][f] = (np.interp(vals[f], av, aa) * 255).astype(np.uint8)
    else:
        out[..., 3][f] = 255
    return out


def dealias_box(sw, az0, az1, r0, r1, half_a=6, half_g=14, iters=3):
    order = np.argsort(sw["az"]); A = sw["az"][order]; D = sw["data"][order].copy()
    vn = np.nanmax(np.abs(D)); rng = sw["g0"] + sw["gs"] * np.arange(D.shape[1])
    ia = np.where((A >= az0) & (A <= az1))[0]; ig = np.where((rng >= r0) & (rng <= r1))[0]
    for _ in range(iters):
        N = D.copy()
        for i in ia:
            for k in ig:
                x = D[i, k]
                if np.isnan(x):
                    continue
                m = np.nanmedian(D[max(i - half_a, 0):i + half_a + 1, max(k - half_g, 0):k + half_g + 1])
                if x - m > vn: N[i, k] = x - 2 * vn
                elif m - x > vn: N[i, k] = x + 2 * vn
        D = N
    s = dict(sw); s["az"] = A; s["data"] = D; return s


def hhmm(sw):
    ms = int(sw["ms"].min()); return "%02d:%02d:%02d" % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60)


VEL = [(-45, (215, 255, 225)), (-30, (90, 240, 140)), (-18, (20, 190, 80)), (-8, (10, 110, 50)), (-1.5, (30, 60, 45)),
       (0, (58, 62, 66)), (1.5, (70, 40, 40)), (8, (130, 20, 30)), (18, (215, 35, 45)), (30, (255, 110, 110)), (45, (255, 225, 225))]
CC = [(0.2, (255, 250, 230)), (0.55, (245, 217, 139)), (0.8, (216, 161, 58)), (0.9, (90, 118, 143)), (0.95, (38, 54, 70)), (1.05, (30, 42, 56))]
REF = [(10, (20, 60, 50)), (20, (30, 120, 70)), (30, (70, 175, 80)), (38, (225, 210, 60)), (45, (235, 150, 40)), (52, (220, 50, 45)), (60, (200, 60, 200)), (70, (255, 230, 255))]
REF_A = [(10, 0.0), (15, 0.45), (25, 0.85), (35, 0.95)]

# couplet window: 20 km x 15 km centred on the 04:08 UTC couplet (46.603 N, 97.563 W)
BOX = (46.603 - 0.0674, 46.603 + 0.0674, -97.563 - 0.1306, -97.563 + 0.1306)
# state view: equirectangular at cos(47.45)
STATE = (45.7, 49.2, -104.3, -96.3)

if __name__ == "__main__":
    src = sys.argv[1]
    os.makedirs(OUT, exist_ok=True)
    buf = open(os.path.join(src, "KMVX_0408.ar2"), "rb").read()
    v = dealias_box(sweep(buf, 2, "VEL"), 180, 202, 85e3, 125e3); c = sweep(buf, 1, "RHO")
    LA, LO = grid(*BOX, 1680, 1260)
    Image.fromarray(cmap(sample(v, "KMVX", LA, LO), VEL)).save(os.path.join(OUT, "kmvx-20250621-0408utc-vel.png"))
    Image.fromarray(cmap(sample(c, "KMVX", LA, LO), CC)).save(os.path.join(OUT, "kmvx-20250621-0408utc-cc.png"))
    print("KMVX vel sweep start", hhmm(v), "UTC, el %.2f" % v["el"], "| cc sweep start", hhmm(c), "UTC")
    LA, LO = grid(*STATE, 1300, 841)
    for t in ("0200", "0300", "0405", "0500", "0600"):
        mos = np.full(LA.shape, np.nan, np.float32); stamps = []
        for r in RAD:
            fb = open(os.path.join(src, "st_%s_%s.ar2" % (r, t)), "rb").read()
            z = sweep(fb, 1, "REF"); stamps.append(r + " " + hhmm(z))
            mos = np.fmax(mos, sample(z, r, LA, LO, rmax=300e3))
        mos[mos < 15] = np.nan
        Image.fromarray(cmap(mos, REF, REF_A)).save(os.path.join(OUT, "nd-refl-20250621-%sutc.png" % t))
        print(t, "; ".join(stamps))
