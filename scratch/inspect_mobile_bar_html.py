with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<div class="v2-solo-mobile-buy-bar">')
print('Before:')
print(text[idx-500:idx])
print('After:')
print(text[idx:idx+800])
