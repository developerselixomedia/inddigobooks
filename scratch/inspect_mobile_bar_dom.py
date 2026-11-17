with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('v2-solo-mobile-buy-bar')
print('Before mobile buy bar:')
print(text[idx-400:idx])
print('After mobile buy bar:')
print(text[idx:idx+700])
