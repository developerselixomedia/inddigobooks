with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.v2-drawer-')
print('Found .v2-drawer- at:', idx)
if idx != -1:
    print(text[idx:idx+500])
