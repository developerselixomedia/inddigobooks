with open('indigo-books-shopify-theme/assets/main-store.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 263819
print(text[idx-1000:idx-300])
