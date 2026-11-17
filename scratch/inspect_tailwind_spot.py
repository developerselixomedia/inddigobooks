with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<!-- Tailwind CSS Engine -->')
print(text[idx-200:idx+600])
