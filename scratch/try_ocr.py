try:
    import pytesseract
    from PIL import Image
    text = pytesseract.image_to_string(Image.open('scratch/p1_hero.png'))
    print("OCR on p1_hero.png:")
    print(text)
except Exception as e:
    print("OCR not available:", e)
