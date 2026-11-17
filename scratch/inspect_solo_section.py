with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('@media (max-width: 900px) {\n    header.site-navbar')
print(text[idx:idx+600])
