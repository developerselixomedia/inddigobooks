for fname in ['editorial_video_theme.py', 'store_styles.py', 'build_html_generator.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = 0
    while True:
        pos = text.find('#indigo-solo-product-view', idx)
        if pos == -1:
            break
        print(f"{fname} at {pos}:")
        print(text[pos:pos+250].replace('\n', ' '))
        print('-'*50)
        idx = pos + 25
