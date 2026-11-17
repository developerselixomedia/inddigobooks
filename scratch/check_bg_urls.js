const fs = require('fs');
const html = fs.readFileSync('preview.html', 'utf-8');

// Check all occurrences of fallbackSvg in preview.html
const matches = html.match(/background-image:\s*url\([^)]+\)/g);
console.log('Total background-image url occurrences:', matches ? matches.length : 0);
if (matches) {
  matches.slice(0, 10).forEach(m => console.log('  ', m.substring(0, 80)));
}
