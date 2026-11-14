const fs = require('fs');
const js = fs.readFileSync('assets/main-store.js', 'utf8');

// Mock DOM
global.window = global;
global.window.addEventListener = () => {};
global.document = {
  getElementById: (id) => ({
    textContent: '',
    style: {},
    classList: { add: ()=>{}, remove: ()=>{} },
    setAttribute: ()=>{},
    getAttribute: ()=>''
  }),
  querySelectorAll: () => [],
  addEventListener: () => {}
};
global.localStorage = { getItem: () => null, setItem: () => {} };

eval(js);

console.log('Testing addToCart...');
try {
  window.addToCart('podium-godan');
  console.log('✓ addToCart succeeded without stack overflow! Cart count:', cart.length);
} catch (e) {
  console.error('❌ addToCart failed:', e);
  process.exit(1);
}

console.log('Testing search query "akh"...');
const pool = getUnifiedSearchPool();
console.log('Unified pool size:', pool.length);
const matches = [];
pool.forEach(b => {
  const t = (b.title || '').toLowerCase();
  const a = (b.author || b.vendor || '').toLowerCase();
  if (t.includes('akh') || a.includes('akh')) matches.push(b.title + ' by ' + (b.author || b.vendor));
});
console.log('✓ Matches found for "akh":', matches.length);
matches.slice(0, 5).forEach(m => console.log('  -', m));

console.log('Testing Piyush Mishra recommendations...');
const piyushRecs = pool.filter(b => (b.author || '').toLowerCase().includes('piyush') || (b.title || '').toLowerCase().includes('piyush'));
console.log('✓ Piyush Mishra books found:', piyushRecs.length);
piyushRecs.forEach(b => console.log('  -', b.title, '|', b.author, '|', b.price));
