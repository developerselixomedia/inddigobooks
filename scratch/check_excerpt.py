with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('v2-see-full-excerpt')
print("At:", idx)
print(text[idx-150:idx+350])

idx2 = text.find('v2-see-full-excerpt', idx + 1)
print("\nAt:", idx2)
print(text[idx2-150:idx2+350])

