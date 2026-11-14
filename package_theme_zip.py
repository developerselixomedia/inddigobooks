# -*- coding: utf-8 -*-
"""
Package Shopify Theme into indigo-books-theme.zip
"""

import os
import zipfile

THEME_DIRS = [
    'assets',
    'blocks',
    'config',
    'layout',
    'locales',
    'sections',
    'snippets',
    'templates'
]

OUTPUT_ZIP = 'indigo-books-theme.zip'

print(f"Creating {OUTPUT_ZIP}...")

# Count files
total_files = 0
with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
    for folder in THEME_DIRS:
        if not os.path.exists(folder):
            print(f"Warning: {folder} does not exist!")
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                # Store relative path without leading slash
                rel_path = os.path.relpath(file_path, '.')
                zf.write(file_path, rel_path)
                total_files += 1

print(f"Successfully packaged {total_files} files into {OUTPUT_ZIP}!")
file_size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
print(f"Archive size: {file_size_mb:.2f} MB")


