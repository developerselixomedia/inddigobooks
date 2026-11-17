with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count('function renderCurrentSearchResults')
print("Count of 'function renderCurrentSearchResults' in preview.html:", count)
idx = 0
while True:
    pos = text.find('function renderCurrentSearchResults', idx)
    if pos == -1: break
    print(f"Found at {pos}:")
    print(text[pos+1800:pos+2200])
    print('='*50)
    idx = pos + 30
