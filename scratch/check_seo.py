with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

import re
titles = re.findall(r'<title>.*?</title>', text, re.IGNORECASE | re.DOTALL)
print('Title tags in theme.liquid:', titles)

schemas = re.findall(r'<script type="application/ld\+json">.*?</script>', text, re.DOTALL)
print(f'JSON-LD in theme.liquid: {len(schemas)}')
for s in schemas:
    print(s[:300])
