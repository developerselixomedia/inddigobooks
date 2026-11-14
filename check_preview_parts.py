with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
headers = [
    '<!DOCTYPE html>',
    '<nav id="indigo-main-header"',
    'id="indigo-video-hero"',
    'class="marquee-ribbon"',
    'class="stats-bar"',
    'id="bestsellers-podium"',
    'id="mehfil-rekhta"',
    'id="contemporary-fiction"',
    'id="law-academic-vault"',
    'class="promo-banners-section"',
    'id="shop-all-catalog"',
    'id="indigo-dedicated-product-page"',
    'id="cartDrawer"',
    '<script>'
]

for h in headers:
    pos = text.find(h)
    print(f"{h:35} pos: {pos}")

