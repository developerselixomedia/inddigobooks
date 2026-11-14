# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """<div class="rekhta-book-card" data-poet="{b.get('poet', 'all')}" data-book-id="{b['id']}">'"""
if target not in text:
    target = """<div class="rekhta-book-card" data-poet="{b.get('poet', 'all')}" data-book-id="{b['id']}">'"""

# Let's search for the line
import re
match = re.search(r'<div class="rekhta-book-card" data-poet="[^"]*" data-book-id="[^"]*">', text)
if match:
    old_str = match.group(0)
    new_str = old_str[:-1] + ' data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}">'
    text = text.replace(old_str, new_str)
    with open('build_html_generator.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated rekhta-book-card data attributes successfully!")
else:
    print("rekhta-book-card not matched")

