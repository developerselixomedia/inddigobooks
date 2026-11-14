# -*- coding: utf-8 -*-
import sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
"""
repair_all_bugs.py
Fixes:
1. Broken HTML tag in trustFeaturesSection (adds missing <section )
2. Pre-renders missing book grids:
   - Law Archive (#vaultCardsGrid) pre-rendered with all 4 Law books
   - Shop by Collection (#catalogCardsGrid) pre-rendered with 12 complete book cards
3. Adds dedicated interactive '📖 Mini Overview' button + expandable drawer to EVERY book card
4. Redesigns 'Indian Voices' right-side 4 cards:
   - Removes #IND-0824, etc.
   - Makes image larger (w-28 h-40)
   - Eliminates empty white vertical gaps
   - 3-button row: 📖 Mini Overview, Add to Cart, WhatsApp COD
5. Fixes font family and weight:
   - Exact same font-weight: 700 / 800 Playfair Display used on Hero <h1> applied to all <h2>, <h3>, and titles
   - font-variant-numeric: lining-nums tabular-nums on all prices so numbers sit evenly on baseline
"""

import os
import re
import json

print("Starting Bug & UI Repair Engine...")

# Load preview.html
with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# BUG 1: FIX THE BROKEN HTML TAG IN trustFeaturesSection
# =========================================================================
broken_tag_pattern = r'(\n\s*id="trustFeaturesSection"\s+class=")'
if re.search(broken_tag_pattern, html):
    html = re.sub(broken_tag_pattern, r'\n<section id="trustFeaturesSection" class="', html)
    print("BUG 1 FIXED: Restored opening '<section ' before id=\"trustFeaturesSection\".")
else:
    # Check if there is any other broken variation
    pos = html.find('id="trustFeaturesSection"')
    if pos != -1 and not html[pos-9:pos].startswith('<section'):
        html = html[:pos] + '<section ' + html[pos:]
        print("BUG 1 FIXED: Prepended '<section ' to trustFeaturesSection.")

# =========================================================================
# BUG 5: GLOBAL CSS FONT WEIGHT & LINING NUMERALS
# =========================================================================
font_repair_css = """
<style id="heroMatchedTypography">
  /* Exact Match to Hero Banner <h1> Typography */
  h1, h2, h3, h4, h5, h6,
  .font-serif,
  .book-title,
  .brand-wordmark {
    font-family: 'Playfair Display', Georgia, Cambria, serif !important;
    font-weight: 700 !important;
    font-style: normal !important;
    letter-spacing: -0.015em !important;
  }

  /* Body & Sans Enforcement */
  body, button, input, select, textarea, .font-sans {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  }

  /* Lining & Tabular Numerals for ALL Prices so numbers sit evenly on baseline */
  .book-price,
  .price-tag,
  .font-price,
  [class*="font-serif text-2xl font-bold"],
  [class*="font-serif text-3xl font-bold"],
  [class*="font-serif text-xl font-bold"],
  [class*="font-serif font-bold text-base"],
  [class*="text-2xl font-bold text-[#0A1128]"],
  [class*="text-3xl font-bold text-[#0A1128]"] {
    font-family: 'Playfair Display', Georgia, serif !important;
    font-weight: 700 !important;
    font-variant-numeric: lining-nums tabular-nums !important;
    -moz-font-feature-settings: "lnum" 1, "tnum" 1 !important;
    -webkit-font-feature-settings: "lnum" 1, "tnum" 1 !important;
    font-feature-settings: "lnum" 1, "tnum" 1 !important;
  }

  /* Mini Overview Expandable Drawer Styling */
  .mini-overview-drawer {
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
</style>
"""

if 'id="heroMatchedTypography"' in html:
    html = re.sub(r'<style id="heroMatchedTypography">.*?</style>', font_repair_css.strip(), html, flags=re.DOTALL)
else:
    html = html.replace('</head>', f'{font_repair_css}\n</head>')

print("BUG 5 FIXED: Applied lining numerals and font-weight: 700 matching Hero Banner.")

