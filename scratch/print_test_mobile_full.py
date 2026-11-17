with open('scratch/test_mobile_full.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('verified_mobile_1_home')
print(text[max(0, idx-300):idx+300])
