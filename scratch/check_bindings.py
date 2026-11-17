import openpyxl
import re

print("Loading Updated_Catalog.xlsx...")
wb = openpyxl.load_workbook('Updated_Catalog.xlsx', read_only=True)
sheet = wb.active
rows = list(sheet.iter_rows(values_only=True))

isbn_to_binding = {}
isbn_to_mrp = {}
title_to_editions = {}

for r in rows[1:]:
    isbn = str(r[2] or '').strip()
    title = str(r[3] or '').strip()
    author = str(r[4] or '').strip()
    binding = str(r[5] or '').strip()
    mrp = r[9]
    if isbn:
        isbn_to_binding[isbn] = binding
        isbn_to_mrp[isbn] = mrp
    if title:
        key = title.lower()
        if key not in title_to_editions:
            title_to_editions[key] = []
        title_to_editions[key].append({
            'isbn': isbn,
            'title': title,
            'author': author,
            'binding': binding,
            'mrp': mrp
        })

print(f"Total ISBNs in Excel: {len(isbn_to_binding)}")
print(f"Total Unique Titles in Excel: {len(title_to_editions)}")

# Find titles that have both Paperback and Hardcover
dual_format_titles = []
single_format_titles = []

for title, eds in title_to_editions.items():
    bindings = set(e['binding'].lower() for e in eds)
    has_pb = any('paper' in b for b in bindings)
    has_hc = any('hard' in b for b in bindings)
    if has_pb and has_hc:
        dual_format_titles.append((title, eds))
    else:
        single_format_titles.append((title, eds))

print(f"Titles with BOTH Paperback & Hardcover: {len(dual_format_titles)}")
print(f"Titles with ONLY ONE format: {len(single_format_titles)}")

print("\nExamples of DUAL format titles:")
for t, eds in dual_format_titles[:5]:
    print(f"  Title: {eds[0]['title']}")
    for e in eds:
        print(f"    - ISBN: {e['isbn']}, Binding: {e['binding']}, MRP: {e['mrp']}")

print("\nExamples of SINGLE format titles:")
for t, eds in single_format_titles[:5]:
    print(f"  Title: {eds[0]['title']}")
    for e in eds:
        print(f"    - ISBN: {e['isbn']}, Binding: {e['binding']}, MRP: {e['mrp']}")
