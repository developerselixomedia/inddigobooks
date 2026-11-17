with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'scrollToAppSection', text)]
print('Matches for scrollToAppSection in editorial_video_theme.py:', len(matches))
for m in matches:
    print(m, text[max(0, m-50):min(len(text), m+150)].replace('\n', ' '))
