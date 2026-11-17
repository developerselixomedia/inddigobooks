with open('sections/product-information.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Buy Now|buy-now|buy_now', text, re.IGNORECASE)]
for m in matches:
    print('product-information.liquid at', m, ':', text[max(0, m-50):min(len(text), m+150)])
