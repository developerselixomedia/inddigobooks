with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('@media', idx)
    if pos == -1:
        break
    print('Media query at:', pos, text[pos:pos+100].replace('\n', ' '))
    idx = pos + 10
