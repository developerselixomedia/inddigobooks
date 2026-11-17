with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('editorial-header-actions', idx)
    if pos == -1:
        break
    print(f"editorial_video_theme.py at {pos}:")
    print(text[max(0, pos-60):pos+250].replace('\n', ' '))
    print('='*50)
    idx = pos + 24
