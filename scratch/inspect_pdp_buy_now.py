with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function pdpBuyNow()')
print(text[idx-500:idx+1000])
