with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('archiveSearchQuery')
print("archiveSearchQuery at:", idx)
if idx != -1:
    print(text[idx-50:idx+1500])
