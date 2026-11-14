# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('Site Header with Indigo Books Emblem', 'INDIGO BOOKS'),
    ('4-Phase Choreographed Hero Section', 'id="heroSection"'),
    ('Golden Lotus Rangoli', 'hero-rangoli-wrap'),
    ('Diyas & Flame Animation', 'flame-outer-flicker'),
    ('2-Tier Zero-Overlap Book Grid & Spotlight', 'book-shelf-item'),
    ('Section 1: Literary Marquee & Ticker', 'id="literaryMarqueeSection"'),
    ('Section 2: 3D Curator Podium & Page Flip', 'id="curatorsPodiumSection"'),
    ('Section 3: Mehfil-e-Rekhta Dark Lounge', 'id="mehfilRekhtaSection"'),
    ('Section 4: Bundle Unboxing Showcase', 'id="bundleUnboxingSection"'),
    ('Section 5: Regional Magazine Masonry', 'id="regionalMagazineSection"'),
    ('Section 6: Law & Academic Vault', 'id="academicVaultSection"'),
    ('Section 7: Trust Features Strip', 'id="trustFeaturesSection"'),
    ('Floating Concierge Dock (WhatsApp & Cart)', 'WhatsApp Order'),
    ('Rich Literary Footer', '<footer'),
    ('Slide-Over Shopping Cart Drawer', 'id="cartDrawerBackdrop"'),
    ('Quick View Modal', 'id="quickViewBackdrop"'),
    ('Member Login Modal', 'id="loginModalBackdrop"'),
]

print("=== PREVIEW.HTML VERIFICATION ===")
all_passed = True
for label, needle in checks:
    status = "PASS" if needle in html else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"[{status}] {label}")

import json
with open('templates/index.json', 'r', encoding='utf-8') as f:
    idx = json.load(f)
print("\n=== TEMPLATES/INDEX.JSON ORDER ===")
for i, s in enumerate(idx['order'], 1):
    print(f"{i}. {s}")

print("\nAll checks passed!" if all_passed else "\nSome checks failed!")
