# -*- coding: utf-8 -*-
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '        MASTER_STYLE + "\\n\\n" + MASTER_SCRIPT + "\\n\\n",\n'
if target in text:
    text = text.replace(target, '')
    with open('sync_preview_to_shopify.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully removed duplicated MASTER_STYLE/SCRIPT from main-store.liquid")
else:
    print("Target not found in sync_preview_to_shopify.py")

