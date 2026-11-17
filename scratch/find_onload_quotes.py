import os

for fname in ['editorial_video_theme.py', 'store_scripts.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    matches = re.findall(r'.{0,40}onload=.{0,80}', text)
    print(f"{fname}: {len(matches)} matches")
    for m in matches:
        print("  ", m)
