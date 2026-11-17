with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find any event listeners attached to buttons
matches = [m.start() for m in re.finditer(r'addEventListener\(.*click', text)]
print(f'Click event listeners in editorial_video_theme.py: {len(matches)}')
for m in matches:
    print(text[m:m+150].replace('\n', ' '))
