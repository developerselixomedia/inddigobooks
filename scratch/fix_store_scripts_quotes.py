with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('"""')
if idx != -1:
    before = text[:idx]
    after = text[idx+3:].strip()
    new_text = before + "\n" + after + '\n"""\n'
    with open('store_scripts.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed store_scripts.py triple quotes!")
