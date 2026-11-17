const fs = require('fs');
const html = fs.readFileSync('preview.html', 'utf-8');

// Extract getFallbackCover function
const fnMatch = html.match(/function getFallbackCover\([\s\S]*?return 'data:image\/svg\+xml;charset=utf-8,' \+ encodeURIComponent\(svg\);\s*\}/);
eval(fnMatch[0]);

const titleSafe = "Jaane Jaan Lucknow";
const authorSafe = "Suboor Usmani";
const fallbackSvg = getFallbackCover(titleSafe, authorSafe);
const cover = "https://images.rajkamalprakashan.com/products/2026/10/22/be5f344c-82dc-4b9e-9bd0-55c58f81e88a-jaane-jaan-lucknow-front.jpg";

const cardHtml = `
<div style="width: 100%; aspect-ratio: 2 / 3; background-color: #FAF7F0; background-image: url(&quot;${fallbackSvg}&quot;); background-size: cover; background-position: center; border-radius: 8px; overflow: hidden; margin-bottom: 14px; box-shadow: -4px 8px 18px rgba(0,0,0,0.18); position: relative;">
  <img referrerpolicy="no-referrer" src="${cover}" alt="${titleSafe}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block;" onerror="this.onerror=null; this.src='${fallbackSvg}';" />
</div>
`;

console.log("Card HTML length:", cardHtml.length);
// Check if fallbackSvg has single quotes
console.log("fallbackSvg has single quotes:", fallbackSvg.includes("'"));
// Check if fallbackSvg has double quotes
console.log("fallbackSvg has double quotes:", fallbackSvg.includes('"'));
// Check if fallbackSvg has parentheses
console.log("fallbackSvg has parentheses:", fallbackSvg.includes('('), fallbackSvg.includes(')'));
