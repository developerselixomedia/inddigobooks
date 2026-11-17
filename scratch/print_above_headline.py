with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('.scatter-headline-center {')
if idx != -1:
    print(text[idx-600:idx])
