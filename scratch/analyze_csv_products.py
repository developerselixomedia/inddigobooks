import csv

count = 0
products = {}
with open('shopify_products_import.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        handle = row.get('Handle', '').strip()
        title = row.get('Title', '').strip()
        variant_sku = row.get('Variant SKU', '').strip()
        variant_price = row.get('Variant Price', '').strip()
        variant_option = row.get('Option1 Value', '').strip()
        if handle:
            if handle not in products:
                products[handle] = {
                    'title': title,
                    'variants': []
                }
            if variant_price:
                products[handle]['variants'].append({
                    'option': variant_option,
                    'price': variant_price,
                    'sku': variant_sku
                })

print(f"Total unique product handles in CSV: {len(products)}")
# Check top books
for test_h in ['raag-darbari-shrilal-shukla', 'godan-premchand', 'tarkash-javed-akhtar', 'chitralekha-bhagwaticharan-verma', 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap']:
    p = products.get(test_h)
    if p:
        print(f"FOUND in CSV: {test_h} -> Title: {p['title']}, Variants: {p['variants']}")
    else:
        print(f"NOT found in CSV: {test_h}")
