with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderArchiveCard(')
if idx == -1: idx = text.find('renderArchiveGrid')
print(text[idx:idx+2000])
