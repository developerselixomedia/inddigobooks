with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const pool = getUnifiedSearchPool();')
print(text[idx:idx+2000])
