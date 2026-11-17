with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("querySelectorAll('.scatter-book-cover')")
if idx != -1:
    print(text[idx-200:idx+1200])
