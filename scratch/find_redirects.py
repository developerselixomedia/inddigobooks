import re

for filename in ['store_scripts.py', 'editorial_video_theme.py', 'sections/main-product.liquid', 'layout/theme.liquid']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = [m.start() for m in re.finditer(r'(location\.href|location\.replace|\.submit\(\))', text)]
    print(f'=== {filename}: {len(matches)} matches ===')
    for m in matches:
        print(text[max(0, m-40):min(len(text), m+80)].replace('\n', ' '))
