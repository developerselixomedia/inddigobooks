with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('openSoloBookPage')
while idx != -1:
    print('Found at:', idx)
    print(text[max(0, idx-20):idx+150])
    print('='*40)
    idx = text.find('openSoloBookPage', idx+1)
