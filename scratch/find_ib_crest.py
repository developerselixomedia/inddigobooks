import os, re

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'brain', '.gemini', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.py', '.liquid', '.js')):
            p = os.path.join(root, f)
            try:
                c = open(p, 'r', encoding='utf-8', errors='ignore').read()
                if '>IB<' in c or 'INDIGO BOOKS INDIA' in c:
                    print(f'{p}: found IB / INDIGO BOOKS INDIA')
            except: pass
