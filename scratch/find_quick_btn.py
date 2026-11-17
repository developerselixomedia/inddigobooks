with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'v2-mobile-quick-btn', text)]
for m in matches:
    print('--- MATCH ---')
    print(text[max(0, m-80):min(len(text), m+200)])
