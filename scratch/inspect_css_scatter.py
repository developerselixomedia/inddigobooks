with open('indigo-books-shopify-theme/assets/main-store.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('.scatter-book-cover', idx)
    if pos == -1:
        break
    print(f"main-store.css at {pos}:")
    print(text[max(0, pos-40):pos+180].replace('\n', ' '))
    print('-'*50)
    idx = pos + 20
