with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function getAssetUrl(')
print(text[idx:idx+1800])
