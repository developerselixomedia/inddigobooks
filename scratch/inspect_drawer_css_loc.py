with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/* 2. Slide-out Mobile Navigation Drawer */')
print(text[idx:idx+1200])
