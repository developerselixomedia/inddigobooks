# -*- coding: utf-8 -*-
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''        "book-highcourt.jpg": "{{ 'book-highcourt.jpg' | asset_url }}",
        "book-samvidhan.jpg": "{{ 'book-samvidhan.jpg' | asset_url }}",
        "book-bench-bar.jpg": "{{ 'book-bench-bar.jpg' | asset_url }}",
        "book-10-faisle.jpg": "{{ 'book-10-faisle.jpg' | asset_url }}",'''

replacement = '''        "book-highcourt.jpg": "{{ 'book-highcourt.jpg' | asset_url }}",
        "book-samvidhan.jpg": "{{ 'book-samvidhan.jpg' | asset_url }}",
        "book-sanhita.jpg": "{{ 'book-sanhita.jpg' | asset_url }}",
        "book-kasauti.jpg": "{{ 'book-kasauti.jpg' | asset_url }}",
        "book-shilp-vidhi.jpg": "{{ 'book-shilp-vidhi.jpg' | asset_url }}",
        "book-anusandhan.jpg": "{{ 'book-anusandhan.jpg' | asset_url }}",
        "book-badalata-desh.jpg": "{{ 'book-badalata-desh.jpg' | asset_url }}",
        "book-nyay-sangharsh.jpg": "{{ 'book-nyay-sangharsh.jpg' | asset_url }}",
        "book-soochana.jpg": "{{ 'book-soochana.jpg' | asset_url }}",
        "book-azad.jpg": "{{ 'book-azad.jpg' | asset_url }}",
        "vault-law-highcourt": "{{ 'book-highcourt.jpg' | asset_url }}",
        "vault-law-constitution": "{{ 'book-samvidhan.jpg' | asset_url }}",
        "vault-law-ucc": "{{ 'book-sanhita.jpg' | asset_url }}",
        "vault-law-judiciary": "{{ 'book-kasauti.jpg' | asset_url }}",
        "book-bench-bar.jpg": "{{ 'book-bench-bar.jpg' | asset_url }}",
        "book-10-faisle.jpg": "{{ 'book-10-faisle.jpg' | asset_url }}",'''

assert target in text, 'target not found'
text = text.replace(target, replacement)
with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated cdn_covers_map in sync_preview_to_shopify.py!")
