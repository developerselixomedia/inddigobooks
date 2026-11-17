with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
kh = re.findall(r'KNOWN_HANDLES\s*=\s*{(.*?)}', text, re.DOTALL)
for k in kh:
    print("Found KNOWN_HANDLES:")
    print(k[:500])