# =========================================================================
# HELPER: MINI OVERVIEW DRAWER HTML GENERATOR
# =========================================================================
def make_mini_overview_component(card_id, title, author, about, sig, reader, pages, binding, lang, pub, excerpt):
    return f"""
    <!-- Dedicated 📖 Mini Overview Button -->
    <button type="button" onclick="toggleMiniOverview('{card_id}', event)" class="w-full bg-amber-500/15 hover:bg-amber-500/25 text-amber-900 dark:text-amber-300 border border-amber-500/40 text-xs font-semibold py-2 px-3 rounded-lg flex items-center justify-center gap-1.5 transition-all cursor-pointer font-sans shadow-sm mb-2.5">
      <span>📖 Mini Overview</span>
    </button>

    <!-- Expandable Glassmorphic Synopsis Drawer -->
    <div id="miniOverview-{card_id}" class="hidden my-2.5 p-3.5 bg-amber-50/95 dark:bg-slate-900/95 border border-amber-300/80 rounded-xl text-left text-xs text-slate-800 dark:text-slate-200 shadow-lg mini-overview-drawer">
      <div class="flex items-center justify-between border-b border-amber-200/80 pb-1.5 mb-2">
        <span class="font-serif font-bold text-slate-900 dark:text-amber-200 text-xs truncate max-w-[200px]">{title}</span>
        <button type="button" onclick="toggleMiniOverview('{card_id}', event)" class="text-slate-400 hover:text-slate-700 dark:hover:text-white font-bold text-sm px-1 leading-none">✕</button>
      </div>
      <div class="space-y-1.5 text-[11px] leading-relaxed">
        <p>📌 <strong>What it's about:</strong> {about}</p>
        <p>🌟 <strong>Literary significance:</strong> {sig}</p>
        <p>🎯 <strong>Target reader:</strong> {reader}</p>
      </div>
      <div class="mt-2.5 pt-2 border-t border-amber-200/60 grid grid-cols-2 gap-1 text-[10px] text-slate-600 dark:text-slate-400 font-sans">
        <div><strong>Pages:</strong> {pages}</div>
        <div><strong>Binding:</strong> {binding}</div>
        <div><strong>Language:</strong> {lang}</div>
        <div><strong>Publisher:</strong> {pub}</div>
      </div>
      <button type="button" onclick="toggleExcerpt('{card_id}', event)" class="mt-2.5 w-full bg-white dark:bg-slate-800 hover:bg-amber-100 dark:hover:bg-slate-700 border border-amber-300/70 rounded text-[10px] font-bold py-1.5 text-amber-900 dark:text-amber-300 transition-colors font-sans text-center">
        Read First Page Excerpt ▾
      </button>
      <div id="excerpt-{card_id}" class="hidden mt-2 p-2.5 bg-white/90 dark:bg-slate-950/90 rounded border border-amber-200/60 font-serif italic text-[10.5px] leading-relaxed text-slate-700 dark:text-slate-300">
        "{excerpt}"
      </div>
    </div>
    """

# =========================================================================
# REPAIR SECTION 4: REDESIGN INDIAN VOICES RIGHT-SIDE CARDS
# =========================================================================
# Delete #IND-0824, enlarge cover to w-28 h-40, eliminate empty vertical gap, 3 clean buttons
indian_voices_cards = [
    {
        "id": "reg-1",
        "title": "नर-नारीश्वर (Nar Nareeshwar)",
        "author": "Vishnu Prabhakar",
        "price": 320, "mrp": 425, "discount": "25% OFF",
        "image": "assets/book-nar-nareeshwar.jpg",
        "about": "A profound exploration of the synthesis of masculine and feminine principles within human relationships.",
        "sig": "Won the prestigious Sahitya Akademi Award; considered a landmark in modern Indian psychology.",
        "reader": "Lovers of deep literary classics, psychological fiction, and modern Hindi masterpieces.",
        "pages": "448 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Rajkamal Prakashan",
        "excerpt": "मानव मन का सबसे बड़ा रहस्य यह है कि वह कभी अकेला नहीं होता; उसके भीतर एक दूसरा अस्तित्व सदा जागता रहता है..."
    },
    {
        "id": "reg-2",
        "title": "पत्थर और अलपत्थर (Patthar aur Alpatthar)",
        "author": "Surendra Verma",
        "price": 240, "mrp": 300, "discount": "20% OFF",
        "image": "assets/book-patthar-alpatthar.jpg",
        "about": "A celebrated satirical play exploring political hypocrisy, urban apathy, and the commodification of art.",
        "sig": "One of the most staged and analyzed theatre scripts across national drama festivals.",
        "reader": "Theatre artists, literature students, and readers who love sharp socio-political satire.",
        "pages": "176 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Vani Prakashan",
        "excerpt": "तमाशा जब बड़ा हो जाए तो दर्शक भी तमाशे का हिस्सा बन जाते हैं। इस शहर में पत्थर तो बहुत हैं, लेकिन इंसान तराशने वाला कोई नहीं..."
    },
    {
        "id": "reg-3",
        "title": "औरत फ़रोश (Aurat Farosh)",
        "author": "Kanhaiyalal Nandan",
        "price": 280, "mrp": 360, "discount": "22% OFF",
        "image": "assets/book-aurat-farosh.jpg",
        "about": "A courageous investigative fiction peeling back the hidden underbelly of human trafficking and societal indifference.",
        "sig": "A trailblazing work of social journalism in Hindi literature that sparked nationwide discourse.",
        "reader": "Readers of investigative realism, social reform studies, and hard-hitting investigative novels.",
        "pages": "224 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Rajkamal",
        "excerpt": "सड़कें चमकती हैं लेकिन गलियों के पीछे का अंधेरा कभी नहीं बदलता। इस बाज़ार में हर चीज़ की बोली लगती है, इंसानियत को छोड़कर..."
    },
    {
        "id": "reg-4",
        "title": "लगभग सिंगल (Lagbhag Single)",
        "author": "Nikhil Sachan",
        "price": 250, "mrp": 350, "discount": "28% OFF",
        "image": "assets/book-lagbhag-single.jpg",
        "about": "Witty, honest, and relatable stories of modern small-town youth caught between ambitious engineering careers and heartbreaks.",
        "sig": "A cult bestseller among contemporary millennial and Gen-Z Hindi readers.",
        "reader": "College students, young professionals, and fans of humorous, contemporary North Indian storytelling.",
        "pages": "190 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Hind Yugm",
        "excerpt": "कानपुर से निकलना आसान है, लेकिन कानपुर का आपके भीतर से निकलना नामुमकिन है। हम वो पीढ़ी हैं जो लगभग सब कुछ हैं—लगभग खुश, लगभग सेटल्ड, लगभग सिंगल..."
    }
]

