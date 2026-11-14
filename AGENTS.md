# Indigo Books India — Shopify Redesign Architecture & Automation Guide

Official website reference: **[https://www.indigobooksindia.com/](https://www.indigobooksindia.com/)**  
Headquarters: **Prayagraj, Uttar Pradesh, India**  
WhatsApp & Customer Support: **+91 8933063306** | Email: **info@indigobooks.com**  
Instagram: **[@indigobooksindia](https://www.instagram.com/indigobooksindia)** | Facebook: **[@indigobooks](https://www.facebook.com/indigobooks)**

---

## 1. Store Overview & Strategy

This Shopify theme is engineered to redesign **Indigo Books India** using Shopify's modern OS 2.0 Horizon framework. It is optimized for:
1. **2,000+ Book Inventory**: Instant predictive search, faceted category/genre filtering, and high-speed page loads.
2. **Meta Ads (Facebook & Instagram) Performance**: Automated `ViewContent`, `AddToCart`, `InitiateCheckout` tracking, high-intent landing sections, and a sticky mobile buy bar (85%+ of Indian book buyers browse on mobile).
3. **End-to-End WhatsApp Commerce**: Floating concierge widget, 1-click book orders with prefilled details, and cart drawer WhatsApp checkout for Cash on Delivery (COD) buyers.

---

## 2. Directory Structure

```text
indigo books/
├── assets/                             # 129 files (JS components, SVGs, CSS, TypeScript definitions)
│   ├── theme.css                       # Responsive bookstore typography, book shadows, grid
│   ├── theme.js                        # Cart drawer, predictive search, image switching
│   ├── whatsapp-commerce.js            # Dynamic WhatsApp cart message generator & lead tracking
│   ├── meta-ads-tracking.js            # Meta Pixel / CAPI event dispatchers
│   ├── variant-picker.js               # Paperback / Hardcover format picker
│   ├── volume-pricing.js               # Bulk tier discount calculator
│   └── (35 SVGs, base.css, etc.)
├── blocks/                             # 95 modular theme blocks
│   ├── _*.liquid                       # 48 internal Horizon component blocks
│   └── *.liquid                        # 47 customizable blocks (buy-buttons, accordion, etc.)
├── config/
│   ├── settings_schema.json            # Customizer controls (WhatsApp: 918933063306, Meta Pixel)
│   └── settings_data.json              # Active store settings
├── layout/
│   ├── theme.liquid                    # Base layout with OpenGraph, WhatsApp widget & Meta script
│   └── password.liquid                 # Pre-launch landing layout
├── locales/                            # 57 international and regional language files
│   ├── en.default.json                 # English default bookstore strings
│   └── (ar, es, fr, de, hi/ur, etc.)
├── sections/                           # 42 section files matching Horizon structure 1:1
│   ├── hero.liquid                     # "DISCOVER YOUR NEXT FAVOURITE BOOK"
│   ├── header.liquid                   # Predictive search for 2,000+ titles
│   ├── header-announcements.liquid     # Top bar: +91 8933063306 WhatsApp order
│   ├── cart-drawer-section.liquid      # Slide-out cart with "Order via WhatsApp"
│   ├── collection-links.liquid         # Rekhta, Sudha Murty, Ruskin Bond, Law, Bundles
│   ├── main-collection.liquid          # 2,000+ catalog page with faceted filtering
│   ├── product-information.liquid      # PDP with ISBN specs & mobile sticky buy bar
│   ├── quick-order-list.liquid         # Bulk school/library order sheet
│   └── (34 more sections)
├── snippets/                           # 148 snippets matching Horizon component architecture
│   ├── book-filter-facets.liquid       # Faceted filters for Genre, Author, Format, Price
│   ├── whatsapp-button.liquid          # Floating widget, PDP button, cart drawer button
│   ├── meta-pixel-events.liquid        # Meta Pixel automatic event tracking
│   ├── product-card.liquid             # Book card with 2:3 aspect ratio & WhatsApp button
│   ├── volume-pricing-info.liquid      # Bulk institutional discount tier table
│   └── (143 more styling & component snippets)
└── templates/                          # 13 JSON & Liquid templates
    ├── index.json                      # Homepage with live site categories
    ├── product.json                    # Book PDP
    ├── collection.json                 # Catalog & genre listing
    ├── cart.json                       # Shopping cart
    ├── search.json                     # Search results
    ├── gift_card.liquid                # Branded gift card
    └── (7 more templates)
```

---

## 3. Core Collections from Live Site (https://www.indigobooksindia.com/)

The theme is pre-configured with the actual core collections of Indigo Books India:
* **Best Sellers**: Top trending books in India.
* **Rekhta Publications**: Urdu poetry, Shayari, and literary classics (*Dozakh Nama, Thanda Ghost, Dhuaan, Ranjish hi Sahi*).
* **Sudha Murty**: Bestselling storytelling books (*Grandma's Bag of Stories, The Gopi Diaries, The Sage with Two Horns*).
* **Ruskin Bond**: Beloved Himalayan tales (*The Mystery Omnibus, School's Out!, Journeys to Remember*).
* **McGraw Hill & Textbooks**: Academic, engineering, management, and competitive examination books.
* **Law & Human Rights Books**: High-demand reference texts for advocates and law students.
* **Book Bundles & Box Sets**: Curated multi-book sets (e.g. *Best of Murakami Collection*).
* **Manga for Children & Graphic Novels**: Curated visual stories for younger readers.

---

## 4. WhatsApp Commerce & Automation Configuration

1. **WhatsApp Business Number**: Configured as `918933063306` (matches live site `+91 8933063306`).
2. **PDP 1-Click Order**:
   ```text
   Hello Indigo Books India! 📚
   I would like to order this book:
   *Book:* [Title]
   *Author:* [Author Name]
   *Price:* [Price]
   *Format:* [Paperback/Hardcover]
   *URL:* [Shopify URL]
   Please confirm availability and share COD / Payment details!
   ```
3. **Cart Drawer Order**: Tapping "Order Cart via WhatsApp" parses all cart items, line prices, and subtotal into an itemized WhatsApp message for instant confirmation.
4. **WhatsApp Lead Conversion**: Dispatches `WhatsAppLead` custom conversion events to Meta Pixel whenever a customer inquires or orders via WhatsApp.

---

## 5. Meta Ads Conversion Setup

1. **Meta Pixel & CAPI**: Add your Pixel ID in **Shopify Admin > Themes > Customize > Theme Settings > Meta Ads & Conversions API**.
2. **Dynamic Product Ads (DPA)**: All book cards and PDPs output semantic IDs and ISBN barcodes to sync directly with Meta Commerce Manager for retargeting campaigns.
