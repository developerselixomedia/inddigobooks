# -*- coding: utf-8 -*-
"""
apply_complete_de_ai_polish.py
Comprehensive script executing the 4 major de-AI polish tasks for Indigo Books India.
"""

import os
import re
import urllib.parse

print("=== STARTING COMPLETE DE-AI POLISH & BUG FIX ===")

# =========================================================================
# STEP 1: LOAD LUCIDE ICONS IN layout/theme.liquid & ADD CSS IN theme.css
# =========================================================================
print("\n[Step 1] Loading Lucide Icons in layout/theme.liquid...")
with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    theme_liquid = f.read()

# Add Lucide unpkg script in <head>
lucide_head_script = '    <!-- Lucide Icons (Stroke-width 1.75) -->\n    <script src="https://unpkg.com/lucide@latest"></script>'
if 'lucide@latest' not in theme_liquid:
    theme_liquid = theme_liquid.replace('</head>', f'{lucide_head_script}\n</head>')

# Add Lucide createIcons() before </body>
lucide_init_script = """    <!-- Initialize Lucide Icons -->
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        if (typeof lucide !== 'undefined') {
          lucide.createIcons();
        }
      });
      window.addEventListener('load', function() {
        if (typeof lucide !== 'undefined') {
          lucide.createIcons();
        }
      });
    </script>"""

if 'lucide.createIcons()' not in theme_liquid:
    theme_liquid = theme_liquid.replace('</body>', f'{lucide_init_script}\n  </body>')

with open('layout/theme.liquid', 'w', encoding='utf-8') as f:
    f.write(theme_liquid)
print("SUCCESS: Lucide Icons CDN and initialization added to layout/theme.liquid")


# Add Lucide CSS in assets/theme.css
with open('assets/theme.css', 'r', encoding='utf-8') as f:
    theme_css = f.read()

lucide_css = """
/* ==========================================================================
   LUCIDE ICONS UNIVERSAL STYLING (De-AI Polish: Replaces all emojis)
   ========================================================================== */
[data-lucide],
i.lucide,
svg.lucide {
  display: inline-block !important;
  vertical-align: middle !important;
  width: 16px !important;
  height: 16px !important;
  stroke-width: 1.75 !important;
}
.icon-sm [data-lucide], [data-lucide].icon-sm {
  width: 13px !important;
  height: 13px !important;
}
.icon-md [data-lucide], [data-lucide].icon-md {
  width: 18px !important;
  height: 18px !important;
}
.icon-lg [data-lucide], [data-lucide].icon-lg {
  width: 22px !important;
  height: 22px !important;
}

/* Ensure permanent removal of white floating tooltip box */
.whatsapp-floating-tooltip {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

/* Clean Editorial Hairline Overline for section titles */
.editorial-overline {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin-bottom: 8px !important;
}
.editorial-overline__line {
  display: inline-block !important;
  width: 24px !important;
  height: 1.5px !important;
  background-color: #D99B26 !important;
}
.editorial-overline__text {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  color: #B45309 !important;
}
.editorial-overline--dark .editorial-overline__text {
  color: #FCD34D !important;
}
.editorial-overline--dark .editorial-overline__line {
  background-color: #F59E0B !important;
}
"""

if 'LUCIDE ICONS UNIVERSAL STYLING' not in theme_css:
    theme_css += "\n\n" + lucide_css.strip()
    with open('assets/theme.css', 'w', encoding='utf-8') as f:
        f.write(theme_css)
    print("SUCCESS: Lucide CSS and hairline overline styles added to assets/theme.css")


# =========================================================================
# STEP 2: DELETE WHITE BOTTOM BAR & DUPLICATE POWERED BY SHOPIFY
# =========================================================================
print("\n[Step 2] Removing duplicate white bottom bar...")

# Fix sections/footer-group.json to only contain "footer"
footer_group_json = """{
  "name": "Footer Group",
  "type": "footer",
  "sections": {
    "footer": {
      "type": "footer",
      "settings": {}
    }
  },
  "order": [
    "footer"
  ]
}
"""
with open('sections/footer-group.json', 'w', encoding='utf-8') as f:
    f.write(footer_group_json.strip())

# Empty sections/footer-utilities.liquid so nothing prints even if referenced
footer_utilities_empty = """{% comment %}
  Footer Utilities removed in favor of unified dark luxury footer
{% endcomment %}
{% schema %}
{
  "name": "Footer Utilities",
  "settings": []
}
{% endschema %}
"""
with open('sections/footer-utilities.liquid', 'w', encoding='utf-8') as f:
    f.write(footer_utilities_empty.strip())
print("SUCCESS: Duplicate white bottom bar removed from sections/footer-group.json and footer-utilities.liquid")


# =========================================================================
# STEP 3: DELETE FLOATING WHITE CHAT TOOLTIP BOX
# =========================================================================
print("\n[Step 3] Deleting floating white chat tooltip popup...")
with open('snippets/whatsapp-button.liquid', 'r', encoding='utf-8') as f:
    wa_btn = f.read()

# Remove the entire <div class="whatsapp-floating-tooltip" ...>...</div>
wa_btn_clean = re.sub(
    r'<div class="whatsapp-floating-tooltip".*?</div>\s*<button',
    '<button',
    wa_btn,
    flags=re.DOTALL
)

# Purge any emojis in whatsapp-button
wa_btn_clean = wa_btn_clean.replace('📚', '').replace('💬', '')

with open('snippets/whatsapp-button.liquid', 'w', encoding='utf-8') as f:
    f.write(wa_btn_clean)
print("SUCCESS: Floating tooltip box permanently deleted from snippets/whatsapp-button.liquid")


