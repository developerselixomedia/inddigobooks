with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('btn-reading-bag')
if idx != -1:
    print(text[idx-400:idx+800])
