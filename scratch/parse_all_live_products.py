import urllib.request
import re

req = urllib.request.Request(
    'https://indigobooks.shop/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

match = re.search(r'window\.SHOPIFY_LIVE_PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
if match:
    raw = match.group(1).strip()
    print("Length of raw SHOPIFY_LIVE_PRODUCTS:", len(raw))
    # Count occurrences of 'handle:'
    handles = re.findall(r'handle:\s*"([^"]+)"', raw)
    titles = re.findall(r'title:\s*"([^"]+)"', raw)
    variants = re.findall(r'variant_id:\s*(\d+)', raw)
    prices = re.findall(r'price:\s*"([^"]+)"', raw)
    print(f"Found {len(handles)} handles, {len(titles)} titles, {len(variants)} variants, {len(prices)} prices.")
    for i in range(min(len(handles), len(titles))):
        v = variants[i] if i < len(variants) else 'N/A'
        p = prices[i] if i < len(prices) else 'N/A'
        print(f"{i+1}. handle: {handles[i]} | title: {titles[i]} | variant: {v} | price: {p}")
