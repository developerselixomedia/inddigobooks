with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'express-checkout-card', text)]
for m in matches:
    print('MATCH AT', m, ':', text[max(0, m-50):min(len(text), m+250)])