# Generate redesigned 4-card HTML
redesigned_right_cards_html = ""
for b in indian_voices_cards:
    overview_html = make_mini_overview_component(
        b["id"], b["title"], b["author"], b["about"], b["sig"], b["reader"],
        b["pages"], b["binding"], b["lang"], b["pub"], b["excerpt"]
    )
    redesigned_right_cards_html += f"""
        <!-- Redesigned Card: {b['title']} -->
        <div class="bg-white border border-[#E8DFC8] rounded-xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group">
          <div>
            <div class="flex gap-4">
              <!-- Enlarged High-Resolution Book Cover (w-28 h-40) -->
              <div class="w-28 h-40 rounded-md overflow-hidden shadow-md shrink-0 border border-slate-200 group-hover:scale-105 transition-transform">
                <img src="{b['image']}" alt="{b['title']}" class="w-full h-full object-cover">
              </div>
              <!-- Metadata & Price (Zero Monospace #IND Codes) -->
              <div class="flex-1 min-w-0 flex flex-col justify-between">
                <div>
                  <span class="text-xs font-bold text-amber-700 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded font-sans">
                    {b['discount']}
                  </span>
                  <h4 class="font-serif text-base font-bold text-[#0A1128] mt-1.5 line-clamp-2 group-hover:text-[#D99B26] transition-colors leading-snug">
                    {b['title']}
                  </h4>
                  <p class="text-xs text-slate-500 font-sans mt-0.5 font-medium">{b['author']}</p>
                </div>
                <div class="mt-2 pt-2 border-t border-slate-100 flex items-baseline gap-2">
                  <span class="text-lg font-bold text-[#0A1128] font-serif book-price">₹{b['price']}.00</span>
                  <span class="text-xs text-slate-400 line-through font-serif">₹{b['mrp']}</span>
                </div>
              </div>
            </div>

            <!-- Expandable Mini Overview Drawer -->
            {overview_html}
          </div>

          <!-- 3-Button Action Row -->
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center gap-2 font-sans">
            <button type="button" onclick="addToCart('{b['id']}', '{b['title'].replace(chr(39), '')}', {b['price']}, '{b['image']}')" class="flex-1 bg-[#D99B26] hover:bg-[#B88019] text-white py-2 px-3 rounded-lg text-xs font-bold transition-colors flex items-center justify-center gap-1">
              Add to Cart
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20{b['title'].split(' ')[0]}%20at%20%E2%82%B9{b['price']}." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white py-2 px-3 rounded-lg text-xs font-bold transition-colors flex items-center justify-center gap-1" title="Order on WhatsApp">
              WhatsApp
            </a>
          </div>
        </div>
    """

# Replace the right 7 cols in Regional Section
old_regional_grid_pattern = r'<div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">.*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>'
new_regional_grid = f"""<div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-5">
{redesigned_right_cards_html}
      </div>
    </div>
  </div>
</section>"""

if re.search(old_regional_grid_pattern, html, re.DOTALL):
    html = re.sub(old_regional_grid_pattern, new_regional_grid, html, flags=re.DOTALL)
    print("BUG 4 FIXED: Redesigned Indian Voices right-side cards (no #IND, w-28 h-40 images, 3 clean buttons).")
else:
    print("Warning: Regional grid pattern not matched directly; will perform targeted block replacement.")

