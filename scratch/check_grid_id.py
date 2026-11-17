with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'id=["\']([^"\']*(?:grid|catalog|archive|shelf)[^"\']*)["\']', text, re.IGNORECASE)
for m in sorted(set(matches))[:25]:
    print('Found ID:', m)
