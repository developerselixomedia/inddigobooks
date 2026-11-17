with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,50}scatter-book-cover.{0,100}', text)
print(f'Matches for scatter-book-cover in preview.html: {len(matches)}')
for m in matches[:10]:
    print(m)
