with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="v2SoloAuthor"')
if idx != -1:
    print(text[idx-200:idx+600])
