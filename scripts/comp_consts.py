"""Fold a composition's timing constants into literals so the static gates can read its timeline.

Comps are authored with a `const CUES = { six: 6.84, ... }` block (word cues from words.json) and a
`const DUR = 14.45` window, and place tweens at `CUES.six`, `DUR - 0.6`, `CUES.dark + 1.5`. The gates
(sweep check 7, beat_density) parse tween positions and durations with regexes that only see numeric
literals, so every cue-positioned tween was invisible to them (ep-1974, 21 Sep 26: 14 false "holds",
one hard beat_density exit). This folds `NAME.key`, bare `NAME` numeric consts, and `num op num`
arithmetic into literals. Unknown identifiers are left alone: the gates then report them as before.
"""
import re


def fold(src: str) -> str:
    consts = {k: float(v) for k, v in re.findall(r'const\s+([A-Za-z_]\w*)\s*=\s*(-?[\d.]+)\s*;', src)}
    for name, body in re.findall(r'const\s+([A-Za-z_]\w*)\s*=\s*\{([^}]*)\}', src):
        for k, v in re.findall(r'(\w+)\s*:\s*(-?[\d.]+)', body):
            consts[f"{name}.{k}"] = float(v)
    for k in sorted(consts, key=len, reverse=True):          # longest first: CUES.six before CUES
        src = re.sub(r'(?<![\w.])' + re.escape(k) + r'(?![\w.(])', repr(consts[k]), src)
    num = r'(-?\d+(?:\.\d+)?)'
    for _ in range(3):                                        # a + b - c
        src = re.sub(num + r'\s*([-+*])\s*' + num,
                     lambda m: repr(eval(f"{m.group(1)}{m.group(2)}{m.group(3)}")), src)
    return src
