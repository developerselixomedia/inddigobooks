with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('isIndianCatalogBook')
print(text[idx:idx+1200])
