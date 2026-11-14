# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '"""\n\n  /* ========================================================================='
if marker in text:
    parts = text.split(marker)
    before = parts[0]
    after = '  /* =========================================================================' + parts[1]
    after = after.replace('"""', '').strip()
    new_text = before + '\n\n' + after + '\n"""\n'
    with open('store_styles.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed store_styles.py syntax!")
else:
    print("Marker not found, inspecting last 30 lines:")
    lines = text.splitlines()
    for l in lines[-25:]:
        print(l)

