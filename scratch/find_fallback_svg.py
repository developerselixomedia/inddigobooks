with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('getFallbackCoverSvg')
while idx != -1:
    print('Found getFallbackCoverSvg at:', idx)
    print(text[idx:idx+600])
    print('='*50)
    idx = text.find('getFallbackCoverSvg', idx+1)
