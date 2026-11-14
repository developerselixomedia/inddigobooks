
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('sync_preview_to_shopify.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[40:150], 41):
    print(f'{i:3d}: {line}', end='')
