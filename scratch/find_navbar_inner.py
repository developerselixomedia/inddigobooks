with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('.navbar-inner', idx)
    if pos == -1:
        break
    print(f"store_styles.py at {pos}:")
    print(text[max(0, pos-40):pos+140].replace('\n', ' '))
    print('-'*50)
    idx = pos + 14
