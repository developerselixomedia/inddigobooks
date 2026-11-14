# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the helper block
marker = '// --- GLOBAL NAVIGATION & AUTHOR FILTER HELPERS ---'
if marker in text:
    helper_code = text[text.find(marker):].strip()
    # Remove helper_code from the end
    text = text[:text.find(marker)].strip()
    # Find the closing """ of UNIFIED_STORE_JS
    last_quote = text.rfind('"""')
    if last_quote != -1:
        # Insert helper_code before the closing quote
        text = text[:last_quote] + '\n\n' + helper_code + '\n"""\n'

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed store_scripts.py: helper functions moved inside UNIFIED_STORE_JS")

