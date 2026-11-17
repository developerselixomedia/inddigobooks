const fs = require('fs');
const html = fs.readFileSync('preview.html', 'utf-8');

const fnMatch = html.match(/function getFallbackCoverSvg\([\s\S]*?return 'data:image\/svg\+xml;charset=utf-8,' \+ encodeURIComponent\(svg\);\s*\}/);
eval(fnMatch[0]);

const dataUri = getFallbackCoverSvg("Jaane Jaan Lucknow", "Suboor Usmani");
console.log("dataUri created, length:", dataUri.length);

const decoded = decodeURIComponent(dataUri.replace('data:image/svg+xml;charset=utf-8,', ''));
console.log("Contains Title 'Jaane Jaan Lucknow':", decoded.includes("Jaane Jaan Lucknow"));
console.log("Contains Author 'Suboor Usmani':", decoded.includes("Suboor Usmani"));
console.log("Contains 'INDIGO ARCHIVE':", decoded.includes("INDIGO ARCHIVE"));
