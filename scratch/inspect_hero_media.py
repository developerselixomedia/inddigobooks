with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'@media[^{]*\{[^}]*scatter[^}]*\}', text, re.I)
print(f'Media queries with scatter: {len(matches)}')
for m in matches:
    print(m)
    print('---')
