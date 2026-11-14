with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(715, min(len(lines), 850)):
    l = lines[i]
    if "b['" in l or "HINDI_FEATURE_BOOK['" in l:
        print(f"{i+1}: {l.strip()}")

