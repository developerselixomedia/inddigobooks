with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,40}background-image:.{0,80}', text)
for m in matches:
    print(m)
