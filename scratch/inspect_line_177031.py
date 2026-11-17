with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 177031
print(text[idx-300:idx+300])
