with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print('Last 30 lines:')
for line in lines[-30:]:
    print(line)

