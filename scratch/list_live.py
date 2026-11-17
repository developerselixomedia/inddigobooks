import urllib.request
import re

req = urllib.request.Request('https://indigobooks.shop/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

m = re.search(r'window\.SHOPIFY_LIVE_PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
if m:
    content = m.group(1)
    handles = re.findall(r'handle:\s*"([^"]+)"', content)
    titles = re.findall(r'title:\s*"([^"]+)"', content)
    variant_ids = re.findall(r'variant_id:\s*(\d+)', content)
    print(f"Total handles: {len(handles)}")
    for i in range(len(handles)):
        vid = variant_ids[i] if i < len(variant_ids) else 'none'
        print(f"{i+1}. {titles[i]} | handle: {handles[i]} | variant: {vid}")
else:
    print("SHOPIFY_LIVE_PRODUCTS not found")
