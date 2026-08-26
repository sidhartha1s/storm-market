import re, os

files = []
for root, dirs, fs in os.walk('landing'):
    for f in fs:
        if f == 'index.html':
            files.append(os.path.join(root, f))

def norm(path):
    return path.replace(os.sep, '/')

missing = []
all_hrefs = []
for fp in files:
    fpn = norm(fp)
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    for m in re.finditer(r'href="(/[^"]*)"', content):
        href = m.group(1)
        all_hrefs.append((fpn, href))
        if href.startswith('//') or href.startswith('http'):
            continue
        path = href.split('#')[0].split('?')[0]
        if path == '' or path == '/':
            continue
        rel = 'landing' + path
        if rel.endswith('/'):
            target = rel + 'index.html'
        else:
            target = rel
        if not os.path.exists(target):
            missing.append((fpn, href))

for fp, href in sorted(set(missing)):
    print(fp, '->', href)
print('total distinct missing refs:', len(set(missing)))
