with open('indigo-books-shopify-theme/layout/theme.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('viewport')
print('viewport in theme.liquid:', idx)
if idx != -1:
    print(text[idx-50:idx+150])
else:
    print("NO VIEWPORT META TAG FOUND IN theme.liquid!")
