import urllib.request
import json

req = urllib.request.Request('https://indigobooks.shop/products.json?limit=250', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        products = data.get('products', [])
        print(f"Total products found on live shopify: {len(products)}")
        for p in products:
            variants = p.get('variants', [])
            v_id = variants[0]['id'] if variants else 'none'
            print(f"HANDLE: '{p.get('handle')}', TITLE: '{p.get('title')}', VID: {v_id}, PRICE: {variants[0].get('price') if variants else '0'}")
except Exception as e:
    print('Error:', e)
