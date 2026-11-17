with open('store_modals_and_search.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Mobile Number (for Courier Tracking')
if idx != -1:
    print(text[idx-200:idx+800])
