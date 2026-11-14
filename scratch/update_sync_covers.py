# -*- coding: utf-8 -*-
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    c = f.read()

target = '"hero-gypsy.jpg": "{{ \'hero-gypsy.jpg\' | asset_url }}"\n};'
replacement = '''"hero-gypsy.jpg": "{{ 'hero-gypsy.jpg' | asset_url }}",
  "book-highcourt.jpg": "{{ 'book-highcourt.jpg' | asset_url }}",
  "book-samvidhan.jpg": "{{ 'book-samvidhan.jpg' | asset_url }}",
  "book-bench-bar.jpg": "{{ 'book-bench-bar.jpg' | asset_url }}",
  "book-10-faisle.jpg": "{{ 'book-10-faisle.jpg' | asset_url }}",
  "book-lawful-awful.jpg": "{{ 'book-lawful-awful.jpg' | asset_url }}",
  "book-gyan-aur-karm.jpg": "{{ 'book-gyan-aur-karm.jpg' | asset_url }}",
  "book-hindi-vyakaran.jpg": "{{ 'book-hindi-vyakaran.jpg' | asset_url }}",
  "book-hindi-sahitya-itihas.jpg": "{{ 'book-hindi-sahitya-itihas.jpg' | asset_url }}",
  "book-hindi-bhasha.jpg": "{{ 'book-hindi-bhasha.jpg' | asset_url }}",
  "book-hadappa.jpg": "{{ 'book-hadappa.jpg' | asset_url }}",
  "book-gyandan.jpg": "{{ 'book-gyandan.jpg' | asset_url }}",
  "book-halant.jpg": "{{ 'book-halant.jpg' | asset_url }}",
  "book-halyog.jpg": "{{ 'book-halyog.jpg' | asset_url }}",
  "book-savarkar.jpg": "{{ 'book-savarkar.jpg' | asset_url }}",
  "book-haashiye.jpg": "{{ 'book-haashiye.jpg' | asset_url }}",
  "book-cheelwali-kothi.jpg": "{{ 'book-cheelwali-kothi.jpg' | asset_url }}",
  "book-haadse.jpg": "{{ 'book-haadse.jpg' | asset_url }}",
  "book-aadha-gaon.jpg": "{{ 'book-aadha-gaon.jpg' | asset_url }}",
  "book-mahabhoj.jpg": "{{ 'book-mahabhoj.jpg' | asset_url }}",
  "book-shekhar.jpg": "{{ 'book-shekhar.jpg' | asset_url }}",
  "book-halaq.jpg": "{{ 'book-halaq.jpg' | asset_url }}",
  "book-gyarahaveen.jpg": "{{ 'book-gyarahaveen.jpg' | asset_url }}",
  "book-guzara-hua-zamana.jpg": "{{ 'book-guzara-hua-zamana.jpg' | asset_url }}"
};'''

if target in c:
    c = c.replace(target, replacement)
    with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated PODIUM_CDN_COVERS in sync_preview_to_shopify.py')
else:
    print('Target not matched in sync_preview_to_shopify.py')

