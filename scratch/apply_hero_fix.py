# -*- coding: utf-8 -*-
import sys
import re

with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

hero_replacement = """    <!-- =========================================================================
         2. HERO SECTION & SEQUENTIAL SPOTLIGHT ANIMATION
         ========================================================================= -->
    <style id="hero-locked-styles">
      /* LOCKED 2-COLUMN HERO LAYOUT */
      #indigo-video-hero,
      .ivh-section {{
        position: relative !important;
        min-height: 520px !important;
        width: 100% !important;
        background: linear-gradient(115deg, #09132C 0%, #101D40 48%, #2B2118 78%, #4A3314 100%) !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
      }}

      .ivh-container {{
        position: relative !important;
        z-index: 20 !important;
        max-width: 1280px !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding: 44px 32px !important;
        display: grid !important;
        grid-template-columns: 1fr 1.1fr !important;
        gap: 32px !important;
        align-items: center !important;
        box-sizing: border-box !important;
      }}

      /* LEFT COLUMN: HEADING, SUBTITLE, SEARCH & BUTTONS */
      .ivh-left {{
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        text-align: left !important;
        z-index: 25 !important;
        order: 1 !important;
      }}

      .ivh-title {{
        font-family: 'Merriweather', Georgia, serif !important;
        font-size: 52px !important;
        font-weight: 700 !important;
        line-height: 1.12 !important;
        color: #FFFFFF !important;
        margin: 0 0 16px 0 !important;
      }}

      .ivh-story-italic {{
        font-family: 'Merriweather', Georgia, serif !important;
        font-style: italic !important;
        color: #E5A93C !important;
      }}

      /* RIGHT COLUMN: RANGOLI + STRICT 3x2 BOOK GRID + DIYAS */
      .ivh-right {{
        position: relative !important;
        min-height: 430px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        order: 2 !important;
      }}

      .ivh-rangoli-anchor {{
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        width: 440px !important;
        height: 440px !important;
        transform: translate(-50%, -50%) !important;
        z-index: 8 !important;
        pointer-events: none !important;
      }}

      .ivh-rangoli-spin {{
        width: 100% !important;
        height: 100% !important;
        animation: ivhSpinClockwise 42s linear infinite !important;
        transform-origin: center center !important;
      }}

      @keyframes ivhSpinClockwise {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      /* STRICT 3 COLUMNS x 2 ROWS BOOK GRID (NEVER STACK VERTICALLY!) */
      #ivh-books-grid,
      .ivh-books-grid {{
        position: relative !important;
        z-index: 25 !important;
        display: grid !important;
        grid-template-columns: repeat(3, 126px) !important;
        grid-template-rows: repeat(2, 186px) !important;
        gap: 18px !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
      }}

      .ivh-book-card {{
        position: relative !important;
        width: 126px !important;
        height: 186px !important;
        max-width: 126px !important;
        max-height: 186px !important;
        border-radius: 6px !important;
        overflow: hidden !important;
        border-right: 4px solid #F8FAFC !important;
        box-shadow: 0 14px 28px rgba(0,0,0,0.6) !important;
        cursor: pointer !important;
        background: #0F172A !important;
        display: block !important;
        transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.42s ease, box-shadow 0.42s ease !important;
      }}

      .ivh-book-card img {{
        width: 100% !important;
        height: 100% !important;
        max-width: 126px !important;
        max-height: 186px !important;
        object-fit: cover !important;
        display: block !important;
      }}

      @media (max-width: 900px) {{
        .ivh-container {{
          grid-template-columns: 1fr !important;
          padding: 24px 16px !important;
        }}
        .ivh-title {{ font-size: 34px !important; }}
        .ivh-rangoli-anchor {{ width: 290px !important; height: 290px !important; }}
        #ivh-books-grid, .ivh-books-grid {{
          grid-template-columns: repeat(3, 94px) !important;
          grid-template-rows: repeat(2, 140px) !important;
          gap: 10px !important;
        }}
        .ivh-book-card, .ivh-book-card img {{
          width: 94px !important;
          height: 140px !important;
          max-width: 94px !important;
          max-height: 140px !important;
        }}
      }}
    </style>

    <section class="hero-section ivh-section" id="indigo-video-hero">
      <div class="hero-topleft-watermark">
        {HERO_TOPLEFT_WATERMARK_SVG}
      </div>

      {HERO_FLOOR_CURVE_SVG}
      {STRING_LIGHTS_SVG}
      {HERO_DIYAS_SVG}

      <div class="site-container hero-main-grid hero-inner-container ivh-container">
        
        <!-- Left Column -->
        <div class="hero-left-col ivh-left">
          <h1 class="ivh-title">Discover Your Next<br>Favorite <em class="ivh-story-italic" style="color: #E5A93C; font-style: italic; font-family: Georgia, serif;">Story</em></h1>
          <p>Explore India's largest online collection of bestsellers, regional gems, academic reads, and more.</p>
          
          <!-- Search Box -->
          <div class="hero-search-wrap search-input-wrap">
            <i data-lucide="search" style="width: 18px; height: 18px; color: #94A3B8; flex-shrink: 0;"></i>
            <input type="text" id="hero-search-input" placeholder="Search for a book, author, or ISBN..." oninput="handleSearchInput(this.value, 'hero')" onkeydown="handleHeroSearch(event)" autocomplete="off" />
            <div id="hero-search-suggestions" class="search-suggestions-dropdown" style="display: none;"></div>
          </div>

          <!-- CTA Row -->
          <div class="hero-cta-row">
            <button type="button" class="hero-shop-btn" onclick="scrollToCatalog('all')">
              <span>Shop Now →</span>
            </button>
            <a href="https://wa.me/918933063306?text=Hello%20Indigo%20Books!%20I%20want%20to%20place%20a%20Cash%20on%20Delivery%20order." target="_blank" class="hero-wa-cod-btn">
              <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981; margin-right: 8px; box-shadow: 0 0 8px #10B981;"></span>
              <span>WhatsApp COD</span>
            </a>
          </div>
        </div>

        <!-- Right Column: 3x2 Grid with Rangoli & Precise Spotlights -->
        <div class="hero-right-col ivh-right hero-stage-col">
          <div class="hero-rangoli-bg hero-rangoli-wrapper hero-wheel-wrap ivh-rangoli-anchor">
            <div class="ivh-rangoli-spin">
              {HERO_GEOMETRIC_RANGOLI_SVG}
            </div>
          </div>

          <div class="hero-books-grid ivh-books-grid hero-books-grid-video" id="ivh-books-grid">
            
            <!-- Book 1: Godan (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="0" onclick="handleBookAction('cat-book-1-9789389742152', '/products/godan-premchand', event)" title="View Godan by Premchand">
              <div class="hero-book-thumb">
                <img src="assets/hero-godan.jpg" alt="Godan (गोदान)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Godan</div>
                <div class="hero-book-author">Premchand</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 2: Raag Darbari (₹499.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="1" onclick="handleBookAction('cat-book-2-9788126713967', '/products/raag-darbari-shrilal-shukla', event)" title="View Raag Darbari by Shrilal Shukla">
              <div class="hero-book-thumb">
                <img src="assets/hero-raag-darbari.jpg" alt="Raag Darbari (राग दरबारी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Raag Darbari</div>
                <div class="hero-book-author">Shrilal Shukla</div>
                <div class="hero-book-price">₹499.00</div>
              </div>
            </div>

            <!-- Book 3: Chitralekha (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="2" onclick="handleBookAction('cat-book-3-9788126715855', '/products/chitralekha-bhagwaticharan-verma', event)" title="View Chitralekha by Bhagwaticharan Verma">
              <div class="hero-book-thumb">
                <img src="assets/hero-chitralekha.jpg" alt="Chitralekha (चित्रलेखा)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Chitralekha</div>
                <div class="hero-book-author">Bhagwaticharan Verma</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 4: Rashmirathi (₹299.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="3" onclick="handleBookAction('cat-book-4-9788180313639', '/products/rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar', event)" title="View Rashmirathi by Ramdhari Singh Dinkar">
              <div class="hero-book-thumb">
                <img src="assets/hero-rashmirathi.jpg" alt="Rashmirathi (रश्मिरथी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Rashmirathi</div>
                <div class="hero-book-author">Ramdhari Singh Dinkar</div>
                <div class="hero-book-price">₹299.00</div>
              </div>
            </div>

            <!-- Book 5: Kuchh Ishq Kiya Kuchh Kaam Kiya (₹250.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="4" onclick="handleBookAction('cat-book-5-9788126728435', '/products/kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra', event)" title="View Kuchh Ishq Kiya by Piyush Mishra">
              <div class="hero-book-thumb">
                <img src="assets/hero-kuchh-ishq.jpg" alt="Kuchh Ishq Kiya Kuchh Kaam Kiya" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Kuchh Ishq Kiya</div>
                <div class="hero-book-author">Piyush Mishra</div>
                <div class="hero-book-price">₹250.00</div>
              </div>
            </div>

            <!-- Book 6: Gypsy (₹995.00) -->
            <div class="hero-book-card ivh-book-card hero-video-book-card" data-hero-idx="5" onclick="handleBookAction('cat-book-6-9789352210046', '/products/gypsy-ila-chandra-joshi', event)" title="View Gypsy by Ila Chandra Joshi">
              <div class="hero-book-thumb">
                <img src="assets/hero-gypsy.jpg" alt="Gypsy (जिप्सी)" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src=getFallbackCover(this.alt);" />
              </div>
              <div class="hero-book-info hero-book-meta">
                <div class="hero-book-title">Gypsy</div>
                <div class="hero-book-author">Ila Chandra Joshi</div>
                <div class="hero-book-price">₹995.00</div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>"""

# Replace in content
pattern = r'<!--\s*=+\s*2\.\s*HERO SECTION[\s\S]*?</section>'
if re.search(pattern, content):
    content = re.sub(pattern, hero_replacement, content, count=1)
    print("Replaced Hero section in build_html_generator.py with locked styles and exact .ivh-* classes.")
else:
    print("ERROR: Could not find Hero pattern in build_html_generator.py!")
    sys.exit(1)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_html_generator.py successfully.")