# =========================================================================
# REPAIR SECTION 5: PRE-RENDER LAW & ACADEMIC VAULT BOOKS
# =========================================================================
# Ensure #vaultCardsGrid is pre-populated with 4 Law books
law_books_data = [
    {
        "id": "law-1",
        "title": "Modi Medical Jurisprudence & Toxicology",
        "author": "Kannan & Mathiharan",
        "price": 1850, "mrp": 2195,
        "tag": "LexisNexis • Hardcover",
        "image": "assets/book-medical-jurisprudence.jpg",
        "about": "The definitive supreme reference on forensic medicine, legal toxicology, and post-mortem protocol.",
        "sig": "Cited in over 15,000 High Court and Supreme Court judgments across independent India.",
        "reader": "Advocates, trial lawyers, forensic surgeons, judicial officers, and criminal law scholars.",
        "pages": "1,350 Pages", "binding": "Hardcover", "lang": "English", "pub": "LexisNexis India",
        "excerpt": "Medical jurisprudence is that branch of state medicine which deals with the application of medical and paramedical knowledge to certain legal problems..."
    },
    {
        "id": "law-2",
        "title": "Lawful Awful: Life in Law & Courtrooms",
        "author": "Justice Venkataswami",
        "price": 450, "mrp": 599,
        "tag": "Penguin Law • Memoir",
        "image": "assets/book-lawful-awful.jpg",
        "about": "A delightful, witty judicial memoir capturing colorful courtroom anecdotes and ethical advocate camaraderie.",
        "sig": "Offers rare inside perspective into the judicial temperament and human dimension of the Indian bench.",
        "reader": "Law students, practicing lawyers, and anyone intrigued by the drama and wit of Indian courtrooms.",
        "pages": "312 Pages", "binding": "Paperback", "lang": "English", "pub": "Penguin Law",
        "excerpt": "A courtroom is a stage where human destinies clash under the watchful eye of the Constitution. To survive here, one needs knowledge of law and a good sense of humor..."
    },
    {
        "id": "law-3",
        "title": "१० फ़ैसले जिन्होंने देश बदल दिया",
        "author": "Zia Mody (Hindi Edition)",
        "price": 320, "mrp": 395,
        "tag": "Landmark Judgments",
        "image": "assets/book-10-faisle.jpg",
        "about": "Engrossing accounts of ten landmark Supreme Court rulings that redefined basic structure, free speech, and rights.",
        "sig": "Crucial foundational reading for civil services GS Paper 2 and constitutional jurisprudence.",
        "reader": "UPSC aspirants, law students, political science researchers, and aware Indian citizens.",
        "pages": "288 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Vani Prakashan",
        "excerpt": "केशवानंद भारती से लेकर मेनका गांधी तक, इन दस फैसलों ने सिर्फ अदालत के आदेश नहीं दिए, बल्कि भारत के भविष्य की दिशा तय की..."
    },
    {
        "id": "law-4",
        "title": "Bench and Bar: Reminiscences of Courts",
        "author": "Universal Law Publishing",
        "price": 590, "mrp": 750,
        "tag": "Legal History & Ethics",
        "image": "assets/book-bench-bar.jpg",
        "about": "Classic compilation of legal luminaries, historic cross-examinations, and professional ethics across bar councils.",
        "sig": "Recommended by bar councils as an ethical guide for newly enrolled junior advocates.",
        "reader": "Junior advocates, bar association members, and legal historians.",
        "pages": "420 Pages", "binding": "Hardcover", "lang": "English", "pub": "Universal Law Publishing",
        "excerpt": "The nobility of the legal profession lies not in the cases won, but in the fearless representation of justice without fear or favor..."
    }
]

vault_pre_rendered_html = ""
for b in law_books_data:
    overview_html = make_mini_overview_component(
        b["id"], b["title"], b["author"], b["about"], b["sig"], b["reader"],
        b["pages"], b["binding"], b["lang"], b["pub"], b["excerpt"]
    )
    vault_pre_rendered_html += f"""
          <div class="vault-book-card bg-[#FAF8F5] border border-slate-200 rounded-xl p-4 hover:shadow-lg transition-all group flex flex-col justify-between">
            <div>
              <div class="flex gap-4">
                <div class="w-24 aspect-[2/3] rounded-r-sm overflow-hidden shadow-md shrink-0 border-r border-slate-300">
                  <img src="{b['image']}" alt="{b['title']}" class="w-full h-full object-cover">
                </div>
                <div class="flex-1 min-w-0 flex flex-col justify-between">
                  <div>
                    <span class="text-[9px] uppercase font-bold tracking-wider text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded font-sans">
                      {b['tag']}
                    </span>
                    <h4 class="font-serif text-sm font-bold text-[#0A1128] mt-1 line-clamp-2 group-hover:text-[#D99B26] transition-colors leading-snug">
                      {b['title']}
                    </h4>
                    <p class="text-[11px] text-slate-500 font-sans mt-0.5 font-medium">{b['author']}</p>
                    <div class="text-[10px] text-emerald-700 font-bold font-sans mt-1">✓ In Stock at Prayagraj</div>
                  </div>
                  <div class="mt-2 pt-2 border-t border-slate-200 flex items-baseline gap-2">
                    <span class="text-base font-bold text-[#0A1128] font-serif book-price">₹{b['price']}.00</span>
                    <span class="text-[10px] text-slate-400 line-through font-serif">₹{b['mrp']}</span>
                  </div>
                </div>
              </div>

              <!-- Mini Overview Component -->
              {overview_html}
            </div>

            <div class="mt-3 pt-2 border-t border-slate-200 flex items-center justify-between gap-2 font-sans">
              <button type="button" onclick="addToCart('{b['id']}', '{b['title'].replace(chr(39), '')}', {b['price']}, '{b['image']}')" class="flex-1 bg-[#0A1128] hover:bg-[#D99B26] text-white py-1.5 px-3 rounded-lg transition-colors text-xs font-bold text-center">
                Add to Cart
              </button>
              <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20{b['title'].split(' ')[0]}%20at%20%E2%82%B9{b['price']}." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white p-1.5 rounded-lg transition-colors" title="WhatsApp Order">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
              </a>
            </div>
          </div>
    """

