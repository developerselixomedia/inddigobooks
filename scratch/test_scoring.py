import json

with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('window.MASTER_SEARCH_CATALOG =')
end = text.find(';\n    window.MODAL_METADATA_DATABASE', pos)
catalog = json.loads(text[pos + len('window.MASTER_SEARCH_CATALOG ='):end].strip())

POPULAR_HANDLES = [
  'godan-premchand', 'raag-darbari-shrilal-shukla', 'chitralekha-bhagwaticharan-verma',
  'rashmirathi-ramdhari-singh-dinkar', 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
  'tarkash-javed-akhtar', 'gypsy-ila-chandra-joshi', 'bharat-ka-samvidhan-dr-br-ambedkar',
  'aadha-gaon-rahi-masoom-raza', 'mahabhoj-mannu-bhandari', 'shekhar-ek-jeevani-agyeya',
  'gaban-premchand', 'nirmala-premchand', 'murakami-collection'
]

ICONIC_TITLES = [
  'godan', 'gaban', 'nirmala', 'sevasadan', 'karmabhoomi', 'rangbhoomi', 'mansarovar', 'idgah', 'kafan',
  'raag darbari', 'makaan', 'aadmi ka zahar', 'bishrampur ka sant',
  'rashmirathi', 'urvashi', 'kurukshetra', 'sanskriti ke chaar adhyay',
  'samvidhan', 'constitution', 'annihilation of caste', 'buddha and his dhamma',
  'tarkash', 'lava',
  'kuchh ishq', 'tumhari auqat', 'gagan damama',
  'aadha gaon', 'topi shukla', 'neem ka ped',
  'madhushala', 'madhubala', 'madhukalash',
  'chitralekha', 'thanda gosht', 'toba tek singh'
]

def score_query(query):
    q = query.lower().strip()
    scored = []
    for item in catalog:
        title = (item.get('title') or '').lower()
        author = (item.get('author') or '').lower()
        handle = str(item.get('handle') or item.get('id') or '').lower()
        isbn = str(item.get('isbn') or '').lower()
        
        has_author = q in author
        has_title = q in title
        has_isbn = q in isbn
        
        if not (has_author or has_title or has_isbn):
            continue
            
        score = 0
        if author == q:
            score += 400
        elif author.startswith(q):
            score += 350
        elif has_author:
            score += 250
            
        if title == q:
            score += 350
        elif title.startswith(q):
            if has_author:
                score += 60
            else:
                score += 200
        elif has_title:
            score += 90
            
        for ic in ICONIC_TITLES:
            if ic in title:
                score += 200
                break
        for ph in POPULAR_HANDLES:
            if ph in handle or handle in ph:
                score += 250
                break
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    seen = set()
    dedup = []
    for sc, it in scored:
        clean = (it.get('title') or '').lower().strip()
        if clean not in seen:
            seen.add(clean)
            dedup.append((sc, it))
        if len(dedup) >= 5:
            break
    print(f'Top results for "{query}":')
    for sc, it in dedup:
        print(f"  [{sc}] {it.get('title')} | Author: {it.get('author')}")

score_query('premchand')
score_query('shrilal shukla')
score_query('piyush mishra')
score_query('subhash kashyap')
