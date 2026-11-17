import urllib.request
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_handles = [
    'raag-darbari-shrilal-shukla',
    'godan-premchand',
    'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
    'tarkash-javed-akhtar',
    'chitralekha-bhagwaticharan-verma',
    'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
    'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
    'aadha-gaon-rahi-masoom-raza',
    'gaban-premchand',
    'nirmala-premchand',
    'madhushala-harivansh-rai-bachchan',
    'gunahon-ka-devta-dharamvir-bharati',
    'kamayani-jaishankar-prasad'
]

results = {}
for h in test_handles:
    url = f"https://indigobooks.shop/products/{h}.js"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results[h] = {
                'id': data.get('id'),
                'title': data.get('title'),
                'variants': [
                    {'id': v['id'], 'title': v['title'], 'price': v['price']/100.0, 'sku': v['sku']}
                    for v in data.get('variants', [])
                ]
            }
            print(f"[FOUND] {h}: {len(results[h]['variants'])} variants")
            for v in results[h]['variants']:
                print(f"   variant {v['id']}: {v['title']} - ₹{v['price']}")
    except Exception as e:
        print(f"[FAILED] {h}: {e}")
    time.sleep(0.5)

with open('scratch/live_product_variants_map.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print("Saved to scratch/live_product_variants_map.json")
