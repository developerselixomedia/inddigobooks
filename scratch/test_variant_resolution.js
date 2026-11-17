// Node test to verify variant lookup logic against preview.html data
const fs = require('fs');

const html = fs.readFileSync('preview.html', 'utf-8');

// Extract MASTER_SEARCH_CATALOG
const mMatch = html.match(/window\.MASTER_SEARCH_CATALOG\s*=\s*(\[[\s\S]*?\]);/);
if (!mMatch) {
  console.error("MASTER_SEARCH_CATALOG not found");
  process.exit(1);
}

const catalog = JSON.parse(mMatch[1]);
console.log("Loaded catalog size:", catalog.length);

function testBookVariants(queryTitle, clickedIsbn) {
  console.log(`\n================================`);
  console.log(`Testing: "${queryTitle}" (Clicked ISBN: ${clickedIsbn})`);

  // 1. Find clicked book
  let found = catalog.find(b => b.isbn === clickedIsbn) || catalog.find(b => (b.title || '').toLowerCase().includes(queryTitle.toLowerCase()));
  if (!found) {
    console.error("Book not found!");
    return;
  }
  console.log(`Found clicked book: ${found.title} | ${found.binding} | ₹${found.rawPrice || found.mrp} | ISBN: ${found.isbn}`);

  // 2. Sibling Variant Resolution
  const normTitle = String(found.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
  let pbVariant = null;
  let hcVariant = null;

  for (let i = 0; i < catalog.length; i++) {
    const item = catalog[i];
    const itNorm = String(item.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    if (itNorm === normTitle) {
      const b = String(item.binding || item.format || '').toLowerCase();
      if (b.includes('hard')) {
        if (!hcVariant) hcVariant = item;
      } else {
        if (!pbVariant) pbVariant = item;
      }
    }
    if (pbVariant && hcVariant) break;
  }

  const clickedBinding = String(found.binding || found.format || '').toLowerCase();
  const isClickedHc = clickedBinding.includes('hard');
  if (isClickedHc && !hcVariant) hcVariant = found;
  if (!isClickedHc && !pbVariant) pbVariant = found;

  const initialFmt = (isClickedHc && hcVariant) ? 'Hardcover' : (pbVariant ? 'Paperback' : (hcVariant ? 'Hardcover' : 'Paperback'));

  console.log("Variant Resolution Result:");
  console.log(" - Initial Format:", initialFmt);
  console.log(" - PB Variant:", pbVariant ? `₹${pbVariant.rawPrice || pbVariant.mrp} (ISBN: ${pbVariant.isbn})` : 'NONE');
  console.log(" - HC Variant:", hcVariant ? `₹${hcVariant.rawPrice || hcVariant.mrp} (ISBN: ${hcVariant.isbn})` : 'NONE');

  // Verify applyFormat
  function getVariantData(fmt) {
    const currentVar = (fmt === 'Hardcover' && hcVariant) ? hcVariant : (pbVariant || found);
    const exactPrice = currentVar.rawPrice || currentVar.mrp || (parseFloat(String(currentVar.price).replace(/[^0-9.]/g, '')) || 299);
    const exactIsbn = currentVar.isbn || currentVar.sku || found.isbn;
    return { fmt, price: exactPrice, isbn: exactIsbn };
  }

  const initData = getVariantData(initialFmt);
  console.log(` - When opened (${initialFmt}): ₹${initData.price} | ISBN: ${initData.isbn}`);

  if (initialFmt === 'Hardcover' && pbVariant) {
    const toggled = getVariantData('Paperback');
    console.log(` - When toggled to Paperback: ₹${toggled.price} | ISBN: ${toggled.isbn}`);
  } else if (initialFmt === 'Paperback' && hcVariant) {
    const toggled = getVariantData('Hardcover');
    console.log(` - When toggled to Hardcover: ₹${toggled.price} | ISBN: ${toggled.isbn}`);
  }
}

// Test 1: Jaag Piyari Hardcover (User's exact screenshot)
testBookVariants("Jaag Piyari Ab Ka Sovai", "9789377470036");

// Test 2: Jaag Piyari Paperback
testBookVariants("Jaag Piyari Ab Ka Sovai", "9789377470043");

// Test 3: Karbala (Only Paperback in catalog)
testBookVariants("Karbala", "9788197989650");
