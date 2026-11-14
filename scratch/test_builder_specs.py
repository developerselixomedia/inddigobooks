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

def get_book_record(handle):
    sub = df[df['Handle'] == handle]
    if sub.empty:
        return None
    first = sub.iloc[0]
    specs = parse_specs_dict(first['Body (HTML)'])
    
    variants = []
    for _, r in sub.iterrows():
        opt1 = str(r['Option1 Value']) if pd.notna(r['Option1 Value']) else 'Paperback'
        sku = str(r['Variant SKU']).replace('.0', '') if pd.notna(r['Variant SKU']) else specs.get('isbn', '')
        price = float(r['Variant Price']) if pd.notna(r['Variant Price']) else 299.0
        grams = int(r['Variant Grams']) if pd.notna(r['Variant Grams']) else 250
        qty = int(r['Variant Inventory Qty']) if pd.notna(r['Variant Inventory Qty']) else 100
        img = str(r['Image Src']) if pd.notna(r['Image Src']) and str(r['Image Src']).startswith('http') else ''
        variants.append({
            'format': opt1,
            'sku': sku,
            'isbn': sku,
            'price': price,
            'grams': grams,
            'qty': qty,
            'img': img
        })
    
    # Sort variants so Paperback is preferred default if available, or first
    p_var = next((v for v in variants if 'paperback' in v['format'].lower()), variants[0])
    
    title = str(first['Title']) if pd.notna(first['Title']) else specs.get('title', handle)
    author = specs.get('author') or 'Celebrated Author'
    publisher = specs.get('publisher') or str(first['Vendor']) or 'Indigo Books India'
    category = specs.get('category') or str(first['Type']) or 'Curated Literature'
    pages = specs.get('pages') or '250p'
    edition = specs.get('edition') or '1st Edition'
    lang = specs.get('language') or 'Hindi'
    
    cover = p_var['img'] or variants[0]['img']
    price = p_var['price']
    isbn = p_var['sku']
    weight = p_var['grams']
    qty = p_var['qty']
    
    return {
        'handle': handle,
        'title': title,
        'author': author,
        'pub': publisher,
        'category': category,
        'pages': pages,
        'edition': edition,
        'lang': lang,
        'binding': p_var['format'],
        'price': price,
        'isbn': isbn,
        'weight': f"{weight} g",
        'stock': qty,
        'cover': cover,
        'variants': variants,
        'overview': f"Authentic work by {author}. Published by {publisher}, this authoritative volume represents an essential edition in Indian literature and scholarly thought.",
        'highlights': [
            f"Official Edition from {publisher}",
            f"ISBN: {isbn} • {pages} Standard Print Pages",
            "Verified Authentic Text with Complete Unabridged Content",
            "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"
        ]
    }

print("Testing Godan:")
print(json.dumps(get_book_record('godan-premchand'), indent=2))

