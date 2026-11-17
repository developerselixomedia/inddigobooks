# -*- coding: utf-8 -*-
import re

with open('store_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

urls = list(set(re.findall(r'https://images\.rajkamalprakashan\.com/[^\s"\',]+', text)))
print(f"Total unique rajkamal image URLs in store_data.py: {len(urls)}")
for u in urls[:10]:
    print(" ", u)
