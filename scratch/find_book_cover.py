import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls_to_check = [
    'https://www.bhartiyasahityas.com/products/jaane-jaan-lucknow',
    'https://www.buybooksindia.com/jaane-jaan-lucknow-9789377374068.html',
    'https://rajkamalprakashan.com/products/jaane-jaan-lucknow'
]

for url in urls_to_check:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=7) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            print(f"=== {url} (Status: {resp.status}) ===")
            imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', content)
            found_cover = [img for img in imgs if 'jaane' in img.lower() or 'products' in img.lower() or 'lucknow' in img.lower()]
            for img in found_cover[:5]:
                print("  Candidate:", img)
    except Exception as e:
        print(f"Failed {url}: {e}")
