// Test resolution of Raag Darbari, Godan, Tarkash, Bharat Ka Samvidhan
const EXACT_LIVE_VARIANTS = {
  'raag-darbari-shrilal-shukla': {
    'paperback': '67709913825570',
    'hardcover': '67709913858338',
    'default': '67709913825570'
  },
  'godan-premchand': {
    'paperback': '67709593944354',
    'hardcover': '67709593977122',
    'default': '67709593944354'
  },
  'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap': {
    'paperback': '67709702504738',
    'default': '67709702504738'
  },
  'tarkash-javed-akhtar': {
    'hardcover': '67710011605282',
    'paperback': '67710011638050',
    'default': '67710011605282'
  }
};

const KNOWN_HANDLES = {
  'book-samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
  'samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
  'bharat-ka-samvidhan': 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
  'podium-godan': 'godan-premchand',
  'godan': 'godan-premchand',
  'hero-book-godan': 'godan-premchand',
  'podium-raag-darbari': 'raag-darbari-shrilal-shukla',
  'raag-darbari': 'raag-darbari-shrilal-shukla',
  'book-tarkash': 'tarkash-javed-akhtar',
  'tarkash': 'tarkash-javed-akhtar'
};

function resolveShopifyVariant(book, preferredFormat) {
  if (!book) return null;
  const fmt = String(preferredFormat || book.selectedFormat || book.binding || book.format || '').toLowerCase();
  
  if (book.variantId && String(book.variantId).match(/^\d+$/)) return String(book.variantId);
  if (book.variant_id && String(book.variant_id).match(/^\d+$/)) return String(book.variant_id);

  let lookupH = book.handle || KNOWN_HANDLES[book.id] || KNOWN_HANDLES[book.handle] || '';
  if (!lookupH && book.id && !String(book.id).startsWith('podium-') && !String(book.id).startsWith('book-') && !String(book.id).startsWith('hero-')) {
    lookupH = String(book.id);
  }

  if (lookupH && EXACT_LIVE_VARIANTS[lookupH]) {
    const map = EXACT_LIVE_VARIANTS[lookupH];
    if (fmt.indexOf('hard') !== -1 && map.hardcover) return map.hardcover;
    if (fmt.indexOf('paper') !== -1 && map.paperback) return map.paperback;
    return map.default || map.paperback || map.hardcover;
  }
  return null;
}

// Test cases
console.log("Test 1 - Raag Darbari Hardcover Deluxe:");
const rdHardcover = resolveShopifyVariant({ handle: 'raag-darbari-shrilal-shukla', title: 'Raag Darbari' }, 'Hardcover Deluxe');
console.log("  Resolved variant:", rdHardcover, "(Expected 67709913858338 - ₹1295)");
if (rdHardcover !== '67709913858338') throw new Error("Raag Darbari Hardcover mismatch!");

console.log("Test 2 - Raag Darbari Paperback:");
const rdPaperback = resolveShopifyVariant({ handle: 'raag-darbari-shrilal-shukla', title: 'Raag Darbari' }, 'Paperback');
console.log("  Resolved variant:", rdPaperback, "(Expected 67709913825570 - ₹499)");
if (rdPaperback !== '67709913825570') throw new Error("Raag Darbari Paperback mismatch!");

console.log("Test 3 - Bharat Ka Samvidhan:");
const samvidhan = resolveShopifyVariant({ id: 'bharat-ka-samvidhan' }, 'Paperback');
console.log("  Resolved variant:", samvidhan, "(Expected 67709702504738 - ₹195)");
if (samvidhan !== '67709702504738') throw new Error("Samvidhan mismatch!");

// Test Cart Deduplication
const mockCart = [
  { id: 'bharat-ka-samvidhan', title: 'Bharat Ka Samvidhan', qty: 1, price: 195, binding: 'Paperback' },
  { handle: 'raag-darbari-shrilal-shukla', title: 'Raag Darbari', qty: 2, price: 499, binding: 'Paperback' },
  { handle: 'raag-darbari-shrilal-shukla', title: 'Raag Darbari', qty: 1, price: 499, binding: 'Paperback' }
];

const resolvedItems = [];
mockCart.forEach(item => {
  const vid = resolveShopifyVariant(item, item.binding);
  resolvedItems.push({
    id: vid,
    quantity: item.qty
  });
});

const variantMap = {};
resolvedItems.forEach(it => {
  if (!it.id) return;
  const k = String(it.id);
  if (!variantMap[k]) {
    variantMap[k] = { id: k, quantity: 0 };
  }
  variantMap[k].quantity += it.quantity;
});
const payloadItems = Object.values(variantMap);
console.log("Test 4 - Cart Aggregation Payload:", payloadItems);
if (payloadItems.length !== 2) throw new Error("Cart aggregation failed to combine duplicates!");
if (payloadItems.find(p => p.id === '67709913825570').quantity !== 3) throw new Error("Quantity summing failed!");

console.log("ALL TESTS PASSED PERFECTLY!");