# =========================================================================
# STEP 4: REWRITE sections/media-with-content.liquid AS 2-COLUMN HERITAGE BANNER
# =========================================================================
print("\n[Step 4] Rewriting sections/media-with-content.liquid as 2-Column Editorial Heritage Banner...")
editorial_heritage_content = """{% comment %}
  Indigo Books India - Editorial Heritage Banner & Concierge Card
  Symmetrical 2-Column Layout: Heritage Narrative on Left + Prayagraj Concierge Card on Right
{% endcomment %}

<style id="editorialHeritageStyles">
  .editorial-heritage-section {
    padding: 72px 0 !important;
    background-color: #FAF8F5 !important;
    border-top: 1px solid #e2e8f0 !important;
    border-bottom: 1px solid #e2e8f0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .heritage-container {
    max-width: 1280px !important;
    margin: 0 auto !important;
    padding: 0 28px !important;
    box-sizing: border-box !important;
  }
  .heritage-grid {
    display: grid !important;
    grid-template-columns: 1.15fr 0.85fr !important;
    gap: 48px !important;
    align-items: center !important;
  }
  @media (max-width: 1023px) {
    .heritage-grid {
      grid-template-columns: 1fr !important;
      gap: 40px !important;
    }
  }
  .heritage-title {
    font-family: 'Libre Baskerville', Georgia, serif !important;
    font-size: 32px !important;
    font-weight: 700 !important;
    color: #0A1128 !important;
    line-height: 1.25 !important;
    margin: 8px 0 16px 0 !important;
  }
  @media (min-width: 1024px) {
    .heritage-title {
      font-size: 38px !important;
    }
  }
  .heritage-body {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    line-height: 1.75 !important;
    color: #475569 !important;
    margin-bottom: 14px !important;
  }
  .heritage-stat-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 16px !important;
    padding-top: 24px !important;
    margin-top: 24px !important;
    border-top: 1px solid #cbd5e1 !important;
  }
  .heritage-stat-val {
    font-family: 'Libre Baskerville', Georgia, serif !important;
    font-size: 26px !important;
    font-weight: 700 !important;
    color: #0A1128 !important;
    line-height: 1 !important;
  }
  .heritage-stat-val--gold {
    color: #D99B26 !important;
  }
  .heritage-stat-lbl {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 12px !important;
    color: #64748b !important;
    font-weight: 500 !important;
    margin-top: 6px !important;
  }
  .concierge-card {
    background-color: #0A1128 !important;
    color: #ffffff !important;
    padding: 36px 32px !important;
    border-radius: 12px !important;
    border: 1px solid rgba(217, 155, 38, 0.35) !important;
    box-shadow: 0 20px 40px -15px rgba(10, 17, 40, 0.4) !important;
    position: relative !important;
  }
  .concierge-header {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    padding-bottom: 20px !important;
    margin-bottom: 20px !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  }
  .concierge-emblem {
    width: 40px !important;
    height: 40px !important;
    border-radius: 8px !important;
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(217, 155, 38, 0.35) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #D99B26 !important;
    flex-shrink: 0 !important;
  }
  .concierge-item {
    display: flex !important;
    align-items: flex-start !important;
    gap: 12px !important;
    margin-bottom: 16px !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
    color: #cbd5e1 !important;
  }
  .concierge-item strong {
    color: #ffffff !important;
    display: block !important;
  }
  .concierge-item a {
    color: #D99B26 !important;
    text-decoration: none !important;
  }
  .concierge-item a:hover {
    text-decoration: underline !important;
  }
  .btn-concierge-wa {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    width: 100% !important;
    background: #25D366 !important;
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    padding: 14px 20px !important;
    border-radius: 8px !important;
    text-decoration: none !important;
    box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3) !important;
    transition: background 0.2s, transform 0.2s !important;
    margin-top: 24px !important;
    box-sizing: border-box !important;
  }
  .btn-concierge-wa:hover {
    background: #1eb956 !important;
    transform: translateY(-1px) !important;
  }
</style>

<section class="editorial-heritage-section" id="AboutIndigo-{{ section.id }}">
  <div class="heritage-container">
    <div class="heritage-grid">
      
      <!-- Left Column: Heritage Story & Unified Metric Baseline -->
      <div>
        <div class="editorial-overline" style="justify-content: flex-start;">
          <span class="editorial-overline__line"></span>
          <span class="editorial-overline__text">PRAYAGRAJ LITERARY HERITAGE</span>
        </div>

        <h2 class="heritage-title">
          From the Literary Heart of Prayagraj to Every Reader in India
        </h2>

        <p class="heritage-body">
          Indigo Books India is rooted in the historic literary city of Prayagraj—the cultural crossroads of the Hindi belt and Urdu poetry. We provide over 11,922+ authentic publisher editions ranging from timeless Rekhta poetry and contemporary Indian fiction to university legal treatises and competitive examination archives.
        </p>

        <p class="heritage-body">
          Every volume is verified for original printing, individually bubble-cushioned, and dispatched with pan-India express tracking and Cash on Delivery (COD) to every pin code across India.
        </p>

        <!-- 3-Column Metric Grid Aligned on Baseline -->
        <div class="heritage-stat-grid">
          <div>
            <div class="heritage-stat-val">11,922+</div>
            <div class="heritage-stat-lbl">Titles in Stock</div>
          </div>
          <div>
            <div class="heritage-stat-val heritage-stat-val--gold">24-Hour</div>
            <div class="heritage-stat-lbl">Express Dispatch</div>
          </div>
          <div>
            <div class="heritage-stat-val">Pan-India</div>
            <div class="heritage-stat-lbl">Cash on Delivery</div>
          </div>
        </div>
      </div>

      <!-- Right Column: Direct Store & Concierge Card -->
      <div>
        <div class="concierge-card">
          <div class="concierge-header">
            <span class="concierge-emblem">
              {% render 'icon-indigo-emblem' %}
            </span>
            <div>
              <h3 style="font-family: 'Libre Baskerville', Georgia, serif; font-size: 17px; font-weight: 700; color: #ffffff; margin: 0;">
                Indigo Books India — Headquarters
              </h3>
              <span style="font-size: 11px; color: #D99B26; letter-spacing: 0.05em; text-transform: uppercase;">Literary Concierge & Distribution</span>
            </div>
          </div>

          <div class="concierge-item">
            <i data-lucide="map-pin" style="color: #D99B26; margin-top: 3px; flex-shrink: 0;"></i>
            <div>
              <strong>Headquarters & Dispatch Facility:</strong>
              <span style="color: #94a3b8;">Civil Lines / Katra Literary District, Prayagraj, Uttar Pradesh 211001, India</span>
            </div>
          </div>

          <div class="concierge-item">
            <i data-lucide="clock" style="color: #D99B26; margin-top: 3px; flex-shrink: 0;"></i>
            <div>
              <strong>Operating Hours:</strong>
              <span style="color: #94a3b8;">Monday &ndash; Saturday: 10:00 AM &ndash; 8:30 PM IST (Sunday Online Dispatch)</span>
            </div>
          </div>

          <div class="concierge-item">
            <i data-lucide="phone" style="color: #D99B26; margin-top: 3px; flex-shrink: 0;"></i>
            <div>
              <strong>Direct Phone & Bulk Inquiries:</strong>
              <a href="tel:+918881122722">+91 8881122722</a>
            </div>
          </div>

          <div class="concierge-item">
            <i data-lucide="mail" style="color: #D99B26; margin-top: 3px; flex-shrink: 0;"></i>
            <div>
              <strong>Official Publisher Correspondence:</strong>
              <a href="mailto:info@indigobooks.com" style="color: #cbd5e1;">info@indigobooks.com</a>
            </div>
          </div>

          <a
            href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%20Prayagraj!%20I%20would%20like%20to%20order%20books%20from%20your%20store."
            target="_blank"
            rel="noopener"
            class="btn-concierge-wa"
          >
            <i data-lucide="message-circle"></i>
            <span>Order via WhatsApp (+91 8881122722)</span>
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

{% schema %}
{
  "name": "Editorial Heritage Banner",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "From the Literary Heart of Prayagraj to Every Reader in India"
    }
  ],
  "presets": [
    {
      "name": "Editorial Heritage Banner"
    }
  ]
}
{% endschema %}
"""

with open('sections/media-with-content.liquid', 'w', encoding='utf-8') as f:
    f.write(editorial_heritage_content.strip())
print("SUCCESS: sections/media-with-content.liquid rewritten as 2-Column Editorial Heritage Banner")


