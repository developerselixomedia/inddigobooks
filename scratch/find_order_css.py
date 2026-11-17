with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('order:', idx)
    if pos == -1:
        break
    print(f"editorial_video_theme.py at {pos}:")
    print(text[max(0, pos-40):pos+120].replace('\n', ' '))
    print('-'*50)
    idx = pos + 7
