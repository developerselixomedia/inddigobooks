with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/* Scatter Hero section - Clean Uncluttered Mobile Experience */')
print(text[idx-200:idx+800])
