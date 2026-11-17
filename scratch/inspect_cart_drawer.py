with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="cartDrawer"')
if idx == -1: idx = text.find('cart-drawer')
print(text[idx:idx+3000])
