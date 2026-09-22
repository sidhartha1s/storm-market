"""Flesch Reading Ease for YouTube titles. Same formula as textstat, syllables by a vowel-group count with the
usual silent-e rule. Print score, words, syllables per word. Usage: python3 fre.py "title" "title" ..."""
import re, sys
def syl(w):
    w = w.lower(); w = re.sub(r"[^a-z]", "", w)
    if not w: return 1
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w); w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))
def fre(t):
    words = [x for x in re.findall(r"[A-Za-z0-9']+", t)]
    sents = max(1, len(re.findall(r"[.!?:]+", t)) or 1)
    n = len(words); s = sum(1 if x.isdigit() else syl(x) for x in words)
    return 206.835 - 1.015 * (n / sents) - 84.6 * (s / n), n, s / n
for t in sys.argv[1:]:
    f, n, spw = fre(t); print(f"{f:6.1f}  {n:2d}w  {spw:.2f} syl/w  {len(t):2d}ch  {t}")
