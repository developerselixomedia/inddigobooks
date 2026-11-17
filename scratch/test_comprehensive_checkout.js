const fs = require('fs');
const jsCode = fs.readFileSync('assets/main-store.js', 'utf8');
const vm = require('vm');

function createFreshEnv() {
  let fetchCalls = [];
  const mockCalls = [];

  function makeMockEl(id) {
    return {
      id: id || '',
      classList: {
        contains: () => false,
        add: (c) => mockCalls.push({ action: 'classAdd', id, c }),
        remove: (c) => mockCalls.push({ action: 'classRemove', id, c })
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
    SHOPIFY_LIVE_PRODUCTS: [],
    fbq: () => {}
  };

  const mockDoc = {
    getElementById: (id) => makeMockEl(id),
    querySelector: (sel) => makeMockEl(sel),
    querySelectorAll: () => [],
    createElement: (tag) => makeMockEl(tag),
    body: makeMockEl('body'),
    addEventListener: () => {}
  };

  const mockFetch = function(url, opts) {
    fetchCalls.push({ url, opts });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  };

  const context = vm.createContext({
    window: mockWindow,
    document: mockDoc,
    fetch: mockFetch,
    localStorage: { getItem: () => null, setItem: () => {} },
    console: console,
    setTimeout: setTimeout,
    clearTimeout: clearTimeout,
    requestAnimationFrame: (cb) => setTimeout(cb, 16),
    cancelAnimationFrame: (id) => clearTimeout(id),
    Math: Math, Array: Array, String: String, JSON: JSON,
    alert: console.log
  });

  vm.runInContext(jsCode, context);

  return { context, mockWindow, fetchCalls };
}

// Test 1: Raag Darbari Hardcover Deluxe
console.log('\n--- TEST 1: Buy Now on Raag Darbari Hardcover Deluxe (₹1295) ---');
const env1 = createFreshEnv();
env1.mockWindow.currentActiveBook = {
  id: 'podium-raag-darbari',
  handle: 'raag-darbari-shrilal-shukla',
  title: 'Raag Darbari',
  author: 'Shrilal Shukla',
  selectedPrice: 1295,
  selectedFormat: 'Hardcover',
  cover: 'cover.jpg'
};

env1.mockWindow.handleSoloBuyNow();

setTimeout(() => {
  const addCall1 = env1.fetchCalls.find(f => f.url.includes('/cart/add.js'));
  const body1 = JSON.parse(addCall1.opts.body);
  console.log('Added to Shopify Cart:', body1);
  if (body1.id !== '67709913858338') {
    throw new Error('Expected Raag Darbari Hardcover variant 67709913858338, got: ' + body1.id);
  }
  if (env1.mockWindow.location.href !== '/checkout') {
    throw new Error('Did not redirect to /checkout, href: ' + env1.mockWindow.location.href);
  }
  console.log('✅ TEST 1 PASSED: Raag Darbari Hardcover Deluxe (₹1295) mapped to REAL variant 67709913858338!');

  // Test 2: Proceed to Checkout from Cart Drawer with Multiple Books
  console.log('\n--- TEST 2: Proceed to Checkout from Cart Drawer (Multiple Books) ---');
  const env2 = createFreshEnv();
  
  // Add 1 copy of Bharat Ka Samvidhan and 2 copies of Raag Darbari via VM addToCart
  vm.runInContext(`
    cart = [
      {
        id: 'bharat-ka-samvidhan',
        handle: 'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
        title: 'Bharat Ka Samvidhan',
        author: 'Subhash Kashyap',
        price: 195,
        binding: 'Paperback',
        qty: 1
      },
      {
        id: 'raag-darbari-shrilal-shukla',
        handle: 'raag-darbari-shrilal-shukla',
        title: 'Raag Darbari',
        author: 'Shrilal Shukla',
        price: 499,
        binding: 'Paperback',
        qty: 2
      }
    ];
    proceedToCheckout();
  `, env2.context);

  setTimeout(() => {
    const addCall2 = env2.fetchCalls.find(f => f.url.includes('/cart/add.js'));
    const body2 = JSON.parse(addCall2.opts.body);
    console.log('Cart Drawer Add Payload:', body2);
    if (!body2.items || body2.items.length !== 2) {
      throw new Error('Expected 2 unique items in payload, got: ' + JSON.stringify(body2));
    }
    const samvidhanItem = body2.items.find(i => i.id === '67709702504738');
    const raagItem = body2.items.find(i => i.id === '67709913825570');
    if (!samvidhanItem || samvidhanItem.quantity !== 1) {
      throw new Error('Samvidhan item incorrect: ' + JSON.stringify(samvidhanItem));
    }
    if (!raagItem || raagItem.quantity !== 2) {
      throw new Error('Raag Darbari item incorrect: ' + JSON.stringify(raagItem));
    }
    if (env2.mockWindow.location.href !== '/checkout') {
      throw new Error('Did not redirect to /checkout, href: ' + env2.mockWindow.location.href);
    }
    console.log('✅ TEST 2 PASSED: Cart Drawer proceeded to checkout with 100% REAL variant IDs and correct quantities!');
    console.log('\n🎉 ALL REAL DATA CHECKOUT TESTS PASSED WITH 100% SUCCESS!');
    process.exit(0);
  }, 500);

}, 500);
