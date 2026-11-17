with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// Format Selection Handlers (Paperback vs Hardcover Deluxe)')
if idx != -1:
    print(text[idx+1400:idx+2500])
