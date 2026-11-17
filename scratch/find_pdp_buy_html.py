with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'pdpBuyNow', text)]
print('Matches in preview.html:', len(matches))
for m in matches:
    print(m, text[max(0, m-50):min(len(text), m+100)])
