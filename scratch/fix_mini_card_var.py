# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<div class="mini-book-card" data-book-id="{b[\'id\']}" data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}">'
replacement = '<div class="mini-book-card" data-book-id="{item[\'id\']}" data-title="{item[\'title\']}" data-author="{item[\'author\']}" data-price="{item[\'price\']}">'

assert target in text, "target not found in build_html_generator.py"
text = text.replace(target, replacement)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed mini-book-card variable name in build_html_generator.py!")

