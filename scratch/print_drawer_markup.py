with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="v2MobileDrawer"')
print(text[idx-100:idx+3500])
