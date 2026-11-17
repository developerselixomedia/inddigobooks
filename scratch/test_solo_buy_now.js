const fs = require('fs');
const jsCode = fs.readFileSync('assets/main-store.js', 'utf8');
const vm = require('vm');

const mockCalls = [];
let fetchCalls = [];

function makeMockEl(id) {
  return {
    id: id || '',
    classList: {
      contains: () => false,
      add: (c) => mockCalls.push({ action: 'classAdd', id: id, cls: c }),
      remove: (c) => mockCalls.push({ action: 'classRemove', id: id, cls: c })
    },
    style: {},
    getAttribute: () => null,
    setAttribute: () => {},
    addEventListener: () => {},
    querySelector: (s) => makeMockEl(s),
    querySelectorAll: () => [],
    appendChild: () => {},
    removeChild: () => {},
    getBoundingClientRect: () => ({ top: 0, bottom: 500, left: 0, right: 500, width: 500, height: 500 }),
    value: '',
    innerHTML: '',
    textContent: ''
  };
}

const mockWindow = {
  location: {
    hostname: 'indigobooks.shop',
    pathname: '/',
    href: 'https://indigobooks.shop/'
  },
  addEventListener: () => {},
  removeEventListener: () => {},
  SHOPIFY_LIVE_PRODUCTS: [
    {
      id: 15399894745378,
      variantId: '67709588799778',
      variant_id: '67709588799778',
      title: 'Raag Darbari',
      handle: 'raag-darbari-shrilal-shukla'
    }
  ],
  fbq: (act, evt, data) => mockCalls.push({ action: 'fbq', evt, data })
};

global.window = mockWindow;
global.document = {
  getElementById: (id) => makeMockEl(id),
  querySelector: (sel) => makeMockEl(sel),
  querySelectorAll: () => [],
  createElement: (tag) => makeMockEl(tag),
  body: makeMockEl('body'),
  addEventListener: () => {}
};
global.fetch = function(url, opts) {
  fetchCalls.push({ url: url, opts: opts });
  return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
};
global.localStorage = { getItem: () => null, setItem: () => {} };

const context = vm.createContext({
  window: mockWindow,
  document: global.document,
  fetch: global.fetch,
  localStorage: global.localStorage,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  requestAnimationFrame: (cb) => setTimeout(cb, 16),
  cancelAnimationFrame: (id) => clearTimeout(id),
  Math: Math, Array: Array, String: String, JSON: JSON,
  alert: console.log
});

vm.runInContext(jsCode, context);

// Test 1: Open solo book page for Raag Darbari and click Buy Now
console.log('Testing handleSoloBuyNow()...');
mockWindow.currentActiveBook = {
  id: 'podium-raag-darbari',
  title: 'Raag Darbari',
  author: 'Shrilal Shukla',
  price: '₹499.00',
  rawPrice: 499,
  binding: 'Hardcover',
  cover: 'cover.jpg'
};

mockWindow.handleSoloBuyNow();

setTimeout(() => {
  console.log('--- Buy Now Results ---');
  console.log('Fetch calls:', fetchCalls.map(f => f.url));
  const hasClear = fetchCalls.some(f => f.url.includes('/cart/clear.js'));
  const hasAdd = fetchCalls.some(f => f.url.includes('/cart/add.js'));
  const finalHref = mockWindow.location.href;

  console.log('Did call /cart/clear.js:', hasClear);
  console.log('Did call /cart/add.js:', hasAdd);
  console.log('Target location.href:', finalHref);

  const addCall = fetchCalls.find(f => f.url.includes('/cart/add.js'));
  if (addCall) {
    const body = JSON.parse(addCall.opts.body);
    console.log('Item added to Shopify Cart:', body);
  }

  if (hasClear && hasAdd && finalHref === '/checkout') {
    console.log('>>> BUY NOW DIRECT TO CHECKOUT VERIFIED! <<<');
    process.exit(0);
  } else {
    console.error('FAILED Buy Now verification!');
    process.exit(1);
  }
}, 500);
