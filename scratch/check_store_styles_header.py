with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['brand-logo-img', 'v2-nav-brand-group', 'v2-hamburger-btn', 'Reading Bag (0)', 'editorial-header-actions']:
    idx = text.find(term)
    print(term, 'in store_styles.py:', idx)
    if idx != -1:
        print(text[idx-50:idx+200])
        print('='*50)
