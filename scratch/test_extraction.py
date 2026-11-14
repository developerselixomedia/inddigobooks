# -*- coding: utf-8 -*-
with open("build_html_generator.py", "r", encoding="utf-8") as f:
    code = f.read()

import re

# In build_preview_html(), let's run build_preview_html()
from build_html_generator import build_preview_html
html = build_preview_html()

# Find navbar
nav_start = html.find('<header class="site-navbar"')
nav_end = html.find('</header>', nav_start) + len('</header>')
navbar_html = html[nav_start:nav_end]
print(f"Navbar extracted: {len(navbar_html)} chars")

# Find footer
footer_start = html.find('<footer class="site-footer"')
footer_end = html.find('</footer>', footer_start) + len('</footer>')
footer_html = html[footer_start:footer_end]
print(f"Footer extracted: {len(footer_html)} chars")

# Find cart drawer
cart_start = html.find('<div id="cartDrawerOverlay"')
cart_end = html.find('<!-- =========================================================================\n       14. UNIVERSAL MINI OVERVIEW MODAL', cart_start)
if cart_end == -1:
    cart_end = html.find('<div id="overviewModalOverlay"', cart_start)
cart_html = html[cart_start:cart_end].strip()
print(f"Cart drawer extracted: {len(cart_html)} chars")

# Find overview modal
overview_start = html.find('<div id="overviewModalOverlay"')
overview_end = html.find('<div id="loginModalOverlay"', overview_start)
overview_html = html[overview_start:overview_end].strip()
print(f"Overview modal extracted: {len(overview_html)} chars")

# Find login modal
login_start = html.find('<div id="loginModalOverlay"')
login_end = html.find('<script', login_start)
login_html = html[login_start:login_end].strip()
print(f"Login modal extracted: {len(login_html)} chars")

# Find main content (between navbar and footer)
main_content = html[nav_end:footer_start].strip()
print(f"Main content extracted: {len(main_content)} chars")

assert '<div id="single-product-page-view"' in main_content
assert '<div id="homepage-view"' in main_content
assert '<section id="bestsellers-podium"' in main_content
assert '<section id="shop-all-catalog"' in main_content
print("All assertions passed!")

