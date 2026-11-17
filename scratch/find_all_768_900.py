with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for match in re.finditer(r'@media[^{]+(768px|900px|901px)[^{]*\{', text):
    start = match.start()
    print(f"Match at {start}: {match.group().strip()}")
    print(text[start:start+250].replace('\n', ' '))
    print('='*50)
