with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('#indigo-solo-product-view', idx)
    if pos == -1:
        break
    print(f"preview.html at {pos}:")
    print(text[pos:pos+300].replace('\n', ' '))
    print('-'*50)
    idx = pos + 25
