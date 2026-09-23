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
    # num must stand alone: a word char right before/after it means it is part of an
    # identifier (t0, x1), not a literal. Without the lookaround, "t0 + 0.25" matched the "0"
    # inside "t0" as the left operand and folded to "t0.25" (qc-gates-10 RCA, 23 Sep 26) —
    # silently eating the identifier's digit and handing the gates a wrong number instead of
    # an honest "can't parse this".
    num = r'(?<![\w.])(-?\d+(?:\.\d+)?)(?![\w.])'
    ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}
    def calc(op):
        def _calc(m):                                          # dates like 2026-09 stay text
            a, b = m.group(1), m.group(2)
            if (len(a) > 1 and a.lstrip("-").startswith("0") and "." not in a) or (len(b) > 1 and b.startswith("0") and "." not in b):
                return m.group(0)
            return repr(round(ops[op](float(a), float(b)), 4))
        return _calc
    for _ in range(3):                                        # a + b - c, chained
        for op in ("*", "+", "-"):                            # multiply before add/subtract:
            src = re.sub(num + r'\s*' + re.escape(op) + r'\s*' + num, calc(op), src)  # "DUR - 2*0.5" folded 4.0 instead of 9.0 with one combined pass
    return src
