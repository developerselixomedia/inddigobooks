with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function renderCatalog()')
print(text[pos+3200:pos+5000])

