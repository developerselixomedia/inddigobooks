# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
import subprocess
import store_scripts

with open('scratch/test_syntax.js', 'w', encoding='utf-8') as f:
    f.write('const PODIUM_BOOKS = [];\nconst POET_SHAYARI_DATA = {};\nconst VAULT_BOOKS = {};\nconst CATALOG_BOOKS = [];\nconst MODAL_METADATA_DATABASE = {};\n' + store_scripts.UNIFIED_STORE_JS)

res = subprocess.run(['node', '-c', 'scratch/test_syntax.js'], capture_output=True, text=True)
print('Node return code:', res.returncode)
if res.returncode != 0:
    print('Syntax Error Output:\n', res.stderr)
else:
    print('SUCCESS: ZERO SYNTAX ERRORS IN store_scripts.py!')
