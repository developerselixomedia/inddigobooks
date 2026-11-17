with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('for (var i = 0; i < pool.length; i++)')
print(text[idx:idx+1500])
