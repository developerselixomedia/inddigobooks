with open('store_scripts.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = """function getAssetUrl(url, bookId) {
  if (!url && !bookId) return '';
  if (bookId && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[bookId]) {
    return window.PODIUM_CDN_COVERS[bookId];
  }
  if (url && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[url]) {
    return window.PODIUM_CDN_COVERS[url];
  }
  if (!url) return '';
  if (url.startsWith('//')) {
    return 'https:' + url;
  }
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }"""

replacement = """function getAssetUrl(url, bookId) {
  if (!url && !bookId) return '';
  // Intercept dead remote host to eliminate net::ERR_CONNECTION_CLOSED
  if (url && (url.includes('images.rajkamalprakashan.com') || url.includes('rajkamalprakashan.com'))) {
    if (bookId && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[bookId]) {
      return window.PODIUM_CDN_COVERS[bookId];
    }
    if (typeof getFallbackCover === 'function') {
      return getFallbackCover(bookId || 'Indigo Books Edition', 'Prayagraj Classic');
    }
    return '';
  }
  if (bookId && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[bookId]) {
    return window.PODIUM_CDN_COVERS[bookId];
  }
  if (url && typeof window !== 'undefined' && window.PODIUM_CDN_COVERS && window.PODIUM_CDN_COVERS[url]) {
    return window.PODIUM_CDN_COVERS[url];
  }
  if (!url) return '';
  if (url.startsWith('//')) {
    return 'https:' + url;
  }
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) {
    return url;
  }"""

assert target in content, "target not found in store_scripts.py!"
content = content.replace(target, replacement, 1)

target2 = """  if (isIndianCatalogBook) {
    const pubFile = clean.replace(/^products\//, '').replace(/^\/+/, '').replace(/\s+/g, '-');
    return 'https://images.rajkamalprakashan.com/products/' + pubFile;
  }"""

replacement2 = """  if (isIndianCatalogBook) {
    // Intercept dead remote host (zero net::ERR_CONNECTION_CLOSED)
    if (typeof window !== 'undefined' && window.PODIUM_CDN_COVERS) {
      if (window.PODIUM_CDN_COVERS[clean]) return window.PODIUM_CDN_COVERS[clean];
      let cleanBase = clean.replace(/\\.[^.]+$/, '');
      if (window.PODIUM_CDN_COVERS[cleanBase]) return window.PODIUM_CDN_COVERS[cleanBase];
    }
    if (typeof getFallbackCover === 'function') {
      return getFallbackCover(clean, 'Indigo Books Edition');
    }
    return '';
  }"""

assert target2 in content, "target2 not found in store_scripts.py!"
content = content.replace(target2, replacement2, 1)

with open('store_scripts.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully patched store_scripts.py!")
