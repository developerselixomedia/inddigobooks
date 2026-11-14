with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print('Sections in build_html_generator.py:', matches)