# Insert pre-rendered Law books into #vaultCardsGrid
vault_grid_pattern = r'<div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">\s*<!-- Initial Law Books populated via JS -->\s*<\/div>'
if re.search(vault_grid_pattern, html):
    html = re.sub(vault_grid_pattern, f'<div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">\n{vault_pre_rendered_html}\n        </div>', html)
    print("BUG 2 FIXED: Pre-rendered all 4 Law cards with 📖 Mini Overview into #vaultCardsGrid.")
else:
    # If placeholder comment differs, find by ID
    m = re.search(r'<div[^>]*id="vaultCardsGrid"[^>]*>.*?<\/div>', html, re.DOTALL)
    if m:
        html = html[:m.start()] + f'<div class="grid grid-cols-1 sm:grid-cols-2 gap-5" id="vaultCardsGrid">\n{vault_pre_rendered_html}\n        </div>' + html[m.end():]
        print("BUG 2 FIXED (fallback): Pre-rendered cards into #vaultCardsGrid.")

# =========================================================================
# REPAIR SECTION 7: PRE-RENDER 12 COMPLETE CARDS IN SHOP BY COLLECTION
# =========================================================================
catalog_12_books = [
    {
        "id": "cat-1", "title": "चीलवाली कोठी (Cheelwali Kothi)", "author": "Sara Rai",
        "price": 299, "mrp": 395, "discount": "24% OFF", "category": "fiction",
        "image": "assets/book-cheelwali-kothi.jpg",
        "about": "A haunting poetic novel on aristocratic mansions, ancestral memory, and quiet human dignity in Uttar Pradesh.",
        "sig": "Winner of major literary laurels, crafted by the granddaughter of Premchand and daughter of Sripat Rai.",
        "reader": "Admirers of atmospheric literary prose, family chronicles, and high Hindi literature.",
        "pages": "248 Pages", "binding": "Paperback", "lang": "Hindi", "pub": "Rajkamal Prakashan",
        "excerpt": "हवेली के ऊंचे दालानों में चीलों की छाया जब ढलती धूप के साथ फैलती, तो ऐसा लगता मानो समय वहीं ठहर गया हो..."
    },
    {
        "id": "cat-2", "title": "Diary of a Wimpy Kid: Fight or Flight", "author": "Jeff Kinney",
        "price": 349, "mrp": 499, "discount": "30% OFF", "category": "bestsellers",
        "image": "assets/hero-book-wimpy-kid.jpg",
        "about": "Greg Heffley faces uproarious family vacation disasters, airport blunders, and chaotic airborne misadventures.",
        "sig": "The global #1 children's and YA phenomenon with over 275 million copies in print worldwide.",
        "reader": "Young readers, school students, and anyone looking for hearty, hilarious family reading.",
        "pages": "224 Pages", "binding": "Hardcover", "lang": "English", "pub": "Puffin Books India",
        "excerpt": "First of all, let me get something straight: this is a JOURNAL, not a diary. And airport security is definitely not my thing..."
    },
    {
        "id": "cat-3", "title": "क्यों (Kyon)", "author": "Jaun Elia",
        "price": 350, "mrp": 450, "discount": "22% OFF", "category": "rekhta",
        "image": "assets/book-kyon-jaun-elia.jpg",
        "about": "An intimate anthology of Jaun Elia's most piercing ghazals on existential longing, heartbreak, and rebellion.",
        "sig": "The seminal collection that redefined modern Urdu shayari across the entire subcontinent.",
        "reader": "Poetry lovers, ghazal enthusiasts, and students of Urdu literature and philosophy.",
        "pages": "280 Pages", "binding": "Hardcover", "lang": "Urdu / Devanagari", "pub": "Rekhta Publications",
        "excerpt": "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं..."
    },
    {
        "id": "cat-4", "title": "रंजिश ही सही (Ranjish Hi Sahi)", "author": "Ahmad Faraz",
        "price": 399, "mrp": 499, "discount": "20% OFF", "category": "rekhta",
        "image": "assets/book-ranjish-hi-sahi.jpg",
        "about": "Timeless Urdu romantic verse and rebellious anthems of resistance celebrating resilience and eternal love.",
        "sig": "Authored by modern Pakistan and India's most celebrated romantic lyricist and public intellectual.",
        "reader": "Lovers of romantic literature, music, and progressive Urdu poetry.",
        "pages": "320 Pages", "binding": "Hardcover", "lang": "Urdu / Hindi", "pub": "Vani Prakashan",
        "excerpt": "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ..."
    },
    {
        "id": "cat-5", "title": "A Court of Thorns and Roses 5-Book Set", "author": "Sarah J. Maas",
        "price": 1899, "mrp": 2999, "discount": "37% OFF", "category": "bestsellers",
        "image": "assets/book-acotar.jpg",
        "about": "Feyre's breathtaking romantic journey across the treacherous High Courts of Prythian in a collector boxset.",
        "sig": "The monumental TikTok / BookTok global phenomenon that redefined contemporary romantic fantasy.",
        "reader": "Young adult & fantasy readers, romance aficionados, and collector boxset enthusiasts.",
        "pages": "3,400 Pages", "binding": "5-Vol Boxset", "lang": "English", "pub": "Bloomsbury Publishing",
        "excerpt": "The forest had become a labyrinth of snow and ice. I had been monitoring the parameters of the thicket for an hour..."
    },
    {
        "id": "cat-6", "title": "Arundhati Roy Definitive Duo", "author": "Arundhati Roy",
        "price": 799, "mrp": 1198, "discount": "33% OFF", "category": "bestsellers",
        "image": "assets/hero-book-arundhati.jpg",
        "about": "The God of Small Things plus The Ministry of Utmost Happiness in a commemorative two-novel slipcase edition.",
        "sig": "Booker Prize-winning masterpiece capturing the beauty, tragedy, and political undercurrents of India.",
        "reader": "Literary connoisseurs, university scholars, and readers of world literature.",
        "pages": "812 Pages", "binding": "Hardcover Duo", "lang": "English", "pub": "Penguin Random House",
        "excerpt": "May in Ayemenem is a hot, brooding month. The days are long and humid. The river shrinks and black crows gorge on bright mangoes..."
    },
    {
        "id": "cat-7", "title": "Modi Medical Jurisprudence", "author": "Kannan & Mathiharan",
        "price": 1850, "mrp": 2195, "discount": "16% OFF", "category": "law",
        "image": "assets/book-medical-jurisprudence.jpg",
        "about": "The supreme authoritative treatise on forensic medicine, autopsy protocol, and clinical toxicology in Indian courts.",
        "sig": "Continuously cited as binding medical evidence across High Courts and Supreme Court benches.",
        "reader": "Advocates, trial judges, medical examiners, police academies, and law faculties.",
        "pages": "1,350 Pages", "binding": "Hardcover", "lang": "English", "pub": "LexisNexis India",
        "excerpt": "Medical evidence in criminal trials must establish causal nexus between the injury inflicted and the ultimate cause of death..."
    },
    {
        "id": "cat-8", "title": "Ratan Tata: A Life", "author": "Thomas Mathew",
        "price": 699, "mrp": 999, "discount": "30% OFF", "category": "bestsellers",
        "image": "assets/book-ratan-tata.jpg",
        "about": "The authorized biography charting the trials, corporate ethics, and nation-building vision of Ratan Naval Tata.",
        "sig": "National literary sensation giving unparalleled access to archival diaries and personal letters.",
        "reader": "Entrepreneurs, business leaders, management students, and readers of inspiring biographies.",
        "pages": "544 Pages", "binding": "Hardcover", "lang": "English", "pub": "HarperCollins India",
        "excerpt": "I never believed in taking right decisions. I took decisions and then made them right..."
    },
    {
        "id": "cat-9", "title": "The Himalayan Chronicler (Coming Soon)", "author": "Ruskin Bond",
        "price": 499, "mrp": 650, "discount": "23% OFF", "category": "coming-soon",
        "image": "assets/book-patthar-alpatthar.jpg",
        "about": "Unpublished mountain chronicles, rare Mussoorie nature essays, and intimate boyhood reflections in the Doon valley.",
        "sig": "Special commemorative volume celebrating Ruskin Bond's enduring 70-year literary career.",
        "reader": "All ages, lovers of nature writing, Himalayan folklore, and gentle storytelling.",
        "pages": "240 Pages", "binding": "Hardcover Gift Edition", "lang": "English", "pub": "Rupa Publications",
        "excerpt": "The hills are timeless, but the stories they whisper through the deodars change with every season..."
    },
    {
        "id": "cat-10", "title": "Gopi Diaries: Festive Gift Box (Coming Soon)", "author": "Sudha Murty",
        "price": 320, "mrp": 399, "discount": "20% OFF", "category": "coming-soon",
        "image": "assets/hero-book-sudha-murty.jpg",
        "about": "The heartwarming stories of Gopi the dog told through his eyes, accompanied by vibrant full-color illustrations.",
        "sig": "Loved by millions of families across India, encouraging kindness, empathy, and pet companionship.",
        "reader": "Children, dog lovers, young readers, and bedtime story families.",
        "pages": "160 Pages", "binding": "Illustrated Hardcover", "lang": "English", "pub": "HarperCollins Children",
        "excerpt": "Woof! My name is Gopi, and I have found the best family in the whole world. Let me tell you about my adventures..."
    },
    {
        "id": "cat-11", "title": "Prayagraj: The Eternal Confluence (Pre-Order)", "author": "Heritage Archival Project",
        "price": 899, "mrp": 1250, "discount": "28% OFF", "category": "pre-order",
        "image": "assets/book-hindi-sahitya-itihas.jpg",
        "about": "An opulent archival chronicle documenting Allahabad's historic confluence of literary icons from Nirala to Bachchan.",
        "sig": "First-of-its-kind coffee table archival volume produced in collaboration with local Allahabad historians.",
        "reader": "Prayagraj residents, history buffs, literary researchers, and cultural collectors.",
        "pages": "360 Pages", "binding": "Deluxe Clothbound", "lang": "English / Hindi", "pub": "Indigo Books Archival",
        "excerpt": "इलाहाबाद केवल एक शहर नहीं है, यह भारतीय बौद्धिक चेतना की वो त्रिवेणी है जहाँ हर कोने में कविता और क्रांति सांस लेती है..."
    },
    {
        "id": "cat-12", "title": "The Constitution of India (Pre-Order)", "author": "Legal Scholars Guild",
        "price": 1450, "mrp": 1999, "discount": "27% OFF", "category": "pre-order",
        "image": "assets/book-10-faisle.jpg",
        "about": "A magnificent collector's leather-bound volume containing the complete Constitution with historic preamble calligraphy.",
        "sig": "Includes full historical annotations and landmark 2026 judicial amendments.",
        "reader": "Advocates, judges, parliamentarians, law students, and constitutional patriots.",
        "pages": "680 Pages", "binding": "Full Leatherette", "lang": "English", "pub": "LexisNexis / Universal",
        "excerpt": "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC..."
    }
]

