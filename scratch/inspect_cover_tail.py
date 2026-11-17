with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('coverImg.src = found.cover;')
if idx != -1:
    print(text[idx:idx+1500])
