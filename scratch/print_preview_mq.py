with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('#editorial-scatter-hero .scatter-book-cover {')
if idx != -1:
    print(text[idx-400:idx+400])
