// test_search_simulation.js
const fs = require('fs');

const js = fs.readFileSync('assets/main-store.js', 'utf-8');

// Simulate the browser environment
const window = {
  location: { pathname: '/products/bharat-ka-samvidhan' },
  addEventListener: () => {},
  scrollTo: () => {}
};

const document = {
  getElementById: (id) => {
    return {
      id: id,
      style: {},
      addEventListener: (evt, fn) => {
        if (!window.__handlers) window.__handlers = {};
        window.__handlers[evt] = fn;
      },
      dispatchEvent: () => {},
      querySelectorAll: () => []
    };
  },
  addEventListener: () => {}
};

// Evaluate the script in this mock context
try {
  eval(js);
  console.log("main-store.js evaluated successfully in Node!");
} catch (e) {
  console.error("Evaluation error:", e);
}

// Now test setupPredictiveSearch
console.log("Checking window.MASTER_SEARCH_CATALOG length:", window.MASTER_SEARCH_CATALOG ? window.MASTER_SEARCH_CATALOG.length : 'undefined');

// Test searching 'prem'
const query = 'prem';
const pool = (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) ? window.MASTER_SEARCH_CATALOG : [];
console.log("Pool size:", pool.length);

const matches = [];
for (let i = 0; i < pool.length; i++) {
  const item = pool[i];
  const title = (item.title || '').toLowerCase();
  const author = (item.author || item.vendor || '').toLowerCase();
  const isbn = (item.isbn || item.sku || '').toLowerCase();

  if (title.indexOf(query) !== -1 || author.indexOf(query) !== -1 || isbn.indexOf(query) !== -1) {
    matches.push(item);
    if (matches.length >= 8) break;
  }
}

console.log("Matches found for 'prem':", matches.length);
matches.forEach(m => console.log(" -", m.title, "by", m.author));
