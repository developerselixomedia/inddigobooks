with open('indigo-books-shopify-theme/layout/theme.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

print("theme.liquid length:", len(text))
for term in ['main-store.css', 'theme.css', 'editorial-scatter-hero', 'v2-mobile-hero']:
    idx = text.find(term)
    print(term, 'in theme.liquid:', idx)