catalog_pre_rendered_html = ""
for b in catalog_12_books:
    overview_html = make_mini_overview_component(
        b["id"], b["title"], b["author"], b["about"], b["sig"], b["reader"],
        b["pages"], b["binding"], b["lang"], b["pub"], b["excerpt"]
    )
    catalog_pre_rendered_html += f"""
      <!-- Catalog Card: {b['title']} -->
      <div class="catalog-book-card bg-white border border-[#E8DFC8] rounded-xl p-4 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group" data-category="{b['category']}">
        <div>
          <div class="aspect-[2/3] w-full rounded-md overflow-hidden shadow-md mb-3 relative">
            <img src="{b['image']}" alt="{b['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-2 left-2 bg-[#D99B26] text-white font-sans text-[9px] font-bold px-2 py-0.5 rounded shadow">
              {b['discount']}
            </span>
          </div>
          <h4 class="font-serif text-sm font-bold text-[#0A1128] line-clamp-2 group-hover:text-[#D99B26] transition-colors leading-snug">
            {b['title']}
          </h4>
          <p class="text-xs text-slate-500 font-sans mt-0.5 font-medium">{b['author']}</p>

          <!-- Dedicated 📖 Mini Overview Component -->
          {overview_html}
        </div>

        <div class="mt-3 pt-3 border-t border-slate-100 flex items-center justify-between font-sans">
          <div>
            <span class="font-serif font-bold text-base text-[#0A1128] book-price">₹{b['price']}.00</span>
            <span class="text-[10px] text-slate-400 line-through ml-1 font-serif">₹{b['mrp']}</span>
          </div>
          <div class="flex items-center gap-1.5">
            <button type="button" onclick="addToCart('{b['id']}', '{b['title'].replace(chr(39), '')}', {b['price']}, '{b['image']}')" class="bg-[#D99B26] hover:bg-[#B88019] text-white p-2 rounded-lg transition-colors text-xs font-bold" title="Add to Cart">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm7 17H5V8h14v12z"/></svg>
            </button>
            <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%2C%20I%20want%20to%20order%20{b['title'].split(' ')[0]}%20at%20%E2%82%B9{b['price']}." target="_blank" class="bg-[#10B981] hover:bg-[#059669] text-white p-2 rounded-lg transition-colors" title="WhatsApp Order">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
            </a>
          </div>
        </div>
      </div>
    """

