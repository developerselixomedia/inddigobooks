with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['site-navbar', 'editorial-scatter-hero', 'scatter-book', 'v2-mobile-hero']:
    idx = text.find(term)
    print(term, 'in store_styles.py:', idx)
    if idx != -1:
        print(text[idx-50:idx+200].replace('\n', ' '))
        print('='*50)
