import glob

for fname in ['editorial_video_theme.py', 'store_styles.py', 'build_html_generator.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = 0
    while True:
        pos = text.find('60px', idx)
        if pos == -1:
            break
        snippet = text[max(0, pos-40):pos+60].replace('\n', ' ')
        if 'solo' in snippet.lower() or 'top' in snippet.lower() or 'height' in snippet.lower():
            print(f"{fname} at {pos}: {snippet}")
        idx = pos + 10
