with open('scratch/build_comprehensive_store_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

# in build_book_object, add 'rating' and 'publisher'
target = "'pub': publisher,"
replacement = "'pub': publisher,\n        'publisher': publisher,\n        'rating': '4.9 (12,840 verified readers)',"

code = code.replace(target, replacement)

with open('scratch/build_comprehensive_store_data.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_comprehensive_store_data.py with publisher and rating")

