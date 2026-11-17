with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('No books found matching your query')
print(text[max(0, idx-2500):idx])
