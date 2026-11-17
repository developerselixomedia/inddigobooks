with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean renderArchiveGrid card
target_archive = """var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0; background-image: url(\'"\' + fallbackSvg + \'"\'); background-size: cover; background-position: center;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=\'"\' + fallbackSvg + \'"\';" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +"""

replacement_archive = """var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0; background-image: url(&quot;' + fallbackSvg + '&quot;); background-size: cover; background-position: center;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + fallbackSvg + '&quot;;" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +"""

assert target_archive in text, "target_archive not found"
text = text.replace(target_archive, replacement_archive, 1)

# 2. Clean renderShelfRow card
target_shelf = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#FAF7F0; background-image:url(\'"\' + shelfFallback + \'"\'); background-size:cover; background-position:center;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=\'"\' + shelfFallback + \'"\';" />' +
          '</div>' +
        '</div>' +"""

replacement_shelf = """var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#FAF7F0; background-image:url(&quot;' + shelfFallback + '&quot;); background-size:cover; background-position:center;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="this.onerror=null; this.src=&quot;' + shelfFallback + '&quot;;" />' +
          '</div>' +
        '</div>' +"""

assert target_shelf in text, "target_shelf not found"
text = text.replace(target_shelf, replacement_shelf, 1)

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully replaced quotes with &quot; in editorial_video_theme.py!")
