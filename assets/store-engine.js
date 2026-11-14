
// =========================================================================
// INDIGO BOOKS INDIA - PURE VANILLA JS ENGINE
// =========================================================================

// --- 1. PODIUM STATE & FUNCTIONS ---
let currentPodiumIndex = 0;

function selectPodiumBook(index) {
  if (index < 0 || index >= PODIUM_BOOKS.length) return;
  currentPodiumIndex = index;
  const book = PODIUM_BOOKS[index];

  // Update center book 3D cover & text
  const elCoverImg = document.getElementById('podium-cover-img');
  const elInsideThumb = document.getElementById('podium-inside-thumb');
  const elInsideTitle = document.getElementById('podium-inside-title');
  const elInsideAuthor = document.getElementById('podium-inside-author');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  if (elCoverImg) {
    elCoverImg.src = book.coverUrl;
    elCoverImg.alt = book.title;
  }
  if (elInsideThumb) {
    elInsideThumb.src = book.coverUrl;
    elInsideThumb.alt = book.title;
  }
  if (elInsideTitle) elInsideTitle.textContent = book.title;
  if (elInsideAuthor) elInsideAuthor.textContent = book.author;
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.firstPageExcerpt;
  if (el3dBook) el3dBook.classList.remove('is-open');

  // Update Right Spotlight Card
  const elBadge = document.getElementById('podiumSpotBadge');
  const elStock = document.getElementById('podiumSpotStock');
  const elHeading = document.getElementById('podiumSpotHeading');
  const elAuthor = document.getElementById('podiumSpotAuthor');
  const elRating = document.getElementById('podiumSpotRating');
  const elQuote = document.getElementById('podiumSpotQuote');
  const elPages = document.getElementById('podiumSpotPages');
  const elPublisher = document.getElementById('podiumSpotPublisher');
  const elPrice = document.getElementById('podiumSpotPrice');
  const elOldPrice = document.getElementById('podiumSpotOldPrice');
  const elDiscount = document.getElementById('podiumSpotDiscount');

  if (elBadge) elBadge.textContent = book.badge;
  if (elStock) elStock.textContent = book.stock;
  if (elHeading) elHeading.textContent = book.title;
  if (elAuthor) elAuthor.textContent = book.author;
  if (elRating) elRating.textContent = book.rating;
  if (elQuote) elQuote.textContent = '"' + book.quote + '"';
  if (elPages) elPages.textContent = book.pages;
  if (elPublisher) elPublisher.textContent = book.publisher;
  if (elPrice) elPrice.textContent = book.price;
  if (elOldPrice) elOldPrice.textContent = book.oldPrice;
  if (elDiscount) elDiscount.textContent = book.discount;

  // Update Flanking Books positions
  const count = PODIUM_BOOKS.length;
  const fL2 = (index - 2 + count) % count;
  const fL1 = (index - 1 + count) % count;
  const fR1 = (index + 1) % count;
  const fR2 = (index + 2) % count;

  const imgL2 = document.getElementById('flankImgL2');
  const imgL1 = document.getElementById('flankImgL1');
  const imgR1 = document.getElementById('flankImgR1');
  const imgR2 = document.getElementById('flankImgR2');

  if (imgL2) { imgL2.src = PODIUM_BOOKS[fL2].coverUrl; imgL2.alt = PODIUM_BOOKS[fL2].title; }
  if (imgL1) { imgL1.src = PODIUM_BOOKS[fL1].coverUrl; imgL1.alt = PODIUM_BOOKS[fL1].title; }
  if (imgR1) { imgR1.src = PODIUM_BOOKS[fR1].coverUrl; imgR1.alt = PODIUM_BOOKS[fR1].title; }
  if (imgR2) { imgR2.src = PODIUM_BOOKS[fR2].coverUrl; imgR2.alt = PODIUM_BOOKS[fR2].title; }

  // Update Dots
  const dots = document.querySelectorAll('.podium-dot');
  dots.forEach((dot, i) => {
    if (i === index) dot.classList.add('active');
    else dot.classList.remove('active');
  });

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function prevPodiumBook() {
  const nextIdx = (currentPodiumIndex - 1 + PODIUM_BOOKS.length) % PODIUM_BOOKS.length;
  selectPodiumBook(nextIdx);
}

function nextPodiumBook() {
  const nextIdx = (currentPodiumIndex + 1) % PODIUM_BOOKS.length;
  selectPodiumBook(nextIdx);
}

function selectPodiumByFlank(slotOffset) {
  const count = PODIUM_BOOKS.length;
  const targetIdx = (currentPodiumIndex + slotOffset + count) % count;
  selectPodiumBook(targetIdx);
}

function togglePodiumCover(e) {
  if (e) e.stopPropagation();
  const el = document.getElementById('podium-3d-book');
  if (el) el.classList.toggle('is-open');
}

function addCurrentPodiumToCart() {
  const book = PODIUM_BOOKS[currentPodiumIndex];
  addToCart(book.id);
}

function openCurrentPodiumOverview() {
  const book = PODIUM_BOOKS[currentPodiumIndex];
  openOverviewModal(book.id);
}

function orderCurrentPodiumWhatsApp() {
  const book = PODIUM_BOOKS[currentPodiumIndex];
  const msg = "Hello Indigo Books Prayagraj! I would like to order: " + book.title + " (Price: " + book.price + "). Please confirm stock and COD details.";
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(msg), '_blank');
}


