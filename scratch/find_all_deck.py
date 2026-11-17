with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,50}v2-mobile-hero-showcase.{0,100}', text)
for m in matches:
    print(m)
