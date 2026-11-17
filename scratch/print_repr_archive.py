with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('var fallbackSvg = getFallbackCoverSvg')
if idx != -1:
    print(repr(text[idx:idx+700]))
