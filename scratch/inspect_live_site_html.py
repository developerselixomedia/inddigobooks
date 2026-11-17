import urllib.request
import re

req = urllib.request.Request(
    'https://indigobooks.shop/',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Fetched {len(html)} bytes from indigobooks.shop")
        # Search for SHOPIFY_LIVE_PRODUCTS
        match = re.search(r'window\.SHOPIFY_LIVE_PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
        if match:
            content = match.group(1).strip()
            print(f"SHOPIFY_LIVE_PRODUCTS content length: {len(content)}")
            if len(content) > 0:
                print("First 300 chars of SHOPIFY_LIVE_PRODUCTS:")
                print(content[:300])
            else:
                print("SHOPIFY_LIVE_PRODUCTS is EMPTY array []!")
        else:
            print("window.SHOPIFY_LIVE_PRODUCTS NOT found in HTML!")
except Exception as e:
    print("Error:", e)
