with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.editorial-search-results')
print(text[idx-50:idx+800])
