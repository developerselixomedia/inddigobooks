with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    idx = text.find('indigo-search-results-view', idx)
    if idx == -1:
        break
    print(f"Match at {idx}:")
    print(text[max(0, idx-50):idx+250])
    print("-" * 50)
    idx += len('indigo-search-results-view')