# =========================================================================
# STEP 5: REWRITE sections/footer.liquid
#    - Strict 4-column baseline alignment
#    - Lucide icons replacing all emojis
#    - Unified flex row newsletter input
#    - Final bottom element (no white bar below)
# =========================================================================
print("\n[Step 5] Upgrading sections/footer.liquid...")
footer_content = """{% comment %}
  Main Bookstore Footer - Indigo Books India (Prayagraj)
  100% Standalone CSS with Lucide SVG Icons & Strict Baseline Alignment
{% endcomment %}

<style id="footerStandaloneCss">
  .site-footer {
    background: #0A1128 !important;
    color: #cbd5e1 !important;
    border-top: 1px solid rgba(217, 155, 38, 0.35) !important;
    padding: 64px 0 32px 0 !important;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    width: 100% !important;
    margin-bottom: 0 !important;
    box-sizing: border-box !important;
  }
  .site-footer .footer-container {
    max-width: 1280px !important;
    margin: 0 auto !important;
    padding: 0 24px !important;
    box-sizing: border-box !important;
  }
  @media (min-width: 1024px) {
    .site-footer .footer-container {
      padding: 0 32px !important;
    }
  }
  .footer-grid {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 40px !important;
    margin-bottom: 48px !important;
    align-items: start !important;
  }
  @media (min-width: 768px) {
    .footer-grid {
      grid-template-columns: 1.5fr 1fr 1fr 1.3fr !important;
      gap: 36px !important;
      align-items: start !important;
    }
  }
  @media (min-width: 1024px) {
    .footer-grid {
      grid-template-columns: 1.8fr 1fr 1fr 1.4fr !important;
      gap: 48px !important;
      align-items: start !important;
    }
  }
  .footer-col {
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: flex-start !important;
  }
  .footer-subheading {
    font-family: 'Libre Baskerville', Georgia, serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin: 0 0 18px 0 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    border-bottom: 2px solid #D99B26 !important;
    display: inline-block !important;
    padding-bottom: 4px !important;
    line-height: 1.3 !important;
  }
  .footer-text {
    font-size: 13px !important;
    line-height: 1.7 !important;
    color: #94a3b8 !important;
    margin: 0 0 14px 0 !important;
  }
  .footer-contact-details {
    margin-top: 14px !important;
    font-size: 13px !important;
    line-height: 1.8 !important;
    color: #cbd5e1 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 6px !important;
  }
  .footer-contact-item {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
  }
  .footer-contact-details a {
    color: #D99B26 !important;
    text-decoration: none !important;
  }
  .footer-contact-details a:hover {
    text-decoration: underline !important;
  }
  .footer-links {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .footer-links li {
    margin-bottom: 10px !important;
  }
  .footer-links a {
    color: #94a3b8 !important;
    text-decoration: none !important;
    font-size: 13px !important;
    transition: color 0.2s, transform 0.2s !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
  }
  .footer-links a:hover {
    color: #D99B26 !important;
    transform: translateX(3px) !important;
  }
  .footer-whatsapp-box {
    background: rgba(37, 211, 102, 0.08) !important;
    border: 1px solid rgba(37, 211, 102, 0.3) !important;
    border-radius: 10px !important;
    padding: 14px 16px !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 12px !important;
    color: #ffffff !important;
    margin-top: 18px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .footer-whatsapp-box strong {
    color: #25D366 !important;
    font-size: 13px !important;
    display: block !important;
    margin-bottom: 2px !important;
  }
  .footer-whatsapp-box p {
    font-size: 11px !important;
    color: #cbd5e1 !important;
    margin: 0 0 6px 0 !important;
  }
  .footer-wa-link {
    color: #25D366 !important;
    font-weight: 700 !important;
    font-size: 12px !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
  }
  .footer-wa-link:hover {
    text-decoration: underline !important;
  }
  .footer-social-row {
    margin-top: 18px !important;
    display: flex !important;
    gap: 14px !important;
    font-size: 13px !important;
  }
  .footer-social-row a {
    color: #cbd5e1 !important;
    text-decoration: none !important;
  }
  .footer-social-row a:hover {
    color: #D99B26 !important;
  }
  .newsletter-input-group {
    display: flex !important;
    gap: 8px !important;
    margin-top: 14px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .newsletter-input {
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    font-size: 13px !important;
    flex: 1 !important;
    outline: none !important;
    box-sizing: border-box !important;
  }
  .newsletter-input:focus {
    border-color: #D99B26 !important;
  }
  .btn--newsletter {
    background: #D99B26 !important;
    color: #020617 !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    padding: 10px 18px !important;
    font-size: 13px !important;
    border: none !important;
    cursor: pointer !important;
    transition: background 0.2s !important;
    flex-shrink: 0 !important;
  }
  .btn--newsletter:hover {
    background: #b88019 !important;
  }
  .footer-bottom-bar {
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
    padding-top: 24px !important;
    margin-top: 24px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    align-items: center !important;
    justify-content: space-between !important;
    font-size: 12px !important;
    color: #64748b !important;
  }
  @media (min-width: 768px) {
    .footer-bottom-bar {
      flex-direction: row !important;
    }
  }
</style>

<footer class="site-footer" id="Footer-{{ section.id }}">
  <div class="footer-container">
    <div class="footer-grid">
      
      <!-- Column 1: Brand & Headquarters Info -->
      <div class="footer-col footer-col--brand">
        <div class="footer-logo-wrap" style="margin-bottom: 16px; display: inline-flex; align-items: center; gap: 10px;">
          <span style="width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;">
            {% render 'icon-indigo-emblem' %}
          </span>
          <span style="font-family: 'Libre Baskerville', Georgia, serif; font-size: 20px; letter-spacing: 0.12em; color: #ffffff; font-weight: normal; text-transform: uppercase;">
            INDIGO BOOKS
          </span>
        </div>

        <p class="footer-text">
          {{ section.settings.about_text | default: 'Indigo Books India is your premier independent bookstore based in the historic literary city of Prayagraj. Providing authentic publisher editions with Cash on Delivery (COD) and express delivery to every pin code across India.' }}
        </p>

        <!-- Direct Contact Details with Lucide Icons -->
        <div class="footer-contact-details">
          <div class="footer-contact-item">
            <i data-lucide="phone" style="color: #D99B26;"></i>
            <span><strong>Phone:</strong> <a href="tel:+918881122722">+91 8881122722</a></span>
          </div>
          <div class="footer-contact-item">
            <i data-lucide="mail" style="color: #D99B26;"></i>
            <span><strong>Email:</strong> <a href="mailto:info@indigobooks.com">info@indigobooks.com</a></span>
          </div>
          <div class="footer-contact-item">
            <i data-lucide="map-pin" style="color: #D99B26;"></i>
            <span><strong>HQ:</strong> Prayagraj, Uttar Pradesh, India</span>
          </div>
        </div>

        <!-- WhatsApp Support Card -->
        <div class="footer-whatsapp-box">
          <i data-lucide="message-circle" style="color: #25D366; width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px;"></i>
          <div>
            <strong>Need Book Recommendations or Quick Order?</strong>
            <p>Chat directly with our book concierge on WhatsApp.</p>
            <a href="https://wa.me/{{ settings.whatsapp_number | default: '918881122722' | remove: '+' | remove: ' ' }}?text=Hi%20Indigo%20Books%20India,%20I%20need%20help%20finding%20a%20book." target="_blank" rel="noopener" class="footer-wa-link">
              <span>Chat on WhatsApp (+91 8881122722)</span>
              <i data-lucide="arrow-right" class="icon-sm"></i>
            </a>
          </div>
        </div>

        <!-- Social Media Links -->
        <div class="footer-social-row">
          <a href="https://www.instagram.com/indigobooksindia" target="_blank" rel="noopener">
            <strong>Instagram (@indigobooksindia)</strong>
          </a>
          <span style="color: #64748b;">•</span>
          <a href="https://www.facebook.com/indigobooks" target="_blank" rel="noopener">
            <strong>Facebook</strong>
          </a>
        </div>
      </div>

      <!-- Column 2: Featured Collections -->
      <div class="footer-col">
        <h4 class="footer-subheading">Featured Collections</h4>
        <ul class="footer-links">
          <li>
            <a href="/collections/all?filter.p.m.custom.genre=Best+Sellers">
              <span>Best Sellers</span>
              <i data-lucide="trending-up" class="icon-sm" style="color: #D99B26;"></i>
            </a>
          </li>
          <li><a href="/collections/all?filter.p.m.custom.publisher=Rekhta">Rekhta Publications</a></li>
          <li><a href="/collections/all?filter.p.m.custom.author=Sudha+Murty">Sudha Murty Collection</a></li>
          <li><a href="/collections/all?filter.p.m.custom.author=Ruskin+Bond">Ruskin Bond Stories</a></li>
          <li><a href="/collections/all?filter.p.m.custom.genre=Law">Law &amp; Legal Studies</a></li>
          <li><a href="/collections/all?filter.p.m.custom.genre=Bundles">Book Bundles &amp; Box Sets</a></li>
          <li><a href="/collections/all?filter.p.m.custom.genre=Pre-Order">Coming Soon &amp; Pre-Orders</a></li>
        </ul>
      </div>

      <!-- Column 3: Customer Care -->
      <div class="footer-col">
        <h4 class="footer-subheading">Customer Care</h4>
        <ul class="footer-links">
          <li><a href="/pages/track-order">Track Your Order</a></li>
          <li><a href="/pages/shipping-policy">Shipping &amp; Delivery Across India</a></li>
          <li><a href="/pages/refund-policy">Easy Returns &amp; Replacements</a></li>
          <li><a href="/pages/quick-order">Bulk / Library / School Orders</a></li>
          <li><a href="/blogs">Indigo Reading Club Blogs</a></li>
          <li><a href="/pages/contact">Contact Us (Prayagraj)</a></li>
        </ul>
      </div>

      <!-- Column 4: Newsletter -->
      <div class="footer-col footer-col--newsletter">
        <h4 class="footer-subheading">Join The Book Club</h4>
        <p class="footer-text">Weekly reading guides, author interviews, and exclusive discounts delivered to your inbox.</p>
        {% form 'customer', class: 'footer-newsletter-form', style: 'width: 100%;' %}
          <input type="hidden" name="contact[tags]" value="newsletter,bookclub">
          <div class="newsletter-input-group">
            <input
              type="email"
              name="contact[email]"
              id="NewsletterEmail"
              placeholder="Enter your email"
              required
              class="newsletter-input"
            >
            <button type="submit" class="btn--newsletter">
              Subscribe
            </button>
          </div>
        {% endform %}
        
        <div style="margin-top: 18px; display: flex; align-items: center; gap: 8px; font-size: 11px; color: #64748b;">
          <i data-lucide="shield-check" style="color: #D99B26;"></i>
          <span>100% Privacy. Zero Spam Guarantee.</span>
        </div>
      </div>

    </div>

    <!-- Bottom Copyright & Credit -->
    <div class="footer-bottom-bar">
      <div>
        &copy; {{ 'now' | date: '%Y' }} Indigo Books India (Prayagraj). All Rights Reserved. Pan-India Delivery &amp; COD.
      </div>
      <div style="display: flex; gap: 16px; align-items: center;">
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <i data-lucide="check-circle" class="icon-sm" style="color: #25D366;"></i>
          <span>100% Genuine Editions</span>
        </span>
        <span>•</span>
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <i data-lucide="lock" class="icon-sm" style="color: #D99B26;"></i>
          <span>Verified Secure Payments</span>
        </span>
      </div>
    </div>
  </div>
</footer>

{% schema %}
{
  "name": "Footer",
  "settings": [
    {
      "type": "textarea",
      "id": "about_text",
      "label": "About Store Description",
      "default": "Indigo Books India is your premier online bookstore based in Prayagraj. Buy books online, explore latest releases, events, book clubs, and special offers across India."
    }
  ]
}
{% endschema %}
"""

