# -*- coding: utf-8 -*-
with open('assets/main-store.css', 'r', encoding='utf-8') as f:
    css = f.read()

checks = [
    ('Modal card white background', '.modal-card' in css and 'background: #FFFFFF !important' in css),
    ('Modal card box shadow & border radius', 'border-radius: 16px !important' in css and 'box-shadow: 0 24px 60px' in css),
    ('PDP full-width on mobile', 'display: contents !important' in css),
    ('PDP tech table width 100%', '.pdp-tech-table' in css and 'width: 100% !important' in css),
    ('Vault cards 2-col on mobile', 'grid-template-columns: repeat(2, minmax(0, 1fr)) !important' in css),
    ('wa-tooltip hidden on mobile', '.wa-tooltip' in css and 'display: none !important' in css)
]

for name, res in checks:
    status = "PASS" if res else "FAIL"
    print(f"{name}: {status}")
