with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function executeFullSearch')
if idx == -1:
    idx = text.find('window.executeFullSearch =')
print("executeFullSearch at:", idx)
if idx != -1:
    print(text[idx-50:idx+1500])