with open('sections/footer.liquid', 'w', encoding='utf-8') as f:
    f.write(footer_content.strip())
print("SUCCESS: sections/footer.liquid rewritten with Lucide icons, baseline alignment, and clean newsletter flex row.")


# =========================================================================
# STEP 6: FIX CURATOR'S PODIUM COVERS (Remove Unsplash & Add 5 Vector Hardcover Jackets)
# =========================================================================
print("\n[Step 6] Upgrading sections/curators-podium.liquid & sections/podium.liquid...")

def build_svg_data_url(svg_content):
    # Minify and quote safely
    clean_svg = re.sub(r'\s+', ' ', svg_content).strip()
    return "data:image/svg+xml;utf8," + urllib.parse.quote(clean_svg)

# 1. Kasaibada (Manoj Rajan Tripathi) - Deep crimson/saffron hardcover with Devanagari typography
svg_kasaibada = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="300" height="450">
  <defs>
    <linearGradient id="bgKasaibada" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#580812"/>
      <stop offset="60%" stop-color="#350207"/>
      <stop offset="100%" stop-color="#190104"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D99B26"/>
      <stop offset="50%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#D99B26"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#bgKasaibada)"/>
  <!-- Spine Shadow -->
  <rect x="0" y="0" width="16" height="450" fill="#000000" opacity="0.35"/>
  <!-- Outer Gold Filigree Border -->
  <rect x="18" y="18" width="264" height="414" fill="none" stroke="url(#goldGrad)" stroke-width="2"/>
  <rect x="23" y="23" width="254" height="404" fill="none" stroke="#D99B26" stroke-width="0.75" opacity="0.7"/>
  <!-- Corner Ornaments -->
  <circle cx="28" cy="28" r="3" fill="#D99B26"/>
  <circle cx="272" cy="28" r="3" fill="#D99B26"/>
  <circle cx="28" cy="422" r="3" fill="#D99B26"/>
  <circle cx="272" cy="422" r="3" fill="#D99B26"/>
  <!-- Header Imprint -->
  <text x="150" y="55" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="3" fill="#D99B26" font-weight="700">VANI PRAKASHAN • CLASSIC FICTION</text>
  <line x1="60" y1="65" x2="240" y2="65" stroke="url(#goldGrad)" stroke-width="1"/>
  <!-- Decorative Floral Icon -->
  <path d="M150 90 C140 105 135 120 150 135 C165 120 160 105 150 90 Z" fill="#D99B26" opacity="0.3"/>
  <!-- Main Devanagari Title -->
  <text x="150" y="195" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="34" font-weight="bold" fill="#FFFDF0">कसाईबाड़ा</text>
  <text x="150" y="222" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" letter-spacing="4" fill="#D99B26" font-weight="700">K A S A I B A D A</text>
  <line x1="90" y1="240" x2="210" y2="240" stroke="url(#goldGrad)" stroke-width="1.5"/>
  <!-- Subtitle -->
  <text x="150" y="265" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" fill="#E2E8F0" opacity="0.85">उत्तर भारत का बहुचर्चित यथार्थवादी उपन्यास</text>
  <!-- Author Name in Devanagari -->
  <text x="150" y="335" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" letter-spacing="2" fill="#D99B26">लेखक</text>
  <text x="150" y="360" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="18" font-weight="bold" fill="#FFFFFF">मनोज राजन त्रिपाठी</text>
  <!-- Bottom Seal -->
  <circle cx="150" cy="405" r="12" fill="#D99B26" opacity="0.15" stroke="url(#goldGrad)" stroke-width="1"/>
  <text x="150" y="409" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#D99B26" font-weight="bold">वाणी</text>
