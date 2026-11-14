import pandas as pd
import re

df = pd.read_csv('shopify_products_import.csv')
handles_to_test = [
    'godan-premchand',
    'raag-darbari-shrilal-shukla',
    'chitralekha-bhagwaticharan-verma',
    'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
    'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
    'tarkash-javed-akhtar',
    'gypsy-ila-chandra-joshi',
    'aacharya-ramchandra-shukla-aur-hindi-aalochana-ramvilas-sharma'
]

for h in handles_to_test:
    sub = df[df['Handle'] == h]
    print(f"=== Handle: {h} (rows: {len(sub)}) ===")
    first_row = sub.iloc[0]
    print("Title:", first_row['Title'])
    print("Vendor:", first_row['Vendor'])
    print("Type:", first_row['Type'])
    body = str(first_row['Body (HTML)'])
    print("Body snippet:", body[:300] if len(body) > 300 else body)
    
    # check variants
    for idx, r in sub.iterrows():
        print(f"  Variant: opt1={r['Option1 Value']}, sku={r['Variant SKU']}, price={r['Variant Price']}, grams={r['Variant Grams']}, qty={r['Variant Inventory Qty']}, img={r['Image Src']}")