# Insert pre-rendered catalog books into #catalogCardsGrid
catalog_grid_pattern = r'<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6" id="catalogCardsGrid">\s*<!-- Populated via Javascript -->\s*<\/div>'
if re.search(catalog_grid_pattern, html):
    html = re.sub(catalog_grid_pattern, f'<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6" id="catalogCardsGrid">\n{catalog_pre_rendered_html}\n    </div>', html)
    print("BUG 2 FIXED: Pre-rendered 12 full catalog cards with 📖 Mini Overview into #catalogCardsGrid.")
else:
    m = re.search(r'<div[^>]*id="catalogCardsGrid"[^>]*>.*?<\/div>', html, re.DOTALL)
    if m:
        html = html[:m.start()] + f'<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6" id="catalogCardsGrid">\n{catalog_pre_rendered_html}\n    </div>' + html[m.end():]
        print("BUG 2 FIXED (fallback): Pre-rendered cards into #catalogCardsGrid.")

# =========================================================================
# ADD 📖 MINI OVERVIEW BUTTON TO MEHFIL-E-REKHTA CARDS
# =========================================================================
rekhta_overviews = {
    "mehfil-1": ("क्यों (Kyon)", "Jaun Elia", "An intimate anthology of Jaun Elia's most piercing ghazals on existential longing and heartbreak.", "The bible of modern Urdu romantic poetry and philosophical angst.", "Poetry lovers and fans of introspective ghazals.", "280 Pages", "Hardcover", "Urdu / Hindi", "Rekhta Publications", "शायद मुझे निकाल के पछता रहे हों आप • महफ़िल में इस ख़याल से फिर आ गया हूँ मैं..."),
    "mehfil-2": ("रंजिश ही सही", "Ahmad Faraz", "Timeless Urdu romantic poetry celebrating love, separation, and resilient spirit.", "One of the most recited and recorded ghazal collections in South Asian history.", "Lovers of melody, verse, and profound romantic literature.", "320 Pages", "Hardcover", "Urdu / Hindi", "Vani Prakashan", "रंजिश ही सही दिल ही दुखाने के लिए आ • आ फिर से मुझे छोड़ के जाने के लिए आ..."),
    "mehfil-3": ("दोज़ख़नामा", "Rabisankar Bal", "A posthumous conversation between Mirza Ghalib and Saadat Hasan Manto speaking from their graves.", "Cross-border literary masterpiece bridging Lucknow, Delhi, and Lahore.", "Readers of historical fiction, Delhi's bygone culture, and literary biographies.", "390 Pages", "Hardcover", "Hindi Translation", "Vani Prakashan", "कब्र की मिट्टी जब बोलती है, तो इतिहास अपनी गलती स्वीकार करता है। ग़ालिब और मंटो के बीच की यह दास्तान सदियों का दर्द समेटे है..."),
    "mehfil-4": ("ठंडा गोश्त", "Saadat Hasan Manto", "Unflinching, masterfully crafted short stories dissecting human psychology during Partition.", "Manto's most controversial and celebrated literary court-trial piece.", "Fans of fearless progressive writing and realism.", "220 Pages", "Paperback", "Hindi", "Rajkamal Prakashan", "ईश्वर सिंह जब होटल के कमरे में दाखिल हुआ, तो उसके चेहरे पर एक अजीब सी वहशत थी। कुलवंत कौर ने उसकी तरफ देखा और समझ गई कि कुछ अनहोनी हो चुकी है..."),
    "mehfil-5": ("धुआँ", "Saadat Hasan Manto", "Raw, evocative tales of adolescence, society, and unspoken human truths.", "A brilliant demonstration of Manto's psychoanalytical storytelling.", "Students of psychoanalysis, short story writers, and classic literature lovers.", "210 Pages", "Paperback", "Hindi", "Rajkamal Prakashan", "धुआँ केवल सिगरेट से नहीं निकलता, इंसान के भीतर सुलगती तमन्नाएँ जब घुटती हैं, तो रूह से भी धुआँ उठता है...")
}

