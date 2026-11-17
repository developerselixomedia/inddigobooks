with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

selectors = [
    'editorial-scatter-hero', 'scatter-book-cover', 'v2-mobile-hero-showcase',
    'editorial-header-actions', 'v2-hamburger-btn', 'v2-mobile-nav-actions',
    'v2-nav-brand-group', 'site-navbar'
]

# Find all @media blocks
mq_matches = list(re.finditer(r'@media[^{]+\{', text))
print(f"Total @media queries in editorial_video_theme.py: {len(mq_matches)}")

for m in mq_matches:
    start = m.start()
    header = m.group()
    # find snippet
    snippet = text[start:start+1200]
    matched_sel = [s for s in selectors if s in snippet]
    if matched_sel:
        print(f"MQ at {start}: {header.strip()}")
        print(f"  Selectors found: {matched_sel}")
        print("="*50)
