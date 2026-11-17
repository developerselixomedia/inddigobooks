with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('editorial-header-actions')
print(text[idx:idx+1500])
