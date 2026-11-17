with open('assets/theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 7042
print(text[idx-400:idx+400])
