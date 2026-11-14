import pandas as pd
import json
from test_builder_specs import get_book_record

handles = [
    'godan-premchand',
    'raag-darbari-shrilal-shukla',
    'chitralekha-bhagwaticharan-verma',
    'rashmirathi-dinkar-granthmala-ramdhari-singh-dinkar',
    'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
    'tarkash-javed-akhtar',
    'gypsy-ila-chandra-joshi',
    'aacharya-ramchandra-shukla-aur-hindi-aalochana-ramvilas-sharma',
    'bharatiya-bhasha-mein-high-court-ki-vakalat-anoop-baranwal-deshbandhu',
    'bharat-ka-samvidhan-sankshipt-parichay-subhash-kashyap',
    'samaan-nagrik-sanhita-chunautiya-aur-samadhan-anoop-baranwal',
    'nyayapalika-kasauti-par-kamlesh-jain-edi-ranjeet-verma',
    'tumhari-auqat-kya-hai-piyush-mishra',
    'jab-shahar-hamara-sota-hai-piyush-mishra',
    'mere-manch-ki-sargam-piyush-mishra',
    'arambh-hai-prachand-piyush-mishra',
    'tum-meri-jaan-ho-raziya-b-piyush-mishra',
    'aadha-gaon-rahi-masoom-raza',
    'mahabhoj-mannu-bhandari',
    'shekhar-ek-jeevani-vol-1-sachchidananda-hirananda-vatsyayan-ajneya',
    '1084ven-ki-maan-mahashweta-devi-tr-santwana-nigam',
    'gaban-premchand',
    'guzare-lamhe-ashok-yadav',
    '1857-awadh-ka-muktisangram-akhilesh-mishra-ed-vandana-mishra'
]

missing = []
for h in handles:
    rec = get_book_record(h)
    if not rec:
        missing.append(h)
    else:
        print(f"OK: {h} -> '{rec['title']}' by {rec['author']} | {rec['binding']} Rs.{rec['price']} | {rec['pages']} | ISBN: {rec['isbn']} | {len(rec['variants'])} variants")

if missing:
    print("MISSING:", missing)
else:
    print("\nALL 24 HANDLES RESOLVED PERFECTLY!")

