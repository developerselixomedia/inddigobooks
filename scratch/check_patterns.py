import os, re

regex = re.compile(r'<input[^>]*pattern=["\'][^"\']*["\'][^>]*>', re.IGNORECASE)

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'brain', '.gemini', 'node_modules']):
        continue
    for f in files:
        if f.endswith(('.html', '.py', '.liquid', '.js')):
            p = os.path.join(root, f)
            try:
                c = open(p, 'r', encoding='utf-8', errors='ignore').read()
                matches = regex.findall(c)
                if matches:
                    print(f'{p}:')
                    for m in matches:
                        print('   ', m.strip()[:140])
            except Exception as e:
                pass
