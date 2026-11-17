with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'hero-kuchh-ishq'
idx = text.find(target)
if idx != -1:
    print(text[idx:idx+4000])
