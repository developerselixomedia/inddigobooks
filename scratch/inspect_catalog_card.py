with open('store_scripts.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'class="catalog-card"' in l:
        for j in range(max(0, i-3), min(len(lines), i+30)):
            print(f"{j+1}: {lines[j]}", end='')
        break

