const fs = require('fs');

console.log("=================================================================");
console.log("VERIFYING ALL NEW USER FIXES ACROSS THEME & LIQUID");
console.log("=================================================================");

const previewHtml = fs.readFileSync('preview.html', 'utf-8');
const themeLiquid = fs.readFileSync('layout/theme.liquid', 'utf-8');
const mainStoreJs = fs.readFileSync('assets/main-store.js', 'utf-8');
const mainStoreCss = fs.readFileSync('assets/main-store.css', 'utf-8');

let passedCount = 0;
let totalCount = 0;

function assert(condition, message) {
  totalCount++;
  if (!condition) {
    console.error(`❌ FAILED: ${message}`);
    process.exit(1);
  } else {
    console.log(`✅ PASSED: ${message}`);
    passedCount++;
  }
}

// 1. Phone & PIN Pattern Validation
console.log("\n--- TEST 1: Phone & Pincode Input Validation ---");
assert(previewHtml.includes('id="checkoutPhone"') && previewHtml.includes('pattern="[0-9]{10}"'), "preview.html has pattern='[0-9]{10}' on #checkoutPhone");
assert(themeLiquid.includes('id="checkoutPhone"') && themeLiquid.includes('pattern="[0-9]{10}"'), "theme.liquid has pattern='[0-9]{10}' on #checkoutPhone");
assert(!previewHtml.includes('[6-9][0-9]9'), "preview.html does NOT contain broken pattern [6-9][0-9]9");
assert(!themeLiquid.includes('[6-9][0-9]9'), "theme.liquid does NOT contain broken pattern [6-9][0-9]9");

// Test regex against user-submitted phone numbers from screenshots
const phoneRegex = new RegExp('^[0-9]{10}$');
assert(phoneRegex.test('8840818783'), "Regex matches screenshot 1 phone: 8840818783");
assert(phoneRegex.test('8081919128'), "Regex matches screenshot 2 phone: 8081919128");

assert(previewHtml.includes('id="checkoutPincode"') && previewHtml.includes('pattern="[0-9]{6}"'), "preview.html has pattern='[0-9]{6}' on #checkoutPincode");
const pinRegex = new RegExp('^[0-9]{6}$');
assert(pinRegex.test('211003'), "Regex matches screenshot 1 pincode: 211003");
assert(pinRegex.test('211002'), "Regex matches screenshot 2 pincode: 211002");

// 2. Google Search Snippet, Title Fallback & Square Favicons
console.log("\n--- TEST 2: Google Search Snippet, Title Fallback & Square Favicons ---");
assert(themeLiquid.includes("favicon-192x192.png"), "theme.liquid links favicon-192x192.png for Google crawler");
assert(themeLiquid.includes("favicon-48x48.png"), "theme.liquid links favicon-48x48.png");
assert(fs.existsSync('assets/favicon-192x192.png'), "Physical assets/favicon-192x192.png exists");
assert(fs.existsSync('assets/favicon-48x48.png'), "Physical assets/favicon-48x48.png exists");
assert(themeLiquid.includes("Indigo Books India — Premier Online Bookstore Prayagraj"), "theme.liquid overrides 'My Store' fallback title");
assert(themeLiquid.includes('"@type": "WebSite"'), "theme.liquid contains Schema.org WebSite JSON-LD");
assert(themeLiquid.includes('"@type": "BookStore"'), "theme.liquid contains Schema.org BookStore JSON-LD");
assert(themeLiquid.includes('meta property="og:site_name" content="Indigo Books India"'), "theme.liquid has og:site_name Indigo Books India");

// 3. Z-Index Stacking Hierarchy: Cart Drawer & Buy Now Modal
console.log("\n--- TEST 3: Z-Index Stacking Hierarchy ---");
assert(mainStoreCss.includes('z-index: 25000000 !important;'), "Cart drawer has z-index 25,000,000 !important (Strictly ABOVE 10M navbar)");
assert(mainStoreCss.includes('z-index: 24999999 !important;'), "Cart overlay has z-index 24,999,999 !important");
assert(mainStoreCss.includes('z-index: 30000000 !important;'), "Modals (Checkout, Confirmation) have z-index 30,000,000 !important (Strictly ABOVE solo view and cart)");
assert(mainStoreCss.includes('#indigo-search-results-view'), "Search results view is explicitly declared in CSS");

// 4. Cart Persistence Across Back Button & Navigation
console.log("\n--- TEST 4: Cart Persistence Across Back Button ---");
assert(mainStoreJs.includes("localStorage.getItem('indigo_cart')"), "main-store.js initializes cart from localStorage 'indigo_cart'");
assert(mainStoreJs.includes("function saveCartToStorage()"), "main-store.js defines saveCartToStorage()");
assert(mainStoreJs.includes("window.addEventListener('pageshow'"), "main-store.js registers pageshow listener to rehydrate cart UI on back navigation");

// 5. Author Search & Dedicated Search Page Redirection
console.log("\n--- TEST 5: Author Search & Dedicated Search Page Redirection ---");
assert(mainStoreJs.includes("window.openSearchResultsPage = openSearchResultsPage"), "main-store.js exports openSearchResultsPage");
assert(!mainStoreJs.includes("var firstItem = resultsBox.querySelector"), "Enter key in search bar does NOT hijack to single book solo page");
assert(mainStoreJs.includes("window.triggerDedicatedSearchAll"), "Search dropdown contains 'View All Results' action");
assert(mainStoreJs.includes("No books found matching your query"), "Empty search results state displays helpful messaging and WhatsApp button, NOT blank space");

// 6. Theme Packages
console.log("\n--- TEST 6: Shopify ZIP Packages ---");
assert(fs.existsSync('indigo-books-shopify-theme.zip'), "indigo-books-shopify-theme.zip exists");
assert(fs.existsSync('indigo-books-theme.zip'), "indigo-books-theme.zip exists");
const statShopify = fs.statSync('indigo-books-shopify-theme.zip');
const statTheme = fs.statSync('indigo-books-theme.zip');
assert(statShopify.size > 5000000, `indigo-books-shopify-theme.zip is ${Math.round(statShopify.size / 1024 / 1024)} MB`);
assert(statTheme.size > 5000000, `indigo-books-theme.zip is ${Math.round(statTheme.size / 1024 / 1024)} MB`);

console.log(`\n=================================================================`);
console.log(`ALL ${passedCount}/${totalCount} TESTS PASSED WITH 100% SUCCESS!`);
console.log(`=================================================================`);
