# -*- coding: utf-8 -*-
"""
build_store_engine.py
Defines the authoritative visual components and SVGs for Indigo Books India.
"""

# Official Emblem SVG (40px x 40px, Royal Blue #0066B3)
INDIGO_EMBLEM_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 354 352" width="40" height="40" class="indigo-emblem-svg shrink-0" style="width: 40px !important; height: 40px !important; max-width: 40px !important; max-height: 40px !important; min-width: 40px !important; min-height: 40px !important; display: inline-block !important; vertical-align: middle !important; flex-shrink: 0 !important; object-fit: contain !important;" fill="#0066B3" fill-rule="evenodd" aria-hidden="true"><path d="M 207 206 L 207 308 L 211 312 L 296 313 L 296 351 L 352 350 L 351 295 L 313 294 L 313 210 L 309 206 Z M 314 312 L 335 313 L 334 334 L 313 333 Z M 224 223 L 296 224 L 295 295 L 223 294 Z M 44 206 L 42 207 L 41 208 L 40 210 L 39 295 L 1 295 L 1 351 L 57 350 L 58 312 L 141 312 L 143 311 L 146 308 L 146 206 Z M 19 312 L 40 313 L 39 334 L 18 333 Z M 58 223 L 129 224 L 128 295 L 57 294 Z M 296 1 L 295 39 L 212 39 L 210 40 L 207 43 L 207 145 L 309 145 L 313 141 L 314 56 L 352 55 L 351 0 Z M 224 56 L 296 57 L 295 128 L 223 127 Z M 314 17 L 335 18 L 334 39 L 313 38 Z M 75 0 L 75 17 L 144 17 L 147 18 L 150 19 L 152 20 L 154 21 L 158 24 L 162 28 L 164 31 L 167 37 L 168 41 L 167 167 L 42 167 L 38 166 L 32 163 L 28 160 L 24 156 L 22 153 L 19 147 L 18 143 L 18 74 L 1 74 L 1 143 L 2 149 L 3 152 L 4 155 L 8 163 L 10 166 L 19 176 L 10 185 L 8 188 L 6 192 L 3 198 L 2 202 L 1 208 L 1 277 L 18 277 L 18 208 L 19 204 L 23 196 L 29 190 L 32 188 L 38 185 L 42 184 L 168 185 L 168 310 L 167 314 L 164 320 L 154 330 L 152 331 L 150 332 L 147 333 L 144 334 L 75 334 L 75 351 L 144 351 L 149 350 L 153 349 L 156 348 L 162 345 L 165 343 L 169 340 L 176 332 L 185 341 L 188 343 L 191 345 L 197 348 L 200 349 L 203 350 L 209 351 L 278 351 L 278 334 L 209 334 L 205 333 L 199 330 L 195 327 L 191 323 L 189 320 L 186 314 L 185 311 L 186 184 L 311 184 L 315 185 L 321 188 L 324 190 L 329 195 L 331 198 L 332 200 L 333 202 L 334 205 L 335 209 L 335 277 L 352 276 L 352 209 L 351 203 L 350 199 L 349 196 L 345 188 L 342 184 L 333 175 L 342 167 L 345 163 L 349 155 L 350 152 L 351 148 L 352 142 L 352 74 L 335 74 L 335 142 L 334 146 L 333 149 L 332 151 L 331 153 L 328 156 L 328 157 L 326 159 L 321 163 L 315 166 L 311 167 L 185 166 L 185 40 L 186 37 L 187 34 L 188 32 L 191 28 L 196 23 L 199 21 L 205 18 L 209 17 L 278 17 L 278 0 L 209 0 L 203 1 L 200 2 L 197 3 L 189 7 L 186 9 L 176 19 L 168 10 L 165 8 L 162 6 L 156 3 L 153 2 L 149 1 L 144 0 Z M 1 0 L 2 56 L 40 57 L 40 141 L 44 145 L 146 145 L 146 43 L 143 40 L 141 39 L 57 38 L 56 0 Z M 58 56 L 129 57 L 128 128 L 57 127 Z M 19 17 L 40 18 L 39 39 L 18 38 Z" /></svg>'''

# Subtle Dark Geometric Circle Watermark (Top-Left of Hero)
HERO_TOPLEFT_WATERMARK_SVG = '''<svg viewBox="0 0 380 380" width="380" height="380" fill="none" stroke="#475569" stroke-width="1.2" opacity="0.25" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="190" cy="190" r="180" stroke-dasharray="4,6" />
  <circle cx="190" cy="190" r="150" />
  <circle cx="190" cy="190" r="115" />
  <circle cx="190" cy="190" r="75" stroke-dasharray="3,5" />
  <polygon points="190,40 340,190 190,340 40,190" />
  <polygon points="190,40 84,296 296,296" />
  <polygon points="190,340 84,84 296,84" />
  <line x1="190" y1="10" x2="190" y2="370" />
  <line x1="10" y1="190" x2="370" y2="190" />
  <line x1="60" y1="60" x2="320" y2="320" />
  <line x1="320" y1="60" x2="60" y2="320" />
</svg>'''

