with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function handleArchiveSearch')
print("handleArchiveSearch at:", idx)
if idx != -1:
    print(text[idx:idx+1500])