// --- 2. MEHFIL-E-REKHTA STATE & FUNCTIONS ---
let currentPoetKey = 'all';
let currentSherIndex = 0;

function switchPoet(poetKey) {
  if (!POET_SHAYARI_DATA[poetKey]) return;
  currentPoetKey = poetKey;
  currentSherIndex = 0;

  // Update active pill
  document.querySelectorAll('.poet-pill').forEach(btn => {
    if (btn.getAttribute('data-poet') === poetKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  renderCurrentSher();
}

function renderCurrentSher() {
  const poet = POET_SHAYARI_DATA[currentPoetKey];
  const couplets = poet.couplets;
  if (!couplets || couplets.length === 0) return;

  const sher = couplets[currentSherIndex % couplets.length];

  const elUrdu = document.getElementById('rekhtaUrdu');
  const elHindi = document.getElementById('rekhtaHindi');
  const elEng = document.getElementById('rekhtaEng');
  const elAttr = document.getElementById('rekhtaAttr');
  const elFull = document.getElementById('rekhtaFullGhazal');

  if (elUrdu) elUrdu.textContent = sher.urdu;
  if (elHindi) elHindi.textContent = sher.hindi;
  if (elEng) elEng.textContent = sher.eng;
  if (elAttr) elAttr.textContent = sher.attr;
  if (elFull) elFull.textContent = sher.ghazal;

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function nextSher() {
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex + 1) % couplets.length;
  renderCurrentSher();
}

function prevSher() {
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex - 1 + couplets.length) % couplets.length;
  renderCurrentSher();
}

function toggleGhazalDrawer() {
  const el = document.getElementById('rekhtaFullGhazal');
  if (el) el.classList.toggle('is-open');
}


// --- 3. ACADEMIC & LAW VAULT STATE & FUNCTIONS ---
let currentVaultTab = 'law';

function switchVaultTab(tabKey) {
  if (!VAULT_BOOKS[tabKey]) return;
  currentVaultTab = tabKey;

  // Update tab buttons
  document.querySelectorAll('.vault-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  // Render 4 books
  const books = VAULT_BOOKS[tabKey];
  const container = document.getElementById('vaultCardsContainer');
  if (!container) return;

  container.innerHTML = books.map(book => `
    <div class="vault-card">
      <div class="vault-card-thumb">
        <img src="${book.coverUrl}" alt="${book.title}" loading="lazy" />
      </div>
      <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
        ${book.badge}
      </div>
      <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
        ${book.title}
      </h3>
      <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
        ${book.author}
      </div>
      <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
        <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
        <span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <button type="button" class="btn-overview" onclick="openOverviewModal('${book.id}')">
          <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
        </button>
        <button type="button" class="btn-add-cart" onclick="addToCart('${book.id}')">
          <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
        </button>
      </div>
    </div>
  `).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 4. PAN-INDIA CATALOG FILTERING ---
let currentCatalogCategory = 'all';
let currentCatalogQuery = '';

function filterCatalog(category) {
  currentCatalogCategory = category;

  document.querySelectorAll('.cat-pill').forEach(btn => {
    if (btn.getAttribute('data-cat') === category) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  renderCatalog();
}

function handleCatalogSearch(e) {
  currentCatalogQuery = e.target.value.toLowerCase().trim();
  renderCatalog();
}

function handleHeroSearch(e) {
  if (e.key === 'Enter') {
    performHeroSearch();
  }
}

function performHeroSearch() {
  const input = document.getElementById('hero-search-input');
  if (input) {
    currentCatalogQuery = input.value.toLowerCase().trim();
    const catInput = document.getElementById('catalog-search-input');
    if (catInput) catInput.value = input.value;
    scrollToCatalog('all');
    renderCatalog();
  }
}

function renderCatalog() {
  const container = document.getElementById('catalogGridContainer');
  if (!container) return;

  const filtered = CATALOG_BOOKS.filter(book => {
    const matchesCat = currentCatalogCategory === 'all' || book.tags.includes(currentCatalogCategory);
    const matchesQuery = !currentCatalogQuery || 
      book.title.toLowerCase().includes(currentCatalogQuery) || 
      book.author.toLowerCase().includes(currentCatalogQuery);
    return matchesCat && matchesQuery;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px; background: #FFFFFF; border-radius: 12px; border: 1px dashed #CBD5E1;">
        <i data-lucide="search-x" style="width: 36px; height: 36px; color: #94A3B8; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 18px; color: #0F172A; margin-bottom: 6px;">No books found</h4>
        <p style="font-size: 13px; color: #64748B;">Try adjusting your search terms or category filter.</p>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  container.innerHTML = filtered.map(book => `
    <div class="catalog-card">
      <div class="catalog-thumb">
        <img src="${book.coverUrl}" alt="${book.title}" loading="lazy" />
      </div>
      <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
        ${book.discount}
      </div>
      <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
        ${book.title}
      </h3>
      <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
        ${book.author}
      </div>
      <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
        <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
        <span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <button type="button" class="btn-overview" onclick="openOverviewModal('${book.id}')">
          <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
        </button>
        <button type="button" class="btn-add-cart" onclick="addToCart('${book.id}')">
          <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
        </button>
      </div>
    </div>
  `).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 5. UNIVERSAL MINI OVERVIEW MODAL ---
function openOverviewModal(bookId) {
  const book = MODAL_METADATA_DATABASE[bookId] || MODAL_METADATA_DATABASE['podium-kasaibada'];
  if (!book) return;

  const modal = document.getElementById('overviewModalOverlay');
  if (!modal) return;

  document.getElementById('modalCover').src = book.cover;
  document.getElementById('modalCover').alt = book.title;
  document.getElementById('modalTitle').textContent = book.title;
  document.getElementById('modalAuthor').textContent = book.author;
  document.getElementById('modalDiscount').textContent = book.discount;
  document.getElementById('modalPrice').textContent = "₹" + Number(book.price).toFixed(2);
  document.getElementById('modalMRP').textContent = "₹" + Number(book.mrp).toFixed(2);

  document.getElementById('modalLang').textContent = book.lang;
  document.getElementById('modalBinding').textContent = book.binding;
  document.getElementById('modalPages').textContent = book.pages;
  document.getElementById('modalPublisher').textContent = book.pub;
  document.getElementById('modalDispatch').textContent = book.dispatch;

  document.getElementById('modalOverviewText').textContent = book.overview;

  const highlightsContainer = document.getElementById('modalHighlightsList');
  if (highlightsContainer && book.highlights) {
    highlightsContainer.innerHTML = book.highlights.map(h => `
      <li style="display: flex; align-items: flex-start; gap: 8px; font-size: 12.5px; color: #334155;">
        <i data-lucide="check" style="width: 16px; height: 16px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
        <span>${h}</span>
      </li>
    `).join('');
  }

  // Update modal actions
  const addBtn = document.getElementById('modalAddToCartBtn');
  if (addBtn) addBtn.onclick = function() { addToCart(bookId); closeOverviewModal(); };

  const waBtn = document.getElementById('modalWhatsAppBtn');
  if (waBtn) {
    const msg = "Hello Indigo Books India! I would like to order: " + book.title + " (Price: ₹" + book.price + "). Please confirm availability.";
    waBtn.href = "https://wa.me/918933063306?text=" + encodeURIComponent(msg);
  }

  modal.classList.add('is-active');
  document.body.style.overflow = 'hidden';

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeOverviewModal() {
  const modal = document.getElementById('overviewModalOverlay');
  if (modal) modal.classList.remove('is-active');
  document.body.style.overflow = '';
}


// --- 6. SHOPPING CART DRAWER ---
let cart = [];

function addToCart(bookId) {
  const meta = MODAL_METADATA_DATABASE[bookId] || MODAL_METADATA_DATABASE['podium-kasaibada'];
  const existing = cart.find(item => item.id === bookId);

  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({
      id: bookId,
      title: meta.title,
      author: meta.author,
      price: meta.price,
      cover: meta.cover,
      qty: 1
    });
  }

  updateCartUI();
  toggleCartDrawer(true);
}

function updateCartQty(bookId, delta) {
  const item = cart.find(i => i.id === bookId);
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(i => i.id !== bookId);
  }

  updateCartUI();
}

function removeFromCart(bookId) {
  cart = cart.filter(i => i.id !== bookId);
  updateCartUI();
}

function updateCartUI() {
  const count = cart.reduce((sum, item) => sum + item.qty, 0);
  const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);

  const countBadge = document.getElementById('nav-cart-count');
  const totalBadge = document.getElementById('nav-cart-total');
  const drawerCount = document.getElementById('drawerCartCount');
  const drawerSubtotal = document.getElementById('drawerSubtotal');

  if (countBadge) countBadge.textContent = count;
  if (totalBadge) totalBadge.textContent = "₹" + subtotal.toFixed(2);
  if (drawerCount) drawerCount.textContent = count;
  if (drawerSubtotal) drawerSubtotal.textContent = "₹" + subtotal.toFixed(2);

  const list = document.getElementById('drawerCartItems');
  if (!list) return;

  if (cart.length === 0) {
    list.innerHTML = `
      <div style="text-align: center; padding: 48px 16px; color: #64748B;">
        <i data-lucide="shopping-bag" style="width: 48px; height: 48px; color: #CBD5E1; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 16px; color: #0F172A; margin-bottom: 4px;">Your cart is empty</h4>
        <p style="font-size: 13px;">Add some books to read!</p>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  list.innerHTML = cart.map(item => `
    <div style="display: flex; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #F1F5F9;">
      <div style="width: 60px; height: 85px; border-radius: 4px; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
        <img src="${item.cover}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.25; margin-bottom: 2px;">
            ${item.title}
          </h4>
          <div style="font-size: 11px; color: #64748B;">${item.author}</div>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">
          <div style="font-size: 14px; font-weight: 800; color: #0F172A;">
            ₹${(item.price * item.qty).toFixed(2)}
          </div>
          <div style="display: flex; align-items: center; gap: 8px; background: #F1F5F9; border-radius: 6px; padding: 2px 8px;">
            <button type="button" onclick="updateCartQty('${item.id}', -1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">-</button>
            <span style="font-size: 12px; font-weight: 700; color: #0F172A;">${item.qty}</span>
            <button type="button" onclick="updateCartQty('${item.id}', 1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">+</button>
          </div>
        </div>
      </div>
    </div>
  `).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function toggleCartDrawer(forceOpen) {
  const drawer = document.getElementById('cartDrawerOverlay');
  if (!drawer) return;

  if (forceOpen === true) {
    drawer.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  } else if (forceOpen === false) {
    drawer.classList.remove('is-open');
    document.body.style.overflow = '';
  } else {
    drawer.classList.toggle('is-open');
    document.body.style.overflow = drawer.classList.contains('is-open') ? 'hidden' : '';
  }
}

function checkoutWhatsApp() {
  if (cart.length === 0) {
    alert("Your shopping cart is empty!");
    return;
  }

  let text = "Hello Indigo Books India (Prayagraj)!\nI want to place an order via Cash on Delivery (COD):\n\n";
  let total = 0;

  cart.forEach((item, index) => {
    const lineTotal = item.price * item.qty;
    total += lineTotal;
    text += (index + 1) + ". *" + item.title + "* x" + item.qty + " — ₹" + lineTotal.toFixed(2) + "\n";
  });

  text += "\n*Cart Subtotal:* ₹" + total.toFixed(2) + "\n";
  text += "*Dispatch Location:* Prayagraj Hub\n\nPlease confirm delivery time & COD address!";

  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(text), '_blank');
}


// --- 7. MEMBER LOGIN MODAL ---
function toggleLoginModal() {
  const modal = document.getElementById('loginModalOverlay');
  if (!modal) return;
  modal.classList.toggle('is-active');
  document.body.style.overflow = modal.classList.contains('is-active') ? 'hidden' : '';
  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 8. SMOOTH SCROLL & FILTER HELPERS ---
function scrollToCatalog(category) {
  filterCatalog(category);
  const el = document.getElementById('shop-all-catalog');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function scrollToVault(tabKey) {
  switchVaultTab(tabKey);
  const el = document.getElementById('law-academic-vault');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}


// --- 9. DOM INITIALIZATION ---
document.addEventListener('DOMContentLoaded', function() {
  selectPodiumBook(0);
  switchPoet('all');
  switchVaultTab('law');
  renderCatalog();
  updateCartUI();

  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});

window.addEventListener('load', function() {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});
