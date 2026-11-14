with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
comments = re.findall(r'<!--\s*={5,}\s*([\d\w\s.:&#;()\-]+?)\s*={5,}\s*-->', text)
print('Section comments in preview.html:')
for c in comments:
    print('  ', c.strip().replace('\n', ' '))