</svg>
"""

# 2. Ujli Raaten (Fyodor Dostoevsky) - Midnight navy & gold starry classic
svg_ujli_raaten = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="300" height="450">
  <defs>
    <linearGradient id="bgUjli" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B132B"/>
      <stop offset="50%" stop-color="#1C2541"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="starGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#D99B26"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#bgUjli)"/>
  <rect x="0" y="0" width="16" height="450" fill="#000000" opacity="0.4"/>
  <!-- Starlight Constellation Dots -->
  <circle cx="50" cy="80" r="1.5" fill="#FCD34D" opacity="0.7"/>
  <circle cx="100" cy="50" r="2" fill="#FFFFFF" opacity="0.8"/>
  <circle cx="230" cy="70" r="1.5" fill="#FCD34D" opacity="0.6"/>
  <circle cx="260" cy="110" r="2" fill="#FFFFFF" opacity="0.9"/>
  <circle cx="70" cy="280" r="1.5" fill="#FCD34D" opacity="0.5"/>
  <circle cx="240" cy="300" r="2" fill="#FFFFFF" opacity="0.7"/>
  <!-- Border -->
  <rect x="18" y="18" width="264" height="414" fill="none" stroke="url(#starGold)" stroke-width="1.75"/>
  <rect x="23" y="23" width="254" height="404" fill="none" stroke="#FCD34D" stroke-width="0.75" opacity="0.5"/>
  <text x="150" y="55" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="3" fill="#D99B26" font-weight="700">PENGUIN CLASSICS • SWADESH</text>
  <line x1="70" y1="65" x2="230" y2="65" stroke="url(#starGold)" stroke-width="1"/>
  <!-- Moon Crescent -->
  <path d="M150 95 A16 16 0 0 0 162 120 A20 20 0 1 1 150 95 Z" fill="url(#starGold)" opacity="0.4"/>
  <text x="150" y="195" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="34" font-weight="bold" fill="#FFFDF0">उजली रातें</text>
  <text x="150" y="222" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" letter-spacing="4" fill="#FCD34D" font-weight="700">WHITE NIGHTS</text>
  <line x1="90" y1="240" x2="210" y2="240" stroke="url(#starGold)" stroke-width="1.5"/>
  <text x="150" y="265" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" fill="#E2E8F0" opacity="0.85">सपनों के मुसाफ़िर की डायरी से</text>
  <text x="150" y="335" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" letter-spacing="2" fill="#D99B26">विश्व प्रसिद्ध रूसी क्लासिक</text>
  <text x="150" y="360" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="17" font-weight="bold" fill="#FFFFFF">फ्योदोर दोस्तोएव्स्की</text>
  <text x="150" y="410" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="2" fill="#94A3B8">COMPLETE &amp; UNABRIDGED</text>
</svg>
"""

# 3. Diary of a Wimpy Kid: Fight or Flight - Bright illustrated yellow & red hardcover
svg_wimpy_kid = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="300" height="450">
  <defs>
    <linearGradient id="bgWimpy" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FACC15"/>
      <stop offset="100%" stop-color="#EAB308"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#bgWimpy)"/>
  <rect x="0" y="0" width="16" height="450" fill="#000000" opacity="0.25"/>
  <!-- Top Red Banner -->
  <rect x="18" y="24" width="264" height="60" fill="#DC2626" rx="4"/>
  <text x="150" y="48" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" fill="#FFFFFF" letter-spacing="2">DIARY OF A</text>
  <text x="150" y="72" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="900" fill="#FFFFFF" letter-spacing="1">WIMPY KID</text>
  <!-- Book Number Badge -->
  <circle cx="245" cy="54" r="16" fill="#FBBF24" stroke="#DC2626" stroke-width="2"/>
  <text x="245" y="58" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="900" fill="#991B1B">21</text>
  <!-- Ruled Notebook Paper Box in Center -->
  <rect x="30" y="110" width="240" height="200" fill="#FFFFFF" rx="4" stroke="#D1D5DB" stroke-width="2"/>
  <!-- Ruled Lines -->
  <line x1="30" y1="140" x2="270" y2="140" stroke="#E5E7EB" stroke-width="1.5"/>
  <line x1="30" y1="170" x2="270" y2="170" stroke="#E5E7EB" stroke-width="1.5"/>
  <line x1="30" y1="200" x2="270" y2="200" stroke="#E5E7EB" stroke-width="1.5"/>
  <line x1="30" y1="230" x2="270" y2="230" stroke="#E5E7EB" stroke-width="1.5"/>
  <line x1="30" y1="260" x2="270" y2="260" stroke="#E5E7EB" stroke-width="1.5"/>
  <line x1="30" y1="290" x2="270" y2="290" stroke="#E5E7EB" stroke-width="1.5"/>
  <!-- Main Title -->
  <text x="150" y="175" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="900" fill="#0F172A">FIGHT OR</text>
  <text x="150" y="210" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="26" font-weight="900" fill="#DC2626">FLIGHT</text>
  <!-- Cartoon Stick Figure Plane -->
  <path d="M120 250 L180 250 M140 235 L160 250 L140 265 M170 245 L175 240" stroke="#0F172A" stroke-width="3" stroke-linecap="round"/>
  <!-- Author Box -->
  <rect x="50" y="340" width="200" height="42" fill="#0F172A" rx="6"/>
  <text x="150" y="366" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="800" fill="#FACC15">by Jeff Kinney</text>
  <text x="150" y="420" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" fill="#713F12">THE INTERNATIONAL BESTSELLER</text>
