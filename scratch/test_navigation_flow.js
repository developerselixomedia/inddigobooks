const fs = require('fs');
const { JSDOM } = require('jsdom');

console.log("=== RUNNING NAVIGATION STATE MACHINE AUTOMATED TEST SUITE ===");

const html = fs.readFileSync('preview.html', 'utf-8');
const dom = new JSDOM(html, {
  runScripts: "dangerously",
  resources: "usable",
  url: "https://www.indigobooksindia.com/"
});

const { window } = dom;
const { document } = window;

function assert(condition, message) {
  if (!condition) {
    console.error("❌ FAILED: " + message);
    process.exit(1);
  } else {
    console.log("✓ PASSED: " + message);
  }
}

// Wait for initial store initialization
setTimeout(() => {
  try {
    const sView = document.getElementById('indigo-search-results-view');
    const hView = document.getElementById('homepage-view');
    const soloView = document.getElementById('indigo-solo-product-view');
    const editorialSearchInput = document.getElementById('editorialSearchInput');
    const resultsSearchInput = document.getElementById('results-search-input');

    assert(sView !== null, "Search results view element exists");
    assert(hView !== null, "Homepage view element exists");
    assert(soloView !== null, "Solo product view element exists");
    assert(editorialSearchInput !== null, "editorialSearchInput exists");

    console.log("\n--- TEST 1: User performs search for ISBN 9789377374068 ---");
    window.performDedicatedSearch('9789377374068');
    assert(sView.style.display === 'block', "Search results view is DISPLAY: BLOCK");
    assert(hView.style.display === 'none', "Homepage view is DISPLAY: NONE");
    assert(editorialSearchInput.value === '9789377374068', "editorialSearchInput holds search query");
    assert(window.previousViewBeforeSolo === 'search', "window.previousViewBeforeSolo is 'search'");

    console.log("\n--- TEST 2: User clicks bookstore logo to return to Homepage ---");
    window.returnToHome();
    assert(sView.style.display === 'none', "Search results view is DISPLAY: NONE after returnToHome");
    assert(hView.style.display === 'block', "Homepage view is DISPLAY: BLOCK after returnToHome");
    assert(editorialSearchInput.value === '', "editorialSearchInput is CLEARED after returnToHome");
    assert(resultsSearchInput.value === '', "resultsSearchInput is CLEARED after returnToHome");
    assert(window.previousViewBeforeSolo === 'home', "window.previousViewBeforeSolo is reset to 'home'");

    console.log("\n--- TEST 3: User clicks 'Gaban' on Homepage to open Solo Book Page ---");
    window.openSoloBookPage('book-gaban');
    assert(soloView.style.display === 'block', "Solo product view is active");
    assert(sView.style.display === 'none', "Search view remains hidden");
    assert(hView.style.display === 'none', "Homepage view is hidden while solo is active");

    console.log("\n--- TEST 4: User clicks '<- Back' on 'Gaban' ---");
    window.closeSoloBookPage();
    assert(soloView.style.display === 'none', "Solo product view is closed");
    assert(hView.style.display === 'block', "Homepage view is RESTORED cleanly");
    assert(sView.style.display === 'none', "CRITICAL: Search view DID NOT reopen when returning from homepage book!");
    assert(window.previousViewBeforeSolo === 'home', "window.previousViewBeforeSolo remains 'home'");

    console.log("\n--- TEST 5: User clicks another book ('Kuchh Ishq...') from Homepage ---");
    window.openSoloBookPage('podium-kuchh-ishq');
    assert(soloView.style.display === 'block', "Solo product view is active for Kuchh Ishq");
    window.handleSoloAddToCart();
    window.closeSoloBookPage();
    assert(hView.style.display === 'block', "Homepage view is STILL restored cleanly");
    assert(sView.style.display === 'none', "Search view did NOT reopen after Kuchh Ishq");

    console.log("\n--- TEST 6: User searches again and opens a book FROM search view ---");
    window.performDedicatedSearch('Premchand');
    assert(sView.style.display === 'block', "Search view active for Premchand");
    window.openSoloBookPage('podium-godan');
    assert(soloView.style.display === 'block', "Godan opened from search results");
    window.closeSoloBookPage();
    assert(sView.style.display === 'block', "Search results view correctly restored when closing book opened from search");

    console.log("\n--- TEST 7: User clicks '<- Back to Bookstore' on Search Results Page ---");
    window.closeSearchResultsView();
    assert(sView.style.display === 'none', "Search view is closed");
    assert(hView.style.display === 'block', "Homepage view is open");
    assert(editorialSearchInput.value === '', "editorialSearchInput is cleared");
    assert(window.previousViewBeforeSolo === 'home', "previousViewBeforeSolo is reset to 'home'");

    console.log("\n--- TEST 8: Opening book after Back to Bookstore ---");
    window.openSoloBookPage('podium-chitralekha');
    window.closeSoloBookPage();
    assert(hView.style.display === 'block', "Homepage view remains open");
    assert(sView.style.display === 'none', "Search view never opens unexpectedly");

    console.log("\n🎉 ALL 8 NAVIGATION STATE MACHINE TESTS PASSED WITH 100% SUCCESS!");
    process.exit(0);
  } catch (err) {
    console.error("Test execution error:", err);
    process.exit(1);
  }
}, 500);
