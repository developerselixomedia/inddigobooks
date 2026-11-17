# -*- coding: utf-8 -*-
import re

with open('store_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

dated_urls = list(set(re.findall(r'https://images\.rajkamalprakashan\.com/products/2026/[^\s"\',]+', text)))
print(f"Total dated 2026 URLs: {len(dated_urls)}")
for u in dated_urls:
    print(" ", u)
