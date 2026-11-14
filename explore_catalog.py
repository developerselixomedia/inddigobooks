import csv

with open('Updated_Catalog.csv', 'r', encoding='latin1') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

def get_qty(r):
    try:
        return int(r['QTY'])
    except:
        return 0

sorted_by_qty = sorted(rows, key=get_qty, reverse=True)
print('Top 20 Books by In-Stock Quantity:')
for r in sorted_by_qty[:20]:
    title = r['Title']
    author = r['Author']
    binding = r['Binding']
    mrp = r['MRP']
    qty = r['QTY']
    subj = r['Subject']
    pub = r['Publisher']
    img = r['Primary Image']
    print(f"  - '{title}' by {author} ({binding}) | MRP: INR {mrp} | QTY: {qty} | {subj} | {pub}")

