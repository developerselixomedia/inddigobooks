import urllib.request
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

queries = ['Raag Darbari', 'Godan', 'Samvidhan', 'Premchand', 'Tarkash']

for q in queries:
    url = f"https://indigobooks.shop/search/suggest.json?q={urllib.parse.quote(q)}&resources[type]=product"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            products = data.get('resources', {}).get('results', {}).get('products', [])
            print(f"Query '{q}': found {len(products)} products")
            for p in products:
                print(f"  -> Title: {p.get('title')}, Handle: {p.get('handle')}, Price: {p.get('price')}, URL: {p.get('url')}")
    except Exception as e:
        print(f"Query '{q}' error: {e}")
