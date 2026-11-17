with open('indigo-books-shopify-theme/sections/main-store.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

print("main-store.liquid length:", len(text))
for term in ['editorial-scatter-hero', 'v2-mobile-hero', 'scatter-book-cover']:
    idx = text.find(term)
    print(term, 'in main-store.liquid:', idx)
