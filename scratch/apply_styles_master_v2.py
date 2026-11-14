# -*- coding: utf-8 -*-
with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we insert before the closing """
closing_quotes = '"""'
assert text.rstrip().endswith(closing_quotes), "store_styles.py does not end with triple quotes"

new_styles = """
/* =========================================================================
   MASTER FIX 3 & 4: BALANCED 1320PX VAULT, INDIAN VOICES & PRAYAGRAJ HERITAGE
   ========================================================================= */

/* 1. Contemporary Indian Voices Grid (Balanced 1320px Layout) */
#contemporary-fiction .site-container,
.voices-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 28px !important;
  box-sizing: border-box !important;
}

.contemporary-grid {
  display: grid !important;
  grid-template-columns: 1fr 1.25fr !important;
  gap: 36px !important;
  width: 100% !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .contemporary-grid {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.feat-book-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 16px !important;
  padding: 32px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04) !important;
}

.mini-grid-2x2 {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

@media (max-width: 600px) {
  .mini-grid-2x2 {
    grid-template-columns: 1fr !important;
  }
}

.mini-book-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 16px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
}

/* 2. Law, Judiciary & Academic Reference Vault (Full 1320px Symmetry) */
#law-academic-vault .site-container,
.vault-container {
  max-width: 1320px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 28px !important;
  box-sizing: border-box !important;
}

.vault-layout {
  display: grid !important;
  grid-template-columns: 320px 1fr !important;
  gap: 36px !important;
  width: 100% !important;
  align-items: start !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .vault-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
}

.vault-nav-col {
  width: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}

.vault-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

@media (max-width: 640px) {
  .vault-cards-grid {
    grid-template-columns: 1fr !important;
  }
}

.vault-card {
  background: #FFFFFF !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 12px !important;
  padding: 18px !important;
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
}

/* 3. Prayagraj Heritage & Headquarters Section (Perfect Alignment) */
.heritage-section {
  background: #FAF8F5 !important;
  padding: 64px 0 !important;
  border-top: 1px solid #E2E8F0 !important;
  width: 100% !important;
}

.heritage-grid {
  display: grid !important;
  grid-template-columns: 1.2fr 0.8fr !important;
  gap: 48px !important;
  align-items: center !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
}

@media (max-width: 992px) {
  .heritage-grid {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
}

.heritage-stats-row {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 16px !important;
  margin-top: 24px !important;
  padding: 20px 0 !important;
  border-top: 1px solid #E2E8F0 !important;
  border-bottom: 1px solid #E2E8F0 !important;
  text-align: left !important;
}

.heritage-stat-val {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 24px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.2 !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.heritage-stat-lbl {
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  margin-top: 4px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

.heritage-card,
.heritage-hq-card {
  background: #0A1128 !important;
  color: #FFFFFF !important;
  border: 2px solid #D99B26 !important;
  border-radius: 16px !important;
  padding: 36px 32px !important;
  box-shadow: 0 12px 32px rgba(10, 17, 40, 0.25) !important;
  box-sizing: border-box !important;
}

.heritage-card h3,
.heritage-hq-card h3 {
  color: #FFFFFF !important;
  margin-top: 0 !important;
  font-family: 'Merriweather', Georgia, serif !important;
  font-size: 20px !important;
  font-weight: 700 !important;
}

.heritage-card p,
.heritage-hq-card p {
  color: #CBD5E1 !important;
  font-size: 13.5px !important;
  line-height: 1.6 !important;
}

.heritage-details-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 0 24px 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}

.heritage-details-list li {
  display: flex !important;
  align-items: flex-start !important;
  gap: 12px !important;
  font-size: 13.5px !important;
  color: #E2E8F0 !important;
  line-height: 1.5 !important;
}

.heritage-details-list li i,
.heritage-details-list li svg {
  color: #D99B26 !important;
  margin-top: 2px !important;
  flex-shrink: 0 !important;
}
"""

# Append before the last """
rpos = text.rfind(closing_quotes)
updated_text = text[:rpos] + new_styles + '\n' + closing_quotes + '\n'

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("Appended Master Fix 3 & 4 styles to store_styles.py successfully!")

