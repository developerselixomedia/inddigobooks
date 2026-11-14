# -*- coding: utf-8 -*-
with open('store_scripts.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        <div class="catalog-thumb" onclick="handleBookAction('${book.id}', '${bookUrl}')" style="${bookUrl ? 'cursor: pointer;' : ''}">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${titleSafe}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${titleSafe}', '${authorSafe}');" />
        </div>"""

replacement = """        <div class="indigo-3d-book-stage" onclick="handleBookAction('${book.id}', '${bookUrl}')" style="margin-bottom: 12px; cursor: pointer;">
          <div class="indigo-3d-inside-page">
            <div style="font-size: 8.5px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.1em;">
              INDIGO ARCHIVE
            </div>
            <div style="font-family: 'Merriweather', serif; font-size: 11px; line-height: 1.35; color: #1E293B; font-weight: 700;">
              ${escapeHtml(book.title)}
            </div>
            <div style="font-size: 9.5px; color: #64748B;">
              By ${escapeHtml(book.author || book.vendor || '')}
            </div>
            <div style="font-size: 8.5px; color: #94A3B8; border-top: 1px dashed #CBD5E1; padding-top: 3px;">
              ${escapeHtml(book.pages || '250p')} &bull; ${escapeHtml(book.pub || 'Lokbharti')}
            </div>
          </div>
          <div class="indigo-3d-cover-leaf">
            <div class="indigo-3d-cover-front">
              <img referrerpolicy="no-referrer" src="${cover}" alt="${titleSafe}" loading="lazy" onerror="this.onerror=null; this.src=getFallbackCover('${titleSafe}', '${authorSafe}');" />
            </div>
            <div class="indigo-3d-cover-back">
              <div style="font-size: 9px; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 2px;">
                100% GENUINE
              </div>
              <div style="font-size: 10px; font-weight: 700; color: #FFFFFF; margin-bottom: 2px;">
                ${escapeHtml(book.pub || book.vendor || 'Authorized Copy')}
              </div>
              <div style="font-size: 9.5px; color: #CBD5E1;">
                ${escapeHtml(book.binding || 'Paperback')} &bull; ${priceFormatted}
              </div>
              <div style="font-size: 8.5px; color: #FCD34D; margin-top: 4px; border: 1px solid rgba(251,191,36,0.4); padding: 1px 4px; border-radius: 4px;">
                Click for Details &rarr;
              </div>
            </div>
          </div>
        </div>"""

if target in text:
    text = text.replace(target, replacement)
    with open('store_scripts.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Catalog card 3D stage updated successfully!")
else:
    print("Target not found in store_scripts.py!")

