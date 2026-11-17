import urllib.request
import re
import json

req = urllib.request.Request(
    'https://indigobooks.shop/',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
)

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

match = re.search(r'window\.SHOPIFY_LIVE_PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
if match:
    raw = match.group(1).strip()
    # Let's inspect the first object
    first_obj = raw.split('},\n    {')[0] + '}'
    print("First object in SHOPIFY_LIVE_PRODUCTS on live site:")
    print(first_obj[:800])
