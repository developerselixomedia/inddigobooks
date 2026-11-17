import urllib.request
import re

url = 'https://indigobooks.shop/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')

    print('Favicon tags:')
    for m in re.finditer(r'<link[^>]*rel=[\"\'](shortcut )?icon[\"\'][^>]*>', html, re.I):
        print(' ', m.group(0))

    print('\nOpenGraph image:')
    for m in re.finditer(r'<meta[^>]*property=[\"\']og:image[\"\'][^>]*>', html, re.I):
        print(' ', m.group(0))

    print('\nSchema.org snippets:')
    for m in re.finditer(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', html, re.I | re.DOTALL):
        print(' ', m.group(1).strip()[:150], '...')
except Exception as e:
    print('Error:', e)
