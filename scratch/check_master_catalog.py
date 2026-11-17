with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for Jaag Piyari in preview.html
matches = re.findall(r'\{[^{}]*Jaag Piyari[^{}]*\}', text)
print(f'Matches for Jaag Piyari in preview.html: {len(matches)}')
for m in matches:
    print(' ', m[:150])
