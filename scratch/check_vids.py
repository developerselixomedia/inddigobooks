import re

with open('prepare_master_blocks.py', 'r', encoding='utf-8') as f:
    text = f.read()

vids = set(re.findall(r'variant_?id[\'\":\s]+(\d+)', text, re.IGNORECASE))
print('Variant IDs in prepare_master_blocks.py:', vids)
