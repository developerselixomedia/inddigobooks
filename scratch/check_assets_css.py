with open('assets/main-store.css', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['brand-logo-img', 'v2-nav-brand-group', 'v2-hamburger-btn', 'editorial-header-actions']:
    idx = text.find(term)
    print(term, 'in assets/main-store.css:', idx)
