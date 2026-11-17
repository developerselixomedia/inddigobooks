with open('scratch/verify_all_fixes_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('TEST GROUP 4')
print(repr(text[idx-50:idx+600]))
