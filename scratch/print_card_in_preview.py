with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function renderCurrentSearchResults')
if pos != -1:
    print(text[pos+2600:pos+3500])
