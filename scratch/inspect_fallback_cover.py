with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function getFallbackCover')
if idx != -1:
    print(text[idx:idx+2500])
