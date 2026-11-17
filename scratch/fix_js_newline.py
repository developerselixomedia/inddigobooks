with open('scratch/verify_all_fixes_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('console.log("\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---");', 'console.log("\\n--- TEST GROUP 4: Phone Number & PIN Input Validation ---");')

with open('scratch/verify_all_fixes_complete.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed console.log in verify_all_fixes_complete.js")
