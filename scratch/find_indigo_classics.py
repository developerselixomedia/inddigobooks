import os

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'brain', '.gemini', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.py', '.liquid', '.js')):
            p = os.path.join(root, f)
            try:
                c = open(p, 'r', encoding='utf-8', errors='ignore').read()
                if 'By Indigo Classics' in c or 'Indigo Books Archive' in c:
                    print(f'{p}: found Indigo Books Archive')
            except: pass
