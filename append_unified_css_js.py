# -*- coding: utf-8 -*-
"""
append_unified_css_js.py
Appends the updated -140deg cover flip physics, parchment page styling,
and poet/tab filter handlers to assets/theme.css and assets/theme.js
"""

theme_css_additions = """
/* ==========================================================================
   INDIGO BOOKS - UPDATED 3D COVER OPEN & TYPOGRAPHY RULES
   ========================================================================== */

/* Universal Font Enforcement */
body, button, input, select, textarea, .font-sans {
  font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}
h1, h2, h3, h4, h5, h6, .font-serif, .book-title, .book-price, .poet-couplet, .brand-wordmark {
  font-family: 'Playfair Display', Georgia, Cambria, serif !important;
}

/* 3D Podium Wide Cover Open to -140deg */
.podium-stage-container {
  perspective: 1600px;
}
.book-cover-front {
  transform-origin: left center;
  transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.5s ease;
  backface-visibility: hidden;
  z-index: 25;
}
.book-cover-back {
  position: absolute;
  inset: 0;
  transform-origin: left center;
  transform: rotateY(180deg);
  backface-visibility: hidden;
  background: linear-gradient(135deg, #1A120B 0%, #2D1E12 100%);
  border: 1px solid #4A3525;
  border-radius: 4px 2px 2px 4px;
  z-index: 24;
  transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}
.podium-book-card.is-active:hover .book-cover-front,
.podium-book-card.is-active.is-open .book-cover-front {
  transform: rotateY(-140deg) !important;
  box-shadow: 25px 30px 60px rgba(0, 0, 0, 0.8) !important;
}
.podium-book-card.is-active:hover .book-cover-back,
.podium-book-card.is-active.is-open .book-cover-back {
  transform: rotateY(40deg) !important;
}

/* Right Parchment Page Revealed Underneath */
.book-page-underneath {
  background-color: #FFFDF9;
  background-image: radial-gradient(#F5EFE6 1px, transparent 1px);
  background-size: 12px 12px;
  border: 1px solid #E8DFC8;
  box-shadow: inset 5px 0 15px rgba(0,0,0,0.06), 0 10px 25px rgba(0,0,0,0.15);
}
"""

theme_js_additions = """
// ==========================================================================
// INDIGO BOOKS - WIDE COVER OPEN & POET FILTERING LOGIC
// ==========================================================================
let isShopifyPodiumOpen = false;

window.togglePodiumCoverOpen = function() {
  isShopifyPodiumOpen = !isShopifyPodiumOpen;
  const activeCard = document.querySelector('.podium-book-card.is-active');
  const btnText = document.getElementById('flipCoverBtnText');
  if (activeCard) {
    if (isShopifyPodiumOpen) {
      activeCard.classList.add('is-open');
      if (btnText) btnText.innerText = "Cover Open (-140°) • Click to Close";
    } else {
      activeCard.classList.remove('is-open');
      if (btnText) btnText.innerText = "Hover or Click Book to Open Cover (-140°)";
    }
  }
};

window.filterMehfilPoet = function(poetKey) {
  const pills = document.querySelectorAll('#poetSelectorPills button');
  pills.forEach(p => {
    p.className = 'poet-pill px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/20 bg-white/5 text-amber-300/70 hover:bg-white/10 hover:text-amber-200 transition-all font-sans';
  });
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.className = 'poet-pill active px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide border border-amber-500/50 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(217,155,38,0.3)] transition-all font-sans';
  }

  if (typeof POET_VERSES !== 'undefined') {
    const q = POET_VERSES[poetKey] || POET_VERSES['elia'];
    const urduEl = document.getElementById('poetUrduVerse');
    const hindiEl = document.getElementById('poetHindiVerse');
    const engEl = document.getElementById('poetEngVerse');
    const attrEl = document.getElementById('poetAttribution');

    if (urduEl && hindiEl && engEl && attrEl && q) {
      urduEl.style.opacity = '0';
      hindiEl.style.opacity = '0';
      engEl.style.opacity = '0';

      setTimeout(() => {
        urduEl.innerText = q.urdu;
        hindiEl.innerText = `"${q.hindi}"`;
        engEl.innerText = q.eng;
        attrEl.innerText = `— ${q.name} (${q.pen})`;

        urduEl.style.opacity = '1';
        hindiEl.style.opacity = '1';
        engEl.style.opacity = '1';
      }, 200);
    }
  }

  const cards = document.querySelectorAll('.rekhta-book-card');
  cards.forEach(card => {
    const cardPoet = card.getAttribute('data-poet');
    if (poetKey === 'all' || cardPoet === poetKey) {
      card.style.opacity = '1';
      card.style.transform = 'scale(1)';
      card.style.borderColor = (cardPoet === poetKey) ? '#F59E0B' : 'rgba(245, 158, 11, 0.2)';
      if (cardPoet === poetKey) {
        card.style.boxShadow = '0 0 25px rgba(217, 155, 38, 0.35)';
      } else {
        card.style.boxShadow = '';
      }
    } else {
      card.style.opacity = '0.35';
      card.style.transform = 'scale(0.96)';
      card.style.borderColor = 'rgba(255, 255, 255, 0.05)';
      card.style.boxShadow = '';
    }
  });
};
"""

with open('assets/theme.css', 'a', encoding='utf-8') as f:
    f.write('\n' + theme_css_additions + '\n')
print("Appended updated CSS to assets/theme.css")

with open('assets/theme.js', 'a', encoding='utf-8') as f:
    f.write('\n' + theme_js_additions + '\n')
print("Appended updated JS to assets/theme.js")


