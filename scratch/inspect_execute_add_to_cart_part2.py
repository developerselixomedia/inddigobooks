with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('if (!meta) {\n    console.warn("Indigo Books: Could not resolve book for add-to-cart:", bookId);')
print(text[idx:idx+2500])
