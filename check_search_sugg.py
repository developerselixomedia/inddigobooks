with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function renderSearchSuggestions(')
print(text[pos:pos+1500])

