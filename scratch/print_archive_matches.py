with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'.{0,100}Indigo Books Archive.{0,100}', text):
    print(m.group(0))
    print('---')
