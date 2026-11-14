# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.abspath('.'))

vault_updates = {
    # law
    'vault-law-highcourt': ('assets/book-highcourt.jpg', '9788197989667'),
    'vault-law-constitution': ('assets/book-samvidhan.jpg', '9789390971480'),
    'vault-law-ucc': ('assets/book-sanhita.jpg', '9789389742299'),
    'vault-law-judiciary': ('assets/book-kasauti.jpg', '9788119835416'),
    # sahitya
    'vault-sah-gyan': ('assets/book-gyan-aur-karm.jpg', '9788126725359'),
    'vault-sah-shilp': ('assets/book-shilp-vidhi.jpg', '9788126715015'),
    'vault-sah-itihas': ('assets/book-hindi-sahitya-itihas.jpg', '9789389742220'),
    'vault-sah-anusandhan': ('assets/book-anusandhan.jpg', '9788126729579'),
    # civil
    'vault-civ-hadappa': ('assets/book-hadappa.jpg', '9788126715367'),
    'vault-civ-badalata': ('assets/book-badalata-desh.jpg', '9788126727285'),
    'vault-civ-nyay': ('assets/book-nyay-sangharsh.jpg', '9788126727407'),
    'vault-civ-soochana': ('assets/book-soochana.jpg', '9788126725342'),
    # history
    'vault-his-savarkar': ('assets/book-savarkar.jpg', '9789389742282'),
    'vault-his-haashiye': ('assets/book-haashiye.jpg', '9788126728077'),
    'vault-his-azad': ('assets/book-azad.jpg', '9788126728619'),
    'vault-his-haadse': ('assets/book-haadse.jpg', '9788126727292'),
}

with open('store_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Update VAULT_BOOKS entries
for bid, (cover_path, isbn) in vault_updates.items():
    pat = rf'("id":\s*"{bid}"[\s\S]*?"coverUrl":\s*")[^"]*(")'
    text = re.sub(pat, rf'\g<1>{cover_path}\g<2>', text)
    pat_c = rf'("id":\s*"{bid}"[\s\S]*?"cover":\s*")[^"]*(")'
    text = re.sub(pat_c, rf'\g<1>{cover_path}\g<2>', text)

with open('store_data.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated VAULT_BOOKS in store_data.py!")
