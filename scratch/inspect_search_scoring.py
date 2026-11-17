with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('pool.forEach(function(b) {')
print(text[idx:idx+1500])
