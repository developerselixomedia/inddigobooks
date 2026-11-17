with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('cdn.tailwindcss.com')
if idx != -1:
    print(text[idx-200:idx+300])
