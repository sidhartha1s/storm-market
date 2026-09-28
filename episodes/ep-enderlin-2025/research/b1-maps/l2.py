"""Minimal NEXRAD Level II (message 31) reader: returns sweeps as dicts of numpy arrays."""
import bz2, struct, numpy as np


def records(buf):
    pos = 24  # volume header
    while pos + 4 <= len(buf):
        (n,) = struct.unpack(">i", buf[pos:pos + 4]); n = abs(n); pos += 4
        chunk = buf[pos:pos + n]; pos += n
        if len(chunk) < n or n == 0:
            break
        yield bz2.decompress(chunk) if chunk[:3] == b"BZh" else chunk


def radials(buf, max_elev=99):
    for rec in records(buf):
        p = 0
        while p + 28 <= len(rec):
            size, ch, mtype = struct.unpack(">HBB", rec[p + 12:p + 16])
            if mtype != 31:
                p += 2432
                continue
            m = rec[p + 28:]
            (rid, ms, date, azn, az, comp, _s, rlen, azres, rstat, eln, cut, el, _b, _i, nblk) = struct.unpack(
                ">4sIHHfBBHBBBBfBBH", m[:32])
            if eln > max_elev:
                return
            ptrs = struct.unpack(">%dI" % nblk, m[32:32 + 4 * nblk])
            mom = {}
            for q in ptrs:
                name = m[q + 1:q + 4].decode()
                if m[q:q + 1] != b"D":
                    continue
                ng, g0, gs = struct.unpack(">HHH", m[q + 8:q + 14])
                ws = m[q + 19]
                scale, off = struct.unpack(">ff", m[q + 20:q + 28])
                dt = ">u1" if ws == 8 else ">u2"
                raw = np.frombuffer(m[q + 28:q + 28 + ng * ws // 8], dtype=dt).astype(np.float32)
                val = (raw - off) / scale
                val[raw <= 1] = np.nan
                mom[name.strip()] = (g0, gs, val)
            yield dict(eln=eln, el=el, az=az, ms=ms, date=date, mom=mom)
            p += 12 + size * 2


def sweep(buf, eln, name):
    az, data, meta, ms = [], [], None, []
    for r in radials(buf, max_elev=eln):
        if r["eln"] != eln or name not in r["mom"]:
            continue
        g0, gs, v = r["mom"][name]
        meta = (g0, gs, r["el"], r["date"])
        az.append(r["az"]); data.append(v); ms.append(r["ms"])
    n = max(len(d) for d in data)
    arr = np.full((len(data), n), np.nan, np.float32)
    for i, d in enumerate(data):
        arr[i, :len(d)] = d
    return dict(az=np.array(az), data=arr, g0=meta[0], gs=meta[1], el=meta[2], date=meta[3], ms=np.array(ms))


if __name__ == "__main__":
    import sys
    buf = open(sys.argv[1], "rb").read()
    seen = {}
    for r in radials(buf, max_elev=4):
        k = (r["eln"], round(r["el"], 1), tuple(sorted(r["mom"])))
        seen[k] = seen.get(k, 0) + 1
    for k, v in seen.items():
        print(k, v)