# Rotating Golden Geometric Rangoli Wheel SVG (440px x 440px, From Video)
def _generate_geometric_wheel_svg():
    spokes = []
    for deg in range(0, 360, 15):
        spokes.append(f'    <line x1="220" y1="20" x2="220" y2="420" transform="rotate({deg} 220 220)" />')
    spokes_str = '\n'.join(spokes)

    diamonds = []
    for deg in range(0, 360, 30):
        diamonds.append(f'    <polygon points="220,55 224,65 220,75 216,65" fill="#FBBF24" transform="rotate({deg} 220 220)" />')
        diamonds.append(f'    <polygon points="220,115 224,123 220,131 216,123" fill="#FDE68A" transform="rotate({deg + 15} 220 220)" />')
    diamonds_str = '\n'.join(diamonds)

    return f'''<svg viewBox="0 0 440 440" width="440" height="440" class="hero-wheel-svg" style="width: 440px; height: 440px; max-width: 440px; max-height: 440px; display: block;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="wheelGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.28"/>
      <stop offset="60%" stop-color="#D97706" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#B45309" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="220" cy="220" r="218" fill="url(#wheelGlow)" />
  <circle cx="220" cy="220" r="212" fill="none" stroke="#FBBF24" stroke-width="1.2" stroke-dasharray="4,6" opacity="0.6" />
  <circle cx="220" cy="220" r="198" fill="none" stroke="#F59E0B" stroke-width="1.8" opacity="0.75" />
  <circle cx="220" cy="220" r="182" fill="none" stroke="#FBBF24" stroke-width="1" stroke-dasharray="2,4" opacity="0.5" />
  
  <!-- 24 Radiating Spoke Lines -->
  <g stroke="#FBBF24" stroke-width="0.9" opacity="0.45">
{spokes_str}
  </g>

  <!-- Diamond Markers at Radial Intersections -->
  <g opacity="0.75">
{diamonds_str}
  </g>

  <!-- Concentric Inner Astrological Rings -->
  <circle cx="220" cy="220" r="145" fill="none" stroke="#FDE68A" stroke-width="1.4" opacity="0.75" />
  <circle cx="220" cy="220" r="115" fill="none" stroke="#F59E0B" stroke-width="1.6" stroke-dasharray="3,5" opacity="0.8" />
  <circle cx="220" cy="220" r="82" fill="none" stroke="#FBBF24" stroke-width="1.5" opacity="0.85" />
  <circle cx="220" cy="220" r="48" fill="rgba(245, 158, 11, 0.22)" stroke="#FDE68A" stroke-width="1.5" />
  <circle cx="220" cy="220" r="24" fill="#F59E0B" opacity="0.7" />
  <circle cx="220" cy="220" r="10" fill="#FFFBEB" />
</svg>'''

HERO_GEOMETRIC_RANGOLI_SVG = _generate_geometric_wheel_svg()
HERO_RANGOLI_SVG = HERO_GEOMETRIC_RANGOLI_SVG

# Hanging String Lights SVG
STRING_LIGHTS_SVG = '''<svg viewBox="0 0 450 160" width="450" height="160" style="position: absolute; right: 0; top: 0; pointer-events: none; z-index: 15;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="bulbGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFBEB" stop-opacity="1"/>
      <stop offset="35%" stop-color="#FCD34D" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#D97706" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#B45309" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- 3 Curved Catenary Wires -->
  <path d="M 0,0 Q 80,45 160,15 T 320,30 T 450,10" fill="none" stroke="#D99B26" stroke-width="1.2" opacity="0.65" />
  <path d="M 40,0 Q 140,75 240,30 T 420,50" fill="none" stroke="#B45309" stroke-width="1" opacity="0.5" />
  <path d="M 100,0 Q 220,95 360,40 T 450,70" fill="none" stroke="#D99B26" stroke-width="1" opacity="0.4" />
  <!-- Twinkling Bulbs Wire 1 -->
  <g class="string-bulb"><circle cx="45" cy="18" r="8" fill="url(#bulbGlow)"/><circle cx="45" cy="18" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.6s;"><circle cx="110" cy="35" r="9" fill="url(#bulbGlow)"/><circle cx="110" cy="35" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.2s;"><circle cx="175" cy="20" r="8" fill="url(#bulbGlow)"/><circle cx="175" cy="20" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.3s;"><circle cx="240" cy="26" r="9" fill="url(#bulbGlow)"/><circle cx="240" cy="26" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.5s;"><circle cx="310" cy="32" r="8" fill="url(#bulbGlow)"/><circle cx="310" cy="32" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.9s;"><circle cx="380" cy="22" r="8" fill="url(#bulbGlow)"/><circle cx="380" cy="22" r="2.5" fill="#FFF"/></g>
  <!-- Bulbs Wire 2 -->
  <g class="string-bulb" style="animation-delay: 0.4s;"><circle cx="90" cy="38" r="8" fill="url(#bulbGlow)"/><circle cx="90" cy="38" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.1s;"><circle cx="190" cy="56" r="10" fill="url(#bulbGlow)"/><circle cx="190" cy="56" r="3" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 0.7s;"><circle cx="290" cy="38" r="8" fill="url(#bulbGlow)"/><circle cx="290" cy="38" r="2.5" fill="#FFF"/></g>
  <g class="string-bulb" style="animation-delay: 1.4s;"><circle cx="370" cy="46" r="9" fill="url(#bulbGlow)"/><circle cx="370" cy="46" r="3" fill="#FFF"/></g>
</svg>'''

