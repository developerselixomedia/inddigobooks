with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,50}querySelectorAll\([\'\"].scatter-book-cover[\'\"].{0,300}', text)
for m in matches:
    print(m)
