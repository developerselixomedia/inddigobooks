with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.editorial-header-actions')
while idx != -1:
    print('Found .editorial-header-actions at:', idx)
    print(text[idx-50:idx+300].replace('\n', ' '))
    print('='*50)
    idx = text.find('.editorial-header-actions', idx+1)
