with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.closeSoloBookPage = function(')
if idx == -1:
    idx = text.find('closeSoloBookPage')
print(text[idx:idx+1000])
