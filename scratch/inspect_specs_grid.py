with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="v2-solo-specs-grid"')
print(text[idx:idx+1500])
