# -*- coding: utf-8 -*-
import os

print("=== Checking Viewport Meta Tag ===")

for fname in ['layout/theme.liquid', 'preview.html', 'build_html_generator.py', 'sync_preview_to_shopify.py']:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        pos = text.find('viewport')
        if pos != -1:
            snippet = text[max(0, pos-40):min(len(text), pos+120)].replace('\n', ' ')
            print(f"{fname}: {snippet}")
        else:
            print(f"{fname}: NO VIEWPORT META TAG FOUND!!!")

