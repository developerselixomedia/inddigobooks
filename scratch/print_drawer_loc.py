with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.v2-mobile-drawer {')
print(text[idx-100:idx+1200])
