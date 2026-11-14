# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="single-product-page-view"')
if pos != -1:
    print("Found single-product-page-view in preview.html:")
    print(text[pos:pos+1500])

import re
matches = list(re.finditer(r'\.product-pdp-grid[^{]*\{[^}]*\}', text))
print(f"\nFound {len(matches)} CSS rules for .product-pdp-grid in preview.html:")
for m in matches:
    print(m.group(0))

# Also search in assets/main-store.css
with open('assets/main-store.css', 'r', encoding='utf-8') as f:
    css_text = f.read()

matches_css = list(re.finditer(r'[^{}]*product-pdp-grid[^{]*\{[^}]*\}', css_text))
print(f"\nFound {len(matches_css)} CSS rules for product-pdp-grid in assets/main-store.css:")
for m in matches_css:
    print(m.group(0).strip())

