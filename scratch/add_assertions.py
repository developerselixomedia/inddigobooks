# -*- coding: utf-8 -*-
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'main_content_html = html[nav_end:footer_start].strip()'
replacement = '''main_content_html = html[nav_end:footer_start].strip()

    assert '<div id="homepage-view"' in main_content_html, 'homepage-view missing from main content!'
    assert '<div id="indigo-search-results-view"' in main_content_html, 'indigo-search-results-view missing from main content!'
    assert '<div id="single-product-page-view"' in main_content_html, 'single-product-page-view missing from main content!'
    print("All 3 views (homepage, search results, single product) verified in main content!")'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added view assertions to sync_preview_to_shopify.py!")
else:
    print("Target not found")

