import csv

print("=== shopify_products_import.csv ===")
with open('shopify_products_import.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print("Columns:", headers[:15])
    row_count = sum(1 for _ in reader)
    print(f"Total rows in shopify_products_import.csv: {row_count}")

print("\n=== Updated_Catalog.csv ===")
with open('Updated_Catalog.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    headers2 = next(reader)
    print("Columns:", headers2[:15])
    row_count2 = sum(1 for _ in reader)
    print(f"Total rows in Updated_Catalog.csv: {row_count2}")
