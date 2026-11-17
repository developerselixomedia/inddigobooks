with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderArchiveGrid')
print(text[idx+7000:idx+9500])