</svg>
"""

# 4. Alchemised (SenLinYu) - Obsidian black & antique brass geometric mandala
svg_alchemised = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="300" height="450">
  <defs>
    <linearGradient id="bgAlchemised" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090A0F"/>
      <stop offset="50%" stop-color="#141724"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D99B26"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#bgAlchemised)"/>
  <rect x="0" y="0" width="16" height="450" fill="#000000" opacity="0.45"/>
  <!-- Border -->
  <rect x="18" y="18" width="264" height="414" fill="none" stroke="url(#brassGrad)" stroke-width="1.75"/>
  <rect x="23" y="23" width="254" height="404" fill="none" stroke="#D99B26" stroke-width="0.75" opacity="0.6"/>
  <!-- Alchemical Sacred Geometry Mandala in Center -->
  <g transform="translate(150, 160)" stroke="url(#brassGrad)" stroke-width="1.2" fill="none" opacity="0.6">
    <circle r="60"/>
    <circle r="44"/>
    <polygon points="0,-44 38,22 -38,22"/>
    <polygon points="0,44 38,-22 -38,-22"/>
    <circle r="18" fill="#D99B26" fill-opacity="0.15"/>
  </g>
  <text x="150" y="55" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="3" fill="#D99B26" font-weight="700">COLLECTOR’S HARDCOVER EDITION</text>
  <line x1="70" y1="65" x2="230" y2="65" stroke="url(#brassGrad)" stroke-width="1"/>
  <!-- Main Title -->
  <text x="150" y="270" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="28" font-weight="bold" fill="#F8FAFC" letter-spacing="4">ALCHEMISED</text>
  <line x1="80" y1="285" x2="220" y2="285" stroke="url(#brassGrad)" stroke-width="1.5"/>
  <text x="150" y="310" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" letter-spacing="2" fill="#E2E8F0" opacity="0.8">DARK FANTASY &amp; ROMANCE PHENOMENON</text>
  <!-- Author -->
  <text x="150" y="360" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" letter-spacing="4" fill="#F59E0B" font-weight="800">SENLINYU</text>
  <text x="150" y="415" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="3" fill="#64748B">DELUXE EMBOSSED EDITION</text>
</svg>
"""

# 5. Ratan Tata: A Life (Thomas Mathew) - Executive charcoal slate & gold foil
svg_ratan_tata = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="300" height="450">
  <defs>
    <linearGradient id="bgTata" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="tataGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="50%" stop-color="#D99B26"/>
      <stop offset="100%" stop-color="#FCD34D"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#bgTata)"/>
  <rect x="0" y="0" width="16" height="450" fill="#000000" opacity="0.4"/>
  <!-- Executive Double Frame -->
  <rect x="18" y="18" width="264" height="414" fill="none" stroke="url(#tataGold)" stroke-width="2"/>
  <rect x="23" y="23" width="254" height="404" fill="none" stroke="#D99B26" stroke-width="0.75" opacity="0.6"/>
  <text x="150" y="55" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="3" fill="#D99B26" font-weight="700">HARPERCOLLINS INDIA • BIOGRAPHY</text>
  <line x1="70" y1="65" x2="230" y2="65" stroke="url(#tataGold)" stroke-width="1"/>
  <!-- Minimalist Executive Monogram / Emblem -->
  <circle cx="150" cy="130" r="32" fill="#D99B26" opacity="0.1" stroke="url(#tataGold)" stroke-width="1.5"/>
  <text x="150" y="138" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="24" font-weight="bold" fill="url(#tataGold)">T</text>
  <!-- Main Title -->
  <text x="150" y="215" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="30" font-weight="bold" fill="#FFFFFF" letter-spacing="3">RATAN TATA</text>
  <text x="150" y="242" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" letter-spacing="4" fill="#D99B26" font-weight="700">A  L I F E</text>
  <line x1="90" y1="260" x2="210" y2="260" stroke="url(#tataGold)" stroke-width="1.5"/>
  <text x="150" y="285" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" letter-spacing="2" fill="#E2E8F0" opacity="0.85">THE AUTHORIZED BIOGRAPHY</text>
  <!-- Author -->
  <text x="150" y="345" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" letter-spacing="2" fill="#D99B26">BY</text>
  <text x="150" y="370" text-anchor="middle" font-family="'Libre Baskerville', serif" font-size="17" font-weight="bold" fill="#FFFFFF">DR. THOMAS MATHEW</text>
  <text x="150" y="415" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" letter-spacing="2" fill="#94A3B8">NATIONAL BESTSELLER</text>
</svg>
"""

svg_data_urls = {
    "kasaibada": build_svg_data_url(svg_kasaibada),
    "ujli_raaten": build_svg_data_url(svg_ujli_raaten),
    "wimpy_kid": build_svg_data_url(svg_wimpy_kid),
    "alchemised": build_svg_data_url(svg_alchemised),
    "ratan_tata": build_svg_data_url(svg_ratan_tata)
}

print(f"Generated 5 SVG Hardcover Jackets (sizes: {[len(v) for v in svg_data_urls.values()]})")

# Now update sections/curators-podium.liquid and sections/podium.liquid
for podium_file in ['sections/curators-podium.liquid', 'sections/podium.liquid']:
    if not os.path.exists(podium_file):
        continue
    with open(podium_file, 'r', encoding='utf-8') as f:
        p_code = f.read()

    # 1. Completely delete any unsplash image references
    p_code = re.sub(r'https://images\.unsplash\.com/[^\'"\s>]+', svg_data_urls['kasaibada'], p_code)

    # 2. Inject PODIUM_COVER_SVGS javascript object
    svg_js_object = f"""
<script>
  window.PODIUM_COVER_SVGS = {{
    "wimpy": "{svg_data_urls['wimpy_kid']}",
    "ujli": "{svg_data_urls['ujli_raaten']}",
    "kasaibada": "{svg_data_urls['kasaibada']}",
    "alchemised": "{svg_data_urls['alchemised']}",
    "tata": "{svg_data_urls['ratan_tata']}"
  }};
</script>
"""
    if 'PODIUM_COVER_SVGS' not in p_code:
        p_code = p_code.replace('<script>', svg_js_object + '\n<script>', 1)

    # 3. Replace the 5 initial static flanking and center <img> src attributes with our SVG data URLs
    p_code = re.sub(r'id="flankImg0" src="[^"]*"', f'id="flankImg0" src="{svg_data_urls["wimpy_kid"]}"', p_code)
    p_code = re.sub(r'id="flankImg1" src="[^"]*"', f'id="flankImg1" src="{svg_data_urls["ujli_raaten"]}"', p_code)
    p_code = re.sub(r'id="podium-cover-img" src="[^"]*"', f'id="podium-cover-img" src="{svg_data_urls["kasaibada"]}"', p_code)
    p_code = re.sub(r'id="flankImg3" src="[^"]*"', f'id="flankImg3" src="{svg_data_urls["alchemised"]}"', p_code)
    p_code = re.sub(r'id="flankImg4" src="[^"]*"', f'id="flankImg4" src="{svg_data_urls["ratan_tata"]}"', p_code)

    # 4. Update PODIUM_DATA definitions in javascript to use the 5 exact books requested
    # Book 0: Diary of a Wimpy Kid
    # Book 1: Ujli Raaten
    # Book 2: Kasaibada (Center)
    # Book 3: Alchemised
    # Book 4: Ratan Tata: A Life
    updated_podium_data_js = f"""
