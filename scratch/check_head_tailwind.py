with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('cdn.tailwindcss.com')
print(text[max(0, idx-400):idx+300])
