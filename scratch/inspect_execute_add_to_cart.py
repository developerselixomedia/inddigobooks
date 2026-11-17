with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function executeAddToCart(')
print(text[idx+1400:idx+3000])
