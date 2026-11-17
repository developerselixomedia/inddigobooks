with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('>IB<')
if idx != -1:
    print(text[idx-400:idx+600])
