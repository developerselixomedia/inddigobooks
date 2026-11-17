with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('See full excerpt')
print("In sections/main-product.liquid at:", idx)
if idx != -1:
    print(text[max(0, idx-200):idx+300])

