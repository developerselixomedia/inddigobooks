with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('expressPhoneCheckoutForm')
print(repr(text[idx:idx+800]))
