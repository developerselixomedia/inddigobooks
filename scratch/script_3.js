
    window.getFallbackCover = function(title, author) {
      var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').substring(0, 32);
      var a = (author || 'Indigo Classics').replace(/<[^>]*>/g, '').substring(0, 24);
      var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 450" width="100%" height="100%">' +
        '<rect width="300" height="450" fill="#1C1A17"/>' +
        '<rect x="12" y="12" width="276" height="426" fill="none" stroke="#E04F33" stroke-width="2"/>' +
        '<text x="150" y="210" font-family="serif" font-size="20" fill="#FAF8F5" font-weight="bold" text-anchor="middle">' + t + '</text>' +
        '<text x="150" y="245" font-family="sans-serif" font-size="13" fill="#D4AF37" text-anchor="middle">' + a + '</text>' +
        '</svg>';
      return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    };
    var getFallbackCover = window.getFallbackCover;
    window.getFallbackCoverSvg = window.getFallbackCover;
  