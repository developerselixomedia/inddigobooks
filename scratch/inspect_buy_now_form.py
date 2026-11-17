with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="v2-btn-buy-now"')
print('=== OCCURRENCE 1 ===')
print(text[idx-300:idx+300])

idx2 = text.find('class="v2-btn-buy-now"', idx+1)
print('=== OCCURRENCE 2 ===')
print(text[idx2-300:idx2+300])
