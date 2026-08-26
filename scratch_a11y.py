import re, glob

files = glob.glob('landing/**/index.html', recursive=True)
issues = []
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    # images missing alt
    for m in re.finditer(r'<img\b([^>]*)>', content):
        tag = m.group(1)
        if 'alt=' not in tag:
            issues.append((fp, 'img missing alt', tag[:80]))
    # iframes missing title
    for m in re.finditer(r'<iframe\b([^>]*)>', content):
        tag = m.group(1)
        if 'title=' not in tag:
            issues.append((fp, 'iframe missing title', tag[:80]))
    # heading order: crude check h1 count
    h1s = re.findall(r'<h1[ >]', content)
    if len(h1s) != 1:
        issues.append((fp, f'h1 count = {len(h1s)}', ''))

for fp, kind, extra in issues:
    print(fp, '|', kind, '|', extra)
print('total issues', len(issues))
