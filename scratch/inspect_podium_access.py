with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(620, min(len(lines), 660)):
    print(f"{i+1}: {lines[i]}", end='')

