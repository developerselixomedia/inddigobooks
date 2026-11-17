with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function openExpressPhoneCheckout(bookId, qty)')
print(text[idx:idx+3500])
