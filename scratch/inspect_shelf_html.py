with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("card.className = 'v2-shelf-book-card'")
if idx == -1: idx = text.find('v2-shelf-book-card')
idx2 = text.find('v2-shelf-book-card', idx+1)
print(text[idx2-100:idx2+600])
