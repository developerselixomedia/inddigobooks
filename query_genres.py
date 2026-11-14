import csv

with open('Updated_Catalog.csv', 'r', encoding='latin1') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

def find_by_subj(keyword, limit=5):
    matches = []
    for r in rows:
        if keyword.lower() in r['Subject'].lower() or keyword.lower() in r['Title'].lower():
            if r['Primary Image'].strip().startswith('http') and int(r.get('QTY', 0) or 0) > 0:
                matches.append(r)
    return matches[:limit]

print("=== POETRY / SHAYARI ===")
for r in find_by_subj('Poetry', 6):
    print(f"{r['Title']} | {r['Author']} | {r['Publisher']} | MRP: {r['MRP']} | ISBN: {r['ISBN']}")

print("\n=== HISTORY / LAW / CRITICISM ===")
for r in find_by_subj('History', 6):
    print(f"{r['Title']} | {r['Author']} | {r['Publisher']} | MRP: {r['MRP']} | ISBN: {r['ISBN']}")

print("\n=== FICTION / NOVEL ===")
for r in find_by_subj('Fiction : Novel', 6):
    print(f"{r['Title']} | {r['Author']} | {r['Publisher']} | MRP: {r['MRP']} | ISBN: {r['ISBN']}")

print("\n=== SATIRE / STORIES ===")
for r in find_by_subj('Stories', 6):
    print(f"{r['Title']} | {r['Author']} | {r['Publisher']} | MRP: {r['MRP']} | ISBN: {r['ISBN']}")

