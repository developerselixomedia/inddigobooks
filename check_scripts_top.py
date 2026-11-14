with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of store_scripts.py:', len(text))
for line in text.splitlines()[:25]:
    print(line)

