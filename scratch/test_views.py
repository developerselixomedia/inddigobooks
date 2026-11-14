# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.abspath('.'))

from build_html_generator import build_preview_html

html = build_preview_html()
nav_end = html.find('</header>') + len('</header>')
footer_start = html.find('<footer class="site-footer"')
content = html[nav_end:footer_start]

print('Has homepage-view:', '<div id="homepage-view"' in content)
print('Has indigo-search-results-view:', '<div id="indigo-search-results-view"' in content)
print('Has single-product-page-view:', '<div id="single-product-page-view"' in content)
print('Content length:', len(content))
