# -*- coding: utf-8 -*-
import os

with open('store_styles.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure stats bar and grid are rock solid and centered
old_stats = """.stats-bar {
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
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 20px 12px !important;
  padding: 0 16px !important;
  width: 100% !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
  text-align: center !important;
  box-sizing: border-box !important;
}

@media (min-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 32px 24px !important;
    padding: 0 32px !important;
  }
}

.stat-item {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
}"""

new_stats = """.stats-bar {
  display: block !important;
  width: 100% !important;
  background: #FFFFFF !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 28px 0 !important;
  box-sizing: border-box !important;
}

.stats-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 24px !important;
  width: 100% !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  text-align: center !important;
  box-sizing: border-box !important;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 0 16px !important;
  }
}

.stat-item, .stat-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
}

.stat-num, .stat-number {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 32px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.15 !important;
  margin-bottom: 6px !important;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.stat-label {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #64748B !important;
  line-height: 1.35 !important;
  text-align: center !important;
}"""

if old_stats in content:
    content = content.replace(old_stats, new_stats)
    print("Replaced old_stats with new_stats in store_styles.py")
else:
    print("old_stats not found; will append new_stats")

pdp_css = """
/* =========================================================================
   DEDICATED AMAZON-STYLE PRODUCT DETAILS PAGE (#single-product-page-view)
   ========================================================================= */
.store-view-section {
  width: 100%;
  min-height: 80vh;
}

.product-page-wrapper {
  max-width: 1280px;
  margin: 0 auto;
  padding: 24px 20px 60px;
  box-sizing: border-box;
}

.product-breadcrumb-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 0 20px;
  border-bottom: 1px solid #E2E8F0;
  margin-bottom: 28px;
  font-size: 13px;
  color: #64748B;
  flex-wrap: wrap;
  gap: 12px;
}

.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.breadcrumb-nav a {
  color: #0066B3;
  text-decoration: none;
  font-weight: 500;
}

.breadcrumb-nav a:hover {
  text-decoration: underline;
}

.breadcrumb-separator {
  color: #94A3B8;
  font-size: 12px;
}

.btn-back-to-store {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #F1F5F9;
  color: #0F172A;
  border: 1px solid #CBD5E1;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-back-to-store:hover {
  background: #E2E8F0;
  border-color: #94A3B8;
}

/* Amazon-Style 3-Column Grid */
.product-pdp-grid {
  display: grid;
  grid-template-columns: 360px 1fr 320px;
  gap: 36px;
  align-items: start;
}

@media (max-width: 1100px) {
  .product-pdp-grid {
    grid-template-columns: 320px 1fr 280px;
    gap: 24px;
  }
}

@media (max-width: 900px) {
  .product-pdp-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}

/* Left Column: Cover & Excerpt Toggle */
.pdp-left-col {
  position: sticky;
  top: 96px;
}

.pdp-cover-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  text-align: center;
}

.pdp-cover-img-wrap {
  width: 100%;
  aspect-ratio: 2 / 3;
  max-height: 480px;
  margin: 0 auto 16px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FAF8F5;
}

.pdp-cover-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.pdp-cover-img:hover {
  transform: scale(1.03);
}

.pdp-look-inside-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  background: #FEF3C7;
  color: #92400E;
  border: 1px solid #FDE68A;
  padding: 10px 16px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 12px;
}

.pdp-look-inside-btn:hover {
  background: #FDE68A;
}

.pdp-excerpt-box {
  display: none;
  background: #FFFDF9;
  border: 1px solid #F59E0B;
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
  text-align: left;
  font-size: 13.5px;
  line-height: 1.7;
  color: #334155;
  font-family: 'Merriweather', serif;
}

.pdp-excerpt-box.open {
  display: block;
  animation: fadeIn 0.25s ease;
}

.pdp-perks-checklist {
  list-style: none;
  padding: 0;
  margin: 16px 0 0;
  border-top: 1px solid #F1F5F9;
  padding-top: 16px;
  text-align: left;
}

.pdp-perks-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 12.5px;
  color: #475569;
  margin-bottom: 8px;
  line-height: 1.4;
}

/* Center Column: Book Editorial & Tech Table */
.pdp-center-col {
  padding-right: 12px;
}

.pdp-genre-pill {
  display: inline-block;
  background: #EFF6FF;
  color: #0066B3;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
}

.pdp-book-title {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 30px;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.25;
  margin: 0 0 8px;
}

.pdp-author-row {
  font-size: 15px;
  color: #64748B;
  margin-bottom: 12px;
}

.pdp-author-row strong {
  color: #0F172A;
}

.pdp-rating-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.pdp-stars {
  display: flex;
  gap: 2px;
  color: #F59E0B;
}

.pdp-rating-text {
  font-size: 13px;
  color: #64748B;
  font-weight: 600;
}

.pdp-price-wrap {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 14px 0;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
  margin-bottom: 20px;
}

.pdp-selling-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 28px;
  font-weight: 800;
  color: #0F172A;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-compare-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 16px;
  color: #94A3B8;
  text-decoration: line-through;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-discount-badge {
  background: #DC2626;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
}

.pdp-format-row {
  margin-bottom: 20px;
}

.pdp-format-label {
  font-size: 12px;
  font-weight: 700;
  color: #64748B;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}

.pdp-format-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #FFFFFF;
  border: 2px solid #0066B3;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  color: #0066B3;
}

.pdp-description-wrap {
  margin-bottom: 24px;
}

.pdp-sec-heading {
  font-family: 'Merriweather', Georgia, serif;
  font-size: 18px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 10px;
}

.pdp-description-text {
  font-size: 14px;
  line-height: 1.7;
  color: #334155;
  margin-bottom: 16px;
}

.pdp-tech-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  font-size: 13px;
}

.pdp-tech-table tr {
  border-bottom: 1px solid #F1F5F9;
}

.pdp-tech-table th {
  text-align: left;
  padding: 10px 0;
  color: #64748B;
  font-weight: 600;
  width: 35%;
}

.pdp-tech-table td {
  padding: 10px 0;
  color: #0F172A;
  font-weight: 500;
}

/* Right Column: Amazon-Style Sticky Buy Box */
.pdp-buy-box {
  background: #FFFFFF;
  border: 1px solid #CBD5E1;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 96px;
}

.pdp-bb-price {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 26px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 8px;
  font-variant-numeric: lining-nums tabular-nums !important;
}

.pdp-bb-stock {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #059669;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 14px;
}

.pdp-bb-delivery {
  font-size: 13px;
  color: #475569;
  line-height: 1.5;
  margin-bottom: 16px;
  padding-bottom: 14px;
  border-bottom: 1px solid #F1F5F9;
}

.pdp-bb-delivery strong {
  color: #0F172A;
}

.pdp-qty-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.pdp-qty-label {
  font-size: 13px;
  font-weight: 600;
  color: #0F172A;
}

.pdp-qty-control {
  display: inline-flex;
  align-items: center;
  border: 1px solid #CBD5E1;
  border-radius: 6px;
  overflow: hidden;
}

.pdp-qty-btn {
  background: #F8FAFC;
  border: none;
  width: 32px;
  height: 32px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  color: #0F172A;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pdp-qty-btn:hover {
  background: #E2E8F0;
}

.pdp-qty-input {
  width: 44px;
  height: 32px;
  border: none;
  border-left: 1px solid #CBD5E1;
  border-right: 1px solid #CBD5E1;
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  outline: none;
}

.pdp-btn-stack {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}

.pdp-btn-add-cart {
  width: 100%;
  background: #D99B26;
  color: #0A1128;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.pdp-btn-add-cart:hover {
  background: #B45309;
  color: #FFFFFF;
}

.pdp-btn-buy-now {
  width: 100%;
  background: #0F172A;
  color: #FFFFFF;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.pdp-btn-buy-now:hover {
  background: #1E293B;
}

.pdp-btn-wa-cod {
  width: 100%;
  background: #10B981;
  color: #FFFFFF;
  border: none;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.pdp-btn-wa-cod:hover {
  background: #059669;
}

.pdp-bb-security {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-size: 12px;
  color: #64748B;
  padding-top: 12px;
  border-top: 1px solid #F1F5F9;
}

/* Similar Books / Recommendations Grid */
.pdp-recommendations-sec {
  margin-top: 48px;
  padding-top: 36px;
  border-top: 1px solid #E2E8F0;
}

.pdp-rec-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 20px;
}

@media (max-width: 900px) {
  .pdp-rec-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
}

@media (max-width: 500px) {
  .pdp-rec-grid {
    grid-template-columns: 1fr;
  }
}
"""

if 'DEDICATED AMAZON-STYLE PRODUCT DETAILS PAGE' not in content:
    last_idx = content.rfind('"""')
    if last_idx != -1:
        content = content[:last_idx] + pdp_css + '\n' + content[last_idx:]
        print("Appended pdp_css successfully!")
    else:
        print("Could not find last triple quote")

with open('store_styles.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("store_styles.py written successfully!")

