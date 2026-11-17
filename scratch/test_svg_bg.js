const fs = require('fs');
const html = fs.readFileSync('preview.html', 'utf-8');

const fnMatch = html.match(/function getFallbackCoverSvg\([\s\S]*?return 'data:image\/svg\+xml;charset=utf-8,' \+ encodeURIComponent\(svg\);\s*\}/);
console.log('Found getFallbackCoverSvg:', !!fnMatch);

eval(fnMatch[0]);
const svgUrl = getFallbackCoverSvg('Jaag Piyari Ab Ka Sovai', 'Suman Jain');
console.log('URL length:', svgUrl.length);
console.log('URL start:', svgUrl.substring(0, 100));

// Test what happens in CSS when you set style.backgroundImage = 'url(' + soloFallbackSvg + ')'
// NOTICE: It's 'url(' + soloFallbackSvg + ')' WITHOUT quotes around the data: URI!
console.log("Without quotes: url(" + svgUrl.substring(0, 50) + "... )");
console.log("With quotes: url('" + svgUrl.substring(0, 50) + "... ')");
