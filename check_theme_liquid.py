with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re

for line_num, line in enumerate(lines, 1):
    # Check for liquid tags
    for tag in re.finditer(r'{%\s*(.*?)\s*%}', line):
        t_content = tag.group(1).strip()
        # Ensure it has a valid liquid keyword
        first_word = t_content.split()[0] if t_content.split() else ''
        valid_keywords = ['if', 'else', 'elsif', 'endif', 'for', 'endfor', 'unless', 'endunless', 'case', 'when', 'endcase', 'assign', 'capture', 'endcapture', 'include', 'render', 'section', 'sections', 'form', 'endform', 'paginate', 'endpaginate', 'raw', 'endraw', 'comment', 'endcomment', 'javascript', 'endjavascript', 'stylesheet', 'endstylesheet', 'schema', 'endschema']
        if first_word not in valid_keywords:
            print(f"INVALID LIQUID TAG at line {line_num}: {{% {t_content} %}}")
    for var in re.finditer(r'{{\s*(.*?)\s*}}', line):
        v_content = var.group(1).strip()
        if not v_content:
            print(f"EMPTY LIQUID VAR at line {line_num}: {{{{ }}}}")

print("Tag syntax scan finished.")