const PODIUM_DATA = [
  {{
    id: 'podium-0',
    title: 'Diary of a Wimpy Kid: Fight or Flight',
    author: 'Jeff Kinney',
    rank: '#1 IN CHILDREN FICTION',
    rating: '4.8 (890+ verified reviews)',
    quote: '"First of all, let me get something straight: this is a JOURNAL, not a diary. The hilarious airborne adventures of Greg Heffley continue."',
    excerpt: '"First of all, let me get something straight: this is a JOURNAL, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn\\'t say \\'diary\\' on it."',
    pages: '224 Pages • Hardcover',
    publisher: 'Puffin Books',
    price: '₹399.00',
    mrp: '₹499.00',
    save: '20% OFF',
    coverSvg: window.PODIUM_COVER_SVGS["wimpy"]
  }},
  {{
    id: 'podium-1',
    title: 'उजली रातें (Ujli Raaten)',
    author: 'फ्योदोर दोस्तोएव्स्की (Fyodor Dostoevsky)',
    rank: '#1 IN HINDI TRANSLATION',
    rating: '4.9 (640+ verified reviews)',
    quote: '"सेंट पीटर्सबर्ग की जादुई रातों में एक भावुक स्वप्नदर्शी और नास्तेनका की अमर प्रेम कहानी। मानवीय अकेलेपन की सबसे कोमल गाथा।"',
    excerpt: '"वह एक जादुई रात थी, ऐसी रात जो केवल तभी हो सकती है जब हम युवा हों, प्रिय पाठक। आकाश इतना तारों से भरा था कि उसे देखकर अनायास ही यह पूछने का मन होता था कि क्या ऐसे आकाश के नीचे इतने क्रोधी और अस्थिर लोग रह सकते हैं?"',
    pages: '160 Pages • Hardcover Classic',
    publisher: 'Penguin Swadesh',
    price: '₹220.00',
    mrp: '₹299.00',
    save: '26% OFF',
    coverSvg: window.PODIUM_COVER_SVGS["ujli"]
  }},
  {{
    id: 'podium-2',
    title: 'कसाईबाड़ा (Kasaibada)',
    author: 'मनोज राजन त्रिपाठी (Manoj Rajan Tripathi)',
    rank: '#1 IN CONTEMPORARY FICTION',
    rating: '5.0 (1,120+ verified reviews)',
    quote: '"कसाईबाड़ा सत्ता, समाज और व्यवस्था के वीभत्स सच का वह निर्भीक दस्तावेज है जो हर संवेदनशील पाठक को भीतर तक झकझोर देता है।"',
    excerpt: '"कसाईबाड़ा महज एक जगह का नाम नहीं, यह हमारे समय की उस सड़ांध का रूपक है जिसे सबने देखा मगर बोलने की हिम्मत किसी ने नहीं की। जब व्यवस्था ही कसाई बन जाए, तब अदब को हथियार बनना पड़ता है। यह उसी बगावत का आख्यान है।"',
    pages: '210 Pages • Deluxe Hardcover',
    publisher: 'वाणी प्रकाशन (Vani Prakashan)',
    price: '₹299.00',
    mrp: '₹350.00',
    save: '15% OFF',
    coverSvg: window.PODIUM_COVER_SVGS["kasaibada"]
  }},
  {{
    id: 'podium-3',
    title: 'Alchemised (The Collector Edition)',
    author: 'SenLinYu',
    rank: '#1 IN DARK FANTASY',
    rating: '4.9 (2,450+ verified reviews)',
    quote: '"An intoxicating masterpiece of sacrifice, memory, and redemption woven through intricate alchemical warfare and spellbinding romantic tension."',
    excerpt: '"The war was not lost in the field; it was lost in the quiet corners of minds that had forgotten what light felt like. She touched the bruised parchment, tracing the brass alchemical circles that whispered of old magic and dangerous debts."',
    pages: '480 Pages • Foil Embossed Hardcover',
    publisher: 'Collector Imprint',
    price: '₹599.00',
    mrp: '₹799.00',
    save: '25% OFF',
    coverSvg: window.PODIUM_COVER_SVGS["alchemised"]
  }},
  {{
    id: 'podium-4',
    title: 'Ratan Tata: A Life',
    author: 'Dr. Thomas Mathew',
    rank: '#1 IN BUSINESS & BIOGRAPHY',
    rating: '4.9 (1,890+ verified reviews)',
    quote: '"The definitive authorized biography of India\\'s most revered industrialist, visionary philanthropist, and symbol of ethical leadership."',
    excerpt: '"\\'I do not believe in taking right decisions. I take decisions and then make them right.\\' From the historic corridors of Bombay House to the global acquisition of Jaguar Land Rover, this is the unvarnished story of quiet resilience."',
    pages: '560 Pages • Executive Hardcover',
    publisher: 'HarperCollins India',
    price: '₹799.00',
    mrp: '₹999.00',
    save: '20% OFF',
    coverSvg: window.PODIUM_COVER_SVGS["tata"]
  }}
];
"""
    # Replace PODIUM_DATA block in file
    p_code = re.sub(r'const PODIUM_DATA = \[.*?\];', updated_podium_data_js.strip(), p_code, flags=re.DOTALL)

    # 5. Update selectPodiumBook in javascript to strictly use book.coverSvg
    cover_update_code = """
  // 1. Update 3D Book Cover & Inside Page
  const elCoverImg = document.getElementById('podium-cover-img');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  if (elCoverImg) {
    elCoverImg.src = book.coverSvg;
    elCoverImg.alt = book.title;
  }
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.excerpt;

  // Reset cover open state when changing books
  if (el3dBook) el3dBook.classList.remove('is-open');

  // 2. Update Flanking Books Around Active Index
  const slotIndices = [
    (index + 3) % 5, // Far left
    (index + 4) % 5, // Near left
    (index + 1) % 5, // Near right
    (index + 2) % 5  // Far right
  ];

  const elFlank0 = document.getElementById('flankImg0');
  const elFlank1 = document.getElementById('flankImg1');
  const elFlank3 = document.getElementById('flankImg3');
  const elFlank4 = document.getElementById('flankImg4');

  if (elFlank0) elFlank0.src = PODIUM_DATA[slotIndices[0]].coverSvg;
  if (elFlank1) elFlank1.src = PODIUM_DATA[slotIndices[1]].coverSvg;
  if (elFlank3) elFlank3.src = PODIUM_DATA[slotIndices[2]].coverSvg;
  if (elFlank4) elFlank4.src = PODIUM_DATA[slotIndices[3]].coverSvg;
