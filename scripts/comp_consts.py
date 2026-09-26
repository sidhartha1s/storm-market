"""Fold a composition's timing constants into literals so the static gates can read its timeline.

Comps are authored with a `const CUES = { six: 6.84, ... }` block (word cues from words.json) and a
`const DUR = 14.45` window, and place tweens at `CUES.six`, `DUR - 0.6`, `CUES.dark + 1.5`. The gates
(sweep check 7, beat_density) parse tween positions and durations with regexes that only see numeric
literals, so every cue-positioned tween was invisible to them (ep-1974, 21 Sep 26: 14 false "holds",
one hard beat_density exit). This folds `NAME.key`, bare `NAME` numeric consts, and arithmetic on
literals into literals. Unknown identifiers are left alone: the gates then report them as before.

The arithmetic pass used to be regex passes that ran every '+' before any '-' (wrong: "10 - 2 + 3"
folded to 5.0 instead of 11.0 — left-to-right, not "additions first"). It now finds maximal spans of
number/paren/operator text and hands each to `ast.parse(mode='eval')`, which gets precedence and
associativity right for free (fix-fold-ast, 24 Sep 26).
"""
import ast
import re


def _eval_node(node):
    """Whitelist walker: numeric constants, + - * /, unary +/-. Anything else raises."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
        return float(node.value)
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        left, right = _eval_node(node.left), _eval_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        return left / right
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        val = _eval_node(node.operand)
        return -val if isinstance(node.op, ast.USub) else val
    raise ValueError(f"unsupported node {node!r}")


def _find_arith_spans(src):
    """Maximal (start, end) spans of numeric-literal arithmetic: digits, '.', parens, + - * /.

    A grammar-driven scan, not a flat regex, so a span can never start on a bare operator glued to a
    non-numeric left operand — "t0 + 0.25" must stay untouched entirely, not lose its "+ 0.25" (same
    identifier-digit-eating hazard the const substitution above already guards against).
    """
    n = len(src)

    def is_ident_char(c):
        return c.isalnum() or c in "_."

    def skip_ws(j):
        while j < n and src[j] in " \t":
            j += 1
        return j

    def parse_number(j):
        if j < n and src[j] == "-":
            j += 1
        if j >= n or not src[j].isdigit():
            return None
        while j < n and src[j].isdigit():
            j += 1
        if j < n and src[j] == "." and j + 1 < n and src[j + 1].isdigit():
            j += 1
            while j < n and src[j].isdigit():
                j += 1
        return j

    def parse_term(j):
        j = skip_ws(j)
        if j > 0 and is_ident_char(src[j - 1]):
            return None                                          # mid-identifier: t0, x1 — leave alone
        if j < n and src[j] == "(":
            res = parse_expr(j + 1)
            if res is None:
                return None
            end = skip_ws(res[0])
            if end < n and src[end] == ")":
                return end + 1
            return None
        e = parse_number(j)
        if e is None:
            return None
        if e < n and is_ident_char(src[e]):
            return None
        return e

    def parse_expr(j):
        end = parse_term(j)
        if end is None:
            return None
        has_op = False
        while True:
            k = skip_ws(end)
            if k < n and src[k] in "+-*/":
                nend = parse_term(skip_ws(k + 1))
                if nend is None:
                    break
                end, has_op = nend, True
            else:
                break
        return end, has_op

    def borders_identifier(start, end):
        """A span glued to an identifier through an operator is part of a bigger unresolved
        expression ("t0 - 0.5 - 0.2", "t0 - 2 + 3", "x * 2 + 3") — fold none of it, not just the
        literal-looking tail, or the operator that ties it to the identifier gets silently eaten.
        """
        b = start - 1
        while b >= 0 and src[b] in " \t":
            b -= 1
        if b >= 0:
            if src[b] in "-*/%":
                return True
            if src[b] == "+":
                b2 = b - 1
                while b2 >= 0 and src[b2] in " \t":
                    b2 -= 1
                if b2 >= 0 and (is_ident_char(src[b2]) or src[b2] == ")"):
                    return True
        a = skip_ws(end)
        if a < n and src[a] in "*/%":
            return True
        return False

    spans = []
    i = 0
    while i < n:
        c = src[i]
        if c.isdigit() or c == "(" or (c == "-" and i + 1 < n and src[i + 1].isdigit()):
            res = parse_expr(i)
            if res is not None and res[1]:                       # has_op: a lone literal is already folded
                if not borders_identifier(i, res[0]):
                    spans.append((i, res[0]))
                i = res[0]
                continue
        i += 1
    return spans


def _is_date_like(text):
    # dates like 2026-09 read as arithmetic (2026 - 9); a leading-zero multi-digit integer with no
    # decimal point is a date/time fragment, not a literal meant to be computed — stay text.
    return re.search(r'(?<![\d.])0\d+(?![\d.])', text) is not None


def fold(src: str) -> str:
    consts = {k: float(v) for k, v in re.findall(r'const\s+([A-Za-z_]\w*)\s*=\s*(-?[\d.]+)\s*;', src)}
    for name, body in re.findall(r'const\s+([A-Za-z_]\w*)\s*=\s*\{([^}]*)\}', src):
        for k, v in re.findall(r'(\w+)\s*:\s*(-?[\d.]+)', body):
            consts[f"{name}.{k}"] = float(v)
    for k in sorted(consts, key=len, reverse=True):          # longest first: CUES.six before CUES
        src = re.sub(r'(?<![\w.])' + re.escape(k) + r'(?![\w.(])', repr(consts[k]), src)

    out = []
    pos = 0
    for start, end in _find_arith_spans(src):
        text = src[start:end]
        out.append(src[pos:start])
        if _is_date_like(text):
            out.append(text)                                  # dates like 2026-09 stay text
        else:
            try:
                out.append(repr(round(_eval_node(ast.parse(text, mode="eval")), 4)))
            except Exception:
                out.append(text)                                # unparseable: honest "can't parse this"
        pos = end
    out.append(src[pos:])
    return "".join(out)
