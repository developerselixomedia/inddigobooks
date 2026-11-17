with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
found = 0
while True:
    pos = text.find('src="https://images.rajkamalprakashan.com', idx)
    if pos == -1:
        break
    found += 1
    if found <= 5:
        print('preview.html occurrence at:', pos)
        print(text[max(0, pos-40):pos+120])
        print('='*50)
    idx = pos + 40
print('Total <img src="https://images.rajkamalprakashan.com in preview.html:', found)
