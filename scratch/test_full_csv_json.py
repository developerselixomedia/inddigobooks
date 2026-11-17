import csv, json

books = []
seen = set()
with open('Updated_Catalog.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for r in reader:
        isbn = r.get('ISBN', '').strip()
        title = r.get('Title', '').strip()
        if not title: continue
        
        author = r.get('Author', '').strip()
        mrp_raw = r.get('MRP', '').replace('₹', '').replace(',', '').strip()
        try:
            mrp = float(mrp_raw)
        except:
            mrp = 299.0
        
        binding = r.get('Binding', '').strip() or 'Paperback'
        pages = r.get('Pages', '').strip() or '280p'
        pub = r.get('Publisher', '').strip() or 'Rajkamal Prakashan'
        subject = r.get('Subject', '').strip() or 'Classic Literature'
        img = r.get('Primary Image', '').strip()
        edition = r.get('Edition', '').strip() or 'Official Edition'
        lang = r.get('Language', '').strip() or 'Hindi'
        
        # Unique ID
        bid = f"book-{isbn}" if isbn else f"book-{len(books)}"
        
        books.append({
            "id": bid,
            "title": title,
            "author": author,
            "isbn": isbn,
            "price": f"₹{mrp:.2f}",
            "rawPrice": mrp,
            "binding": binding,
            "format": binding,
            "pub": pub,
            "publisher": pub,
            "pages": pages,
            "category": subject,
            "image": img,
            "cover": img,
            "coverUrl": img,
            "edition": edition,
            "lang": lang
        })

print(f"Total curated books from Updated_Catalog.csv: {len(books)}")
json_str = json.dumps(books, ensure_ascii=False)
print(f"Total JSON size: {len(json_str) / (1024*1024):.2f} MB")
