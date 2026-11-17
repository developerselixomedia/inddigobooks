with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="cart-drawer-footer"')
if idx == -1: idx = text.find('cart-drawer-footer')
print(text[idx:idx+2500])
