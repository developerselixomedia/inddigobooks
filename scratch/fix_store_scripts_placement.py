# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

# The JS block was added after """ at line 2276
q_idx = text.rfind('"""')
# Find where the JS code starts after """
js_after = text[q_idx+3:].strip()

# Now strip everything after """ from text
main_code = text[:q_idx].rstrip()

# Find window.closeDedicatedProductPage in main_code
w_idx = main_code.rfind('window.closeDedicatedProductPage = closeDedicatedProductPage;')
if w_idx != -1:
    end_of_func = main_code.rfind('}', w_idx)
    # Insert js_after BEFORE end_of_func
    # But wait, the new functions should be at top level inside UNIFIED_STORE_JS, not inside an inner function
    # Let's see what is right before `// --- GLOBAL EXPORTS / WINDOW MOUNT ---` or before `function initIndigoStore()`
    init_idx = main_code.rfind('function initIndigoStore()')
    if init_idx != -1:
        updated = main_code[:init_idx] + "\n" + js_after + "\n\n" + main_code[init_idx:] + '\n"""\n'
    else:
        updated = main_code + "\n" + js_after + '\n"""\n'
else:
    updated = main_code + "\n" + js_after + '\n"""\n'

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(updated)

print("store_scripts.py placement fixed successfully!")

