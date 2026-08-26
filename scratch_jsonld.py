import re, os, json, glob

files = glob.glob('landing/**/index.html', recursive=True)
bad = []
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, re.S):
        block = m.group(1).strip()
        try:
            json.loads(block)
        except Exception as e:
            bad.append((fp, str(e)))

for fp, e in bad:
    print(fp, '->', e)
print('total bad blocks:', len(bad), 'of', len(files), 'files scanned')
