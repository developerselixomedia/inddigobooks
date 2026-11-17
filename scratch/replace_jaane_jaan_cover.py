# -*- coding: utf-8 -*-
import os

target_old = "https://images.rajkamalprakashan.com/products/2026/10/22/be5f344c-82dc-4b9e-9bd0-55c58f81e88a-jaane-jaan-lucknow-front.jpg"
target_new = "assets/book-jaane-jaan-lucknow.jpg"

files = ['store_data.py', 'shopify_products_import.csv']

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        cnt = content.count(target_old)
        if cnt > 0:
            content = content.replace(target_old, target_new)
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Replaced {cnt} occurrences in {fn}")
        else:
            print(f"Target not found in {fn}")
