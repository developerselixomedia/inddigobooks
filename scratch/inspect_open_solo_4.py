with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.openSoloBookPage = function')
if idx != -1:
    print(text[idx+9000:idx+13000])
