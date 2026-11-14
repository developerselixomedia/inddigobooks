import csv

with open('Updated_Catalog.csv', 'r', encoding='latin1') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

screenshot_titles = [
    'Halyog', 'Halant', 'Halaq Ka Darogha', 'Hadappa Sabhyata Aur Vaidik Sahitya',
    'Hadapada Appanna-Lingam', 'Haashiye Par Padi Duniya', 'Haadse',
    'Gypsy', 'Gyarahaveen-A ke Ladke', 'Gyandan', 'Gyan Aur Karm',
    'Guzare Lamhe', 'Guzara Hua Zamana', 'Godan', 'Chitralekha', 'Raag Darbari', 'Rashmirathi'
]

print("=== EXACT MATCHES FROM USER'S SCREENSHOT & BESTSELLERS ===")
for r in rows:
    for title in screenshot_titles:
        if r['Title'].strip().lower() == title.lower():
            print(f"{r['Title']} | {r['Author']} | {r['Publisher']} | {r['Binding']} | MRP: {r['MRP']} | ISBN: {r['ISBN']} | Img: {r['Primary Image']}")
            break

