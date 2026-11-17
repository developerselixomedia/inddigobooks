with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('@media', idx)
    if pos == -1:
        break
    snippet = text[pos:pos+150].replace('\n', ' ')
    if 'header' in snippet.lower() or 'nav' in snippet.lower():
        print(f"store_styles.py at {pos}: {snippet}")
    idx = pos + 7
