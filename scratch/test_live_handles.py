import urllib.request
import json

test_handles = [
    'raag-darbari-shrilal-shukla',
    'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
    'godan-premchand',
    'aadami-aur-aurat-premchand-ed-chandan-pandey'
]

for h in test_handles:
    url = f'https://indigobooks.shop/products/{h}.js'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            vid = data['variants'][0]['id']
            print(f"FOUND {h}: variantId={vid}")
    except Exception as e:
        print(f"FAILED {h}: {e}")
