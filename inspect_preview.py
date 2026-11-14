with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print('Sections in preview.html:', matches)

