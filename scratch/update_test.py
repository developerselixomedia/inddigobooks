with open('scratch/test_final_verification.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'body_overflow_after = driver.execute_script("return window.getComputedStyle(document.body).overflow;")\n    print(f"Body overflow after close: {body_overflow_after}")\n    assert "hidden" not in body_overflow_after, "Body overflow should be unlocked after close!"',
    'body_overflow_y_after = driver.execute_script("return window.getComputedStyle(document.body).overflowY;")\n    print(f"Body overflowY after close: {body_overflow_y_after}")\n    assert body_overflow_y_after in ["auto", "visible", ""], f"Body overflowY should be auto/visible after close, got {body_overflow_y_after}!"'
)

with open('scratch/test_final_verification.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated test script assertion!")
