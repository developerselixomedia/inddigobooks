with open('store_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
urls = re.findall(r'"image":\s*"([^"]+)"', text)
print('Total book image entries in store_data.py:', len(urls))
domains = {}
for u in urls:
    d = u.split('/')[2] if u.startswith('http') else 'local'
    domains[d] = domains.get(d, 0) + 1
for d, count in sorted(domains.items(), key=lambda x: x[1], reverse=True):
    print(f'{d}: {count}')
