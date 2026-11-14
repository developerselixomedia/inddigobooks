with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function renderCatalog()')
print(text[pos+6100:pos+7200])

