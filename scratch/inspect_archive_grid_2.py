with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderArchiveGrid')
if idx != -1:
    print(text[idx+2500:idx+6500])