"""
    p_code = re.sub(
        r'// 1\. Update 3D Book Cover & Inside Page.*?if \(elFlank4\) elFlank4\.src = [^;]+;',
        cover_update_code.strip(),
        p_code,
        flags=re.DOTALL
    )

    # 6. Replace bubbly pill badge above section title with architectural hairline overline
    p_code = re.sub(
        r'<div class="inline-flex items-center gap-2 bg-amber-100.*?<span>{{ section\.settings\.badge[^<]+</span>\s*</div>',
        """<div class="editorial-overline">
        <span class="editorial-overline__line"></span>
        <span class="editorial-overline__text">{{ section.settings.badge | default: 'CURATOR’S CHOICE & NATIONAL BESTSELLERS' }}</span>
        <span class="editorial-overline__line"></span>
      </div>""",
        p_code,
        flags=re.DOTALL
    )

    with open(podium_file, 'w', encoding='utf-8') as f:
        f.write(p_code)
    print(f"SUCCESS: {podium_file} updated with 5 vector hardcover jackets and hairline overline.")


# =========================================================================
# STEP 7: PURGE ALL EMOJIS & REPLACE WITH LUCIDE ICONS ACROSS THE ENTIRE REPO
# =========================================================================
print("\n[Step 7] Purging all Unicode emojis across the codebase and replacing with Lucide icons...")

# Direct file replacements for sections with known emojis
def replace_emojis_in_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    orig = c
    # Purge common emojis
    c = c.replace('📞', '<i data-lucide="phone"></i>')
    c = c.replace('✉️', '<i data-lucide="mail"></i>')
    c = c.replace('📍', '<i data-lucide="map-pin"></i>')
    c = c.replace('💬', '<i data-lucide="message-circle"></i>')
    c = c.replace('🔥', '<i data-lucide="trending-up"></i>')
    c = c.replace('🔒', '<i data-lucide="shield-check"></i>')
    c = c.replace('⚡', '<i data-lucide="zap"></i>')
    c = c.replace('📖', '<i data-lucide="book-open"></i>')
    c = c.replace('⚖️', '<i data-lucide="scale"></i>')
    c = c.replace('🏛️', '<i data-lucide="landmark"></i>')
    c = c.replace('🎓', '<i data-lucide="graduation-cap"></i>')
    c = c.replace('🌍', '<i data-lucide="compass"></i>')
    c = c.replace('✨', '')
    c = c.replace('✦', '•')
    c = c.replace('📜', '<i data-lucide="feather"></i>')
    c = c.replace('🌸', '<i data-lucide="heart"></i>')
    c = c.replace('🌲', '<i data-lucide="trees"></i>')
    c = c.replace('📦', '<i data-lucide="package"></i>')
    c = c.replace('🎨', '<i data-lucide="palette"></i>')
    c = c.replace('📌', '<i data-lucide="bookmark"></i>')
    c = c.replace('🎯', '<i data-lucide="target"></i>')
    c = c.replace('📚', '')
    c = c.replace('★★★★★', '<span class="rating-stars" style="color: #f59e0b; display: inline-flex; align-items: center; gap: 1px;"><i data-lucide="star" style="width: 13px; height: 13px; fill: #f59e0b;"></i><i data-lucide="star" style="width: 13px; height: 13px; fill: #f59e0b;"></i><i data-lucide="star" style="width: 13px; height: 13px; fill: #f59e0b;"></i><i data-lucide="star" style="width: 13px; height: 13px; fill: #f59e0b;"></i><i data-lucide="star" style="width: 13px; height: 13px; fill: #f59e0b;"></i></span>')

    if c != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"SUCCESS: Purged emojis in {filepath}")

all_target_files = [
    'sections/academic-vault.liquid',
    'sections/bestsellers-bundles.liquid',
    'sections/bundle-unboxing.liquid',
    'sections/cart-drawer-section.liquid',
    'sections/catalog-directory.liquid',
    'sections/collection-links.liquid',
    'sections/curators-podium.liquid',
    'sections/podium.liquid',
    'sections/footer.liquid',
    'sections/header-announcements.liquid',
    'sections/literary-marquee.liquid',
    'sections/marquee.liquid',
    'sections/mehfil-rekhta.liquid',
    'sections/product-information.liquid',
    'sections/quick-order-list.liquid',
    'sections/regional-magazine.liquid',
    'sections/product-list.liquid',
    'snippets/curated-book-item.liquid',
    'snippets/product-card.liquid',
    'snippets/quick-view-modal.liquid',
    'snippets/whatsapp-button.liquid',
    'assets/theme.js',
    'assets/whatsapp-commerce.js',
    'config/settings_data.json'
]

for tf in all_target_files:
    replace_emojis_in_file(tf)


# =========================================================================
# STEP 8: REPLACE BUBBLY PILL BADGES WITH ARCHITECTURAL HAIRLINE OVERLINES
# =========================================================================
print("\n[Step 8] Replacing bubbly pill badges with architectural hairline overlines...")

# 1. sections/bundle-unboxing.liquid
with open('sections/bundle-unboxing.liquid', 'r', encoding='utf-8') as f:
    bu = f.read()
bu = re.sub(
    r'<div class="inline-flex items-center gap-2 bg-amber-200/70.*?<span>{{ section\.settings\.badge[^<]+</span>\s*</div>',
    """<div class="editorial-overline">
        <span class="editorial-overline__line"></span>
        <span class="editorial-overline__text">{{ section.settings.badge | default: "COLLECTOR'S CORNER & BOX SETS" }}</span>
        <span class="editorial-overline__line"></span>
      </div>""",
    bu,
    flags=re.DOTALL
)
with open('sections/bundle-unboxing.liquid', 'w', encoding='utf-8') as f:
    f.write(bu)
print("SUCCESS: Architectural hairline overline applied to bundle-unboxing.liquid")

# 2. sections/academic-vault.liquid
with open('sections/academic-vault.liquid', 'r', encoding='utf-8') as f:
    av = f.read()
av = re.sub(
    r'<div class="inline-flex items-center gap-2 bg-slate-100.*?<span>ACADEMIC &amp; SCHOLARLY VAULT</span>\s*</div>',
    """<div class="editorial-overline">
        <span class="editorial-overline__line"></span>
        <span class="editorial-overline__text">ACADEMIC &amp; SCHOLARLY VAULT</span>
        <span class="editorial-overline__line"></span>
      </div>""",
    av,
    flags=re.DOTALL
)
with open('sections/academic-vault.liquid', 'w', encoding='utf-8') as f:
    f.write(av)
print("SUCCESS: Architectural hairline overline applied to academic-vault.liquid")

# 3. sections/mehfil-rekhta.liquid
with open('sections/mehfil-rekhta.liquid', 'r', encoding='utf-8') as f:
    mr = f.read()
mr = re.sub(
    r'<div class="inline-flex items-center gap-2 bg-amber-900/40.*?</div>',
    """<div class="editorial-overline editorial-overline--dark">
        <span class="editorial-overline__line"></span>
        <span class="editorial-overline__text">महेफ़िल-ए-रेख़्ख़ता • MEHFIL-E-REKHTA</span>
        <span class="editorial-overline__line"></span>
      </div>""",
    mr,
    count=1,
    flags=re.DOTALL
)
with open('sections/mehfil-rekhta.liquid', 'w', encoding='utf-8') as f:
    f.write(mr)
print("SUCCESS: Architectural hairline overline applied to mehfil-rekhta.liquid")

# 4. sections/regional-magazine.liquid
with open('sections/regional-magazine.liquid', 'r', encoding='utf-8') as f:
    rm = f.read()
rm = re.sub(
    r'<div class="inline-flex items-center gap-2 bg-amber-100.*?<span>LITERARY SPOTLIGHT[^<]*</span>\s*</div>',
    """<div class="editorial-overline" style="justify-content: flex-start;">
          <span class="editorial-overline__line"></span>
          <span class="editorial-overline__text">LITERARY SPOTLIGHT • REGIONAL CLASSICS</span>
        </div>""",
    rm,
    flags=re.DOTALL
)
with open('sections/regional-magazine.liquid', 'w', encoding='utf-8') as f:
    f.write(rm)
print("SUCCESS: Architectural hairline overline applied to regional-magazine.liquid")


# =========================================================================
# STEP 9: REPACK indigo-books-theme.zip
# =========================================================================
print("\n[Step 9] Packaging polished theme into indigo-books-theme.zip...")
os.system("python package_theme_zip.py")
print("=== DE-AI POLISH & REPAIR COMPLETED SUCCESSFULLY ===")

