# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the appended text if outside
patch_marker = '/* STRICT SYMMETRICAL FULL-WIDTH STATS BAR (ZERO SQUISHING) */'
if patch_marker in text:
    text = text[:text.find(patch_marker)].strip()

# Now find where UNIFIED_STORE_CSS ends
# The docstring uses """ (1 at start, 1 at end of docstring)
# UNIFIED_STORE_CSS uses """ (1 at start, 1 at end)
# So there should be 4 triple quotes in total.
if not text.endswith('"""'):
    # append patch INSIDE the triple quotes
    text = text.rstrip()
    if text.endswith('"""'):
        text = text[:-3]
    stats_css_patch = '''
/* STRICT SYMMETRICAL FULL-WIDTH STATS BAR (ZERO SQUISHING) */
.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 28px 0 !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
  padding: 0 32px !important;
  text-align: center !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px 12px !important;
    padding: 0 16px !important;
  }
}

.stat-card, .stat-item {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
  padding: 8px 12px !important;
  border: none !important;
  border-right: none !important;
  border-left: none !important;
  box-sizing: border-box !important;
}

.stat-number, .stat-num {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
  border: none !important;
}

.stat-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  max-width: 220px !important;
  margin: 0 auto !important;
  border: none !important;
}

/* KILL ALL VERTICAL BARS, PSEUDO-ELEMENTS, OR CARETS */
.stats-bar *,
.stats-grid *,
[class*="stat"] *,
.stats-bar *::before,
.stats-bar *::after,
.stats-grid *::before,
.stats-grid *::after,
[class*="stat"]::before,
[class*="stat"]::after {
  content: none !important;
  border-right: none !important;
  border-left: none !important;
  outline: none !important;
  box-shadow: none !important;
  caret-color: transparent !important;
}
"""
'''
    text += stats_css_patch

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed store_styles.py")

