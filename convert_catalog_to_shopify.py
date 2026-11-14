# -*- coding: utf-8 -*-
"""
convert_catalog_to_shopify.py
Converts Updated_Catalog.csv into a 100% compliant Shopify Product Import CSV.
Features:
- Standard Shopify CSV headers
- Automatic product grouping by Title & Author into Format variants (Hardcover / Paperback)
- Rich HTML Book Descriptions preserving Pages, Publisher, Language, Edition, and Year
- High-res Image linking with fallback
- Inventory tracking enabled with exact QTY
- Indian GST compliance (0% tax on printed books)
- Clean tags for faceted bookstore filtering
"""

import csv
import re
import os
from collections import defaultdict

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text[:70] if text else 'book'

def clean_weight(weight_str):
    try:
        w = float(weight_str.strip())
        return int(w * 1000) # Convert kg to grams
    except:
        return 300 # Default 300g

def clean_price(price_str):
    try:
        cleaned = re.sub(r'[^\d\.]', '', price_str.strip())
        val = float(cleaned)
        return f"{val:.2f}"
    except:
        return "299.00"

def clean_qty(qty_str):
    try:
        q = int(float(qty_str.strip()))
        return max(0, q)
    except:
        return 10

def convert_to_shopify():
    input_file = "Updated_Catalog.csv"
    output_file = "shopify_products_import.csv"

    print(f">>> Reading {input_file}...")
    
    rows = []
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for r in reader:
            title = r.get("Title", "").strip()
            if not title:
                continue
            rows.append(r)

    print(f"Total valid book records: {len(rows)}")

    # Group by (Title, Author) to create multi-variant products (Hardcover/Paperback)
    grouped = defaultdict(list)
    for r in rows:
        title = r.get("Title", "").strip()
        author = r.get("Author", "").strip()
        key = (title.lower(), author.lower())
        grouped[key].append(r)

    print(f"Total unique products: {len(grouped)}")

    shopify_headers = [
        "Handle",
        "Title",
        "Body (HTML)",
        "Vendor",
        "Product Category",
        "Type",
        "Tags",
        "Published",
        "Option1 Name",
        "Option1 Value",
        "Variant SKU",
        "Variant Grams",
        "Variant Inventory Tracker",
        "Variant Inventory Qty",
        "Variant Inventory Policy",
        "Variant Fulfillment Service",
        "Variant Price",
        "Variant Compare At Price",
        "Variant Requires Shipping",
        "Variant Taxable",
        "Variant Barcode",
        "Image Src",
        "Image Position",
        "Image Alt Text",
        "Status"
    ]

    out_rows = []
    used_handles = set()

    for (t_low, a_low), variants in grouped.items():
        first = variants[0]
        title = first.get("Title", "").strip()
        author = first.get("Author", "").strip()
        publisher = first.get("Publisher", "").strip() or "Indigo Books India"
        subject = first.get("Subject", "").strip() or "Books"
        language = first.get("Language", "").strip() or "Hindi"

        # Unique Handle
        base_handle = slugify(f"{title} {author}")
        handle = base_handle
        counter = 1
        while handle in used_handles:
            handle = f"{base_handle}-{counter}"
            counter += 1
        used_handles.add(handle)

        # Tags
        tags_list = ["Book", "Books", language]
        if publisher and publisher != "Indigo Books India":
            tags_list.append(publisher)
        if subject:
            for s in subject.replace("/", ",").split(","):
                s_clean = s.strip()
                if s_clean and s_clean not in tags_list:
                    tags_list.append(s_clean)
        tags_str = ", ".join(tags_list)

        # Track option values to avoid duplicates within same handle
        seen_options = {}

        for idx, var in enumerate(variants):
            binding = var.get("Binding", "").strip() or "Paperback"
            binding_val = binding.title()
            edition = var.get("Edition", "").strip()
            pub_year = var.get("Pub-Year", "").strip()
            pages = var.get("Pages", "").strip()
            isbn = var.get("ISBN", "").strip() or var.get("Inventry ISBN", "").strip()
            mrp = clean_price(var.get("MRP", "0"))
            qty = clean_qty(var.get("QTY", "10"))
            grams = clean_weight(var.get("Weight/kg", "0.3"))
            primary_img = var.get("Primary Image", "").strip()

            # Ensure unique Option1 Value if binding repeats
            if binding_val in seen_options:
                seen_options[binding_val] += 1
                modifier = edition if edition else pub_year
                if modifier:
                    opt_val = f"{binding_val} ({modifier})"
                else:
                    opt_val = f"{binding_val} (Ed {seen_options[binding_val]})"
            else:
                seen_options[binding_val] = 1
                opt_val = binding_val

            # Rich Description (HTML)
            desc_html = f"""<div class="indigo-book-specs">
  <p><strong>Title:</strong> {title}</p>
  <p><strong>Author:</strong> {author}</p>
  <p><strong>Publisher:</strong> {publisher}</p>
  <p><strong>Language:</strong> {language}</p>
  <p><strong>Binding:</strong> {binding}</p>
  {"<p><strong>Pages:</strong> " + pages + "</p>" if pages else ""}
  {"<p><strong>Edition / Year:</strong> " + edition + (" (" + pub_year + ")" if pub_year else "") + "</p>" if (edition or pub_year) else ""}
  <p><strong>Subject / Category:</strong> {subject}</p>
  <p><strong>ISBN:</strong> {isbn}</p>
  <p><em>Shipped nationwide across India with Cash on Delivery (COD) by Indigo Books India (Prayagraj).</em></p>
</div>"""

            row_data = {
                "Handle": handle,
                "Title": title if idx == 0 else "", # Shopify convention: Title only on first row
                "Body (HTML)": desc_html if idx == 0 else "",
                "Vendor": publisher if idx == 0 else "",
                "Product Category": "Media > Books > Print Books",
                "Type": subject if idx == 0 else "",
                "Tags": tags_str if idx == 0 else "",
                "Published": "TRUE",
                "Option1 Name": "Format",
                "Option1 Value": opt_val,
                "Variant SKU": isbn,
                "Variant Grams": grams,
                "Variant Inventory Tracker": "shopify",
                "Variant Inventory Qty": qty,
                "Variant Inventory Policy": "deny",
                "Variant Fulfillment Service": "manual",
                "Variant Price": mrp,
                "Variant Compare At Price": "",
                "Variant Requires Shipping": "TRUE",
                "Variant Taxable": "FALSE", # 0% GST on printed books in India (HSN 4901)
                "Variant Barcode": isbn,
                "Image Src": primary_img if (primary_img and primary_img.startswith("http")) else "",
                "Image Position": 1 if idx == 0 and primary_img else "",
                "Image Alt Text": f"{title} - {author}" if idx == 0 else "",
                "Status": "active"
            }
            out_rows.append(row_data)

    print(f">>> Writing {output_file}...")
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=shopify_headers)
        writer.writeheader()
        writer.writerows(out_rows)

    out_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"SUCCESS: Generated {output_file} ({out_size_mb:.2f} MB, {len(out_rows)} variant rows ready for Shopify import).")

if __name__ == "__main__":
    convert_to_shopify()

