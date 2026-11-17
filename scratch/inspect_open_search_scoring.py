with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 5. Query Unified Store Pool & Score Matches')
print(text[idx:idx+2500])
