with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<header class="site-navbar')
print(text[idx:idx+2500])
