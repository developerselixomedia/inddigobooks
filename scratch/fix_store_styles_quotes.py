# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove line 4010/4011's """
cleaned_lines = []
for i, line in enumerate(lines):
    if i in (4009, 4010, 4011) and line.strip() == '"""':
        print(f"Removed premature closing quotes at line {i+1}")
        continue
    cleaned_lines.append(line)

content = "".join(cleaned_lines)
if not content.rstrip().endswith('"""'):
    content = content.rstrip() + '\n"""\n'
    print("Added closing quotes at end of store_styles.py")

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved fixed store_styles.py!")

