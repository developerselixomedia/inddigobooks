import os

target = 'See full excerpt'
found_any = False
for root, dirs, files in os.walk('.'):
    if any(skip in root for skip in ['.git', 'node_modules', 'scratch']):
        continue
    for f in files:
        if f.endswith(('.liquid', '.html', '.js', '.css', '.json', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fh:
                    if target.lower() in fh.read().lower():
                        print(f"Still found in: {p}")
                        found_any = True
            except:
                pass

if not found_any:
    print("VERIFIED: 'See full excerpt' is completely removed from all theme files!")

