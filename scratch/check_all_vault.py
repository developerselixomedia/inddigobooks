# -*- coding: utf-8 -*-
import sys, os, csv
sys.path.insert(0, os.path.abspath('.'))
import store_data

books_to_find = []
for cat, blist in store_data.VAULT_BOOKS.items():
    for b in blist:
        books_to_find.append((cat, b['id'], b['title'], b.get('isbn', '')))

with open('Updated_Catalog.csv', 'r', encoding='utf-8', errors='ignore') as f:
    rows = list(csv.DictReader(f))

results = {}
for cat, bid, title, isbn in books_to_find:
    found = None
    if isbn:
        for r in rows:
            if r.get('ISBN') == isbn:
                found = r
                break
    if not found:
        t_low = title.lower().strip()
        for r in rows:
            if t_low in r.get('Title', '').lower():
                found = r
                break
    if found:
        img = found.get('Primary Image') or found.get('Image_1')
        print(f"{cat} | {bid} | {title} => {img}")
        results[bid] = img
    else:
        print(f"NOT FOUND: {cat} | {bid} | {title}")
