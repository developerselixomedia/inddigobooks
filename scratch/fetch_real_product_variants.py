import urllib.request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

handles = [
    'raag-darbari-shrilal-shukla',
    'raag-darbari-deluxe-edition-shrilal-shukla',
    'godan-premchand',
    'tarkash-javed-akhtar',
    'aadha-gaon-rahi-masoom-raza',
    '1984-george-orwell-tr-abhishek-srivastava'
]

for h in handles:
    url = f"https://indigobooks.shop/products/{h}.js"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"PRODUCT: {data.get('title')} (handle: {h})")
            print(f"  Price: {data.get('price') / 100.0} | URL: {data.get('url')}")
            for v in data.get('variants', []):
                print(f"    Variant ID: {v.get('id')}, Title: '{v.get('title')}', Price: {v.get('price') / 100.0}, Available: {v.get('available')}, Sku: {v.get('sku')}")
    except Exception as e:
        print(f"ERROR {h}: {e}")
