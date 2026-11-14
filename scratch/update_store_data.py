# -*- coding: utf-8 -*-
"""
scratch/update_store_data.py
Updates VAULT_BOOKS covers and reorders CATALOG_BOOKS so top bestsellers appear first.
"""

import store_data
import re

# Read store_data.py
with open("store_data.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace duplicate covers in VAULT_BOOKS
replacements = [
    # Law
    ('vault-law-ucc', 'assets/book-highcourt.jpg', 'assets/book-bench-bar.jpg'),
    ('vault-law-judiciary', 'assets/book-samvidhan.jpg', 'assets/book-10-faisle.jpg'),
    # Sahitya
    ('vault-sah-shilp', 'assets/book-gyan-aur-karm.jpg', 'assets/book-hindi-vyakaran.jpg'),
    ('vault-sah-itihas', 'assets/book-gyan-aur-karm.jpg', 'assets/book-hindi-sahitya-itihas.jpg'),
    ('vault-sah-anusandhan', 'assets/book-gyan-aur-karm.jpg', 'assets/book-hindi-bhasha.jpg'),
    # Civil
    ('vault-civ-badalata', 'assets/book-hadappa.jpg', 'assets/book-gyandan.jpg'),
    ('vault-civ-nyay', 'assets/book-hadappa.jpg', 'assets/book-halant.jpg'),
    ('vault-civ-soochana', 'assets/book-hadappa.jpg', 'assets/book-halyog.jpg'),
    # History
    ('vault-his-azad', 'assets/book-savarkar.jpg', 'assets/book-cheelwali-kothi.jpg')
]

for book_id, old_cover, new_cover in replacements:
    # Find block with book_id
    idx = text.find(f'"{book_id}"')
    if idx != -1:
        end_idx = text.find('}', idx)
        block = text[idx:end_idx]
        if old_cover in block:
            new_block = block.replace(old_cover, new_cover)
            text = text[:idx] + new_block + text[end_idx:]
            print(f"Updated {book_id} cover to {new_cover}")
        else:
            print(f"Warning: {old_cover} not found in {book_id}")
    else:
        print(f"Warning: {book_id} not found in store_data.py")

# Now reorder CATALOG_BOOKS: Top bestsellers first!
# Currently CATALOG_BOOKS has 24 books. Books 12 to 23 are the top bestsellers:
# Godan, Raag Darbari, Chitralekha, Rashmirathi, Kuchh Ishq, Tarkash, Aadha Gaon, Mahabhoj, Shekhar, Savarkar, Samvidhan, High Court!
# Let's reorder them so books 12-23 come FIRST, followed by books 0-11!
cat_start = text.find("CATALOG_BOOKS = [")
if cat_start != -1:
    # Find the end of CATALOG_BOOKS list
    # Use store_data's existing list
    all_books = list(store_data.CATALOG_BOOKS)
    # Split: bestsellers (indices 12 to 24), rest (indices 0 to 12)
    bestsellers = all_books[12:]
    rest = all_books[:12]
    reordered_books = bestsellers + rest
    
    import json
    # Format nicely
    formatted_json = json.dumps(reordered_books, ensure_ascii=False, indent=2)
    # Find closing bracket of CATALOG_BOOKS
    # Find end of CATALOG_BOOKS
    cat_end = text.find("\n]\n", cat_start)
    if cat_end == -1:
        cat_end = text.find("\n]", cat_start)
    
    if cat_end != -1:
        text = text[:cat_start] + "CATALOG_BOOKS = " + formatted_json + text[cat_end+2:]
        print("Successfully reordered CATALOG_BOOKS: Top bestsellers are now at indices 0-11!")

with open("store_data.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved store_data.py successfully!")

