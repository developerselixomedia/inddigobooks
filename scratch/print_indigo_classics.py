with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('By Indigo Classics')
if idx != -1:
    print(text[idx-300:idx+800])
