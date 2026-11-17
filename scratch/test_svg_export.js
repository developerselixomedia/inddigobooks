const fs = require('fs');

function getFallbackCoverSvg(title, author) {
  var palettes = [
    { top: '#3E1715', bot: '#180706', gold: '#E5C07B', text: '#FAF7F2' },
    { top: '#15263D', bot: '#0A131F', gold: '#D4AF37', text: '#F8FAFC' },
    { top: '#1A2E22', bot: '#0B150F', gold: '#C5A059', text: '#F4F7F4' },
    { top: '#2D182A', bot: '#140813', gold: '#E0B084', text: '#FBF5F8' },
    { top: '#222035', bot: '#0D0C17', gold: '#DFB76C', text: '#F6F5FA' }
  ];
  var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
  var a = (author || 'Curated Edition').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
  
  var h = 0;
  for (var k = 0; k < t.length; k++) h = (h + t.charCodeAt(k)) % palettes.length;
  var pal = palettes[h];
  
  var words = t.split(/\s+/);
  var lines = [];
  var curr = '';
  for (var w = 0; w < words.length; w++) {
    var word = words[w];
    if ((curr + ' ' + word).trim().length <= 16) {
      curr = (curr + ' ' + word).trim();
    } else {
      if (curr) lines.push(curr);
      curr = word;
    }
  }
  if (curr) lines.push(curr);
  if (lines.length > 3) {
    lines = lines.slice(0, 2);
    lines.push(words.slice(lines.join(' ').split(/\s+/).length).join(' ').substring(0, 13) + '...');
  }
  
  var startY = 135 - ((lines.length - 1) * 11);
  var titleSvg = '';
  for (var i = 0; i < lines.length; i++) {
    var y = startY + (i * 22);
    titleSvg += '<text x="100" y="' + y + '" fill="' + pal.text + '" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">' + lines[i] + '</text>';
  }
  
  var authorY = startY + (lines.length * 22) + 14;
  var authorStr = a.substring(0, 22);
  
  var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" width="100%" height="100%">' +
    '<defs>' +
      '<linearGradient id="ev_g_' + h + '" x1="0%" y1="0%" x2="100%" y2="100%">' +
        '<stop offset="0%" stop-color="' + pal.top + '"/>' +
        '<stop offset="100%" stop-color="' + pal.bot + '"/>' +
      '</linearGradient>' +
    '</defs>' +
    '<rect width="200" height="300" rx="3" fill="url(#ev_g_' + h + ')"/>' +
    '<rect x="0" y="0" width="10" height="300" fill="rgba(0,0,0,0.3)"/>' +
    '<line x1="10" y1="0" x2="10" y2="300" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>' +
    '<rect x="16" y="16" width="168" height="268" rx="2" fill="none" stroke="' + pal.gold + '" stroke-width="1.2" opacity="0.85"/>' +
    '<rect x="19" y="19" width="162" height="262" rx="1" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.6"/>' +
    '<circle cx="100" cy="58" r="22" fill="none" stroke="' + pal.gold + '" stroke-width="1"/>' +
    '<circle cx="100" cy="58" r="18" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.7"/>' +
    '<text x="100" y="63" fill="' + pal.gold + '" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">IB</text>' +
    '<text x="100" y="94" fill="' + pal.gold + '" font-family="sans-serif" font-size="7.5" font-weight="700" letter-spacing="1.5" text-anchor="middle">INDIGO ARCHIVE</text>' +
    titleSvg +
    '<line x1="60" y1="' + (authorY - 6) + '" x2="140" y2="' + (authorY - 6) + '" stroke="' + pal.gold + '" stroke-width="0.75" opacity="0.5"/>' +
    '<text x="100" y="' + (authorY + 8) + '" fill="' + pal.gold + '" font-family="sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">By ' + authorStr + '</text>' +
    '<text x="100" y="266" fill="#888888" font-family="sans-serif" font-size="7" letter-spacing="1.2" text-anchor="middle">PRAYAGRAJ &bull; INDIA</text>' +
  '</svg>';
  return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

const data = getFallbackCoverSvg('Jaag Piyari Ab Ka Sovai', 'Suman Jain');
fs.writeFileSync('scratch/jaag_piyari_svg.html', `<div style="width:200px;height:300px;background-image:url('${data}');background-size:cover;"></div>`);
console.log('Saved scratch/jaag_piyari_svg.html');