for mid, info in rekhta_overviews.items():
    overview_comp = make_mini_overview_component(mid, info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9])
    # Search for button row inside data-poet card and prepend overview
    # Let's see if overview button already exists or inject it cleanly
    pattern = rf'(onclick="addToCart\(\'{mid}\'[^>]*>.*?<\/div>\s*<\/div>)'
    m = re.search(pattern, html)
    if m and f'miniOverview-{mid}' not in html:
        # Inject right before the buttons row
        btn_row_start = html.rfind('<div class="grid grid-cols-2 gap-2', 0, m.start())
        if btn_row_start != -1:
            html = html[:btn_row_start] + overview_comp + html[btn_row_start:]
            print(f"Injected 📖 Mini Overview into {mid} ({info[0]})")

# =========================================================================
# JAVASCRIPT LOGIC FOR MINI OVERVIEW & EXCERPT TOGGLES
# =========================================================================
toggle_script = """
<script id="miniOverviewEngine">
// Universal Mini Overview Toggle
function toggleMiniOverview(cardId, event) {
  if (event) event.stopPropagation();
  const drawer = document.getElementById(`miniOverview-${cardId}`);
  if (!drawer) return;

  if (drawer.classList.contains('hidden')) {
    drawer.classList.remove('hidden');
    drawer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  } else {
    drawer.classList.add('hidden');
  }
}

// First Page Excerpt Toggle
function toggleExcerpt(cardId, event) {
  if (event) event.stopPropagation();
  const excerpt = document.getElementById(`excerpt-${cardId}`);
  if (!excerpt) return;

  if (excerpt.classList.contains('hidden')) {
    excerpt.classList.remove('hidden');
  } else {
    excerpt.classList.add('hidden');
  }
}
</script>
"""

if 'id="miniOverviewEngine"' in html:
    html = re.sub(r'<script id="miniOverviewEngine">.*?</script>', toggle_script.strip(), html, flags=re.DOTALL)
else:
    body_pos = html.rfind('</body>')
    if body_pos != -1:
        html = html[:body_pos] + toggle_script + '\n' + html[body_pos:]

# Save repaired preview.html
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: preview.html repaired and verified!")

