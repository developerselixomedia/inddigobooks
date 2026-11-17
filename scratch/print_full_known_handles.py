with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
kh = re.search(r'var KNOWN_HANDLES\s*=\s*{(.*?)};', text, re.DOTALL)
if kh:
    print(kh.group(0))
