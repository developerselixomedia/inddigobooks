with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    if (btnPb) {
      btnPb.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Paperback');
      };
    }
    if (btnHc) {
      btnHc.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Hardcover');
      };
    }
    applyFormat(activeInitialFmt);

    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Guaranteed Visible Cover)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#FAF7F0';
      coverLeafFront.style.backgroundImage = 'url(\"' + soloFallbackSvg + '\")';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.display = 'block';
      coverImg.style.opacity = '1';
      coverImg.style.width = '100%';
      coverImg.style.height = '100%';
      coverImg.style.objectFit = 'cover';
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.onerror = function() {
        this.onerror = null;
        if (window.getFallbackCoverSvg) {
          this.src = window.getFallbackCoverSvg(found.title, found.author);
        }
      };
      var targetCover = getCoverUrl(found.cover, found.title, found.author);
      coverImg.src = targetCover;
    }"""

replacement = """    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Guaranteed Visible Cover)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#FAF7F0';
      coverLeafFront.style.backgroundImage = 'url(\"' + soloFallbackSvg + '\")';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.display = 'block';
      coverImg.style.opacity = '1';
      coverImg.style.width = '100%';
      coverImg.style.height = '100%';
      coverImg.style.objectFit = 'cover';
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.onerror = function() {
        this.onerror = null;
        if (window.getFallbackCoverSvg) {
          this.src = window.getFallbackCoverSvg(found.title, found.author);
        }
      };
      var targetCover = getCoverUrl(found.cover, found.title, found.author);
      coverImg.src = targetCover;
    }

    if (btnPb) {
      btnPb.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Paperback');
      };
    }
    if (btnHc) {
      btnHc.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Hardcover');
      };
    }
    applyFormat(activeInitialFmt);"""

assert target in text, "Target block not found in editorial_video_theme.py"
text = text.replace(target, replacement, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully re-ordered coverImg setup before applyFormat!")
