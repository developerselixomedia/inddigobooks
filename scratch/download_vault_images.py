# -*- coding: utf-8 -*-
import urllib.request, os

images_to_download = {
    'assets/book-highcourt.jpg': 'https://images.rajkamalprakashan.com/products/--1776288058601.jpg',
    'assets/book-samvidhan.jpg': 'https://images.rajkamalprakashan.com/products/--1776285478375.jpg',
    'assets/book-sanhita.jpg': 'https://images.rajkamalprakashan.com/products/--1776276748463.jpg',
    'assets/book-kasauti.jpg': 'https://images.rajkamalprakashan.com/products/--1776287918098.jpg',
    'assets/book-gyan-aur-karm.jpg': 'https://images.rajkamalprakashan.com/products/--1776279603665.jpg',
    'assets/book-shilp-vidhi.jpg': 'https://images.rajkamalprakashan.com/products/--1776277159772.jpg',
    'assets/book-hindi-sahitya-itihas.jpg': 'https://images.rajkamalprakashan.com/products/--1776277485047.jpg',
    'assets/book-anusandhan.jpg': 'https://images.rajkamalprakashan.com/products/--1776284895141.jpg',
    'assets/book-hadappa.jpg': 'https://images.rajkamalprakashan.com/products/--1776278159998.jpg',
    'assets/book-badalata-desh.jpg': 'https://images.rajkamalprakashan.com/products/--1776276958819.jpg',
    'assets/book-nyay-sangharsh.jpg': 'https://images.rajkamalprakashan.com/products/--1776281327554.jpg',
    'assets/book-soochana.jpg': 'https://images.rajkamalprakashan.com/products/--1776279601546.jpg',
    'assets/book-savarkar.jpg': 'https://images.rajkamalprakashan.com/products/--1776283610095.jpg',
    'assets/book-haashiye.jpg': 'https://images.rajkamalprakashan.com/products/--1776282936560.jpg',
    'assets/book-azad.jpg': 'https://images.rajkamalprakashan.com/products/--1776277773460.jpg',
    'assets/book-haadse.jpg': 'https://images.rajkamalprakashan.com/products/--1776278864270.jpg',
}

for dest, url in images_to_download.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
            print(f"Downloaded {dest} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {dest}: {e}")
