with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderShelfRow')
print(text[idx+1300:idx+2500])
