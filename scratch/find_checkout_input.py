import os

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'brain', '.gemini', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.py', '.liquid', '.js')):
            p = os.path.join(root, f)
            try:
                c = open(p, 'r', encoding='utf-8', errors='ignore').read()
                if 'Mobile Number (for Courier Tracking' in c or '1-Click Express Checkout' in c:
                    print(f'Found in {p}')
            except: pass
