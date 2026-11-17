with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderCurrentSearchResults')
if idx != -1:
    print(text[idx+2600:idx+3500])
