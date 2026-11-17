with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderArchiveGrid')
print(text[idx+9500:idx+12000])
