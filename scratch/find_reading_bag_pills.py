import glob

for fname in glob.glob('*.py') + glob.glob('assets/*.*') + glob.glob('sections/*.*') + glob.glob('snippets/*.*') + glob.glob('layout/*.*'):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    if 'btn-reading-bag' in text or 'Reading Bag (' in text:
        idx = 0
        while True:
            pos = text.find('btn-reading-bag', idx)
            if pos == -1:
                break
            print(f"{fname} at {pos}:")
            print(text[max(0, pos-40):pos+120].replace('\n', ' '))
            print('-'*40)
            idx = pos + 16
