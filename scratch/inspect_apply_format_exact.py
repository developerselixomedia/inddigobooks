with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function applyFormat(fmt)')
print(text[idx-50:idx+1200])
