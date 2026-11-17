import urllib.request
import re

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
    # Find all handles and titles
    handles = re.findall(r'handle:\s*"([^"]+)"', raw)
    titles = re.findall(r'title:\s*"([^"]+)"', raw)
    variant_ids = re.findall(r'variant_id:\s*(\d+)', raw)
    print(f"Total live products in SHOPIFY_LIVE_PRODUCTS: {len(handles)}")
    for h, t, v in zip(handles, titles, variant_ids):
        if any(w in (h + ' ' + t).lower() for w in ['samvidhan', 'darbari', 'godan', 'premchand', 'rashmirathi', 'chitralekha', 'tarkash']):
            print(f"MATCH -> handle: {h}, title: {t}, variant_id: {v}")
