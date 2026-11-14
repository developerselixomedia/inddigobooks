# -*- coding: utf-8 -*-
with open('preview.html', encoding='utf-8') as f:
    p = f.read()
assert 'https://cdn.tailwindcss.com' in p, 'Tailwind missing in preview.html'
assert 'id="hero-locked-styles"' in p, 'hero-locked-styles missing in preview.html'
assert 'id="indigo-video-hero"' in p, 'indigo-video-hero missing in preview.html'
assert 'id="ivh-books-grid"' in p, 'ivh-books-grid missing in preview.html'
assert 'ivh-book-card' in p, 'ivh-book-card missing in preview.html'

with open('layout/theme.liquid', encoding='utf-8') as f:
    t = f.read()
assert 'https://cdn.tailwindcss.com' in t, 'Tailwind missing in theme.liquid'
assert 'theme.css' in t, 'theme.css missing in theme.liquid'
assert 'id="hero-locked-styles"' in t, 'hero-locked-styles missing in theme.liquid'

with open('sections/main-indigo-store.liquid', encoding='utf-8') as f:
    s = f.read()
assert 'id="indigo-video-hero"' in s, 'indigo-video-hero missing in main-indigo-store.liquid'
assert 'id="ivh-books-grid"' in s, 'ivh-books-grid missing in main-indigo-store.liquid'
assert 'ivh-book-card' in s, 'ivh-book-card missing in main-indigo-store.liquid'

with open('sections/main-store.liquid', encoding='utf-8') as f:
    s2 = f.read()
assert 'id="indigo-video-hero"' in s2, 'indigo-video-hero missing in main-store.liquid'
assert 'id="ivh-books-grid"' in s2, 'ivh-books-grid missing in main-store.liquid'

print("ALL HERO & TAILWIND ASSERTIONS PASSED 100%!")

