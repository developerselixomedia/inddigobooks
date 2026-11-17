with open('editorial_video_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """      html += '<div class="editorial-search-view-all" onclick="window.performDedicatedSearch(document.getElementById(\\'editorialSearchInput\\').value)" style="padding:11px 16px;text-align:center;font-size:12.5px;font-weight:700;color:#E04F33;cursor:pointer;background:#FFF9F7;border-top:1px solid #FFE4DD;letter-spacing:0.02em;">View All Results for &ldquo;' + (searchInput.value || '').trim() + '&rdquo; &rarr;</div>';"""

replacement = """      html += '<div class="editorial-search-view-all" onclick="window.triggerDedicatedSearchAll()" style="padding:11px 16px;text-align:center;font-size:12.5px;font-weight:700;color:#E04F33;cursor:pointer;background:#FFF9F7;border-top:1px solid #FFE4DD;letter-spacing:0.02em;">View All Results for &ldquo;' + (searchInput.value || '').trim() + '&rdquo; &rarr;</div>';"""

if target in text:
    text = text.replace(target, replacement)
    print("Replaced onclick target")
else:
    print("Direct target not matched, searching...")
    # Find line containing editorial-search-view-all
    lines = text.splitlines()
    for i, l in enumerate(lines):
        if 'editorial-search-view-all' in l:
            lines[i] = replacement
            print(f"Replaced line {i+1}")
            break
    text = "\n".join(lines)

# Also ensure window.triggerDedicatedSearchAll is defined
if 'window.triggerDedicatedSearchAll =' not in text:
    def_code = """
  window.triggerDedicatedSearchAll = function() {
    var searchInput = document.getElementById('editorialSearchInput') || document.getElementById('results-search-input');
    var q = searchInput ? (searchInput.value || '').trim() : '';
    if (q && typeof window.performDedicatedSearch === 'function') {
      window.performDedicatedSearch(q);
    }
  };
"""
    # Insert right before setupPredictiveSearch
    text = text.replace('  function setupPredictiveSearch() {', def_code + '\n  function setupPredictiveSearch() {')
    print("Added window.triggerDedicatedSearchAll definition")

with open('editorial_video_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated editorial_video_theme.py!")
