# -*- coding: utf-8 -*-
with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Vault card
old_vc = '<div class="vault-card">'
new_vc = '<div class="vault-card" data-book-id="{b[\'id\']}" data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}" data-binding="{b.get(\'binding\', \'Paperback\')}">'
if old_vc in text:
    text = text.replace(old_vc, new_vc)
    print("1. Added data attributes to vault-card in build_html_generator.py")

# 2. Rekhta card
old_rc = '<div class="rekhta-card">'
new_rc = '<div class="rekhta-card" data-book-id="{b[\'id\']}" data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}">'
if old_rc in text:
    text = text.replace(old_rc, new_rc)
    print("2. Added data attributes to rekhta-card in build_html_generator.py")

# 3. Contemporary feat card
old_fc = '<div class="feat-book-card">'
new_fc = '<div class="feat-book-card" data-book-id="{HINDI_FEATURE_BOOK[\'id\']}" data-title="{HINDI_FEATURE_BOOK[\'title\']}" data-author="{HINDI_FEATURE_BOOK[\'author\']}" data-price="{HINDI_FEATURE_BOOK[\'price\']}">'
if old_fc in text:
    text = text.replace(old_fc, new_fc)
    print("3. Added data attributes to feat-book-card in build_html_generator.py")

# 4. Contemporary mini card
old_mc = '<div class="mini-book-card">'
new_mc = '<div class="mini-book-card" data-book-id="{b[\'id\']}" data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}">'
if old_mc in text:
    text = text.replace(old_mc, new_mc)
    print("4. Added data attributes to mini-book-card in build_html_generator.py")

# 5. Hero cards
old_hc = '<div class="hero-video-book-card ivh-book-card"'
new_hc = '<div class="hero-video-book-card ivh-book-card" data-book-id="{b[\'id\']}" data-title="{b[\'title\']}" data-author="{b[\'author\']}" data-price="{b[\'price\']}"'
if old_hc in text:
    text = text.replace(old_hc, new_hc)
    print("5. Added data attributes to hero cards in build_html_generator.py")

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

# Also in store_scripts.py for catalog cards
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    stext = f.read()

old_cc = '<div class="catalog-card"'
new_cc = '<div class="catalog-card" data-book-id="${escapeHtml(book.id)}" data-title="${escapeHtml(book.title)}" data-author="${escapeHtml(book.author || book.vendor || \'\')}" data-price="${escapeHtml(book.price || \'299\')}"'
if old_cc in stext:
    stext = stext.replace(old_cc, new_cc)
    with open('store_scripts.py', 'w', encoding='utf-8') as f:
        f.write(stext)
    print("6. Added data attributes to catalog-card in store_scripts.py")

print("Finished adding card data attributes successfully!")

