with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('rajkamalprakashan.com', idx)
    if pos == -1:
        break
    print('store_scripts.py occurrence at:', pos)
    print(text[max(0, pos-80):pos+120])
    print('='*50)
    idx = pos + 22
