import csv, json

with open('Updated_Catalog.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    csv_rows = list(reader)

print(f"Total rows in Updated_Catalog.csv: {len(csv_rows)}")
sample = csv_rows[0]
print("Sample row:")
for k, v in sample.items():
    print(f"  {k}: {v}")
