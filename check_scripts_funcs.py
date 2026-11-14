with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
funcs = [
    'switchCategoryBento',
    'renderCatalog',
    'renderSearchSuggestions',
    'handleHeroBookHover',
    'openOverviewModal',
    'closeOverviewModal',
    'addToCart',
    'updateCartUI',
    'toggleCartDrawer'
]

for fn in funcs:
    pos = text.find(f'function {fn}')
    print(f"{fn:25}: {'FOUND' if pos != -1 else 'MISSING'}")

