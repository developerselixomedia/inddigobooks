import urllib.request
import re

req = urllib.request.Request('https://indigobooks.shop/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

js_urls = re.findall(r'src="([^"]+main-store\.js[^"]*)"', html)
print('Found main-store.js URL on live site:', js_urls)
if js_urls:
    u = js_urls[0]
    if u.startswith('//'):
        u = 'https:' + u
    req2 = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req2) as resp2:
        js = resp2.read().decode('utf-8', errors='ignore')
        print('Live main-store.js size:', len(js))
        if 'proceedToCheckout' in js:
            idx = js.find('function proceedToCheckout')
            print('--- Live proceedToCheckout ---')
            print(js[idx:idx+1500])
        if 'handleSoloBuyNow' in js:
            idx2 = js.find('window.handleSoloBuyNow')
            print('--- Live handleSoloBuyNow ---')
            print(js[idx2:idx2+1500])
        if '67709588799778' in js:
            print('WARNING: 67709588799778 IS IN LIVE JS!')
