with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('v2-shelf-book-card')
print(text[idx-200:idx+800])
