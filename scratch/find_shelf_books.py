import pandas as pd
import re

df = pd.read_csv('shopify_products_import.csv')

def parse_specs(body_html):
    if not isinstance(body_html, str):
        return {}
    specs = {}
    patterns = {
        'title': r'<strong>Title:</strong>\s*([^<]+)',
        'author': r'<strong>Author:</strong>\s*([^<]+)',
        'publisher': r'<strong>Publisher:</strong>\s*([^<]+)',
        'language': r'<strong>Language:</strong>\s*([^<]+)',
        'binding': r'<strong>Binding:</strong>\s*([^<]+)',
        'pages': r'<strong>Pages:</strong>\s*([^<]+)',
        'edition': r'<strong>Edition\s*/\s*Year:</strong>\s*([^<]+)',
        'category': r'<strong>Subject\s*/\s*Category:</strong>\s*([^<]+)',
        'isbn': r'<strong>ISBN:</strong>\s*([^<]+)'
    }
    for k, p in patterns.items():
        m = re.search(p, body_html, re.IGNORECASE)
        if m:
            specs[k] = m.group(1).strip()
    return specs

target_queries = [
    'godan', 'raag darbari', 'chitralekha', 'gypsy', 'aadha gaon', 'mahabhoj', 'shekhar ek jeevani', '1084', 'gaban',
    'kuchh ishq', 'rashmirathi', 'tarkash', 'mere manch', 'arambh hai', 'tum meri jaan', 'guzare lamhe',
    'aacharya ramchandra shukla', '1857', 'samvidhan', 'high court', 'samaan nagrik', 'nyayapalika'
]

results = {}
for q in target_queries:
    matches = df[df['Title'].fillna('').str.contains(q, case=False) | df['Handle'].fillna('').str.contains(q.replace(' ', '-'), case=False)]
    unique_handles = matches['Handle'].unique()
    print(f"\nQuery '{q}': found {len(unique_handles)} handles")
    for h in unique_handles[:3]:
        sub = df[df['Handle'] == h]
        first = sub.iloc[0]
        specs = parse_specs(first['Body (HTML)'])
        print(f"  Handle: {h} | Title: {first['Title']} | Author: {specs.get('author')} | Vendor: {first['Vendor']}")
        variants = []
        for _, r in sub.iterrows():
            variants.append({
                'format': r['Option1 Value'],
                'sku': r['Variant SKU'],
                'price': r['Variant Price'],
                'grams': r['Variant Grams'],
                'qty': r['Variant Inventory Qty'],
                'img': r['Image Src']
            })
        print(f"    Variants: {variants}")

