# -*- coding: utf-8 -*-
import re

with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check raw liquid tags
raw_liquid = re.findall(r'\{\{[^}]*\}\}', html)
print('Raw liquid tags count:', len(raw_liquid))
if raw_liquid:
    print('Samples:', raw_liquid[:3])

# 2. Check emojis
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
emojis = emoji_pattern.findall(html)
print('Emojis count:', len(emojis))
if emojis:
    print('Samples:', emojis[:5])

# 3. Check hero z-index & overflow
print('hero-bg-clip present:', 'hero-bg-clip' in html)
print('ivh-section z-index 500:', 'z-index: 500' in html)

# 4. Check cart drawer
print('cartDrawer present:', 'id="cartDrawer"' in html)
print('btn-add-pop present:', 'btn-add-pop' in html)

# 5. Check Law Vault covers
print('book-sanhita.jpg present:', 'book-sanhita.jpg' in html)
print('book-kasauti.jpg present:', 'book-kasauti.jpg' in html)

# 6. Check PDP clickable author & browseAllBooks
print('pdp-clickable-author present:', 'pdp-clickable-author' in html)
print('browseAllBooks present:', 'browseAllBooks' in html)
print('searchByAuthor present:', 'searchByAuthor' in html)
print('badge-binding present:', 'badge-binding' in html)

