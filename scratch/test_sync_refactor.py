# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
import os
import re
from build_html_generator import build_preview_html

html = build_preview_html()

# 1. Extract Navbar
nav_start = html.find('<header class="site-navbar"')
nav_end = html.find('</header>', nav_start) + len('</header>')
assert nav_start != -1 and nav_end != -1
navbar_html = html[nav_start:nav_end]
print(f"Navbar extracted: {len(navbar_html)} chars")

# 2. Extract Footer
footer_start = html.find('<footer class="site-footer"')
footer_end = html.find('</footer>', footer_start) + len('</footer>')
assert footer_start != -1 and footer_end != -1
footer_html = html[footer_start:footer_end]
print(f"Footer extracted: {len(footer_html)} chars")

# 3. Extract Floating WA button
wa_start = html.find('<a href="https://wa.me/918933063306', footer_end)
wa_end = html.find('</a>', wa_start) + len('</a>')
assert wa_start != -1 and wa_end != -1
wa_float_html = html[wa_start:wa_end]
print(f"WA Float extracted: {len(wa_float_html)} chars")

# 4. Extract Cart Drawer
cart_start = html.find('<div id="cartDrawerOverlay"')
cart_end = html.find('<!-- =========================================================================\n       14. UNIVERSAL MINI OVERVIEW MODAL', cart_start)
if cart_end == -1:
    cart_end = html.find('<div id="overviewModalOverlay"', cart_start)
cart_html = html[cart_start:cart_end].strip()
print(f"Cart drawer extracted: {len(cart_html)} chars")

# 5. Extract Overview Modal
overview_start = html.find('<div id="overviewModalOverlay"')
overview_end = html.find('<div id="loginModalOverlay"', overview_start)
overview_html = html[overview_start:overview_end].strip()
print(f"Overview modal extracted: {len(overview_html)} chars")

# 6. Extract Login Modal
login_start = html.find('<div id="loginModalOverlay"')
login_end = html.find('<script', login_start)
login_html = html[login_start:login_end].strip()
print(f"Login modal extracted: {len(login_html)} chars")

# 7. Extract Main Content (between navbar end and footer start)
main_content_html = html[nav_end:footer_start].strip()
print(f"Main content extracted: {len(main_content_html)} chars")

assert '<div id="single-product-page-view"' in main_content_html
assert '<div id="homepage-view"' in main_content_html
assert '<section id="bestsellers-podium"' in main_content_html
assert '<section id="shop-all-catalog"' in main_content_html
print("All extraction tests PASSED!")

