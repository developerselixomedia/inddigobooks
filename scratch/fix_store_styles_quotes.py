with open('store_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the incorrectly appended text after """
idx = text.rfind('"""')
if idx != -1:
    before = text[:idx]
    after = text[idx+3:].strip()
    # If there is CSS in after, move it inside before
    new_text = before + "\n" + after + '\n"""\n'
    with open('store_styles.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed store_styles.py triple quotes!")
