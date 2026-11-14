# -*- coding: utf-8 -*-
import os
import json

# 1. Read existing preview.html
with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Extract header and hero (up to </section>)
hero_end = text.find('</section>') + len('</section>')
head_and_hero = text[:hero_end]

# 3. Update the nav links in head_and_hero
import re
old_nav = re.search(r'<header class="sticky top-0.*?<\/header>', head_and_hero, re.DOTALL)

enhanced_navbar = """  <!-- A. Navigation Bar (h-20, Sticky at top-0, bg-[#FAF8F5]/95 backdrop-blur-md, z-50) -->
  <header class="sticky top-0 h-20 bg-[#FAF8F5]/95 backdrop-blur-md border-b border-amber-900/10 z-50 transition-shadow duration-200 shadow-sm" id="siteHeader">
    <div class="max-w-7xl mx-auto px-6 lg:px-8 h-full flex justify-between items-center">
      
      <!-- Left: Official INDIGO BOOKS Brand Logo -->
      <a href="#heroSection" class="flex items-center gap-3 cursor-pointer group select-none">
        <!-- Brand Emblem (SVG Icon: Symmetric Blue Geometric Knot Emblem #0066B3) -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 354 352" class="w-10 h-10 shrink-0 group-hover:scale-105 transition-transform" fill="#0066B3" fill-rule="evenodd" aria-label="Indigo Books Emblem">
          <path d="M 207 206 L 207 308 L 211 312 L 296 313 L 296 351 L 352 350 L 351 295 L 313 294 L 313 210 L 309 206 Z M 314 312 L 335 313 L 334 334 L 313 333 Z M 224 223 L 296 224 L 295 295 L 223 294 Z M 44 206 L 42 207 L 41 208 L 40 210 L 39 295 L 1 295 L 1 351 L 57 350 L 58 312 L 141 312 L 143 311 L 146 308 L 146 206 Z M 19 312 L 40 313 L 39 334 L 18 333 Z M 58 223 L 129 224 L 128 295 L 57 294 Z M 296 1 L 295 39 L 212 39 L 210 40 L 207 43 L 207 145 L 309 145 L 313 141 L 314 56 L 352 55 L 351 0 Z M 224 56 L 296 57 L 295 128 L 223 127 Z M 314 17 L 335 18 L 334 39 L 313 38 Z M 75 0 L 75 17 L 144 17 L 147 18 L 150 19 L 152 20 L 154 21 L 158 24 L 162 28 L 164 31 L 167 37 L 168 41 L 167 167 L 42 167 L 38 166 L 32 163 L 28 160 L 24 156 L 22 153 L 19 147 L 18 143 L 18 74 L 1 74 L 1 143 L 2 149 L 3 152 L 4 155 L 8 163 L 10 166 L 19 176 L 10 185 L 8 188 L 6 192 L 3 198 L 2 202 L 1 208 L 1 277 L 18 277 L 18 208 L 19 204 L 23 196 L 29 190 L 32 188 L 38 185 L 42 184 L 168 185 L 168 310 L 167 314 L 164 320 L 154 330 L 152 331 L 150 332 L 147 333 L 144 334 L 75 334 L 75 351 L 144 351 L 149 350 L 153 349 L 156 348 L 162 345 L 165 343 L 169 340 L 176 332 L 185 341 L 188 343 L 191 345 L 197 348 L 200 349 L 203 350 L 209 351 L 278 351 L 278 334 L 209 334 L 205 333 L 199 330 L 195 327 L 191 323 L 189 320 L 186 314 L 185 311 L 186 184 L 311 184 L 315 185 L 321 188 L 324 190 L 329 195 L 331 198 L 332 200 L 333 202 L 334 205 L 335 209 L 335 277 L 352 276 L 352 209 L 351 203 L 350 199 L 349 196 L 345 188 L 342 184 L 333 175 L 342 167 L 345 163 L 349 155 L 350 152 L 351 148 L 352 142 L 352 74 L 335 74 L 335 142 L 334 146 L 333 149 L 332 151 L 331 153 L 328 156 L 328 157 L 326 159 L 321 163 L 315 166 L 311 167 L 185 166 L 185 40 L 186 37 L 187 34 L 188 32 L 191 28 L 196 23 L 199 21 L 205 18 L 209 17 L 278 17 L 278 0 L 209 0 L 203 1 L 200 2 L 197 3 L 189 7 L 186 9 L 176 19 L 168 10 L 165 8 L 162 6 L 156 3 L 153 2 L 149 1 L 144 0 Z M 1 0 L 2 56 L 40 57 L 40 141 L 44 145 L 146 145 L 146 43 L 143 40 L 141 39 L 57 38 L 56 0 Z M 58 56 L 129 57 L 128 128 L 57 127 Z M 19 17 L 40 18 L 39 39 L 18 38 Z" />
        </svg>
        <!-- Store Name Wordmark -->
        <span class="font-serif text-xl lg:text-2xl tracking-[0.12em] font-normal text-black uppercase">
          INDIGO BOOKS
        </span>
      </a>

      <!-- Center Nav Links -->
      <nav class="hidden xl:flex items-center gap-6" id="SiteNav">
        <a href="#heroSection" class="text-sm font-semibold text-[#0A1128] py-2 border-b-2 border-[#D99B26] hover:text-[#D99B26] transition-all">
          Home
        </a>
        <a href="#shopAllSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Shop All (11,900+)
        </a>
        <a href="#bestsellersSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Best Sellers
        </a>
        <a href="#bentoGridSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Coming Soon
        </a>
        <a href="#bundlesSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Bundles
        </a>
        <a href="#bentoGridSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Pre-Order
        </a>
        <a href="#lawSection" class="text-sm font-medium text-slate-700 hover:text-[#D99B26] py-2 border-b-2 border-transparent hover:border-[#D99B26] transition-all">
          Law Books
        </a>
      </nav>

      <!-- Right Action Bar: Flag Badge, Search, Account, Cart Drawer Button, WhatsApp -->
      <div class="flex items-center gap-2.5 sm:gap-3">
        
        <!-- Indian Centric Badge -->
        <div class="hidden sm:flex items-center gap-2 bg-white border border-slate-200/90 rounded-full px-3 py-1 shadow-sm">
          <div class="w-6 h-6 rounded-full overflow-hidden border border-slate-300 shadow-inner flex flex-col justify-between shrink-0 relative">
            <div class="h-1/3 w-full bg-[#FF9933]"></div>
            <div class="h-1/3 w-full bg-white flex items-center justify-center relative">
              <svg class="w-2 h-2 text-[#000080]" viewBox="0 0 24 24" fill="currentColor">
                <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/>
                <circle cx="12" cy="12" r="3" fill="currentColor"/>
                <path d="M12 2v20M2 12h20M5 5l14 14M5 19L19 5" stroke="currentColor" stroke-width="1.5"/>
              </svg>
            </div>
            <div class="h-1/3 w-full bg-[#128807]"></div>
          </div>
          <div class="flex flex-col text-left">
            <span class="text-[10px] font-bold text-slate-900 leading-tight">Indian</span>
            <span class="text-[9px] font-medium text-slate-500 leading-tight">centric</span>
          </div>
        </div>

        <!-- Search Trigger Icon -->
        <button onclick="focusCatalogSearch()" class="p-2 text-slate-700 hover:text-[#0A1128] hover:bg-slate-100 rounded-full transition-colors" title="Quick Search Catalog">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        </button>

        <!-- User Account (Sign In) Button -->
        <button onclick="openLoginModal()" class="flex items-center gap-1.5 p-2 text-slate-700 hover:text-[#0A1128] hover:bg-slate-100 rounded-lg transition-colors text-xs font-semibold" title="Member Sign In">
          <svg class="w-5 h-5 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span class="hidden md:inline">Sign In</span>
        </button>

        <!-- Interactive Cart Drawer Button with Live Badge -->
        <button onclick="openCartDrawer()" class="relative flex items-center gap-2 bg-white hover:bg-amber-50 border border-slate-200 hover:border-amber-400 px-3 py-1.5 rounded-full transition-all shadow-sm group" title="Shopping Cart">
          <div class="relative">
            <svg class="w-5 h-5 text-slate-800 group-hover:text-[#D99B26] transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/>
            </svg>
            <span id="cartCountBadge" class="absolute -top-2 -right-2 bg-rose-600 text-white font-bold text-[10px] w-4 h-4 rounded-full flex items-center justify-center shadow">
              0
            </span>
          </div>
          <span id="cartTotalNav" class="text-xs font-bold text-[#0A1128] hidden lg:inline">
            ₹0.00
          </span>
        </button>

        <!-- WhatsApp Order Button (+91 8881122722) in Emerald Green -->
        <a href="https://wa.me/918881122722?text=Hello%20Indigo%20Books%20India%2C%20I%20would%20like%20to%20place%20an%20order." target="_blank" class="flex items-center gap-1.5 bg-[#10B981] hover:bg-[#059669] text-white px-3.5 py-2 rounded-md font-semibold text-xs transition-colors shadow-sm" title="Instant WhatsApp Order">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
          <span class="hidden sm:inline">WhatsApp</span>
        </a>

      </div>

    </div>
  </header>"""

head_and_hero = head_and_hero.replace(old_nav.group(0), enhanced_navbar)

print("Navbar successfully upgraded in head_and_hero.")
with open('head_and_hero.html', 'w', encoding='utf-8') as f:
    f.write(head_and_hero)

