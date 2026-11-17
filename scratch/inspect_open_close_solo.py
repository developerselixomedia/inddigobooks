with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.closeSoloBookPage = function() {')
print(text[idx:idx+1200])
