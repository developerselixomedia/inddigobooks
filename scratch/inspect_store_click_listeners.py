with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

matches = [m.start() for m in re.finditer(r'addEventListener\(.*click', text)]
print(f'Click event listeners in store_scripts.py: {len(matches)}')
for m in matches:
    print(text[m:m+150].replace('\n', ' '))
