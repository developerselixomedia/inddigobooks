with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('currentSearchResultsList =')
print(text[idx-200:idx+800])
