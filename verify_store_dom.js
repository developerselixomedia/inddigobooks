// Extract scripts from preview.html and test DOM simulation
const fs = require('fs');

console.log("Reading preview.html...");
const html = fs.readFileSync('preview.html', 'utf-8');

// Check script blocks
const scriptMatches = [...html.matchAll(/<script(?:\s+id="([^"]+)")?[^>]*>([\s\S]*?)<\/script>/gi)];
console.log(`Found ${scriptMatches.length} script tags in preview.html`);

const elements = {};
function createMockElement(id, tag = 'div') {
  return {
    id: id,
    tagName: tag.toUpperCase(),
    style: {
      setProperty: function(k, v) { this[k] = v; }
    },
    classList: {
      _classes: new Set(),
      add: function(c) { this._classes.add(c); },
      remove: function(c) { this._classes.delete(c); },
      contains: function(c) { return this._classes.has(c); },
      toggle: function(c) {
        if (this._classes.has(c)) { this._classes.delete(c); return false; }
        else { this._classes.add(c); return true; }
      }
    },
    setAttribute: function(k, v) { this[k] = v; },
    getAttribute: function(k) { return this[k] || null; },
    addEventListener: function() {},
    appendChild: function() {},
    querySelector: function() { return null; },
    querySelectorAll: function() { return []; },
    getBoundingClientRect: function() {
      return { top: 100, bottom: 500, left: 0, right: 1000, width: 1000, height: 400 };
    },
    innerHTML: '',
    textContent: '',
    value: ''
  };
}

const mockDoc = {
  getElementById: function(id) {
    if (!elements[id]) {
      elements[id] = createMockElement(id);
    }
    return elements[id];
  },
  createElement: function(tag) {
    return createMockElement('el_' + Math.random(), tag);
  },
  body: createMockElement('body'),
  documentElement: createMockElement('html'),
  addEventListener: function() {},
  querySelectorAll: function() { return []; },
  querySelector: function() { return null; }
};

const mockWin = {
  document: mockDoc,
  location: { pathname: '/', hash: '' },
  history: { pushState: function() {} },
  scrollTo: function() {},
  addEventListener: function() {},
  innerWidth: 1440,
  innerHeight: 900,
  requestAnimationFrame: function(cb) { return setTimeout(cb, 16); },
  cancelAnimationFrame: function(id) { clearTimeout(id); },
  cleanPrice: function(v, fb) {
    var n = parseFloat(String(v || '').replace(/[^0-9.]/g, ''));
    return isNaN(n) || n <= 0 ? (fb || 299) : n;
  }
};

global.window = mockWin;
global.document = mockDoc;
global.localStorage = { getItem: () => null, setItem: () => null };
global.requestAnimationFrame = mockWin.requestAnimationFrame;

// Let's run scripts 2, 3, 4 (database + scripts, master, editorial)
for (let i = 2; i < scriptMatches.length; i++) {
  const sId = scriptMatches[i][1] || ('script_' + i);
  const code = scriptMatches[i][2];
  console.log(`Evaluating script: ${sId} (${code.length} chars)`);
  try {
    const fn = new Function('window', 'document', 'localStorage', 'requestAnimationFrame', code);
    fn(mockWin, mockDoc, global.localStorage, mockWin.requestAnimationFrame);
    console.log(` -> ${sId} evaluated successfully!`);
  } catch (err) {
    console.error(` -> ERROR in ${sId}:`, err.message);
    process.exit(1);
  }
}

console.log("\n--- Testing Solo Book Page Opening ---");
try {
  mockWin.openSoloBookPage('podium-godan');
  console.log("PASS: openSoloBookPage('podium-godan') ran without error!");
  const soloView = elements['indigo-solo-product-view'];
  console.log("indigo-solo-product-view display:", soloView.style.display);
  console.log("indigo-solo-product-view classes:", [...soloView.classList._classes]);
  console.log("v2SoloTitle textContent:", elements['v2SoloTitle'].textContent);
  console.log("v2SoloPrice textContent:", elements['v2SoloPrice'].textContent);
} catch (err) {
  console.error("FAIL: openSoloBookPage threw:", err);
  process.exit(1);
}

console.log("\n--- Testing openDedicatedProductPage Alias ---");
try {
  mockWin.openDedicatedProductPage('podium-raag-darbari');
  console.log("PASS: openDedicatedProductPage('podium-raag-darbari') ran without recursion!");
  console.log("v2SoloTitle textContent:", elements['v2SoloTitle'].textContent);
  console.log("v2SoloPrice textContent:", elements['v2SoloPrice'].textContent);
} catch (err) {
  console.error("FAIL: openDedicatedProductPage threw:", err);
  process.exit(1);
}

console.log("\n--- Testing 3D Book Spread Toggle ---");
try {
  mockWin.toggleSoloBookSpread(true);
  console.log("PASS: toggleSoloBookSpread(true) ran!");
  const spreadStage = elements['v2BookSpreadStage'];
  console.log("v2BookSpreadStage has is-open:", spreadStage.classList.contains('is-open'));
  console.log("v2ViewDetails display:", elements['v2ViewDetails'].style.display);
  console.log("v2ViewExcerpt display:", elements['v2ViewExcerpt'].style.display);
  
  mockWin.toggleSoloBookSpread(false);
  console.log("PASS: toggleSoloBookSpread(false) ran!");
  console.log("v2BookSpreadStage has is-open:", spreadStage.classList.contains('is-open'));
  console.log("v2ViewDetails display:", elements['v2ViewDetails'].style.display);
  console.log("v2ViewExcerpt display:", elements['v2ViewExcerpt'].style.display);
} catch (err) {
  console.error("FAIL: toggleSoloBookSpread threw:", err);
  process.exit(1);
}

console.log("\n--- Testing 1-Click Buy / Express Phone Checkout ---");
try {
  mockWin.openQuickOrderModal('podium-godan');
  console.log("PASS: openQuickOrderModal('podium-godan') ran!");
  const expModal = elements['indigo-express-checkout-modal'] || elements['expressPhoneCheckoutModal'];
  console.log("expressPhoneCheckoutModal display:", expModal.style.display);
  console.log("checkoutOrderTotal textContent:", elements['checkoutOrderTotal'].textContent);
} catch (err) {
  console.error("FAIL: openQuickOrderModal threw:", err);
  process.exit(1);
}

console.log("\n--- Testing Close Solo Book Page ---");
try {
  mockWin.closeSoloBookPage();
  console.log("PASS: closeSoloBookPage() ran!");
  const soloView = elements['indigo-solo-product-view'];
  console.log("indigo-solo-product-view display:", soloView.style.display);
} catch (err) {
  console.error("FAIL: closeSoloBookPage threw:", err);
  process.exit(1);
}

console.log("\n==============================================");
console.log("--- Testing Format Pills (Paperback vs Hardcover Deluxe) ---");
mockWin.openSoloBookPage('podium-raag-darbari');
console.log('Opened Raag Darbari Base Price:', elements['v2SoloPrice'].textContent);

// Click Hardcover Deluxe
console.log('Clicking Hardcover Deluxe...');
elements['v2FormatHardcover'].onclick({ stopPropagation: function() {} });
console.log('Hardcover Deluxe Price:', elements['v2SoloPrice'].textContent);
console.log('Hardcover Deluxe Format:', elements['v2MetaFormat'].textContent);

if (!elements['v2FormatHardcover'].classList.contains('active')) {
  throw new Error('Hardcover Deluxe did not get active class!');
}
if (elements['v2SoloPrice'].textContent !== '₹649.00') {
  throw new Error('Hardcover price did not increase to ₹649.00 (+150)!');
}

// Click Paperback
console.log('Clicking Paperback...');
elements['v2FormatPaperback'].onclick({ stopPropagation: function() {} });
console.log('Paperback Price:', elements['v2SoloPrice'].textContent);
if (!elements['v2FormatPaperback'].classList.contains('active')) {
  throw new Error('Paperback did not get active class!');
}
if (elements['v2SoloPrice'].textContent !== '₹499.00') {
  throw new Error('Paperback price did not restore to ₹499.00!');
}
console.log('PASS: Format pills are fully interactive with live price & format switching!');

console.log("ALL JS TESTS PASSED CLEANLY WITH ZERO ERRORS!");
console.log("==============================================");
process.exit(0);
