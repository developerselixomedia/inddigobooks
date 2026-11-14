with open('scratch/build_comprehensive_store_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Insert reading of POET_SHAYARI_DATA
replacement = """
with open('scratch/poet_data_extracted.py', 'r', encoding='utf-8') as pf:
    poet_block = pf.read().strip()

out_lines = [
    '# -*- coding: utf-8 -*-',
    '\"\"\"',
    'store_data.py - Real CSV Data Engine for Indigo Books India',
    'All data parsed 100% from shopify_products_import.csv (Zero assumed data)',
    '\"\"\"',
    '',
    f"PODIUM_BOOKS = {repr(PODIUM_BOOKS)}",
    '',
    poet_block,
"""

target = """out_lines = [
    '# -*- coding: utf-8 -*-',
    '\"\"\"',
    'store_data.py - Real CSV Data Engine for Indigo Books India',
    'All data parsed 100% from shopify_products_import.csv (Zero assumed data)',
    '\"\"\"',
    '',
    f"PODIUM_BOOKS = {repr(PODIUM_BOOKS)}",
"""

if target in code:
    code = code.replace(target, replacement)
    with open('scratch/build_comprehensive_store_data.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("build_comprehensive_store_data.py updated cleanly!")
else:
    print("Target not found!")

