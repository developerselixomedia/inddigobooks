with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// Update cover preview if variant has distinct cover')
if idx != -1:
    print(text[idx-200:idx+600])