# 3 Terracotta Diyas Component SVG
HERO_DIYAS_SVG = '''<svg viewBox="0 0 260 100" width="260" height="100" style="position: absolute; right: 40px; bottom: 12px; z-index: 30; pointer-events: none;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <radialGradient id="flameInner" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="40%" stop-color="#FEF08A" stop-opacity="0.95"/>
      <stop offset="75%" stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="flameHalo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FDE047" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#EA580C" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#7C2D12" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="clayGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#C2410C"/>
      <stop offset="50%" stop-color="#9A3412"/>
      <stop offset="100%" stop-color="#431407"/>
    </linearGradient>
  </defs>
  
  <!-- Diya 1 (Left, Medium) -->
  <g transform="translate(15, 25)">
    <circle cx="30" cy="20" r="24" fill="url(#flameHalo)" class="diya-flame-halo" />
    <path d="M 30,8 C 22,18 24,28 30,34 C 36,28 38,18 30,8 Z" fill="url(#flameInner)" class="diya-flame" />
    <path d="M 6,32 C 12,48 48,48 54,32 C 50,38 10,38 6,32 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1"/>
    <ellipse cx="30" cy="32" rx="24" ry="4" fill="#7C2D12" opacity="0.9"/>
  </g>

  <!-- Diya 2 (Center, Large) -->
  <g transform="translate(95, 10)">
    <circle cx="35" cy="22" r="30" fill="url(#flameHalo)" class="diya-flame-halo" style="animation-delay: 0.35s;" />
    <path d="M 35,6 C 26,18 28,30 35,38 C 42,30 44,18 35,6 Z" fill="url(#flameInner)" class="diya-flame" style="animation-delay: 0.35s;" />
    <path d="M 7,36 C 14,54 56,54 63,36 C 58,43 12,43 7,36 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1.2"/>
    <ellipse cx="35" cy="36" rx="28" ry="5" fill="#7C2D12" opacity="0.9"/>
  </g>

  <!-- Diya 3 (Right, Small) -->
  <g transform="translate(185, 32)">
    <circle cx="25" cy="18" r="20" fill="url(#flameHalo)" class="diya-flame-halo" style="animation-delay: 0.7s;" />
    <path d="M 25,9 C 18,17 20,25 25,30 C 30,25 32,17 25,9 Z" fill="url(#flameInner)" class="diya-flame" style="animation-delay: 0.7s;" />
    <path d="M 5,28 C 10,42 40,42 45,28 C 41,33 9,33 5,28 Z" fill="url(#clayGrad)" stroke="#7C2D12" stroke-width="1"/>
    <ellipse cx="25" cy="28" rx="20" ry="3.5" fill="#7C2D12" opacity="0.9"/>
  </g>
</svg>'''

# Sweeping Solid Marigold-Gold Floor Curve SVG
HERO_FLOOR_CURVE_SVG = '''<svg viewBox="0 0 680 260" preserveAspectRatio="none" width="680" height="260" style="position: absolute; right: 0; bottom: 0; width: 680px; height: 260px; pointer-events: none; z-index: 12;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="marigoldFloorGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E5A93C" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#D99B26" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#B37418" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="floorShine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A" stop-opacity="0.65"/>
      <stop offset="15%" stop-color="#D99B26" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#78350F" stop-opacity="0.4"/>
    </linearGradient>
  </defs>
  <path d="M 0,260 C 180,260 270,90 680,60 L 680,260 Z" fill="url(#marigoldFloorGrad)" />
  <path d="M 0,260 C 180,260 270,90 680,60" fill="none" stroke="url(#floorShine)" stroke-width="4" opacity="0.9" />
</svg>'''

print("build_store_engine.py loaded: 24-petal Lotus Mandala SVG generated.")
