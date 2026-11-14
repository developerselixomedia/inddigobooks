import pandas as pd
import re
import json

df = pd.read_csv('shopify_products_import.csv')

def parse_specs_dict(body_html):
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

print("Total handles:", df['Handle'].nunique())
sample_handles = df['Handle'].unique()[:10]
for h in sample_handles:
    sub = df[df['Handle'] == h]
    first = sub.iloc[0]
    specs = parse_specs_dict(first['Body (HTML)'])
    print(h, "->", first['Title'], "| Author:", specs.get('author'), "| Variants:", len(sub))

