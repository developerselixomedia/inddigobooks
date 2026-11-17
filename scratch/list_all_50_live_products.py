import urllib.request
import re
import json

# Let's fetch the live site HTML and inspect window.SHOPIFY_LIVE_PRODUCTS
req = urllib.request.Request(
    'https://indigobooks.shop/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Extract SHOPIFY_LIVE_PRODUCTS
match = re.search(r'window\.SHOPIFY_LIVE_PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
if match:
    raw = match.group(1).strip()
    # Let's parse all products
    items = raw.split('},\n    {')
    print(f"Total products in SHOPIFY_LIVE_PRODUCTS: {len(items)}")
    for idx, item_str in enumerate(items):
        # find handle, title, variantId, price
        h_m = re.search(r'handle:\s*"([^"]+)"', item_str)
        t_m = re.search(r'title:\s*"([^"]+)"', item_str)
        v_m = re.search(r'variant_id:\s*(\d+)', item_str) or re.search(r'variantId:\s*(\d+)', item_str)
        p_m = re.search(r'price:\s*"([^"]+)"', item_str)
        h = h_m.group(1) if h_m else 'unknown'
        t = t_m.group(1) if t_m else 'unknown'
        v = v_m.group(1) if v_m else 'unknown'
        p = p_m.group(1) if p_m else 'unknown'
        print(f"[{idx}] handle: {h} | title: {t} | variant_id: {v} | price: {p}")
