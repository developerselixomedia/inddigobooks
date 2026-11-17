with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['Reading Bag', '1-Click Order', '1-Click', 'reading-bag']:
    idx = text.find(term)
    print(term, 'in store_styles.py:', idx)
    if idx != -1:
        print(text[idx-50:idx+200])
