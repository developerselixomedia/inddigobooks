# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

tests = [
    ("Global Typography - Playfair Display & Plus Jakarta Sans", "Playfair Display" in html and "Plus Jakarta Sans" in html),
    ("3D Cover Open to -140deg", "rotateY(-140deg)" in html),
    ("Parchment Inside Page with Chapter 1 Excerpt & Mini Overview", "book-page-underneath" in html and "Read Full Preview" in html),
    ("Mehfil-e-Rekhta Vertical Flex Stack (Zero Cutoff)", "h-56 flex items-center justify-center mb-3" in html),
    ("Mehfil Full Titles (Kyon, Ranjish, Dozakhnama, Thanda, Dhuaan)", 
     "क्यों (Kyon)" in html and "रंजिश ही सही (Ranjish Hi Sahi)" in html and "दोज़ख़नामा (Dozakhnama)" in html and "ठंडा गोश्त (Thanda Gosht)" in html and "धुआँ (Dhuaan)" in html),
    ("Mehfil Mini Overviews", "An intimate anthology of Jaun Elia" in html and "A spellbinding posthumous conversation between Mirza Ghalib" in html),
    ("Regional Fiction Mini Overviews", "A profound, Sahitya Akademi-winning exploration of gender duality" in html),
    ("Bundle Showcase Mini Overviews", "Experience the complete literary breadth of Booker prize-winner" in html),
    ("Academic Vault Mini Overviews", "The supreme authority on forensic medicine" in html),
    ("Navbar Functional Tabs (handleNavClick)", "handleNavClick" in html and "activeNavTab" in html),
    ("Mehfil All Poets Tab & Dynamic Filter", "All Poets (सब शो'रा)" in html and "filterMehfilPoet" in html),
    ("Law & Academic Vault Tabs", "selectVaultDrawer" in html and "vault-drawer-btn" in html),
    ("Catalog Directory (#shop-all-catalog)", 'id="shop-all-catalog"' in html and "catalogActiveBanner" in html),
    ("Navbar Brand Logo Intact", 'INDIGO BOOKS' in html and 'aria-label="Indigo Books Emblem"' in html),
    ("4-Phase Hero Intact", 'id="heroSection"' in html and 'hero-rangoli-wrap' in html),
]

print("=== FINAL VERIFICATION RESULTS ===")
passed = 0
for name, condition in tests:
    status = "PASS" if condition else "FAIL"
    if condition: passed += 1
    print(f"[{status}] {name}")

print(f"\nTotal: {passed}/{len(tests)} tests passed.")

