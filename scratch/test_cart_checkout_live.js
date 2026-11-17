const fs = require('fs');
const jsCode = fs.readFileSync('assets/main-store.js', 'utf8');

// Mock DOM & Browser Environment
const mockWindow = {
  location: {
    hostname: 'indigobooks.shop',
    pathname: '/',
    href: 'https://indigobooks.shop/'
  },
  addEventListener: function() {},
  removeEventListener: function() {},
  SHOPIFY_LIVE_PRODUCTS: [
    {
      id: 15399894745378,
      variantId: '67709588799778',
      variant_id: '67709588799778',
      title: '1084ven Ki Maan',
      handle: '1084ven-ki-maan-mahashweta-devi-tr-santwana-nigam'
    },
    {
      id: 15399894745379,
      variantId: '67709588799779',
      variant_id: '67709588799779',
      title: 'Bharat Ka Samvidhan : Sankshipt Parichay',
      handle: 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap'
    }
  ],
  fbq: function(act, evt, data) {
    mockCalls.push({ action: 'fbq', evt: evt, data: data });
  }
};

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

global.window = mockWindow;
global.document = {
  getElementById: function(id) { return makeMockEl(id); },
  querySelector: function(sel) { return makeMockEl(sel); },
  querySelectorAll: function() { return []; },
  createElement: function(tag) { return makeMockEl(tag); },
  body: makeMockEl('body'),
  addEventListener: function() {}
};
global.fetch = function(url, opts) {
  fetchCalls.push({ url: url, opts: opts });
  if (url.includes('/products/')) {
    return Promise.resolve({
      ok: true,
      json: () => Promise.resolve({
        variants: [{ id: 1234567890 }]
      })
    });
  }
  return Promise.resolve({
    ok: true,
    json: () => Promise.resolve({})
  });
};
const testCartData = [
  {
    id: 'book-samvidhan',
    title: 'Bharat Ka Samvidhan (भारत का संविधान)',
    author: 'Government of India / Dr. B.R. Ambedkar',
    price: 450,
    binding: 'Hardcover',
    qty: 1
  },
  {
    id: 'podium-raag-darbari',
    title: 'Raag Darbari',
    author: 'Shrilal Shukla',
    price: 499,
    binding: 'Paperback',
    qty: 2
  }
];

global.localStorage = {
  getItem: (k) => (k === 'indigo_cart' ? JSON.stringify(testCartData) : null),
  setItem: () => {}
};

console.log('Testing proceedToCheckout logic in main-store.js...');

// Evaluate the script functions in our mock environment
// Specifically extract and test getOrFetchVariantId and proceedToCheckout
const vm = require('vm');
const context = vm.createContext({
  window: mockWindow,
  document: global.document,
  fetch: global.fetch,
  localStorage: global.localStorage,
  console: console,
  requestAnimationFrame: (cb) => setTimeout(cb, 16),
  cancelAnimationFrame: (id) => clearTimeout(id),
  alert: (msg) => console.log('ALERT:', msg),
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  Math: Math,
  Array: Array,
  String: String,
  JSON: JSON,
  cart: [
    {
      id: 'book-samvidhan',
      title: 'Bharat Ka Samvidhan (भारत का संविधान)',
      author: 'Government of India / Dr. B.R. Ambedkar',
      price: 450,
      binding: 'Hardcover',
      qty: 1
    },
    {
      id: 'podium-raag-darbari',
      title: 'Raag Darbari',
      author: 'Shrilal Shukla',
      price: 499,
      binding: 'Paperback',
      qty: 2
    }
  ]
});

// Run file in vm
vm.runInContext(jsCode, context);

// Now populate cart and trigger proceedToCheckout
console.log('Populating cart with Bharat Ka Samvidhan and Raag Darbari...');
context.cart.push(
  {
    id: 'book-samvidhan',
    title: 'Bharat Ka Samvidhan (भारत का संविधान)',
    author: 'Government of India / Dr. B.R. Ambedkar',
    price: 450,
    binding: 'Hardcover',
    qty: 1
  },
  {
    id: 'podium-raag-darbari',
    title: 'Raag Darbari',
    author: 'Shrilal Shukla',
    price: 499,
    binding: 'Paperback',
    qty: 2
  }
);

console.log('Invoking proceedToCheckout()...');
context.proceedToCheckout();

setTimeout(() => {
  console.log('--- Verification Results ---');
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
    console.log('Items added to Shopify Cart:', body.items.map(it => ({
      id: it.id,
      qty: it.quantity,
      title: it.properties['Book Title']
    })));
  }

  if (hasClear && hasAdd && finalHref === '/checkout') {
    console.log('>>> ALL VERIFICATION CHECKS PASSED PERFECTLY! <<<');
    process.exit(0);
  } else {
    console.error('FAILED verification!');
    process.exit(1);
  }
}, 500);
