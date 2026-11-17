import glob
import re

for pattern in ['sections/**/*.liquid', 'snippets/**/*.liquid', 'blocks/**/*.liquid']:
    for f in glob.glob(pattern, recursive=True):
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        if 'Buy Now' in content or 'buy_now' in content or 'buy-now' in content:
            print(f'{f}: matches')
