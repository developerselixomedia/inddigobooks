import urllib.request
import re

total_found = 0
for page in range(1, 15):
    url = f"https://indigobooks.shop/collections/all?page={page}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for /products/ links
            matches = re.findall(r'/products/([a-z0-9\-]+)', html)
            unique_h = set(matches)
            total_found += len(unique_h)
            print(f"Page {page}: found {len(unique_h)} unique products (cumulative: {total_found})")
            if len(unique_h) == 0:
                break
    except Exception as e:
        print(f"Page {page} error: {e}")
        break
