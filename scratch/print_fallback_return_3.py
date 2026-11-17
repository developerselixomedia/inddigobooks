with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function getFallbackCoverSvg')
if idx != -1:
    print(text[idx+3500:idx+4000])
